---
name: user-software-engineering
description: Design, implement, review, refactor, and maintain production-quality software across languages, repositories, APIs, and services. Use for coding tasks, feature work, architecture decisions, code review, performance work, and technical debt.
---

# Software Engineering

## Engineering workflow

1. Inspect the repository, runtime, package manager, entry points, tests, and local conventions.
2. Convert the request into behavior and acceptance criteria. Identify compatibility, security, performance, and migration constraints.
3. Trace the current implementation before changing it. Prefer the smallest coherent change that fits the existing architecture.
4. Design clear boundaries: input validation, domain logic, persistence or external calls, and presentation or transport.
5. Implement readable code with explicit names, narrow functions, predictable errors, and minimal duplication.
6. Update tests, schemas, types, documentation, and configuration together when behavior changes.
7. Run focused checks first, then the broader test, lint, type, build, and security checks available in the project.
8. Review the diff for accidental changes, secrets, dead code, backwards incompatibility, and untested paths.

## Design priorities

Prefer correctness, clarity, testability, observability, and secure defaults. Apply abstraction only when it removes repeated complexity or protects a stable boundary. Preserve public behavior unless the user requests a breaking change. Use dependency injection or adapters at external boundaries so tests do not require live services.

## Code review lens

Check behavior, edge cases, error handling, input validation, data integrity, concurrency, resource cleanup, authorization, performance, portability, logging, test coverage, and documentation. Distinguish blocking defects from optional improvements and explain each finding with location, impact, and fix.

## Deliverable

Report files changed, behavior added or changed, tests executed and their results, migration or deployment notes, and known limitations. Never claim a test passed unless it was actually run.

Read the debugging-and-testing module for failures and the security-risk-review module when code handles credentials, personal data, permissions, payments, or external integrations.
