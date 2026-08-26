---
name: user-product-discovery
description: Investigate user problems, jobs, constraints, alternatives, evidence, and opportunity hypotheses before committing to a product solution. Use for discovery briefs, roadmap inputs, and product decisions.
---

# Product Discovery

## Quick start

Use this skill when the request matches **Investigate user problems, jobs, constraints, alternatives, evidence, and opportunity hypotheses before committing to a product solution. Use for discovery briefs, roadmap inputs, and product decisions.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Reduce solution bias by separating observed user problems from assumptions, validating the highest-risk hypotheses, and connecting evidence to a bounded decision. Investigate user problems, jobs, constraints, alternatives, evidence, and opportunity hypotheses before committing to a product solution. Use for discovery briefs, roadmap inputs, and product decisions.

## Classification and inputs

Identify the request, audience, source materials, constraints, assumptions, permissions, version or jurisdiction, and required precision before selecting a method. Separate observed facts, user-provided inputs, calculations, model outputs, and interpretations.

## Workflow

1. Define the target users, context, outcome, business or mission constraint, decision date, and what would make the discovery inconclusive.
2. Gather evidence from user research, support data, analytics, workflow observation, market or competitor research, and existing product constraints; label source and freshness.
3. Map jobs, pain points, current alternatives, triggers, barriers, willingness or ability to change, and affected stakeholders.
4. Rank hypotheses by uncertainty and consequence; choose the cheapest ethical test that can distinguish meaningful alternatives.
5. Synthesize evidence into problem statements, opportunity areas, acceptance signals, risks, and a recommendation with explicit confidence.
6. Keep discovery separate from solution design until the evidence supports a narrower product bet.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | State the user or service outcome, decision owner, evidence, time horizon, capacity, dependencies, risk, and explicit non-goals before recommending a plan. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **product-discovery**, use this compact record:

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

Triangulate claims across sources, distinguish stated preference from observed behavior, check sample and selection bias, test alternative explanations, document non-users or missing segments, and trace each recommendation to evidence.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If evidence or ownership is missing, mark the item as a hypothesis, decision needed, or escalation rather than presenting a speculative commitment as a plan. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include leading questions, treating a feature request as the underlying problem, generalizing from a few users, confusing competitor presence with demand, and hiding contradictory evidence.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For product and operations, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not fabricate interviews, market size, demand, revenue, or user consent. Protect personal data, avoid dark patterns, and do not make regulated or financial claims from weak discovery evidence. Do not invent sources, data, results, approvals, or completed actions. Use the smallest relevant skill set and hand off to specialized research, security, data, accessibility, or implementation skills when the task crosses boundaries.

## Handoff

Return users and context, evidence table, assumptions and confidence, opportunity map, tested hypotheses, decision options, recommendation or no-go, unresolved questions, and next discovery experiment.
