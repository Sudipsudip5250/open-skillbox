---
name: user-javascript-node-development
description: Build, debug, refactor, or review modern JavaScript and Node.js applications. Use for JavaScript language behavior, modules, async code, HTTP servers, streams, workers, filesystem, package scripts, runtime errors, or Node performance.
---

# JavaScript and Node.js Development

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

## Handoff

Report runtime and module assumptions, changed paths, async and error behavior, security boundaries, tests, build output, performance evidence, and compatibility risks.
