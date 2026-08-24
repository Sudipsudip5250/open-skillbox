---
name: user-api-interface-design
description: Design, review, or evolve APIs, schemas, module boundaries, and public interfaces. Use for REST, GraphQL, RPC, webhooks, SDKs, database contracts, service boundaries, or reusable component APIs.
---

# API and Interface Design

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

## Handoff

Report the contract, validation and error model, compatibility impact, tests, documentation, migration or deprecation plan, and unresolved decisions.
