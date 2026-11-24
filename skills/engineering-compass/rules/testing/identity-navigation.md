# Identity and navigation

## Type and identity

**Default:** one leading marker names the main proof organization:

| Marker | Purpose |
| --- | --- |
| `[s]` | Scenario behavior at the highest practical interface, in process or browser. |
| `[f]` | Narrow-owner invariant that Scenario evidence cannot distinguish or needs disproportionate cases to prove. |
| `[c]` | Independently specified contract across implementations/environments; one implementation is not another's oracle. |
| `[v]` | Contractual exact bytes, wire representation, canonical form or identity; equality alone is insufficient. |
| `[b]` | Production operation with controlled input, agreed method and independently agreed threshold. |

A Scenario's invariant stays `[s]`; no `[i]` exists. **Contextual choice:** at an
intersection preserve a valid main-organization choice; no universal `[c]`/`[v]`
precedence or duplicate Test for another marker. Typechecking, artifact/config
inspection, readback and delivery checks may be Verification without invented
Scenarios/markers. Threshold-free measurements are diagnostic, not `[b]`; a marker
authorizes no new infrastructure.

**Invariant:** use one space between marker and ID block, then a short expected-behavior
statement. IDs reference documentation definitions, not URLs/paths. Each repository
category has one canonical definition; Checks are category-local. Tests for different
inputs/environments can share a Check only for the same guarantee. Distinct guarantees
need distinct identities.

```ts
describe('[[save-document]] Save document', () => {
  test('[s] [[draft-preserved]] failed save preserves the draft', async () => {
    // Arrange, act, and prove this guarantee.
  })
})

// An independent non-Scenario Test uses its complete reference.
test('[f] [[revision-order#stale-rejected]] rejects an older revision', () => {
  // Arrange, act, and prove this guarantee.
})
```

Grouped Tests use local `check-id`; the nearest ID-bearing `describe` supplies its
category. Scenarios require `describe`; nested Scenario groups only combine child Checks
and reflect the documented tree. Outer IDs name ancestors. Root category is
`scenario-id`; State category is `scenario-id/state-id`, without intermediate IDs.
MD owns its complete ancestry and unique tree position. Category ancestry is not
the executed Check path. Titles own references; no duplicate metadata or SOM is needed.

## Independent Check documentation

**Default:** define Checks in existing MD at the narrow semantic contract owner,
or create a meaningful document there; no universal directory or file-per-Check rule.
Adapt heading depth, retaining this grammar:

```markdown
## Checks [[revision-order]] — Revision order
### Check [[revision-order#stale-rejected]] — Reject stale revision
- **Guarantee:** An older revision cannot replace the current revision.
- **Conditions:** The current revision has already been committed.
```

Conditions appear only when needed. IDs use semantic kebab-case, not ordinals/versions.
Invariants belong to modules, conformance to interfaces, Vectors to formats, budgets
to the operation/method owner's Flow. Reference executable schemas, values and
measurement configuration instead of copying them. Marker, runner, implementation
and execution do not define Check identity; retaining an ID proves no semantic stability.
**Invariant:** align definitions, guarantees, scopes, declarations and references;
never reuse an ID for another meaning. Independent Checks need no artificial States
or `At`/`Paths`. Treat evidence for a Scenario subject as Scenario evidence
regardless of marker or documentation form. Use the canonical Check for its
meaning, scope and address.

## Organization and navigation

**Default:** locate evidence beneath its semantic owner:

```text
test/scenarios/<scenario-id>/<behavior>.scenario.test.ts
test/scenarios/<scenario-id>/<behavior>.scenario.spec.ts
test/scenarios/<scenario-id>/internal/
test/invariants/<module-owner>/<responsibility>.invariant.test.ts
test/conformance/<interface-owner>/<interface>.conformance.test.ts
test/vectors/<contract-owner>/<representation>.vector.test.ts
```

Scenario suffixes distinguish in-process/browser execution; adapt to JS/TS and the
native environment. Justified departures preserve ownership, navigation and native
filtering; spelling alone mandates no repository migration. A Scenario file has one
documented root/subtree root without all-ancestor wrappers. Parent Checks stay in
the parent's file. Split independent behavior by preparation/resources/dependencies,
not size; keep an execution's preparation/action/proof together. No import-only
registration. Splitting Tests need not split MD; folders are not IDs.
**Default:** conformance has one interface-owned file and an explicit implementation
matrix. Cross-package test composition depends on implementations, without production
depending back on that composition. Budget Flow owns placement/invocation without a
universal suffix/directory. **Invariant:** native discovery collects intended
declarations without accidental import duplicates; deliberate case/environment
repetitions are explicit. Markers alone do not configure discovery.

**Invariant:** each visible Test exposes or permits recovery of type, full Check
reference, claim and declaration file; distinguish multiple implementations/environments.
Use available line numbers, never as identity. **Default:** recover category from
native hierarchy or source and nearest ID-bearing `describe`, not arbitrary splits
of flattened names. Native projects/modules/suites are not automatically MD categories.
Find the canonical definition, distinguish references/examples and establish uniqueness;
search hits alone do not. Read guarantee, conditions and owner. Scenario ancestry
follows `Initial`/`To`, separately from `At`/`Paths`. Detached IDs need context, not
folder inference. Collection proves discovery, not behavior or gap absence. Determine
included declaration states; source/native reporting must account for pending/skipped
declarations omitted by collection before claiming a complete inventory. Automation
needs an observed gap; no mandatory parser/reporter/registry/index/metadata follows.

