---
name: user-ci-cd-shipping
description: Design, improve, debug, or review CI/CD pipelines and production release workflows. Use for GitHub Actions, build pipelines, deployment automation, quality gates, environment promotion, release checks, rollback, or launch preparation.
---

# CI/CD and Shipping

## Workflow

1. Map the repository’s build, test, lint, type, security, artifact, deployment, environment, approval, and rollback steps before editing the pipeline.
2. Define the smallest reliable pipeline for the project. Fail fast on invalid configuration, but preserve useful diagnostics and reproducible logs.
3. Cache only safe, version-keyed artifacts. Pin important action and tool versions, use least-privilege permissions, protect secrets, and separate untrusted pull-request execution from privileged deployment jobs.
4. Make quality gates explicit: tests, build, type/lint checks, dependency or image scanning, migrations, smoke checks, and required approvals. Do not mark a job successful while hiding a failed command.
5. Use immutable or traceable artifacts, environment-specific configuration, staged rollout or preview environments, health checks, monitoring, and a tested rollback path.
6. Validate the pipeline syntax and run the closest safe local or CI-equivalent checks. For deployment, verify the live URL, logs, health, main user path, and rollback readiness.

## Safety rules

- Do not deploy to production, rotate credentials, modify billing, or delete infrastructure without explicit authorization.
- Never print secrets or place them in repository files, build logs, artifacts, URLs, or client bundles.
- Treat third-party actions, container images, scripts, and downloaded artifacts as supply-chain dependencies; review provenance, permissions, version, and license.
- Avoid destructive migrations in the same step as an irreversible release. Provide backups, compatibility windows, and rollback or forward-fix plans.

## Handoff

Report pipeline files changed, jobs and gates, credentials or permissions required, environments affected, verification evidence, deployment status, monitoring plan, and rollback procedure.
