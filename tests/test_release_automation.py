import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".github/scripts"))
import release


class ReleaseAutomationTest(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory(prefix="compass-release-test-")
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name).resolve()
        self.checkout = self.root / "publisher"
        self.checkout.mkdir()
        self.remote = self.root / "origin.git"
        self.addCleanup(os.chdir, Path.cwd())
        os.chdir(self.checkout)
        self.git("init", "-qb", "main")
        self.git("init", "--bare", "-q", str(self.remote))
        self.git("remote", "add", "origin", str(self.remote))
        self.git("config", "user.name", "Release Test")
        self.git("config", "user.email", "test@example.invalid")
        env = patch.dict(os.environ, {
            "GITHUB_REPOSITORY": "example/engineering-compass",
            "GITHUB_SERVER_URL": "https://github.com",
            "GITHUB_EVENT_NAME": "push",
            "GITHUB_OUTPUT": str(self.root / "output"),
        })
        env.start()
        self.addCleanup(env.stop)
        self.write(release.CATALOG, (ROOT / release.CATALOG).read_text())
        self.write("README.md", "A source repository.\n")
        for name in ("engineering-compass", "engineering-compass-setup", "engineering-compass-update"):
            self.write(f"skills/{name}/SKILL.md", f"# {name}\n")
        self.write(f"{release.UPDATE}/migrations/initial.md", "Original published migration.\n")
        self.write(release.RELEASE_MAP, "| `0.1.0` | — | [initial.md](migrations/initial.md) |\n")
        self.manifest("0.1.0")
        self.base = self.commit("Initial release")
        self.git("tag", "-am", "First release", "v0.1.0")
        self.git("push", "-q", "origin", "main", "refs/tags/v0.1.0")

        self.published = {"v0.1.0"}
        self.created = []
        self.original_run = {}
        self.recovery_evidence = {}
        self.native_run = release.run
        provider = patch.multiple(release, github_api=self.github_api, run=self.run_command)
        provider.start()
        self.addCleanup(provider.stop)

    def git(self, *args):
        return subprocess.check_output(["git", *args], text=True, stderr=subprocess.PIPE).strip()

    def write(self, path, value):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value)

    def manifest(self, version):
        self.write("plugin.json", json.dumps({"name": "engineering-compass", "version": version}))

    def commit(self, message):
        self.git("add", "-A")
        self.git("commit", "-qm", message)
        return self.git("rev-parse", "HEAD")

    def next_release(self):
        self.manifest("0.2.0")
        with Path(release.RELEASE_MAP).open("a") as output:
            output.write("| `0.2.0` | `0.1.0` | — |\n")
        self.write("skills/engineering-compass/SKILL.md", "# Updated skill\n")
        return self.commit("Publish new package")

    def github_api(self, path, *, missing_ok=False):
        if path == "actions/runs/100":
            return self.original_run
        tag = path.rsplit("/", 1)[-1]
        if tag not in self.published and missing_ok:
            return None
        if tag not in self.published:
            self.fail(f"Unexpected lookup {path}")
        return {"tag_name": tag, "draft": False, "prerelease": False}

    def run_command(self, *args, **options):
        if args[:3] == ("gh", "release", "create"):
            self.git("ls-remote", "--exit-code", "origin", f"refs/tags/{args[3]}")
            self.created.append(args[3])
            self.published.add(args[3])
        elif args[:4] == ("gh", "run", "download", "100"):
            (Path(args[-1]) / "release-candidate.json").write_text(json.dumps(self.recovery_evidence))
        else:
            return self.native_run(*args, **options)

    def test_docs_only_does_not_produce_a_candidate(self):
        self.write("README.md", "Only the documentation changed.\n")
        self.assertIsNone(release.check_candidate(self.base, self.commit("Edit docs")))

    def test_push_records_evidence_only_for_the_exact_checked_out_commit(self):
        commit = self.next_release()
        event = self.root / "event.json"
        receipt = self.root / "receipt.json"
        push = {"ref": "refs/heads/main", "before": self.base, "after": commit}
        with patch.dict(os.environ, {"GITHUB_EVENT_PATH": str(event)}):
            event.write_text(json.dumps(push))
            release.verify(receipt)
            self.assertEqual(json.loads(receipt.read_text())["commit"], commit)
            push["after"] = self.base
            event.write_text(json.dumps(push))
            with self.assertRaisesRegex(ValueError, "exact push to main"):
                release.verify(receipt)

    def test_package_change_requires_a_version_and_append_only_map(self):
        self.write("skills/engineering-compass/SKILL.md", "# Unversioned change\n")
        with self.assertRaisesRegex(ValueError, "Bump plugin.json"):
            release.check_candidate(self.base, self.commit("Unversioned change"))
        self.next_release()
        self.write(f"{release.UPDATE}/migrations/initial.md", "Rewritten history.\n")
        with self.assertRaisesRegex(ValueError, "Published migration changed"):
            release.check_candidate(self.base, self.commit("Rewrite historical migration"))

    def test_tagged_package_keeps_its_public_installation_id(self):
        self.next_release()
        catalog = json.loads(Path(release.CATALOG).read_text())
        catalog["name"] = "renamed-marketplace"
        self.write(release.CATALOG, json.dumps(catalog))
        with self.assertRaisesRegex(ValueError, "Preserve the published marketplace and plugin ID"):
            release.check_candidate(self.base, self.commit("Rename marketplace"))

    def test_tag_only_recovery_publishes_once_and_preserves_the_channel(self):
        commit = self.next_release()
        candidate = release.check_candidate(self.base, commit)
        self.git("push", "-q", "origin", f"{commit}:refs/tags/v0.2.0")
        with self.assertRaisesRegex(ValueError, "confirmed published"):
            release.deliver("v0.2.0", "")
        release.publish(json.dumps(candidate._asdict()))
        release.publish(json.dumps(candidate._asdict()))
        self.assertEqual(self.created, ["v0.2.0"])
        self.assertIsNone(release.remote_commit(release.CHANNEL))

    def test_existing_version_tag_cannot_be_reassigned(self):
        commit = self.next_release()
        candidate = release.check_candidate(self.base, commit)
        self.git("push", "-q", "origin", f"{self.base}:refs/tags/v0.2.0")
        with self.assertRaisesRegex(ValueError, "already identifies a different commit"):
            release.publish(json.dumps(candidate._asdict()))
        self.assertEqual(release.remote_commit("refs/tags/v0.2.0"), self.base)
        self.assertEqual(self.created, [])

    def test_recovery_requires_evidence_of_the_exact_eligible_push(self):
        commit = self.next_release()
        self.original_run = {
            "path": release.PUBLICATION_WORKFLOW + "@main",
            "event": "push",
            "head_branch": "main",
            "repository": {"full_name": "example/engineering-compass"},
            "status": "completed",
            "head_sha": commit,
        }
        self.recovery_evidence = release.check_candidate(self.base, commit)._asdict()
        self.assertEqual(release.recover_candidate("100").commit, commit)
        self.write("README.md", "Different push, same version.\n")
        docs_commit = self.commit("Docs-only push")
        self.original_run["head_sha"] = docs_commit
        self.recovery_evidence.update(base=commit, commit=docs_commit)
        with self.assertRaisesRegex(ValueError, "original eligible main push"):
            release.recover_candidate("100")

    def test_release_branch_rollback_is_forward_only_and_manual(self):
        commit = self.next_release()
        release.publish(json.dumps(release.check_candidate(self.base, commit)._asdict()))
        with patch.dict(os.environ, {"GITHUB_EVENT_NAME": "workflow_dispatch"}):
            release.deliver("v0.1.0", "missing")
        initial_channel = release.remote_commit(release.CHANNEL)
        release.deliver("v0.2.0", "")
        next_channel = release.remote_commit(release.CHANNEL)
        self.assertEqual(self.git("rev-parse", f"{next_channel}^"), initial_channel)
        release.deliver("v0.1.0", "")
        self.assertEqual(release.remote_commit(release.CHANNEL), next_channel)
        with patch.dict(os.environ, {"GITHUB_EVENT_NAME": "workflow_dispatch"}):
            with self.assertRaisesRegex(ValueError, "Expected release head"):
                release.deliver("v0.1.0", initial_channel)
            release.deliver("v0.1.0", next_channel)
        rollback = release.remote_commit(release.CHANNEL)
        self.assertEqual(self.git("rev-parse", f"{rollback}^"), next_channel)
        self.assertEqual(self.git("rev-parse", f"{rollback}:skills"), self.git("rev-parse", f"{self.base}:skills"))
        catalog = json.loads(self.git("show", f"{rollback}:{release.CATALOG}"))
        self.assertEqual(catalog["plugins"][0]["source"], {
            "source": "url", "url": "https://github.com/example/engineering-compass.git", "ref": "v0.1.0",
        })
        self.assertEqual(release.remote_commit("refs/tags/v0.1.0"), self.base)
        self.assertEqual(release.remote_commit("refs/tags/v0.2.0"), commit)
