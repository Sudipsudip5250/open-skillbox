---
name: user-sre-error-budgets-slos
description: Define service-level indicators, objectives, error budgets, windows, alerting, and release policies. Use for reliability planning with observability and delivery teams.
---

# SRE SLOs and Error Budgets

## Purpose and scope

Start from user-visible reliability outcomes and service boundaries, not from whichever system metric is easiest to collect.

## Workflow

Define service and critical journeys; choose indicators for availability, latency, correctness, freshness, or throughput; set objective, window, aggregation, exclusions, and data source; calculate budget; define alert thresholds and burn rate; agree release, toil, and escalation policy; review error-budget consumption.

## Verification and quality checks

Validate the indicator against real user impact, test missing telemetry and denominator changes, compare with incident history, simulate burn rates, and verify that the policy produces actionable decisions.

## Common errors

Common errors include confusing uptime with correctness, setting targets without baseline or owner, alerting on averages that hide tails, ignoring multi-service dependencies, and treating the budget as permission to harm users.

## Rules, safety, and non-goals

Do not disable safety, security, accessibility, privacy, or compliance controls to meet an SLO. State uncertainty and avoid claiming reliability from incomplete telemetry. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return service scope, SLI/SLO definitions, data source, budget math, alert policy, release policy, ownership, exceptions, and review cadence.
