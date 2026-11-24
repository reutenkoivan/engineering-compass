# Engineering Compass

Engineering Compass routes web development work to the engineering rules that
apply, from defining product behavior to delivering and verifying changes.

## Install the Codex plugin

Add the GitHub marketplace and install Engineering Compass. The plugin includes
the Compass, Setup, and Update skills.

```sh
codex plugin marketplace add reutenkoivan/engineering-compass
codex plugin add engineering-compass@engineering-compass
```

To test from a local checkout, use `codex plugin marketplace add /path/to/engineering-compass`
in the first step. In the desktop app, choose the Engineering Compass marketplace
in the Plugins Directory and install the plugin. Start a new chat after installation.

For an existing installation, follow the [procedure for switching to the plugin](skills/engineering-compass-update/bundle-refresh.md#switch-to-the-plugin)
to retain approved revisions and retire duplicate skill discovery paths.

## Update the plugin

Capture the repository's [active release](skills/engineering-compass-update/migration-workflow.md#capture-the-current-release-before-updating)
before refreshing the installed skills.

```sh
codex plugin marketplace upgrade engineering-compass
```

Start a new chat to use the updated skills. Repositories continue to use the
rule revisions recorded in their root `AGENTS.md`. Existing symlink installs
can follow the [symlink refresh procedure](skills/engineering-compass-update/bundle-refresh.md#refresh-a-symlink-installation).

## Adopt in a repository

Invoke `$engineering-compass:engineering-compass-setup` from the repository
you want to prepare. A standalone installation exposes `$engineering-compass-setup`.
It follows the [repository setup procedure](skills/engineering-compass-setup/setup.md)
to audit existing policy, record the approved revision in the root `AGENTS.md`,
and verify automatic use of the rules. You can also invoke it to verify or
repair an existing adoption.

For a plugin-backed adoption, Setup uses a persistent Git checkout at
`~/.local/share/engineering-compass` to retain approved rule revisions across
plugin updates. Vendored adoptions use the recorded tree in the project.

For a versioned repository-local route, Setup records a vendored Git tree in
the consumer repository. Review existing links to external checkouts as legacy
routes when adopting a revision.

## Migrate an adopted repository

Invoke `$engineering-compass:engineering-compass-update` to fetch the published
target, see the migration graph, and approve changes. A standalone installation
exposes `$engineering-compass-update`. Update reads
the [release map](skills/engineering-compass-update/release-map.md) and the
Markdown migrations it selects, then prepares and verifies the approved changes.
