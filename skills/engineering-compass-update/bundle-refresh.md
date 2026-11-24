# Synchronize the global installation

Keep the type of the active global installation. Use
`https://github.com/reutenkoivan/engineering-compass.git` and the
`refs/heads/release` branch. The target is the branch snapshot's `plugin.json`
and `skills/`. Keep the selected snapshot fixed through readback.

If the installation still needs to move to the release channel, follow the
[delivery migration](migrations/migrate-to-release-channel.md) for
preparation, switching and separately approved cleanup. Use this document's
branch snapshot and readback to verify the package for that transition.

## Codex marketplace

Fetch a shallow copy of `release` in a staging directory outside skill
discovery. Confirm that the configured Engineering Compass Git marketplace
tracks `release` at the publisher. Refresh that marketplace:

```sh
codex plugin marketplace upgrade engineering-compass --json
```

Read the result, the enabled plugin in `codex plugin list --json`, and the
new installed package from the same Codex configuration. Verify that
`plugin.json` and the complete `skills/` contents match the staged snapshot.
Read the migration instructions from those verified files even if the current
chat started with the previous skill. A fresh Codex chat discovers the updated
package.

## Git installation

Confirm that the discoverable checkout tracks the publisher's `release`
branch. Preserve local work. In a clean checkout, fetch the branch and
fast-forward to that exact fetch:

```sh
git fetch --no-tags origin refs/heads/release
git merge --ff-only FETCH_HEAD
```

Verify that the installed checkout and the fetched snapshot agree in
`plugin.json` and `skills/`. The branch can deliver an older package in a new
commit, so it still uses a fast-forward. Git ancestry is only needed for
updating the checkout by fast-forward. Migration uses the version and files
in the resulting snapshot.

## Readback

Record the actual installed version and package before preparing repository
changes. If the source, refresh, discovery, or comparison fails, report the
observed state and keep the repository configuration. If `release` changed
during a marketplace refresh, verify one new snapshot against the actual
installation before continuing or retry Update.
