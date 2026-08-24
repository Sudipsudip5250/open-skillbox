---
name: user-cost-efficient-execution
description: Reduce time, token use, compute, API calls, and recurring operating cost while preserving correctness, security, and required quality. Use when choosing tools, models, data sources, workflows, hosting, automation, or implementation approaches.
---

# Cost-Efficient Execution

## Decision rule

Optimize total cost of ownership, not the cheapest first action. Compare setup cost, run cost, maintenance cost, failure cost, lock-in, latency, and quality. Choose the least expensive option that satisfies the acceptance criteria and risk level.

## Workflow

1. Define the required quality, freshness, scale, latency, privacy, and reliability.
2. Estimate the cost drivers: context size, number of calls, data volume, compute, storage, external services, human review, and future maintenance.
3. Prefer deterministic local operations for deterministic work; use AI only where judgment or generation adds value.
4. Reuse existing files, project helpers, cached results, schemas, templates, and validated scripts.
5. Batch independent work when safe, but do not parallelize tiny tasks or operations with shared mutable state.
6. Use progressive disclosure: retrieve summaries or targeted ranges first, then expand only where uncertainty remains.
7. Add stopping conditions based on the acceptance criteria. Do not continue research after the decision is adequately supported.
8. Measure actual usage and note the cheaper alternative for future runs.

## Practical rules

| Situation | Prefer | Avoid |
|---|---|---|
| File inspection | Targeted search and ranges | Reading every large file repeatedly |
| Simple transformation | Local script or standard utility | Calling an external model |
| Repeated classification | Batch structured requests | One request per item without need |
| Large document | Extract headings and relevant sections | Sending the entire document repeatedly |
| Web research | A few authoritative sources | Broad unfocused browsing |
| Image or media work | Existing assets and deterministic edits | Regenerating unchanged assets |
| Deployment | Existing project scaffold and managed service | Rebuilding infrastructure unnecessarily |
| Automation | Idempotent scheduled jobs | Frequent polling without a trigger |

## Quality guardrails

Never reduce verification, source quality, security, backups, or required accessibility merely to save resources. When a lower-cost option has a material limitation, state it and offer the trade-off. For expensive or irreversible actions, obtain confirmation before execution when required.

## Reusable cost record

Record the chosen approach, alternatives considered, primary cost drivers, quality trade-off, and a future optimization. Keep the record short enough to reuse in later projects.
