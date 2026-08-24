---
name: user-api-security-assessment-authorized
description: Assess REST, GraphQL, webhook, and service APIs owned by the user or covered by explicit authorization for authentication, authorization, input handling, abuse resistance, data exposure, and workflow security.
---

# Authorized API Security Assessment

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

## Safety and non-goals

Do not attack public APIs without authorization, enumerate unrelated tenants, send destructive payloads, stress services, bypass rate limits, exfiltrate data, or publish weaponized requests. Never request or retain credentials when a safer user-side action is available. Redact secrets, tokens, PII, and private topology from reports.

## Remediation and retest

Prefer a narrow, owner-assigned fix at the boundary that enforces the security property. Record the change, regression or acceptance test, deployment or configuration version, rollback consideration, and residual risk. If this skill only produces intake, mapping, or evidence, hand the confirmed issue to the findings and remediation skills rather than claiming it is fixed.

## Handoff

Return API inventory and scope, schema and version, roles and test data, cases and rate limits, redacted evidence, severity and confidence, remediation, regression and retest status, and residual risk.
