# Engineering Compass Context Map

Select all applicable rows for the task and its consequences. Read each
selected entry in full and follow its routes to applicable detailed rule
owners. For a full audit, including first adoption, select every entry
and detailed owner.
For an affected-scope audit, select the entries for that scope and its
consequences.

## Rule entry points

| Rule owner | Read the complete entry when the task or its consequences involve | Insufficient by itself |
| --- | --- | --- |
| [Code](rules/code.md) | Module or interface boundaries, decomposition and dependency direction, ownership of values/state/resources, validation and failure/async semantics, semantic names in code or authored protocol/persistence, types or contracts affected through JSDoc, dependency choice, algorithms or memory/performance decisions. | A spelling correction without semantic change, reading unchanged implementation, or running an unchanged command. |
| [Refactoring](rules/refactoring.md) | Planning, carrying out, or reviewing structural changes in implementation, tests, tooling, or documentation that preserve identified guarantees or meaning. | Formatting, mechanical import sorting, or a spelling correction alone. |
| [Documentation](rules/documentation.md) | Comments or JSDoc, repository documentation, semantic terms or titles in prose, documentation ownership or lifecycle, or substantive design/contract explanations (including in conversation). | A spelling correction without semantic change or an ordinary status update/summary of established facts alone. |
| [Product](rules/product.md) | Defining, implementing, restoring, or evaluating semantic inputs, outcomes, transitions, invariants, or supported guarantees, including those expressed only in types and internal tools. | Moving an import or private implementation with established unchanged semantics; reading an unchanged test to establish a fact. |
| [Behavior](rules/behavior.md) | Defining, changing, restoring, or evaluating a behavior model: states, transitions, Check meaning/IDs, ancestry, or changed implementation's agreement with documented behavior. | Markdown format, moving a link, or changing a fixture without changing model meaning. |
| [Testing](rules/testing.md) | Evidence design, implementation, evaluation, or maintenance, including Scenario-tree effects on existing proof. Test data, declarations, and support also qualify, including Stories and rendering support with no change to proof. | Running existing tests or reading an unchanged test only to establish a contract fact. |
| [UI](rules/ui.md) | Design-system setup or changes, presentation meaning, structure or styling, view state, action availability, interactions, accessibility, semantic view interfaces, or customization. | A UI consumer of a headless module, mention of a UI, a mechanical view import correction, or testing unchanged UI behavior. |
| [Integrations](rules/integrations.md) | Interaction across a contract owned elsewhere, including in-process boundaries. Covers configuration, translation, effects, resources, and lifecycle, including fixtures and scripts that work with real external resources. | Mention of HTTP, pure stub data, unchanged native tool I/O, or reading an unchanged adapter. |
| [Tooling](rules/tooling.md) | Configuration, commands, task graph, discovery and inputs, toolchain, dependency manifests, CI and hooks, builds, entry mapping, or delivery artifacts. | Running an unchanged command; a CLI/compiler product feature without such consequences. |

## Consequences to investigate

Use the affected responsibility to select a row above. The pairs below
describe how facts or decisions affect other responsibilities.

| Responsibilities | What crosses the boundary | Example consequence |
| --- | --- | --- |
| Behavior → Product | Supported guarantee represented by Scenario paths and Checks | A changed guarantee can require updating the modeled paths. |
| Testing → Behavior | Scenario Check meaning, address and covered paths | Changing a Check can invalidate its evidence. A test-only change can look up a stable Check for its expected result. |
| Testing → Product | Supported contract as a Requirement Origin | Changing a promised type, format or compatibility property can require new evidence. |
| Integrations → Product | Operation guarantee promised to consumers | A new outcome after a remote timeout can change both the supported contract and provider interaction. |
| Testing → UI or Integrations | Observable interaction, effect or resource lifecycle | A changed interaction or external effect can require a different observation or environment. |
| Tooling → Testing | Evidence required for a candidate and its environment | Changing how CI collects or runs tests can invalidate the required evidence. |

Apply Code or Documentation wherever their responsibilities are affected. A change
to a type or contract expressed in JSDoc reaches both routes.

## Route examples

- **Private module refactor.** Read Refactoring and Code, including its Modules owner.
  Assess the enclosing responsibilities even if the approved change stays in
  one file. Add Tooling when files move and Documentation when authored guidance
  or comments change.
- **Documentation restructuring.** Read Refactoring and Documentation when
  splitting a guide while preserving its meaning. For a split into new files,
  read Tooling's Cache and discovery route. Add Entries and delivery artifacts
  when the delivered documentation set is affected.
- **Internal move with a supported type change.** Read Refactoring and the
  applicable Code rules for the move. Read Product for the change to the type
  consumers see, even when runtime behavior stays the same.
- **Substantive explanation of an established contract.**
  Read Documentation. Add the applicable Code owners if the task also evaluates
  or changes a code interface or guarantee.
- **A contract change expressed in JSDoc.** Read Documentation for JSDoc
  and Code for the affected type or interface guarantee.
- **Scenario transition and its proof.** Read Behavior and Testing when the
  transition changes and the evidence needs reconciliation, including when the
  test files are unchanged. Read Product when defining, restoring
  or evaluating the semantic transition, including a regression fix that
  restores an agreed outcome. Read the accepted guarantee at its owner.
- **UI design-system work.** Read UI and its Design systems route. Use initial setup
  for a new system, or incremental changes for an existing system. Add Product,
  Behavior, Testing, Code, or Integrations as their responsibilities apply. Read
  applicable repository surface guidance through the local policy.
- **Remote write retry after timeout.** A changed guarantee and its proof
  reach Product, Integrations, Code's Failures and effects, and Testing.
  Add Behavior when the Scenario model or Check is affected. If investigation
  reveals a remote write behind a retry assumed to be local, classify external
  effect confirmation before proceeding with changes to retry behavior.
- **Browser tests omitted by CI.** Restoring native discovery and CI selection
  for a known suite reaches Tooling's Cache and discovery and Release and CI.
  Read the required suite and environment at their owners. Add Testing when
  proof changes or its sufficiency needs evaluation.
