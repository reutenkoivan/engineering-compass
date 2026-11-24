# Repository setup

Start with the [adoption contract](../engineering-compass/adoption.md) and the
repository's effective local policy. Use the active installed version for the
entire Setup. When Update calls Setup, use the package it just verified.

## Select the work

- First adoption covers the foundation and all rule sets in the installed
  package. Read the installed principles and Context Map to find the owners.
- For a matching version, verify the selector, effective rules, local links,
  and applicable enforcement. Report a valid setup directly. Audit the
  affected scope before repairing an invalid integration.
- After a rollback, use the installed principles, Context Map, and affected
  rule owners to check the existing integration and local policy. Keep
  compatible local rules. Reconcile links and enforcement with the installed
  rules and apply the verified result.
- For an older or unversioned adoption, give the user the exact Update
  invocation for this installation. Update can use the audit and verification
  sections below to prepare its target integration.

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

Prepare the root entry from the
[adoption contract](../engineering-compass/adoption.md#root-entry) and the
affected local changes together. Verify that Codex can resolve the selected
global skill and version in the active environment. Present conflicts and changes
to local policy or enforcement for the user to decide. Apply compatible
integration changes within the request once their prerequisites are met.

Verify the candidate's root entry, links, rule coverage, local differences,
enforcement, and ordinary routing through the root entry and explicit skill
invocation. Before applying, recheck the installed version and affected
working files. Preserve unrelated edits. Apply the verified changes in the
calling working copy and read back its effective files and resolved rules.
If readback fails, restore this operation's changes while preserving user
edits. Record the installed version in the entry only as part of the verified
configuration. Report the version, applied changes, and any outstanding
decisions or environments still to verify.

## UI adoption checks

When adopting the Design systems workflow, verify the initial setup and an
incremental task that applies an existing rule and checks affected consumers.
When shared routing changes, also exercise an unrelated headless task and a
mixed UI/operation task. Confirm the catalog resolves under its skill owner,
local profile and behavior links resolve from repository policy, and both
entry routes preserve independently applicable rules. Keep repository-specific
values and evidence with their local owner.
