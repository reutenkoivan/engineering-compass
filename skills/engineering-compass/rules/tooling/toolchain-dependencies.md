# Toolchain and dependencies

**Invariant:** support ranges, execution pins and installation ownership are distinct.
Available executables do not establish support; conformance runtimes do not become
package managers. **Default:** each accepted install unit has one coherent resolution
owner and canonical lockfile/equivalent respected locally and in CI. Accepted separate
units may have separate owners; convenience does not justify competing resolution.

**Invariant:** reproduction differs from updating. Use native frozen/immutable mode
or equivalent. Manifest/lockfile inconsistency is a defect, not permission to retry
with updates; approved dependency changes may intentionally change resolution. Verify
actual versions, relevant environment differences and reproduction for install-contract
changes, without requiring reinstall for every edit.

**Invariant:** the narrowest actual consumer declares direct dependencies in roles
matching development/build/delivered use. Hoisting/transitive availability is insufficient.
Account for bundling/externalization, runtime, declarations and support promises; imports
alone do not decide roles. Frameworks are not automatically peers; optional requires a
real absence contract. **Default:** reuse version/catalog owners; manifests retain need/
role. Catalog membership neither declares consumption nor requires installation everywhere.

**Invariant:** approved changes align version source, manifests and lockfile through native
resolution. Inspect material transitive effects; do not hand-edit generated selection or
blindly remove lockfiles. Proven-unused removal includes causal imports/configuration/
metadata; unknown use is not non-use. Retain applicable dependency approvals.
Effective graph changes separately need graph approval;
a version update need not change an edge. Prefer native static checks with sufficient
install/build/consumer evidence and resolution review.

At first Tooling adoption, audit **every direct external runtime/development/peer/
optional dependency across all accepted install units**, including contractual environments
and concrete planned use. Establish each problem, consumer, actual/approved use, role,
version source and significant install/build/runtime/delivery effects. Use manifests,
lockfile, native graphs and analyzers; include tool entries, plugin discovery, environments
and public contracts before declaring unused. Missing textual imports prove no absence.

For each dependency, recommend justified `accept`, `replace` or `remove`; keep unresolved use/unverified
alternatives unknown. Transitives are footprint: name significant problematic nodes,
without a separate whole-lockfile approval list. **Default:** one coherent review records
reasons/decisions/unknowns and reuses exact approval. Auditing does not perform replacements.
First adoption requires completeness; later tasks audit affected
dependencies. No permanent registry or new scanner is mandated.

