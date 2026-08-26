---
name: user-frontend-styling
description: Design, implement, review, or refactor CSS and Tailwind styling in web applications. Use for utility classes, responsive layouts, themes, design tokens, hover/focus states, CSS architecture, dark mode, or style bugs.
---

# Frontend Styling

## Quick start

Use this skill when the request matches **Design, implement, review, or refactor CSS and Tailwind styling in web applications. Use for utility classes, responsive layouts, themes, design tokens, hover/focus states, CSS architecture, dark mode, or style bugs.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Inspect the framework, Tailwind or CSS version, build pipeline, existing tokens, component conventions, source scanning, reset, themes, and responsive breakpoints.
2. Define semantic color roles, typography, spacing, radii, elevation, motion, layering, and state tokens before adding one-off values. Reuse the project design system.
3. Build mobile-first layouts with clear containment, flex or grid behavior, intrinsic sizing, overflow handling, long-content behavior, and dark or high-contrast variants when relevant.
4. Implement states explicitly: loading, empty, success, error, disabled, hover, focus-visible, active, selected, invalid, and reduced-motion. Do not use hover as the only path.
5. Keep styles maintainable: avoid duplicated arbitrary values, specificity wars, unsafe global selectors, giant class strings, unused rules, and fragile DOM-dependent selectors. Use component boundaries and composition.
6. Verify responsive screenshots, keyboard focus, contrast, zoom, text expansion, reduced motion, layout shifts, browser support, and production CSS output.

## Rules

- Prefer semantic HTML and accessible focus-visible states. Never hide focus or communicate state by color alone.
- Avoid animating layout-heavy properties when transform or opacity communicates the same effect. Respect `prefers-reduced-motion`.
- Verify the installed Tailwind version and framework integration before using syntax from another release.
- Do not add gradients, glass effects, shadows, or decorative motion without a clear hierarchy or product purpose.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **frontend-styling**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If the failure is not reproducible, capture environment and logs, reduce the case, state uncertainty, and avoid speculative rewrites or destructive recovery steps. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For software and systems, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

run the narrowest relevant tests, type/build checks, runtime reproduction, compatibility checks, rollback review, and an inspection of the final diff for unintended behavior. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Handoff

Report styling architecture, tokens and files changed, responsive and state coverage, accessibility checks, browser limitations, build output, and remaining visual debt.
