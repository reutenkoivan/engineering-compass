---
name: engineering-compass-setup
description: Adopt Engineering Compass in a repository or verify and repair its existing integration.
---

# Engineering Compass setup

When asked to audit a staged target, use this Setup procedure with the
target's Compass rules. Read the current repository policy as the starting
state and keep the existing adoption in force until a transition is approved.

1. Locate the target repository root and read its `AGENTS.md`, when present,
   and the local policy it routes to. For an existing adoption, resolve the
   Engineering Compass `SKILL.md` identified by the root entry. For first
   adoption, prefer the user-installed base Compass skill when it is
   discoverable in each environment that will rely on the entry. If a required
   environment cannot resolve the intended copy, agree with the user on
   installing it or using a repository copy before editing the integration.
2. Use [setup.md](setup.md) to establish the rule source, including the Git
   checkout for a plugin installation. Read the Compass rules from the exact
   revision under review. On first adoption, audit all rule sets. On a repeat
   run, verify the effective integration and report a valid setup without
   editing. When a repair is needed, audit the affected rules before editing.
   For a change to an already adopted revision, use the installed Engineering Compass Update skill.
3. Treat a setup request as authorization for compatible configuration within
   its scope. Present conflicts, proposed local differences, and effective
   changes to the task graph for a user decision before the affected edits.
   Reuse exact decisions the user has already supplied.
4. Apply the authorized setup and verify the result as specified in `setup.md`.
   Report which copy the root entry resolves, what was applied and verified,
   and any outstanding decisions or environments still to verify.
