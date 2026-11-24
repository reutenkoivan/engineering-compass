# Proof and environments

## Test boundary and seam

**Default:** one Test proves one independently nameable guarantee; assertions can
express facets of one outcome, transition or inseparable causal sequence.
**Invariant:** guarantees needing independent failure reporting, filtering, retry,
cleanup or state require separate Tests. Expensive setup does not combine them;
another native Test is never a prerequisite. Files/nesting follow responsibility,
not assertion count.

**Default:** use the highest practical production interface that sufficiently
distinguishes the guarantee, not necessarily the whole application. A focused seam
is justified by an insufficient higher seam or disproportionate cases. Caller-facing
is module-relative and can be private. Decompose a real responsibility without a
minimum consumer count. **Invariant:** create no public exports, private-field access,
testing handles or injection solely to reveal internals. Public-package claims use
supported specifiers, not source aliases. Remove lower evidence only when replacement
preserves every relevant guarantee, condition, environment and distinguishing regression;
equal IDs, longer paths and green runs are insufficient.

## Oracles and interactions

**Invariant:** author expected values, relations and thresholds independently of the
subject's algorithm, serializer or predicate. An oracle repeating business logic needs
authored cases/Vectors or a justified independent property. Public semantic guards
can classify actual data; expectations remain independent. Test a guard itself with
independent positive and negative expectations. Private tags are not semantic
observations; round trips do not prove canonical bytes; overwriting output is not approval.
**Default:** use local native assertions over results, responses, public state or
locators, with minimal observations distinguishing alternatives. Probes, witnesses,
Spies and Page Objects observe without deciding pass/fail. Normalize only instability
outside the contract. A reusable oracle needs independent responsibility.

**Invariant:** dependency evidence detects a concrete defect in our transformation,
configuration, composition or use; provider implementation is not our responsibility.
Assess observations at the provider's public interface before adding resources and
explain each resource's distinguishing contribution. Use a real environment when an
imitation cannot prove our claim. **Contextual choice:** interaction proof follows
target proof only for a required observable effect or necessary distinction. Prepare
stubs/Spies before action. A throwing stub is insufficient if swallowed failure leaves
assertions passing. Avoid duplicate target/interaction proof; call counts need a
contract, and observing `abort()` proves no cancellation effect.

## Environments

**Default:** choose the smallest real environment that can falsify the guarantee.
**Invariant:** supported-platform claims need actual platform evidence, not fakes,
project names, skips or typechecks. Each claim needs at least one real end-to-end
example, not complete feature coverage by that minimum. Use a requirement/capability
matrix and justified combinations, not a Cartesian product. Shared data creates no
new Check IDs. Required unrun environments stay gaps; matching-candidate CI can cover
local unavailability. An accidental run creates no support promise.

