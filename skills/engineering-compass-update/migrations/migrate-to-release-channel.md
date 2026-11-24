```json
{"depends_on": []}
```

# Move the installation to the release channel

## Applicability

Apply once per user installation that uses the default-branch marketplace,
separate downloaded or cloned skill folders, or a symlinked Git bundle.
Run this explicitly. A project migration can offer this procedure as a
separate action. Users with an older package can open this record directly
from the GitHub Release that introduces it.

Keep the existing installation type by default. Move the marketplace to
`release`, or move an older Git or standalone installation to a direct Git
clone. Switching types requires an explicit choice. Preserve an intentionally
pinned installation unless its user requests a switch. A fresh installation
starts at preparation and has no old artifacts to clean up.

## Capture and prepare

Record the active installation, its version, Git source or marketplace
registration, and exact discovery paths. Check the documented candidates
against the actual installation.

- `~/.agents/skills/engineering-compass`, `engineering-compass-setup`, and
  `engineering-compass-update` under the user skills directory.
- `~/.agents/skills/engineering-compass-bundle`. Inspect whether it is a
  symlink, and resolve its target and common Git directory independently.
- The `engineering-compass` marketplace registration and installed package.
  Inspect them with `codex plugin marketplace list --json` and
  `codex plugin list --json`.
- `~/.local/share/engineering-compass` and any linked release worktrees.
  A worktree can depend on the shared store after its discovery link is gone.

Capture the approved version and effective rule source for every affected
project. A legacy project without a proven version needs its active source
preserved before a refresh. Use Setup's explicit adoption audit when that
source is uncertain. Keep the legacy binding only when it identifies the
rules actually in force. Record the relevant `refs/engineering-compass/approved/`
refs and their objects, the common store, and any local edits, commits,
configuration or untracked files. Preserve data and refs with uncertain
ownership or consumers.

Fetch the publisher's `refs/heads/release` into a clean staging checkout
outside live skill discovery. Use its `.agents/plugins/marketplace.json` to
find the publisher URL and exact version tag for Engineering Compass. Keep
the fetched channel snapshot fixed. Check that the tag has a published
GitHub Release and that the tagged `plugin.json`, release-map version and
channel selection agree. Compare `skills/` and `plugin.json` with the tag in
Git. If the channel or tag cannot be verified, retain the active installation.

### Prepare a marketplace installation

Test the commands in an isolated Codex configuration before replacing the
live marketplace registration:

```sh
codex plugin marketplace add reutenkoivan/engineering-compass --ref release
codex plugin add engineering-compass@engineering-compass
```

Keep or prepare the approved rule store at `~/.local/share/engineering-compass`.
For a route change, transfer and verify all affected refs and their objects
if the recipient store differs. Verify discovery of the intended plugin
skills and the rule source using the namespaced skill invocation. Record
the previous registration and prepare a verified recovery source that
installs the captured package with the same marketplace and plugin names.
Use the original source if it still resolves that package, its published
tag, or a retained local marketplace root verified against the captured
package. Test that recovery source in isolation before changing a live
registration.

### Prepare a Git installation

Clone into a staging directory outside live discovery. For a fresh
installation with a vacant destination, use these commands.

```sh
mkdir -p "$HOME/.agents/skills"
git clone --branch release https://github.com/reutenkoivan/engineering-compass.git \
  "$HOME/.agents/skills/engineering-compass-bundle"
```

For a migration, use the staged clone as the new checkout. Fetch the approved
refs and reachable objects it needs from the verified old store. Fetch
each ref into a temporary ref or `FETCH_HEAD` first, verify its binding,
then create the approved ref in the new checkout. An existing approved ref
must already agree. Transfer a proven legacy binding when needed. Verify
rule reads from the new checkout and test discovery with the standalone
skill names.

## Switch, verify and clean up

Agree on affected routes. If a project's explicit skill selector changes,
approve that edit with the project owner and keep its approved rules.
Stop if a still-active old route cannot be safely detached. Move superseded
filesystem discovery entries outside discovery while retaining their
recovery copies.

For a Git destination, remove the old marketplace registration if switching
from the plugin and its recovery source is verified. Place the staged Git
checkout at the now-vacant `~/.agents/skills/engineering-compass-bundle`.

For a verified marketplace replacement, switch the live registration
with the following commands after preparing its recovery source.

```sh
codex plugin marketplace remove engineering-compass
codex plugin marketplace add reutenkoivan/engineering-compass --ref release
codex plugin add engineering-compass@engineering-compass
```

If installing a marketplace from Git and its name is vacant, use the
two add commands after detaching the old Git discovery entries.

Open a fresh Codex chat after the actual switch. Verify the intended source
and the three skill entries. Compare the installed version and package
with the verified staged tag. If the channel moved during the switch,
verify the new candidate before proceeding. Verify normal rule loading
and required resources in each affected project. Check separately any
project whose approved rules are newer than the installed package during
a rollback. If Git readback fails, move the replacement checkout out of
discovery, put the retained entries back and verify the old route.
For marketplace recovery, remove the replacement registration
if it was added, then add the previously verified recovery source and run
`codex plugin add engineering-compass@engineering-compass`. Read back the
restored package and rules, and report the failed check.

After successful readback, present the exact superseded paths or marketplace
entries to remove and obtain approval for that list. Recheck ownership, Git
status, common stores and remaining consumers immediately before deletion.
Unlink a confirmed retired symlink by its own path. Use Git's worktree
removal for a retired linked worktree after checking its state. Remove
confirmed obsolete installations and managed registration or cache entries
only when their replacement and recovery evidence are available. Preserve
user changes, unknown artifacts and stores still needed by any route.

On retry, identify the active route, previous verification and leftover
artifacts before continuing. Recheck ownership and approval for anything
still eligible for removal. Report installation, rule readback and cleanup
separately. Report deferred cleanup with the retained paths and reasons
when the new route works and the superseded discovery entry is detached.

## Use the channel

Update between Codex sessions. For the marketplace run
`codex plugin marketplace upgrade engineering-compass`. For a clean Git
checkout tracking `release` use this command.

```sh
git -C "$HOME/.agents/skills/engineering-compass-bundle" pull --ff-only
```

A shared rollback reaches both paths on their next refresh. For a local pin,
select an exact published tag with the marketplace's `--ref` or switch the
clean Git checkout to that tag. Return to the `release` source to resume
channel updates. During a rollback to an older package, stage this record's
introducing tag `v0.2.0` outside live discovery when you need a compatible
Setup or Update. Give Codex the staged
`skills/engineering-compass-setup/SKILL.md` or
`skills/engineering-compass-update/SKILL.md` path explicitly. Those procedures
select the channel's tag and preserve the approved rules of existing projects.
