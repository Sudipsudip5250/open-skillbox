---
name: user-ui-ux-design
description: Design, build, review, or improve user interfaces and user experiences. Use for UI/UX design, frontend visual polish, accessibility audits, responsive layouts, design systems, interaction design, or requests to make an interface look more professional.
---

# UI/UX Design

## Quick start

Use this skill when the request matches **Design, build, review, or improve user interfaces and user experiences. Use for UI/UX design, frontend visual polish, accessibility audits, responsive layouts, design systems, interaction design, or requests to make an interface look more professional.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **ui-ux-design**, use this compact record:

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

Report the design direction, changed files, responsive and accessibility checks, screenshots or runtime evidence, unresolved trade-offs, and any new dependency or asset decision. For a complex visual system, save reusable tokens and component rules in project knowledge or a design-system file instead of repeating them in every task.
