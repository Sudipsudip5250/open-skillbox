---
name: user-code-simplification
description: Simplify working code without changing intended behavior. Use when code is hard to read, over-abstracted, repetitive, deeply nested, bloated, or when a refactor should reduce maintenance complexity.
---

# Code Simplification

## Workflow

1. Read tests, callers, project conventions, and the current behavior before editing. Preserve the reason behind unfamiliar code until it is understood.
2. Identify the actual complexity: branching, indirection, duplication, oversized files, unclear types, state coupling, dead code, or repeated policy decisions.
3. Choose the smallest structural remedy that reduces the number of concepts a reader must hold: delete unused paths, flatten control flow, extract a focused helper, clarify a type boundary, or split an owning module.
4. Keep behavior changes separate from simplification unless the behavior change is the explicit goal. Avoid broad rewrites and new abstractions without a real repeated use case.
5. Run focused tests before and after, then the broader suite, type/lint checks, build, and relevant runtime checks. Review the final diff for accidental changes.

## Rules

- Do not polish an abstraction that should be deleted. Do not relocate complexity and call it simplification.
- Do not remove code merely because it is unfamiliar; check references, history, feature flags, migrations, and external consumers first.
- Prefer canonical helpers and existing project patterns over near-duplicates.
- Ask before deleting uncertain dead code or compatibility behavior.

## Handoff

Report the complexity removed, behavior preserved, tests and checks run, deleted or retained compatibility code, and any remaining structural debt.
