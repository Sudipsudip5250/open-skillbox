---
name: user-web-application-security
description: Secure and review browser applications, web servers, REST/GraphQL APIs, and business workflows the user owns or is authorized to assess. Use for scoped client-side or server-side security review, XSS, CSRF, CORS, CSP, SSRF, file uploads, sessions, API abuse, security headers, or web production-readiness checks.
---

# Web Application Security


## Authorization and Rules of Engagement

Before reviewing private assets or performing any active check, confirm that the user owns the target or has documented contractual authorization. Capture a short Rules of Engagement (ROE) record containing:

- **Authority:** owner, client, engagement reference, and who can approve scope changes.
- **In scope:** exact URLs, APIs, repositories, applications, accounts, cloud projects, hosts, CIDRs, environments, tenants, and test data.
- **Out of scope:** excluded assets, accounts, data classes, third parties, production actions, and techniques.
- **Window and controls:** time window, environment preference, test accounts, allowed tools, rate limits, notification contacts, evidence retention, and redaction rules.
- **Risk and stops:** whether production is permitted and who accepted the risk; stop on unexpected PII or secrets, instability, destructive impact, scope drift, or any signal that an action is no longer authorized.

Prefer local code, configuration, passive observation, fixtures, and non-production targets. If authority, scope, or stop contacts are missing or ambiguous, do not perform intrusive testing; ask for the missing boundary or limit work to passive and local analysis. Summarize the ROE before active testing and update it before any approved scope change.

## Workflow

1. Map browser, CDN, reverse proxy, server, API, worker, database, third-party, and administrative boundaries. Identify assets, roles, workflows, sensitive data, and trust transitions.
2. Review client-side controls: HTTPS, secure cookies, CSP, frame protection, referrer and permissions policy, safe DOM/API use, output encoding, dependency and third-party script controls, CSRF defenses, and avoidance of secrets in browser code.
3. Review server and API controls: authentication, endpoint authorization, object-level access, input and content-type validation, request-size limits, safe parsers, method allowlists, rate limits, idempotency, generic errors, audit logs, CORS specificity, and secure response headers.
4. Verify business logic on the server. Model valid workflow states, reject out-of-order or replayed transitions, bind tokens to the intended user and action, and do not rely on frontend sequencing.
5. Review risky features separately: uploads, downloads, redirects, SSRF, WebSockets, deserialization, command execution, GraphQL depth, multi-tenancy, payments, webhooks, and management endpoints.
6. Test authorized flows using benign inputs and test accounts. Cover anonymous, authenticated, unauthorized, malformed, expired, replayed, cross-tenant, and failure cases. Verify logs and recovery.

## Rules

- Client-side checks improve user experience but never replace server-side authorization or validation.
- Never put API secrets, database credentials, signing keys, or privileged tokens in client bundles, URLs, screenshots, or logs.
- Use allowlists and exact origins where possible. Avoid wildcard CORS with credentials.
- Return safe content types and encode output for its context. Do not expose stack traces, internal IDs, credentials, or sensitive state in errors.
- Do not run intrusive tests, exploit payloads, credential attacks, or scans against live targets without explicit authorization and scope.

## Assessment handoff template

Return a concise record with **authority and ROE**, assets and environment tested, out-of-scope items, time window, tools and versions, methods and limitations, and a findings table using: **ID | severity | confidence | asset/location | issue | evidence | impact | remediation | retest status**. Mark findings as confirmed, suspected, false positive, accepted risk, or needs investigation. Redact credentials, tokens, PII, exploit-enabling detail, and private topology. End with residual risk, owner or escalation path, and the next verification or review date.

## Handoff

Report architecture and trust boundaries, controls reviewed, tests performed, confirmed findings with evidence, remediation and regression tests, residual risks, and production assumptions.
