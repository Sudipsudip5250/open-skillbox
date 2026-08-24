---
name: user-identity-access-security
description: Design, review, and test authentication, authorization, session management, MFA, OAuth/OIDC, password recovery, service identities, and tenant isolation for systems the user owns or is authorized to assess. Use for scoped login, permissions, roles, tokens, account-security, access-control, or identity production-readiness work.
---

# Identity and Access Security


## Authorization and Rules of Engagement

Before reviewing private assets or performing any active check, confirm that the user owns the target or has documented contractual authorization. Capture a short Rules of Engagement (ROE) record containing:

- **Authority:** owner, client, engagement reference, and who can approve scope changes.
- **In scope:** exact URLs, APIs, repositories, applications, accounts, cloud projects, hosts, CIDRs, environments, tenants, and test data.
- **Out of scope:** excluded assets, accounts, data classes, third parties, production actions, and techniques.
- **Window and controls:** time window, environment preference, test accounts, allowed tools, rate limits, notification contacts, evidence retention, and redaction rules.
- **Risk and stops:** whether production is permitted and who accepted the risk; stop on unexpected PII or secrets, instability, destructive impact, scope drift, or any signal that an action is no longer authorized.

Prefer local code, configuration, passive observation, fixtures, and non-production targets. If authority, scope, or stop contacts are missing or ambiguous, do not perform intrusive testing; ask for the missing boundary or limit work to passive and local analysis. Summarize the ROE before active testing and update it before any approved scope change.

## Workflow

1. Model users, services, administrators, tenants, resources, actions, trust boundaries, and the difference between authentication, authorization, and identity proofing.
2. Review authentication: strong transport, password hashing, length and blocklist policy, MFA or phishing-resistant options when appropriate, throttling, generic errors, recovery, re-authentication for sensitive actions, and risk-event handling.
3. Review sessions and tokens: unpredictability, expiry, rotation, revocation, secure cookie attributes, CSRF model, issuer/audience/signature/expiry validation, key management, and replay resistance.
4. Review authorization at every server-side resource and action. Test least privilege, object-level access, role transitions, tenant boundaries, default-deny behavior, administrative paths, and direct API calls that bypass the UI.
5. Review OAuth/OIDC or SAML configuration for exact redirect URIs, state/nonce handling, issuer and audience validation, token storage, scopes, consent, logout, and account-linking risks.
6. Test allowed and denied paths with test accounts, expired credentials, changed roles, cross-tenant identifiers, replayed requests, recovery flows, and concurrent sessions. Verify audit events and alerts.

## Rules

- Never rely on hidden UI controls, client-side roles, sequential IDs, or frontend workflow order for authorization.
- Do not expose internal service or database accounts through public login surfaces.
- Do not reveal whether an account exists through messages or timing differences when enumeration matters.
- Do not weaken MFA, rate limits, session expiry, or recovery controls just to simplify testing or reduce friction without an explicit risk decision.
- Do not access real accounts or test credentials without authorization.

## Assessment handoff template

Return a concise record with **authority and ROE**, assets and environment tested, out-of-scope items, time window, tools and versions, methods and limitations, and a findings table using: **ID | severity | confidence | asset/location | issue | evidence | impact | remediation | retest status**. Mark findings as confirmed, suspected, false positive, accepted risk, or needs investigation. Redact credentials, tokens, PII, exploit-enabling detail, and private topology. End with residual risk, owner or escalation path, and the next verification or review date.

## Remediation and retest

Prefer a narrow, owner-assigned fix at the boundary that enforces the security property. Record the change, regression or acceptance test, deployment or configuration version, rollback consideration, and residual risk. If this skill only produces intake, mapping, or evidence, hand the confirmed issue to the findings and remediation skills rather than claiming it is fixed.

## Handoff

Report identity model, flows, token/session decisions, authorization matrix, negative-test evidence, recovery and audit behavior, residual risks, and required user or provider configuration.
