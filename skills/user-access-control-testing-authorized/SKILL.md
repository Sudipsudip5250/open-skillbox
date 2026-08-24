---
name: user-access-control-testing-authorized
description: Test authentication and server-side authorization, object-level access, tenant isolation, roles, sessions, and recovery flows on applications the user owns or is authorized to assess, using controlled test identities.
---

# Authorized Access-Control Testing

## Purpose

Use for deep AuthN/AuthZ and IDOR-style verification after scope approval. It complements identity design review by organizing negative-path tests and evidence without accessing real users’ data.

## Authorization gate

Confirm ownership or documented contractual authorization before touching private or live assets. Load or create a short Rules-of-Engagement record with in-scope and out-of-scope assets, environment, time window, allowed methods, rate limits, data handling, notification contacts, and stop conditions. Prefer local review, fixtures, passive checks, and non-production. If authority or scope is ambiguous, stop active work and request the missing boundary.

## Workflow

1. Load the ROE and build an authorization matrix of actors, roles, tenants, resources, actions, states, and expected allow or deny outcomes.
2. Use dedicated test accounts and synthetic resources for anonymous, authenticated, low-privilege, peer-tenant, administrator, service, expired, revoked, and recovery states.
3. Trace direct server-side requests rather than trusting UI visibility; test object identifiers, tenant binding, role transitions, method changes, workflow order, replay, and concurrent sessions.
4. Review session and token issuance, expiry, rotation, revocation, audience, issuer, signature, CSRF model, cookie flags, recovery, and re-authentication controls.
5. Send only benign, minimally necessary variations and stop on unexpected data, privilege, or service impact.
6. Compare observed outcomes with the matrix; preserve redacted request/response evidence, identity state, timestamps, and exact preconditions.
7. Convert confirmed failures into a server-side fix, regression case, and retest plan.

## Verification

Check default-deny behavior, cross-tenant and horizontal/vertical privilege boundaries, expired and revoked states, recovery paths, audit events, and server-side enforcement through a second interface or direct API where approved.

## Safety and non-goals

Do not use real accounts, guess credentials, brute-force, harvest tokens, access another user’s data, alter durable records, or treat a denial as permission to escalate further. Never request or retain credentials when a safer user-side action is available. Redact secrets, tokens, PII, and private topology from reports.

## Remediation and retest

Prefer a narrow, owner-assigned fix at the boundary that enforces the security property. Record the change, regression or acceptance test, deployment or configuration version, rollback consideration, and residual risk. If this skill only produces intake, mapping, or evidence, hand the confirmed issue to the findings and remediation skills rather than claiming it is fixed.

## Handoff

Return the authorization matrix, identities and synthetic assets used, flows tested, redacted evidence, confirmed or suspected findings, remediation, regression tests, retest status, residual risk, and excluded paths.
