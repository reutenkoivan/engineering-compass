# Documentation rules

Apply these rules to the affected documentation, including substantive design or
contract explanations in conversation. When a comment or JSDoc also defines or
changes a type or contract, apply the corresponding [Code rules](code.md).

## Names and terms

Use the [terminology principle](../principles.md#general-principles).
**Default:** use full meanings in normative document names. Avoid homemade durable
abbreviations and define unfamiliar abbreviations in prose.

## Comments and JSDoc

**Invariant:** code/types express what; narrative comments explain purpose,
ownership, invariants or non-obvious consequences without a documentation quota. **Default:** function JSDoc records non-obvious whole-function rationale
at its stable owner, not mere public visibility. **Invariant:** branch/expression/
workaround rationale stays adjacent; no function extraction solely for comments.
Preserve contract tags and type-bearing JS JSDoc without repeating TS parameters/
returns. **Default:** apply the [rationale principle](../principles.md#general-principles)
to narrative comments and remove stale rationale. Deprecation
text does not authorize compatibility code.

## Document ownership

**Invariant:** detail belongs to the narrow stable contract owner; transfers move it
and repair navigation, not copy it. A README is a truthful concise entry, not another
specification. **Default:** root docs cover availability/setup/structure; part docs
purpose/use/inputs/responsibility/local material proportionally. Keep current norms
and rationale in the main read set, history/rejected prototypes outside it.
Distinguish implementation, accepted intent and open questions. Exact schemas/exports
stay executable knowledge. Behavior's MD-first workflow maintains intent
and reconciles temporary divergence. Adopt glossary filenames, lifecycle tags,
`Implements` syntax or GitHub workflows through their applicable owners.

## Structure and reader navigation

**Default:** structure documentation by purpose, readers, their questions and
needed actions. Group related meaning, order explanation by understanding and
state actual action prerequisites. Disclose conditional detail through meaningful
links when the resulting route retains sufficient explanation and navigation.
**Contextual choice:** sections, names and templates follow the document's role;
a mandatory format needs concrete reader/navigation benefit. A checker enforcing
a template does not itself establish that benefit.
