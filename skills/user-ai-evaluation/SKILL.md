---
name: user-ai-evaluation
description: Evaluate AI models, prompts, RAG systems, agents, and tool-using workflows for quality, safety, reliability, latency, and cost. Use for eval sets, prompt regression, model comparison, hallucination checks, tool-call tests, or AI release readiness.
---

# AI Evaluation

## Quick start

Use this skill when the request matches **Evaluate AI models, prompts, RAG systems, agents, and tool-using workflows for quality, safety, reliability, latency, and cost. Use for eval sets, prompt regression, model comparison, hallucination checks, tool-call tests, or AI release readiness.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the agent host, available tools, instruction precedence, context budget, data boundary, approval gates, expected output, and the smallest skill chain that can complete the task. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **ai-evaluation**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If a host cannot load the canonical format or a tool is unavailable, preserve the source skill and document a reversible adapter or manual fallback rather than claiming compatibility. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For agent workflow and governance, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

run a representative prompt, inspect tool traces and handoffs, test refusal and uncertainty behavior, verify no private context leaks, and compare against a fixed baseline when evaluating changes. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Handoff

Report evaluation set and version, baseline, metrics and thresholds, comparison method, results, error examples, safety and privacy findings, cost/latency trade-offs, release decision, and regression plan.
