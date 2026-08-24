---
name: user-responsive-design
description: Design, implement, review, or test responsive behavior across screen sizes, viewport widths, zoom levels, device orientations, input modes, and component containers. Use for breakpoint bugs, mobile layout failures, overflow, reflow, responsive images, adaptive navigation, or screen-size production readiness.
---

# Responsive Design

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

## Handoff

Report environment matrix, breakpoints or container rules, changed components, content and overflow cases, accessibility and input checks, screenshots or test evidence, known browser limitations, and unresolved responsive risks.
