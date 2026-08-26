---
name: user-data-quality-validation
description: Design and execute data-quality checks for schemas, nulls, duplicates, drift, reconciliation, contracts, and quarantine decisions. Use for analytics, pipelines, and ML inputs.
---

# Data Quality Validation

## Quick start

Use this skill when the request matches **Design and execute data-quality checks for schemas, nulls, duplicates, drift, reconciliation, contracts, and quarantine decisions. Use for analytics, pipelines, and ML inputs.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Define what makes the dataset fit for its intended use, including freshness, completeness, validity, uniqueness, consistency, lineage, and acceptable thresholds.

## Workflow

Profile the raw and transformed layers; define schema and contract rules; test nulls, ranges, formats, uniqueness, referential integrity, freshness, drift, and reconciliation; classify failures; quarantine or block unsafe outputs; record owners and remediation.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Declare unit of analysis, grain, schema, population, time window, denominator, provenance, missingness, and the decision the result must support before calculating. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **data-quality-validation**, use this compact record:

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

Compare checks with baselines, test false positives, verify counts before and after filtering, inspect representative failures, and rerun after correction.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If data is incomplete or definitions conflict, preserve the ambiguity, show the affected result, and request a source-of-truth decision instead of silently coercing values. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include checking only row counts, hiding failures by coercing values, changing thresholds without review, confusing missingness with zero, and failing to trace a broken field to its source.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For data and quantitative work, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not silently discard records, fabricate quality scores, or expose sensitive samples. Preserve raw data and document retention, access, and remediation boundaries. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return the quality contract, checks and thresholds, failure sample with redaction, decision, owner, remediation, rerun evidence, and residual risk.
