---
name: user-identity-access-security
description: Design, review, and test authentication, authorization, session management, MFA, OAuth/OIDC, password recovery, service identities, and tenant isolation. Use for login, permissions, roles, tokens, account security, access-control bugs, or identity production readiness.
---

# Identity and Access Security

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

## Handoff

Report identity model, flows, token/session decisions, authorization matrix, negative-test evidence, recovery and audit behavior, residual risks, and required user or provider configuration.
