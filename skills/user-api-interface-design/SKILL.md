---
name: user-api-interface-design
description: Design, review, or evolve APIs, schemas, module boundaries, and public interfaces. Use for REST, GraphQL, RPC, webhooks, SDKs, database contracts, service boundaries, or reusable component APIs.
---

# API and Interface Design

## Quick start

Use this skill when the request matches **Design, review, or evolve APIs, schemas, module boundaries, and public interfaces. Use for REST, GraphQL, RPC, webhooks, SDKs, database contracts, service boundaries, or reusable component APIs.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Identify consumers, use cases, trust boundaries, data ownership, compatibility requirements, version policy, error semantics, and performance constraints.
2. Define the contract before implementation: request and response shapes, types, required versus optional fields, validation, authentication, authorization, idempotency, pagination, ordering, rate limits, and failure behavior.
3. Keep the interface minimal and explicit. Avoid leaking storage schemas, ambiguous nulls, hidden side effects, and options that no consumer needs.
4. Validate untrusted input at the boundary and return stable, actionable errors without exposing secrets or internal details. Design retries and duplicate delivery behavior intentionally.
5. Implement contract tests and representative integration tests. Check backward compatibility, generated clients, documentation, migrations, observability, and failure paths.
6. Version or deprecate deliberately. Provide a migration path and do not silently change meanings or defaults.

## Rules

- Treat every observable behavior as part of the contract once consumers can depend on it.
- Prefer one canonical representation and consistent naming across endpoints and modules.
- Make ownership and direction of dependencies clear; avoid circular or feature-leaking interfaces.
- Do not invent requirements or breaking changes. State assumptions and ask when the compatibility target is unknown.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **api-interface-design**, use this compact record:

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

Report the contract, validation and error model, compatibility impact, tests, documentation, migration or deprecation plan, and unresolved decisions.
