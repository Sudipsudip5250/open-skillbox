---
name: user-performance-optimization
description: Measure, diagnose, and improve application, website, API, database, build, or container performance. Use for slow pages, high latency, large bundles, excessive memory, expensive queries, render problems, or performance regressions.
---

# Performance Optimization

## Quick start

Use this skill when the request matches **Measure, diagnose, and improve application, website, API, database, build, or container performance. Use for slow pages, high latency, large bundles, excessive memory, expensive queries, render problems, or performance regressions.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **performance-optimization**, use this compact record:

```text
Request: [the concrete task and intended outcome]
Scope and inputs: [files, data, versions, permissions, audience]
Classification: [task type, risk, and relevant branch]
Method: [selected procedure and why alternatives were rejected]
Steps: [ordered actions with intermediate outputs]
Result: [answer or artifact, separated from interpretation]
Checks: [independent verification, edge cases, safety, accessibility, or reproducibility]
Handoff: [files, owners, limitations, and next action]
```

Do not fill this pattern with invented evidence. If the task is underspecified, keep placeholders visible or ask for the missing decision.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If information is missing or conflicting, state the uncertainty, ask only blocking questions, and avoid fabricating evidence, permissions, results, or completed actions. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For general professional workflow, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

verify assumptions, important claims, edge cases, usability, safety, reproducibility, and whether the handoff contains enough information for another person or agent to continue. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Handoff

Report baseline, bottleneck evidence, change, before/after measurements, test environment, trade-offs, and the guard that will detect regression.
