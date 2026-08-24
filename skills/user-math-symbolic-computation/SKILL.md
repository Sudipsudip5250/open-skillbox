---
name: user-math-symbolic-computation
description: Use computer algebra systems such as SymPy to manipulate expressions, solve equations, differentiate, integrate, expand series, analyze matrices, and verify symbolic results.
---

# Mathematical Symbolic Computation

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

## Verification and quality checks

Substitute symbolic solutions back into the original expression, compare equivalent forms under stated assumptions, check domains and branches, test representative numerical values, and distinguish a solver failure from a false mathematical claim.

## Common errors

Common errors include simplifying under false assumptions, accepting extraneous roots, ignoring piecewise or complex branches, trusting a pretty expression, and using floating-point input when exact structure matters.

## Rules, safety, and non-goals

Do not execute untrusted code or expressions merely because a symbolic tool suggests it. Do not treat a CAS result as a proof, a numerical error bound, or professional advice without independent checks. Do not invent sources, data, results, approvals, or completed actions. Use the smallest relevant skill set and hand off to specialized research, security, data, accessibility, or implementation skills when the task crosses boundaries.

## Handoff

Return mathematical goal, assumptions, reproducible symbolic steps, exact result, approximation if used, verification, domain or branch caveats, software/version, and human interpretation.
