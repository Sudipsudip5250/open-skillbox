---
name: user-incident-response-runbooks
description: Create and execute safe, authorized incident-response runbooks for owned systems, covering preparation, detection, analysis, containment, eradication, recovery, communications, and lessons learned.
---

# Incident Response Runbooks

## Quick start

Use this skill when the request matches **Create and execute safe, authorized incident-response runbooks for owned systems, covering preparation, detection, analysis, containment, eradication, recovery, communications, and lessons learned.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Turn incident signals into coordinated, reversible actions with clear authority, evidence handling, service-protection priorities, and post-incident improvement. Create and execute safe, authorized incident-response runbooks for owned systems, covering preparation, detection, analysis, containment, eradication, recovery, communications, and lessons learned.

## Classification and inputs

Identify the request, audience, source materials, constraints, assumptions, permissions, version or jurisdiction, and required precision before selecting a method. Separate observed facts, user-provided inputs, calculations, model outputs, and interpretations.

## Workflow

1. Confirm the incident channel, incident commander, affected owner, authorization to act, severity criteria, communication contacts, and safety or legal constraints.
2. Record the initial signal, time, affected assets, current impact, confidence, evidence location, and what is not yet known; preserve volatile evidence without exposing secrets or PII.
3. Triage scope and business impact, protect people and critical services, and choose the least disruptive containment that limits further harm.
4. Coordinate eradication and recovery with system owners; preserve rollback, backups, change records, validation gates, and a decision log.
5. Communicate factual status, uncertainty, user impact, and next update time to the right audiences; do not speculate or disclose sensitive technical detail unnecessarily.
6. Verify recovery with health, security, data-integrity, monitoring, and access checks; then conduct a blameless review and track corrective actions.

## Runbook template

For each action, record **precondition → owner → command or decision → expected result → evidence → rollback or stop condition**. Keep preparation, detection, containment, recovery, communication, and closure steps separately addressable. Mark destructive or externally visible actions as approval-gated and define a safe dry run where practical.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | State the user or service outcome, decision owner, evidence, time horizon, capacity, dependencies, risk, and explicit non-goals before recommending a plan. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **incident-response-runbooks**, use this compact record:

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

## Verification and quality checks

Check authority and approvals, timeline consistency, evidence integrity, containment side effects, recovery health, credential rotation or access changes where applicable, monitoring coverage, and closure criteria.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If evidence or ownership is missing, mark the item as a hypothesis, decision needed, or escalation rather than presenting a speculative commitment as a plan. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include deleting evidence, making uncontrolled changes, confusing symptoms with root cause, communicating unverified claims, restoring a compromised artifact, and closing without monitoring or follow-up owners.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For product and operations, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Use only on incidents involving systems or organizations the user owns or is authorized to operate. Do not provide retaliation, unauthorized intrusion, destructive cleanup, anti-forensics, or public disclosure instructions. Follow the organization’s legal, privacy, safety, and regulatory process. Do not invent sources, data, results, approvals, or completed actions. Use the smallest relevant skill set and hand off to specialized research, security, data, accessibility, or implementation skills when the task crosses boundaries.

## Handoff

Return incident authority and severity, timeline, affected assets, evidence and limitations, decisions and approvals, containment/recovery status, communications, residual risk, corrective actions, owners, and next review date.
