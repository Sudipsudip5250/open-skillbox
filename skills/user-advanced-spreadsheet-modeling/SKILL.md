---
name: user-advanced-spreadsheet-modeling
description: Design auditable spreadsheet models with structured assumptions, formulas, scenarios, sensitivity analysis, controls, and decision-ready outputs. Use for operational, planning, analytical, or finance-oriented work.
---

# Advanced Spreadsheet Modeling

## Quick start

Use this skill when the request matches **Design auditable spreadsheet models with structured assumptions, formulas, scenarios, sensitivity analysis, controls, and decision-ready outputs. Use for operational, planning, analytical, or finance-oriented work.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Build a transparent workbook whose inputs, calculations, outputs, and checks remain traceable and reviewable without hiding assumptions inside formulas. Design auditable spreadsheet models with structured assumptions, formulas, scenarios, sensitivity analysis, controls, and decision-ready outputs. Use for operational, planning, analytical, or finance-oriented work.

## Classification and inputs

Identify the request, audience, source materials, constraints, assumptions, permissions, version or jurisdiction, and required precision before selecting a method. Separate observed facts, user-provided inputs, calculations, model outputs, and interpretations.

## Workflow

1. Define the decision, audience, time horizon, unit of analysis, source data, ownership, update cadence, and materiality of errors.
2. Separate input, calculation, output, control, and documentation areas; give each assumption a label, unit, source, date, and change owner.
3. Build formulas from stable keys and named assumptions; avoid duplicated hard-coded constants, hidden rows, circular references, and mixed time bases.
4. Add base, downside, upside, and user-defined scenarios; use sensitivity tables or controlled parameter changes to expose drivers rather than claiming a forecast is certain.
5. Add reconciliation totals, error flags, boundary tests, version metadata, protected formulas where appropriate, and a short model map.
6. Review the rendered workbook and recalculate in the target spreadsheet engine before delivery.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Declare unit of analysis, grain, schema, population, time window, denominator, provenance, missingness, and the decision the result must support before calculating. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **advanced-spreadsheet-modeling**, use this compact record:

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

Reconcile source totals, test formula invariants, inspect blanks and errors, compare scenario deltas, check units and sign conventions, test extreme inputs, review circularity and manual overrides, and confirm the workbook recalculates reproducibly.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If data is incomplete or definitions conflict, preserve the ambiguity, show the affected result, and request a source-of-truth decision instead of silently coercing values. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include mixing actuals and forecasts, using inconsistent periods, hard-coding assumptions, hiding manual overrides, treating sensitivity as probability, and reporting a model output without uncertainty or source notes.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For data and quantitative work, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not present a model as financial, legal, tax, investment, or operational advice for a person or organization without qualified review. Preserve raw inputs and never conceal a manual adjustment or unsupported assumption. Do not invent sources, data, results, approvals, or completed actions. Use the smallest relevant skill set and hand off to specialized research, security, data, accessibility, or implementation skills when the task crosses boundaries.

## Handoff

Return workbook structure, assumptions and sources, formulas or scripts, scenarios, key drivers, controls and reconciliations, sensitivity limits, known errors, review status, and decision-use caveats.
