# Agent Skill Kit

**Agent Skill Kit** is a curated, modular, open-source **skill powerhouse** for AI agents and coding assistants. It is a library of focused `SKILL.md` workflows that help an agent classify a request, load only the relevant guidance, work from evidence, verify its output, and keep security, privacy, and project boundaries explicit. The catalog now covers **155 skills** across software, data/ML, product, reliability, writing, creative production, education, science, mathematics, and authorized security.

The repository deliberately uses many small skills rather than one oversized instruction file. Each module has a trigger-oriented description, a bounded workflow, verification guidance, non-goals, and a handoff format. The generated [skill index](docs/SKILL_INDEX.md) is the catalog and source of truth for discovery.

## Coverage map

| Area | Representative capabilities |
|---|---|
| Orchestration and context | Task routing, context engineering, project delivery, knowledge boundaries, cost-efficient execution |
| Software and quality | Software engineering, code review, debugging, testing, migrations, Git, APIs, TypeScript, JavaScript/Node.js |
| Frontend and experience | React, CSS/Tailwind, responsive design, accessibility, browser testing, UI/UX, motion, visual quality, Three.js, games |
| Security and trust | Rules of engagement, attack-surface mapping, access-control and API assessment, findings and retesting, application/web/database/identity/cloud security, secrets, AI-agent permissions, vulnerability detection, provenance |
| Data and systems | Data analysis, data engineering, machine-learning evaluation, systems design, architecture, networking, operating systems, embedded/IoT |
| Mathematics | Foundations, algebra, functions, trigonometry, precalculus, limits, differential and integral calculus, multivariable calculus, linear algebra, probability, statistics, discrete math, units, and modeling |
| Science | Mechanics, electricity and magnetism, waves and optics, thermodynamics, stoichiometry, bonding, cell and molecular biology, genetics, evolution, earth and environmental systems, experimental design, and scientific visualization |
| Research and evidence | Systematic literature review, citation management, scientific research, fact-checking, and source-driven development |
| Product and operations | Product discovery, PRDs, roadmap prioritization, support playbooks, SLOs, postmortems, capacity, backups, rate-limit resilience, feature flags, and decision logs |
| Writing and creative production | Technical deep dives, RFCs, changelogs, stakeholder updates, localization, video, brand, podcast, slides, image prompting, documentation, and communication |
| Education and literacy | Tutoring, curriculum, practice, concept maps, health information literacy, personal finance concepts, privacy-policy literacy, and learning design |
| Business and communication | Documentation, blog and SEO writing, spreadsheets, finance concepts, monetization, payments, media rights, and professional communication |

Browse the complete grouped catalog in [docs/SKILL_INDEX.md](docs/SKILL_INDEX.md). The index is generated from the skill directories and is checked in continuous integration so links and catalog entries stay synchronized. It shows both clean portable aliases and legacy-compatible skill IDs; read [docs/NAMING_AND_MIGRATION.md](docs/NAMING_AND_MIGRATION.md) before changing names.

## Starter packs and cross-agent use

Use the curated [starter packs](docs/STARTER_PACKS.md) for a web-app team, solo builder, security review, student STEM workflow, or content creator. The portable [cross-agent compatibility guide](docs/CROSS_AGENT_COMPATIBILITY.md) covers Manus, Claude Code, Codex, Cursor, Replit, Kiro, Kilo, Antigravity, OpenCode, Mimo Code, and future hosts. `AGENTS.md`, `CLAUDE.md`, and `.cursor/rules/open-skillbox.mdc` are lightweight host pointers; the canonical source remains under `skills/`.

Use `scripts/export_skills.py` to copy a selected skill or starter pack to an explicit host destination. Host paths and frontmatter behavior vary, so the repository promises portable content and documented setup—not identical native installation behavior.

## Installation and composition

Each skill is self-contained. Copy the selected `skills/user-<kebab-case>/` directory into the skill location supported by your agent, or copy its `SKILL.md` into the corresponding project or user-level skills directory. Keep the directory and `SKILL.md` together when the host supports directory-based discovery.

Install the smallest useful subset. A typical workflow begins with `user-task-orchestrator`, adds one or two domain skills, and then composes focused verification, security, research, or delivery skills only when the task requires them. Do not enable the full catalog by default: progressive disclosure reduces ambiguity and makes it easier to inspect which guidance influenced a result.

Discovery paths and frontmatter support vary across Manus, Claude Code, Codex, Cursor, Replit, Kiro, Kilo, Antigravity, OpenCode, Mimo Code, Gemini, and other agent hosts. This repository preserves the common `SKILL.md` format and provides portable aliases plus export guidance, but compatibility is not a universal guarantee; check the target host’s current skill-loading documentation and test a small subset before broad deployment.

Skills provide procedures, not private knowledge. Keep project facts, user preferences, credentials, account-level Knowledge, and sensitive research artifacts in the host’s separate protected context system. Do not commit secrets or private project instructions to this public repository.

## Safety and responsible use

This project supports authorized development, education, research, privacy protection, and production readiness. It does not provide instructions for credential theft, unauthorized access, destructive exploitation, persistence, evasion, anti-forensics, watermark removal from third-party media, copyright bypass, invalid advertising traffic, deceptive monetization, prompt-injection bypass, or safeguard circumvention.

Security and infrastructure skills require an explicitly authorized target, defined scope, a safe environment where possible, rate limits, evidence handling, stop conditions, and responsible reporting. Read [docs/SECURITY_USAGE.md](docs/SECURITY_USAGE.md) for a copyable authorization and Rules-of-Engagement statement. Science and education skills are informational and must not be treated as personal medical, legal, financial, or other regulated professional advice. Experimental skills remain at a safe planning and analysis level and do not replace institutional review, laboratory controls, or qualified supervision. Tutoring skills support complete reasoning and learning rather than answer-only exam circumvention.

## Quality principles

Skills should be concise, actionable, version-aware, evidence-led, and independently useful. A new module should have a distinct trigger, explicit overlap analysis, clear assumptions and non-goals, verification checks, safe handoff, and authoritative references for time-sensitive guidance. Existing skills should be preserved and improved surgically rather than merged or deleted merely to reduce the count.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. The [taxonomy guide](docs/TAXONOMY.md) explains categories, naming, overlap policy, and the new-skill checklist. Read [docs/NAMING_AND_MIGRATION.md](docs/NAMING_AND_MIGRATION.md) before renaming anything. Use the issue templates when proposing a focused module or a math/science/education skill.

## License

Released under the [MIT License](LICENSE).
