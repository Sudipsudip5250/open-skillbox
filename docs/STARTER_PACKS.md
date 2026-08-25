# Starter Packs

Starter packs are curated subsets, not separate products or duplicated skills. Use the exporter with an explicit destination selected from the target host’s current documentation.

| Pack | Intended audience | Included focus |
|---|---|---|
| `web-app-team` | Web product teams | Orchestration, software, React, TypeScript, APIs, browser testing, accessibility, security review, debugging |
| `solo-indie-hacker` | Small product teams and individual builders | Delivery, product discovery, PRD writing, roadmap prioritization, frontend, monetization, spreadsheet modeling |
| `security-review` | Authorized defensive reviews | ROE, attack surface, authorized testing, findings, remediation/retest, risk review, vulnerability detection |
| `student-stem` | STEM learning | Orchestration, Socratic tutoring, mathematics, mechanics, chemistry, units, exam practice |
| `content-creator` | Lawful content production | Technical blogging, video scripting, slide structure, podcast cleanup, brand application, image prompting, localization |

## Example export

```bash
python scripts/export_skills.py --pack web-app-team --destination /path/to/host/skills
python scripts/export_skills.py --pack student-stem --destination /path/to/host/rules --flatten
```

Keep the canonical repository copy as the source of truth. If a host requires a transformed rule format, preserve the original `SKILL.md` in a reviewable location and record the transformation, host version, date checked, and test result.
