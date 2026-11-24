# Preparation, Cases and resources

## State preparation

**Contextual choice:** prepare materialized state by the shortest production path
and confirm prerequisites; internally traversed state uses normal invocation and a
Test-interpreted witness. **Default:** replay preceding transitions only when production
preparation cannot establish state. **Invariant:** use production access without private
writes/testing handles. `At` invents no entry; `Paths` proof accounts for Entry, Target,
guards, events and temporal property, not just final success. Targets may be intermediate
without pausing production or adding handles; missing witnesses are evidence gaps.
## Cases and resources

**Invariant:** extract Scenario Cases from executable Test files. Cases hold immutable
semantic input, controlled dependency outcomes and optional independent expected values, not setup,
subject creation, lifecycle, actions, observations, proof or copied tree prose. Titles
own Check references; MD owns `At`/`Paths`. With multiple paths, case name/data plus
preparation/action identifies the path. **Default:** no `Case.path`, scenario/Entry/Target
metadata, framework or JSON is required. One Case may serve several Checks. Keep small
coherent sets in adjacent `cases.ts`; split by responsibility into `<behavior>.cases.ts`.
Scenario-shared support belongs in `internal`; independent data keeps its own owner.
Use files when bytes/format/layout matter, otherwise authored TS/JS. Name data directories
by meaning; do not mix resources into a generic fixture collection.
**Invariant:** executions cannot mutate shared Cases, including nested data. Allocate
mutable buffers/handles/stub state per execution. `readonly` does not prove isolation;
ownership can suffice without universal copying/freezing.

**Default:** keep simple inputs/dependencies local; fixtures need a lifecycle, isolation,
readiness or boundary responsibility. Use native runner adapters for injection/scope/order/
cleanup; resources stay runner-independent. Construct subjects explicitly in Tests or
composers, not hidden in fixtures. **Invariant:** own completion from creation, including
partial setup and Test failure; borrowing transfers no ownership. **Contextual choice:**
broader resource scope needs per-Test isolation or concurrency-safe restoration;
clearing shared namespaces after Tests does not isolate concurrent executions.
**Default:** keep support near its Scenario/`internal`; independent environment resources
may use `test/fixtures/<role>-fixture.ts`. No fixture framework or automatic support-file
test suite. Roles: Stub controls, Spy records, composer wires, Driver performs a real multistep
action, Probe/witness observes, Page Object exposes interaction, renderer/bootstrap
establishes environment. Support owns no expectations or pass/fail. Native `mock` APIs
are allowed with explicit roles; an ambiguous Mock is not a responsibility. Prefer
direct actions/native observations over proof-hiding `runScenario`. External test kits
need an accepted support contract; exporting a helper does not make it public automatically.

## Authored cases and generation

**Invariant:** authors choose guarantees, input classes/boundaries, actions and independent
expectations. Property-based discovery is outside this approach; a seed proves no
authorship. Independent cases need native Tests with independent reporting/filtering/
retry/cleanup, not loops inside one Test. Preparation, causal-sequence and indivisible-
guarantee loops are allowed. **Default:** explicitly declare one to three semantically
different cases; use declaration-time `for...of` for homogeneous authored object records.
More than three does not require a table. **Contextual choice:** Vitest `test.for` suits
genuinely tabular matrices or required parameterized TestContext. `test.each`, positional
tuples, printf placeholders, tagged tables and custom registration are not the convention.
Justify another runner's native facility rather than installing Vitest. Every generated
declaration retains marker, ID, claim and meaningful case name, not index/random identity.
**Contextual choice:** bounded generation removes demonstrated boilerplate under authored
constraints, without discovering guarantees or deriving expectations from the subject.
Prefer explicit data/narrow builders. Extract Case constraints; materialize execution
outside Cases. Seeds are deterministic/isolated; failures expose needed reproduction
data without dumping every run. Generator dependencies need their own justification/approval.

