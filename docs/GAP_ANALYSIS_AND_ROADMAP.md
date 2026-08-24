# Gap Analysis and Prioritized Roadmap

## Executive summary

The original audit found a public repository of 64 focused skills with strong coverage in software delivery, security, frontend engineering, operations, monetization, research, and media. The largest gaps were chapter-level mathematics, science and technology fundamentals, education workflows, and specialized analytical procedures. The follow-up security brief then required a deeper authorized-testing layer with shared Rules of Engagement, safe reproduction, findings, remediation, and retesting.

Those expansion phases are now implemented. The catalog contains **121 modular skills**, including mathematics from foundations through calculus, linear algebra, probability, statistics, discrete math, differential equations, numerical methods, proof techniques, symbolic computation, and modeling; science and technology fundamentals; education and research-depth workflows; and a 19-skill authorized-defensive-security set. The repository keeps the `skills/user-<kebab-case>/SKILL.md` format, MIT license, public-safe boundaries, generated grouped index, validation scripts, contribution guidance, and CI checks.

## Current coverage and status

| Area | Status | Result |
|---|---|---|
| Meta, orchestration, context, knowledge, and delivery | Expanded | Routing now covers chapter mathematics, science, education, data/ML, systems, diagrams, product, incidents, legal-document literacy, security assessment stages, and personal knowledge-base workflows. |
| Software engineering and quality | Preserved and hardened | General implementation remains separate from code review, debugging, testing, modernization, migration, and focused quality modules. |
| Frontend, design, accessibility, and browser QA | Preserved | Existing specialized boundaries remain intact. |
| Security, privacy, identity, and authorized testing | Expanded | Existing skills have shared authorization gates; seven focused authorized-security modules and a security quality check were added. |
| Data, ML, analytics, and spreadsheets | Expanded | Data engineering, ML training/evaluation, scientific visualization, and advanced spreadsheet modeling are now covered. |
| DevOps, cloud, reliability, and incident response | Expanded | Systems design and incident-response runbooks complement existing infrastructure, CI/CD, observability, and automation skills. |
| Research, science, and evidence | Expanded | Physics, chemistry, biology, earth/environmental systems, experiments, systematic reviews, citation management, and visualization are available. |
| Mathematics | Expanded | Chapter skills now cover the original P0 set and the deferred differential-equations, numerical, proof, symbolic, multivariable, and word-problem extensions. |
| Education and tutoring | Expanded | Socratic tutoring, curriculum and lesson planning, and ethical exam-preparation practice are available. |
| Product, legal literacy, and personal knowledge | Expanded surgically | Product discovery and legal-document literacy were added; the existing knowledge-management skill now includes a personal knowledge-base workflow rather than creating an overlapping module. |

The generated [skill index](SKILL_INDEX.md) is the authoritative catalog. The heuristic [current coverage audit](CURRENT_COVERAGE_AUDIT.md) is retained as an inventory aid; its category counts may overlap because a single skill can serve multiple domains.

## Completed implementation phases

| Phase | Completed work |
|---|---|
| Phase 0 | Audited the baseline, documented overlap and gaps, selected P0/P1/P2 priorities, and corrected public index-link strategy. |
| Phase 1–3 | Hardened the orchestrator, research and engineering boundaries, validator, index generator, existing high-impact skills, and public contribution tooling. |
| Mathematics | Added foundations, algebra, functions, polynomials, exponents/logarithms, trigonometry, precalculus sequences/series, limits/continuity, differential and integral calculus, multivariable calculus, linear algebra, probability, statistics, discrete math, units, and word-problem modeling. Added the later differential-equations, numerical-methods, proof-techniques, and symbolic-computation modules. |
| Science and technology | Added physics mechanics/electricity-waves-thermodynamics, chemistry stoichiometry/structure, biology cell/genetics, earth/environmental systems, experimental design, scientific visualization, computer architecture, networking, operating systems, embedded/IoT, electronics, data engineering, ML training/evaluation, systems design, and Mermaid diagramming. |
| Education and research | Added Socratic tutoring, curriculum and lesson planning, exam practice, systematic literature review, and citation/reference management. |
| Product and operations | Added advanced spreadsheet modeling, product discovery, incident-response runbooks, and legal-document literacy; extended knowledge management for personal knowledge bases. |
| Authorized security follow-up | Added the security audit, shared authorization/ROE gates, attack-surface mapping, access-control testing, API assessment, findings reports, remediation retests, AI-agent permission review, explicit orchestrator refusal routing for jailbreak/bypass requests, and a CI-enforced security quality check. |

## Quality gates

Every new skill must have valid frontmatter, a distinct trigger, one task boundary, a concise workflow, explicit non-goals, verification, common failure modes where relevant, safety or authorization boundaries, and a handoff format. Skills must not copy textbook prose, invent citations or numerical results, include secrets, or hard-code private project details.

For tutoring and exam preparation, complete worked solutions are allowed when requested, but the workflow must preserve understanding, expose assumptions, and avoid shortcuts intended to conceal lack of learning. For regulated domains, the skills provide literacy or analytical support rather than personalized professional advice. For security, the preferred sequence is **find → verify safely → report → fix → retest**, beginning with explicit authority and scope.

## Future backlog

The core expansion is complete, but the catalog should continue through evidence-led increments rather than indiscriminate growth. Future candidates include a deeper secure-code-review module only if usage demonstrates a boundary not covered by existing code-review, hardening, vulnerability-detection, and web/API skills; more domain-specific science chapters; richer local test fixtures; and host-specific packaging adapters after compatibility has been verified. Any future addition should begin with an overlap audit and remain optional until it passes the repository quality gates.
