---
name: user-podcast-show-notes-transcript-cleanup
description: Clean transcripts faithfully and produce show notes, timestamps, summaries, and quotes without inventing speech. Use for authorized recordings and published or approved episodes.
---

# Podcast Show Notes and Transcript Cleanup

## Quick start

Use this skill when the request matches **Clean transcripts faithfully and produce show notes, timestamps, summaries, and quotes without inventing speech. Use for authorized recordings and published or approved episodes.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Confirm recording ownership or permission, speakers, intended audience, transcript quality, sensitive content, editorial style, and whether verbatim accuracy or readability is the priority.

## Workflow

Preserve meaning and uncertainty; label speakers; remove only agreed disfluencies; mark inaudible sections; create timestamps and topic headings; summarize without adding facts; select quotes that remain faithful; flag names, claims, and sensitive content for review.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define audience, purpose, format, voice, source material, version or jurisdiction, accessibility, asset rights, review owner, and the claims the deliverable is allowed to make. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **podcast-show-notes-transcript-cleanup**, use this compact record:

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

Compare cleaned text with audio, verify speaker turns, timestamps, names, quotes, and links, check privacy and consent, and identify machine-transcription uncertainty.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If the source is incomplete or an asset is not clearly permitted, mark the gap and use a placeholder or original alternative instead of inventing, copying, or removing rights information. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include silently changing meaning, hallucinating missing words, misattributing speakers, inventing timestamps, and publishing private or defamatory material.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For writing and creative production, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Process only authorized recordings. Do not impersonate speakers, fabricate quotes, expose private data, or create deceptive edits. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return cleaned transcript, uncertainty markers, speaker list, show notes, timestamps, quote verification, privacy/consent status, and editorial review items.
