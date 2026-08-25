---
name: user-dashboard-metrics-definition
description: Define auditable dashboard KPIs, dimensions, denominators, grains, freshness, and anti-vanity checks. Use before building or revising analytics dashboards.
---

# Dashboard Metrics Definition

## Purpose and scope

Anchor each metric to a decision and define the entity, event, time window, inclusion rules, denominator, owner, source, and acceptable freshness.

## Workflow

Write a metric contract; resolve naming conflicts; specify numerator and denominator; define dimensions and filters; document aggregation and late-arriving data; add quality indicators; design a small decision-oriented dashboard; review accessibility and interpretation.

## Verification and quality checks

Reconcile the metric with source data, test filters and segments, inspect time-zone and period boundaries, compare with a known report, and verify that a viewer can reproduce the headline value.

## Common errors

Common errors include mixing active-user definitions, hiding denominator changes, showing totals with incompatible grains, using vanity counts, and omitting freshness or data-quality status.

## Rules, safety, and non-goals

Do not present estimated or modeled values as observed facts. Protect personal data and avoid dashboards that expose unnecessary individual-level information. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return metric contracts, dashboard purpose and audience, source lineage, validation results, freshness/quality status, caveats, and owner.
