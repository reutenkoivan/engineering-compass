# Engineering Compass

Engineering Compass is an agent skill that routes web development work to the
engineering rules that apply, from defining product behavior to delivering and
verifying changes.

## Install for your user in Codex

```sh
git clone git@github.com:reutenkoivan/engineering-compass.git "$HOME/.agents/skills/engineering-compass"
```

This makes `$engineering-compass` available across repositories. See the
[Codex skill discovery documentation](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).

## Adopt in a repository

With `$engineering-compass` installed, send the following prompt in Codex to
install the companion skill for your user.

```text
$skill-installer Install .skills/engineering-compass-setup from reutenkoivan/engineering-compass into ~/.agents/skills.
```

Invoke `$engineering-compass-setup` from the repository you want to prepare.
It follows the [repository setup procedure](setup.md) to audit existing policy,
add the adoption entry to the root `AGENTS.md`, and verify the result. You can
also invoke it to verify or repair an existing adoption.
