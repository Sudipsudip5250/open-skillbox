# Agent Skill Kit project guidance

This repository is a public, modular skill catalog. The canonical procedural modules live under `skills/user-<kebab-case>/SKILL.md`; consult `docs/SKILL_INDEX.md` to discover them.

For substantial tasks, begin with `user-task-orchestrator`, then load the smallest relevant domain and verification skills. Preserve existing skills and prefer surgical extensions over duplicates. Do not copy private project knowledge, credentials, account-level memory, or sensitive research into this repository.

Security work is authorized-defensive only: establish ownership or documented authorization, scope, environment, rate limits, evidence handling, and stop conditions before active testing. Refuse unauthorized access, credential theft, destructive exploitation, persistence, evasion, anti-forensics, jailbreak or safeguard-bypass requests, and third-party watermark or DRM removal.

Math, science, education, health, legal, and finance modules are informational and must state assumptions, uncertainty, verification, and professional-review boundaries where relevant. Media workflows use owned, licensed, or permitted assets.

Run these checks after changes:

```bash
python scripts/generate_skill_index.py
python scripts/validate_skills.py
python scripts/check_security_quality.py
python scripts/export_skills.py --pack web-app-team --destination /tmp/open-skillbox-smoke-test
```

Host-specific setup is documented in [`docs/CROSS_AGENT_COMPATIBILITY.md`](docs/CROSS_AGENT_COMPATIBILITY.md). The canonical `SKILL.md` content is portable, but discovery paths, frontmatter support, permissions, and context limits vary by host.
