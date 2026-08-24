---
name: user-data-analysis-reporting
description: Clean, analyze, visualize, and explain structured data with reproducible calculations and decision-oriented reporting. Use for spreadsheets, CSV/JSON datasets, metrics, dashboards, forecasts, experiments, charts, and analytical reports.
---

# Data Analysis and Reporting

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
