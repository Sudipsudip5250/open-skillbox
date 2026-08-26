# Agent-Skill Ecosystem Benchmark

**Checked:** 26 August 2026

This benchmark compares Agent Skill Kit with public skill-format and platform documentation. It uses official sources for platform behavior and treats repository examples as patterns to inspect rather than instructions to copy.

## Findings

| Source | Verified pattern | Implication for Agent Skill Kit |
|---|---|---|
| Vercel Agent Skills documentation [1] | Skills are modular, composable packages installed through a CLI, and the ecosystem advertises compatibility across many agent hosts. | Keep the canonical directory package, provide deterministic export/discovery tooling, and document host caveats honestly. |
| Vercel Labs agent-skills repository [2] | Mature skills use a clear trigger section, domain rules grouped by impact, and optional scripts/references; the repository includes `AGENTS.md`, `CLAUDE.md`, a discovery index, and CI/build tooling. | Add repository-level host pointers, richer task-specific rules, structured resources when valuable, and a machine-readable catalog. |
| Claude Agent Skills documentation [3] | Progressive disclosure is explicit: metadata first, instructions when triggered, and resources/scripts only when needed. Skills are filesystem packages and custom skills differ by product surface. | Do not inflate every `SKILL.md` with textbook content. Improve depth through actionable procedures, examples, checklists, and optional references/scripts. State per-host installation and runtime limits. |
| Cursor Agent Skills documentation [4] | Skills are portable, version-controlled, actionable, and progressive; optional `scripts/`, `references/`, `assets/`, file-path scoping, explicit invocation, and nested discovery are supported. | Preserve the simple common denominator while optionally using host-specific metadata only in adapters. Add path-scoped guidance only where it does not compromise portability. |
| Agent Skills open format [5] | The format is intentionally lightweight and package-oriented. | Keep `SKILL.md` canonical, use descriptive metadata, and avoid vendor lock-in or hidden dependencies. |

## Current catalog assessment

The current catalog’s structure and safety boundaries are strong, but many of the newest modules were generated as approximately 30-line summaries. They are **valid minimum packages**, yet they are not equally strong as long-term operating playbooks because several lack concrete examples, decision tables, reusable templates, failure triage, or reference links.

The correct improvement is not to make every skill long. It is to make every skill **operationally complete for its scope**. A small skill can be high quality when its trigger is precise and its workflow includes the required decision points, expected inputs, verification, failure handling, and handoff. Larger or high-risk skills should use optional references, scripts, templates, or assets so the core body remains progressive and portable.

## House standard for durable skills

Each skill should contain the following where relevant:

1. **Trigger and boundary:** what activates the skill, what does not, and which neighboring skill owns adjacent work.
2. **Inputs and assumptions:** required files, versions, permissions, audience, constraints, and unknowns.
3. **Classification and method selection:** a decision table or short branching rule for choosing the workflow.
4. **Actionable procedure:** numbered steps with stop conditions, approval gates, tool-neutral commands or pseudocode where useful, and an explicit output contract.
5. **Worked pattern:** at least one small illustrative example, schema, checklist, table, or before/after pattern when the domain benefits from it. Do not copy proprietary or textbook material.
6. **Verification:** correctness, reproducibility, safety, accessibility, privacy, cost, or operational checks appropriate to the task.
7. **Failure handling:** common errors, diagnosis, recovery, escalation, and when to stop or hand off.
8. **Composition:** neighboring skills, required input/output handoff, and context-loading guidance.
9. **Resources:** optional `references/`, `scripts/`, `templates/`, or `assets/` only when they provide repeatable value; do not duplicate the core instructions.
10. **Evidence and maintenance:** authoritative sources for version-sensitive claims, source dates, and a maintenance trigger when APIs, standards, or policies change.

## Scope of compatibility claims

The canonical package is portable across hosts that support the Agent Skills pattern or can load Markdown instructions. Native discovery, path scoping, frontmatter extensions, permission models, network access, context limits, and upload mechanisms vary by host. The repository therefore promises:

- stable canonical `SKILL.md` packages;
- clean aliases mapped to legacy IDs;
- deterministic exports, including flattened Markdown when needed;
- starter packs and host-neutral pointers;
- documented setup patterns and validation evidence;
- no claim that all agents behave identically.

## Improvement priority

The first deepening pass should prioritize skills with high operational consequence, high reuse, or high risk: orchestration/context, software/debugging/testing, security/privacy, data/ML, product/reliability, document/media production, and education/regulated-literacy boundaries. Low-risk explanatory skills can remain shorter if they meet the house standard and include clear examples or verification.

## References

[1]: https://vercel.com/docs/agent-resources/skills "Vercel Agent Skills documentation"

[2]: https://github.com/vercel-labs/agent-skills "Vercel Labs agent-skills repository"

[3]: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview "Claude Agent Skills overview"

[4]: https://cursor.com/docs/skills "Cursor Agent Skills documentation"

[5]: https://agentskills.io/home "Agent Skills open format overview"
