# Naming and Migration

## Decision

Agent Skill Kit keeps the existing `user-<kebab-case>` directory and frontmatter IDs as **legacy-compatible canonical paths**. These names are already published, linked by the index, referenced by routing, and likely copied by users. Removing the prefix or mass-renaming directories would break installs, links, scripts, and downstream agent configurations.

The catalog now exposes a clean **portable alias** by removing only the `user-` display prefix. For example:

| Portable alias | Legacy ID and path |
|---|---|
| `sql-analytics-workflows` | `user-sql-analytics-workflows` → `skills/user-sql-analytics-workflows/SKILL.md` |
| `security-findings-report` | `user-security-findings-report` → `skills/user-security-findings-report/SKILL.md` |
| `task-orchestrator` | `user-task-orchestrator` → `skills/user-task-orchestrator/SKILL.md` |

The generated [skill index](SKILL_INDEX.md) shows both forms, and [SKILL_ALIASES.json](SKILL_ALIASES.json) is the machine-readable mapping.

## Rules for new skills

New repository modules should continue using `user-<kebab-case>` for directory and frontmatter compatibility. Their portable alias is automatically derived for display and export. Do not create a second physical directory only to remove the prefix.

## Future major migration

A future major release could add unprefixed directories only if the repository provides redirect metadata, duplicate-path compatibility, migration tooling, updated links, and a deprecation window. Until then, the alias approach gives users the clean name they want without removing or breaking existing skills.
