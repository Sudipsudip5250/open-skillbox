---
name: user-database-security
description: Secure, review, or perform authorized tests against relational and NoSQL databases and application data access the user owns or is authorized to assess. Use for scoped PostgreSQL, MySQL, MariaDB, SQL Server, MongoDB, Redis, database permissions, encryption, backups, migrations, SQL injection defense, row-level security, or database production-readiness review.
---

# Database Security


## Authorization and Rules of Engagement

Before reviewing private assets or performing any active check, confirm that the user owns the target or has documented contractual authorization. Capture a short Rules of Engagement (ROE) record containing:

- **Authority:** owner, client, engagement reference, and who can approve scope changes.
- **In scope:** exact URLs, APIs, repositories, applications, accounts, cloud projects, hosts, CIDRs, environments, tenants, and test data.
- **Out of scope:** excluded assets, accounts, data classes, third parties, production actions, and techniques.
- **Window and controls:** time window, environment preference, test accounts, allowed tools, rate limits, notification contacts, evidence retention, and redaction rules.
- **Risk and stops:** whether production is permitted and who accepted the risk; stop on unexpected PII or secrets, instability, destructive impact, scope drift, or any signal that an action is no longer authorized.

Prefer local code, configuration, passive observation, fixtures, and non-production targets. If authority, scope, or stop contacts are missing or ambiguous, do not perform intrusive testing; ask for the missing boundary or limit work to passive and local analysis. Summarize the ROE before active testing and update it before any approved scope change.

## Workflow

1. Identify database engines and versions, data classification, application roles, administrative paths, network boundaries, replicas, backups, migrations, and recovery objectives.
2. Isolate the database from public access. Restrict network sources, management interfaces, ports, and service accounts to the smallest required set. Require strong transport protection and verify certificate behavior.
3. Apply least privilege: separate application read/write roles, migration and administrative roles, tenant or row-level boundaries, restricted extensions and procedures, and short-lived credentials where feasible.
4. Review application queries and parsers for parameterization, type and range validation, safe ORM usage, mass assignment, injection, unsafe deserialization, excessive result sets, and sensitive data exposure.
5. Protect data at rest and in backups. Define encryption and key ownership, retention, access auditing, restore testing, deletion behavior, masking in non-production, and migration rollback or forward-fix plans.
6. Verify with permission tests, negative cross-tenant tests, migration checks, backup restore tests, query review, logging review, and performance or denial-of-service safeguards.

## Rules

- Never connect a browser or thick client directly to a privileged database. Use a controlled server-side boundary.
- Do not store plaintext passwords, long-lived shared credentials, or secrets in source, images, logs, fixtures, or query strings.
- Do not assume an ORM prevents all injection or authorization bugs. Review generated queries and object-level access.
- Treat backups, replicas, exports, analytics copies, and development databases as sensitive data stores.
- Do not run destructive queries, migrations, resets, or production tests without authorization, backup checks, and a recovery plan.

## Assessment handoff template

Return a concise record with **authority and ROE**, assets and environment tested, out-of-scope items, time window, tools and versions, methods and limitations, and a findings table using: **ID | severity | confidence | asset/location | issue | evidence | impact | remediation | retest status**. Mark findings as confirmed, suspected, false positive, accepted risk, or needs investigation. Redact credentials, tokens, PII, exploit-enabling detail, and private topology. End with residual risk, owner or escalation path, and the next verification or review date.

## Remediation and retest

Prefer a narrow, owner-assigned fix at the boundary that enforces the security property. Record the change, regression or acceptance test, deployment or configuration version, rollback consideration, and residual risk. If this skill only produces intake, mapping, or evidence, hand the confirmed issue to the findings and remediation skills rather than claiming it is fixed.

## Handoff

Report engine and topology, network and identity controls, roles and permissions, data protections, query findings, backup/restore evidence, migration risks, residual exposure, and operational owners.
