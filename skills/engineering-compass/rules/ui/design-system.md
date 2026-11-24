# Design systems

A design system defines the foundations, components, composition, behavior, and
interaction guarantees a product's UI shares. The repository UI profile owns
product-specific visual decisions; the product, UI, and Scenario owners keep
their established responsibilities.

## Choose the scope

**Invariant:** for every UI design, implementation, or review task, find the
affected UI owner and the applicable system rules, components, and references
before deciding what to change. Identify the required outcome and what must be
preserved. If an established pattern covers the outcome, apply it to the local
composition. If its guarantee or boundary obstructs the outcome, propose the
smallest sufficient revision with rationale, owner, affected consumers, and
proof. Apply the [change and review process](../product.md) to a changed
guarantee. A local exception needs a concrete scope and reason.

- Use [Initial setup](#initial-setup) when establishing or deliberately
  rethinking the system for a product or agreed surface.
- Use [Incremental changes](#incremental-changes) when a system already covers
  the surface. Carry forward prior decisions and work at the affected scope.

## Pattern classification

Read the [pattern catalog](pattern-catalog.yaml) when planning a new or materially
changed screen, layout/navigation, or interaction pattern, including before
Lo-fi. Start with the user goal, information, action, and constraints such as
volume, width, and available data. Apply the catalog's `selection_policy` to
candidate search, evidence, and the result. Record the applicable screen
archetype, layout/navigation pattern, and interaction/workflow pattern with
their IDs and relationship to UI responsibilities. The catalog owns matching
and identity rules. Apply [UI composition](../ui.md#planning-responsibility-and-composition)
and [Modules](../code/modules.md) to derive the structure and contracts.

## Visual iterations

1. Use the last shown revision of the affected variant unless the operator
   chooses a different baseline. Record the feedback against frame and
   transition IDs.
2. Before each new visual round, recheck classification for the affected
   surfaces against the feedback. Reassess candidates when the goal, constraint,
   or interaction changes. Record consequential changes and uncertainty.
3. Reconcile the model, rules, transition maps, and frames as one revision.
   Keep IDs while their meaning holds. Recheck preserved guarantees and return
   to the earliest affected approval when its basis changes.
4. Use static, numbered frames and state transition maps as the default
   interaction review. Compare before and after on the same data. Make the
   user's goal and available action apparent, show timely feedback, and make
   the next action or recovery clear. Follow local prototype formats; an
   interactive prototype needs a distinct question that calls for one.

## State transition maps

Give each UI state and transition a stable ID. For a state, record the conditions,
visible data and frame. For each transition, record the action or event, its
availability conditions, visible feedback, next state and effects on other UI
regions. Specify preserved or reset selection, filters and position. Show
material before/after pairs on the same data. Include accessible names, roles,
states and supported inputs. Where focus changes, state its location before,
during and after the transition, including failure and unavailable-action
outcomes. Review these decisions with the maps at Lo-fi and Hi-fi.

Maps and frames support visual scenario review. Transfer accepted behavioral
guarantees to the [canonical Scenario owner](../behavior.md#implementation-and-reconciliation)
at handoff. The [UI interaction owner](../ui.md#platform-actions-and-accessible-interaction)
defines the implemented accessibility and focus contract.

## Initial setup

Work through the applicable [Product reviews](../product.md#request-process)
and reuse their approvals. Group independent operator decisions in one round.
Continue context research and clarification while material needs, the model, or
combinations of patterns remain uncertain.

1. **Inventory and goal.** Establish business boundaries, users, guarantees and
   constraints. Inspect existing screens, components, tokens, themes,
   composition, interaction states, accessibility, tools and evidence. Separate
   actual behavior, accepted intent and pending work. Agree the scope, quality
   criteria and direction. Bring the existing system to production readiness,
   fill gaps with the operator, or rethink it.
2. **Research.** Find relevant competitors and alternative approaches. Present
   each candidate with its relevance and let the operator choose or add sources.
   Analyze approved sources. Establish User Persona, Journey Map and User Flow,
   including alternatives, frequency, data sources and failure/absence.
   Identify where the proposed UX helps and how to check that advantage.
   Capture operator preferences and optional screenshots or links. Classify
   each reference as visual, behavioral, or combined. Record the property,
   scope and observation for each part. Clarify ambiguous roles and await the
   operator's explicit completion of reference collection. Review and approve
   the business basis before dependent architecture planning.
3. **Structure and Lo-fi.** Classify problems using the catalog. Take the
   module map with responsibilities, relationships, data flows and
   classification through [independent architecture review](../product.md#architecture-review)
   and operator approval before drawing. Apply relevant, agreed visual reference
   properties to first-round structure and use behavioral references for
   actions and state. Show two meaningfully different variants and one balanced
   variant for the same flows on the same typical and large fixtures. Show how
   users find and act on items beyond the first screen. Use a numbered
   whiteboard and state transition maps. Explore other mechanisms in parallel
   Ideate alternatives while narrowing the main options. Check relevant flow
   branches, state guards, preserved/reset context, feedback, supported inputs
   and focus. Before Lo-fi approval, automatically check coverage of agreed
   branches, transition availability and map-to-frame consistency. Also walk
   a realistic scenario with the operator, including a frequent action and
   locating an item in a large set where relevant. Verify the action, visible
   response and next step.
4. **Hi-fi.** Start from operator-approved Lo-fi, maps and scenario-review
   results. Resolve material Lo-fi issues first. Use the established style
   or a neutral baseline when the system is new. Choose a main and second
   representative surface with different composition or density. When the
   second surface requires a new scenario, agree it and complete applicable
   Research and Lo-fi before detailing it. Show agreed
   actions and feedback, ordinary, loading, empty and error states where they
   apply, and the same surfaces at narrow, ordinary and wide available widths.
   Exercise long localized content and large lists or trees together at the
   narrow width where relevant. Use the agreed framing and measure the
   available UI area within it. Review automatically against the agreed
   criteria and review key frames, states and transitions manually with the
   operator. Include both surfaces in the same approval round before using this
   baseline for style.
5. **Visual style.** After Hi-fi, apply [Visual profile and style](#visual-profile-and-style).
6. **Handoff.** Base a shared rule on a shared semantic role or guarantee with
   concrete current or agreed future uses. Check existing rules, semantic tokens
   and component variants before adding a rule. Give each shared rule an owner,
   scope, applicability, observable guarantee and consumers. Keep
   screen-specific detail with the screen owner.
   Save the approved profile, frame references, maps and decision links in the
   repository's agreed locations. The behavior owner reconciles the UI map
   with existing Scenarios and prepares the target Scenario and Checks before
   dependent implementation. Link the relevant frames and transitions to those
   guarantees. In the implementation task, provide a native Test or Todo for
   every accepted Check and covered path under the [evidence lifecycle](../testing/lifecycle.md#missing-proof).
   After implementation and verification, reconcile Scenario, Checks, actual
   behavior and proof in both directions under [Behavior](../behavior.md#implementation-and-reconciliation).
   Review business intent through the actual architecture,
   transitions, side effects and proof in both directions. Obtain approval of
   the reviewed basis before dependent implementation. When adopting the
   workflow as policy, follow the [UI adoption checks](../../setup.md#ui-adoption-checks).

## Visual profile and style

Use the latest approved Hi-fi. Prefill known properties from inventory and the
agreed visual portions of references. Ask granular questions about remaining
visible properties. Give the operator a concrete choice or same-frame sample
when it distinguishes the options. Batch independent questions, resolve
dependent ones after their prerequisites, and distinguish a fixed requirement
from a preference. Cover character and references, color and themes,
typography, spacing and density, icons, shapes and surfaces, illustration and
backgrounds, and motion. Expand applicable categories to actual roles, states,
and components. Allow explicit values, confirmed inheritance or a delegated
proposal. Record the value, scope, priority and source. Record why excluded
properties do not apply. Propose two or three product-character traits from
the purpose and operator preferences. For each relevant surface, record the task
the styling should support and the visible criterion that connects it to an
agreed trait. Agree these traits and criteria as part of the complete profile.

Compare the baseline and distinct style candidates on the same representative
frame, data and state. Describe the visible principle, purpose and consequence
of each candidate. Validate unusual shapes and backgrounds with real content,
contrast, control visibility and supported widths. Show motion through static
keyframes, timing, repeated and reduced-motion states, and applicable controls
and focus behavior. For automatically starting decorative web motion that
continues for more than five seconds alongside content, provide pause, stop, or
hide. Preserve that control outcome when focus moves and other content is used.
If a style proposal changes behavior, agree its transition before using it in a
visual baseline. When a reference, property, or state changes, revisit affected
profile branches and exceptions. Confirm those values before accepting or
spreading the style.

Apply the selected direction to the second surface. Show each alongside its
baseline and ask the operator to identify visible shared traits before naming
them. Compare the observations with the agreed product-character traits and
task-specific visible criteria. Confirm a trait when the operator independently
names its supporting common feature and that feature is new or more apparent
on both surfaces than in their baselines. With
a relevant external reference, also show the difference from that reference.
Revise unconfirmed traits. Recheck hierarchy, readability, contrast, affordances and state
recognition across affected themes, widths and states. Resolve lost guarantees
before saving the approved rules and frames.

## Incremental changes

1. Start with the surface owner, its current UI profile, rules and relevant
   evidence. Check the change against the existing pattern and supported
   guarantees. Classify the affected patterns when their roles change or a
   visual round needs them.
2. Apply an existing rule locally where sufficient. When changing a shared
   rule, identify direct and indirect consumers, preserve unaffected
   guarantees, and agree affected changes through the Product process. Scale
   research, visual work and reviews to the decision at hand.
3. Reconcile affected rules, tokens, components, frame references, transitions
   and Checks. For each material guarantee record the known expectation, the
   appropriate observation and the evidence obtained. Use [UI verification](../ui.md#verification-and-completion)
   for browser, accessibility and interaction proof.
4. When using an increment as a routing probe, start at the real entry and
   record the reached rule, owner, consumer checks and expected versus actual
   observations. A reproducible result that matches the expectation passes
   at the observed layer. Record remaining proof at its owner.

## Catalog format

The catalog has one `selection_policy` mapping and three pattern sequences,
`screen_archetypes`, `layout_navigation_patterns` and `interaction_workflow_patterns`.
A pattern requires textual `id`, `name` and `name_origin`, and sequences
`problems`, `prerequisites`, `constraints`, `contrasts` and `sources`.
Each contrast contains a target `id` and textual `distinction`. Each source
contains textual `kind` and `description`, and a sequence of textual
`search_terms`. Source-specific text such as an `entry` or `title` identifies
the work for retrieval. Optional `aliases` and `compatible_with` contain textual
names and pattern IDs. Mappings and sequences organize the document. Every
scalar key and value is text. The catalog's `selection_policy` owns selection
and identity semantics.
