# Repository migrations

## Capture the current release before updating

Start with the selected repository's committed adoption entry and active
local policy. Read the base skill's [adoption contract](../engineering-compass/adoption.md).
Resolve and inspect the rules actually in force. Capture the repository, rule
source, adopted release and full revision, and whether the entry is versioned.
Record the installed bundle version separately from its discovered manifest or
the verified checkout commit for a legacy installation. Put this evidence in the
update review before refreshing the bundle or changing repository state.
If a refresh requires a new Codex chat, carry the same evidence into it.
Select migrations from the repository's captured release.

For an older entry without a release field, establish the actual rule source.
For a verified upstream revision, read its `plugin.json` when present. For an
earlier published source, use its exact full commit from the release map.
A matching installed `HEAD` alone does not establish repository adoption.

## Fetch the fixed target

Stage a checkout outside skill discovery and the consumer worktree. Use the
latest stable GitHub Release from `reutenkoivan/engineering-compass`. Fetch
its exact `refs/tags/v<version>` and resolve the tag to a commit. Verify that
the version agrees with both that commit's `plugin.json` and its
`skills/engineering-compass-update/release-map.md`. For a versioned baseline,
fetch its exact publisher tag too and verify that it resolves to the recorded
baseline commit. The pre-versioned rows identify their published commits
directly. Keep the target commit and release fixed for the run. Read Setup,
the rules and migration records from that same target. Report a missing
published release or failed target fetch as unavailable. If the baseline tag
cannot be verified, block map selection pending provenance.

If the legacy baseline cannot be proven, report what can and cannot be
established about the old rules. Use the exact target's full Setup audit and
present explicit adoption of the target and reconciliation of local policy
for approval. Describe any remaining unknown historical effects. If the
baseline is known but the target's map has no forward route from it, report
the missing route and obtain a separate decision before replanning.

Matching release IDs must identify the same published revision. Report a
conflicting binding and establish provenance before using the map. An exact
match completes the update check when the versioned entry and current routes
also verify. If that revision still uses an unversioned entry
or obsolete setup path, apply the review in
[Record the approved revision](migrations/record-approved-revision.md).
A newer target with no applicable migrations still requires a reviewed and
verified revision change.

## Select instructions from the release map

1. Start at the target row in the frozen map. Follow predecessor entries
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
   valid equivalent before a dependent step can proceed.

## Plan and obtain decisions

Use the target's Setup procedure to audit each affected rule, repository
owner, local difference, and executable projection.

Show a graph from the current to the target revision with the applicable
nodes, prerequisites, verified equivalents, reasons for skips, and blockers.
For each decision, show the affected files, intended changes, consequences,
and verification. Scope approval to the repository, exact revisions,
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

Report a verified candidate as ready. Activation occurs when the operator
selects that verified checkout for work or integrates it through the
repository's agreed Git workflow. Reverify affected proof if integration
changes the candidate. Confirm activation through a fresh ordinary Codex
request in the selected context and report which commit and rules it read.
