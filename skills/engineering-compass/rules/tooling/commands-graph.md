# Commands and task graph

**Invariant:** every command has approved purpose, scope, inputs, CWD, arguments, mode,
admission conditions and truthful completion. Preserve these through root entry points,
hooks, CI and runners. **Default:** invoke canonical owners without copied logic or a
universal executor. **Invariant:** wrappers preserve failure status, diagnostics and
evidence links; swallowed failures/trailing success messages cannot manufacture success.
Verify argument forwarding; do not assume universal `--`. Finite checks use finite modes.

At first Tooling adoption, audit the **whole repository
task graph**: root/package commands, runner configuration, hooks, CI and implicit
invocation dependencies. Compare every edge with command policy; show current/recommended
structure, missing/unnecessary/inconsistent prerequisites and concrete reasons. This
differs from the direct-dependency audit. Later tasks inspect causal changes, not the
whole graph by ritual.

**Invariant:** edges implement approved policies and consumer guarantees through actual
data, artifact, effect, readiness or separately approved admission reasons. Aggregate
membership does not impose sequencing. Consumers do not copy upstream prerequisites;
current configuration does not establish desired policy. Include missing/conflicting
policies in the proposal before dependent changes.

**Invariant:** before adding, removing or changing an effective dependency, obtain operator approval of
the recommended structure, including indirect manifest/command/configuration changes
to edges or prerequisite meaning. Show current/target context, policies, reasons for
each changed relation, scope/parallelism/cache/local-CI effects and verification.
Reuse exact prior approval. Relocation preserving graph/policy needs no new graph
approval. Account for any effects on supported outcomes.

Require upstream build for consumed output/code/declarations, not task names; source
aliases must not conceal missing prerequisites for supported imports. Tasks without
policy dependencies stay independent subject to resource/output conflicts. **Default:**
package dependencies do not automatically run upstream tests; broader delivery proof
has explicit scope. Missing prerequisites cannot yield successful dependent proof.
Distinguish failed/interrupted/not-attempted work. Verify native graph/order/readiness
without old `dist`; no perpetual clean build or graph framework is implied.

