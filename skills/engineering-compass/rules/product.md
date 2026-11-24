# Product

## Request process

**Invariant:** process semantic work through business planning, business review,
architecture planning, architecture review, cross-cutting review, implementation,
and change review. The first five stages are planning; the last two are
implementation. Scale artifacts to consequences and uncertainty; a concise
message with owner links can suffice. No template, document count or file layout
is required. Ordinary mechanical work with established unchanged meaning stays
outside this process.

A plan-only request ends at its requested reviewed/approved planning result.
An implementation request proceeds after the required approvals without another
generic permission to switch vectors. Read-only investigation can prepare a
decision. An experiment involving code first has an explicit question, bounded
scope, verification method, conditions for using its result and needed approval.
An approved plan can cover an experiment and implementation under explicit
conditions. Prototype success does not establish a supported contract.

### Business planning

**Invariant:** establish shared understanding with the operator: problem, goal,
boundaries, consumers, concepts, inputs and prerequisites, constraints and
material assumptions, conditions/actions/results/failures, new/changed/preserved
guarantees, acceptance criteria and transition. Reuse agreed facts; silence is
not agreement to new meaning. Distinguish unknown intent, unknown mechanism and
missing proof. Investigate available facts before asking for genuinely missing
intent; do not use passing code/tests to accept new semantics or an accepted
document to prove implementation.

Choose sources by their responsibility and resolve conflicting meanings
explicitly. No particular CONTEXT, ADR, issue, lifecycle file or tracker is
required by this set.

### Business review

**Invariant:** a separate AI reviews the business basis for meaning, completeness
and contradictory outcomes. Apply the review-handling rules below and obtain
operator approval of the current reviewed basis before dependent architecture
planning.

### Architecture planning

**Invariant:** explain current → target → transition. Assign each material
guarantee an owner/mechanism and planned sufficient proof. Identify responsibility
boundaries, interfaces, state/resources and lifecycle, significant alternatives
and consequences. Distinguish dependency direction, data flow and execution
prerequisites. Make implementation, migration and verification prerequisites,
conditional branches and unknowns explicit. Include the affected supported
contracts below; avoid a second approval for an exactly approved decision.

### Architecture review

**Invariant:** a separate AI checks architectural coherence, boundaries,
contracts, ownership, lifecycle, dependencies, alternatives and evidence limits.
Apply review handling and obtain operator approval of the reviewed architecture.

### Cross-cutting review

**Invariant:** a separate AI follows business paths through the architecture,
including negative and early terminal outcomes, side effects and behavior
introduced by architectural choices. Verify coverage both from business
requirements to mechanisms/proof and from architecture to agreed business intent.
Apply review handling and obtain operator approval of the combined reviewed basis
before implementation. AI agreement alone satisfies none of these approvals.

### Implementation

**Invariant:** implement against an identifiable approved basis and maintain
cumulative bidirectional trace: planned guarantees/mechanisms/proof → actual
changes and actual changes → approved scope. Use proportionate existing artifacts,
not a mandatory trace registry. Distinguish defect correction, an approved
conditional branch and a change that invalidates an agreed decision. Current
candidate evidence must correspond to the actual change; rerun invalidated proof.
Reconcile causal consumers, documentation and evidence through their applicable
owners.

### Change review

**Invariant:** review the actual candidate, including uncommitted, untracked and
deleted sources, against applicable standards and approved intent/plan. Execute
sufficient current proof and reconcile causal owners. Report implemented,
verified, pending and external outcomes truthfully. No mandatory commit, PR,
publication or fourth generic operator approval follows from change review.

## Review handling and invalidation

**Invariant:** each reviewer is separate from the proposal author. Give it the
current proposal, known uncertainties, and access to canonical facts
and applicable requirements. Apply the same classification to reviews;
full conversation history is not automatically needed. Pre-implementation review
uses planned versus actual evidence honestly and requires no hidden product
implementation. If a separate reviewer is unavailable, prepare a transferable
review packet, identify the outstanding step and continue independent authorized
work; self-review does not satisfy it.

**Default:** distinguish requirement violations, questions/missing evidence and
optional improvements. Each material finding identifies the decision,
requirement/fact, consequence and basis. Preferences do not turn Defaults into
Invariants. **Invariant:** address every material finding by correction, evidence
or reasoned disagreement; give the operator the current basis and unresolved
material disagreements. An invariant violation must be fixed, disproved or
resolved through an explicit change to its owner. Missing material proof stays
visible. **Contextual choice:** the operator may choose between valid alternatives
with known consequences without requiring AI consensus.

**Invariant:** material invalidation returns to the earliest affected stage and
repeats the affected reviews and approvals before dependent work. This includes
changed problem/scope, responsibility, significant dependency, contract,
guarantee, lifecycle, material consequence or evidence basis. Reuse sufficient
unchanged decisions, approval and context. A wording correction or private detail
within approved guarantees does not restart the process merely because a file
changed; an old verdict does not approve newly invalidated meaning.

## Supported contracts

**Invariant:** identify consumers and the boundary providing a supported
capability. Publication and human users do not define it: a private workspace
package can support other packages. Local exports are not automatically public;
actual external usage and accidental exposure need investigation. Distinguish
current, concretely planned and illustrative consumers. Planned capability may
have zero current consumers; exposure still needs justification.

**Default:** provide a sufficient focused main entry for actual or planned common
uses. Independent supported capabilities may have their own entries; no package
root, entry depth or all-leaf re-export quota follows.

**Invariant:** before dependent implementation, present the exact affected
access/interface, capability scope, inputs/results, invariants, order, failures
and lifecycle where relevant. Show current and target forms, direction,
consumers, transition and proof. Opening a supported boundary explains why
private implementation is insufficient. Assess independent contract dimensions:
imports/access/exports; TypeScript inference/declarations; runtime inputs,
results and behavior; wire/persisted values; canonical bytes/identity; and
generated/delivered artifacts. Relevant dimensions require sufficient evidence,
not a compulsory per-edit table or declaration-test suite.

For migrations identify usage/data, accessible changes, unknown consequences and
transition conditions. No local reference is not proof of no external consumer.
An open audience uses supported patterns and explicit verification limits rather
than an invented exhaustive census. Move accessible consumers to the target and
remove superseded forms. For work outside access, identify action, owner, order
and confirmation. Data migration can replace an old contract; removing
compatibility does not permit data loss or changing already issued meanings.

Completion requires accepted guarantees, actual accessible surface,
implementation, causal consumers and sufficient evidence to agree. Distinguish
local completion, a prepared external plan and confirmed full transition; expose
material unknowns and outstanding prerequisites.
