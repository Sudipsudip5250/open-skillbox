---
name: user-infrastructure-cloud-security
description: Review and harden cloud, server, network, infrastructure-as-code, Kubernetes, serverless, and hosting environments the user owns or is authorized to assess. Use for scoped IAM, firewall rules, public exposure, IaC security, Kubernetes, server hardening, cloud configuration, or infrastructure production-readiness review.
---

# Infrastructure and Cloud Security


## Authorization and Rules of Engagement

Before reviewing private assets or performing any active check, confirm that the user owns the target or has documented contractual authorization. Capture a short Rules of Engagement (ROE) record containing:

- **Authority:** owner, client, engagement reference, and who can approve scope changes.
- **In scope:** exact URLs, APIs, repositories, applications, accounts, cloud projects, hosts, CIDRs, environments, tenants, and test data.
- **Out of scope:** excluded assets, accounts, data classes, third parties, production actions, and techniques.
- **Window and controls:** time window, environment preference, test accounts, allowed tools, rate limits, notification contacts, evidence retention, and redaction rules.
- **Risk and stops:** whether production is permitted and who accepted the risk; stop on unexpected PII or secrets, instability, destructive impact, scope drift, or any signal that an action is no longer authorized.

Prefer local code, configuration, passive observation, fixtures, and non-production targets. If authority, scope, or stop contacts are missing or ambiguous, do not perform intrusive testing; ask for the missing boundary or limit work to passive and local analysis. Summarize the ROE before active testing and update it before any approved scope change.

## Workflow

1. Inventory accounts, environments, regions, networks, subnets, hosts, clusters, functions, storage, queues, registries, identities, public endpoints, and management planes.
2. Map trust boundaries and apply least privilege to human, workload, CI, and break-glass identities. Separate development, staging, and production.
3. Review network exposure, ingress and egress, segmentation, private endpoints, firewall and security-group rules, administrative access, TLS, DNS, metadata services, and service-to-service authentication.
4. Review IaC and manifests for public resources, wildcard permissions, plaintext secrets, insecure defaults, unpinned images, privileged containers, host mounts, unsafe capabilities, missing resource limits, and absent network policies.
5. Apply secure baselines, immutable or traceable artifacts, patching, backups, logging, monitoring, vulnerability scanning, configuration drift detection, and recovery testing.
6. Validate with static IaC checks, identity policy tests, container and image checks, non-production smoke tests, access-denial tests, and configuration review. Record exceptions with owner and expiry.

## Rules

- Do not change production infrastructure, firewall rules, IAM, DNS, certificates, backups, or deletion policies without explicit authorization and a rollback plan.
- Never use broad administrator permissions as a shortcut. Prefer scoped roles and temporary elevation.
- Treat public cloud metadata, object storage, snapshots, logs, images, and state files as sensitive.
- Do not claim cloud security from an IaC scan alone; verify effective runtime configuration and provider-side controls.

## Assessment handoff template

Return a concise record with **authority and ROE**, assets and environment tested, out-of-scope items, time window, tools and versions, methods and limitations, and a findings table using: **ID | severity | confidence | asset/location | issue | evidence | impact | remediation | retest status**. Mark findings as confirmed, suspected, false positive, accepted risk, or needs investigation. Redact credentials, tokens, PII, exploit-enabling detail, and private topology. End with residual risk, owner or escalation path, and the next verification or review date.

## Remediation and retest

Prefer a narrow, owner-assigned fix at the boundary that enforces the security property. Record the change, regression or acceptance test, deployment or configuration version, rollback consideration, and residual risk. If this skill only produces intake, mapping, or evidence, hand the confirmed issue to the findings and remediation skills rather than claiming it is fixed.

## Handoff

Report topology and exposure, identity findings, configuration and IaC issues, affected environments, remediation, tests, exceptions, monitoring, and recovery evidence.
