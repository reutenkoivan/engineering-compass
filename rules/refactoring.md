# Refactoring

## Scope and applicability

Use this procedure to plan, carry out, or review structural changes in
implementation, tests, tooling, or documentation that preserve identified
guarantees or meaning. Select the other applicable owners through the
[Context Map](../context-map.md) as consequences become clear.

## Establish the baseline and preservation target

**Invariant:** before editing, establish the problem, affected consumers, and
the guarantees or meaning to preserve from their canonical owners. Compare
the current implementation or text with the accepted baseline. When they
differ, establish the preservation target and explicitly resolve whether a
correction is in scope. Resolve unknown contract meaning or ownership before
dependent work. Scale the investigation to the uncertainty and consequences.

## Set the refactoring boundary

The refactoring boundary is the agreed scope of structural change needed to
achieve the goal while preserving the identified guarantees or meaning. The
entity named in the request is the starting point for investigation.

### Assess enclosing responsibilities

**Invariant:** during planning, trace the starting entity through its enclosing
responsibilities to locate the cause and clarify the operator's intent. For a
file, assess its module and package. Follow semantic ownership through
classification directories and account for affected consumers across boundaries.
When a change to an enclosing responsibility would better address the cause,
propose it with its consequences and agree on the broader boundary before
editing it.

### Reconcile the approved scope downward

**Invariant:** assess the constituent parts and their interactions throughout
the agreed boundary. For a package, review all its modules, their interfaces
and dependencies, and the division of responsibility among files inside each
module. For a guide, review its sections, placement of requirements, and reader
navigation. Bring discrepancies within scope into line with the approved target.
Apply [Code's module rules](code/modules.md) or [Documentation](documentation.md)
where applicable. Handle incidental findings outside the approved scope separately.

## Reconcile affected consumers

**Invariant:** follow causal effects across the boundary and reconcile affected
imports, links, tool selection, documentation, and evidence under their applicable
owners. Preserve the access guarantees of supported paths in the preservation
target. Confirm that consumers reach the intended replacement and that superseded
internal forms have been retired where applicable.

## Handle mixed changes

**Invariant:** make preserved guarantees and intentional changes separately
traceable to their verification. Apply [Product](product.md) to changes to
supported guarantees, including consumer-visible types or access paths even
when runtime behavior is unchanged. Apply [Behavior](behavior.md) when the
behavior model or its reconciliation is affected. When a supported path is
intentionally replaced, follow its applicable transition and migration rules.
A single diff can provide this traceability.

## Verify preservation on the candidate

**Invariant:** verify the actual candidate with evidence capable of detecting
the loss that the structural change could cause. Reuse existing checks when
they cover the affected property and the evidence applies to the candidate.
State remaining evidence gaps.

- For a moved test, apply [Tooling](tooling/cache-discovery.md) to confirm
  native selection and [Testing](testing.md) to verify execution and retained
  failure detection where affected.
- For restructured documentation, verify retained meaning, working references,
  and reader navigation. When the delivered documentation set is affected,
  confirm that it includes the linked pages under
  [Tooling](tooling/entries-delivery.md).
