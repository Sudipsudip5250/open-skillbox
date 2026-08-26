---
name: user-ci-cd-shipping
description: Design, improve, debug, or review CI/CD pipelines and production release workflows. Use for GitHub Actions, build pipelines, deployment automation, quality gates, environment promotion, release checks, rollback, or launch preparation.
---

# CI/CD and Shipping

## Quick start

Use this skill when the request matches **Design, improve, debug, or review CI/CD pipelines and production release workflows. Use for GitHub Actions, build pipelines, deployment automation, quality gates, environment promotion, release checks, rollback, or launch preparation.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **ci-cd-shipping**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If information is missing or conflicting, state the uncertainty, ask only blocking questions, and avoid fabricating evidence, permissions, results, or completed actions. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For general professional workflow, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

verify assumptions, important claims, edge cases, usability, safety, reproducibility, and whether the handoff contains enough information for another person or agent to continue. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Handoff

Report pipeline files changed, jobs and gates, credentials or permissions required, environments affected, verification evidence, deployment status, monitoring plan, and rollback procedure.
