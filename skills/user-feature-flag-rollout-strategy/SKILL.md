---
name: user-feature-flag-rollout-strategy
description: Plan safe feature-flag rollout, cohort exposure, observability, kill switches, rollback, lifecycle ownership, and cleanup. Use for product and service releases.
---

# Feature-Flag Rollout Strategy

## Purpose and scope

Define flag purpose, default, audience, risk, dependency, owner, expiry, metric, and rollback authority before enabling exposure.

## Workflow

Choose release cohorts; define eligibility and exclusions; instrument exposure and outcome; stage internal, small, percentage, segment, and general rollout; set guardrails and stop conditions; document kill switch and data migration behavior; remove the flag after stabilization.

## Verification and quality checks

Test default and opposite states, refresh and caching behavior, cohort consistency, access control, observability, rollback, stale-flag detection, and cleanup in source and configuration.

## Common errors

Common errors include flags without owners or expiry, evaluating on unstable attributes, mixing experiment and release flags, forgetting data compatibility, and assuming rollback is safe after an irreversible migration.

## Rules, safety, and non-goals

Do not use flags to bypass authorization, hide material behavior from users deceptively, or expose sensitive cohorts without governance. Treat flag configuration as production code. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return flag contract, cohorts, rollout stages, metrics and guardrails, kill switch, rollback, ownership, expiry, test evidence, and cleanup plan.
