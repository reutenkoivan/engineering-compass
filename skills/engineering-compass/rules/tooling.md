# Tooling

Repository Verification is distinct from a product Scenario. Choose tools using
the applicable project and dependency requirements.

## Common planning and enforcement

**Invariant:** each requirement has one canonical owner; consumer configuration,
commands and CI project their roles, not independent policy copies. **Default:** shared
requirements stay at their shared owner; inputs/environments/entries at their native
package/application/lane owner. A shared-config package needs responsibility/lifecycle,
not a reuse threshold; sufficient configuration needs no package/factory. Keep browser/
test globals out of unrelated common bases. Types create no runtime capabilities.
Project and package configurations can each own their appropriate scope.
JavaScript acquires no mandatory TypeScript flags.

**Invariant:** verify effective configuration: merge behavior, paths, CWD, defaults and
downstream effects. An `extends`/factory import is insufficient. Regenerate derived
configuration under its accepted owner model.

**Default:** use configured native options, commands and diagnostics before custom
parsing of source, manifests, human output or workflows. Orchestration may pass scope/
inputs and enforce real dependencies while preserving exit meaning and diagnostics;
a wrapper name proves nothing. Necessary output may be read as data.

**Contextual choice:** custom automation needs an unambiguous narrow invariant that
existing tools/evidence cannot sufficiently express. First state owner, violation
predicate, scope, concrete defect, current-owner insufficiency, smallest mechanism/data
source and distinguishing valid/invalid cases. Prefer an existing executor. Root
orchestration must not copy package rules; preserve justified Default departures and
contextual choices.

Desired shape follows accepted project rules and applicable rule sets, not merely
current files. **Default:** give precise static enforcement maximum priority; runtime
tests/manual review do not justify leaving expressible requirements uncontrolled.
Prefer the native static owner; additional evidence needs a distinct guarantee.
A concrete gap can justify a tool under dependency policy or the custom-check gate.
**Invariant:** enforcement detects violations and accepts permitted forms, including
justified Default departures. Static heuristics do not prove semantic responsibility
or replace runtime/artifact/environment evidence. Verify actual scope and distinguishing
permitted/forbidden cases; installation/incomplete green runs are insufficient. No
mandatory rule registry or speculative declaration suite follows.

## Common verification and completion

Readiness, collection, execution, build and publication prove different facts. Zero
selected required tests or Todo is not executed proof; an empty scope may be valid
under the actual command contract. Verify actual invocation and selected/result scope. Wrappers need no
automatic wrapper test suite.

**Default:** proportional owner checks serve development; agreed automation owns the
full gate. Do not duplicate it in hooks or rerun manually as ritual; new changes,
failures or gaps may justify reruns.

Retain safe evidence identifying candidate, scope, environment, result and failure.
Traces/screenshots serve needed guarantees, not a quota. Never substitute another
candidate's evidence or expose credentials. Unexecuted CI/hooks stay explicit; local success is not
executed CI. Do not commit/publish merely for evidence. Use local policy for
issue management.

## Select complete owners

Read every applicable owner in full; several rows may apply. These routes refine
Tooling only. Retain other applicable and local requirements. Establish unknown facts
at their narrow owner before skipping; reclassify causal consequences, including
those without a configuration edit.

| Owner | Load for | Alone insufficient |
| --- | --- | --- |
| [Commands and task graph](tooling/commands-graph.md) | Command purpose/scope/arguments/CWD/mode/status, wrappers, prerequisites, or direct/indirect effective-edge or prerequisite-meaning changes, including through manifests, outputs or readiness. | Unchanged graph and command policy established from affected owners; invocation of an unchanged command. |
| [Cache and discovery](tooling/cache-discovery.md) | Cache guarantees, inputs/environment/output restoration, native selection/packing scope, or file/package additions, moves, renames and removals. | Content edits with established unchanged selected sets and cache guarantees; running an unchanged selector. |
| [Toolchain and dependencies](tooling/toolchain-dependencies.md) | Support ranges, execution/install pins, resolution ownership/reproduction, or dependency use/role/version/removal and footprint. | Existing approved dependencies/toolchain with established unchanged roles and install contract. |
| [Entries and delivery artifacts](tooling/entries-delivery.md) | Public entry mapping, generated artifacts/metadata, packaging or delivered contract evidence, candidate correspondence, consumer docs/path usability or examples. | A private file move with established unchanged entry map and artifact/documentation contracts. |
| [Release and CI](tooling/release-ci.md) | Establishing initial publication/delivery, release/no-release intent under an accepted delivery/version policy, compatibility comparison, or CI/hooks/workflow scope, permissions, credentials, environment and evidence. | Local work outside a delivery/version decision with established unchanged CI/hooks; merely using existing CI evidence. |

Follow responsibilities, not filenames: a manifest can change graph, cache and
delivery contracts; a CI edit can change commands, installation or artifact transfer.
An artifact or release proposal involving special authored declaration evidence
also reaches Entries and delivery artifacts.
