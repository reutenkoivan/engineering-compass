# Repository setup

Establish current adoption from the root entry and local policy. Initial
adoption covers the foundation and all rule sets together. For an existing
integration or a change to rules, routing or local differences, identify the
affected scope and audit the consequences.

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
repository-wide. For a repository copy, link to its `SKILL.md` using a
repository-relative path. For a user-installed copy, name `$engineering-compass`
in the entry and verify that skill discovery resolves the intended copy in
each environment that relies on the entry. Keep local policy and approved
differences reachable from root. The Context Map owns the conditions for
reading each rule set.

Prepare the root entry and affected local changes together, including decisions
about conflicts, retained local contracts and executable projections.
Apply the authorized transition once the replacement routes exist. Keep the
repository adoption entry in root `AGENTS.md`. Local surface routes link to the
applicable rule and source owners.

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
