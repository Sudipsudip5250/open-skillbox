---
name: user-infrastructure-cloud-security
description: Review and harden cloud, server, network, infrastructure-as-code, Kubernetes, serverless, and hosting environments the user owns or is authorized to assess. Use for scoped IAM, firewall rules, public exposure, IaC security, Kubernetes, server hardening, cloud configuration, or infrastructure production-readiness review.
---

# Infrastructure and Cloud Security

## Quick start

Use this skill when the request matches **Review and harden cloud, server, network, infrastructure-as-code, Kubernetes, serverless, and hosting environments the user owns or is authorized to assess. Use for scoped IAM, firewall rules, public exposure, IaC security, Kubernetes, server hardening, cloud configuration, or infrastructure production-readiness review.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.



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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Confirm ownership or written authorization, target scope, environment, evidence handling, rate limits, and stop conditions before active access or testing. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **infrastructure-cloud-security**, use this compact record:

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

Report topology and exposure, identity findings, configuration and IaC issues, affected environments, remediation, tests, exceptions, monitoring, and recovery evidence.
