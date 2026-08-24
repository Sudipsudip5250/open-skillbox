---
name: user-authorized-security-testing
description: Plan and perform authorized defensive security testing of applications, APIs, previews, containers, and infrastructure the user owns or is contractually authorized to assess. Use for scoped security QA, staging scans, penetration-test preparation, DAST, fuzzing, abuse-case testing, or production-readiness verification.
---

# Authorized Security Testing


## Authorization and Rules of Engagement

Before reviewing private assets or performing any active check, confirm that the user owns the target or has documented contractual authorization. Capture a short Rules of Engagement (ROE) record containing:

- **Authority:** owner, client, engagement reference, and who can approve scope changes.
- **In scope:** exact URLs, APIs, repositories, applications, accounts, cloud projects, hosts, CIDRs, environments, tenants, and test data.
- **Out of scope:** excluded assets, accounts, data classes, third parties, production actions, and techniques.
- **Window and controls:** time window, environment preference, test accounts, allowed tools, rate limits, notification contacts, evidence retention, and redaction rules.
- **Risk and stops:** whether production is permitted and who accepted the risk; stop on unexpected PII or secrets, instability, destructive impact, scope drift, or any signal that an action is no longer authorized.

Prefer local code, configuration, passive observation, fixtures, and non-production targets. If authority, scope, or stop contacts are missing or ambiguous, do not perform intrusive testing; ask for the missing boundary or limit work to passive and local analysis. Summarize the ROE before active testing and update it before any approved scope change.

## Authorization gate

Confirm ownership or written authorization, exact targets, test window, accounts, data boundaries, allowed techniques, rate limits, notification contacts, and stop conditions. If authorization or scope is unclear, limit work to passive review, local code, configuration, or a safe test fixture.

## Test plan

1. Define assets, threat model, entry points, roles, sensitive workflows, expected controls, and evidence requirements.
2. Map requirements to an appropriate verification baseline such as OWASP ASVS and map test scenarios to OWASP WSTG identifiers or project-specific acceptance criteria.
3. Start with non-destructive checks: dependency and secret scanning, configuration review, headers/TLS, authentication and authorization matrices, input validation, error handling, logging, and safe test data.
4. In an authorized non-production target, run controlled dynamic checks with conservative limits. Test anonymous, authenticated, unauthorized, malformed, replayed, cross-tenant, workflow-order, upload, rate-limit, and failure-recovery paths using benign inputs.
5. Preserve timestamps, target, tool and version, request class, response evidence, reproduction steps, expected impact, and confidence. Redact credentials, personal data, tokens, and exploit details that are not needed for remediation.
6. Validate fixes with the same test, regression tests, deployment checks, and a clean re-scan. Separate confirmed findings, suspected risks, environmental assumptions, and false positives.

## Safety boundary

Do not scan or exploit third-party, public, production, or private targets without explicit authorization. Do not brute-force, phish, exfiltrate, persist, evade detection, weaponize payloads, disrupt availability, or access data outside the agreed scope. Stop immediately on unexpected sensitive-data exposure or service instability.

## Assessment handoff template

Return a concise record with **authority and ROE**, assets and environment tested, out-of-scope items, time window, tools and versions, methods and limitations, and a findings table using: **ID | severity | confidence | asset/location | issue | evidence | impact | remediation | retest status**. Mark findings as confirmed, suspected, false positive, accepted risk, or needs investigation. Redact credentials, tokens, PII, exploit-enabling detail, and private topology. End with residual risk, owner or escalation path, and the next verification or review date.

## Handoff

Deliver scope and authorization, methodology, ASVS/WSTG mapping, findings by severity and confidence, redacted evidence, remediation, retest results, residual risk, and disclosure or escalation path.
