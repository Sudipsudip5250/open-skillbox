---
name: user-capacity-planning-basics
description: Estimate demand, resource needs, headroom, bottlenecks, load-test plans, uncertainty, and scaling triggers. Use for services, teams, infrastructure, or operational capacity.
---

# Capacity Planning Basics

## Quick start

Use this skill when the request matches **Estimate demand, resource needs, headroom, bottlenecks, load-test plans, uncertainty, and scaling triggers. Use for services, teams, infrastructure, or operational capacity.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Define workload unit, forecast horizon, service target, current baseline, constraints, resource dimensions, seasonality, and acceptable risk.

## Workflow

Model demand scenarios; map workload to CPU, memory, storage, network, queue, dependency, and human capacity; identify bottleneck and scaling unit; estimate headroom; test with representative load; define trigger thresholds, procurement or staffing lead time, and rollback or fallback.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | State the user or service outcome, decision owner, evidence, time horizon, capacity, dependencies, risk, and explicit non-goals before recommending a plan. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **capacity-planning-basics**, use this compact record:

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

Reconcile forecast with historical data, test sensitivity, check saturation and tail latency, validate assumptions in a safe environment, and document uncertainty rather than reporting a single certain number.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If evidence or ownership is missing, mark the item as a hypothesis, decision needed, or escalation rather than presenting a speculative commitment as a plan. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include extrapolating linear growth, ignoring burstiness, sizing only the first bottleneck, using averages, forgetting dependency capacity, and confusing reserved capacity with usable headroom.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For product and operations, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not run disruptive load tests against systems without authorization. Avoid using estimates as financial, staffing, or safety certainty without responsible review. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return demand scenarios, resource model, bottlenecks, headroom, test evidence, triggers, costs or constraints, uncertainty, and review date.
