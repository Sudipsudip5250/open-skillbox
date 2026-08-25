# Skill Taxonomy and Maintenance Guide

Agent Skill Kit is organized as a catalog of independent `user-<kebab-case>` skills. The taxonomy is a discovery aid, not a permission boundary: a task may compose skills from several categories, while the orchestrator should load the smallest set that covers the work.

## Categories

| Category | Typical scope | Example modules |
|---|---|---|
| Meta and orchestration | Request classification, context, planning, delivery, and skill authoring | `user-task-orchestrator`, `user-context-engineering` |
| Software and quality | Implementation, review, debugging, testing, migrations, and interfaces | `user-software-engineering`, `user-debugging-testing` |
| Frontend and experience | Browser interfaces, styling, accessibility, motion, visual quality, and 3D | `user-react-development`, `user-responsive-design` |
| Security and trust | Authorized security, identity, privacy, secrets, provenance, and risk review | `user-web-application-security`, `user-threat-modeling` |
| Data and systems | Data pipelines, analysis, ML evaluation, architecture, networks, OS, and embedded systems | `user-data-engineering-pipelines`, `user-systems-design-architecture` |
| Mathematics | Foundations, algebra, calculus, linear algebra, probability, statistics, discrete math, units, and modeling | `user-differential-calculus`, `user-linear-algebra` |
| Science | Physics, chemistry, biology, earth systems, experiments, and scientific visualization | `user-physics-mechanics`, `user-experimental-design-lab-methods` |
| Education and research | Tutoring, lesson design, assessment practice, literature review, citations, and evidence synthesis | `user-tutoring-socratic-method`, `user-literature-review-systematic` |
| Product and operations | Discovery, PRDs, roadmaps, support, SLOs, postmortems, capacity, backups, rate limits, feature flags, and decision logs | `user-prd-spec-writing`, `user-sre-error-budgets-slos` |
| Writing and creative production | Technical blogs, RFCs, changelogs, stakeholder updates, localization, video, brand, podcast, slides, image prompts, and communication | `user-technical-blog-deep-dive`, `user-video-script-storyboard` |
| Agent meta and portability | Skill authoring, quality review, composition, evaluation, context packaging, starter packs, and host-neutral export | `user-skill-authoring`, `user-skill-quality-review` |
| Education and careful literacy | Learning design, health information, personal finance concepts, privacy-policy literacy, and regulated-domain boundaries | `user-health-information-literacy`, `user-personal-finance-concepts` |
| Product and communication | Product discovery, documents, writing, spreadsheets, finance, monetization, and media rights | `user-product-discovery`, `user-documentation-communication` |

## Naming and overlap policy

Use the `user-` prefix followed by a stable, descriptive kebab-case name for canonical directories and frontmatter. Names should describe the task or method rather than a temporary vendor, model, person, or private project. The generated catalog exposes a clean alias without the `user-` display prefix through `docs/SKILL_ALIASES.json`; do not create duplicate unprefixed directories. Preserve an existing name when revising behavior. If two skills overlap, prefer a surgical update, an explicit handoff, or a narrowly scoped new module rather than a blind merge.

Broad routing skills should classify and hand off; they should not absorb the detailed procedure of every specialist. Domain skills should explain their own method and checks while composing with the orchestrator, research, data, security, or delivery modules as needed. A new skill is justified when its trigger, failure modes, evidence needs, or safety boundary would otherwise be unclear inside an existing module.

## New-skill checklist

A proposed skill should answer the following questions in its `SKILL.md`:

1. What recurring request activates it, and what similar requests do not?
2. What inputs, assumptions, constraints, versions, or permissions matter?
3. How does the agent classify the task and select a method?
4. What actionable workflow, worked reasoning, or artifact procedure should it follow?
5. How does it verify correctness, reproducibility, safety, accessibility, or operational readiness?
6. What common errors and non-goals should prevent misuse or scope creep?
7. What should the handoff contain, and which neighboring skills should be composed?
8. Which public sources support version-sensitive or domain-specific guidance?

## Progressive disclosure and public safety

Keep the core file concise and put optional scripts, references, or assets in the skill directory only when they provide real reuse. Never commit credentials, account-level Knowledge, personal preferences, private research, private repository instructions, or hardcoded sandbox paths. Security, laboratory, regulated, financial, and external-action workflows must make authorization and professional-review boundaries explicit. The canonical `SKILL.md` is host-neutral; use [cross-agent compatibility guidance](CROSS_AGENT_COMPATIBILITY.md) and the explicit exporter instead of duplicating or rewriting skills for each host. Run the generator and validator before proposing a change.
