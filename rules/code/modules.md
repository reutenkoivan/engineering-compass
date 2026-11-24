# Modules

**Invariant:** before adding or changing behavior, establish the target
responsibility, result, invariants, contract and exclusions independently of the
caller; compare the current implementation and reassess boundaries/interfaces,
lifecycle, composition and causal consumers. Find existing owners, including
under other names. Map actual/planned uses to guarantees; detect duplicated
invariants from narrow boundaries and unnecessary dependencies from broad ones.
Choose reuse, extension, extraction, reclassification with consumer migration or
local code. Scale analysis to uncertainty/consequences; no document per edit is
required. This does not change private-file placement Defaults or introduce
Product review gates.

**Invariant:** one problem/invariant has one implementation owner, possibly across
files. Consumers reuse its validation and derived decisions. Adapters may own
separate mechanics with one semantic owner; similar code need not share a problem,
and different names do not prove independence. **Contextual choice:** a concretely
planned responsibility may have zero consumers; distinguish planned/actual use and
provide contract evidence. No numeric reuse threshold applies.

**Default:** keep a cohesive responsibility in one file; extract independent private
responsibilities with their own invariants/lifecycle under the nearest semantic
owner. Size and consumer count do not decide placement. **Invariant:** directory
modules keep entry/composition inside their directory and expose one defined
interface, not all children. Consumers do not navigate private trees. **Default:**
use `index.ts` or its environment equivalent; respect tool-fixed contracts.
**Invariant:** file-to-directory migration updates imports, build mapping, docs and
evidence and removes the replaced entry.

**Invariant:** one-child code stays with that child; genuinely shared child contracts
belong to the nearest common owner's private `internal`. Private visibility or
similarity alone does not justify sharing/promotion. Names express responsibility
or child relationships; `utils`, `helpers`, `components`, `hooks` alone do not.
Classification directories have no interface/composition; responsible directories
are modules. **Default:** `steps` groups meaningful algorithm stages without
prescribing execution order.

**Invariant:** imports follow consumed contracts and the permitted semantic graph,
not directory location. Composition selects/wires implementations; external variable
behavior and caller resources cross the real consumer's narrow seam. Structural
ownership, imports, calls and result flow differ; callbacks do not require reverse
imports. Preserve project enforcement; no new graph file is implied.
**Default:** data is input, one-call dependencies are arguments, lifetime dependencies
are construction inputs, and canonical internal modules can be imported directly
within real external boundaries. **Invariant:** application composition chooses
infrastructure; no mutable global registry/service locator replaces explicit wiring.

**Default:** a stateless operation uses a named function; identity, private mutable state,
repeated operations or lifecycle can justify a class. Validation, normalization,
composition, variant selection or hidden representation can justify an opaque
factory, possibly using a class. Avoid instances solely for one call and factories
that only rename constructors, delegate once or return input. Method count differs
from invocation count; stateless operations may have effects. Validation alone
requires no factory.

