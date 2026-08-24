---
name: user-codebase-modernization
description: Improve or modernize an existing codebase safely without unnecessary rewrites. Use for legacy cleanup, architecture drift, large modules, technical debt, framework migration, modularization, dead-code reduction, or maintainability improvement.
---

# Codebase Modernization

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

## Handoff

Report baseline, evidence and metrics, boundaries mapped, tests added, migration seam, compatibility strategy, data reconciliation, rollout and rollback plan, files changed, validation, and remaining technical debt.
