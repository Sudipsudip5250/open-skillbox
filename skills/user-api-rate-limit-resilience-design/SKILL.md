---
name: user-api-rate-limit-resilience-design
description: Design reliable client and service behavior for quotas, throttling, retries, backoff, jitter, idempotency, fairness, and rate-limit observability.
---

# API Rate-Limit Resilience Design

## Quick start

Use this skill when the request matches **Design reliable client and service behavior for quotas, throttling, retries, backoff, jitter, idempotency, fairness, and rate-limit observability.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Identify caller, service, resource, quota scope, failure semantics, user impact, and whether a request is safe to retry.

## Workflow

Define limits and response contract; classify retryable and non-retryable failures; use bounded exponential backoff with jitter and retry budgets; add idempotency keys or deduplication; use queues or admission control where appropriate; expose remaining quota and retry timing; monitor saturation and unfairness; document client and server behavior.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **api-rate-limit-resilience-design**, use this compact record:

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

## Verification and quality checks

Test bursts, clock skew, duplicate requests, partial failures, long outages, retry storms, fairness across tenants, and graceful degradation. Verify that metrics distinguish rejection, latency, success, and downstream overload.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If the failure is not reproducible, capture environment and logs, reduce the case, state uncertainty, and avoid speculative rewrites or destructive recovery steps. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include unbounded retries, synchronized backoff, retrying non-idempotent writes, hiding 429 responses, ignoring quota scope, and creating a retry storm that worsens the incident.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For software and systems, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not bypass a third-party provider’s limits or use undocumented evasion. Use only authorized services, respect terms, protect credentials, and avoid sending sensitive payloads in test traces. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return traffic model, limit contract, retry matrix, idempotency strategy, observability, load-test evidence, failure behavior, and operational handoff.
