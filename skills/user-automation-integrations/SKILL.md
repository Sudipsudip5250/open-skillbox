---
name: user-automation-integrations
description: Design, implement, and verify integrations with APIs, webhooks, schedulers, external services, and background jobs. Use for synchronization, bots, recurring execution, event-driven workflows, notifications, imports, exports, and service connectors.
---

# Automation and Integrations

## Quick start

Use this skill when the request matches **Design, implement, and verify integrations with APIs, webhooks, schedulers, external services, and background jobs. Use for synchronization, bots, recurring execution, event-driven workflows, notifications, imports, exports, and service connectors.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **automation-integrations**, use this compact record:

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
