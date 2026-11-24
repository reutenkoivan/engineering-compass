```json
{"depends_on": []}
```

# Use the active global version

## Applicability

Apply when an existing repository moves to the version-based global
integration introduced in `0.3.0`. A repository already using the
[version-based entry](../../engineering-compass/adoption.md#root-entry)
satisfies this migration once its installed version and integration match.

## Start from an older installation

Capture available evidence of an unversioned integration before replacing
its rule source.

If the installed Update still prepares a separate candidate or selects a
published tag, refresh the global installation once before invoking the new
Update. If the installation does not yet follow `release`, use the
[delivery migration](migrate-to-release-channel.md) first. For a marketplace
already tracking `release`, use
`codex plugin marketplace upgrade engineering-compass`. For a clean Git
checkout tracking `release`, use `git pull --ff-only` in that checkout.

In a fresh Codex chat in the repository, invoke the newly installed Update
skill to complete this migration. Use
`$engineering-compass:engineering-compass-update` for a plugin and
`$engineering-compass-update` for a standalone installation. Check the
actual installed version if the new procedure is not available.
Invoke the global Update explicitly when the root entry still selects a
repository-local copy. The old selector identifies the rules to audit.

## Change the repository integration

Capture the current version, source selector, and effective local policy.
Audit the old route and affected policy and enforcement against the active
installed rules. Resolve material uncertainty with the user. Preserve
compatible project-specific policy and its links. An unversioned integration
uses the same audit to establish its first version.

Use the current Setup verification procedure to replace the former adoption
entry with the global skill selector and the installed release number. Retire
the old revision and rules-tree fields from that entry. Locate any remaining
uses of old project rule paths before changing their links. Preserve local
files, Git refs and shared stores during this migration.

The current version-based entry satisfies the former snapshot and version
recording conditions of [record-approved-revision.md](record-approved-revision.md).
Use that record to audit older policy and routes. Its old pinned rule source
and parallel-version readback are superseded by the active-version comparison.
Installation changes and cleanup from
[migrate-to-release-channel.md](migrate-to-release-channel.md) remain subject
to that record's applicability and approvals.

## Verify and recover

Read back the working `AGENTS.md`, installed version and repository policy.
Check ordinary Compass routing and the affected links and enforcement.
With a second connected repository still recording the preceding version,
verify that it requests Update at its next Compass run.

After a rollback to a package with older instructions, use the comparison
and rollback directions in the new root entry. They select the actual
installed rules for Setup's policy audit. Verify the reconfigured repository
before writing the lower version. When returning from such a package to the
current workflow, use the refresh procedure above.
