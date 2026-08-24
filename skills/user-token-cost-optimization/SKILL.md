---
name: user-token-cost-optimization
description: Reduce AI token usage, model calls, latency, and inference cost while preserving correctness, safety, and required quality. Use for prompt compression, context budgets, model routing, batching, caching, structured outputs, agent loops, or token-usage analysis.
---

# Token Cost Optimization

## Workflow

1. Define the quality, freshness, latency, privacy, reliability, and output requirements before optimizing. Establish a token and call budget when measurable.
2. Measure the baseline: input and output tokens, repeated context, model, calls, retries, tool results, cache behavior, latency, failure rate, and human review cost.
3. Reduce unnecessary context with task-specific retrieval, summaries, targeted ranges, progressive disclosure, deduplication, stable prompt prefixes, and compact schemas. Keep instructions that affect safety or correctness.
4. Route simple deterministic tasks to local code or smaller suitable models. Batch independent items, cache stable results, reuse verified artifacts, and avoid repeated calls caused by unclear schemas or weak stopping conditions.
5. Constrain outputs with explicit formats, limits, and acceptance criteria. Prefer structured extraction or classification over open-ended prose when that satisfies the task.
6. Re-measure quality, safety, latency, cost, and failure modes. Keep the change only when the total trade-off improves and critical verification is preserved.

## Rules

- Never remove security, privacy, source verification, accessibility, backup, or regression checks merely to save tokens.
- Do not assume prompt caching, batching, or a smaller model is available or cheaper; verify provider behavior and current pricing.
- Do not compress away project constraints, user intent, tool permissions, or uncertainty labels.
- Keep a short cost record: baseline, change, measured effect, quality impact, and rollback condition.

## Handoff

Report baseline and measurement method, optimization changes, token/call/latency effect, quality and safety comparison, provider assumptions, and remaining cost opportunities.
