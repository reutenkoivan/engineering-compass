# Adoption and revision resolution

The root `AGENTS.md` owns adoption. Its Engineering Compass section instructs
ordinary repository work to use the exact installed skill name or links to the intended
repository-relative `SKILL.md`. A versioned entry records these fields.

```text
Engineering Compass release: <release-map ID>
Engineering Compass revision: <full upstream Git commit SHA>
Engineering Compass rules tree: <full repository Git tree OID>
```

The release identifies the starting row for Update. It comes from the
approved revision's `plugin.json` or the exact legacy commit in the release
map. The revision identifies the immutable content used for ordinary work.
The rules tree is present for a vendored copy. Its subtree is the directory
holding the linked `SKILL.md` in the adoption commit. Setup establishes the
source and verifies correspondence with the upstream revision. Update changes
the revision and, where applicable, the tree as part of an approved migration.

## Resolve before work

Use the committed adoption entry for the selected checkout. Read the effective
root instructions too. If a working copy edit changes the adoption fields or
the source selector, reconcile it before using the edited entry. Treat missing,
conflicting or unavailable versioned bindings as a blocker for dependent work.

- **Named skill from the Codex plugin.** Use `$engineering-compass:engineering-compass` and
  `~/.local/share/engineering-compass` as the Git checkout for rules. Plugin
  upgrades replace the installed copy. Keep local refs in the persistent
  checkout.
- **Named skill from a standalone installation.** Load `$engineering-compass` and use the intended installed
  Git checkout behind the discovered skill.
- **Vendored copy.** Use the repository-relative directory named by the entry.
  Its committed tree at `HEAD` must match the recorded tree before reading it.
  Read `SKILL.md` and this contract from that tree using Git.
  Treat the verified tree as the rule source even if files in the working copy
  have been edited. Reconcile conflicting edits before using the changed loader.

Both named routes read `refs/engineering-compass/approved/<revision>` from the
selected checkout. Use the commit from the adoption entry regardless of that
checkout's `HEAD`.

Use native Git commands to read the approved objects. For a named route,
verify that the approved ref resolves to the exact recorded commit. Use its
`skills/engineering-compass` subtree, or the rule paths at its root for an
older published package. For a vendored route, verify the committed tree at
the repository-relative package path against the recorded tree OID.

Locate each required file with `git ls-tree` in the selected tree, and read
its regular-file blob with `git cat-file blob`. Disable Git replacement
objects with `git --no-replace-objects`. Start at `principles.md` and follow
its Context Map. Resolve relative links against the same tree so their
contents come from the same revision.

These ordinary reads are local. If an object is unavailable, report its OID
and source so Setup or Update can restore it. Treat a loaded snapshot as the
authority for the session and verify changed adoption from a fresh context.

## Existing unversioned adoption

Keep a proven previous source for ordinary work until the operator approves a
transition. A named global route can use `refs/engineering-compass/legacy` in
the selected checkout when that ref retains the exact source the route used.
A confirmed legacy ref selects the same immutable lookup procedure.
A legacy repo-relative entry continues to use its established copy.
If the route or contents cannot be established, report the ambiguity and use
the explicit Setup or Update audit. The discovery checkout alone is evidence
of what is installed, so establish its relationship to the repository before
using a legacy ref.
