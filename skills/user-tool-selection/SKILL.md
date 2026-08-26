---
name: user-tool-selection
description: Choose, compare, and safely use tools, APIs, connectors, libraries, models, browsers, CLIs, and local utilities for a task. Use when selecting tools, integrating services, replacing a tool, reducing cost, or deciding whether a tool is necessary.
---

# Tool Selection

## Quick start

Use this skill when the request matches **Choose, compare, and safely use tools, APIs, connectors, libraries, models, browsers, CLIs, and local utilities for a task. Use when selecting tools, integrating services, replacing a tool, reducing cost, or deciding whether a tool is necessary.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the agent host, available tools, instruction precedence, context budget, data boundary, approval gates, expected output, and the smallest skill chain that can complete the task. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **tool-selection**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If a host cannot load the canonical format or a tool is unavailable, preserve the source skill and document a reversible adapter or manual fallback rather than claiming compatibility. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For agent workflow and governance, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

run a representative prompt, inspect tool traces and handoffs, test refusal and uncertainty behavior, verify no private context leaks, and compare against a fixed baseline when evaluating changes. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Handoff

Report the selected tool and version, alternatives, evidence, permissions, cost, test result, fallback, and operational owner.
