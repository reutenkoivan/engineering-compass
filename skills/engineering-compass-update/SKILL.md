---
name: engineering-compass-update
description: Review and migrate an adopted repository between published Engineering Compass versions.
---

# Engineering Compass update

Locate the selected repository and its root `AGENTS.md`. Send repositories
without an adoption entry to the installed Engineering Compass Setup skill.

Follow [migration-workflow.md](migration-workflow.md) for a repository
migration. Capture its approved version and use the selected tag's release
map and migration records to build the plan and obtain concrete decisions.
Prepare and verify approved changes in an isolated Git worktree. Report the
candidate and whether the operator has activated it in the working checkout.
Carry out the workflow directly as the agent using document reads and native
Git or Codex operations. Keep bundled scripts and language runtimes outside
the client workflow.

For an explicit installation transition or a detected legacy installation,
offer the separate [delivery migration](migrations/migrate-to-release-channel.md).
