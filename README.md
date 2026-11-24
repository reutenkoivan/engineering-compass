# Engineering Compass

Engineering Compass routes web development work to the engineering rules that
apply, from defining product behavior to delivering and verifying changes.

## Install the Codex plugin

Add the GitHub marketplace and install Engineering Compass. The plugin includes
the Compass, Setup, and Update skills.

```sh
codex plugin marketplace add reutenkoivan/engineering-compass --ref release
codex plugin add engineering-compass@engineering-compass
```

To test from a local checkout, use `codex plugin marketplace add /path/to/engineering-compass`
in the first step. In the desktop app, choose the Engineering Compass marketplace
in the Plugins Directory and install the plugin. Start a new chat after installation.

## Adopt in a repository

Invoke `$engineering-compass:engineering-compass-setup` from the repository
you want to prepare. A standalone installation exposes `$engineering-compass-setup`.
It follows the [repository setup procedure](skills/engineering-compass-setup/setup.md)
to audit existing policy, record the active global version in the root
`AGENTS.md`, and verify automatic use of the rules. Run Setup again to verify
or repair an integration using the installed version.

## Update an adopted repository

Invoke `$engineering-compass:engineering-compass-update` in the repository
you want to update. A standalone installation exposes
`$engineering-compass-update`. Update synchronizes the global installation
with `release` and applies the repository migration. Other adopted
repositories check their configured version when Compass next runs there.
