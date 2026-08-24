---
name: user-numerical-methods
description: Choose, apply, and validate numerical methods for roots, linear systems, interpolation, differentiation, integration, and ordinary differential equations. Use when exact algebra is unavailable or insufficient.
---

# Numerical Methods

## Purpose and scope

Turn a mathematical problem into a controlled numerical computation with explicit discretization, error, stability, conditioning, and stopping criteria. Choose, apply, and validate numerical methods for roots, linear systems, interpolation, differentiation, integration, and ordinary differential equations. Use when exact algebra is unavailable or insufficient.

## Classification and inputs

Identify the request, audience, source materials, constraints, assumptions, permissions, version or jurisdiction, and required precision before selecting a method. Separate observed facts, user-provided inputs, calculations, model outputs, and interpretations.

## Workflow

1. State the mathematical problem, input scale, desired output, tolerances, units, and whether an exact or approximate answer is required.
2. Inspect conditioning, smoothness, domain, constraints, and available derivatives before choosing bisection, Newton, secant, elimination or factorization, interpolation, quadrature, finite differences, or time-stepping.
3. Choose step size, precision, initialization, stopping rule, and safeguards; distinguish truncation, round-off, iteration, and data error.
4. Compute with reproducible settings and preserve inputs, method, parameters, software version, and convergence trace.
5. Compare with a benchmark, refinement study, alternate method, residual, or known invariant before interpreting the result.

## Verification and quality checks

Check residuals, convergence or bracketing, sensitivity to step size and precision, stability, units, boundary conditions, and whether the error estimate actually supports the reported digits.

## Common errors

Common errors include confusing a small residual with a small solution error, using Newton’s method without a safe initial region, ignoring ill-conditioning, over-reporting precision, and mistaking instability for physical behavior.

## Rules, safety, and non-goals

Do not claim numerical accuracy without a tolerance or error argument. Do not use an unstable or uncontrolled computation for safety-critical, financial, medical, or infrastructure decisions without qualified review. Do not invent sources, data, results, approvals, or completed actions. Use the smallest relevant skill set and hand off to specialized research, security, data, accessibility, or implementation skills when the task crosses boundaries.

## Handoff

Return problem formulation, method and rationale, parameters, reproducible computation, convergence or error evidence, result with precision, sensitivity, limitations, and next validation step.
