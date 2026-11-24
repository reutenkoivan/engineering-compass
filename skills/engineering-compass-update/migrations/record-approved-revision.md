```json
{"depends_on": []}
```

# Record the approved revision

## Applicability

Use this transition when an existing Engineering Compass adoption predates
versioned entries in root `AGENTS.md` or still uses the former setup path.
A verified versioned entry with current routes satisfies this migration.

## Decision and change

Show the effective old rules, the new snapshot source and revision, and any
affected local rule links. Use Setup's full audit when previous provenance
cannot be established reliably. Present any unresolved differences or
enforcement changes for the operator's decision.

Write the approved release, revision and source to the root adoption entry. Use the
verified committed package tree for a vendored installation. Update links to
Setup's adoption procedure where the repository used the former location.
Retain repository-specific policy with its local owner. For a user-installed
route, establish availability of the approved snapshot in the shared store.

## Verification

Read the candidate root entry and resolve the recorded immutable rules. Check
relative resources, local-policy links, and every changed enforcement route.
Use a fresh normal Codex request in the selected checkout to prove automatic
loading at the approved revision. For shared bundles, confirm a second
repository still resolves its own revision and source.
