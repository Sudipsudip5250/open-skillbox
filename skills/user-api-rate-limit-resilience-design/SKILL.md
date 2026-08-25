---
name: user-api-rate-limit-resilience-design
description: Design reliable client and service behavior for quotas, throttling, retries, backoff, jitter, idempotency, fairness, and rate-limit observability.
---

# API Rate-Limit Resilience Design

## Purpose and scope

Identify caller, service, resource, quota scope, failure semantics, user impact, and whether a request is safe to retry.

## Workflow

Define limits and response contract; classify retryable and non-retryable failures; use bounded exponential backoff with jitter and retry budgets; add idempotency keys or deduplication; use queues or admission control where appropriate; expose remaining quota and retry timing; monitor saturation and unfairness; document client and server behavior.

## Verification and quality checks

Test bursts, clock skew, duplicate requests, partial failures, long outages, retry storms, fairness across tenants, and graceful degradation. Verify that metrics distinguish rejection, latency, success, and downstream overload.

## Common errors

Common errors include unbounded retries, synchronized backoff, retrying non-idempotent writes, hiding 429 responses, ignoring quota scope, and creating a retry storm that worsens the incident.

## Rules, safety, and non-goals

Do not bypass a third-party provider’s limits or use undocumented evasion. Use only authorized services, respect terms, protect credentials, and avoid sending sensitive payloads in test traces. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return traffic model, limit contract, retry matrix, idempotency strategy, observability, load-test evidence, failure behavior, and operational handoff.
