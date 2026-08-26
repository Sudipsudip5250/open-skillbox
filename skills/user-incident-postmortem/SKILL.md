---
name: user-incident-postmortem
description: Produce blameless incident postmortems with impact, timeline, contributing factors, detection, corrective actions, owners, and verification. Use after authorized operational or security incidents.
---

# Incident Postmortem

## Quick start

Use this skill when the request matches **Produce blameless incident postmortems with impact, timeline, contributing factors, detection, corrective actions, owners, and verification. Use after authorized operational or security incidents.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Establish incident scope, impact window, audience, confidentiality level, and evidence sources before assigning causes.

## Workflow

Preserve a factual timeline; quantify user and system impact; describe detection and response; identify contributing conditions and control gaps; distinguish proximate trigger from systemic factors; record what went well; define prioritized corrective actions with owners, due dates, verification, and residual risk.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | State the user or service outcome, decision owner, evidence, time horizon, capacity, dependencies, risk, and explicit non-goals before recommending a plan. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **incident-postmortem**, use this compact record:

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

Cross-check timestamps and logs, redact secrets and personal data, separate facts from hypotheses, validate action feasibility, and schedule a follow-up review that checks whether risk actually changed.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If evidence or ownership is missing, mark the item as a hypothesis, decision needed, or escalation rather than presenting a speculative commitment as a plan. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include blame, hindsight bias, unsupported root-cause certainty, missing near misses, action lists without owners, and closing the report without verification.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For product and operations, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Use only for owned or authorized systems and respect legal, privacy, employment, and disclosure processes. Do not include retaliation, anti-forensics, or unauthorized access instructions. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return executive summary, impact, timeline, detection and response, contributing factors, lessons, corrective-action table, owners, deadlines, verification, and residual risk.
