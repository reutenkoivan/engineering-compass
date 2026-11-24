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

Invoke `$engineering-compass` to start first adoption. Follow the
[repository setup procedure](setup.md) to audit the existing policies and add
the adoption entry to the repository's root `AGENTS.md`.
