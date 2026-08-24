---
name: user-software-engineering
description: Design, implement, review, refactor, and maintain production-quality software across languages, repositories, APIs, and services. Use for coding tasks, feature work, architecture decisions, code review, performance work, and technical debt.
---

# Software Engineering

## Engineering workflow

1. Inspect the repository, runtime, package manager, entry points, tests, local conventions, and deployment boundary.
2. Convert the request into observable behavior and acceptance criteria. Identify compatibility, security, performance, data, and migration constraints.
3. Trace the current implementation before changing it. Prefer the smallest coherent change that fits the existing architecture.
4. Design clear boundaries among input validation, domain logic, persistence or external calls, and presentation or transport.
5. Implement readable code with explicit names, narrow functions, predictable errors, minimal duplication, and secure defaults.
6. Update tests, schemas, types, documentation, configuration, and observability together when behavior changes.
7. Run focused checks first, then the broader test, lint, type, build, performance, and security checks available in the project.
8. Review the diff for accidental changes, secrets, dead code, backwards incompatibility, untested paths, and operational impact.

## Design priorities

Prefer correctness, clarity, testability, observability, accessibility, and secure defaults. Apply abstraction only when it removes repeated complexity or protects a stable boundary. Preserve public behavior unless a breaking change is requested and documented. Use adapters or dependency injection at external boundaries so tests do not require live services.

## Routing and boundaries

Use this skill for the general implementation lifecycle. Defer to focused modules for systematic debugging when behavior is broken, test-driven development when changing behavior requires behavior-first tests, code review for findings and approval, code simplification for behavior-preserving cleanup, modernization for legacy migration, dependency migration for version changes, API design for public contracts, and source-driven development for version-sensitive framework or library decisions.

For mathematics, science, education, finance, legal-document literacy, or other domain-specific work, load the relevant domain skill and use this skill only for implementation structure. For security, privacy, payments, personal data, external integrations, or production releases, load the appropriate security, privacy, payments, automation, and shipping skills.

## When not to use this skill

Do not use this as a substitute for a narrow bug-fix, code-review, migration, testing, security, or domain workflow when that skill is available. Do not use it to invent requirements, bypass authorization, weaken safety controls, or make regulated decisions on a user’s behalf. Do not begin a broad rewrite when a smaller verified change satisfies the acceptance criteria.

## Verification and deliverable

Verify observable behavior, edge cases, failure handling, input validation, data integrity, concurrency, cleanup, authorization, performance, portability, logging, tests, documentation, and deployment effects. Report files changed, behavior added or changed, commands and tests run with results, migration or deployment notes, known limitations, rollback needs, and unresolved risks. Never claim a test passed unless it was actually run.

Read debugging/testing and security-risk-review when the relevant conditions apply. Keep domain-specific facts and project conventions in project knowledge, not in this general skill.


## Rules

Do not invent requirements, bypass authorization, weaken safety or security checks, expose secrets, or begin a broad rewrite when a smaller verified change satisfies the acceptance criteria. Preserve public behavior unless a breaking change is requested and documented.
