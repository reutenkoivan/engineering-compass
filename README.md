# Engineering Compass

Engineering Compass routes web development work to the engineering rules that
apply, from defining product behavior to delivering and verifying changes.

## Install for your user in Codex

Run this command to install every skill in `skills/` together.

```sh
mkdir -p "$HOME/.local/share" "$HOME/.agents/skills" &&
  git clone https://github.com/reutenkoivan/engineering-compass.git \
    "$HOME/.local/share/engineering-compass" &&
  ln -s "$HOME/.local/share/engineering-compass/skills" \
    "$HOME/.agents/skills/engineering-compass-bundle"
```

Codex follows the link and makes the skills available across repositories.
See the [Codex skill discovery documentation](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).

For an earlier installation, move the old `engineering-compass` and
`engineering-compass-setup` directories out of `~/.agents/skills` before running
the command. Keep them until the new installation works in Codex.

## Update the installation

```sh
git -C "$HOME/.local/share/engineering-compass" pull --ff-only
```

Skills added to `skills/` become available with the same update.

## Adopt in a repository

Invoke `$engineering-compass-setup` from the repository you want to prepare.
It follows the [repository setup procedure](skills/engineering-compass/setup.md)
to audit existing policy, add the adoption entry to the root `AGENTS.md`, and
verify the result. You can also invoke it to verify or repair an existing adoption.

If your repository links into a checkout of this project, point its `AGENTS.md`
entry and rule links to `skills/engineering-compass/` inside that checkout.
