# Refresh the installed bundle

## Refresh the Codex plugin

Capture the selected repository's active release and installed bundle version
using the [migration procedure](migration-workflow.md#capture-the-current-release-before-updating).
Run `codex plugin marketplace upgrade engineering-compass` and carry the
captured evidence into the new Codex chat. Project rules resolve through the
[adoption contract](../engineering-compass/adoption.md). Use the
[repository migration procedure](migration-workflow.md) to advance a project
to another rule revision.

## Switch to the plugin

Capture the active repository release, installed bundle version and current
discovery paths before installing the plugin. Verify that the Git checkout at
`~/.local/share/engineering-compass` resolves each approved global revision
through `refs/engineering-compass/approved/<revision>`. The documented symlink
installation already keeps its Git store there. For a custom checkout, make
that path resolve to the verified Git store, preserving its refs.

For an unversioned global adoption, verify that `refs/engineering-compass/legacy`
retains the exact previous rule source. If the ref is missing, use the symlink
refresh below to capture it, or use Setup and Update to establish a verified
versioned adoption before switching. For an older standalone install or an
uncertain previous source, use the staged Setup audit below.

Install the plugin using the Engineering Compass marketplace. Move the legacy
discovery entries to a location outside discovery, then verify the plugin's
three skills and a previously approved adoption in a fresh Codex chat.
Restore the previous discovery entries and disable the plugin if verification
fails. Keep the Git checkout available for the approved revisions.

## Refresh a symlink installation

Symlink refresh makes a new complete `skills/` directory discoverable through
the existing user symlink.

1. Capture the actual previous source and release before preparing the
   refresh. Inspect the visible discovery link and compare the effective
   `skills/` file set and contents with the verified commit. Include ignored
   files that could be discovered as skills. On the first refresh, establish
   `refs/engineering-compass/legacy` in the same Git store only for that
   proven commit. If the live source moved after a partial first refresh,
   reconcile its identity before relying on the saved binding.
2. Use the [published target procedure](migration-workflow.md#fetch-the-fixed-target)
   to fetch the verified release into a staged checkout outside discovery.
   Read its release map and verify the forward route from the current bundle.
3. Copy the frozen object into the existing Git store with `git fetch` from
   the staged checkout. Create a detached `git worktree` at that commit
   outside discovery. Check the complete `skills/` tree and its `SKILL.md`
   entries against the published tree. Keep the old checkout and all
   approved refs available.
4. Recheck the previously selected source, prepare a replacement symlink next
   to the live one, and atomically rename it over that link using a native
   symlink replacement operation. If a safe replacement is unavailable or
   the source changed, keep the old link selected. Verify discovery and a
   known old adoption in a fresh Codex context.

For an older standalone installation, the existing discovered folders are
the live source. Audit the staged target first and establish a verified route
for affected adoptions before replacing those discovery paths. The symlink
refresh steps apply to an established bundle link.

If the old source or its provenance is uncertain, keep the prior bundle
selected. Give Codex the staged `skills/engineering-compass-setup/SKILL.md`
path explicitly and ask it to audit that exact target against current local
policy. For an approved target that must be activated while the older bundle
remains live, use Setup's committed vendored route in the affected repository
and verify it there. Report an unavailable audit path as blocked. Keep
repository-relative legacy copies on their established routes until their
individual transitions.
