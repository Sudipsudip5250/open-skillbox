---
name: user-personal-finance-concepts
description: Explain budgeting, cash flow, debt, savings, insurance, taxes, diversification, fees, and risk concepts without personalized investment or financial advice. Use for general financial literacy.
---

# Personal Finance Concepts

## Quick start

Use this skill when the request matches **Explain budgeting, cash flow, debt, savings, insurance, taxes, diversification, fees, and risk concepts without personalized investment or financial advice. Use for general financial literacy.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Define the concept and jurisdictional sensitivity; distinguish education from a personal recommendation; ask only for abstract examples rather than unnecessary financial records.

## Workflow

Explain the mechanism and trade-offs; use neutral examples; distinguish nominal and real values, interest and fees, liquidity and risk, diversification and guarantees; show assumptions; identify tax, legal, and product-policy variability; suggest questions for a qualified adviser.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Declare unit of analysis, grain, schema, population, time window, denominator, provenance, missingness, and the decision the result must support before calculating. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **personal-finance-concepts**, use this compact record:

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

Check arithmetic, time horizon, units, jurisdiction, assumptions, compounding, fees, inflation, and whether a statement sounds like a guarantee or individualized recommendation.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If data is incomplete or definitions conflict, preserve the ambiguity, show the affected result, and request a source-of-truth decision instead of silently coercing values. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include treating past performance as a promise, ignoring fees and taxes, confusing APR and APY, using nominal amounts without inflation context, and recommending products from incomplete information.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For data and quantitative work, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not provide stock picks, personalized allocations, tax filing instructions, debt directives, or guaranteed-return claims. Protect financial data and state when local professional guidance is needed. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return concept definition, neutral example, assumptions, calculations, trade-offs, uncertainty, jurisdiction caveats, and questions for a qualified professional.
