---
name: user-remediation-verification-retest
description: Verify security fixes on systems the user owns or is authorized to assess by replaying approved evidence, checking regressions, and documenting retest status, residual risk, and closure conditions.
---

# Authorized Remediation Verification and Retest

## Quick start

Use this skill when the request matches **Verify security fixes on systems the user owns or is authorized to assess by replaying approved evidence, checking regressions, and documenting retest status, residual risk, and closure conditions.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose

Use after a finding has an implemented remediation. It verifies the security property and surrounding behavior without expanding scope or treating a single passing test as proof of overall security.

## Authorization gate

Confirm ownership or documented contractual authorization before touching private or live assets. Load or create a short Rules-of-Engagement record with in-scope and out-of-scope assets, environment, time window, allowed methods, rate limits, data handling, notification contacts, and stop conditions. Prefer local review, fixtures, passive checks, and non-production. If authority or scope is ambiguous, stop active work and request the missing boundary.

## Workflow

1. Load the original finding, ROE, asset and version, reproduction preconditions, expected fix, owner, and approved retest window.
2. Confirm the deployed artifact or configuration contains the intended change and identify adjacent paths, versions, feature flags, and migrations that could differ.
3. Reproduce the original benign test with the same account state and data where safe; capture the expected blocked or corrected behavior.
4. Run focused regression tests for neighboring roles, tenants, workflows, inputs, errors, logging, rate limits, and availability, using conservative limits.
5. Check for alternate interfaces or caches that could preserve the issue, but do not expand to unrelated assets without a new approval.
6. Classify the result as fixed, partially fixed, not fixed, unable to verify, false positive, accepted risk, or needs follow-up; explain evidence and residual risk.
7. Record closure approval, remaining owner actions, monitoring, and the next review date.

## Verification

Compare before and after evidence, confirm the deployed version, test both the vulnerable and protected paths, inspect regression signals, and ensure that no secrets or unexpected personal data entered the record.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **remediation-verification-retest**, use this compact record:

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

## Safety and non-goals

Do not retest production or third-party systems without approval, repeat disruptive actions, declare closure from a scanner-only result, or silently broaden the original scope. Never request or retain credentials when a safer user-side action is available. Redact secrets, tokens, PII, and private topology from reports.

## Remediation and retest

Prefer a narrow, owner-assigned fix at the boundary that enforces the security property. Record the change, regression or acceptance test, deployment or configuration version, rollback consideration, and residual risk. If this skill only produces intake, mapping, or evidence, hand the confirmed issue to the findings and remediation skills rather than claiming it is fixed.

## Handoff

Return original finding and scope, deployed version, retest cases, evidence, result classification, regression outcome, remediation confirmation, residual risk, closure authority, and follow-up date.
