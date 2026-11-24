# Declarations and package artifacts

**Default:** ordinary typecheck/build/existing consumer compilation is normal evidence;
API changes do not routinely add declaration tests. Runtime behavior, declaration
usability and artifact availability are distinct claims.
**Invariant:** special type cases, compile fixtures or emitted-declaration checks need
especially strong justification of all four:

1. A material concrete consumer type guarantee and its failure consequence.
2. A demonstrated gap despite typecheck/build/consumer evidence: reproduced regression
   or concrete defect, for example.
3. Why type/configuration correction or existing evidence is insufficient.
4. A narrow distinguishing check whose value exceeds maintenance/execution/context cost.

TypeScript, generics, branding, public APIs and `.d.ts` alone are insufficient; one
justified case authorizes no suite. Positive/negative cases exercise the guarantee
without `any`/casts bypassing it; negatives fail for the intended restriction, not
broken imports, and detect its removal. Package claims use the packed candidate's supported
entries; justified type evidence uses its declarations, not source/workspace aliases.
Ordinary required-file/link inspection is not a special suite. Check importability,
types, forbidden entries or bytes only for promised contracts. Development proof stays
proportional; delivery verifies the delivered candidate. This infers no SemVer and
restores no replaced contract for compatibility.

