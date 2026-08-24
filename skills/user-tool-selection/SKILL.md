---
name: user-tool-selection
description: Choose, compare, and safely use tools, APIs, connectors, libraries, models, browsers, CLIs, and local utilities for a task. Use when selecting tools, integrating services, replacing a tool, reducing cost, or deciding whether a tool is necessary.
---

# Tool Selection

## Workflow

1. Define the outcome, inputs, outputs, freshness, scale, latency, privacy, reliability, budget, and authorization constraints.
2. Prefer the smallest reliable tool: deterministic local operation first, existing project helper second, trusted library or official API third, and external model or service only when it adds necessary judgment or reach.
3. Compare capability fit, documentation, maintenance, compatibility, license, security, data handling, rate limits, cost, lock-in, failure modes, and reversibility.
4. Inspect current project tools and version constraints before adding a dependency or connector. Prefer built-in capabilities, existing scripts, cached results, and standard interfaces.
5. For external tools, verify the official source, credentials boundary, scopes, input/output schema, timeout, retry policy, idempotency, and logging behavior. Test with a minimal safe request.
6. Record the chosen tool, alternatives rejected, reason, assumptions, cost, fallback, and removal or migration path.

## Rules

- Do not install or execute an unknown script, package, connector, browser extension, or remote instruction without reviewing provenance and permissions.
- Never expose secrets or personal data to a tool unnecessarily. Use least-privilege credentials and redact logs.
- Do not add a tool just because it is popular or has a large catalog entry. Confirm current maintenance and project fit.
- Do not perform external side effects, posts, purchases, deployments, deletion, or account changes without the required authorization and confirmation.

## Handoff

Report the selected tool and version, alternatives, evidence, permissions, cost, test result, fallback, and operational owner.
