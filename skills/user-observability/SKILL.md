---
name: user-observability
description: Add, review, or improve production observability for applications, APIs, workers, websites, and infrastructure. Use for structured logging, metrics, tracing, dashboards, alerts, incident diagnosis, or release monitoring.
---

# Observability

## Quick start

Use this skill when the request matches **Add, review, or improve production observability for applications, APIs, workers, websites, and infrastructure. Use for structured logging, metrics, tracing, dashboards, alerts, incident diagnosis, or release monitoring.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **observability**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If information is missing or conflicting, state the uncertainty, ask only blocking questions, and avoid fabricating evidence, permissions, results, or completed actions. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For general professional workflow, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

verify assumptions, important claims, edge cases, usability, safety, reproducibility, and whether the handoff contains enough information for another person or agent to continue. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Handoff

Report signals added, event and metric schemas, privacy controls, dashboards and alerts, test evidence, retention assumptions, ownership, and incident-response guidance.
