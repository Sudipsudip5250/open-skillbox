# Contributing to Agent Skill Kit

Thank you for helping improve Agent Skill Kit. Contributions should make an agent more reliable, more efficient, safer, or better at a clearly defined task.

## Before proposing a skill

Search the [skill index](docs/SKILL_INDEX.md) and existing directories first. Prefer improving an existing skill when the proposed behavior overlaps substantially. A new skill should have a distinct task boundary, clear automatic trigger language, and a reason it should not be merged into a broader module.

## Skill requirements

Every skill must be a directory containing a `SKILL.md` with YAML frontmatter containing `name` and `description`. The description should state what the skill does and when it should activate. The body should explain scope, workflow, verification, assumptions, safety boundaries, and handoff expectations.

Keep skills concise and progressive. Do not duplicate complete framework documentation, include secrets, encode user-specific private information, or claim that a version-sensitive recommendation is timeless. Link to authoritative sources when current behavior or policy matters.

## Safety requirements

Security, privacy, payments, monetization, media rights, and external-action skills must state authorization and boundary conditions. Do not add instructions for unauthorized access, credential theft, destructive exploitation, anti-forensics, platform-policy evasion, deceptive monetization, copyright bypass, or safeguard circumvention.

## Pull requests

Use a focused branch and a focused pull request. Explain the problem, affected skills, trigger changes, overlap analysis, evidence or sources, verification performed, safety implications, and migration or rollback considerations. Keep unrelated formatting or wording changes out of the pull request.

Run the repository validation command before submitting:

```bash
python scripts/validate_skills.py
```

Review the generated index when adding, removing, or renaming a skill. Check that links work, frontmatter is valid, and no private or project-specific content was included.

## Review standard

A contribution is ready when it is useful without hidden context, does not create ambiguous automatic triggers, is compatible with the repository’s license, includes evidence for time-sensitive claims, handles failure and verification, and respects the safety policy. Maintainers may request a narrower scope or merge a proposal into an existing skill.
