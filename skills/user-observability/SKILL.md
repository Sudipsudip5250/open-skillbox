---
name: user-observability
description: Add, review, or improve production observability for applications, APIs, workers, websites, and infrastructure. Use for structured logging, metrics, tracing, dashboards, alerts, incident diagnosis, or release monitoring.
---

# Observability

## Workflow

1. Define the user and operator questions: what failed, who is affected, where, when, how often, and whether the system is recovering.
2. Map the request path and critical dependencies. Choose signals that answer those questions: structured logs, latency/error/traffic/saturation metrics, traces, health checks, and business outcomes.
3. Instrument at boundaries and important state transitions. Use stable names, correlation or trace IDs, bounded cardinality, units, timestamps, severity, and actionable context.
4. Protect privacy and security. Redact secrets, tokens, credentials, payment data, and unnecessary personal information. Define retention and access controls.
5. Create alerts around symptoms and service objectives, not noisy implementation events. Include runbook links, thresholds, ownership, deduplication, and recovery behavior.
6. Validate instrumentation in local or staging environments and during a representative failure. Confirm logs, metrics, traces, dashboards, alerts, and sampling behave as intended.

## Rules

- Do not log sensitive values merely because they are available. Prefer identifiers, classifications, and counts.
- Do not add unbounded labels such as raw URLs, user input, IDs, or exception text to metrics.
- Do not treat a green health endpoint as proof that the user journey works; combine technical and business signals.
- Keep observability overhead measurable and proportionate to risk and cost.

## Handoff

Report signals added, event and metric schemas, privacy controls, dashboards and alerts, test evidence, retention assumptions, ownership, and incident-response guidance.
