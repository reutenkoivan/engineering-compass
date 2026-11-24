# Evidence lifecycle

## Missing proof

**Invariant:** every accepted Scenario Check/path has a concrete native Test or Todo;
required missing automation has a Todo. `At` invents no entry; intermediate States
do not automatically need Tests. Pending declarations retain marker, ID, specific
claim/case and required `describe`, not generic Scenario Todos. Use native forms such as Vitest
`todo` or Playwright `fixme` with a reason, without normalization wrappers/metadata. Skips
disable existing evidence, not create Todos; temporary skips have visible reasons and
unexecuted proof. Distinguish nonapplicable combinations from required unavailable
environments. Missing non-Scenario proof uses its pending type/reference; unrun
Verification is reported without invented Tests. No hypothetical placeholders.

Omission, empty bodies, collection and passing subsets do not close gaps. Execute proof
or accept a requirement change, not deletion/exclusion/skip. Report passed, failed,
pending, skipped and unexecuted separately, even for one Check. Stale models, defects,
missing proof and unknown results differ. No status MD/coverage registry is required.

## Maintain evidence

**Invariant:** Scenario-tree changes and Test changes independently trigger maintenance,
even with an unchanged tree. Preserve guarantees and truthful completion.
**Default:** reconcile the affected responsibility:

1. Establish changed guarantees/conditions, prerequisites, neighbors, resources,
   consumers and supported environments.
2. Search definitions/references and semantic dependents beyond literal IDs.
3. Retain/change/replace/remove/add evidence preserving guarantees and distinguishing
   regressions; equal IDs/counts, green runs or higher seams alone justify no removal.
4. Reconcile MD references, declarations, Cases, observations, preparation, environments
   and layout. Behavior requires MD updates before changed behavior's
   implementation; cosmetic test refactors invent no MD change.
5. Verify native collection after declaration/layout/discovery changes and execute
   sufficient affected proof. Keep project gates; narrow checks waive none and imply
   no manual repository-wide ritual on every edit.
6. Remove obsolete support/data/references/Todos. Unknown use proves no obsolescence. Record gaps without a permanent mapping registry.

