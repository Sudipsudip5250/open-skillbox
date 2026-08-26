---
name: user-database-security
description: Secure, review, or perform authorized tests against relational and NoSQL databases and application data access the user owns or is authorized to assess. Use for scoped PostgreSQL, MySQL, MariaDB, SQL Server, MongoDB, Redis, database permissions, encryption, backups, migrations, SQL injection defense, row-level security, or database production-readiness review.
---

# Database Security

## Quick start

Use this skill when the request matches **Secure, review, or perform authorized tests against relational and NoSQL databases and application data access the user owns or is authorized to assess. Use for scoped PostgreSQL, MySQL, MariaDB, SQL Server, MongoDB, Redis, database permissions, encryption, backups, migrations, SQL injection defense, row-level security, or database production-readiness review.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.



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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Confirm ownership or written authorization, target scope, environment, evidence handling, rate limits, and stop conditions before active access or testing. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **database-security**, use this compact record:

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

Report engine and topology, network and identity controls, roles and permissions, data protections, query findings, backup/restore evidence, migration risks, residual exposure, and operational owners.
