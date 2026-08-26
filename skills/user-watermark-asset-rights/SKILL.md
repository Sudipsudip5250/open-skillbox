---
name: user-watermark-asset-rights
description: Manage visible or invisible watermarks, branding, attribution, licensing, and asset delivery for media that the user owns or is authorized to edit. Use for watermark placement, watermark removal from owned assets, copyright notices, license checks, provenance labels, or brand-safe exports.
---

# Watermark and Asset Rights Management

## Quick start

Use this skill when the request matches **Manage visible or invisible watermarks, branding, attribution, licensing, and asset delivery for media that the user owns or is authorized to edit. Use for watermark placement, watermark removal from owned assets, copyright notices, license checks, provenance labels, or brand-safe exports.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Establish ownership, license, permission to edit, intended use, target channels, attribution terms, brand rules, accessibility needs, and whether the asset contains third-party people, trademarks, or private information.
2. Record the original asset, source URL or contract, license, creator, checksum, and any provenance credentials. Keep an untouched original and a reversible working copy.
3. Choose the least intrusive authorized operation: create a visible watermark, position a brand mark, add a copyright or license notice, preserve or add provenance, or remove a watermark only when the requester owns or is authorized to modify the asset.
4. Make branding legible without covering essential content, faces, captions, controls, or accessibility information. Test crops, responsive sizes, compression, contrast, dark and light backgrounds, and target-channel rendering.
5. Verify the export visually and technically. Check dimensions, quality, transparency, metadata, embedded credentials, attribution, licensing text, and whether the watermark or label survives the intended delivery path.
6. Maintain a delivery record with source, authorization, operation, tool version, output hash, retained notices, and any platform-specific transformations.

## Rules

- Never remove another creator’s watermark, attribution, copyright notice, ownership signal, or provenance marker without explicit rights and a legitimate authorized purpose.
- Do not make content harder to detect, trace, attribute, moderate, or investigate. Do not provide anti-forensics or safeguard-evasion workflows.
- Do not imply ownership, endorsement, authenticity, or licensing that has not been verified.
- Do not use invisible watermarks or fingerprints to collect personal data, track people without notice, or create deceptive provenance.
- When rights, license scope, attribution, or permission is unclear, stop the edit and request documentation or use a clearly licensed replacement asset.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **watermark-asset-rights**, use this compact record:

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

Report rights basis, original preservation, watermark or label operation, placement and accessibility checks, provenance and metadata effect, target-channel tests, output hash, and unresolved legal or branding questions.
