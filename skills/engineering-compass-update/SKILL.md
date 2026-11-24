---
name: engineering-compass-update
description: Review and migrate an adopted repository to a published Engineering Compass revision.
---

# Engineering Compass update

Locate the selected repository and its root `AGENTS.md`. Send repositories
without an adoption entry to the installed Engineering Compass Setup skill.

Follow [migration-workflow.md](migration-workflow.md). Capture the active
release before refreshing a bundle or changing an adoption. Read the target's
[release map](release-map.md) and the migration files it selects. Build the
plan from those instructions and obtain decisions on concrete changes.
Prepare and verify approved changes in an isolated Git worktree. Report the
candidate and whether the operator has activated it in the working checkout.
Carry out the workflow directly as the agent using document reads and native
Git or Codex operations. Keep bundled scripts and language runtimes outside
the client workflow.

For a request to refresh the installed skill bundle, use [bundle-refresh.md](bundle-refresh.md).
