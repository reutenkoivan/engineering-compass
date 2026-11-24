# Failures and effects

**Contextual choice:** invalid program configuration/static composition/lifecycle throws
synchronously; expected negatives after operation start are semantic results;
untrusted invalid data is validation failure; programming defects/broken invariants,
including invalid promised output, remain exceptions for the terminal/global boundary.
**Default:** use owner-specific results with needed guards, without wrappers for
unambiguous returns. Keep generic machinery/tags/dependency types/combinators private;
needed semantic construction may be public. No universal `Result<T, E>` is prescribed.
**Contextual choice:** `undefined` means omitted optional input/property; `null` one
narrow absence; reasons affecting recovery/observability/protocol mapping need semantic
outcomes. Invalid present data is failure; map external meanings explicitly.

**Invariant:** infrastructure recognizes SDK/platform facts; the narrow semantic
owner assigns operation meaning; HTTP/CLI/UI adapters map it without reclassifying
exceptions. Raw causes/classes stay out of public results. Record causes once at
the infrastructure owner, not again above it; no diagnostics framework is implied.

**Default:** suspendable I/O, lazy loading, retry, acquisition/coordination uses
`Promise`; pure parsing/validation/classification/transformation/encoding stays sync.
**Invariant:** each operation has one mode across implementations: `T` or `Promise<T>`,
never `Awaitable<T>`, `MaybePromise<T>`, or `T | PromiseLike<T>`. Adding suspension
changes a sync public contract. Supported suspension normally makes all implementations
async; distinct lifecycles may warrant distinct operations. Cache hits/doubles retain
mode. Hypothetical suspension is insufficient; concrete planned use counts.

**Contextual choice:** accept `AbortSignal` only for owned cancellable waiting/retry/
queueing/acquisition/staging, not pure work. Distinguish caller cancellation, timeout,
invalidation and supersession. Commit is when the effect takes force, not necessarily
the last await. **Invariant:** observed precommit caller cancellation preserves old state and returns
cancellation; confirmed commit returns success despite later abort. Possible unconfirmed
commit needs owned unknown-outcome/reconciliation failure, not cancellation. A signal
neither proves no effect nor removes resource obligations.

For coherent state, stage/validate an inaccessible candidate before one observable
commit. Precommit failure/cancellation preserves active state; cleanup cannot weaken
this. One memory writer may swap a reference; concurrent external writers require
revision-checked transaction/CAS/conditional write against the candidate's base.
Conflicts are semantic: permitted continuation rereads, prepares, validates and commits,
not resends stale content. Arbitrary effects do not thereby become rollbackable.

**Invariant:** the effect owner owns retry, including SDK/outer mechanisms; no nested
retry of one effect. Preserve intent, identity, input, payload, precondition and
idempotency key. Prove idempotence/deduplication/conditional protection; failure/timeout
alone is insufficient. Unknown commit needs reconciliation or duplicate protection.
Replanning confirmed conflicts differs from request repetition; safe repetition does
not make every failure retryable.
**Default:** composition supplies `false` or both `maxAttempts` and `maxElapsedTime`.
Include the first attempt and elapsed work/delays; the first bound or cancellation
stops repetition. `false` preserves the initial attempt. Classification, backoff,
identity, reconciliation and state stay with the owner, not injected algorithms.
Immutable budgets may be shared; equal limits do not justify an executor. Exhaustion
proves neither no effect nor rollback; active-attempt interruption stays contractual.
No universal bounds/backoff apply.

**Invariant:** actionable information is a typed result/diagnostic. Passive observation
is synchronous and safe, never another result channel/retry owner/domain source.
Reporter, serialization, queue, transport or callback failures cannot affect outcomes
or throw/reject into callers. Delivery failures use dropped counts, separate state
or independent fallback without recursively reporting through the broken channel.
Observation need not deliver externally synchronously. **Default:** narrow event
owners define safe typed content; integrations transport it.
**Invariant:** planned retries emit nonterminal `retry-scheduled` with safe normalized reason,
attempt, elapsed time and delay. Exhaustion emits one terminal logical-operation failure;
eventual success emits none solely for earlier attempts. No raw causes in payloads.
Universal logging/tracing/fallback needs its own justified responsibility.

**Contextual choice:** interface-bounded fixed-small work uses `Promise.allSettled`
or explicit settlements; arbitrary input-driven work uses a bounded scheduler at
the constrained resource owner; dependent work follows prerequisites. A currently
short arbitrary list is not bounded by contract. Pure sync work need not become async.
**Invariant:** collect every independent settlement, correlate semantic failures to
input identity; one failure alone does not cancel siblings. Multiple unexpected
rejections remain defects via `AggregateError`, not public raw-cause entries.
Failed prerequisites stop continuation; distinguish observable `notAttempted`.
Direct fallible `Promise.all` neither gathers every result nor cancels siblings;
it cannot prove this obligation. No universal time/concurrency number applies.

**Contextual choice:** `atomic` stages and commits complete groups; `reporting`
finishes possible work with `succeeded`, `failed`, `notAttempted`. Exactly one
correlated final outcome per input; staging is not publication, unknown commit is
not absence, and notAttempted means never started. Parallelism/`allowPartial` does
not establish either contract; atomicity needs a real common commit. The owner
defines exact types and defect combinations. **Default:** buffered results preserve
input/contractual canonical order. Completion order requires a named streaming
contract and concrete consumer; execution and result order differ.

