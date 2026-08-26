---
name: user-differential-equations-intro
description: Model and solve introductory ordinary differential equations, initial-value problems, systems, and qualitative behaviors. Use for educational mathematics, science, and engineering problems.
---

# Introductory Differential Equations

## Quick start

Use this skill when the request matches **Model and solve introductory ordinary differential equations, initial-value problems, systems, and qualitative behaviors. Use for educational mathematics, science, and engineering problems.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Translate a changing quantity into an ODE, select a valid solution method, and interpret the solution with initial conditions, equilibria, units, and limits. Model and solve introductory ordinary differential equations, initial-value problems, systems, and qualitative behaviors. Use for educational mathematics, science, and engineering problems.

## Classification and inputs

Identify the request, audience, source materials, constraints, assumptions, permissions, version or jurisdiction, and required precision before selecting a method. Separate observed facts, user-provided inputs, calculations, model outputs, and interpretations.

## Workflow

1. Define independent and dependent variables, units, initial or boundary conditions, domain, and the physical or abstract quantity being modeled.
2. Classify order, linearity, autonomy, separability, forcing, and system structure before choosing a method.
3. Select separation, integrating factor, characteristic roots, undetermined coefficients, phase-plane reasoning, numerical integration, or a system formulation as appropriate.
4. Solve symbolically when possible, apply conditions only after exposing arbitrary constants, and state intervals where the solution is valid.
5. Interpret equilibria, stability, growth, oscillation, forcing, and parameter sensitivity without confusing a model with reality.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **differential-equations-intro**, use this compact record:

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

Substitute the solution into the original equation, apply every initial condition, check units and limiting behavior, compare with a numerical or graphical solution when useful, and test whether the chosen method’s assumptions hold.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If information is missing or conflicting, state the uncertainty, ask only blocking questions, and avoid fabricating evidence, permissions, results, or completed actions. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include losing arbitrary constants, applying an initial condition to the wrong variable, dividing by a quantity that can be zero, confusing stable and unstable equilibria, and reporting a numerical approximation as an exact solution.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For general professional workflow, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not infer real-world safety or control decisions from a toy model without domain review. Do not hide singular solutions, parameter assumptions, numerical error, or an interval of validity. Do not invent sources, data, results, approvals, or completed actions. Use the smallest relevant skill set and hand off to specialized research, security, data, accessibility, or implementation skills when the task crosses boundaries.

## Handoff

Return model and variables, classification, selected method, stepwise solution, conditions, domain, qualitative interpretation, verification, approximation error if applicable, and limitations.
