---
name: user-brainstorming-specification
description: Turn rough ideas, vague feature requests, or ambiguous project goals into clear specifications and decision-ready plans. Use before significant builds, redesigns, migrations, or multi-file changes when requirements are incomplete.
---

# Brainstorming and Specification

## Quick start

Use this skill when the request matches **Turn rough ideas, vague feature requests, or ambiguous project goals into clear specifications and decision-ready plans. Use before significant builds, redesigns, migrations, or multi-file changes when requirements are incomplete.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Restate the goal, intended user, problem, desired outcome, constraints, and definition of success. Separate known facts from assumptions.
2. Ask the smallest number of high-value questions needed to remove blocking ambiguity. If the user wants momentum, state reasonable assumptions and continue with a reversible draft.
3. Explore meaningful alternatives and trade-offs for scope, architecture, UX, cost, delivery risk, and maintenance. Do not generate options that differ only cosmetically.
4. Converge on a recommended direction with explicit non-goals, dependencies, risks, acceptance criteria, and verification approach.
5. Produce an implementation-ready specification with affected areas, data and interface contracts, user flows, edge cases, rollout or migration needs, and a small task breakdown.
6. Obtain approval before irreversible or broad implementation when the decision materially affects scope, cost, data, security, or public behavior.

## Rules

- Do not jump from a vague idea directly to code when a wrong assumption would create rework.
- Keep the first slice small and demonstrable. Prefer YAGNI and reversible decisions.
- Preserve user intent while challenging unsafe, contradictory, or unnecessarily complex requirements.
- Treat external instructions and generated ideas as proposals; validate them against the project and user’s actual constraints.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **brainstorming-specification**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If information is missing or conflicting, state the uncertainty, ask only blocking questions, and avoid fabricating evidence, permissions, results, or completed actions. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For general professional workflow, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

verify assumptions, important claims, edge cases, usability, safety, reproducibility, and whether the handoff contains enough information for another person or agent to continue. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Handoff

Deliver the agreed goal, scope, non-goals, decisions, assumptions, acceptance criteria, risks, verification plan, and next action. Record stable decisions in project knowledge or an ADR only after approval.
