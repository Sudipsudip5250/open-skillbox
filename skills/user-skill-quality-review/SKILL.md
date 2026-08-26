---
name: user-skill-quality-review
description: Grade and improve modular skills for trigger quality, boundary, workflow, verification, safety, composition, and maintainability. Use for repository skill reviews and pull requests.
---

# Skill Quality Review

## Quick start

Use this skill when the request matches **Grade and improve modular skills for trigger quality, boundary, workflow, verification, safety, composition, and maintainability. Use for repository skill reviews and pull requests.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Review the skill as an agent-facing procedure: determine what task it triggers, what it excludes, and whether another skill already owns part of the work.

## Workflow

Check metadata, naming, scope, progressive disclosure, workflow actionability, assumptions, verification, failure modes, safety, source discipline, handoff, and composition. Assign an A–F grade with evidence; identify the smallest fixes that improve reliability; re-run validation; distinguish style preference from functional defect.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the agent host, available tools, instruction precedence, context budget, data boundary, approval gates, expected output, and the smallest skill chain that can complete the task. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **skill-quality-review**, use this compact record:

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

Use a representative prompt, compare routing against neighboring skills, inspect all relative links, check line count and headings, and verify that suggested fixes do not change intended behavior or erase safety boundaries.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If a host cannot load the canonical format or a tool is unavailable, preserve the source skill and document a reversible adapter or manual fallback rather than claiming compatibility. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include grading prose instead of behavior, rewarding length, overlooking unsafe ambiguity, demanding duplicated boilerplate, or recommending a rename that breaks users without a migration plan.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For agent workflow and governance, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not expose private content, invent failures, or approve a skill that facilitates unauthorized access, bypass, deception, or harmful instructions. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return grade, evidence table, blockers, prioritized fixes, overlap decision, validation result, and maintainer recommendation.
