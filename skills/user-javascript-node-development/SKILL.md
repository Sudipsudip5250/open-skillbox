---
name: user-javascript-node-development
description: Build, debug, refactor, or review modern JavaScript and Node.js applications. Use for JavaScript language behavior, modules, async code, HTTP servers, streams, workers, filesystem, package scripts, runtime errors, or Node performance.
---

# JavaScript and Node.js Development

## Quick start

Use this skill when the request matches **Build, debug, refactor, or review modern JavaScript and Node.js applications. Use for JavaScript language behavior, modules, async code, HTTP servers, streams, workers, filesystem, package scripts, runtime errors, or Node performance.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Inspect Node.js and JavaScript versions, module system, package manager, build and test scripts, runtime flags, environment configuration, and deployment target.
2. Preserve clear module boundaries and use the project’s ESM or CommonJS convention consistently. Prefer standard platform APIs and small dependencies.
3. Handle promises, cancellation, timeouts, retries, streams, backpressure, concurrency, and errors explicitly. Do not swallow failures or create unbounded work.
4. Validate external input, environment variables, URLs, file paths, request sizes, and serialized data at runtime. Keep secrets and privileged operations on trusted server paths.
5. Review filesystem, child-process, crypto, HTTP, TLS, worker, and package behavior for security, portability, resource limits, and graceful shutdown.
6. Run lint, typecheck when present, unit and integration tests, build, and representative runtime checks. Measure performance before changing event-loop, memory, stream, or worker behavior.

## Rules

- Consult the versioned Node.js and MDN documentation for runtime or language behavior that may have changed.
- Do not use `eval`, unsafe dynamic code, shell interpolation, unrestricted filesystem paths, or child processes with untrusted input.
- Do not assume asynchronous code is parallel, cancellable, ordered, or safe under retries without proving it.
- Keep dependency additions justified, locked, audited, and compatible with the project’s support matrix.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **javascript-node-development**, use this compact record:

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

Report runtime and module assumptions, changed paths, async and error behavior, security boundaries, tests, build output, performance evidence, and compatibility risks.
