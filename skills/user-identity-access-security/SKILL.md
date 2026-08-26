---
name: user-identity-access-security
description: Design, review, and test authentication, authorization, session management, MFA, OAuth/OIDC, password recovery, service identities, and tenant isolation for systems the user owns or is authorized to assess. Use for scoped login, permissions, roles, tokens, account-security, access-control, or identity production-readiness work.
---

# Identity and Access Security

## Quick start

Use this skill when the request matches **Design, review, and test authentication, authorization, session management, MFA, OAuth/OIDC, password recovery, service identities, and tenant isolation for systems the user owns or is authorized to assess. Use for scoped login, permissions, roles, tokens, account-security, access-control, or identity production-readiness work.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.



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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Confirm ownership or written authorization, target scope, environment, evidence handling, rate limits, and stop conditions before active access or testing. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **identity-access-security**, use this compact record:

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

## Handoff

Report identity model, flows, token/session decisions, authorization matrix, negative-test evidence, recovery and audit behavior, residual risks, and required user or provider configuration.
