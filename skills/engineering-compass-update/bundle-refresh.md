# Refresh the installed bundle

## Refresh the Codex plugin

On a marketplace tracking the `release` branch, run
`codex plugin marketplace upgrade engineering-compass` and verify discovery in
a fresh chat. Project rules resolve through the
[adoption contract](../engineering-compass/adoption.md).

## Switch to the plugin

Use the [delivery migration](migrations/migrate-to-release-channel.md) to
prepare and verify the new source, preserve approved rules, and clean up the
previous installation. Select the plugin explicitly when leaving a Git route.

## Refresh a symlink installation

Use the [delivery migration](migrations/migrate-to-release-channel.md) to move
the old symlink installation to a clone tracking `release`. It covers linked
worktrees and preservation of the common Git store.
