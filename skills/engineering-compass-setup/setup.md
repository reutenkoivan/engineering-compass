# Repository setup

Establish current adoption from the root entry and local policy. Initial
adoption covers the foundation and all rule sets together. For an existing
integration or a change to rules, routing or local differences, identify the
affected scope and audit the consequences.

## Select the rule revision

Use the [adoption contract](../engineering-compass/adoption.md) to resolve
existing adoptions. For a first adoption through the Codex plugin, use Update's
[published target procedure](../engineering-compass-update/migration-workflow.md#fetch-the-fixed-target)
to select and verify the publisher release and its exact revision. Use Setup
and the rules from that revision for the audit, even if the plugin cache
changes. For an older published snapshot, use its proven full commit from
the [release map](../engineering-compass-update/release-map.md) as the release ID.

When applying approved plugin-backed setup, create the persistent checkout
identified in the adoption contract from the reviewed full checkout if it is
absent. Reuse the existing Engineering Compass checkout at that path when
present. If the reviewed commit is missing there, fetch it from the reviewed
checkout. Verify the commit and retain it as described below.

## Resolve local rules

Audit the adopted rules against active instructions, nearby canonical documents,
and their executable projections. Compare meaning, scope, normative level,
rationale, conditions, and exceptions rather than matching words. Distinguish duplicate
norms, complementary local contracts, and real conflicts. A checker, command,
schema, or required reader contract is not redundant merely because the skill
states the policy it enforces. Remove only a fully covered norm; preserve unique
parts of mixed passages and local rationale at their owner. Investigate uncertain
replacement coverage before deleting anything.

For each conflict present the current and proposed effective rule, their owners
and scopes, the concrete gain from replacing the current rule with the skill's
rule, the transition cost and consequences, and the available decisions:

- Adopt the skill rule and reconcile the local owner and causal projections.
- Retain an explicit local difference: identify the exact skill rule, scope,
  effective requirement, reason, and canonical local owner reachable from root
  instructions. Keep only the difference, not a second copy of the whole domain.

A justified departure from a Default differs from changing an Invariant. Do not
claim an invariant violation is compliance. Resolve incompatible prerequisites
as part of the same decision. Reuse already supplied exact approval. Use an
existing suitable local owner; no exception registry or extra config file is
required. Keep portable rule text separate from repository-specific differences.

## First adoption

The first-adoption audit scope includes every rule set and detailed rule owner.
Include both complete Tooling audits, covering command policies, the task
dependency graph, and every direct dependency. Each proposed edge needs a concrete reason. Obtain operator
approval for effective graph changes before edits. An integration update
for an already adopted Tooling set follows the affected scope.

## Root configuration and verification

Prepare a reviewable root `AGENTS.md` entry that adopts the whole skill
repository-wide and directs Codex to apply Compass automatically before
planning or starting repository work. Use the fields and source selector in
the base skill's [adoption contract](../engineering-compass/adoption.md).
Keep local policy and approved differences reachable from root.

Identify the exact upstream commit under review and verify the rule snapshot
against it. For a global route, retain the verified commit in the Git checkout
selected by the adoption contract with `git update-ref` at
`refs/engineering-compass/approved/<revision>`. An existing ref must already
point to that commit. Check availability in every environment relying on it.
For a vendored route, use the published rule package as one tree in the
adoption commit. Compare paths, modes and contents to upstream and record the
local subtree OID. Direct Codex to read the base entry and loader from that
committed tree. When vendoring Setup too, preserve its package and the base
package as canonical siblings, so that Setup can read the adoption contract.
Resolve a custom legacy copy through the local policy audit before recording
a published revision.

For a first-refresh audit requested with a staged target checkout, use the
Setup procedure and reviewed Compass package from that exact target. Keep the
existing adoption and discovery route active during preparation. If the
previous source cannot be identified, report that limit and obtain explicit
approval to adopt the audited target and its reconciled local policy.

Prepare the root entry and affected local changes together, including decisions
about conflicts, retained local contracts and executable projections.
Apply the authorized transition once the replacement routes exist. Include
the entry and affected policy and package files in one adoption commit.
Prepare the commit for the repository's normal approval flow. Where there is
no `HEAD`, this is part of the repository's initial commit. Create or select
that commit when authorized, and report activation as pending until the
approved commit is selected for ordinary work. Keep the adoption entry in
root `AGENTS.md` and link local surfaces to their rule and source owners.

Read back effective root and local instructions. Verify links, rule coverage,
local differences, required enforcement, and ordinary routing through both
the root entry and explicit skill invocation. Report prepared, applied and
verified configuration distinctly, with any agreed later migration and its owner.

## UI adoption checks

When adopting the Design systems workflow, verify the initial setup and an
incremental task that applies an existing rule and checks affected consumers.
When shared routing changes, also exercise an unrelated headless task and a
mixed UI/operation task. Confirm the catalog resolves under its skill owner,
local profile and behavior links resolve from repository policy, and both
entry routes preserve independently applicable rules. Keep repository-specific
values and evidence with their local owner.
