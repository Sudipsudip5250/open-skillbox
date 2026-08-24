---
name: user-git-workflow
description: Manage Git repositories safely during development, debugging, refactoring, reviews, and releases. Use for branches, commits, worktrees, rebases, merges, pull requests, conflict resolution, history inspection, or repository cleanup.
---

# Git Workflow

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
