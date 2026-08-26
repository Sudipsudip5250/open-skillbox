---
name: user-codebase-modernization
description: Improve or modernize an existing codebase safely without unnecessary rewrites. Use for legacy cleanup, architecture drift, large modules, technical debt, framework migration, modularization, dead-code reduction, or maintainability improvement.
---

# Codebase Modernization

## Quick start

Use this skill when the request matches **Improve or modernize an existing codebase safely without unnecessary rewrites. Use for legacy cleanup, architecture drift, large modules, technical debt, framework migration, modularization, dead-code reduction, or maintainability improvement.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Establish the current baseline: repository state, architecture, ownership, runtime and dependency versions, build and deploy path, critical flows, known incidents, test coverage, performance, security, and operational constraints.
2. Map change points and boundaries: large or highly coupled modules, dependency direction, data ownership, public interfaces, side effects, configuration, persistence, and callers. Use measurements and evidence rather than aesthetic preference.
3. Protect current behavior with characterization tests, contract tests, snapshots, fixtures, metrics, or manual acceptance cases. Record behavior that is intentional, accidental, deprecated, or unknown.
4. Choose a reversible migration seam: extract an interface, introduce an adapter, isolate a module, wrap a dependency, or apply an incremental replacement. Keep commits focused and make one conceptual change at a time.
5. Migrate callers gradually, maintain compatibility where required, dual-read or dual-write only with explicit consistency controls, backfill and compare data when persistence moves, and monitor before cutting over.
6. Remove the legacy path only after tests, metrics, data reconciliation, production behavior, rollback readiness, and stakeholder acceptance support deletion. Update documentation, ownership, dependencies, and runbooks.
7. Re-run quality, security, performance, accessibility, and deployment checks. Report what improved and what debt remains.

## Rules

- Do not rewrite a working system wholesale merely because the code is old or unattractive.
- Do not delete code, data, tests, compatibility paths, or dependencies without proving they are unused or replacing their behavior.
- Do not hide behavior changes inside a refactor. Separate structural and functional changes when possible.
- Preserve rollback paths and avoid risky migrations without backups, reconciliation, observability, and an explicit recovery plan.
- Use `user-code-simplification` for small behavior-preserving cleanup, `user-dependency-migration` for version upgrades, `user-api-interface-design` for public boundaries, and `user-test-driven-development` or `user-systematic-debugging` for behavior protection.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **codebase-modernization**, use this compact record:

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

Report baseline, evidence and metrics, boundaries mapped, tests added, migration seam, compatibility strategy, data reconciliation, rollout and rollback plan, files changed, validation, and remaining technical debt.
