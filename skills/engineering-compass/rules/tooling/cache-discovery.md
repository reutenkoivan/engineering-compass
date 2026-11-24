# Cache and discovery

**Invariant:** cached reuse preserves current guarantees for meaningful inputs and
environment. Old success cannot replace required fresh external effects/current-state
checks. Account for scope/arguments, configuration, dependencies/toolchain/environment
and outputs through verified native mechanisms, not mandatory custom hashes/all-env
lists. Restore consumer-needed outputs, not just logs. Mutable external state needs
sufficient identity/correspondence or fresh execution. Persistent watch/dev startup and publication
are not replayed completion. Preserve applicable noncacheable contracts for persistent,
secret and nondeterministic external checks. Cache changes need valid reuse, relevant
invalidation and restored-output proof; a hit is not a new run and mandates no permanent
double execution.

**Invariant:** tool-selected inputs match policy/configuration. Workspace, typecheck,
tests, entries and packaging are distinct sets; coordinate without parallel manual
indexes. Broad globs can hide invalid placement; narrow ones can omit required files.
Layout enforcement differs from native discovery. **Default:** use native includes/
excludes/entries; canonical explicit public-entry lists do not automatically become globs.

File/package additions, moves, renames and removals require affected-selector, consumer,
stale-reference and unwanted-output checks. Generated status/`.gitignore` does not define
every input set. Ordinary content edits need no all-config reread. Collection proves
declarations/selection, not behavior/artifact validity; counts do not establish the set.

