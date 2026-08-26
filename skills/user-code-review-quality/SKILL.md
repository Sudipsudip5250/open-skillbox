---
name: user-code-review-quality
description: Review, improve, simplify, or assess code quality before merge or release. Use for code review, refactoring review, maintainability checks, architecture review, dependency review, or evaluating code produced by a human or agent.
---

# Code Review and Quality

## Quick start

Use this skill when the request matches **Review, improve, simplify, or assess code quality before merge or release. Use for code review, refactoring review, maintainability checks, architecture review, dependency review, or evaluating code produced by a human or agent.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Review order

1. Read the task, specification, acceptance criteria, project conventions, and tests before judging the implementation.
2. Review the change across correctness, readability and simplicity, architecture, security, and performance.
3. Check edge cases, error paths, state transitions, concurrency, input boundaries, external data, authorization, secrets, dependencies, and unbounded work.
4. Prefer structural remedies: remove duplicate branches, separate orchestration from business logic, keep feature logic in its owning module, make type boundaries explicit, and delete indirection that adds no clarity.
5. Review the verification story: tests, build, lint/type checks, runtime checks, screenshots for UI, benchmarks for performance, and migration or rollback evidence when relevant.

## Finding rules

- Lead with correctness, security, data loss, and release blockers. Use clear severity labels: Critical, Required, Optional, Nit, or FYI.
- Give evidence and a concrete remedy, not vague criticism. Do not rubber-stamp because tests pass or because an agent wrote the code.
- Separate feature work from broad refactors unless the refactor is required for safe implementation.
- Prefer small, focused changes. If a change is too large to understand and verify, split it into vertical slices or logical file groups.
- Review dependency additions and upgrades for necessity, maintenance, license, vulnerability exposure, lockfile changes, and bundle/runtime impact.
- Ask before deleting uncertain dead code; never leave known unreachable code without explaining why.

## Verdict

Approve only when the change meets the specification, preserves or improves code health, and has credible verification evidence. Request changes when a defect, security risk, architectural regression, missing regression test, or unverifiable claim remains. State accepted trade-offs explicitly.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **code-review-quality**, use this compact record:

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
