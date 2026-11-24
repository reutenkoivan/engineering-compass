# UI

## Design system fit

Read [Design systems](ui/design-system.md) to establish or rethink a system,
or when designing, implementing, or reviewing a change to the UI. Start with
the surface owner and applicable repository profile, and use the initial or
incremental workflow according to the scope. For pattern selection, follow
the catalog route in Design systems.

## Planning: responsibility and composition

**Invariant:** a narrow composition owner binds application resources, owns its
semantic UI state and created requests/subscriptions, and prepares a coherent
snapshot of template inputs. A controlled template renders that explicit interface
and invokes supplied semantic actions. It does not obtain hidden application
store/router/network/global state. Domain rules retain one canonical owner; UI
does not duplicate them to derive availability or presentation. Borrowed resources
retain their completion owner. Published snapshot values do not mutate covertly;
new state may yield a new snapshot, without mandatory memoization, deep freeze, or
forever object identity.

A simple already-controlled part with no orchestration responsibility needs no
empty controller/resource layer. No centralized app controller, class, custom
store, or file-count scaffold is required.

**Invariant:** child views receive narrow readonly inputs and semantic actions
for their responsibility, not the entire store/controller/parent props for
convenience. Type size alone does not define a violation. Normalize browser,
form, route, or native inputs at the platform-facing boundary; merely renaming
an event does not make it semantic. Handling DOM events inside a view is valid:
extract needed values, invoke the semantic action, and use canonical validation.
Callback sync/async behavior follows its contract, not a universal `void` type.

**Contextual choice:** a genuinely needed live platform handle can be a separate
explicit context with purpose and use boundary, apart from stable semantic input.
**Default:** use it synchronously; asynchronous use needs a concrete validity and
lifetime contract. Renaming a store/router/i18n client to `context` does not make
it a narrow platform handle.

### Widgets and Pages

**Invariant:** design a widget as a module: bounded problem, invariants, narrow
interface, encapsulated implementation and composition. Independent subproblems
define inner owners, not consumer count. State belongs to its invariant owner;
created resources to their composition. Widget-owned state stays private; state
owned elsewhere arrives through narrow inputs/actions. Shared guarantees need
their actual coordination owner rather than automatically moving to Page/global
state. Keep orchestration and controlled rendering distinct inside widgets.

Selection, draft, availability, and operation outcome are semantic UI state even
within one widget. Proximity to markup, variable name, or short lifetime does not
assign ownership. Measurement/animation mechanics belong to the responsible
platform adapter/composition and enter the template through explicit values or
justified live context. Native/CSS mechanics such as `:hover` and `:focus-visible`
need no duplicate application state. Input value, native `open`, and animation
completion are not exemptions when they control semantic outcomes.

Composition/platform adapters obtain application store/router/locale/permission
capabilities and prepare the view interface. Context/providers/hooks are access
mechanisms, not permission to hide application state in a template. **Default:**
prepare labels, direction, presentation values, and availability at the narrow
owner; locale/theme changes flow through its current interface. A narrow configured
formatting capability is possible, but stable function identity reading hidden
mutable state is not a stable snapshot. Semantic actions may change state through
its owner. Third-party rendering providers have an explicit adapter/composition
environment and configuration owner; do not rewrite library internals or wrap
every component merely to conform.

**Default:** a Page owns a coherent screen context, its specific logic, composition,
and necessary state/lifecycle. Widgets keep their invariants; visual nesting does
not transfer state. Screen coordination belongs to the Page when it is that problem's
owner; domain responsibility stays domain-owned. **Invariant:** route, framework
entry, and Page are not automatically identical. Normalize platform inputs into
the Page interface. Different URLs do not necessarily imply different Pages;
shared URL/layout does not prove one indivisible responsibility. An adequate
existing entry needs no extra adapter. Statefulness alone does not define a Page,
and a Page does not require a PageObject, Story, or testing infrastructure.

## Implementation: files and framework boundaries

**Invariant:** decomposition follows responsibility; orchestration and controlled
template retain their roles regardless of file count. Visual nesting or JSX count
does not define modules. **Default:** a cohesive controlled part can stay in one
file. A separate template with its own children can be a directory module; avoid
a symmetric controller/model/template scaffold.

When UI changes affect module structure, account for entry and composition,
private implementation ownership, and support shared by child modules.
Preserve semantic boundaries in naming and support placement. No global
`pages/`, `widgets/`, `src/`, or template-directory layout is imposed.

**Default:** `regions` groups simultaneous semantic areas; `views` groups mutually
exclusive principal presentations of one owner. Introduce either only when it
explains the real child relationship, recursively when useful. Responsive hiding
does not turn composition regions into alternative views. A conditional button,
badge, or small coherent fragment needs no view file. **Invariant:** these are
classification directories with no own API/entry/barrel; the UI owner composes their
children. Private children do not become public customization points by placement.

Illustration of UI module boundaries and private support:

```text
document-page/
├── index.tsx
└── template/
    ├── index.tsx
    └── regions/
        ├── document-list.tsx
        └── document-details/
            ├── index.tsx
            └── views/
                ├── empty.tsx
                └── content.tsx
```

Template and children consume prepared inputs/actions. A simpler template can be
`template.tsx`; independent child orchestration needs an explicit composition owner,
not hidden application state in a template.

Establish actual framework discovery, entry interfaces, environments, and constraints
before choosing placement. Keep fixed entries contractual and organize free
implementation by ownership. A framework entry may itself compose the Page when
that is one responsibility; otherwise it normalizes input into a separate Page.
A delegation file needs its own responsibility, and a fixed filename does not
justify another arbitrary entry beside private implementation. Multiple entries
may share one Page. Verify affected native discovery/build/routes; typecheck alone
does not prove discovery. No new router or framework abstraction is implied.

## Customization and its maintenance

**Invariant:** adding, changing, or removing UI reviews existing and new customization
within the affected responsibility and its consequences. Decide whether to retain,
introduce, change, or remove a Slot. A confirmed sufficient design may stay unchanged.
**Default:** start with defined child composition. Customization needs a concrete
accepted use, including planned use; there is no minimum actual-consumer count.

Prefer Slot composition for alternative child implementations sharing one semantic
role contract. Configuration configures one cohesive implementation. Do not hide
different responsibilities, structures, interactions, invariants, or lifecycles
inside parameter-switched implementations. Flag count or naming does not replace
that analysis. Values/availability use ordinary inputs/actions, appearance uses
a styling contract, and replacement of immediate public children uses a flat
SlotSet. Universal private variability or test-only substitution is not sufficient
reason for a public customization contract.

Replacements honor their role's inputs, actions, guarantees, and state/resource
ownership. They do not duplicate domain rules or introduce hidden application
state into a controlled template. Review follows this sequence: identify the
responsibility, variability, actual/planned consumers → choose retain/add/change/
remove → justify narrowed capabilities → migrate composition, implementations,
interfaces, entries, consumers, docs, and evidence → verify state/actions/lifecycle
and remove obsolete support.

Remove a Slot only when its capability is obsolete or completely satisfied by
the intended contract. One implementation or zero current users is insufficient
if an accepted plan still needs replacement. Unknown external usage is not absent
usage. Removing a replacement point need not merge an independent child into its
parent. Moving alternatives behind configuration flags is not simplification.
Migrate to the target without compatibility-only parallel forms; fewer Slots or
successful rendering alone does not prove the transition complete.

### SlotSet and styling contracts

**Invariant:** a SlotSet is a flat set of one owner's immediate public child
presentations, named by semantic role. Each takes its narrow child interface,
not parent props/resources. Expose explicit semantic leaves, not a barrel of the
private tree. Deeper customization belongs to that deeper owner's contract, not
parent path maps. Private app slots do not each require a package subpath.

Preserve selected implementation identity under the framework during ordinary
data updates. Runtime replacement is an explicit composition change with defined
state/lifecycle effects. Slot identity and props-snapshot stability are different;
no forever SlotSet-object identity, global cache, or mandatory memoization follows.
Define supported replacements, each default's owner, whether partial sets are
allowed, and supported absence meaning. Do not assume universal `Partial<SlotSet>`,
deep merge, resolver, or `undefined`/`null` semantics. Migrate overrides/defaults,
interfaces, entries, and consumers together. Matching names/props do not establish
behavioral interchangeability. Verify data updates versus actual replacement and
their relevant lifecycle/import consequences.

The owner defines its supported styling surface, preserving behavior/actions.
Avoid arbitrary DOM/platform passthrough and dependence on private markup.
**Default:** narrow appearance values configure one cohesive implementation;
density/variant options undergo the same responsibility analysis. Concrete caller
needs can justify tokens, CSS variables, class hooks, or other points with explicit
target, scope, defaults, and precedence. Neither `className` nor `style` is universally
forbidden. Styling does not authorize replacing semantic actions with event props
or removing Slots by hiding implementations behind conditionals. Ordinary state/
availability conditions alone need not be a Slot. Remove obsolete styling surfaces
with their causal uses. No CSS system or visual-test infrastructure is mandated.

## Platform actions and accessible interaction

**Invariant:** the semantic interaction owner decides the result; the platform-facing
owner executes its mechanism. A widget/internal module can own it; Page is not a
mandatory coordinator. **Default:** use existing framework/platform capabilities
for focus, scrolling, measurement, and effects; managers/wrappers need independent
responsibility. For a needed narrow platform capability define use moment, target
validity/lifetime, unavailable-target outcome, and cleanup owner. Synchronous use
is normal; async use needs justified validity. Created listeners/observers/effects
are cleaned up by their owner; borrowing a handle does not transfer disposal.
Measurements enter templates explicitly. No universal timer, ref, manager, focus
trap, or return-focus algorithm is prescribed.

Visible state, accessibility semantics, and actual interaction express one contract.
Define purpose, state, actions, supported inputs, and their platform accessibility
meaning. Roles, names, state attributes, keyboard and focus behavior follow that
contract. Unavailable actions cannot initiate through supported UI input methods;
disabled appearance alone is insufficient. Inertness does not impose a universal
focusability policy: focus, explanation, and other interactions remain contractual.
Availability arrives through the prepared interface; domain preconditions remain
enforced by the operation owner and are not safeguarded only by a button.
**Default:** use suitable native/chosen-library semantics. A custom mechanism needs
a concrete need and complete interaction contract. Preserve these guarantees through
Slot, styling, and composition changes; no universal ARIA/tag/scanner/WCAG-version
policy is introduced here.

## Verification and completion

**Invariant:** evidence distinguishes a concrete defect in our implementation or
composition. Prepared props, wiring, and browser outcomes are distinct observations.
**Default:** exercise the highest practical production interface in the smallest
sufficient real environment with existing tools:

- Prepared-view-data guarantees use owner results.
- Wiring uses rendered interaction and observed outcome/semantic action payload.
- Disabled, keyboard, and focus guarantees use supported interaction behavior.
- Browser layout/geometry/platform guarantees require the relevant real browser.
- Agreed exact appearance uses visual evidence alongside needed semantic and
  accessibility evidence.

A screenshot alone proves neither behavior nor accessibility; recording a platform
method call does not prove its promised effect. Expectations stay independent.
Prove our wiring/configuration/dependency use rather than provider internals. Cover
affected supported Slots, states, and environments sufficiently without a suite
per component or automatic Cartesian product. Keep duplicate lower evidence only
for a distinct important guarantee/failure mode; preserve sufficient evidence
through customization changes. Use semantic interaction points, observable readiness,
and isolated state. Story presence and lint success are not interaction proof.

State confirmed
guarantees and missing checks separately. Browser evidence requires a sufficient
environment.
