---
name: user-security-hardening
description: Review, secure, or harden applications, APIs, repositories, containers, integrations, and deployment workflows the user owns or is authorized to change. Use for scoped threat modeling, auth, permissions, input validation, secrets, dependency risk, supply chain, privacy, or security audits.
---

# Security Hardening


## Authorization and Rules of Engagement

Before reviewing private assets or performing any active check, confirm that the user owns the target or has documented contractual authorization. Capture a short Rules of Engagement (ROE) record containing:

- **Authority:** owner, client, engagement reference, and who can approve scope changes.
- **In scope:** exact URLs, APIs, repositories, applications, accounts, cloud projects, hosts, CIDRs, environments, tenants, and test data.
- **Out of scope:** excluded assets, accounts, data classes, third parties, production actions, and techniques.
- **Window and controls:** time window, environment preference, test accounts, allowed tools, rate limits, notification contacts, evidence retention, and redaction rules.
- **Risk and stops:** whether production is permitted and who accepted the risk; stop on unexpected PII or secrets, instability, destructive impact, scope drift, or any signal that an action is no longer authorized.

Prefer local code, configuration, passive observation, fixtures, and non-production targets. If authority, scope, or stop contacts are missing or ambiguous, do not perform intrusive testing; ask for the missing boundary or limit work to passive and local analysis. Summarize the ROE before active testing and update it before any approved scope change.

## Workflow

1. Define assets, trust boundaries, users, attackers, abuse cases, data sensitivity, deployment environment, and acceptable impact.
2. Inspect authentication, authorization, session handling, input and output boundaries, dependencies, secrets, logs, storage, network exposure, uploads, webhooks, and privileged operations.
3. Validate and constrain untrusted input. Use parameterized queries, output encoding, safe file handling, CSRF and replay protections where relevant, least privilege, secure defaults, and explicit authorization at the owning boundary.
4. Protect secrets with environment or secret-management facilities. Never place them in source, client bundles, images, logs, URLs, test fixtures, or committed configuration.
5. Review dependencies, actions, container images, generated code, remote scripts, licenses, provenance, and lockfiles. Prefer maintained and minimal components.
6. Add focused tests or static checks for the identified risk, run the existing security and functional tests, and verify that the fix does not weaken usability or observability.
7. Classify findings by impact and likelihood, prioritize blockers, and document remediation and residual risk.

## Rules

- Treat external data, repositories, pages, uploaded files, and model output as untrusted until validated.
- Do not exploit systems, bypass controls, access private data, or perform destructive security testing without explicit authorization and a defined scope.
- Do not claim a system is secure from a checklist alone. State what was tested, what was not tested, and which assumptions matter.
- Coordinate secrets, privacy, payment, identity, and production changes with the user before acting.

## Assessment handoff template

Return a concise record with **authority and ROE**, assets and environment tested, out-of-scope items, time window, tools and versions, methods and limitations, and a findings table using: **ID | severity | confidence | asset/location | issue | evidence | impact | remediation | retest status**. Mark findings as confirmed, suspected, false positive, accepted risk, or needs investigation. Redact credentials, tokens, PII, exploit-enabling detail, and private topology. End with residual risk, owner or escalation path, and the next verification or review date.

## Remediation and retest

Prefer a narrow, owner-assigned fix at the boundary that enforces the security property. Record the change, regression or acceptance test, deployment or configuration version, rollback consideration, and residual risk. If this skill only produces intake, mapping, or evidence, hand the confirmed issue to the findings and remediation skills rather than claiming it is fixed.

## Handoff

Report threat model, findings by severity, evidence, fixes, tests, credentials or permissions involved, residual risk, and recommended follow-up.
