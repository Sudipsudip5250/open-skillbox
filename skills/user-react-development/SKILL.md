---
name: user-react-development
description: Build, debug, refactor, or review React applications and components. Use for JSX, components, props, state, hooks, effects, context, rendering, composition, React Compiler, routing, or React performance and maintainability.
---

# React Development

## Quick start

Use this skill when the request matches **Build, debug, refactor, or review React applications and components. Use for JSX, components, props, state, hooks, effects, context, rendering, composition, React Compiler, routing, or React performance and maintainability.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Inspect the React version, framework, router, state and data libraries, build tool, component conventions, server/client boundaries, and existing tests.
2. Model the UI as components with clear responsibilities, stable props, semantic markup, predictable state ownership, and reusable composition. Prefer data flow that is easy to trace.
3. Use state only for changing data that affects rendering. Derive values where possible; keep effects for synchronization with external systems, not for ordinary calculations or event-driven logic.
4. Handle loading, empty, error, success, disabled, focus, optimistic, stale, and retry states. Make async work cancellable or race-safe and preserve user intent.
5. Use stable keys from data identity, avoid accidental remounts, prevent unnecessary re-renders through measurement, and keep boundaries clear when using server components or framework features.
6. Test behavior through user-visible interactions and focused unit or integration tests. Verify keyboard, responsive, error, network, and hydration or build behavior when relevant.

## Rules

- Follow the project’s installed React and framework version; consult current official documentation for version-sensitive APIs.
- Do not use effects to paper over unclear data flow, mutate state directly, or silence exhaustive-dependency warnings without understanding the lifecycle.
- Do not optimize with memoization, state libraries, or architecture changes without measuring the problem and checking readability.
- Keep authorization, secrets, and security decisions on trusted server boundaries. Client state is not a security boundary.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **react-development**, use this compact record:

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

Report component and state changes, effects and async behavior, tests, render or bundle evidence, accessibility and responsive checks, version assumptions, and remaining trade-offs.
