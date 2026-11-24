# Behavior modeling

**Contract specification** means stating what the responsible owner accepts,
guarantees, and constrains. It is an activity, not a mandatory new document.
Exact schemas, interfaces, and configurations keep their canonical owners.
A Scenario models behavioral paths; a Check identifies a guarantee in documented
context; a test supplies executable evidence. Use authored Markdown and IDs;
there is no required SOM, JSON projection, generated evidence index, or registry.

## Planning: the behavior model

**Invariant:** one Scenario has one independent external Stimulus and a finite
acyclic tree of behaviorally meaningful States and Transitions. Preserve the
main successful route and early terminal outcomes. Include the Scenario boundary,
outcome perspective, Initial State, primary successful Terminal State, stimulus
initiator/event/symbolic inputs, prerequisites and references to external
guarantees, state facts, transition events/guards/targets, and terminal outcomes.

**Default:** one complete Scenario lives at its narrowest stable behavioral
owner in `docs/scenarios/<scenario-id>.md`. Composition can be that owner, including
the repository root. A root catalog may link to local definitions. Test splitting
does not require mirrored MD splitting. A State or Check ID alone is not a reason
for another file; justify a departure on the concrete large Scenario before
splitting its documentation.

**Invariant:** each category has one canonical definition in the repository.
Multiple references or test files do not create more definitions. A Scenario root
is a navigation category, not a runtime State. Initial State begins its behavioral
tree; prerequisite references to other Scenarios are not parent edges.

### Markdown grammar

**Default:** use these definitions; names following the ID are human-readable:

```markdown
# Scenario [[scenario-id]] — Name
## Scenario boundary
- **Outcome perspective:** ...
- **Initial state:** [[scenario-id/initial-state]].
- **Primary terminal:** [[scenario-id/success-state]].
## Stimulus
- **Initiator:** ...
- **Trigger:** ...
- **Inputs:** ...
## Preconditions
- A required fact, or a reference to its owner.
## State [[scenario-id/initial-state]] — Name
- **Holds:** ...
- **On:** an event
  - **Primary:**
    - **When:** a condition
    - **To:** [[scenario-id/success-state]].
### Check [[scenario-id/initial-state#check-id]] — Name
- **Guarantee:** the guarantee or its precise canonical reference.
- **Paths:**
  - **Entry:** [[scenario-id/initial-state]].
    **Target:** [[scenario-id/success-state]].
## State [[scenario-id/success-state]] — Name
- **Holds:** ...
- **Kind:** successful.
- **Outcome:** ...
```

This is a syntax illustration, not a complete product specification. Fill only
concepts that exist; omit empty inputs, conditions, or lists. `On completion`
represents a transition without a separate event. A root-owned Check uses
`## Check [[scenario-id#check-id]] — Name`; a State-owned Check uses the third-level
heading shown above. Other `[[full-id]]` uses are references. Do not add a second
ID field or HTML anchor merely for ID navigation.

**Default:** present States as flat sections.
**Invariant:** heading order and indentation do not define ancestry.
`Initial state` connects the Scenario category to its initial
State. `To` is the sole authored source of behavioral edges. Every State is
defined once and reachable; each after Initial has one parent; there are no
cycles. The same parent can reach the same child through different events or
guards. Guards are mutually exclusive and cover known outcomes within a single
`On`, not across independent events. `Primary terminal` and `Primary`/`Terminal`
mark the successful route and early outcomes. Terminal States own their `Holds`,
`Kind`, and `Outcome`, have no outgoing edges, and are not redefined inside `To`.
Avoid a parallel `Parent` field or separately authored tree.

### Check meaning and identity

**Default:** place a Check in the narrowest category that expresses its complete
guarantee. A state result belongs to that State; a guarantee shared by branches
belongs to their nearest common ancestor, possibly the Scenario root.

**Invariant:** category is the definition's address, not an inferred execution
path. `Guarantee` states the property or references a specific fact at its owner.
It does not duplicate the whole contract, setup, observation mechanism, or oracle.
**Contextual choice:** use `At: [[scenario-id/state-id]]` for a property at a state,
or `Paths` containing explicit Entry/Target pairs for a path/transition guarantee.
List all covered semantic paths for a shared guarantee. Add `Conditions` when
events, applicability, or alternative guarded edges need clarification; a unique
State chain need not identify a unique edge choice. Use existing definitions
instead of new transition IDs or a second edge list.

Root Checks still refer to real States. `At` does not waive preparation; Entry
does not create a private pause/resume seam. Concrete input values and environment
combinations belong to evidence. One Check may have several proofs; Paths count,
Checks count, tests count, and assertions count are different quantities.

**Default:** semantic kebab-case IDs identify the subject, not a revision or tree
position. Preserve identity across human renaming, moving MD, and evolution of
the same responsibility; explicitly rename an ID that became misleading.
**Invariant:** a different responsibility/guarantee needs its own identity; never
reassign an old ID to unrelated meaning. Keeping an ID does not prove behavior
unchanged. A State moved within its Scenario keeps `scenario-id/state-id` when
identity is preserved; review edges, Check scopes, and affected test nesting.
Moving a Check between categories changes its full address even if its local
`check-id` stays the same. Rename, split, merge, or delete definitions together
with causal references, scopes, declarations, and navigation. Confirm ownership
transfer or removal before deletion; no automatic legacy aliases.

## Implementation and reconciliation

For an agreed behavior change, use:
**plan → target MD → implementation and tests → checks → reconciliation**.
Independent project evidence obligations remain effective.

Establish the starting state, agreed target, and affected guarantees. Compare the
actual change, including uncommitted changes, with that target. Expand through
causal consequences rather than file adjacency. Reconcile in both directions:

- Implementation → model: changed inputs, outcomes, conditions, transitions,
  and effects, including new behavior with no MD ID or declaration yet.
- Model → implementation: required guarantees and distinguished alternatives.
- Model → evidence: sufficient current evidence for affected guarantees, including
  Checks with no test found.
- Evidence → model: references, prerequisites, inputs, expectations, and actual
  observations match the claimed guarantee.

ID search, declaration collection, and green runs do not replace this semantic
comparison. Use proportional owner checks. Evaluate proof sufficiency for
affected guarantees, including effects beyond the directly changed node.

An **unhandled branch** means implementation changed while the testing model has
not yet been brought up to date. Incomplete investigation does not itself prove
staleness. Reconciliation can confirm that unchanged MD is current; a cosmetic
diff is unnecessary. Distinguish stale model, missing/insufficient automation,
failed execution, implementation defect, and unknown impact; they can coexist.

**Contextual choices:** target MD can intentionally precede implementation.
A behavior-preserving refactor may leave MD and evidence unchanged after
verification. A regression fix restores the agreed guarantee rather than
rewriting correct expectations to match the bug. A test-only edit still reviews
affected evidence. An MD-only edit distinguishes clarification from a new target
and does not silently expand into implementing the latter.

**Default:** report the reviewed scope, material changes or confirmed currency,
actual evidence, and remaining work in the task's existing result. For an open
item identify the guarantee/branch, known fact, uncertainty, and next action.
Do not add persistent run-status fields to Scenario MD. Completed analysis with
findings is not completed implementation.

Count unhandled branches only within an explicitly inventoried scope. Count unique
semantic branches by State, event/condition, and outcome, not test runs, IDs, or
environments. For missing MD, identify the nearest owner and omitted behavior
without inventing a branch-ID registry. If the inventory is incomplete, report
confirmed cases and the unknown remainder, not an exact total or zero. “No
unhandled branches” is limited to the named fully reconciled scope, not repository
coverage or proof of implementation correctness.
