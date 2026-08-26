---
name: user-brand-style-guide-application
description: Apply an existing brand style guide consistently across writing, interfaces, campaigns, and media while recording justified exceptions. Use for brand-governed content production.
---

# Brand Style Guide Application

## Quick start

Use this skill when the request matches **Apply an existing brand style guide consistently across writing, interfaces, campaigns, and media while recording justified exceptions. Use for brand-governed content production.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Collect the approved brand guide, audience, channel, asset rights, voice, visual tokens, accessibility requirements, and approval owner.

## Workflow

Extract reusable voice, terminology, colors, type, spacing, imagery, logo, and motion rules; map them to the deliverable; apply tokens consistently; check contrast and legibility; flag conflicts between brand and accessibility; document exceptions and approvals; package source and final assets.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define audience, purpose, format, voice, source material, version or jurisdiction, accessibility, asset rights, review owner, and the claims the deliverable is allowed to make. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **brand-style-guide-application**, use this compact record:

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

Compare output against the guide, test accessible contrast and text size, verify logo and asset permissions, check terminology, and obtain owner approval for deviations.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If the source is incomplete or an asset is not clearly permitted, mark the gap and use a placeholder or original alternative instead of inventing, copying, or removing rights information. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include treating a style example as a rule, using inaccessible colors, stretching logos, mixing voice, copying competitor identity, and hiding exceptions.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For writing and creative production, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Use only authorized brand assets and fonts. Do not counterfeit another brand, mislead audiences, or override accessibility, privacy, or platform rules for visual consistency. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return applied tokens, content/asset checklist, exceptions, accessibility checks, rights register, preview, and approval status.
