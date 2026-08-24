# Contributing to Agent Skill Kit

Thank you for helping improve Agent Skill Kit. Contributions should make an agent more reliable, more efficient, safer, or better at a clearly defined recurring task. The project favors **small, composable, public-safe skills** over a single broad instruction file.

## Before proposing a skill

Search [docs/SKILL_INDEX.md](docs/SKILL_INDEX.md), the existing directories, and [docs/TAXONOMY.md](docs/TAXONOMY.md) first. Prefer improving an existing skill when the proposed behavior overlaps substantially. Add a new module only when it has a distinct trigger, audience, method, and handoff. Do not delete or rename large groups of existing skills without maintainer discussion.

For mathematics, science, tutoring, and research modules, explain the problem classification, method selection, worked or actionable procedure, verification, common failure modes, safety boundary, and handoff. A math skill may provide full worked reasoning, but it must not become an answer-only exam-cheating shortcut. A science skill must distinguish educational modeling from real-world professional or laboratory advice and must not fabricate evidence or unsafe procedures. For defensive security modules, read [docs/SECURITY_USAGE.md](docs/SECURITY_USAGE.md) and include an explicit authorization gate, in-scope and out-of-scope assets, environment preference, rate limits, evidence handling, stop conditions, and a Rules-of-Engagement handoff before active testing.

## Skill requirements

Every skill must be a directory named `user-<kebab-case>` containing `SKILL.md` with YAML frontmatter for `name` and a trigger-oriented `description`. The body should state scope, workflow, verification, assumptions, safety or non-goals, composition or handoff, and the expected deliverable. Keep it concise and progressive; do not copy a textbook, framework manual, proprietary prompt, answer key, or full vendor documentation.

Use authoritative, version-matched sources when behavior, standards, APIs, policies, scientific claims, or educational frameworks can change. Record useful public references in [SOURCES.md](SOURCES.md) and explain how they informed the workflow. Do not include credentials, account-level Knowledge, personal preferences, private research, project-specific secrets, or hardcoded private paths.

## Safety requirements

Security, privacy, payments, monetization, media rights, external actions, and infrastructure skills must state authorization and boundary conditions. Defensive security work must prefer find → verify safely → report → fix → retest and must never infer permission from public visibility. Do not add instructions for unauthorized access, credential theft, destructive exploitation, persistence, anti-forensics, platform-policy evasion, deceptive monetization, copyright bypass, safeguard circumvention, jailbreaks, or prompt-injection bypass. Experimental and physical-system content must remain safe, educational, and subject to appropriate institutional controls and qualified supervision.

## Local validation

From the repository root, regenerate the public catalog and run the validator:

```bash
python scripts/generate_skill_index.py
python scripts/validate_skills.py
git diff --check
```

If a skill was added, removed, or renamed, include the regenerated `docs/SKILL_INDEX.md`. CI also regenerates the index and fails if the checked-in result is stale. Review the diff for broken links, copied or private content, vague triggers, duplicated scope, unsafe instructions, and accidental changes outside the focused contribution.

## Pull requests

Use a focused branch and a focused pull request. Explain the problem, affected skills, trigger changes, overlap analysis, sources, validation performed, safety implications, and migration or rollback considerations. For domain skills, include at least one representative input or scenario and the expected verification behavior. Keep unrelated formatting or wording changes out of the pull request.

## Review standard

A contribution is ready when it is useful without hidden context, has a narrow and discoverable trigger, composes cleanly with the orchestrator and neighboring skills, handles failure and verification, respects the safety policy, and is grounded in public evidence where appropriate. Maintainers may request a narrower scope, a clearer handoff, or an improvement to an existing module instead of accepting a new one.
