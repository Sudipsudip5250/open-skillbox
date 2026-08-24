---
name: user-infrastructure-cloud-security
description: Review and harden cloud, server, network, infrastructure-as-code, Kubernetes, serverless, and hosting security. Use for IAM, firewall rules, public exposure, IaC security, cloud configuration, Kubernetes, server hardening, or infrastructure production readiness.
---

# Infrastructure and Cloud Security

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

## Handoff

Report topology and exposure, identity findings, configuration and IaC issues, affected environments, remediation, tests, exceptions, monitoring, and recovery evidence.
