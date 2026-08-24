# Agent Skill Kit

**Agent Skill Kit** is a curated, modular, open-source **skill powerhouse** for AI agents and coding assistants. It is a library of focused `SKILL.md` workflows that help an agent classify a request, load only the relevant guidance, work from evidence, verify its output, and keep security, privacy, and project boundaries explicit.

The repository deliberately uses many small skills rather than one oversized instruction file. Each module has a trigger-oriented description, a bounded workflow, verification guidance, non-goals, and a handoff format. The generated [skill index](docs/SKILL_INDEX.md) is the catalog and source of truth for discovery.

## Coverage map

| Area | Representative capabilities |
|---|---|
| Orchestration and context | Task routing, context engineering, project delivery, knowledge boundaries, cost-efficient execution |
| Software and quality | Software engineering, code review, debugging, testing, migrations, Git, APIs, TypeScript, JavaScript/Node.js |
| Frontend and experience | React, CSS/Tailwind, responsive design, accessibility, browser testing, UI/UX, motion, visual quality, Three.js, games |
| Security and trust | Application, web, database, identity, cloud, secrets, AI security, authorized testing, vulnerability detection, provenance |
| Data and systems | Data analysis, data engineering, machine-learning evaluation, systems design, architecture, networking, operating systems, embedded/IoT |
| Mathematics | Foundations, algebra, functions, trigonometry, precalculus, limits, differential and integral calculus, multivariable calculus, linear algebra, probability, statistics, discrete math, units, and modeling |
| Science | Mechanics, electricity and magnetism, waves and optics, thermodynamics, stoichiometry, bonding, cell and molecular biology, genetics, evolution, earth and environmental systems, experimental design, and scientific visualization |
| Education and research | Socratic tutoring, curriculum and lesson planning, exam practice, systematic literature review, citation management, scientific research, and fact-checking |
| Product and communication | Product discovery, documentation, blog and SEO writing, spreadsheets, finance, monetization, payments, media rights, and professional communication |

Browse the complete grouped catalog in [docs/SKILL_INDEX.md](docs/SKILL_INDEX.md). The index is generated from the skill directories and is checked in continuous integration so links and catalog entries stay synchronized.

## Installation and composition

Each skill is self-contained. Copy the selected `skills/user-<kebab-case>/` directory into the skill location supported by your agent, or copy its `SKILL.md` into the corresponding project or user-level skills directory. Keep the directory and `SKILL.md` together when the host supports directory-based discovery.

Install the smallest useful subset. A typical workflow begins with `user-task-orchestrator`, adds one or two domain skills, and then composes focused verification, security, research, or delivery skills only when the task requires them. Do not enable the full catalog by default: progressive disclosure reduces ambiguity and makes it easier to inspect which guidance influenced a result.

Discovery paths and frontmatter support vary across Manus, Claude, Cursor, Codex, Gemini, and other agent hosts. This repository preserves the common `SKILL.md` format, but compatibility is not a universal guarantee; check the target host’s current skill-loading documentation and test a small subset before broad deployment.

Skills provide procedures, not private knowledge. Keep project facts, user preferences, credentials, account-level Knowledge, and sensitive research artifacts in the host’s separate protected context system. Do not commit secrets or private project instructions to this public repository.

## Safety and responsible use

This project supports authorized development, education, research, privacy protection, and production readiness. It does not provide instructions for credential theft, unauthorized access, destructive exploitation, persistence, evasion, anti-forensics, watermark removal from third-party media, copyright bypass, invalid advertising traffic, deceptive monetization, prompt-injection bypass, or safeguard circumvention.

Security and infrastructure skills require an explicitly authorized target, defined scope, a safe environment where possible, rate limits, evidence handling, and responsible reporting. Science and education skills are informational and must not be treated as personal medical, legal, financial, or other regulated professional advice. Experimental skills remain at a safe planning and analysis level and do not replace institutional review, laboratory controls, or qualified supervision. Tutoring skills support complete reasoning and learning rather than answer-only exam circumvention.

## Quality principles

Skills should be concise, actionable, version-aware, evidence-led, and independently useful. A new module should have a distinct trigger, explicit overlap analysis, clear assumptions and non-goals, verification checks, safe handoff, and authoritative references for time-sensitive guidance. Existing skills should be preserved and improved surgically rather than merged or deleted merely to reduce the count.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. The [taxonomy guide](docs/TAXONOMY.md) explains categories, naming, overlap policy, and the new-skill checklist. Use the issue templates when proposing a focused module or a math/science/education skill.

## License

Released under the [MIT License](LICENSE).
