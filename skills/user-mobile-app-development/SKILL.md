---
name: user-mobile-app-development
description: Build, debug, optimize, or review native and cross-platform mobile applications. Use for Expo, React Native, Flutter, SwiftUI, Jetpack Compose, mobile navigation, gestures, permissions, offline behavior, push notifications, or iOS/Android release readiness.
---

# Mobile Application Development

## Quick start

Use this skill when the request matches **Build, debug, optimize, or review native and cross-platform mobile applications. Use for Expo, React Native, Flutter, SwiftUI, Jetpack Compose, mobile navigation, gestures, permissions, offline behavior, push notifications, or iOS/Android release readiness.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Inspect the framework and version, target platforms, build tooling, navigation, state, native modules, permissions, backend contracts, device support, and existing release configuration.
2. Define the mobile user flow, screen states, safe areas, keyboard behavior, touch targets, orientation, network assumptions, offline and retry behavior, lifecycle transitions, deep links, and accessibility requirements.
3. Follow platform conventions and the project’s existing architecture. Keep platform-specific code isolated, handle permission denial and unavailable capabilities, and avoid blocking the UI thread.
4. Optimize startup, lists, images, memory, animations, network, battery, and bundle size using measurements. Handle backgrounding, resume, process death, rotation, low connectivity, and stale state.
5. Test on representative iOS and Android versions or emulators, narrow and large screens, slow network, denied permissions, keyboard, screen reader, reduced motion, deep links, notifications, and upgrade paths.
6. Verify production builds, signing configuration, privacy disclosures, crash reporting, secure storage, API compatibility, and release rollback or staged rollout when relevant.

## Rules

- Never store secrets in the app bundle. Use secure platform storage and server-side authorization.
- Do not assume a browser-like environment, persistent process, filesystem path, permission state, or network connection.
- Respect platform accessibility, privacy, background-execution, and notification rules. Do not request permissions before explaining their user value.
- Do not claim device compatibility from an emulator-only check or one platform.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **mobile-app-development**, use this compact record:

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

Report framework and platform assumptions, screens and states changed, device/OS matrix, tests, performance evidence, permission and privacy behavior, build status, and unresolved release risks.
