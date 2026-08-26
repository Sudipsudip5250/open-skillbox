---
name: user-systematic-debugging
description: Diagnose and fix bugs, failing tests, build errors, runtime errors, regressions, and unexpected behavior using a reproducible evidence-based process.
---

# Systematic Debugging

## Quick start

Use this skill when the request matches **Diagnose and fix bugs, failing tests, build errors, runtime errors, regressions, and unexpected behavior using a reproducible evidence-based process.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **systematic-debugging**, use this compact record:

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

Report the root cause, minimal fix, files changed, regression guard, commands and environments tested, remaining uncertainty, and rollback or follow-up needs.
