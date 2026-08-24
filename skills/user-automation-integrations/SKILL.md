---
name: user-automation-integrations
description: Design, implement, and verify integrations with APIs, webhooks, schedulers, external services, and background jobs. Use for synchronization, bots, recurring execution, event-driven workflows, notifications, imports, exports, and service connectors.
---

# Automation and Integrations

## Integration workflow

1. Define the event or schedule, inputs, outputs, owner, freshness target, failure behavior, and retry policy.
2. Inspect the provider’s current documentation, authentication model, rate limits, pagination, quotas, and data contract.
3. Design idempotent operations with stable identifiers, deduplication, checkpoints, and safe replay.
4. Validate inputs and outputs at the boundary. Store only the minimum data required and protect credentials.
5. Implement timeouts, exponential backoff with limits, rate-limit handling, structured logs, metrics, and alerts.
6. Use a dry run or sandbox when available. Test success, duplicate delivery, partial failure, expired credentials, malformed payloads, and provider downtime.
7. Make scheduling timezone-aware and document concurrency, overlap, retention, and manual recovery.
8. Verify the live behavior and provide an operational runbook.

## Reliability rules

Assume network calls can fail, events can arrive more than once or out of order, and schemas can change. Do not acknowledge a webhook before durable processing or a safe queue handoff. Do not retry non-idempotent actions blindly. Keep secrets in environment or secret storage, never in code or logs.

## Operational handoff

Document setup, permissions, environment variables by name only, schedule or trigger, data flow, retry behavior, alert destination, replay or rollback procedure, and expected operating cost.
