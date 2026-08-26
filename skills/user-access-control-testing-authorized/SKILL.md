---
name: user-access-control-testing-authorized
description: Test authentication and server-side authorization, object-level access, tenant isolation, roles, sessions, and recovery flows on applications the user owns or is authorized to assess, using controlled test identities.
---

# Authorized Access-Control Testing

## Quick start

Use this skill when the request matches **Test authentication and server-side authorization, object-level access, tenant isolation, roles, sessions, and recovery flows on applications the user owns or is authorized to assess, using controlled test identities.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Confirm ownership or written authorization, target scope, environment, evidence handling, rate limits, and stop conditions before active access or testing. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **access-control-testing-authorized**, use this compact record:

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

Do not use real accounts, guess credentials, brute-force, harvest tokens, access another user’s data, alter durable records, or treat a denial as permission to escalate further. Never request or retain credentials when a safer user-side action is available. Redact secrets, tokens, PII, and private topology from reports.

## Remediation and retest

Prefer a narrow, owner-assigned fix at the boundary that enforces the security property. Record the change, regression or acceptance test, deployment or configuration version, rollback consideration, and residual risk. If this skill only produces intake, mapping, or evidence, hand the confirmed issue to the findings and remediation skills rather than claiming it is fixed.

## Handoff

Return the authorization matrix, identities and synthetic assets used, flows tested, redacted evidence, confirmed or suspected findings, remediation, regression tests, retest status, residual risk, and excluded paths.
