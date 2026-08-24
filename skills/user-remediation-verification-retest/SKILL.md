---
name: user-remediation-verification-retest
description: Verify security fixes on systems the user owns or is authorized to assess by replaying approved evidence, checking regressions, and documenting retest status, residual risk, and closure conditions.
---

# Authorized Remediation Verification and Retest

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

## Safety and non-goals

Do not retest production or third-party systems without approval, repeat disruptive actions, declare closure from a scanner-only result, or silently broaden the original scope. Never request or retain credentials when a safer user-side action is available. Redact secrets, tokens, PII, and private topology from reports.

## Handoff

Return original finding and scope, deployed version, retest cases, evidence, result classification, regression outcome, remediation confirmation, residual risk, closure authority, and follow-up date.
