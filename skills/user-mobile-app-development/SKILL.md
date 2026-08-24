---
name: user-mobile-app-development
description: Build, debug, optimize, or review native and cross-platform mobile applications. Use for Expo, React Native, Flutter, SwiftUI, Jetpack Compose, mobile navigation, gestures, permissions, offline behavior, push notifications, or iOS/Android release readiness.
---

# Mobile Application Development

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

## Handoff

Report framework and platform assumptions, screens and states changed, device/OS matrix, tests, performance evidence, permission and privacy behavior, build status, and unresolved release risks.
