---
name: user-dependency-migration
description: Upgrade, replace, deprecate, or migrate libraries, runtimes, frameworks, APIs, schemas, and infrastructure dependencies safely. Use for version bumps, breaking changes, end-of-life packages, lockfile updates, compatibility work, or migration planning.
---

# Dependency and Migration Work

## Quick start

Use this skill when the request matches **Upgrade, replace, deprecate, or migrate libraries, runtimes, frameworks, APIs, schemas, and infrastructure dependencies safely. Use for version bumps, breaking changes, end-of-life packages, lockfile updates, compatibility work, or migration planning.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Inventory direct and transitive dependencies, versions, runtime constraints, consumers, configuration, generated clients, and deployment environments.
2. Read official release notes, migration guides, changelogs, deprecation notices, security advisories, and compatibility matrices for the exact versions involved.
3. Define the target state, non-goals, behavior compatibility, data migration, rollback or forward-fix plan, and acceptance criteria.
4. Upgrade one dependency or coherent group at a time. Update code and configuration using supported APIs; do not silently preserve deprecated behavior without documenting it.
5. Review the lockfile diff, licenses, transitive graph, bundle/image impact, and supply-chain provenance. Never hand-edit a lockfile.
6. Run focused tests, migration checks, full suite, type/lint checks, build, staging or runtime smoke tests, and rollback rehearsal when risk warrants it.

## Rules

- Do not upgrade everything in one untraceable change merely to save time.
- Do not infer compatibility from semver alone. Verify changelogs and actual behavior.
- Preserve backups and compatibility windows before destructive data or API migrations.
- If the dependency is unmaintained or risky, compare replacement, containment, or removal rather than assuming the newest alternative is best.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **dependency-migration**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If the failure is not reproducible, capture environment and logs, reduce the case, state uncertainty, and avoid speculative rewrites or destructive recovery steps. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For software and systems, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

run the narrowest relevant tests, type/build checks, runtime reproduction, compatibility checks, rollback review, and an inspection of the final diff for unintended behavior. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Handoff

Report current and target versions, sources, breaking changes, files and lockfile changes, tests, migration and rollback plan, security/license findings, and remaining compatibility risk.
