---
name: user-changelog-release-notes
description: Produce accurate changelogs and release notes with user impact, migration notes, known issues, and version traceability. Use for software, content, or product releases.
---

# Changelog and Release Notes

## Quick start

Use this skill when the request matches **Produce accurate changelogs and release notes with user impact, migration notes, known issues, and version traceability. Use for software, content, or product releases.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Identify release version, audience, date, change source, compatibility promise, and whether the note is public, internal, or customer-specific.

## Workflow

Collect merged changes and verified fixes; classify added, changed, fixed, deprecated, removed, security, and known issues; describe user impact; add migration or rollback notes; link relevant tickets or docs; state limitations and support path; preserve semantic versioning or the project’s own convention.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define audience, purpose, format, voice, source material, version or jurisdiction, accessibility, asset rights, review owner, and the claims the deliverable is allowed to make. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **changelog-release-notes**, use this compact record:

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

Cross-check each statement against the release artifact, test upgrade paths, verify links and versions, distinguish planned from shipped changes, and confirm that security details follow disclosure policy.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If the source is incomplete or an asset is not clearly permitted, mark the gap and use a placeholder or original alternative instead of inventing, copying, or removing rights information. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include documenting unreleased work, overstating compatibility, omitting breaking changes, hiding known issues, and mixing internal implementation details with user-relevant impact.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For writing and creative production, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not fabricate fixes, security claims, or support commitments. Redact private tickets, secrets, and exploit-enabling details. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return versioned notes, change categories, migration steps, known issues, references, verification status, and owner.
