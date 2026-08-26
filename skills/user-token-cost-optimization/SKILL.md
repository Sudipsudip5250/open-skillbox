---
name: user-token-cost-optimization
description: Reduce AI token usage, model calls, latency, and inference cost while preserving correctness, safety, and required quality. Use for prompt compression, context budgets, model routing, batching, caching, structured outputs, agent loops, or token-usage analysis.
---

# Token Cost Optimization

## Quick start

Use this skill when the request matches **Reduce AI token usage, model calls, latency, and inference cost while preserving correctness, safety, and required quality. Use for prompt compression, context budgets, model routing, batching, caching, structured outputs, agent loops, or token-usage analysis.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Define quality, freshness, latency, privacy, reliability, and output requirements before optimizing. Establish a token and call budget when measurable.
2. Measure the baseline: input and output tokens, repeated context, model, calls, retries, tool results, cache behavior, latency, failure rate, and human review cost.
3. Reduce unnecessary context with task-specific retrieval, summaries, targeted ranges, progressive disclosure, deduplication, stable prompt prefixes, and compact schemas. Keep instructions that affect safety or correctness.
4. Route simple deterministic tasks to local code or smaller suitable models. Batch independent items, cache stable results, reuse verified artifacts, and avoid repeated calls caused by unclear schemas or weak stopping conditions.
5. Constrain outputs with explicit formats, limits, and acceptance criteria. Prefer structured extraction or classification over open-ended prose when that satisfies the task.
6. Re-measure quality, safety, latency, cost, and failure modes. Keep the change only when the total trade-off improves and critical verification is preserved.

## Boundary and routing

Use this skill for inference, prompt, context, model-call, and agent-loop efficiency. Use FinOps cost optimization for infrastructure and recurring project spend, cost-efficient execution for total task cost, context engineering for information selection, and AI evaluation when the quality or safety trade-off needs a formal evaluation.

## Rules

- Never remove security, privacy, source verification, accessibility, backup, or regression checks merely to save tokens.
- Do not assume prompt caching, batching, a model tier, or a provider feature is available or cheaper; verify current provider behavior and pricing.
- Do not compress away project constraints, user intent, tool permissions, citations, uncertainty labels, or failure evidence.
- Do not use a smaller model or aggressive compression for high-risk decisions without a quality and safety comparison.
- Keep a short cost record: baseline, change, measured effect, quality impact, and rollback condition.

## When not to use this skill

Do not use it for generic cloud billing, pricing strategy, or project budget work without an AI-inference component. Do not optimize a task before its acceptance criteria and quality baseline are defined.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **token-cost-optimization**, use this compact record:

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

Report baseline and measurement method, optimization changes, token/call/latency effect, quality and safety comparison, provider assumptions, failure modes, rollback condition, and remaining cost opportunities.
