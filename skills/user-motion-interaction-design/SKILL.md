---
name: user-motion-interaction-design
description: Design, implement, review, or debug hover effects, transitions, keyframe animations, gestures, micro-interactions, and motion systems in web interfaces. Use for CSS/Tailwind/React animation, hover polish, scroll effects, state transitions, or motion accessibility.
---

# Motion and Interaction Design

## Workflow

1. Define the user purpose of each motion: feedback, orientation, continuity, hierarchy, or state change. Identify trigger, start state, end state, interruption, and fallback.
2. Use the simplest mechanism that fits: CSS transitions or keyframes for simple visual changes, platform or framework animation primitives for coordinated state, and JavaScript only when interaction or measurement requires it.
3. Animate compositor-friendly properties such as transform and opacity where possible. Avoid unnecessary layout and paint work, infinite motion, excessive blur, and competing effects.
4. Cover hover, focus-visible, active, pressed, selected, disabled, loading, enter, exit, reduced-motion, touch, keyboard, and no-pointer paths. Hover must never be the only way to discover or operate a feature.
5. Keep timing, easing, distance, and stagger consistent with a small motion system. Make transitions interruptible and avoid delaying essential actions.
6. Verify in a real browser at target sizes and performance conditions. Check frame rate or long-task evidence when motion is complex, and test `prefers-reduced-motion`, keyboard focus, touch, and screen readers.

## Rules

- Respect reduced-motion preferences and provide an equivalent non-animated state.
- Do not use flashing, disorienting, parallax, auto-playing motion, or animation that hides content or blocks input.
- Do not animate layout properties when transform or opacity gives the same result without changing semantics.
- Keep motion subordinate to comprehension. Avoid adding hover or animation merely to make a screen appear more impressive.

## Handoff

Report motion purpose, triggers and states, implementation mechanism, properties and timing, accessibility fallback, performance evidence, browser/device checks, and unresolved interaction risks.
