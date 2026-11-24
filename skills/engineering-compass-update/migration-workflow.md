# Repository migrations

## Capture the current release before updating

Start with the selected repository's committed adoption entry and active
local policy. Read the base skill's [adoption contract](../engineering-compass/adoption.md).
Read `Engineering Compass release` as the baseline version and verify the
effective rule binding against that version's published tag. Record the
installed bundle version separately when relevant to compatibility.

If the repository has no approved version or its provenance cannot be
established, retain its active rules and offer Setup's audit and explicit
first versioned adoption. Conflicting versioned metadata requires repair.

## Fetch the fixed target

Use a staged Git checkout outside skill discovery and the consumer worktree.
Fetch `refs/heads/release` from
`https://github.com/reutenkoivan/engineering-compass.git` and retain the fetched
snapshot locally before additional fetches. Read its
`.agents/plugins/marketplace.json` to find the `engineering-compass` entry.
Require its Git URL to name the publisher and its ref to be an exact
`vMAJOR.MINOR.PATCH` tag. Fetch that tag and confirm the GitHub Release for it
is published as a regular release. Check that the tag version agrees with
`plugin.json` and the final row of
`skills/engineering-compass-update/release-map.md` at that tag. Verify that
the frozen channel's `skills/` and `plugin.json` match the tag. Report an
unavailable channel, tag, or Release as
a blocker and keep the current rules in use.

Keep the verified tag fixed for the request. Use the compatible installed
Setup and Update procedures with the rules, map and migration records from
that tag. This applies when the channel selects `v0.1.0`, whose own Setup and
Update use an earlier target selection procedure.

For a migration, verify the baseline by its published version too. A matching
target version completes the check once the existing binding and route are
verified. An older target has no forward transition and leaves the approved
version in force. A newer version with an empty migration list still requires
review and approval of the change to the adopted version.

## Select instructions from the release map

1. Use the versioned rows beginning at `0.1.0`. Start at the target row and
   follow versioned predecessor entries
   backwards until reaching the captured baseline. Stop for a missing or
   repeated release, an ambiguous predecessor, or a path that ends before
   the baseline. Reverse the selected rows, excluding the baseline row.
2. Take the migration files named by those rows, in release order. Include
   releases with empty migration lists in the version path. Read the listed
   files in the target. Use their stable IDs (filenames including `.md`) and
   `depends_on` lists to validate order and find prerequisites in earlier rows. A missing file,
   duplicate ID, unresolved edge or cycle blocks the plan.
3. Build the repository-specific graph from the written applicability,
   preconditions, actions and proof. A prerequisite from an earlier release
   or a skipped node needs evidence of its required condition or an approved
   valid equivalent before a dependent step can proceed. Use historical
   records for prerequisite evidence where applicable. Offer a delivery
   migration as a separate action for the installation when its applicability
   is met.

## Plan and obtain decisions

Use compatible Setup with the target rules to audit each affected rule, repository
owner, local difference, and executable projection.

Show a graph from the approved to the target version with the applicable
nodes, prerequisites, verified equivalents, reasons for skips, and blockers.
For each decision, show the affected files, intended changes, consequences,
and verification. Scope approval to the repository, exact versions,
affected inputs, effects, and proof. Group related decisions and reuse exact
approvals. Agree on external effects before running commands that cause them.
If a decision leaves a required condition unsatisfied, keep the current
adoption in force and explain the blocked dependents.

## Prepare and verify the transition

Apply approved edits in an isolated Git worktree, keeping the original
checkout as the live source. Before applying or integrating, recheck the
expected repository base and affected inputs. Report overlapping edits or
changed conditions and renew only the decisions affected by the change.

Include the updated root adoption release and revision, affected policy,
enforcement, and vendored files in one coherent candidate commit. For a global route,
retain the verified target in the Git checkout selected by the adoption
contract before using its pin. Fetch the exact frozen commit from the staged
local checkout when the store needs the object. Create
`refs/engineering-compass/approved/<revision>` only for the reviewed commit
and fail on a conflicting existing binding.
For a vendored route, compare the target package's paths, modes, and contents
with the candidate tree, then use the candidate subtree OID in `AGENTS.md`.

Run the migration and Setup checks against that commit, including the exact
rules and relative resources resolved from the candidate. A conflict, decline,
or failed check leaves the existing checkout and effective rules in force.
On a repeat run, identify the existing candidate, recheck approvals and
postconditions, and continue only from the first unverified step. Confirm an
uncertain effect from the repository before attempting it again.

Report a verified candidate as ready with its baseline and target versions.
Activation occurs when the operator
selects that verified checkout for work or integrates it through the
repository's agreed Git workflow. Reverify affected proof if integration
changes the candidate. Confirm activation through a fresh ordinary Codex
request in the selected context and report the approved version and rules it read.
