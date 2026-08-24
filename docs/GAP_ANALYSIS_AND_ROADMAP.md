# Gap Analysis and Prioritized Roadmap

## Executive summary

The public repository currently contains **64 focused skills** under `skills/<skill-name>/SKILL.md`. Its strongest coverage is software delivery, security, frontend engineering, operations, monetization, research, and media. The largest missing capability is a structured learning layer for mathematics, science, technology fundamentals, education, and domain-specific analytical workflows.

The repository is already modular and safety-aware, but its routing and maintenance systems need to scale before a large expansion. The generated index currently contains broken sandbox-absolute links, the validator checks only basic frontmatter and line count, and the orchestrator routes broad task families without chapter-level mathematics, science, education, ML, systems, or diagramming signals. These are P0 repository-quality issues because they affect every future contribution.

## Current coverage

| Category | Current state | Assessment |
|---|---:|---|
| Meta, orchestration, context, knowledge, delivery | 7 detected | Strong foundation; needs expanded domain routing. |
| Software engineering and quality | 9 detected | Strong; clarify handoffs and non-goals among broad and focused skills. |
| Frontend, design, accessibility, and browser QA | 13 detected | Strong; maintain separation between design, implementation, responsive behavior, accessibility, and visual verification. |
| Security, privacy, identity, and authorized testing | 16 detected | Strong and unusually broad; preserve explicit authorization boundaries. |
| Data, ML, and analytics | 3 detected | Adequate baseline; add data engineering and ML training/evaluation. |
| DevOps, cloud, reliability, and automation | 18 detected | Broad coverage; add incident runbooks and systems fundamentals later. |
| Research, science, and evidence | 3 detected | General research is present; specialized science chapters are missing. |
| Business, product, finance, and monetization | 8 detected | Broad coverage; future additions should remain non-advice and evidence-led. |
| Creative, media, and 3D | 6 detected | Useful baseline; add technical diagramming and specialized scientific visualization. |
| Writing and documentation | 5 detected | Good general coverage; add citation/reference management and education outputs. |
| Mathematics | 0 chapter skills | Critical gap. |
| Education and tutoring | 0 dedicated skills | Critical gap for learning workflows. |
| Technology fundamentals | 0 dedicated chapter skills | Important gap for architecture and science/engineering learning. |

## Key overlaps to manage

`user-software-engineering` should remain the general implementation owner, while code review, simplification, modernization, dependency migration, debugging, testing, API design, and source-driven development should remain focused sub-workflows. The general skill should gain explicit “when not to use” guidance and handoffs rather than absorbing all specialized procedures.

`user-research-fact-checking` and `user-scientific-research` should remain separate. The former is for factual investigation and source verification across domains; the latter is for scientific literature, experimental evidence, reproducibility, uncertainty, and research reporting. New literature-review and citation-management skills should connect to both without duplicating their core workflows.

The mathematics and science additions should not become textbooks. They should provide classification, method selection, a stepwise problem-solving procedure, verification, common errors, and a handoff format. The same principle applies to physics, chemistry, biology, engineering, and tutoring.

## P0 roadmap

| Priority | Skill or change | Trigger summary |
|---|---|---|
| P0 | Fix `docs/SKILL_INDEX.md` generation | Use when maintaining the public catalog; generate repository-relative links and grouped categories. |
| P0 | Expand `user-task-orchestrator` routing | Use when a request involves mathematics, science, education, ML, systems, diagrams, or domain learning. |
| P0 | Strengthen `scripts/validate_skills.py` | Use on every contribution; check unique names, frontmatter, headings, descriptions, links, and line limits. |
| P0 | `user-math-foundations` | Arithmetic, fractions, percentages, ratios, order of operations, and number sense. |
| P0 | `user-algebra-equations` | Linear equations, systems, inequalities, absolute value, and algebraic verification. |
| P0 | `user-functions-graphs` | Functions, domain/range, transformations, graph interpretation, and graph checks. |
| P0 | `user-polynomials-factoring` | Polynomial operations, roots, factoring, expansion, and substitution checks. |
| P0 | `user-exponents-logarithms` | Exponential models, logarithms, inverse relationships, and domain restrictions. |
| P0 | `user-trigonometry` | Trigonometric identities, equations, triangles, radians, graphs, and unit-circle checks. |
| P0 | `user-precalculus-sequences-series` | Sequences, series, recurrence, convergence intuition, and model selection. |
| P0 | `user-limits-continuity` | Limits, one-sided behavior, continuity, indeterminate forms, and numerical/symbolic checks. |
| P0 | `user-differential-calculus` | Derivatives, rates, optimization, curve behavior, and units/edge-case checks. |
| P0 | `user-integral-calculus` | Antiderivatives, definite integrals, area/accumulation, substitution, and derivative checks. |
| P0 | `user-linear-algebra` | Vectors, matrices, systems, transformations, eigenvalues, and dimensional checks. |
| P0 | `user-probability-foundations` | Sample spaces, conditional probability, independence, counting, and expectation. |
| P0 | `user-statistics-inference` | Descriptive statistics, intervals, tests, assumptions, effect size, and uncertainty. |
| P0 | `user-discrete-math` | Logic, sets, combinatorics, graph basics, relations, and induction. |
| P0 | `user-units-dimensional-analysis` | Unit conversion, dimensional consistency, scale checks, and uncertainty-aware calculations. |
| P0 | `user-experimental-design-lab-methods` | Variables, controls, randomization, error analysis, reproducibility, and safe lab reasoning. |

## P1 roadmap

P1 should create the first science, technology, and education layer: physics mechanics; electricity and magnetism; waves, optics, and thermodynamics; chemistry stoichiometry and reactions; chemistry structure and bonding; cell and molecular biology; genetics and evolution; earth and environmental science; scientific visualization; computer architecture; networking fundamentals; operating systems concepts; data engineering pipelines; ML training and evaluation; systems design; Socratic tutoring; curriculum and lesson planning; exam-preparation practice; systematic literature review; citation management; and Mermaid technical diagramming.

## P2 roadmap

P2 should add differential equations, numerical methods, proof techniques, word-problem modeling, symbolic computation, multivariable calculus, embedded and IoT basics, electronics fundamentals, advanced spreadsheet modeling, product discovery, incident runbooks, legal-document literacy, and personal knowledge-base workflows. These should follow the P0 routing and validator work so they do not create a large, ambiguous catalog.

## Quality gates for every new skill

Every new skill must have valid frontmatter, a distinct trigger, a single task boundary, a concise workflow, explicit non-goals, verification, common failure modes, safety or authorization boundaries when relevant, and a handoff format. It must not copy textbook prose, invent citations or numerical results, include secrets, or hard-code private project details.

For tutoring and exam preparation, the skill may provide complete worked solutions when requested, but it should preserve understanding, explain reasoning, expose assumptions, and avoid shortcuts intended to conceal lack of learning. For regulated domains, the skill should provide educational or analytical support without presenting itself as professional advice.
