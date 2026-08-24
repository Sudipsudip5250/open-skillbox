---
name: user-typescript-development
description: Build, refactor, migrate, or review TypeScript projects. Use for strict typing, generics, narrowing, type-safe APIs, tsconfig, JSX types, declaration files, JavaScript migration, or TypeScript compiler errors.
---

# TypeScript Development

## Workflow

1. Inspect the TypeScript version, `tsconfig`, module and JSX settings, runtime, build tool, package manager, lint rules, test setup, declaration boundaries, and project strictness.
2. Model domain data with useful types, discriminated unions, branded or constrained values where needed, explicit public interfaces, and narrow unknown inputs at runtime.
3. Prefer inference for local implementation and explicit types at boundaries. Use generics when they express a real relationship; avoid type gymnastics that obscure behavior.
4. Treat external JSON, environment variables, storage, network responses, and user input as unknown until validated. Keep compile-time types aligned with runtime schemas.
5. Fix errors at the boundary or source of incorrect assumptions. Avoid `any`, unsafe assertions, non-null assertions, blanket suppression, and broad casts unless documented and localized.
6. Run typecheck, lint, tests, build, and representative runtime paths. Review generated declarations, module interop, source maps, and package exports when publishing.

## Rules

- Verify version-specific compiler behavior and options against the official TypeScript documentation.
- Do not claim type safety from a successful compile when runtime inputs are unvalidated.
- Preserve public API compatibility unless a breaking change is intentional, documented, and migrated.
- Prefer a small, truthful type model over a complex model that merely makes the compiler quiet.

## Handoff

Report type-model changes, boundary validation, compiler and version assumptions, errors resolved, tests and build checks, public API impact, and remaining unsafe areas.
