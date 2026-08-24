---
name: user-debugging-testing
description: Diagnose failures, reproduce bugs, isolate root causes, implement fixes, and verify regressions with efficient testing. Use when behavior is broken, an error appears, a test fails, performance degrades, or a change needs validation.
---

# Debugging and Testing

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
