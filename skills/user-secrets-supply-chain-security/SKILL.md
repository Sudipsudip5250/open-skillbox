---
name: user-secrets-supply-chain-security
description: Protect secrets, dependencies, build systems, artifacts, containers, and CI/CD supply chains. Use for secret leaks, key rotation, SBOM, dependency provenance, GitHub Actions security, package risk, artifact signing, or supply-chain production readiness.
---

# Secrets and Software Supply Chain

## Workflow

1. Inventory secrets, identities, dependencies, registries, build runners, actions, plugins, base images, artifacts, release channels, and consumers.
2. Establish secret ownership, least privilege, environment separation, centralized storage, access audit, expiration, rotation, revocation, backup, and break-glass procedures.
3. Scan source, history, logs, artifacts, images, and configuration for secrets. If a real secret is exposed, stop distribution, revoke or rotate it, investigate use, and remove it from future history where appropriate.
4. Generate and review an SBOM or dependency graph. Check advisories, transitive reachability, maintainer and package provenance, license, lockfile integrity, typosquatting signals, and update policy.
5. Harden CI/CD: pin or verify actions, minimize token permissions, isolate untrusted pull requests from privileged jobs, protect environments, review scripts, restrict artifact access, and avoid secret interpolation in logs or commands.
6. Verify release integrity with reproducible or traceable builds, checksums or signatures where appropriate, provenance metadata, image scanning, vulnerability gates, and a rollback or revocation path.
7. Exercise the incident path for leaked credentials, compromised dependency, malicious artifact, and runner compromise. Preserve evidence without exposing secrets.

## Rules

- Do not print, request, copy, or attach secret values. Use names, fingerprints, redacted samples, and user-side rotation instructions.
- Treat package registries, GitHub actions, containers, generated code, remote scripts, and model output as untrusted supply-chain inputs.
- Do not broadly ignore a vulnerability or secret finding. Use narrow, documented exceptions with owner and expiry.
- A scanner’s clean result does not prove provenance or security; combine automated checks with review and runtime controls.

## Handoff

Report assets and trust boundaries, secret findings and rotation status, dependency/SBOM results, CI permissions, artifact verification, incident actions, residual risk, and review cadence.
