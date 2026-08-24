---
name: user-test-driven-development
description: Implement features or bug fixes with behavior-first tests and a red-green-refactor workflow. Use when changing program behavior, adding APIs, fixing regressions, or when reliable automated coverage is required.
---

# Test-Driven Development

## Workflow

1. Read the requirement, existing behavior, project test conventions, and acceptance criteria. Identify the smallest observable behavior to change.
2. Write one focused failing test that expresses the desired behavior, including an important edge or error case when practical. Run it and confirm it fails for the expected reason.
3. Implement the smallest production change that makes the test pass. Do not add speculative abstractions or unrelated cleanup.
4. Refactor only after the focused test is green, preserving behavior and improving names, boundaries, duplication, or readability.
5. Add tests at the appropriate level: unit tests for pure logic, integration tests for boundaries and persistence, and end-to-end tests for critical user flows. Prefer deterministic behavior and meaningful assertions.
6. Run the focused test, the relevant suite, lint/type checks, build, and runtime checks. For UI, include accessible interaction and responsive checks when relevant.

## Rules

- A passing test that never failed is weak evidence; record the initial failure when possible.
- Test behavior and contracts, not private implementation details.
- Do not delete or weaken a failing test, add arbitrary sleeps, or mock away the behavior under test.
- Keep fixtures small and readable. Use realistic boundary values, invalid inputs, empty states, retries, permissions, and failure paths.
- For a bug fix, add a regression test that fails before the fix and passes afterward.

## Handoff

Report the test-first change, focused and full-suite results, build/type/lint results, coverage gaps, and any tests that were intentionally deferred with reasons.
