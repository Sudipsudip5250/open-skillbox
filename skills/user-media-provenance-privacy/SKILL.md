---
name: user-media-provenance-privacy
description: Inspect, preserve, validate, or selectively remove metadata from authorized images, audio, video, documents, and generated media. Use for EXIF/GPS privacy, IPTC/XMP, C2PA content credentials, provenance, media authenticity, publication hygiene, or metadata-leak review.
---

# Media Provenance and Privacy

## Quick start

Use this skill when the request matches **Inspect, preserve, validate, or selectively remove metadata from authorized images, audio, video, documents, and generated media. Use for EXIF/GPS privacy, IPTC/XMP, C2PA content credentials, provenance, media authenticity, publication hygiene, or metadata-leak review.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Confirm ownership or permission, source and derivative files, intended publication channel, privacy objective, required attribution, provenance needs, and whether the task is analysis, preservation, or cleanup.
2. Inventory metadata and embedded content: EXIF, GPS, timestamps, device identifiers, IPTC, XMP, ICC profiles, thumbnails, audio/video tags, document properties, C2PA manifests, filenames, paths, and file-system metadata.
3. Classify each field as required for rendering, accessibility, attribution, licensing, provenance, workflow, or unnecessary personal or operational data. Preserve a private original and record hashes or version identifiers.
4. Apply the smallest authorized change. Remove only unnecessary privacy-sensitive fields; preserve color profiles, captions, licensing, accessibility, provenance, and required technical metadata. If content credentials are present, explain the effect before changing them.
5. Validate the output by re-reading metadata, checking hashes and rendering, testing the target platform, and confirming that the requested privacy goal was met without claiming that every trace has disappeared.
6. Maintain a change record with source, tool and version, fields changed, output hash, reviewer, license, and publication decision.

## Rules

- This skill supports privacy protection and authorized cleanup only. It must not be used to evade attribution, copyright enforcement, platform safeguards, forensic review, moderation, or lawful investigation.
- Do not remove C2PA or provenance records merely to make content harder to detect or misattribute. Explain trade-offs and preserve the original.
- Do not claim that metadata removal erases all identifying traces; file content, visual fingerprints, server logs, upload records, and platform records may remain.
- Do not delete GPS, creator, license, or accessibility information when the project requires it or the user has not authorized removal.
- Do not process third-party media without confirmed rights and a legitimate privacy or publication purpose.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Confirm ownership or written authorization, target scope, environment, evidence handling, rate limits, and stop conditions before active access or testing. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **media-provenance-privacy**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If authorization, scope, or safe evidence handling is missing, pause and provide a planning-only alternative rather than probing, bypassing, or guessing. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For security and trust, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

redact secrets and personal data; preserve evidence integrity; distinguish observation from inference; verify fixes with a bounded retest; and escalate when scope or authority is unclear. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Handoff

Report authorization, original preservation, metadata inventory, fields changed or retained, provenance impact, validation results, residual traces, hashes, tool versions, and publication risks.
