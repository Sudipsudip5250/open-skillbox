---
name: user-image-prompt-engineering
description: Plan and refine prompts for generated or edited images with composition, subject, style, text, safety, provenance, and owned or licensed asset boundaries. Use for lawful creative production.
---

# Image Prompt Engineering

## Quick start

Use this skill when the request matches **Plan and refine prompts for generated or edited images with composition, subject, style, text, safety, provenance, and owned or licensed asset boundaries. Use for lawful creative production.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Define purpose, audience, aspect ratio, subject, composition, mood, constraints, reference rights, required text, and what must not appear.

## Workflow

Write a structured prompt; separate subject, environment, camera or layout, lighting, typography, palette, style, constraints, and negative requirements; iterate one variable at a time; use references only when permitted; inspect text legibility, anatomy, accessibility, and provenance; record prompt and model settings.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define audience, purpose, format, voice, source material, version or jurisdiction, accessibility, asset rights, review owner, and the claims the deliverable is allowed to make. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **image-prompt-engineering**, use this compact record:

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

Check prompt-to-output fidelity, accidental logos or likenesses, readable text, rights and attribution, harmful or misleading content, and whether edits preserve the authorized asset’s integrity.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If the source is incomplete or an asset is not clearly permitted, mark the gap and use a placeholder or original alternative instead of inventing, copying, or removing rights information. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include vague style words, conflicting constraints, tiny text, unlicensed references, claiming a generated image is documentary evidence, and hiding material edits.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For writing and creative production, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Use owned, licensed, or user-provided assets with permission. Do not imitate a living person deceptively, remove third-party watermarks, bypass platform safeguards, or create fraud-enabling imagery. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return prompt versions, settings, references and rights, output selection, defects, edits, provenance note, and delivery assets.
