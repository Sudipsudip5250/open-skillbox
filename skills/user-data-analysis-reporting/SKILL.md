---
name: user-data-analysis-reporting
description: Clean, analyze, visualize, and explain structured data with reproducible calculations and decision-oriented reporting. Use for spreadsheets, CSV/JSON datasets, metrics, dashboards, forecasts, experiments, charts, and analytical reports.
---

# Data Analysis and Reporting

## Quick start

Use this skill when the request matches **Clean, analyze, visualize, and explain structured data with reproducible calculations and decision-oriented reporting. Use for spreadsheets, CSV/JSON datasets, metrics, dashboards, forecasts, experiments, charts, and analytical reports.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Analytical workflow

1. Define the decision, population, unit of analysis, time period, key measures, and acceptable uncertainty.
2. Inspect schema, types, missing values, duplicates, outliers, joins, sampling, and provenance before calculating.
3. Preserve raw data and create a documented cleaned layer. Never silently overwrite source data.
4. Validate transformations with counts, totals, ranges, referential integrity, and spot checks.
5. Select methods appropriate to the question; distinguish description, correlation, prediction, and causal inference.
6. Use clear visual encodings with titles, units, source notes, date ranges, and readable labels. Avoid decorative or misleading charts.
7. Reconcile key numbers independently when the result drives money, operations, or public claims.
8. Explain the finding, evidence, uncertainty, assumptions, limitation, and recommended action in that order.

## Quality checks

Check whether denominators are stable, time windows are comparable, categories overlap, missingness is informative, and aggregation hides important segments. Do not infer causation from a trend alone. Label estimates, projections, modeled values, and observed values distinctly.

## Deliverable standard

Provide a clean output dataset or workbook when requested, a short methodology note, key tables or charts, and a narrative that answers “what happened, why it may have happened, how certain we are, and what should be considered next.” Keep formulas or scripts reproducible and preserve a source-data path.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Declare unit of analysis, grain, schema, population, time window, denominator, provenance, missingness, and the decision the result must support before calculating. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **data-analysis-reporting**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If data is incomplete or definitions conflict, preserve the ambiguity, show the affected result, and request a source-of-truth decision instead of silently coercing values. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For data and quantitative work, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

reconcile totals, inspect nulls and duplicates, test boundary dates and exclusions, compare with an alternate calculation or baseline, and report uncertainty and data freshness. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.
