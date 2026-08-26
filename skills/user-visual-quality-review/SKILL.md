---
name: user-visual-quality-review
description: Inspect and improve the visual quality of websites and applications using screenshots, rendered previews, and responsive comparisons. Use for visual QA, screenshot review, layout regressions, spacing, hierarchy, alignment, polish, or “make it look better” requests.
---

# Visual Quality Review

## Quick start

Use this skill when the request matches **Inspect and improve the visual quality of websites and applications using screenshots, rendered previews, and responsive comparisons. Use for visual QA, screenshot review, layout regressions, spacing, hierarchy, alignment, polish, or “make it look better” requests.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **visual-quality-review**, use this compact record:

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

Report baseline and target conditions, screenshots or preview routes, issues by severity, changes made, responsive and accessibility checks, visual differences accepted, and remaining polish opportunities.
