---
name: user-ui-ux-design
description: Design, build, review, or improve user interfaces and user experiences. Use for UI/UX design, frontend visual polish, accessibility audits, responsive layouts, design systems, interaction design, or requests to make an interface look more professional.
---

# UI/UX Design

## Goal

Create interfaces that are clear, accessible, responsive, distinctive, and appropriate to the product rather than generic AI-styled screens.

## Workflow

1. Inspect the existing product, stack, routes, components, assets, and current visual language before changing it.
2. Clarify the primary user, task, content hierarchy, device targets, brand constraints, and success criteria. If the request is vague, propose a small design direction before implementation.
3. Choose a coherent design system: typography, color roles, spacing scale, radii, elevation, icon family, component states, and motion rules. Prefer existing tokens and components.
4. Design the main flow first. Cover loading, empty, success, validation, error, disabled, hover, focus, keyboard, touch, and permission states.
5. Implement semantic structure and accessible interaction. Use labels, correct landmarks, keyboard navigation, visible focus, sufficient contrast, alt text, and reduced-motion support.
6. Test at narrow mobile, tablet, and desktop widths. Check long text, localization-like expansion, zoom, overflow, safe areas, touch targets, and dark/light themes when relevant.
7. Verify with a running build and screenshots. Inspect console errors, layout shifts, focus order, interaction states, and visual consistency before reporting completion.

## Quality rules

- Do not use decorative gradients, glass, cards, or animation merely because they are fashionable; each visual choice needs a product reason.
- Never use color alone to communicate state. Do not use emoji as interface icons when a consistent icon set is available.
- Keep hierarchy obvious, actions identifiable, copy concise, and error messages actionable.
- Avoid giant headings, cramped dashboards, excessive rounded cards, inconsistent spacing, and placeholder content that changes the layout.
- Prefer progressive disclosure and simple flows over dense controls.
- Preserve existing behavior unless a UX change explicitly requires it.

## Handoff

Report the design direction, changed files, responsive and accessibility checks, screenshots or runtime evidence, unresolved trade-offs, and any new dependency or asset decision. For a complex visual system, save reusable tokens and component rules in project knowledge or a design-system file instead of repeating them in every task.
