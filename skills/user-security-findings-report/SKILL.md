---
name: user-security-findings-report
description: Turn evidence from an authorized security review of owned or contractually authorized systems into precise, severity-ranked, fix-oriented findings with reproducible verification and residual-risk reporting.
---

# Security Findings Report

## Quick start

Use this skill when the request matches **Turn evidence from an authorized security review of owned or contractually authorized systems into precise, severity-ranked, fix-oriented findings with reproducible verification and residual-risk reporting.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose

Use after analysis or testing when the main need is a trustworthy security report. It separates confirmed vulnerabilities from hypotheses, assumptions, accepted risks, and false positives.

## Authorization gate

Confirm ownership or documented contractual authorization before touching private or live assets. Load or create a short Rules-of-Engagement record with in-scope and out-of-scope assets, environment, time window, allowed methods, rate limits, data handling, notification contacts, and stop conditions. Prefer local review, fixtures, passive checks, and non-production. If authority or scope is ambiguous, stop active work and request the missing boundary.

## Workflow

1. Confirm the report scope, ROE, asset inventory, time window, environment, methods, tools and versions, and limitations.
2. Normalize observations into one finding per root cause or independently remediable issue; deduplicate scanner output and trace each claim to evidence.
3. State affected location, preconditions, security property, impact, likelihood or exploitability rationale, affected versions or configurations, and confidence.
4. Assign a severity using the project’s approved rubric; explain why the rating is not higher or lower and distinguish technical impact from business impact.
5. Give a fix-first remediation that names the enforcing boundary, an owner, a safe regression test, and any migration or rollback consideration.
6. Redact secrets, PII, tokens, exploit-enabling detail, and private topology; preserve full evidence only in an authorized location.
7. Summarize patterns, confirmed coverage, untested areas, residual risk, disclosure path, and retest status.

## Verification

Have every material claim trace to a timestamped artifact or reproducible observation; check severity consistency, remediation feasibility, evidence redaction, affected-scope accuracy, and whether the report clearly states what was not tested.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Confirm ownership or written authorization, target scope, environment, evidence handling, rate limits, and stop conditions before active access or testing. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **security-findings-report**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If authorization, scope, or safe evidence handling is missing, pause and provide a planning-only alternative rather than probing, bypassing, or guessing. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For security and trust, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

redact secrets and personal data; preserve evidence integrity; distinguish observation from inference; verify fixes with a bounded retest; and escalate when scope or authority is unclear. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Safety and non-goals

Do not invent vulnerabilities, inflate severity, include unverified exploit claims as facts, expose private data, or publish sensitive details before the owner’s agreed disclosure process. Never request or retain credentials when a safer user-side action is available. Redact secrets, tokens, PII, and private topology from reports.

## Remediation and retest

Prefer a narrow, owner-assigned fix at the boundary that enforces the security property. Record the change, regression or acceptance test, deployment or configuration version, rollback consideration, and residual risk. If this skill only produces intake, mapping, or evidence, hand the confirmed issue to the findings and remediation skills rather than claiming it is fixed.

## Handoff

Return executive summary, ROE and coverage, methodology, findings table with ID/severity/confidence/asset/issue/evidence/impact/remediation/retest, limitations, residual risk, owners, and disclosure timeline.
