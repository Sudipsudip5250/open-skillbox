---
name: user-accessibility-audit
description: Review and improve accessibility of websites, applications, documents, and user interfaces. Use for WCAG audits, keyboard navigation, screen readers, ARIA, color contrast, focus, forms, touch targets, accessible documents, or accessibility production readiness.
---

# Accessibility Audit

## Quick start

Use this skill when the request matches **Review and improve accessibility of websites, applications, documents, and user interfaces. Use for WCAG audits, keyboard navigation, screen readers, ARIA, color contrast, focus, forms, touch targets, accessible documents, or accessibility production readiness.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **accessibility-audit**, use this compact record:

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

Report scope and target baseline, automated and manual checks, findings mapped to criteria, affected flows, fixes, retest evidence, remaining barriers, and need for assistive-technology or user testing.
