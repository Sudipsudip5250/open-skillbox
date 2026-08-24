---
name: user-advanced-spreadsheet-modeling
description: Design auditable spreadsheet models with structured assumptions, formulas, scenarios, sensitivity analysis, controls, and decision-ready outputs. Use for operational, planning, analytical, or finance-oriented work.
---

# Advanced Spreadsheet Modeling

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

## Verification and quality checks

Reconcile source totals, test formula invariants, inspect blanks and errors, compare scenario deltas, check units and sign conventions, test extreme inputs, review circularity and manual overrides, and confirm the workbook recalculates reproducibly.

## Common errors

Common errors include mixing actuals and forecasts, using inconsistent periods, hard-coding assumptions, hiding manual overrides, treating sensitivity as probability, and reporting a model output without uncertainty or source notes.

## Rules, safety, and non-goals

Do not present a model as financial, legal, tax, investment, or operational advice for a person or organization without qualified review. Preserve raw inputs and never conceal a manual adjustment or unsupported assumption. Do not invent sources, data, results, approvals, or completed actions. Use the smallest relevant skill set and hand off to specialized research, security, data, accessibility, or implementation skills when the task crosses boundaries.

## Handoff

Return workbook structure, assumptions and sources, formulas or scripts, scenarios, key drivers, controls and reconciliations, sensitivity limits, known errors, review status, and decision-use caveats.
