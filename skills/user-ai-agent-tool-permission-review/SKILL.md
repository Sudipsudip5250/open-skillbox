---
name: user-ai-agent-tool-permission-review
description: Review tool permissions, approval gates, data boundaries, and exfiltration paths in AI agents or model-integrated applications the user owns or is authorized to assess, using benign defensive evaluations.
---

# Authorized AI-Agent Tool Permission Review

## Purpose

Use for a focused review of agent tool-permission overreach and data-flow controls. It complements AI application security and prompt-injection defense without providing jailbreak or safeguard-bypass recipes.

## Authorization gate

Confirm ownership or documented contractual authorization before touching private or live assets. Load or create a short Rules-of-Engagement record with in-scope and out-of-scope assets, environment, time window, allowed methods, rate limits, data handling, notification contacts, and stop conditions. Prefer local review, fixtures, passive checks, and non-production. If authority or scope is ambiguous, stop active work and request the missing boundary.

## Workflow

1. Load the ROE and map models, prompts, retrieved content, memory, tools, plugins, files, APIs, identities, secrets, outputs, and human approval boundaries.
2. Build a tool inventory with purpose, caller, input schema, data access, side effects, network reach, identity, rate limit, timeout, sandbox, and approval requirement.
3. Check least privilege, allowlists, server-side authorization, tenant isolation, argument validation, output validation, data-loss controls, and separation between untrusted content and executable instructions.
4. Create benign test cases for indirect instructions, conflicting content, malformed tool arguments, cross-tenant references, secret-like outputs, unauthorized side effects, replay, and approval bypass attempts without using real secrets or harmful payloads.
5. Observe whether the application—not the model alone—enforces policy, scopes data, logs decisions, blocks unsafe tools, and escalates consequential actions.
6. Trace any data-exfiltration path from source to retrieval, memory, tool, output, log, or external service and stop on unexpected private data.
7. Recommend deterministic controls, regression tests, monitoring, and a retest plan.

## Verification

Check tool permissions from the server-side identity, validate schemas and policy decisions, test approval and refusal paths, inspect redacted logs, verify tenant and data boundaries, and repeat after model, prompt, tool, or retrieval changes.

## Safety and non-goals

Do not reveal hidden prompts, extract secrets, bypass guardrails, jailbreak models, invoke tools against unauthorized systems, create autonomous exploitation, or treat a successful refusal as the only security control. Never request or retain credentials when a safer user-side action is available. Redact secrets, tokens, PII, and private topology from reports.

## Remediation and retest

Prefer a narrow, owner-assigned fix at the boundary that enforces the security property. Record the change, regression or acceptance test, deployment or configuration version, rollback consideration, and residual risk. If this skill only produces intake, mapping, or evidence, hand the confirmed issue to the findings and remediation skills rather than claiming it is fixed.

## Handoff

Return ROE and system map, tool-permission matrix, benign cases and outcomes, data-flow and exfiltration findings, controls, evidence, severity and confidence, remediation, regression and retest status, and residual risk.
