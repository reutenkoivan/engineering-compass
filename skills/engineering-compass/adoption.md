# Repository adoption

The working copy of the root `AGENTS.md` owns the integration. Its Engineering
Compass section names the global skill and records
`Engineering Compass release: <version>`. This is the version for which the
repository has been configured.

## Identify the active installation

Resolve the named global skill in Codex. Setup and Update use the global
package that supplies the invoked skill. A Codex plugin exposes
`$engineering-compass:engineering-compass`. A user-installed Git bundle
exposes `$engineering-compass`. Read the version from `plugin.json` in the
package root above `skills/`. For a marketplace installation, confirm the
installed, enabled package in `codex plugin list --json` and read the
installed package's files. Keep the marker and the rules in the same package.
If the selector or version is missing, ambiguous, or inconsistent, report
what must be resolved in the installation before dependent work.

## Compare versions before applying rules

Use the working root entry and compare its version with the installed version
numerically as `major.minor.patch`. An invalid or conflicting version entry
requires repair before choosing a branch.

| Repository state | Action |
| --- | --- |
| Versions match | Use the installed `principles.md` and `context-map.md`. Resolve their links in the same package. An explicit Setup verifies or repairs the integration. |
| Repository version is older | Show both versions, stop dependent work, and ask the user to invoke Update in this repository. |
| Repository version is newer | Show both versions and run the [Setup procedure](../engineering-compass-setup/setup.md) from the installed package. Resume dependent work after Setup verifies the integration. |
| Existing adoption has no version | Ask the user to invoke Update to audit the previous integration and establish its first recorded version. |

Apply this comparison to ordinary work and to Setup. An explicit Update may
run with mismatched or missing repository version. After it synchronizes the
installation, use its migration procedure to reconcile the repository.
Repositories without an adoption follow their local instructions. An explicit
request to adopt Engineering Compass starts Setup.

## Root entry

Use the selector and skill names for the actual installation. The following
form uses the Codex plugin. For a standalone bundle, use
`$engineering-compass`, `$engineering-compass-setup`, and
`$engineering-compass-update`.

```markdown
## Engineering Compass

Engineering Compass release: <version>

This entry owns version selection and format for Compass, Setup, and Update,
including explicit calls to the installed skills.
Before planning or doing repository work, resolve
$engineering-compass:engineering-compass and read the version in its package's
plugin.json. If the versions match, apply principles.md and context-map.md
from that installed skill. If this repository is older, show both versions,
stop, and ask me to run $engineering-compass:engineering-compass-update here.
If this repository is newer, show both versions and run
$engineering-compass:engineering-compass-setup here. Run only the local-policy
audit and integration checks from the installed Setup's setup.md against the
installed rules, then write the verified version.

An explicit Update may run before the versions match. If the installed
Update still uses Git revision fields, refresh the release marketplace with
`codex plugin marketplace upgrade engineering-compass` or the clean Git
checkout on release with `git pull --ff-only`. Read Update from the refreshed
package. If it still expects revision fields, compare versions again. Use
its migration records for forward changes and the Setup checks above for
integration. Use this entry's format.
```

The comparison and refresh instructions in the entry also apply to packages
that predate the version-based workflow. Keep repository-specific policy
reachable from root in every version.
