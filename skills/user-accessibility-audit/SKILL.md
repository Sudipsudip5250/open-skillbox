---
name: user-accessibility-audit
description: Review and improve accessibility of websites, applications, documents, and user interfaces. Use for WCAG audits, keyboard navigation, screen readers, ARIA, color contrast, focus, forms, touch targets, accessible documents, or accessibility production readiness.
---

# Accessibility Audit

## Workflow

1. Identify users, assistive technologies, platforms, critical flows, content types, target conformance level, and project-specific accessibility requirements. Treat WCAG as a baseline, not a substitute for user testing.
2. Inspect semantic structure, headings, landmarks, labels, names and descriptions, focus order, keyboard operation, dialogs, forms, error recovery, tables, media alternatives, language, zoom, text scaling, contrast, motion, and responsive reflow.
3. Run automated checks for obvious violations, then perform manual keyboard and screen-reader-oriented checks. Automated tools cannot prove understandable content, correct interaction semantics, or complete usability.
4. Test narrow and wide viewports, zoom and text scaling, high contrast or forced colors when relevant, reduced motion, touch targets, long labels, localization-like expansion, and dynamic updates.
5. Classify findings by affected user, severity, reproducibility, standard criterion, location, impact, remediation, and verification. Prioritize blockers in critical paths.
6. Re-test the original flow after fixes and record evidence. Include accessible names, focus behavior, error announcements, and alternative input paths.

## Rules

- Prefer native semantic HTML or platform controls before custom ARIA. Do not add ARIA that changes semantics incorrectly.
- Never rely on color, hover, animation, sound, or visual position alone to communicate meaning or operation.
- Do not claim conformance from an automated score or a single browser. State the scope, tools, manual checks, and limitations.
- Preserve user control over motion, timing, focus, and content scaling. Do not hide essential information behind inaccessible interactions.

## Handoff

Report scope and target baseline, automated and manual checks, findings mapped to criteria, affected flows, fixes, retest evidence, remaining barriers, and need for assistive-technology or user testing.
