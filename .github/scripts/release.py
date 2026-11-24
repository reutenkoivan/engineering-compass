"""Validate, publish, and deliver Engineering Compass releases."""

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from typing import NamedTuple


CATALOG = ".agents/plugins/marketplace.json"
PLUGIN_NAME = "engineering-compass"
UPDATE = "skills/engineering-compass-update"
RELEASE_MAP = f"{UPDATE}/release-map.md"
PACKAGE = ("skills", "plugin.json", CATALOG)
CHANNEL = "refs/heads/release"
PUBLICATION_WORKFLOW = ".github/workflows/plugin-release.yml"
RECEIPT = "release-candidate"
VERSION = r"(?:0|[1-9][0-9]*)(?:\.(?:0|[1-9][0-9]*)){2}"
OBJECT_ID = r"(?:[a-f0-9]{40}|[a-f0-9]{64})"
MIGRATION = re.compile(r"\[([^\]]+)\]\((migrations/[a-z0-9-]+\.md)\)")


class ReleaseRow(NamedTuple):
    version: str
    previous: str
    migrations: str


class Candidate(NamedTuple):
    base: str
    commit: str
    version: str
    previous: str


def release_rows(contents):
    return [
        ReleaseRow(*(cell.strip().strip("`") for cell in line.split("|")[1:-1]))
        for line in contents.splitlines()
        if line.startswith("| `")
    ]


def run(*args, check=True, data=None):
    result = subprocess.run(args, input=data, text=True, capture_output=True, check=False)
    if check and result.returncode:
        raise ValueError(f"{args[0]} {args[1]} failed: {result.stderr.strip()}")
    return result


def git(*args, data=None):
    return run("git", "--no-replace-objects", *args, data=data).stdout.strip()


def read_at(commit, path):
    return git("show", f"{commit}:{path}")


def version_key(version):
    if not isinstance(version, str) or not re.fullmatch(VERSION, version):
        raise ValueError(f"Expected a release version (MAJOR.MINOR.PATCH), found {version!r}")
    return tuple(map(int, version.split(".")))


def tag_version(tag):
    if not re.fullmatch(f"v{VERSION}", tag):
        raise ValueError(f"Expected a version tag, found {tag!r}")
    return tag[1:]


def check_candidate(base, commit):
    for revision in (base, commit):
        if not re.fullmatch(OBJECT_ID, revision) or git("rev-parse", f"{revision}^{{commit}}") != revision:
            raise ValueError(f"Expected an available commit, found {revision!r}")
    git("merge-base", "--is-ancestor", base, commit)
    if not git("diff", "--name-only", base, commit, "--", *PACKAGE):
        return None

    previous = json.loads(read_at(base, "plugin.json"))["version"]
    version = json.loads(read_at(commit, "plugin.json"))["version"]
    if version_key(version) <= version_key(previous):
        raise ValueError(f"The package changed. Bump plugin.json above {previous}, found {version}.")

    old_rows = release_rows(read_at(base, RELEASE_MAP))
    rows = release_rows(read_at(commit, RELEASE_MAP))
    if not old_rows or old_rows[-1].version != previous or rows[:-1] != old_rows:
        raise ValueError("Preserve the previous release map and append exactly one row.")
    if rows[-1][:2] != (version, previous):
        raise ValueError(f"The new release map row must bind {version} to predecessor {previous}.")
    for row in old_rows:
        for _, path in MIGRATION.findall(row.migrations):
            if git("diff", "--name-only", base, commit, "--", f"{UPDATE}/{path}"):
                raise ValueError(f"Published migration changed: {path}. Append a follow-up instead.")
    tagged_catalog(commit)
    return Candidate(base, commit, version, previous)


def github_api(path, *, missing_ok=False):
    result = run("gh", "api", "--include", f"repos/{os.environ['GITHUB_REPOSITORY']}/{path}", check=False)
    headers, _, body = result.stdout.partition("\n\n")
    if missing_ok and headers.splitlines() and re.match(r"HTTP/\S+ 404\b", headers.splitlines()[0]):
        return None
    if result.returncode:
        raise ValueError(f"GitHub API {path} failed: {result.stderr.strip()}")
    return json.loads(body)


def recover_candidate(run_id):
    if not re.fullmatch(r"[0-9]+", run_id):
        raise ValueError("Provide the original publication workflow run ID.")
    original = github_api(f"actions/runs/{run_id}")
    if (original["path"].split("@", 1)[0], original["event"], original["head_branch"],
            original["repository"]["full_name"], original["status"]) != (
            PUBLICATION_WORKFLOW, "push", "main", os.environ["GITHUB_REPOSITORY"], "completed"):
        raise ValueError("Recovery requires a completed publication workflow from a push to this main branch.")
    with tempfile.TemporaryDirectory() as directory:
        run("gh", "run", "download", run_id, "--name", RECEIPT, "--dir", directory)
        evidence = Candidate(**json.loads((Path(directory) / f"{RECEIPT}.json").read_text()))
    if evidence.commit != original["head_sha"] or check_candidate(evidence.base, evidence.commit) != evidence:
        raise ValueError("Recovery evidence does not match the original eligible main push.")
    git("merge-base", "--is-ancestor", evidence.commit, "HEAD")
    return evidence


def verify(receipt):
    event_name = os.environ["GITHUB_EVENT_NAME"]
    event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
    head = git("rev-parse", "HEAD")
    if event_name == "workflow_dispatch":
        candidate = recover_candidate(event["inputs"]["original_run_id"])
    elif event_name == "push":
        if event["ref"] != "refs/heads/main" or head != event["after"]:
            raise ValueError("Publication must validate the exact push to main.")
        candidate = check_candidate(event["before"], head)
    else:
        candidate = check_candidate(event["pull_request"]["base"]["sha"], head)
    record = json.dumps(candidate._asdict()) if candidate else ""
    with Path(os.environ["GITHUB_OUTPUT"]).open("a") as output:
        print(f"candidate={record}", file=output)
    if candidate and event_name == "push":
        receipt.write_text(record + "\n")


def remote_commit(ref):
    result = run("git", "ls-remote", "--exit-code", "origin", ref, check=False)
    if result.returncode == 2:
        return None
    if result.returncode:
        raise ValueError(f"Cannot read {ref}: {result.stderr.strip()}")
    git("fetch", "--no-tags", "origin", ref)
    return git("rev-parse", "FETCH_HEAD^{commit}")


def published_commit(tag):
    version = tag_version(tag)
    release = github_api(f"releases/tags/{tag}", missing_ok=True)
    if not release or release["tag_name"] != tag or release["draft"] or release["prerelease"]:
        raise ValueError(f"{tag} needs a confirmed published GitHub Release.")
    commit = remote_commit(f"refs/tags/{tag}")
    if not commit or json.loads(read_at(commit, "plugin.json"))["version"] != version:
        raise ValueError(f"Published tag {tag} does not identify its declared package version.")
    if release_rows(read_at(commit, RELEASE_MAP))[-1].version != version:
        raise ValueError(f"Published tag {tag} does not match its release map.")
    return commit


def publish(candidate):
    evidence = Candidate(**json.loads(candidate))
    if check_candidate(evidence.base, evidence.commit) != evidence:
        raise ValueError("Publication requires a verified package change.")
    version, previous, commit = evidence.version, evidence.previous, evidence.commit
    tag = f"v{version}"
    prior = published_commit(f"v{previous}")
    if git("diff", "--name-only", prior, evidence.base, "--", *PACKAGE):
        raise ValueError(f"The main baseline disagrees with published predecessor v{previous}.")
    git("merge-base", "--is-ancestor", prior, evidence.base)

    ref = f"refs/tags/{tag}"
    existing = remote_commit(ref)
    if existing and existing != commit:
        raise ValueError(f"{tag} already identifies a different commit.")
    release = github_api(f"releases/tags/{tag}", missing_ok=True)
    if release is None:
        if existing is None:
            git("push", "origin", f"{commit}:{ref}")
        row = release_rows(read_at(commit, RELEASE_MAP))[-1]
        url = repository_url()
        links = [f"- [{name}]({url}/blob/{tag}/{UPDATE}/{path})" for name, path in MIGRATION.findall(row.migrations)]
        notes = ["--notes", "Migration instructions\n\n" + "\n".join(links)] if links else []
        run("gh", "release", "create", tag, "--verify-tag", "--generate-notes", "--title", tag,
            "--notes-start-tag", f"v{previous}", *notes)
    if published_commit(tag) != commit:
        raise ValueError(f"{tag} does not resolve to the verified push after publication.")
    with Path(os.environ["GITHUB_OUTPUT"]).open("a") as output:
        print(f"tag={tag}", file=output)
    print(f"Published {tag} from {commit}.")


def repository_url():
    return f"{os.environ['GITHUB_SERVER_URL']}/{os.environ['GITHUB_REPOSITORY']}"


def tagged_catalog(commit):
    catalog = json.loads(read_at(commit, CATALOG))
    name = json.loads(read_at(commit, "plugin.json"))["name"]
    if catalog["name"] != PLUGIN_NAME or name != PLUGIN_NAME:
        raise ValueError(f"Preserve the published marketplace and plugin ID {PLUGIN_NAME}@{PLUGIN_NAME}.")
    if (len(catalog["plugins"]) != 1 or catalog["plugins"][0]["name"] != PLUGIN_NAME
            or catalog["plugins"][0]["source"] != {"source": "local", "path": "./"}):
        raise ValueError("The tagged marketplace must expose the root package as its single plugin.")
    for name in (PLUGIN_NAME, f"{PLUGIN_NAME}-setup", f"{PLUGIN_NAME}-update"):
        path = f"skills/{name}/SKILL.md"
        entry = git("ls-tree", commit, "--", path)
        if not entry.startswith(("100644 blob ", "100755 blob ")):
            raise ValueError(f"The package needs a regular file at {path}.")
    return catalog


def channel_tree(commit, tag):
    catalog = tagged_catalog(commit)
    catalog["plugins"][0]["source"] = {"source": "url", "url": f"{repository_url()}.git", "ref": tag}
    blob = git("hash-object", "-w", "--stdin", data=json.dumps(catalog, indent=2) + "\n")
    plugins = git("mktree", data=f"100644 blob {blob}\tmarketplace.json\n")
    agents = git("mktree", data=f"040000 tree {plugins}\tplugins\n")
    package = git("ls-tree", commit, "--", "skills", "plugin.json")
    return git("mktree", data=f"040000 tree {agents}\t.agents\n{package}\n")


def deliver(tag, expected):
    version = tag_version(tag)
    commit = published_commit(tag)
    current = remote_commit(CHANNEL)
    manual = os.environ["GITHUB_EVENT_NAME"] == "workflow_dispatch"
    if manual and expected != (current or "missing"):
        raise ValueError(f"Expected release head {expected!r}; found {current or 'missing'}. Review and retry.")
    if current is None and not manual:
        raise ValueError("Bootstrap release from an existing published tag with the manual workflow.")

    desired_tree = channel_tree(commit, tag)
    if current is not None:
        active = json.loads(read_at(current, "plugin.json"))["version"]
        if active == version:
            if git("rev-parse", f"{current}^{{tree}}") != desired_tree:
                raise ValueError(f"release already claims {tag} but its delivered contents disagree.")
            print(f"release already delivers {tag}.")
            return
        if not manual and version_key(active) > version_key(version):
            print(f"release already delivers newer v{active}. Skipped {tag}.")
            return

    delivery = git("-c", "user.name=github-actions[bot]",
                   "-c", "user.email=41898282+github-actions[bot]@users.noreply.github.com",
                   "commit-tree", desired_tree, "-p", current or commit, "-m", f"Deliver {tag}")
    git("push", "origin", f"{delivery}:{CHANNEL}")
    if remote_commit(CHANNEL) != delivery:
        raise ValueError("The release branch changed before readback. Inspect its current state.")
    print(f"release delivers {tag} at {delivery}.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("verify").add_argument("receipt", type=Path)
    commands.add_parser("publish").add_argument("candidate")
    delivery = commands.add_parser("deliver")
    delivery.add_argument("tag")
    delivery.add_argument("expected")
    args = parser.parse_args()
    if args.command == "verify":
        verify(args.receipt)
    elif args.command == "publish":
        publish(args.candidate)
    else:
        deliver(args.tag, args.expected)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, IndexError, TypeError) as error:
        sys.exit(str(error))
