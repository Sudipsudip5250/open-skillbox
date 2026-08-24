---
name: user-authorized-security-testing
description: Plan and perform authorized defensive security testing of applications, APIs, previews, containers, and infrastructure. Use for security QA, staging scans, penetration-test preparation, DAST, fuzzing, abuse-case testing, or production-readiness verification.
---

# Authorized Security Testing

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

## Handoff

Deliver scope and authorization, methodology, ASVS/WSTG mapping, findings by severity and confidence, redacted evidence, remediation, retest results, residual risk, and disclosure or escalation path.
