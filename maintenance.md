# Skill maintenance

Initial creation and setup can correct their own defects before completion.
Afterward, make changes to skill files in a dedicated maintenance task. A task
already scoped to the change qualifies. In an ordinary task, record the defect,
its impact, and the needed fix, then continue independent work.

## Planning

1. Identify the concrete defect or change, its scope, normative owner, and known
   consequences. Read affected files in full as the subject of maintenance;
   that reading does not enable their rules in the repository.
2. Compare current and proposed meaning: scope, normative level, conditions,
   exceptions, capability dependencies, triggers, adopted rules, and approved
   local differences. A small diff or unchanged version label proves no semantic
   equivalence. Find the previous content from an available source. If it cannot
   be established, audit the complete target configuration and expose the unknown
   comparison impact before adoption.
3. Prepare the concrete change and sufficient evidence. Meaning-preserving typo,
   format, or proven link fixes can proceed under this maintenance task's scope
   without asking to approve the unchanged rule again. New duties, changed
   applicability, and conflicts require the corresponding concrete operator
   decision; already granted exact approval remains valid.
4. Identify impacts on adoption, routing, applicability and local differences.
   Use the [repository setup procedure](skills/engineering-compass/setup.md)
   to audit changes to rule scope, routing, adoption, or local differences.
   Audit the affected scope and expand to a full audit when the baseline or
   impact cannot be bounded.

## Implementation

Change each norm at its owner, preserve the distinction between Invariant,
Default, and Contextual choice, and reconcile affected projections and examples.
Adding a rule set or changing applicability changes repository policy even
when the root entry stays the same. Use the repository semantic policy change
process and update the Context Map, affected owners and routing probes in the
same adoption. Retain the effective current rules until the coordinated
semantic transition is ready; mixed files from incompatible
revisions are not a complete update. Updating the skill does not authorize a
repository-wide code migration.

Verify changed file format and links, coverage of the accepted meaning,
adoption and local differences, and the affected behavioral probes. A shared
routing change requires broader isolation and composite-task probes. After
verifying correctness, compare context cost for equivalent tasks. Distinguish
human cognitive load from model input cost, use exact available metrics and
label approximations. Keep measurement reports outside runtime instructions.

Finish by reporting the changed guarantee, proof, affected configuration, and
remaining limitations. Ordinary tasks do not search for a new revision or change
the skill as incidental cleanup.

## UI pattern catalog

When editing the [UI pattern catalog](skills/engineering-compass/rules/ui/pattern-catalog.yaml),
use its identity rule. Verify a single YAML document, unique keys and IDs,
textual scalars, required fields, valid internal links and reciprocal
compatibility. Keep references local-first through textual descriptions and
search terms. Verify candidate selection with independent expectations for
multiple matches, one match and no match. Repeat a scenario with only the
product-category label changed and compare the outcome. When source hints
change, verify retrieval and distinguish what was found from what still needs
evidence.
