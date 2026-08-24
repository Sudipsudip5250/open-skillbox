---
name: user-ai-evaluation
description: Evaluate AI models, prompts, RAG systems, agents, and tool-using workflows for quality, safety, reliability, latency, and cost. Use for eval sets, prompt regression, model comparison, hallucination checks, tool-call tests, or AI release readiness.
---

# AI Evaluation

## Workflow

1. Define the task contract, users, acceptable outputs, failure severity, safety constraints, latency and cost budgets, supported languages, and release threshold.
2. Build a representative evaluation set from real or approved synthetic cases, including normal, boundary, ambiguous, adversarial, refusal, privacy, and tool-use cases. Keep test data versioned and free of unnecessary personal information.
3. Define measurable criteria: correctness, groundedness, completeness, instruction adherence, style, safety, tool-call validity, citation quality, latency, token or API cost, and consistency.
4. Run a baseline with a fixed model, prompt, retrieval set, tool schema, seed or sampling policy where available, and environment. Record inputs, outputs, metadata, evaluator rationale, and failures.
5. Compare one change at a time using deterministic checks, rubric-based review, pairwise comparison, or a trusted judge with calibration samples. Inspect false positives, false negatives, regressions, and subgroup or language differences.
6. Add release gates, red-team cases, privacy checks, cost limits, monitoring, and rollback criteria. Re-run after model, prompt, tool, retrieval, policy, or dependency changes.

## Rules

- Do not treat a single score or model-judge result as proof of quality or safety. Combine automated metrics with targeted human review.
- Do not use private or regulated data without authorization and appropriate protection. Redact outputs and evaluator logs.
- Do not optimize for a benchmark while degrading real user behavior, safety, or maintainability.
- Do not let an evaluated model execute consequential tools without independent authorization, schema validation, and approval controls.

## Handoff

Report evaluation set and version, baseline, metrics and thresholds, comparison method, results, error examples, safety and privacy findings, cost/latency trade-offs, release decision, and regression plan.
