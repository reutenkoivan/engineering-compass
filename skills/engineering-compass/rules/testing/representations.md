# Representation evidence

**Invariant:** contractual exact representations use independently authored input and
expected values; expected changes need contract review, not overwrite. **Default:**
small readable values may be inline. Significant bytes/BOMs/whitespace/order, binary data and
large/multifile examples use source-controlled files:

```text
test/vectors/<contract-owner>/<representation>.vector.test.ts
test/vectors/<contract-owner>/<vector-name>/input...
test/vectors/<contract-owner>/<vector-name>/expected...
```

These name roles, not required extensions. Preserve contractual representation: parsed
JSON proves no original bytes. Prefer small direct loading; format-owned Loaders need
real layout/encoding/diagnostic rules and never execute, assert, register or update
expectations. Author the vector list explicitly, not by glob. Load within its Test for
correct failure identity. Each vector/operation is a Test. Encoder/parser evidence is
distinct from round trips. Native output needs no permanent bundle.
**Contextual choice:** reviewed visual snapshots supplement semantic/accessibility proof
for appearance contracts with defined conditions, comparison and baseline review.
Ordinary text/error/React-tree/runtime-object/release-tree snapshots do not replace
explicit guarantees. Use native placement; no new tool is mandated.

