---
name: user-stakeholder-update-status
description: Write concise evidence-backed project status updates with progress, risks, decisions needed, owners, and next checkpoints. Use for cross-team communication.
---

# Stakeholder Status Update

## Quick start

Use this skill when the request matches **Write concise evidence-backed project status updates with progress, risks, decisions needed, owners, and next checkpoints. Use for cross-team communication.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Set reporting period, audience, objective, source artifacts, confidence, and the level of detail appropriate for the stakeholder.

## Workflow

Summarize outcome and health; report completed, in progress, blocked, risks, decisions needed, scope or date changes, evidence links, owner, and next update; distinguish facts, estimates, and requests; lead with what changed since the last update.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | State the user or service outcome, decision owner, evidence, time horizon, capacity, dependencies, risk, and explicit non-goals before recommending a plan. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **stakeholder-update-status**, use this compact record:

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

Verify dates, percentages, dependency status, risk severity, and owner agreement; remove stale or speculative claims; check that requested decisions include consequence and deadline.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If evidence or ownership is missing, mark the item as a hypothesis, decision needed, or escalation rather than presenting a speculative commitment as a plan. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include activity lists without outcomes, hiding blockers, false precision, burying decisions, reporting stale status, and assigning risk without an owner.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For product and operations, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not manipulate metrics, conceal material risks, disclose confidential information, or promise outcomes unsupported by evidence. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return reporting period, executive summary, progress table, risks and mitigations, decisions needed, owners, dates, evidence, and next checkpoint.
