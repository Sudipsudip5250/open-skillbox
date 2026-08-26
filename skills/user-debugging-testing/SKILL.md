---
name: user-debugging-testing
description: Diagnose failures, reproduce bugs, isolate root causes, implement fixes, and verify regressions with efficient testing. Use when behavior is broken, an error appears, a test fails, performance degrades, or a change needs validation.
---

# Debugging and Testing

## Quick start

Use this skill when the request matches **Diagnose failures, reproduce bugs, isolate root causes, implement fixes, and verify regressions with efficient testing. Use when behavior is broken, an error appears, a test fails, performance degrades, or a change needs validation.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Diagnostic sequence

1. Capture the exact symptom, expected behavior, environment, input, timestamp, and reproducibility.
2. Reproduce the failure with the smallest reliable case. Preserve the original failing example.
3. Read the stack trace, logs, recent diff, configuration, and relevant data flow. Do not guess from the error message alone.
4. Form one or more hypotheses and design the cheapest discriminating check for each.
5. Trace the first point where actual state diverges from expected state. Fix the cause, not only the visible symptom.
6. Add or update a regression test that fails before the fix and passes after it.
7. Run focused tests, then related integration and full checks. Re-test the original reproduction and important edge cases.
8. Record root cause, fix, validation, and any remaining uncertainty.

## Test selection

| Change type | Minimum useful checks |
|---|---|
| Pure function | Unit tests for normal, boundary, invalid, and representative complex inputs |
| API or integration | Contract tests, authorization/error cases, and one realistic end-to-end path |
| UI behavior | Component or interaction tests plus a visual or browser check when relevant |
| Data migration | Dry run, row/count invariants, rollback or backup check, and post-migration validation |
| Performance | Stable benchmark, baseline comparison, realistic load, and resource observation |
| Configuration/deployment | Build, startup, health check, and environment-specific smoke test |

Avoid tests that merely reproduce implementation details. Prefer observable behavior and deterministic fixtures. Isolate time, randomness, network, filesystem, and external services when they make tests flaky or expensive.

## Failure report

State the symptom, reproduction, root cause, minimal fix, tests run, result, and residual risk. If the issue cannot be reproduced, say what was inspected and what evidence is still missing instead of presenting a hypothesis as fact.


## Reliability rules

Do not delete or weaken tests, suppress errors, add arbitrary waits, hide failures with silent fallbacks, or claim a root cause without evidence. If the failure cannot be reproduced, separate observed facts from hypotheses and identify the missing evidence.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **debugging-testing**, use this compact record:

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
