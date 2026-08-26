---
name: user-finops-cost-optimization
description: Analyze and reduce recurring infrastructure, hosting, API, storage, database, observability, and project operating costs without violating reliability, security, privacy, or performance requirements. Use for cloud bills, resource right-sizing, provider comparisons, budget controls, or cost reviews.
---

# FinOps and Operating Cost Optimization

## Quick start

Use this skill when the request matches **Analyze and reduce recurring infrastructure, hosting, API, storage, database, observability, and project operating costs without violating reliability, security, privacy, or performance requirements. Use for cloud bills, resource right-sizing, provider comparisons, budget controls, or cost reviews.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Define the budget, billing period, currency, environments, reliability and latency targets, data-retention needs, and costs that are fixed versus variable.
2. Inventory services, resources, regions, traffic, storage, database usage, observability, AI/API calls, licenses, idle capacity, data transfer, and human maintenance.
3. Attribute spend to projects and environments. Find waste through idle resources, overprovisioning, duplicate services, unnecessary retention, unbounded logs, unused reservations, noisy automation, and expensive failure or retry loops.
4. Compare options using total cost of ownership: setup, usage, egress, support, migration, lock-in, availability, security, compliance, performance, and rollback cost.
5. Apply reversible changes first: schedules, limits, autoscaling, retention, sampling, storage tiers, caching, batching, right-sizing, quotas, and environment cleanup. Protect production and recovery resources.
6. Verify the bill, service-level indicators, latency, error rate, data durability, security controls, and user behavior after the change. Set alerts and review cadence.

## Rules

- Do not delete resources, backups, logs, data, domains, certificates, or production capacity solely to save money without authorization and recovery evidence.
- Never trade away security, privacy, accessibility, durability, or required reliability without stating the risk and obtaining the necessary decision.
- Validate current provider pricing, discounts, taxes, currency, quotas, and regional differences instead of relying on old estimates.
- Separate confirmed savings from projections and state confidence and assumptions.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **finops-cost-optimization**, use this compact record:

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

Report baseline spend and source, cost drivers, ranked opportunities, estimated versus measured savings, quality and risk trade-offs, implementation status, alerts, and next review date.
