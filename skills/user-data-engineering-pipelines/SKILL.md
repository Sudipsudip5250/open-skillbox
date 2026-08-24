---
name: user-data-engineering-pipelines
description: Design reliable batch or streaming pipelines for ingestion, validation, transformation, storage, orchestration, and lineage. Use for data-platform architecture and implementation planning.
---

# Data Engineering Pipelines

## Scope and classification

Design reliable batch or streaming pipelines for ingestion, validation, transformation, storage, orchestration, and lineage. Use for data-platform architecture and implementation planning. Begin by identifying the system, objects, evidence, constraints, and expected level of precision.

## Method-selection workflow

1. Define sources, contracts, entities, freshness, latency, volume, quality, privacy, and consumers; choose batch or streaming; design stages and idempotent boundaries; specify schemas and backfills; and plan observability and recovery.
2. Write definitions, governing relationships, interfaces, or evidence criteria before applying them.
3. Work from the representation that exposes structure: diagram, table, equation, state model, data schema, or source record.
4. Keep units, domains, assumptions, uncertainty, permissions, and exact-versus-approximate status visible.
5. Interpret the result in the original context and identify what would change the conclusion.

## Verification and quality checks

Check row counts, keys, nulls, duplicates, late data, schema evolution, replay behavior, lineage, access controls, cost, and end-to-end reconciliation. Also perform an independent spot check, counterexample, replay, rendering, or alternate calculation whenever practical.

## Cross-domain quality rules

State the scope, assumptions, version or context, and intended audience before applying the method. Prefer a simple model that is explicit about what it omits. Separate observations, calculations, model outputs, interpretations, and recommendations. Preserve provenance for data, code, diagrams, and sources, and make important results reproducible.

## Safety and non-goals

These skills are educational and engineering aids, not substitutes for qualified professional review. Do not fabricate studies, measurements, citations, experimental results, or system behavior. Do not provide unsafe wet-lab, high-voltage, hazardous-material, medical, environmental-release, or physical-intervention instructions; keep procedures at a safe planning and analysis level and require appropriate institutional controls. Networking, systems, embedded, and architecture guidance assumes authorization and must not be used for credential theft, destructive exploitation, evasion, or unauthorized access. Do not expose secrets, private data, private infrastructure, or live exam answers.

## Composition and handoff

Compose with `user-task-orchestrator` for routing, `user-scientific-research` for evidence and reproducibility, `user-data-analysis-reporting` for structured data, and focused engineering or security skills when implementation or risk review is required.

## Handoff

Return: classification and scope; inputs, assumptions, and constraints; selected method; actionable steps or worked reasoning; verification and quality checks; limitations and safety boundary; and a concise final answer or artifact description. Name the next specialized skill when the task crosses domains.
