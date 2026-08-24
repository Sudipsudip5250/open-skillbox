---
name: user-code-review-quality
description: Review, improve, simplify, or assess code quality before merge or release. Use for code review, refactoring review, maintainability checks, architecture review, dependency review, or evaluating code produced by a human or agent.
---

# Code Review and Quality

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
