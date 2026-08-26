---
name: user-video-script-storyboard
description: Plan original video scripts and storyboards with scene intent, narration, shot direction, timing, continuity, accessibility, and rights checks. Use for owned or licensed productions.
---

# Video Script and Storyboard

## Quick start

Use this skill when the request matches **Plan original video scripts and storyboards with scene intent, narration, shot direction, timing, continuity, accessibility, and rights checks. Use for owned or licensed productions.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Define audience, objective, format, duration, distribution, source assets, rights, tone, and required accessibility such as captions or audio description.

## Workflow

Create a beat sheet; write spoken text separately from on-screen text; assign scene purpose, shot, action, audio, duration, transition, asset source, and continuity; plan captions, lower thirds, alt descriptions, and review gates; mark generated or licensed material.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define audience, purpose, format, voice, source material, version or jurisdiction, accessibility, asset rights, review owner, and the claims the deliverable is allowed to make. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **video-script-storyboard**, use this compact record:

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

Read the script aloud, check timing, continuity, factual claims, caption accuracy, visual legibility, audio clarity, asset rights, and whether the storyboard can be produced with available resources.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If the source is incomplete or an asset is not clearly permitted, mark the gap and use a placeholder or original alternative instead of inventing, copying, or removing rights information. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include overcrowded scenes, unverified claims, missing transitions, captions that do not match speech, unclear rights, and writing visuals that cannot be produced.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For writing and creative production, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Use only owned, licensed, or clearly permitted assets. Do not imitate a real person deceptively, remove third-party rights markers, or include unsafe instructions. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return script, storyboard table, shot list, asset and rights register, timing, accessibility plan, production risks, and review checklist.
