---
name: user-ml-training-evaluation
description: Plan, train, compare, and evaluate machine-learning models with leakage control, meaningful metrics, calibration, and reproducible experiments. Use for ML workflows, not high-stakes decisions without domain review.
---

# Machine Learning Training and Evaluation

## Scope and classification

Plan, train, compare, and evaluate machine-learning models with leakage control, meaningful metrics, calibration, and reproducible experiments. Use for ML workflows, not high-stakes decisions without domain review. Begin by identifying the system, objects, evidence, constraints, and expected level of precision.

## Method-selection workflow

1. Define prediction target, unit of analysis, deployment decision, data split, baseline, model family, and metric; build a leakage-resistant pipeline; tune only within training data; evaluate on held-out data; and report uncertainty and subgroup behavior.
2. Write definitions, governing relationships, interfaces, or evidence criteria before applying them.
3. Work from the representation that exposes structure: diagram, table, equation, state model, data schema, or source record.
4. Keep units, domains, assumptions, uncertainty, permissions, and exact-versus-approximate status visible.
5. Interpret the result in the original context and identify what would change the conclusion.

## Feature and serving hygiene

Track feature definition, source, owner, point-in-time availability, transformations, freshness, and access. Check training-serving skew and leakage across the feature pipeline. For each released model, keep a concise model card covering intended use, data scope, evaluation, limitations, subgroup behavior, monitoring signals, and rollback or retirement criteria.

## Verification and quality checks

Check train-test contamination, class or target drift, baseline comparison, calibration, threshold trade-offs, confidence intervals or repeated splits, error slices, reproducibility, and whether the metric matches the decision. Also perform an independent spot check, counterexample, replay, rendering, or alternate calculation whenever practical.

## Cross-domain quality rules

State the scope, assumptions, version or context, and intended audience before applying the method. Prefer a simple model that is explicit about what it omits. Separate observations, calculations, model outputs, interpretations, and recommendations. Preserve provenance for data, code, diagrams, and sources, and make important results reproducible.

## Safety and non-goals

These skills are educational and engineering aids, not substitutes for qualified professional review. Do not fabricate studies, measurements, citations, experimental results, or system behavior. Do not provide unsafe wet-lab, high-voltage, hazardous-material, medical, environmental-release, or physical-intervention instructions; keep procedures at a safe planning and analysis level and require appropriate institutional controls. Networking, systems, embedded, and architecture guidance assumes authorization and must not be used for credential theft, destructive exploitation, evasion, or unauthorized access. Do not expose secrets, private data, private infrastructure, or live exam answers.

## Composition and handoff

Compose with `user-task-orchestrator` for routing, `user-scientific-research` for evidence and reproducibility, `user-data-analysis-reporting` for structured data, and focused engineering or security skills when implementation or risk review is required.

## Handoff

Return: classification and scope; inputs, assumptions, and constraints; selected method; actionable steps or worked reasoning; verification and quality checks; limitations and safety boundary; and a concise final answer or artifact description. Name the next specialized skill when the task crosses domains.
