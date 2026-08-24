---
name: user-database-security
description: Secure, review, or test relational and NoSQL databases and application data access. Use for PostgreSQL, MySQL, MariaDB, SQL Server, MongoDB, Redis, database permissions, encryption, backups, migrations, SQL injection, row-level security, or database production readiness.
---

# Database Security

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

## Handoff

Report engine and topology, network and identity controls, roles and permissions, data protections, query findings, backup/restore evidence, migration risks, residual exposure, and operational owners.
