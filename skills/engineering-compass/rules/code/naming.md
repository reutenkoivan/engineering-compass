# Code naming

**Invariant:** before a public naming proposal, state the responsibility independently
of the caller and justify narrowing qualifiers against the accepted contract.
Base the proposal on supported capabilities.
**Default:** use full meanings in public and interpackage names, authored protocol
and persistence names, and code filenames. Omit qualifiers only in unambiguous
typed context.

**Invariant:** types use role names without `I`/`T` prefixes or `Impl` suffixes; adapters combine integration
and role. Owned TS acronyms use word case (`Id`, `Http`, `Ir`, `Dto`, `Url`); preserve
exact external API/product/platform/header/wire/object-prefix spelling.
**Default:** avoid homemade durable abbreviations in code.
Keep project-consistent role words (`Config`, `Options`, `Input`, `Key`, `Lookup`,
`Reference`, `Record`, `Result`, `Outcome`, `Repository`, `Handler`) and verbs
(`create`, `parse`, `validate`, `read`, `find`, `resolve`, `load`, `ensure`, `handle`,
narrowly owned `execute`). They are not mandatory suffixes or universal definitions.
