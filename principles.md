# Principles

This is the mandatory foundation of an adopted Engineering Compass.
Concrete conventions belong to rule sets reached through the Context Map.

## Philosophy

Reduce cognitive load across planning, implementation, business reasoning,
analysis, documentation, and other solution text. Make it easier to locate a
responsibility, understand its behavior, and trace the consequences of a change.

The file tree is a navigation interface. A developer commonly understands a
module directory as an encapsulated responsibility. Names and placement should
help identify which files answer a problem, while keeping relationships to
other responsibilities visible. A directory used for classification or data
does not become a module merely because it is a directory.

A module creates a mental abstraction for a coherent problem. Its purpose is
responsibility, not a minimum reuse count. Consistent decisions under the same
conditions let people transfer understanding between parts of the solution.

Cognitive convenience must preserve performance and reliability. Evaluate
algorithms, data structures, passes, memory, execution, and failure consequences
alongside readability. Claims about runtime properties need appropriate
evidence. Reliability does not reinstate an obsolete contract during an agreed
change to its replacement.

Where applicable rules leave a choice undefined, establish the facts, purpose,
responsibility, and existing requirements; identify the undecided part; choose
a local solution using these motives; verify its consequences. Explain material
trade-offs briefly. This creates neither a new skill invariant nor a requirement
to approve every local choice. Missing product intent or conflicting requirements
needs resolution; philosophy supplies neither missing facts nor permission to
ignore an applicable rule.

## General principles

Use these in both planning and implementation:

| Principle | Planning | Implementation |
| --- | --- | --- |
| Start with meaning and responsibility | Identify the problem, intended contract, and affected owner. | Judge structure by the responsibility it expresses. |
| Decompose by coherent responsibilities | Establish parts, boundaries, owners, and their combined result. | Keep related meaning together; revise boundaries when responsibility changes. |
| Make direction explicit | Distinguish dependency direction, the route to understanding, and execution prerequisites. | Preserve the intended dependencies and explanation order; express required sequencing and independent work. |
| Keep knowledge with its owner | Find canonical sources of facts, decisions and guarantees. | Reuse guarantees and decisions from their canonical owner. When ownership moves, update the consumers and references that depend on it. |
| Justify complexity | Name the concrete need and obligations of an abstraction, dependency, or mechanism. | Retain sufficient solutions whose obligations are justified. |
| Make meaning and reasons legible | Establish what each concept means, agree on its term and identify material constraints. | Express meaning through names and structure, and use the agreed terms across representations. Explain non-obvious decisions at their owner. |
| Prove the required property | Identify the claim and sufficient evidence. | Verify that property and state the evidence's limits. |
| Complete the consequences | Identify consumers and dependent materials. | Finish the causal transition and remove superseded parts. |

**Invariant:** in semantic naming and explanations, use one term per concept.
Names express accepted responsibility and scope, including justified qualifiers.
Establish that scope from the accepted contract. **Default:** preserve external
vocabulary and make its mapping explicit where it differs from the agreed terms.

For a non-obvious decision, explain what drove it, what was chosen, and what follows
from that choice.

A readable explanation need not imply sequential execution. Data flow does not
determine import direction. These principles prescribe no universal layer stack,
file layout, API, test syntax, or document format.

## Normative meaning

- **Invariant:** holds whenever its scope applies.
- **Default:** the normal choice. A departure identifies the concrete case and
  preserves the rationale; a checker must not reject a justified departure.
- **Contextual choice:** choose using the stated conditions and verify the shared
  guarantees rather than treating one option as mandatory.

Keep each rule's scope, level, requirement, rationale, conditions, exceptions,
and evidence together at one normative owner. Planning and implementation refer
to that rule rather than declaring it twice. Existing project obligations stay
effective. Resolve apparent conflicts through the repository policy process.
An affected rule or local difference may require an audit.

## Workflow guidance

**Invariant:** guide the operator through each agreed workflow that applies to
the task. Open every user-facing assistant message with a visually distinct
fenced `text` block. Use the G-02 left-to-right Git-style graph to show the
full path from its first stage to the agreed endpoint. Keep each applicable
documented stage visible as a distinct step. Label the path as proposed while
establishing its scope or endpoint. Use `↴` and `↳` to wrap long lines.

- `●` Completed stage. Include a short bracketed summary of the decision or
  result needed for later work.
- `◆` Active stage. Expand only the branch containing the action addressed in
  the message. Put one `HEAD` at the exact active position. Show completed
  actions, open decisions and alternatives relevant to the transition. Group
  similar internal steps if their distinction does not affect the next action.
  Include the full path of an agreed active nested workflow in that branch.
  Show other concurrent active stages compactly and identify them as concurrent.
- `○` Upcoming stage. Show only its name on the main path, in order. While a
  route is unresolved, show the common future path and put the alternatives and
  their conditions in the active branch. Check available facts and ask the
  operator to decide choices that determine the outcome. Once resolved, show
  the selected path.

On transition, collapse the completed stage to its summary and expand the
new active stage. When a stage change can proceed under existing authorization,
send a progress message with the updated graph before working in the new
stage. Then continue the authorized work. State the next action, who takes it,
and any operator input or approval the workflow requires. When blocked, place
the prerequisite or the action awaited at `HEAD`. On return, mark the affected
stage with `↶` and explain why. In the final message, mark the agreed endpoint
with `✓` once reached.

Two snapshots of a CSV export show how a choice becomes a summary.

```text
● Business planning [CSV, implementation in scope] ── ● Business review [Fields and access approved] ↴

↳ ◆ Architecture planning ── ○ Architecture review ── ○ Cross-cutting review ↴
  ╰─ ◆ Choice of export approach (HEAD)
       ├─ Generate during the request
       └─ Prepare in the background and show readiness

↳ ○ Implementation ── ○ Change review
```

```text
● Business planning [CSV, implementation in scope] ── ● Business review [Fields and access approved] ↴

↳ ● Architecture planning [Background export with readiness status] ↴

↳ ◆ Architecture review ── ○ Cross-cutting review ── ○ Implementation ── ○ Change review
  ╰─ ● Review by a separate AI ── ◆ Operator approval (HEAD)
```

## Classification closure

1. Read the [Context Map](context-map.md). Classify the requested work, any
   applicable audit scope, and their causal consequences. Use every matching
   row to select rule sets.
2. Read each selected entry and its applicable detailed rule owners completely,
   including both vectors and exceptions. Obtain facts from their narrowest
   owners. A fact lookup by itself leaves rule applicability unchanged.
3. Classify the consequences revealed by the plan and the rules until all
   affected responsibilities have been classified and all applicable rules read.
   Investigate unresolved applicability before dependent work.
4. If a new fact in investigation, planning, or implementation reveals another
   responsibility or invalidates an applicability decision, pause dependent work.
   Reassess the procedure conditions already in context when the task or
   audit scope changes. Reapply the map with the resulting scope, read new
   applicable rules through their entries, and revise the affected plan and
   proof before resuming.
   Continue independent authorized work.

An attempted read with truncated output is not complete; recover the missing
portions of required material before dependent work, reusing unchanged portions
that remain available in context.

If facts are known but routing still cannot classify the responsibility, make
the routing gap explicit and resolve whether it needs a rule or remains a local
choice. Loading every domain or borrowing the nearest domain is not closure.
Apply rules within their documented scope. A relationship or fact reference
can prompt investigation of applicability.

Start with canonical behavior, code, configuration, and evidence owners. Read a
small relevant Scenario whole. Follow consumers, prerequisites, neighboring
outcomes, shared resources, and affected evidence, including semantic
dependencies without explicit links. Use ID search and native collection or
reporting when needed. Reuse unchanged complete material while it remains
available and current in context, unless current instructions require rereading.

If the foundation, Context Map, or an applicable rule file is unavailable,
identify its exact path, cause, and dependent work. Pause that work, restore a
proven reference or agreed source, and resume classification. Continue independent
work and report any outstanding recovery.

## Change boundary and completion

Apply the Boy Scout rule to the task and its consequences: bring the touched
integration responsibility as close as practical to the applicable rules' target
design. Improve existing code in that responsibility as needed. Physical
adjacency alone does not expand the scope, and the scope can cross files or
packages when consequences do.

Move to the intended contract, update affected consumers, and remove replaced
forms instead of maintaining backward compatibility. Preserve data and account
for external consequences; independent project requirements cannot be silently
changed. Completion means the responsibility, consumers, documentation, and
evidence agree, superseded parts are removed, and remaining limitations are
explicit. A plan for an external action is not evidence that it happened.

**Invariant:** after this skill's initial creation and setup are complete, any
change to any skill file requires a separate maintenance task, including a typo,
link, formatting, helper, rule, or package replacement. In an ordinary task,
record the defect, impact, and needed fix; continue independent work. A blocker
or Boy Scout cleanup does not authorize an incidental skill edit. An existing
task already dedicated to that exact maintenance needs no additional task.
Context economy is subordinate to sufficient decisions and evidence. During
skill validation compare equivalent tasks only after correctness; distinguish
human cognitive load from model input cost. Ordinary use requires no metrics log.
