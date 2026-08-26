---
name: user-motion-interaction-design
description: Design, implement, review, or debug hover effects, transitions, keyframe animations, gestures, micro-interactions, and motion systems in web interfaces. Use for CSS/Tailwind/React animation, hover polish, scroll effects, state transitions, or motion accessibility.
---

# Motion and Interaction Design

## Quick start

Use this skill when the request matches **Design, implement, review, or debug hover effects, transitions, keyframe animations, gestures, micro-interactions, and motion systems in web interfaces. Use for CSS/Tailwind/React animation, hover polish, scroll effects, state transitions, or motion accessibility.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **motion-interaction-design**, use this compact record:

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

Report motion purpose, triggers and states, implementation mechanism, properties and timing, accessibility fallback, performance evidence, browser/device checks, and unresolved interaction risks.
