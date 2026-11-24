# Update an adopted repository

## Capture the starting state

Read the working root `AGENTS.md`, its Engineering Compass entry, and the
local policy it routes to. Record the configured version when present.
For an unversioned adoption or old source selector, capture the effective
old rules and their source before replacing the installation if they can be
established. Keep existing repository files in use during preparation.

Resolve the global package that supplies Update using the
[adoption contract](../engineering-compass/adoption.md). A legacy
repository-local selector identifies the previous rules for the audit.
Read Setup's
[audit and verification procedure](../engineering-compass-setup/setup.md)
before replacing the package, so it remains available for a rollback to a
package with older instructions.

## Synchronize and select the work

[Refresh and verify the global installation](bundle-refresh.md) from one
snapshot of `release`. Compare the repository version with the version
installed by that refresh.

| Repository state | Action |
| --- | --- |
| Versions match | Verify or repair the integration with Setup. |
| Repository version is newer | Show both versions and run the Setup audit for the installed rules. Keep compatible local policy and verify the reconfigured integration. Use the already loaded Setup procedure when the installed package predates the version-based integration. |
| Repository version is older | Read the target package's release map and relevant migration files. Prepare the changes for the installed version. |
| Version is absent in an existing adoption | Audit the previous integration and the installed rules. Use the target's applicable migration records for a first versioned adoption. Present unclear provenance when it affects how to reconcile local policy. |

## Select migration instructions

Use the release map bundled with the verified target. Follow its versioned
predecessor rows from the target back to the recorded version. Read the
selected rows in forward order, starting after the recorded version. For an
unversioned adoption, use the versioned rows through the target and evaluate
their applicability against the captured integration.

Read the selected migration files from that one installed package. Use their
stable filenames and `depends_on` lists to verify prerequisites. If a record
was satisfied earlier, identify the evidence in the repository. Apply the
current target's instructions when a later record supersedes a former
condition. Report missing rows, unavailable records, unresolved prerequisites,
or inconsistent version metadata before changing the repository.

Use the files to identify the changes needed for the installed version.
Audit affected local policy, links, enforcement and skill selectors using
Setup. Include compatible integration changes in the candidate. Present
conflicts and proposed changes to local policy or enforcement for the user's
decision.

## Apply and verify in the calling repository

Prepare the changes and the target version together. Verify and apply them
using [Setup's root configuration and verification](../engineering-compass-setup/setup.md#root-configuration-and-verification).
Check that the active installation and affected working files still match the
reviewed inputs before applying. Publish the working entry's version as part
of the verified result. Other repositories will check their versions the next
time Compass runs there.

If the migration stops, retain the refreshed global installation and the
previous repository configuration. Report the installed version, the
configured version, and the remaining decision or failed check. On a repeat
Update, confirm the current state and reapply only unsatisfied changes.
