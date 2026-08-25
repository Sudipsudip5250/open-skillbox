# Cross-Agent Compatibility

Agent Skill Kit has a **portable canonical core**: every module lives in `skills/user-<kebab-case>/SKILL.md` with YAML `name` and `description` frontmatter. This format is intentionally simple so it can be copied into different agent and coding-assistant environments.

> Compatibility means the same public skill content can be discovered and loaded through a documented setup path. It does not mean every host has identical native skill discovery, frontmatter support, permissions, context limits, or tool behavior.

## Recommended portable workflow

1. Clone or download this repository.
2. Choose the smallest starter pack or skill subset for the task.
3. Copy the canonical skill directory, preserving `SKILL.md` and its directory name.
4. If a host does not support directory-based skills, copy the `SKILL.md` content into the host’s documented rule, instruction, prompt, or project-memory location without changing safety boundaries.
5. Load `AGENTS.md` where the host supports repository instruction files; otherwise use the equivalent project instruction mechanism.
6. Begin with `user-task-orchestrator` and add only the domain and verification modules needed for the task.
7. Run a small representative task and confirm that the host actually loaded the intended skill before broad deployment.

## Host setup matrix

The entries below are **setup patterns**, not claims that the repository has been officially tested or integrated by each vendor. Host behavior and documentation can change; verify the current host instructions before installation.

| Host or family | Recommended integration pattern | Important caveat |
|---|---|---|
| Manus | Add selected skill directories through the host’s skill mechanism; keep project knowledge separate from public skills. | Manus may load metadata and bodies through its own progressive-disclosure system. |
| Claude Code | Use the repository’s `CLAUDE.md` pointer and copy selected modules into the project’s documented skills or instructions location. | Verify the current Claude Code project and user instruction conventions. |
| Codex | Keep `AGENTS.md` at repository root and copy selected modules into the documented project instruction or skills location. | `AGENTS.md` is a routing pointer; it is not a guarantee of automatic `SKILL.md` loading. |
| Cursor | Use the provided `.cursor/rules/open-skillbox.mdc` pointer or copy selected content into the current Cursor rules mechanism. | Verify rule file format, scopes, and frontmatter in the installed Cursor version. |
| Replit | Copy selected modules into the project’s documented agent/instruction configuration and retain `AGENTS.md` as human-readable guidance. | Replit agent configuration and permissions are host-managed and may differ by workspace. |
| Kiro | Use the host’s documented steering or specification files and copy only the selected skill content. | Do not assume Claude/Cursor rule syntax is accepted unchanged. |
| Kilo | Use its documented project rules or skills directory; begin with a small subset. | Verify current discovery path and whether frontmatter is preserved. |
| Antigravity | Use its documented workspace instruction or skill import path and the generic exporter for canonical copies. | Treat the profile as provisional until the host’s current documentation confirms the path. |
| OpenCode | Use repository instruction files plus an explicit exported subset in the host’s documented location. | Verify current config names, scopes, and precedence rules. |
| Mimo Code | Use its documented project instructions or skill import flow; retain canonical skill text. | Verify current format and context limits before bulk loading. |
| Other or future agents | Use the generic exporter, copy `SKILL.md`, and map the content into the host’s official instruction mechanism. | Record the tested path in a project-local note rather than assuming compatibility. |

## Export helper

The repository includes `scripts/export_skills.py`. It copies selected canonical directories or flattened `SKILL.md` files to an explicit destination and never edits the source skill. Examples:

```bash
python scripts/export_skills.py --skill user-task-orchestrator --skill user-sql-analytics-workflows --destination /path/to/target/skills
python scripts/export_skills.py --pack web-app-team --destination /path/to/target/skills
python scripts/export_skills.py --skill user-task-orchestrator --destination /path/to/target/rules --flatten
```

Use an explicit destination chosen from the target host’s current documentation. Do not commit credentials, private project instructions, or generated host-specific secrets.

## Compatibility reporting

When documenting a new host, record the host version or date checked, discovery path, frontmatter behavior, precedence rules, context limits, permission model, test task, observed result, and rollback or removal path. If a host cannot load the canonical format directly, keep the repository skill unchanged and document the adapter or copy step instead.
