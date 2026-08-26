---
name: user-numerical-methods
description: Choose, apply, and validate numerical methods for roots, linear systems, interpolation, differentiation, integration, and ordinary differential equations. Use when exact algebra is unavailable or insufficient.
---

# Numerical Methods

## Quick start

Use this skill when the request matches **Choose, apply, and validate numerical methods for roots, linear systems, interpolation, differentiation, integration, and ordinary differential equations. Use when exact algebra is unavailable or insufficient.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Classify the problem, state variables and units, select a method that matches the assumptions, and separate exact reasoning, approximations, measurements, and interpretation. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **numerical-methods**, use this compact record:

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

Check residuals, convergence or bracketing, sensitivity to step size and precision, stability, units, boundary conditions, and whether the error estimate actually supports the reported digits.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If a premise, measurement, or notation is ambiguous, state the ambiguity and solve the defensible cases separately rather than inventing a value or experimental result. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include confusing a small residual with a small solution error, using Newton’s method without a safe initial region, ignoring ill-conditioning, over-reporting precision, and mistaking instability for physical behavior.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For mathematics and science, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not claim numerical accuracy without a tolerance or error argument. Do not use an unstable or uncontrolled computation for safety-critical, financial, medical, or infrastructure decisions without qualified review. Do not invent sources, data, results, approvals, or completed actions. Use the smallest relevant skill set and hand off to specialized research, security, data, accessibility, or implementation skills when the task crosses boundaries.

## Handoff

Return problem formulation, method and rationale, parameters, reproducible computation, convergence or error evidence, result with precision, sensitivity, limitations, and next validation step.
