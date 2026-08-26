---
name: user-responsive-design
description: Design, implement, review, or test responsive behavior across screen sizes, viewport widths, zoom levels, device orientations, input modes, and component containers. Use for breakpoint bugs, mobile layout failures, overflow, reflow, responsive images, adaptive navigation, or screen-size production readiness.
---

# Responsive Design

## Quick start

Use this skill when the request matches **Design, implement, review, or test responsive behavior across screen sizes, viewport widths, zoom levels, device orientations, input modes, and component containers. Use for breakpoint bugs, mobile layout failures, overflow, reflow, responsive images, adaptive navigation, or screen-size production readiness.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Define supported environments and critical flows: narrow phone, large phone, tablet, laptop, wide desktop, orientation changes, browser zoom, text scaling, touch, mouse, keyboard, and reduced-motion preferences. Use content-driven breakpoints rather than device-name assumptions.
2. Inspect the viewport meta tag, layout primitives, breakpoints, container widths, design tokens, typography, media sizing, sticky or fixed elements, navigation, tables, dialogs, forms, and existing responsive tests.
3. Build mobile-first and fluid where practical. Prefer flexible grid and flex layouts, relative units, intrinsic sizing, `min`/`max`/`clamp`, responsive media, and container queries for reusable components. Use media queries when the viewport or user preference is the correct input.
4. Define intentional changes at each layout state: stacking, navigation, density, content priority, controls, sidebars, tables, charts, dialogs, and touch targets. Never merely shrink a desktop layout until it becomes unusable.
5. Prevent overflow and layout shift. Check long words, localized text, empty and error states, large numbers, user-generated content, images, videos, code, tables, fixed headers, safe areas, and keyboard-visible mobile screens.
6. Verify a viewport matrix with real content at representative widths, zoom levels, orientations, themes, and input modes. Test keyboard focus, screen-reader order, touch targets, scroll containers, and screenshots or visual diffs. Record intentional two-dimensional regions such as tables or maps separately from accidental page overflow.

## Rules

- Do not target only a few named devices or trust one browser width. Responsive behavior must work between tested points.
- Do not use horizontal page scrolling to hide ordinary text or controls. Scope unavoidable two-dimensional scrolling to content that requires it and keep surrounding content usable.
- Do not disable zoom, rely on hover, or replace accessible controls with screen-size-specific hidden functionality.
- Keep responsive changes semantically equivalent unless a product decision explicitly changes content priority. Document any mobile-only or desktop-only behavior.
- Combine this skill with `user-frontend-styling`, `user-ui-ux-design`, `user-accessibility-audit`, `user-browser-testing`, and `user-visual-quality-review` when implementation and evidence are required.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **responsive-design**, use this compact record:

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

Report environment matrix, breakpoints or container rules, changed components, content and overflow cases, accessibility and input checks, screenshots or test evidence, known browser limitations, and unresolved responsive risks.
