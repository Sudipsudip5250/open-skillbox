---
name: user-data-quality-validation
description: Design and execute data-quality checks for schemas, nulls, duplicates, drift, reconciliation, contracts, and quarantine decisions. Use for analytics, pipelines, and ML inputs.
---

# Data Quality Validation

## Purpose and scope

Define what makes the dataset fit for its intended use, including freshness, completeness, validity, uniqueness, consistency, lineage, and acceptable thresholds.

## Workflow

Profile the raw and transformed layers; define schema and contract rules; test nulls, ranges, formats, uniqueness, referential integrity, freshness, drift, and reconciliation; classify failures; quarantine or block unsafe outputs; record owners and remediation.

## Verification and quality checks

Compare checks with baselines, test false positives, verify counts before and after filtering, inspect representative failures, and rerun after correction.

## Common errors

Common errors include checking only row counts, hiding failures by coercing values, changing thresholds without review, confusing missingness with zero, and failing to trace a broken field to its source.

## Rules, safety, and non-goals

Do not silently discard records, fabricate quality scores, or expose sensitive samples. Preserve raw data and document retention, access, and remediation boundaries. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return the quality contract, checks and thresholds, failure sample with redaction, decision, owner, remediation, rerun evidence, and residual risk.
