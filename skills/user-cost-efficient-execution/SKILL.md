---
name: user-cost-efficient-execution
description: Reduce time, token use, compute, API calls, and recurring operating cost while preserving correctness, security, and required quality. Use when choosing tools, models, data sources, workflows, hosting, automation, or implementation approaches.
---

# Cost-Efficient Execution

## Quick start

Use this skill when the request matches **Reduce time, token use, compute, API calls, and recurring operating cost while preserving correctness, security, and required quality. Use when choosing tools, models, data sources, workflows, hosting, automation, or implementation approaches.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **cost-efficient-execution**, use this compact record:

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

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If information is missing or conflicting, state the uncertainty, ask only blocking questions, and avoid fabricating evidence, permissions, results, or completed actions. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For general professional workflow, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

verify assumptions, important claims, edge cases, usability, safety, reproducibility, and whether the handoff contains enough information for another person or agent to continue. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.
