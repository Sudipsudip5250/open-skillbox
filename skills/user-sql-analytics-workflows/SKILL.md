---
name: user-sql-analytics-workflows
description: Analyze structured data with SQL joins, grouping, window functions, subqueries, and verification. Use for reproducible analytics queries and result checks.
---

# SQL Analytics Workflows

## Quick start

Use this skill when the request matches **Analyze structured data with SQL joins, grouping, window functions, subqueries, and verification. Use for reproducible analytics queries and result checks.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Translate the question into a grain, population, time window, dimensions, measures, and expected reconciliation before writing SQL.

## Workflow

Inspect schema and keys; declare row grain; choose joins and filters; build a readable query in stages; use windows for within-group comparisons; validate counts, nulls, duplicates, totals, and edge cases; explain assumptions and query cost.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Declare unit of analysis, grain, schema, population, time window, denominator, provenance, missingness, and the decision the result must support before calculating. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **sql-analytics-workflows**, use this compact record:

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

Check join cardinality, denominator stability, date boundaries, null semantics, duplicate multiplication, sample rows, and an independent total or alternate query.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If data is incomplete or definitions conflict, preserve the ambiguity, show the affected result, and request a source-of-truth decision instead of silently coercing values. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include accidental many-to-many joins, filtering after aggregation incorrectly, mixing event and entity grain, using ambiguous dates, and treating a query result as causal evidence.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For data and quantitative work, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not expose private data or run destructive statements. Use read-only queries or a sandbox unless the owner explicitly authorizes writes; redact sensitive values in examples. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return the question and grain, schema assumptions, SQL, validation evidence, result interpretation, limitations, and a reproducible next query.
