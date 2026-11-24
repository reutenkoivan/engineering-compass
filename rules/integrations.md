# Integrations

## Planning: ownership and boundaries

**Invariant:** the consumer owns the capability it requires, its inputs/results,
and interaction guarantees. The adapter owns provider mechanics and translation;
composition owns construction, SDK configuration, and wiring. An interface does
not transfer resource ownership. **Default:** reuse sufficient existing contracts;
introduce a seam for a real external-behavior, resource, translation, or supported
variation responsibility. Standard APIs may be used directly in their permitted
owner. Protocol types can be the meaningful interface of a protocol-owning module.
No wrapper per API, DI framework, `ports/` directory, or package per adapter is required.

### Incoming and outgoing data

**Invariant:** assign each guarantee to one canonical owner in both directions:
I/O/structural protocol form to the boundary owner, shared meaning to its semantic
owner, preconditions/results to the operation, and response/write representation
to the external-contract owner. **Default:** translate external records into the
needed inputs and invoke canonical validation rather than duplicate its rules.
Decoding, renaming, encoding, or assertions do not establish semantic validity.

Reuse established guarantees while data and preconditions remain valid; reassess
after new input, transformation, or changed conditions. Establish outgoing
guarantees before transfer by construction, validation, or both, without obligatory
schema passes. Normalize only contractual equivalences; preserve required lexical
evidence. Invalid present data does not silently become absence or a default.
Verify our mappings, significant acceptance/rejection cases, and output guarantees.

### Failure meaning

**Invariant:** the integration recognizes provider facts; the narrow semantic
owner interprets them; presentation boundaries map the semantic result without
reclassifying SDK exceptions/messages. **Contextual choice:** expected negative
outcomes become semantic results, invalid received data remains validation
failure, and defects retain their exception channel. An SDK throwing does not
determine the category. **Default:** recognize known failures around the relevant
external operation, not with a blanket catch that disguises pipeline defects as
missing/unavailable. Unknown causes remain unknown. Public results contain safe
contractual information; one infrastructure owner records the raw cause, without
downstream duplicate logging or raw public/telemetry payloads. Evidence must also
distinguish a mapper defect from an expected provider failure.

## Implementation: resources and effect truth

**Invariant:** every resource has acquisition/creation and completion owners.
Complete owned resources; preserve borrowed ones unless transfer is explicit.
Receiving a capability alone does not transfer ownership. **Contextual choice:**
lifetime follows an operation, adapter session, or application composition with
appropriate access/state/completion guarantees, not a mutable global registry.
Handle success, failure, supported cancellation, and partial setup. Await promised
async completion or explicitly transfer that obligation to another owner. A returned
stream/handle must remain usable under its transfer/borrowing contract. Failed
cleanup is not confirmed release; no universal cleanup API, timer, or retry is implied.

**Contextual choice:** classify cleanup by its guarantee. A required flush can be
part of the primary effect; release can remain an outstanding obligation; deferred
staging deletion is valid only if the contract permits it. **Invariant:** preserve
all established facts: unconfirmed effect is not success, confirmed effect is not
retrospectively absent, and confirmed effect does not prove every obligation
succeeded. Unknown effect retains a reconciliation owner. When primary work and
cleanup both fail, accidental exception precedence must not choose semantics.
Retain caller-actionable/recovery facts and defect channels while keeping raw
causes private. **Default:** use sufficient existing operation/resource/diagnostic
contracts; clarify unresolved consequences before dependent implementation. No
universal cleanup-wins, cleanup-ignore, or two-errors-means-`AggregateError` rule
applies. Passive telemetry's no-throw rule does not automatically apply to `flush`,
`close`, or `release`. Verify meaningful combinations, not an obligatory cross-product.

### Confirmation, cancellation, and writes

**Invariant:** define the promised effect, when it takes force, and sufficient
confirmation, including promised visibility/durability. Promise settlement, queue
acceptance, and confirmed state change differ unless the contract equates them.
Cancellation is accepted by the responsible owner of work that can actually stop.
Cancellation, timeout, supersession, and effect state also differ. Observed abort
before a controlled local commit preserves old active state; abort/timeout after a
remote request does not prove the effect stopped. A late abort cannot negate a
confirmed effect. Reconcile unknown outcomes through the owning contract; readback
must distinguish this operation, since a newer revision may belong to another
writer. Confirmation does not erase cleanup/resource obligations. No universal
status endpoint, timeout, or physical interruption mechanism is required.

For promised atomic state, stage and validate a candidate inaccessible to active
readers, then publish at one observable commit. Failed staging leaves old state
intact. Concurrent external writers need a base revision/precondition enforced
atomically with the write by the provider. Read-then-unconditional-write is
insufficient. Conflict is semantic, not permission to update the expected revision
and resend stale content. If continuation is supported, reread and reevaluate the
original intent, stage/validate a new candidate, and commit conditionally. Do not
invent merge behavior. Sequential external actions do not become one transaction;
compensation/rollback needs its own actual contract.

### Retry

**Invariant:** the effect owner determines retryable failures and proves safety.
The same physical request preserves logical intent, identity, input, payload,
precondition, and contractual idempotency key. Timeout/disconnection does not prove
absence. Idempotency must cover the actual provider scope, lifetime, and conditions;
a field named “key” is insufficient. A conditional write can prevent duplicates
without revealing whether our prior attempt or another writer caused a conflict.
Replanning is different from retrying the same physical request.

One retry owner accounts for caller, adapter, SDK, and every physical attempt.
Use a sufficient SDK facility or remove duplicated loops. **Default:** composition
disables retries or supplies both maximum attempts and total elapsed time. Count
the initial attempt and work plus delays. Stop at the first exhausted bound or
cancellation; do not wait a delay that cannot fit. The owner retains classification,
backoff, idempotency, and reconciliation. Equal limits do not justify a shared
executor. A budget does not physically interrupt noncancellable in-flight work;
remaining budget does not make a nonretryable failure retryable. No universal
numbers, key generation, units, headers, or library are prescribed.

### Groups, concurrency, and order

**Contextual choice:** decide `atomic` or `reporting` guarantees before execution.
Atomic requires complete staging and a real common commit. Reporting completes
possible independent work and reports every input. Scheduling or `allowPartial`
does not create either contract. **Invariant:** preserve exactly one correlated
final outcome per input, including confirmed effects, failure meaning, and
uncertainty. Repeats do not multiply final outcomes. Unknown effect is not “not
written” or `notAttempted`; do not retry confirmed successes because siblings fail.
Continue dependent work only after its prerequisite; distinguish unstarted work
where observable. Compensation has its own accepted effect, conditions, and
failures; no automatic rollback/saga/resumption API follows. An unconfirmed shared
commit stays unknown.

**Contextual choice:** interface-bounded fixed-small independent work gathers
settlements with `Promise.allSettled` or explicit wrappers. Arbitrary input-driven
work uses a bounded scheduler at the constrained resource's narrowest owner.
Dependent work follows dependency order. A currently short arbitrary list is not
interface-bounded. A shared limit must cover its promised scope across callers;
per-instance limits do not prove a process-wide limit. Prefer sufficient existing
provider/client mechanisms.

**Invariant:** an independent failure does not cancel siblings; correlate all
settlements. Expected failures stay semantic results; multiple unexpected rejections
retain defect semantics through `AggregateError`, without leaking raw causes into
public reports. Settlement accounting promises neither infinite waiting nor
physical cancellation. **Default:** buffered results preserve input or contractual
canonical order; completion order requires a separately named streaming contract
and concrete consumer need. Verify varying completion order, failures, and the
actual resource-limit scope.

### Diagnostic delivery

**Invariant:** actionable information belongs to operation results/typed diagnostics.
Passive signals use a safe synchronous observer; delivery isolates serialization,
queue, reporter, transport, and callback failures. Synchronous acceptance need not
mean synchronous remote delivery. Diagnostic failure cannot change domain outcome
or own domain retries; handle it outside the broken channel. A contractual receipt
or write is not passive merely because it is named a log.

A planned retry emits nonterminal `retry-scheduled` with safe normalized reason,
attempt, elapsed time, and delay. Exhaustion emits one terminal logical-operation
failure; eventual success emits none solely for failed attempts. Exhaustion does
not resolve unknown effect. **Default:** the narrow event owner defines safe typed
content; integration transports it using sufficient existing facilities. No raw
causes, duplicate raw logging, or obligatory logging/queue framework.

## Verification and completion

**Invariant:** target an owned mapping, configuration, lifecycle, composition, or
dependency-use guarantee and a concrete defect in our implementation. Provider
implementation guarantees remain provider-owned. Expectations are independent of
the mapper/serializer under test. **Default:** use the highest practical production
interface and smallest sufficient environment; inspect dependency public observations
before adding processes, networks, or files. Explain each resource's contribution.

A canned conflict may prove mapping but not that a write precondition was sent;
calling `close` or `commit` does not establish its final state. Use a real environment
when controlled boundaries cannot prove our composition/runtime/support guarantee.
Each support claim has a sufficient end-to-end example there, without a mandatory
Cartesian product. Matching available CI evidence can suffice; missing execution
remains explicit. Report confirmed facts, limits, and unexecuted obligations.
Dedicated
declaration tests require an especially strong concrete justification, not mere
type exposure or a public API.
