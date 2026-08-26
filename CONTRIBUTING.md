# Contributing to Agent Skill Kit

Thank you for helping improve Agent Skill Kit. Contributions should make an agent more reliable, more efficient, safer, or better at a clearly defined recurring task. The project favors **small, composable, public-safe skills** over a single broad instruction file.

## Before proposing a skill

Search [docs/SKILL_INDEX.md](docs/SKILL_INDEX.md), the existing directories, and [docs/TAXONOMY.md](docs/TAXONOMY.md) first. Prefer improving an existing skill when the proposed behavior overlaps substantially. Add a new module only when it has a distinct trigger, audience, method, and handoff. Do not delete or rename large groups of existing skills without maintainer discussion.

For mathematics, science, tutoring, and research modules, explain the problem classification, method selection, worked or actionable procedure, verification, common failure modes, safety boundary, and handoff. A math skill may provide full worked reasoning, but it must not become an answer-only exam-cheating shortcut. A science skill must distinguish educational modeling from real-world professional or laboratory advice and must not fabricate evidence or unsafe procedures. For defensive security modules, read [docs/SECURITY_USAGE.md](docs/SECURITY_USAGE.md) and include an explicit authorization gate, in-scope and out-of-scope assets, environment preference, rate limits, evidence handling, stop conditions, and a Rules-of-Engagement handoff before active testing.

## Skill requirements

Every skill must be a directory named `user-<kebab-case>` containing `SKILL.md` with YAML frontmatter for `name` and a trigger-oriented `description`. The body should state scope, workflow, verification, assumptions, safety or non-goals, composition or handoff, and the expected deliverable. Keep it concise and progressive; do not copy a textbook, framework manual, proprietary prompt, answer key, or full vendor documentation.

Use authoritative, version-matched sources when behavior, standards, APIs, policies, scientific claims, or educational frameworks can change. Record useful public references in [SOURCES.md](SOURCES.md) and explain how they informed the workflow. Do not include credentials, account-level Knowledge, personal preferences, private research, project-specific secrets, or hardcoded private paths.

## Naming and compatibility

Keep every existing `user-<kebab-case>` directory and frontmatter name unless a maintainer approves a documented migration. The `user-` prefix is the legacy-compatible canonical ID; the generated index and [alias manifest](docs/SKILL_ALIASES.json) provide a cleaner portable display name without breaking existing installs. Do not create duplicate unprefixed directories solely for presentation.

The canonical `SKILL.md` is host-neutral. When contributing host guidance for Manus, Claude Code, Codex, Cursor, Replit, Kiro, Kilo, Antigravity, OpenCode, Mimo Code, or another agent, document the host version/date checked, discovery path, frontmatter behavior, permissions, context limits, test task, and rollback path. Never claim identical native support without verification. Use `scripts/export_skills.py` for explicit copies and keep the source skill unchanged.

## Safety requirements

Security, privacy, payments, monetization, media rights, external actions, and infrastructure skills must state authorization and boundary conditions. Defensive security work must prefer find → verify safely → report → fix → retest and must never infer permission from public visibility. Do not add instructions for unauthorized access, credential theft, destructive exploitation, persistence, anti-forensics, platform-policy evasion, deceptive monetization, copyright bypass, safeguard circumvention, jailbreaks, or prompt-injection bypass. Experimental and physical-system content must remain safe, educational, and subject to appropriate institutional controls and qualified supervision.

## Examples for the expanded catalog

- **Data skill:** a SQL or data-quality module should define grain, schema assumptions, null and duplicate checks, reconciliation, and a handoff to dashboards or ML evaluation.
- **Product skill:** a PRD or roadmap module should separate user outcomes, requirements, acceptance criteria, non-goals, evidence, capacity, and decision ownership.
- **Reliability skill:** an SLO, postmortem, backup, or rollout module should state service scope, stop conditions, rollback, evidence, owner, and verification.
- **Agent-meta skill:** a skill-authoring or quality-review module should check overlap, triggers, progressive disclosure, safety, validation, and downstream composition.

## Local validation

From the repository root, regenerate the public catalog and run the validator:

```bash
python scripts/generate_skill_index.py
python scripts/validate_skills.py
python scripts/check_skill_depth.py
python scripts/check_security_quality.py
python scripts/export_skills.py --pack web-app-team --destination /tmp/open-skillbox-smoke-test
git diff --check

```

If a skill was added, removed, or renamed, include the regenerated `docs/SKILL_INDEX.md` and `docs/SKILL_ALIASES.json`. CI also regenerates the catalog, checks durable depth, and fails if generated artifacts are stale. Review the diff for broken links, copied or private content, vague triggers, duplicated scope, unsafe instructions, missing examples or failure handling, and accidental changes outside the focused contribution. Use [ECOSYSTEM_BENCHMARK.md](docs/ECOSYSTEM_BENCHMARK.md) as the maintenance standard and [MANUS_QUICKSTART.md](docs/MANUS_QUICKSTART.md) to test a representative workflow.

## Pull requests

Use a focused branch and a focused pull request. Explain the problem, affected skills, trigger changes, overlap analysis, sources, validation performed, safety implications, and migration or rollback considerations. For domain skills, include at least one representative input or scenario and the expected verification behavior. Keep unrelated formatting or wording changes out of the pull request.

## Review standard

A contribution is ready when it is useful without hidden context, has a narrow and discoverable trigger, composes cleanly with the orchestrator and neighboring skills, handles failure and verification, respects the safety policy, and is grounded in public evidence where appropriate. Maintainers may request a narrower scope, a clearer handoff, or an improvement to an existing module instead of accepting a new one.
