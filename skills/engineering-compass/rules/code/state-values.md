# State, resources and values

**Invariant:** mutable state has one owner with semantic operations and readonly
snapshots; request-specific server state is not mutable global state. **Default:** caller inputs and published
results remain stable, including earlier snapshots; `readonly` alone is insufficient.
A named readonly live view may change when that is its purpose, without mutation
rights. Mutate fresh solely owned storage before publication, not borrowed input
without ownership transfer. Universal copies/freezing are unnecessary.

**Invariant:** creators complete owned resources on success, failure, cancellation
and partial creation. Injection preserves caller ownership unless transferred;
close an owned subscription, not its borrowed connection. Operation/environment
contracts define completion, cancellation and cleanup failures; no universal disposal
API or mandatory cancellation follows.

**Invariant:** establish input invariants before semantic use and output invariants
before return/publication; valid input does not prove output. **Default:** accept the
narrowest required readonly caller-authored/serialized/composed shape; its semantic
owner validates/normalizes once and consumers rely on that guarantee. Fields may
contain `unknown`; the whole input need not. Reassess for new arrivals,
transformations, mutation or changed preconditions.

**Invariant:** parsers/validators/normalizers return the exact accepted type.
Assertions, brands, `as const` and `satisfies` do not establish runtime validity,
presence, identity or compatibility. Normalize only documented equivalences; preserve
lexical evidence needed for diagnostics/identity/regeneration. Do not silently trim
or fold identifiers/canonical values. Prove outputs by construction/validation/both;
do not copy the same invariant implementation for each direction or require a schema
pass when construction already proves the output guarantee.

**Contextual choice:** readonly records express named/serialized fields, branded
primitives operationally primitive identity, opaque Value Objects coupled invariants
or operations. **Invariant:** confirmed semantic values are non-forgeable through
the normal public interface; expose operations/guards, not mutable storage or a
universal public `Brand<T, Name>`. Classes are not mandatory. Library-owned public
variants expose type-narrowing semantic guards; consumers do not inspect private
tags. Contractual authored/wire discriminators may remain public without removing
guards. Internal unions and caller-authored tags remain allowed; variant guards
are not necessarily untrusted-input validators.

**Default:** runtime schemas remain private unless an independent supported consumer must
inspect/compose the schema; validation need alone is insufficient. Prefer concrete
public interfaces. Public generics preserve real caller-visible type relationships,
not runtime validity, merging independent responsibilities, or exposure of private
generic machinery.

