---
name: user-ai-agent-tool-permission-review
description: Review tool permissions, approval gates, data boundaries, and exfiltration paths in AI agents or model-integrated applications the user owns or is authorized to assess, using benign defensive evaluations.
---

# Authorized AI-Agent Tool Permission Review

## Quick start

Use this skill when the request matches **Review tool permissions, approval gates, data boundaries, and exfiltration paths in AI agents or model-integrated applications the user owns or is authorized to assess, using benign defensive evaluations.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Confirm ownership or written authorization, target scope, environment, evidence handling, rate limits, and stop conditions before active access or testing. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **ai-agent-tool-permission-review**, use this compact record:

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

Do not reveal hidden prompts, extract secrets, bypass guardrails, jailbreak models, invoke tools against unauthorized systems, create autonomous exploitation, or treat a successful refusal as the only security control. Never request or retain credentials when a safer user-side action is available. Redact secrets, tokens, PII, and private topology from reports.

## Remediation and retest

Prefer a narrow, owner-assigned fix at the boundary that enforces the security property. Record the change, regression or acceptance test, deployment or configuration version, rollback consideration, and residual risk. If this skill only produces intake, mapping, or evidence, hand the confirmed issue to the findings and remediation skills rather than claiming it is fixed.

## Handoff

Return ROE and system map, tool-permission matrix, benign cases and outcomes, data-flow and exfiltration findings, controls, evidence, severity and confidence, remediation, regression and retest status, and residual risk.
