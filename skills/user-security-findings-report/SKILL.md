---
name: user-security-findings-report
description: Turn evidence from an authorized security review of owned or contractually authorized systems into precise, severity-ranked, fix-oriented findings with reproducible verification and residual-risk reporting.
---

# Security Findings Report

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

## Safety and non-goals

Do not invent vulnerabilities, inflate severity, include unverified exploit claims as facts, expose private data, or publish sensitive details before the owner’s agreed disclosure process. Never request or retain credentials when a safer user-side action is available. Redact secrets, tokens, PII, and private topology from reports.

## Remediation and retest

Prefer a narrow, owner-assigned fix at the boundary that enforces the security property. Record the change, regression or acceptance test, deployment or configuration version, rollback consideration, and residual risk. If this skill only produces intake, mapping, or evidence, hand the confirmed issue to the findings and remediation skills rather than claiming it is fixed.

## Handoff

Return executive summary, ROE and coverage, methodology, findings table with ID/severity/confidence/asset/issue/evidence/impact/remediation/retest, limitations, residual risk, owners, and disclosure timeline.
