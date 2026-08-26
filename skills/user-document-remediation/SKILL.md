---
name: user-document-remediation
description: Repair, improve, validate, or accessibility-remediate Word, PDF, spreadsheet, presentation, and converted document files. Use for document structure, headings, tables, alt text, reading order, metadata, form fields, broken conversion, or accessible deliverables.
---

# Document Remediation

## Quick start

Use this skill when the request matches **Repair, improve, validate, or accessibility-remediate Word, PDF, spreadsheet, presentation, and converted document files. Use for document structure, headings, tables, alt text, reading order, metadata, form fields, broken conversion, or accessible deliverables.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Identify the source format, target format, intended audience, accessibility target, conversion path, layout constraints, and whether the file contains sensitive data.
2. Inspect text, styles, headings, tables, links, images, alt text, metadata, page or slide order, reading order, form fields, formulas, and embedded objects. Preserve content and references unless changes are requested.
3. Repair structure before appearance: semantic headings, lists, table headers, language, navigation, labels, captions, meaningful alt text, logical reading order, and document properties.
4. Preserve visual quality: page breaks, contrast, font sizes, spacing, wrapping, formulas, slide layouts, and print or screen behavior. Avoid fixing one format while breaking another.
5. Convert using a reproducible toolchain and inspect both source and output. Test text extraction, links, reading order, keyboard or form operation, images, tables, formulas, and visual rendering.
6. Run format-appropriate accessibility or validation checks, then manually inspect representative pages, dense tables, long documents, and error-prone conversions.

## Rules

- Do not invent missing content, alt text meaning, citations, signatures, or form values. Ask when the intended meaning is unclear.
- Do not treat a PDF visual match as proof that text, structure, tags, links, or reading order survived conversion.
- Keep formulas, data, macros, embedded files, and metadata safe; do not execute untrusted macros or embedded code.
- Protect personal and confidential information in temporary files, screenshots, extracted text, and output artifacts.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **document-remediation**, use this compact record:

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

Report source and output formats, transformations, structural and accessibility repairs, validation evidence, visual inspection, preserved limitations, and any content requiring author confirmation.
