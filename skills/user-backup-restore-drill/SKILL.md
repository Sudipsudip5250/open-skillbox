---
name: user-backup-restore-drill
description: Plan and verify authorized backup and restore drills with recovery objectives, dependency order, integrity checks, access control, and evidence. Use for owned systems and approved test environments.
---

# Backup and Restore Drill

## Quick start

Use this skill when the request matches **Plan and verify authorized backup and restore drills with recovery objectives, dependency order, integrity checks, access control, and evidence. Use for owned systems and approved test environments.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Confirm authority, target environment, data classification, RPO/RTO, backup source, restore destination, dependency order, communications, and stop conditions before touching data.

## Workflow

Select a representative restore; verify backup age, integrity, encryption, access, and chain; restore into an isolated environment; replay dependencies in order; validate data and application behavior; measure RTO/RPO; record failures; clean up test artifacts; assign remediation.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | State the user or service outcome, decision owner, evidence, time horizon, capacity, dependencies, risk, and explicit non-goals before recommending a plan. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **backup-restore-drill**, use this compact record:

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

Compare restored data with checksums or reconciliations, verify permissions and secrets rotation, test monitoring and rollback, document missing data or configuration, and confirm no production impact.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If evidence or ownership is missing, mark the item as a hypothesis, decision needed, or escalation rather than presenting a speculative commitment as a plan. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include testing only that a backup file exists, restoring over production, ignoring application dependencies, leaking restored PII, and declaring success without user-level validation.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For product and operations, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Use only owned or explicitly authorized systems, protect sensitive data, and never overwrite production during a drill without separately approved change control. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return authorization and scope, backup/version, restore plan, evidence, RPO/RTO results, integrity and permission checks, failures, cleanup, remediation, and next drill date.
