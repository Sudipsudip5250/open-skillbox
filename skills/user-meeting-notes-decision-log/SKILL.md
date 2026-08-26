---
name: user-meeting-notes-decision-log
description: Convert meetings into accurate notes, decisions, owners, deadlines, risks, dissent, and follow-up actions. Use for project and operational coordination.
---

# Meeting Notes and Decision Log

## Quick start

Use this skill when the request matches **Convert meetings into accurate notes, decisions, owners, deadlines, risks, dissent, and follow-up actions. Use for project and operational coordination.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Identify meeting purpose, participants, confidentiality, decision authority, and whether the source is a transcript, live notes, or memory.

## Workflow

Separate discussion from decisions; capture the exact decision, rationale, alternatives, owner, due date, dependencies, risks, unresolved questions, and next checkpoint; mark uncertain or unattributed statements; link action items to the relevant project artifact.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | State the user or service outcome, decision owner, evidence, time horizon, capacity, dependencies, risk, and explicit non-goals before recommending a plan. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **meeting-notes-decision-log**, use this compact record:

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

Verify names, dates, decisions, and owners against the source; ask for confirmation where ambiguity matters; check that every decision has an owner and that sensitive content is appropriately redacted.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If evidence or ownership is missing, mark the item as a hypothesis, decision needed, or escalation rather than presenting a speculative commitment as a plan. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include turning suggestions into decisions, inventing consensus, losing dissent, assigning actions without agreement, and copying confidential discussion into a public log.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For product and operations, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not fabricate attendance, consent, commitments, or quotations. Respect recording laws, confidentiality, access control, and organizational retention policy. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return concise notes, decision table, action register, open questions, risks, source and confidence, redactions, and confirmation request.
