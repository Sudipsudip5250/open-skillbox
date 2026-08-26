---
name: user-git-workflow
description: Manage Git repositories safely during development, debugging, refactoring, reviews, and releases. Use for branches, commits, worktrees, rebases, merges, pull requests, conflict resolution, history inspection, or repository cleanup.
---

# Git Workflow

## Quick start

Use this skill when the request matches **Manage Git repositories safely during development, debugging, refactoring, reviews, and releases. Use for branches, commits, worktrees, rebases, merges, pull requests, conflict resolution, history inspection, or repository cleanup.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Before changing files

Inspect repository status, current branch, remotes, recent history, project instructions, and uncommitted work. Never overwrite or discard user changes without explicit approval. Identify the correct repository and avoid mixing unrelated projects.

## Working method

- Use a branch or isolated worktree for meaningful changes when the project workflow supports it.
- Keep changes atomic and logically focused. Separate refactoring, dependency upgrades, generated files, and behavior changes when practical.
- Prefer small commits that compile or pass focused tests. Write imperative, searchable commit messages that explain what changed and why.
- Review the diff and staged file list before every commit. Never commit secrets, credentials, local state, build artifacts, generated caches, or unrelated files.
- Resolve conflicts by understanding both sides and re-running focused tests; do not choose one side blindly.
- Before rebase, reset, clean, force-push, merge, delete, or publish, explain the impact and confirm when the action is destructive or irreversible.
- Use pull requests or patches for review when appropriate. Include verification evidence and known limitations.

## Completion checks

Run status, diff, relevant tests, build/type/lint checks, and repository-specific validation. Confirm the working tree state and report the branch, commits, files changed, checks run, and any uncommitted or intentionally preserved work.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **git-workflow**, use this compact record:

```text
Request: [the concrete task and intended outcome]
Scope and inputs: [files, data, versions, permissions, audience]
Classification: [task type, risk, and relevant branch]
Method: [selected procedure and why alternatives were rejected]
Steps: [ordered actions with intermediate outputs]
Result: [answer or artifact, separated from interpretation]
Checks: [independent verification, edge cases, safety, accessibility, or reproducibility]
Handoff: [files, owners, limitations, and next action]
```

Do not fill this pattern with invented evidence. If the task is underspecified, keep placeholders visible or ask for the missing decision.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If the failure is not reproducible, capture environment and logs, reduce the case, state uncertainty, and avoid speculative rewrites or destructive recovery steps. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For software and systems, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

run the narrowest relevant tests, type/build checks, runtime reproduction, compatibility checks, rollback review, and an inspection of the final diff for unintended behavior. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.
