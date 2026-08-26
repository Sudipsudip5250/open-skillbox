---
name: user-api-security-assessment-authorized
description: Assess REST, GraphQL, webhook, and service APIs owned by the user or covered by explicit authorization for authentication, authorization, input handling, abuse resistance, data exposure, and workflow security.
---

# Authorized API Security Assessment

## Quick start

Use this skill when the request matches **Assess REST, GraphQL, webhook, and service APIs owned by the user or covered by explicit authorization for authentication, authorization, input handling, abuse resistance, data exposure, and workflow security.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose

Use for a scoped API assessment after the ROE gate. It focuses on safe verification of API contracts and abuse cases rather than unrestricted fuzzing or exploit development.

## Authorization gate

Confirm ownership or documented contractual authorization before touching private or live assets. Load or create a short Rules-of-Engagement record with in-scope and out-of-scope assets, environment, time window, allowed methods, rate limits, data handling, notification contacts, and stop conditions. Prefer local review, fixtures, passive checks, and non-production. If authority or scope is ambiguous, stop active work and request the missing boundary.

## Workflow

1. Load the ROE and inventory API hosts, versions, schemas, authentication methods, roles, tenants, rate limits, webhooks, and sensitive operations.
2. Establish a contract baseline from OpenAPI, GraphQL schemas, source, gateway rules, and observed benign requests; identify undocumented behavior as a review item, not automatic permission.
3. Test authentication, object and function authorization, tenant binding, method and content-type allowlists, validation, parsing limits, error handling, and sensitive response fields with synthetic data.
4. Review mass assignment, excessive data exposure, pagination, filtering, batch endpoints, idempotency, replay, webhooks, signature validation, GraphQL depth or cost, and rate-limit semantics.
5. Use conservative request budgets and test accounts; vary one controlled condition at a time and preserve request class, response class, and impact evidence.
6. Reconcile API behavior with service, database, queue, and audit boundaries; recommend a minimal fix and a regression test for each confirmed issue.

## Verification

Validate schema and runtime differences, authentication and authorization at the owning service, limits under safe load, replay and idempotency behavior, error redaction, webhook authenticity, and response minimization.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Confirm ownership or written authorization, target scope, environment, evidence handling, rate limits, and stop conditions before active access or testing. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **api-security-assessment-authorized**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If authorization, scope, or safe evidence handling is missing, pause and provide a planning-only alternative rather than probing, bypassing, or guessing. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For security and trust, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

redact secrets and personal data; preserve evidence integrity; distinguish observation from inference; verify fixes with a bounded retest; and escalate when scope or authority is unclear. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Safety and non-goals

Do not attack public APIs without authorization, enumerate unrelated tenants, send destructive payloads, stress services, bypass rate limits, exfiltrate data, or publish weaponized requests. Never request or retain credentials when a safer user-side action is available. Redact secrets, tokens, PII, and private topology from reports.

## Remediation and retest

Prefer a narrow, owner-assigned fix at the boundary that enforces the security property. Record the change, regression or acceptance test, deployment or configuration version, rollback consideration, and residual risk. If this skill only produces intake, mapping, or evidence, hand the confirmed issue to the findings and remediation skills rather than claiming it is fixed.

## Handoff

Return API inventory and scope, schema and version, roles and test data, cases and rate limits, redacted evidence, severity and confidence, remediation, regression and retest status, and residual risk.
