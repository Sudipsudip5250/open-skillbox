---
name: user-security-hardening
description: Review, secure, or harden applications, APIs, repositories, containers, integrations, and deployment workflows. Use for threat modeling, auth, permissions, input validation, secrets, dependency risk, supply chain, privacy, or security audits.
---

# Security Hardening

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

## Handoff

Report threat model, findings by severity, evidence, fixes, tests, credentials or permissions involved, residual risk, and recommended follow-up.
