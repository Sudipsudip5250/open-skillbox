---
name: user-frontend-styling
description: Design, implement, review, or refactor CSS and Tailwind styling in web applications. Use for utility classes, responsive layouts, themes, design tokens, hover/focus states, CSS architecture, dark mode, or style bugs.
---

# Frontend Styling

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

## Handoff

Report styling architecture, tokens and files changed, responsive and state coverage, accessibility checks, browser limitations, build output, and remaining visual debt.
