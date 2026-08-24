---
name: user-react-development
description: Build, debug, refactor, or review React applications and components. Use for JSX, components, props, state, hooks, effects, context, rendering, composition, React Compiler, routing, or React performance and maintainability.
---

# React Development

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

## Handoff

Report component and state changes, effects and async behavior, tests, render or bundle evidence, accessibility and responsive checks, version assumptions, and remaining trade-offs.
