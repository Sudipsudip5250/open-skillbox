---
name: user-systematic-debugging
description: Diagnose and fix bugs, failing tests, build errors, runtime errors, regressions, and unexpected behavior using a reproducible evidence-based process.
---

# Systematic Debugging

## Process

1. **Reproduce:** Capture the exact command, environment, input, expected result, actual result, logs, stack trace, timing, and whether the failure is deterministic.
2. **Localize:** Map the failure to the smallest responsible layer: input, configuration, dependency, build, network, state, server, client, rendering, persistence, or deployment. Inspect code and history before editing.
3. **Reduce:** Create the smallest failing case or controlled experiment. Change one variable at a time and compare a known-good path where possible.
4. **Explain:** State a falsifiable root-cause hypothesis and the evidence supporting it. Do not patch symptoms or guess from the error message alone.
5. **Fix:** Apply the smallest safe change that addresses the cause and preserves intended behavior. Avoid unrelated refactors while the failure is unresolved.
6. **Guard:** Add or update a regression test, validation, invariant, logging signal, or monitoring check that would catch the same class of failure.
7. **Verify:** Re-run the original reproduction, focused tests, broader tests, build, and relevant runtime checks. Check for new warnings, performance regressions, and environment-specific behavior.

## Rules

- Keep a failure ledger: symptom, reproduction, hypothesis, experiment, result, fix, and verification.
- Prefer real evidence over confidence. If the issue cannot be reproduced, say what was inspected and what remains unknown.
- Do not delete tests, weaken assertions, suppress errors, increase arbitrary timeouts, or add silent fallbacks to make a failure disappear.
- For flaky or asynchronous failures, diagnose readiness and state transitions; use condition-based waits rather than fixed sleeps where possible.
- Stop before irreversible actions, data migrations, production changes, or credential changes unless the user has authorized them.

## Handoff

Report the root cause, minimal fix, files changed, regression guard, commands and environments tested, remaining uncertainty, and rollback or follow-up needs.
