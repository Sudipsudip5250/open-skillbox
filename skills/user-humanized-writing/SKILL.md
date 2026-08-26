---
name: user-humanized-writing
description: Make AI-assisted or overly formulaic writing sound natural, specific, clear, and appropriate to the author’s voice. Use for humanizing drafts, editing robotic prose, matching a writing sample, improving readability, or removing repetitive chatbot language.
---

# Humanized Writing

## Quick start

Use this skill when the request matches **Make AI-assisted or overly formulaic writing sound natural, specific, clear, and appropriate to the author’s voice. Use for humanizing drafts, editing robotic prose, matching a writing sample, improving readability, or removing repetitive chatbot language.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Identify the audience, purpose, format, factual sources, desired voice, and level of editing. Preserve the writer’s meaning, claims, citations, links, code, data, and frontmatter unless a change is requested.
2. Diagnose artificial patterns: inflated importance, vague authority, sales language, repeated sentence openings, forced groups of three, filler, excessive hedging, generic conclusions, excessive headings, overuse of bold or dashes, chatbot offers, and unsupported certainty.
3. Rewrite for directness and specificity. Use natural sentence variety, concrete verbs, appropriate paragraph length, plain language, and the writer’s genuine voice. Keep technical and reference prose neutral.
4. Check every factual detail against the supplied source or ask for missing details. Never invent names, dates, numbers, quotes, citations, personal experiences, or evidence to make prose sound human.
5. Compare the revision with the source for meaning, coverage, tone, and unintended claims. Show a concise change summary when the user needs transparency.

## Integrity boundary

This skill improves clarity, authenticity, and voice. It must not be used to impersonate a real person, conceal plagiarism, fabricate lived experience, misrepresent authorship, or evade academic, employment, platform, or security detection systems. If the user asks to bypass an AI detector, redirect to transparent editing for accuracy, originality, and appropriate disclosure.

## Modes

- **Light edit:** remove obvious robotic phrasing while preserving structure.
- **Voice match:** use a supplied writing sample only as a style reference, not as permission to impersonate its author.
- **Technical edit:** prioritize precision, reproducibility, and source fidelity over personality.
- **Content rewrite:** change structure only when it improves the reader’s task and preserve the factual ledger.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define audience, purpose, format, voice, source material, version or jurisdiction, accessibility, asset rights, review owner, and the claims the deliverable is allowed to make. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **humanized-writing**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If the source is incomplete or an asset is not clearly permitted, mark the gap and use a placeholder or original alternative instead of inventing, copying, or removing rights information. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For writing and creative production, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

review factual claims and citations, structure, readability, accessibility, timing or rendering, rights and attribution, placeholders, and whether the final wording overstates certainty. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Handoff

State what was changed, what was preserved, what remains uncertain, and whether the text still requires source review or author approval.
