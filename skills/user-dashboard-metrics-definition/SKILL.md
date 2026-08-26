---
name: user-dashboard-metrics-definition
description: Define auditable dashboard KPIs, dimensions, denominators, grains, freshness, and anti-vanity checks. Use before building or revising analytics dashboards.
---

# Dashboard Metrics Definition

## Quick start

Use this skill when the request matches **Define auditable dashboard KPIs, dimensions, denominators, grains, freshness, and anti-vanity checks. Use before building or revising analytics dashboards.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Anchor each metric to a decision and define the entity, event, time window, inclusion rules, denominator, owner, source, and acceptable freshness.

## Workflow

Write a metric contract; resolve naming conflicts; specify numerator and denominator; define dimensions and filters; document aggregation and late-arriving data; add quality indicators; design a small decision-oriented dashboard; review accessibility and interpretation.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Declare unit of analysis, grain, schema, population, time window, denominator, provenance, missingness, and the decision the result must support before calculating. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **dashboard-metrics-definition**, use this compact record:

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

Reconcile the metric with source data, test filters and segments, inspect time-zone and period boundaries, compare with a known report, and verify that a viewer can reproduce the headline value.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If data is incomplete or definitions conflict, preserve the ambiguity, show the affected result, and request a source-of-truth decision instead of silently coercing values. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include mixing active-user definitions, hiding denominator changes, showing totals with incompatible grains, using vanity counts, and omitting freshness or data-quality status.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For data and quantitative work, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not present estimated or modeled values as observed facts. Protect personal data and avoid dashboards that expose unnecessary individual-level information. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return metric contracts, dashboard purpose and audience, source lineage, validation results, freshness/quality status, caveats, and owner.
