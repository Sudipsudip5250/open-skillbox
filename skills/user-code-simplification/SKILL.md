---
name: user-code-simplification
description: Simplify working code without changing intended behavior. Use when code is hard to read, over-abstracted, repetitive, deeply nested, bloated, or when a refactor should reduce maintenance complexity.
---

# Code Simplification

## Quick start

Use this skill when the request matches **Simplify working code without changing intended behavior. Use when code is hard to read, over-abstracted, repetitive, deeply nested, bloated, or when a refactor should reduce maintenance complexity.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Read tests, callers, project conventions, and the current behavior before editing. Preserve the reason behind unfamiliar code until it is understood.
2. Identify the actual complexity: branching, indirection, duplication, oversized files, unclear types, state coupling, dead code, or repeated policy decisions.
3. Choose the smallest structural remedy that reduces the number of concepts a reader must hold: delete unused paths, flatten control flow, extract a focused helper, clarify a type boundary, or split an owning module.
4. Keep behavior changes separate from simplification unless the behavior change is the explicit goal. Avoid broad rewrites and new abstractions without a real repeated use case.
5. Run focused tests before and after, then the broader suite, type/lint checks, build, and relevant runtime checks. Review the final diff for accidental changes.

## Rules

- Do not polish an abstraction that should be deleted. Do not relocate complexity and call it simplification.
- Do not remove code merely because it is unfamiliar; check references, history, feature flags, migrations, and external consumers first.
- Prefer canonical helpers and existing project patterns over near-duplicates.
- Ask before deleting uncertain dead code or compatibility behavior.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **code-simplification**, use this compact record:

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

Report the complexity removed, behavior preserved, tests and checks run, deleted or retained compatibility code, and any remaining structural debt.
