---
name: user-test-driven-development
description: Implement features or bug fixes with behavior-first tests and a red-green-refactor workflow. Use when changing program behavior, adding APIs, fixing regressions, or when reliable automated coverage is required.
---

# Test-Driven Development

## Quick start

Use this skill when the request matches **Implement features or bug fixes with behavior-first tests and a red-green-refactor workflow. Use when changing program behavior, adding APIs, fixing regressions, or when reliable automated coverage is required.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **test-driven-development**, use this compact record:

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

Report the test-first change, focused and full-suite results, build/type/lint results, coverage gaps, and any tests that were intentionally deferred with reasons.
