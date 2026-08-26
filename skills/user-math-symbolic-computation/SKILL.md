---
name: user-math-symbolic-computation
description: Use computer algebra systems such as SymPy to manipulate expressions, solve equations, differentiate, integrate, expand series, analyze matrices, and verify symbolic results.
---

# Mathematical Symbolic Computation

## Quick start

Use this skill when the request matches **Use computer algebra systems such as SymPy to manipulate expressions, solve equations, differentiate, integrate, expand series, analyze matrices, and verify symbolic results.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Combine mathematical modeling with controlled symbolic computation while preserving assumptions, exactness, reproducibility, and human-readable reasoning. Use computer algebra systems such as SymPy to manipulate expressions, solve equations, differentiate, integrate, expand series, analyze matrices, and verify symbolic results.

## Classification and inputs

Identify the request, audience, source materials, constraints, assumptions, permissions, version or jurisdiction, and required precision before selecting a method. Separate observed facts, user-provided inputs, calculations, model outputs, and interpretations.

## Workflow

1. Define symbols, domains, assumptions, units, and the exact mathematical object; avoid treating an input string as a trusted expression.
2. Choose simplify, expand, factor, solve, substitute, differentiate, integrate, series, matrix, logic, or ODE operations based on the mathematical goal.
3. Keep exact quantities exact until approximation is requested; record software version, transformation steps, solver options, and any branch or domain choices.
4. Inspect generated expressions for lost conditions, extra roots, branch cuts, arbitrary constants, unevaluated objects, and performance limits.
5. Explain the mathematics independently of the CAS output and use symbolic checks, numerical spot checks, or substitution into the original problem.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Classify the problem, state variables and units, select a method that matches the assumptions, and separate exact reasoning, approximations, measurements, and interpretation. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **math-symbolic-computation**, use this compact record:

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

## Verification and quality checks

Substitute symbolic solutions back into the original expression, compare equivalent forms under stated assumptions, check domains and branches, test representative numerical values, and distinguish a solver failure from a false mathematical claim.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If a premise, measurement, or notation is ambiguous, state the ambiguity and solve the defensible cases separately rather than inventing a value or experimental result. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include simplifying under false assumptions, accepting extraneous roots, ignoring piecewise or complex branches, trusting a pretty expression, and using floating-point input when exact structure matters.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For mathematics and science, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not execute untrusted code or expressions merely because a symbolic tool suggests it. Do not treat a CAS result as a proof, a numerical error bound, or professional advice without independent checks. Do not invent sources, data, results, approvals, or completed actions. Use the smallest relevant skill set and hand off to specialized research, security, data, accessibility, or implementation skills when the task crosses boundaries.

## Handoff

Return mathematical goal, assumptions, reproducible symbolic steps, exact result, approximation if used, verification, domain or branch caveats, software/version, and human interpretation.
