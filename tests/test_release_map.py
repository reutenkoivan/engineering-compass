import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
UPDATE = ROOT / "skills/engineering-compass-update"
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def release_rows():
    for line in (UPDATE / "release-map.md").read_text().splitlines():
        if line.startswith("| `"):
            release, previous, migrations = (cell.strip() for cell in line.split("|")[1:-1])
            yield release.strip("`"), previous.strip("`"), migrations


class ReleaseMapTest(unittest.TestCase):
    def test_published_map_is_an_ordered_chain_ending_at_the_plugin_version(self):
        previous = "—"
        seen = set()
        for release, predecessor, _ in release_rows():
            self.assertNotIn(release, seen)
            self.assertEqual(predecessor, previous, release)
            seen.add(release)
            previous = release
        plugin = json.loads((ROOT / "plugin.json").read_text())
        self.assertEqual(previous, plugin["version"])

    def test_map_selects_each_migration_once_with_prerequisites_in_order(self):
        seen = set()
        for release, _, migrations in release_rows():
            if migrations == "—":
                continue
            for reference in migrations.split(", "):
                link = LINK.fullmatch(reference)
                self.assertIsNotNone(link, (release, reference))
                label, relative = link.groups()
                path = (UPDATE / relative).resolve()
                self.assertEqual(path.parent, UPDATE / "migrations")
                self.assertEqual(label, path.name)
                self.assertRegex(path.name, r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
                self.assertNotIn(path.name, seen)
                contents = path.read_text()
                self.assertTrue(contents.startswith("```json\n"), path)
                header, closing, body = contents[len("```json\n"):].partition("\n```\n")
                self.assertTrue(closing and body.strip(), path)
                metadata = json.loads(header)
                self.assertEqual(metadata.keys(), {"depends_on"}, path)
                dependencies = metadata["depends_on"]
                self.assertIsInstance(dependencies, list)
                self.assertEqual(len(dependencies), len(set(dependencies)), path)
                self.assertLessEqual(set(dependencies), seen, path)
                seen.add(path.name)
        self.assertEqual(seen, {path.name for path in (UPDATE / "migrations").glob("*.md")})
