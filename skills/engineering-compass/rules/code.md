# Code rules

## Select complete owners

Classify affected responsibilities and causal consequences; several rows may apply.
Read every applicable owner in full. Known unchanged facts can rule a row out;
unknown applicability requires facts from its narrow owner before dependent work.
These rows refine Code. Apply other matching routes from the
[Context Map](../context-map.md) and applicable local requirements.

| Owner | Load for | Alone insufficient |
| --- | --- | --- |
| [Modules](code/modules.md) | Responsibility/interface/decomposition, implementation form, file ownership, dependency direction or composition changes/evaluation. | Pure wording with established unchanged responsibility and interface. |
| [State and values](code/state-values.md) | State/resource ownership, inputs/outputs, validation, normalization, value/type/guard guarantees or schema exposure. | Reading an unchanged value as a factual input. |
| [Failures and effects](code/failures-effects.md) | Outcome/absence channels, suspension, cancellation, retry/diagnostics, ordering/grouping, commit or atomic publication. | Merely running an unchanged command or mentioning an external effect. |
| [Code naming](code/naming.md) | Semantic names in code, including interface qualifiers, code filenames, and authored protocol and persistence names. | A spelling-only correction with established unchanged meaning. |
| [Dependencies and performance](code/dependencies-performance.md) | External dependency choice/role/exposure/approval, owned complexity, algorithms, passes, allocations, cache invalidation or performance claims. | An unchanged approved dependency or unchanged operation with no such consequence. |

Do not infer scope from paths alone. Reclassify when an investigation or change
reveals another responsibility.

## Completion

Verify semantic boundaries and owned guarantees. Types/tests alone do not establish
responsibility, names, decomposition or evidence necessity. Reclassify new facts and
finish causal consumers, docs, checks and superseded-form removal.
