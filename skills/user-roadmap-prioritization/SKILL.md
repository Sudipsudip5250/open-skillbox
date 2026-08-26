---
name: user-roadmap-prioritization
description: Rank product or engineering opportunities with explicit evidence, capacity, sequencing, uncertainty, and trade-offs. Use for roadmap decisions, not personal investment advice.
---

# Roadmap Prioritization

## Quick start

Use this skill when the request matches **Rank product or engineering opportunities with explicit evidence, capacity, sequencing, uncertainty, and trade-offs. Use for roadmap decisions, not personal investment advice.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Define the decision horizon, available capacity, strategic constraints, outcome target, and evidence quality before scoring candidates.

## Workflow

Normalize candidate problems and outcomes; collect value, reach, confidence, effort, risk, dependencies, and time-criticality; choose a transparent scoring method; test sensitivity to assumptions; sequence prerequisites; distinguish committed, targeted, and exploratory work; record rejected options.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | State the user or service outcome, decision owner, evidence, time horizon, capacity, dependencies, risk, and explicit non-goals before recommending a plan. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **roadmap-prioritization**, use this compact record:

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

Recalculate scores independently, compare score changes under plausible assumptions, check capacity and dependencies, and verify that qualitative risks are not buried by a numeric score.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If evidence or ownership is missing, mark the item as a hypothesis, decision needed, or escalation rather than presenting a speculative commitment as a plan. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include false precision, scoring features instead of outcomes, ignoring maintenance, double-counting confidence, treating a framework score as a decision, and hiding strategic or ethical constraints.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For product and operations, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not imply guaranteed revenue or returns. Keep personal finance, investment, legal, and regulated decisions outside this information/process skill. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return the decision frame, candidate table, evidence and assumptions, scoring method, sensitivity, sequence, trade-offs, rejected options, owners, and review date.
