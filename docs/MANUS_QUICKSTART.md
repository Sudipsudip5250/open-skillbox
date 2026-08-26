# Manus Quick-Start Guide

Agent Skill Kit is a portable collection of filesystem-based `SKILL.md` packages. This guide shows a safe, small-subset workflow for using the catalog with Manus. The same canonical package can be adapted to other agents; host discovery and permissions may differ.

## 1. Get the repository

```bash
git clone https://github.com/Sudipsudip5250/open-skillbox.git
cd open-skillbox
```

Keep the repository outside private project data when possible. Do not copy credentials, account-level Knowledge, private customer data, or confidential project instructions into the public catalog.

## 2. Choose a starter pack

The five available starter packs are:

| Pack | Best for | Included focus |
|---|---|---|
| `web-app-team` | Web application work | Orchestration, software, React, TypeScript, APIs, browser testing, accessibility, security review, debugging |
| `solo-indie-hacker` | Small product teams | Delivery, discovery, PRDs, roadmap, frontend, monetization, spreadsheet modeling |
| `security-review` | Authorized defensive reviews | Rules of engagement, attack surface, authorized testing, findings, retest, risk, vulnerability detection |
| `student-stem` | STEM learning | Orchestration, Socratic tutoring, math, mechanics, chemistry, units, exam practice |
| `content-creator` | Lawful content production | Technical writing, video, slides, podcast, brand, image prompting, localization |

Start with one pack or two to three individual skills. Loading all 155 modules at once makes routing and review harder.

## 3. Export a pack

The repository includes a deterministic exporter. It copies canonical skill directories without rewriting their content:

```bash
python scripts/export_skills.py \
  --pack web-app-team \
  --destination /path/selected-by-your-manus-setup/skills
```

For a host that accepts one Markdown rule per file, use the flattened form:

```bash
python scripts/export_skills.py \
  --skill user-task-orchestrator \
  --skill user-react-development \
  --destination /path/selected-by-your-manus-setup/rules \
  --flatten
```

Use the destination supported by your current Manus environment. The exporter does not upload, activate, or grant permissions; it only makes an explicit local copy.

## 4. Load the smallest useful sequence

Begin with `user-task-orchestrator`. Add the domain module that owns the main work, then add only the verification, research, accessibility, security, or delivery module required by the acceptance criteria. A typical web change uses:

```text
user-task-orchestrator
user-react-development
user-typescript-development
user-browser-testing
user-accessibility-audit
```

If the task changes authentication, data access, external integrations, deployment, or sensitive content, add the relevant focused security or privacy module and establish authorization before acting.

## 5. Give Manus a useful request

A strong request states the outcome, repository or files in scope, constraints, evidence available, permissions, and definition of done. For example:

> Improve the settings form in this repository. Inspect the existing React and TypeScript patterns first. Keep the public API unchanged, preserve keyboard and screen-reader behavior, and add tests for validation and loading states. Run the existing checks and report files changed, tests run, assumptions, and remaining risks. Do not deploy or modify external services.

The orchestrator should classify this as a scoped frontend and testing task, load the minimum skills, inspect the project, implement a reversible change, verify behavior, and hand off evidence.

## 6. Verify the result

From the repository root, maintainers can verify the source catalog and exporter with:

```bash
python scripts/generate_skill_index.py
python scripts/validate_skills.py
python scripts/check_security_quality.py
python scripts/export_skills.py --pack web-app-team --destination /tmp/open-skillbox-manus-smoke
python scripts/export_skills.py --skill user-task-orchestrator --destination /tmp/open-skillbox-manus-flat --flatten
git diff --check
```

The exporter should create nine directories for `web-app-team` and one flattened Markdown file for the explicit skill test. CI performs the catalog, validator, security, and starter-pack checks on repository changes.

## 7. Keep Manus and private Knowledge separate

Skills are reusable procedures. Project facts, user preferences, private research, credentials, and account-level Knowledge belong in Manus’s protected project or Knowledge context, not in a public skill. When a task depends on private context, state which protected source was consulted without copying its contents into the repository.

## 8. When a task crosses agents

Use [CROSS_AGENT_COMPATIBILITY.md](CROSS_AGENT_COMPATIBILITY.md) to map the canonical package to Claude Code, Codex, Cursor, Replit, Kiro, Kilo, Antigravity, OpenCode, Mimo Code, or another host. Use [NAMING_AND_MIGRATION.md](NAMING_AND_MIGRATION.md) for the clean portable alias and legacy `user-` ID mapping. Confirm the host’s current discovery path, permissions, frontmatter support, and context limits before broad installation.
