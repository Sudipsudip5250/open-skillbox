---
name: user-rules-of-engagement-security
description: Establish and document authorization, scope, allowed methods, safety controls, evidence handling, and stop conditions before performing authorized defensive security testing on owned or contractually authorized systems.
---

# Rules of Engagement for Security Testing

## Purpose

Use this skill as the mandatory intake and safety gate before any active security assessment. It produces a short, reviewable ROE summary rather than performing technical testing itself.

## Authorization gate

Confirm ownership or documented contractual authorization before touching private or live assets. Load or create a short Rules-of-Engagement record with in-scope and out-of-scope assets, environment, time window, allowed methods, rate limits, data handling, notification contacts, and stop conditions. Prefer local review, fixtures, passive checks, and non-production. If authority or scope is ambiguous, stop active work and request the missing boundary.

## Workflow

1. Identify the owner, authorizing person, engagement or ticket reference, tester identity, target owner, and approval authority for scope changes.
2. Inventory exact in-scope assets: URLs, APIs, repositories, applications, accounts, cloud projects, hosts, CIDRs, tenants, environments, and approved test data.
3. Record out-of-scope assets, third parties, production actions, sensitive data classes, forbidden techniques, credential boundaries, and prohibited side effects.
4. Set the time window, environment preference, test accounts, allowed tools, request rate or concurrency limits, notification contacts, evidence retention, redaction rules, and incident escalation path.
5. Define stop conditions for unexpected PII or secrets, instability, destructive impact, scope drift, legal or policy uncertainty, or any action that no longer has approval.
6. Decide whether each planned test is passive, local, staging, or production and obtain explicit risk acceptance for any necessary production activity.
7. Output the ROE summary and obtain confirmation before active testing; record every approved scope change.

## Verification

Verify that every target and technique has an owner or approval, that exclusions are unambiguous, rate limits are feasible, test accounts are safe, notification contacts work, and the stop procedure is understood by the operator.

## Safety and non-goals

Do not use this skill to manufacture authorization, infer permission from public visibility, bypass a missing approval, or authorize credential theft, persistence, evasion, destructive testing, or third-party access. Never request or retain credentials when a safer user-side action is available. Redact secrets, tokens, PII, and private topology from reports.

## Remediation and retest

Prefer a narrow, owner-assigned fix at the boundary that enforces the security property. Record the change, regression or acceptance test, deployment or configuration version, rollback consideration, and residual risk. If this skill only produces intake, mapping, or evidence, hand the confirmed issue to the findings and remediation skills rather than claiming it is fixed.

## Handoff

Return authority, scope, exclusions, window, environment, methods, limits, data handling, contacts, stop conditions, risk acceptance, approval state, and the next authorized assessment skill.
