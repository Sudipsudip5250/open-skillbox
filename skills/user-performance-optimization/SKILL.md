---
name: user-performance-optimization
description: Measure, diagnose, and improve application, website, API, database, build, or container performance. Use for slow pages, high latency, large bundles, excessive memory, expensive queries, render problems, or performance regressions.
---

# Performance Optimization

## Workflow

1. Define the user-visible or operational metric: latency, throughput, frame rate, startup, bundle size, memory, CPU, build time, cost, or error rate. Establish a baseline before changing code.
2. Reproduce under a representative environment and workload. Use profiling, traces, browser performance data, query plans, logs, benchmarks, or container metrics rather than intuition.
3. Locate the dominant bottleneck and form a measurable hypothesis. Avoid optimizing code that is not on the critical path.
4. Apply the smallest change that addresses the bottleneck: remove waterfalls, reduce unnecessary work, cache safely, paginate, batch, stream, virtualize, index, split bundles, reuse resources, or simplify rendering.
5. Re-measure with the same workload and compare before/after results. Check correctness, tail latency, memory, accessibility, cache invalidation, and cost trade-offs.
6. Add a regression benchmark, budget, alert, or test when the improvement is important enough to preserve.

## Rules

- Do not claim improvement without measurements. Distinguish lab results from real-user or production evidence.
- Preserve correctness, freshness, security, and maintainability. A faster incorrect result is a regression.
- Avoid premature micro-optimization and unbounded caching. Document invalidation, capacity, and failure behavior.
- For frontend work, inspect Core Web Vitals, network waterfalls, JavaScript execution, layout shifts, image loading, and accessibility.
- For APIs and databases, inspect query plans, N+1 patterns, pagination, concurrency, serialization, rate limits, and tail behavior.

## Handoff

Report baseline, bottleneck evidence, change, before/after measurements, test environment, trade-offs, and the guard that will detect regression.
