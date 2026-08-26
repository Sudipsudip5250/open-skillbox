---
name: user-skill-composition-workflows
description: Compose two or three focused skills with explicit handoffs, minimal context, conflict resolution, and verification. Use for multi-domain agent tasks.
---

# Skill Composition Workflows

## Quick start

Use this skill when the request matches **Compose two or three focused skills with explicit handoffs, minimal context, conflict resolution, and verification. Use for multi-domain agent tasks.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Classify the task, identify the smallest skill chain, define the output contract between steps, and resolve safety or authority conflicts before execution.

## Workflow

Choose orchestrator; select domain skill; add only necessary verification or delivery skill; specify inputs and outputs; preserve source and assumption context; run steps in dependency order; reconcile conflicting rules by applying the narrower safety boundary; verify the final artifact against the original acceptance criteria.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the agent host, available tools, instruction precedence, context budget, data boundary, approval gates, expected output, and the smallest skill chain that can complete the task. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **skill-composition-workflows**, use this compact record:

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

Check that each selected skill contributes unique value, context is not duplicated, handoff data is complete, no private project facts leak across tasks, and the final result can be traced to each stage.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If a host cannot load the canonical format or a tool is unavailable, preserve the source skill and document a reversible adapter or manual fallback rather than claiming compatibility. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include loading the full catalog, chaining overlapping skills, losing uncertainty at handoff, allowing a downstream skill to override authorization, and reporting a composed result without stage evidence.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For agent workflow and governance, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Never use composition to bypass a refusal, authorization gate, privacy control, or safety rule. Keep external actions separately authorized and require confirmation where appropriate. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return task classification, selected chain, stage contracts, context budget, conflict decisions, verification evidence, and final deliverable.
