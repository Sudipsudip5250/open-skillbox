---
name: user-visual-quality-review
description: Inspect and improve the visual quality of websites and applications using screenshots, rendered previews, and responsive comparisons. Use for visual QA, screenshot review, layout regressions, spacing, hierarchy, alignment, polish, or “make it look better” requests.
---

# Visual Quality Review

## Workflow

1. Establish the target viewport, device pixel ratio, theme, browser, route, state, content, and visual reference. Capture a baseline before changing code.
2. Inspect macro hierarchy first: page structure, focal point, density, alignment, whitespace, contrast, readable width, and relationship between content and actions.
3. Inspect component consistency: typography, tokens, spacing, radii, borders, shadows, icon sizing, image cropping, states, and repeated patterns. Check loading, empty, error, disabled, hover, focus, active, and overflow states.
4. Compare narrow, medium, and wide viewports, long content, zoom, dark mode, reduced motion, and realistic data. Distinguish implementation defects from an intentional design difference.
5. Make the smallest coherent change using existing design tokens and components. Avoid adding decorative effects that do not improve comprehension or task completion.
6. Re-render and compare before/after screenshots. Check layout shift, overflow, clipping, focus visibility, console errors, and interaction behavior. Record unresolved visual trade-offs.

## Rules

- Do not judge visual quality from source code alone. Use a running preview or rendered evidence.
- Do not use screenshot pixel similarity as the only quality criterion; functional, responsive, accessible, and content-aware checks matter.
- Do not hide overflow or reduce font size to conceal a layout problem without understanding the content and interaction impact.
- Protect private data in screenshots and redact credentials, tokens, and personal information.

## Handoff

Report baseline and target conditions, screenshots or preview routes, issues by severity, changes made, responsive and accessibility checks, visual differences accepted, and remaining polish opportunities.
