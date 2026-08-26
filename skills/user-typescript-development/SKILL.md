---
name: user-typescript-development
description: Build, refactor, migrate, or review TypeScript projects. Use for strict typing, generics, narrowing, type-safe APIs, tsconfig, JSX types, declaration files, JavaScript migration, or TypeScript compiler errors.
---

# TypeScript Development

## Quick start

Use this skill when the request matches **Build, refactor, migrate, or review TypeScript projects. Use for strict typing, generics, narrowing, type-safe APIs, tsconfig, JSX types, declaration files, JavaScript migration, or TypeScript compiler errors.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **typescript-development**, use this compact record:

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

Report type-model changes, boundary validation, compiler and version assumptions, errors resolved, tests and build checks, public API impact, and remaining unsafe areas.
