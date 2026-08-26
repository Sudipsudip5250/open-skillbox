---
name: user-sre-error-budgets-slos
description: Define service-level indicators, objectives, error budgets, windows, alerting, and release policies. Use for reliability planning with observability and delivery teams.
---

# SRE SLOs and Error Budgets

## Quick start

Use this skill when the request matches **Define service-level indicators, objectives, error budgets, windows, alerting, and release policies. Use for reliability planning with observability and delivery teams.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Start from user-visible reliability outcomes and service boundaries, not from whichever system metric is easiest to collect.

## Workflow

Define service and critical journeys; choose indicators for availability, latency, correctness, freshness, or throughput; set objective, window, aggregation, exclusions, and data source; calculate budget; define alert thresholds and burn rate; agree release, toil, and escalation policy; review error-budget consumption.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | State the user or service outcome, decision owner, evidence, time horizon, capacity, dependencies, risk, and explicit non-goals before recommending a plan. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **sre-error-budgets-slos**, use this compact record:

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

## Verification and quality checks

Validate the indicator against real user impact, test missing telemetry and denominator changes, compare with incident history, simulate burn rates, and verify that the policy produces actionable decisions.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If evidence or ownership is missing, mark the item as a hypothesis, decision needed, or escalation rather than presenting a speculative commitment as a plan. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include confusing uptime with correctness, setting targets without baseline or owner, alerting on averages that hide tails, ignoring multi-service dependencies, and treating the budget as permission to harm users.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For product and operations, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not disable safety, security, accessibility, privacy, or compliance controls to meet an SLO. State uncertainty and avoid claiming reliability from incomplete telemetry. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return service scope, SLI/SLO definitions, data source, budget math, alert policy, release policy, ownership, exceptions, and review cadence.
