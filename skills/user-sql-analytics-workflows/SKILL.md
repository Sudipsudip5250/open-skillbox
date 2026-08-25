---
name: user-sql-analytics-workflows
description: Analyze structured data with SQL joins, grouping, window functions, subqueries, and verification. Use for reproducible analytics queries and result checks.
---

# SQL Analytics Workflows

## Purpose and scope

Translate the question into a grain, population, time window, dimensions, measures, and expected reconciliation before writing SQL.

## Workflow

Inspect schema and keys; declare row grain; choose joins and filters; build a readable query in stages; use windows for within-group comparisons; validate counts, nulls, duplicates, totals, and edge cases; explain assumptions and query cost.

## Verification and quality checks

Check join cardinality, denominator stability, date boundaries, null semantics, duplicate multiplication, sample rows, and an independent total or alternate query.

## Common errors

Common errors include accidental many-to-many joins, filtering after aggregation incorrectly, mixing event and entity grain, using ambiguous dates, and treating a query result as causal evidence.

## Rules, safety, and non-goals

Do not expose private data or run destructive statements. Use read-only queries or a sandbox unless the owner explicitly authorizes writes; redact sensitive values in examples. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return the question and grain, schema assumptions, SQL, validation evidence, result interpretation, limitations, and a reproducible next query.
