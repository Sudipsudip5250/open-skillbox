---
name: user-document-remediation
description: Repair, improve, validate, or accessibility-remediate Word, PDF, spreadsheet, presentation, and converted document files. Use for document structure, headings, tables, alt text, reading order, metadata, form fields, broken conversion, or accessible deliverables.
---

# Document Remediation

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

## Handoff

Report source and output formats, transformations, structural and accessibility repairs, validation evidence, visual inspection, preserved limitations, and any content requiring author confirmation.
