---
name: user-project-delivery
description: Turn ideas into scoped project plans, milestones, implementation checkpoints, releases, and handoffs. Use for websites, applications, repositories, product features, migrations, deployments, and any work that must move from concept to usable outcome.
---

# Project Delivery

## Quick start

Use this skill when the request matches **Turn ideas into scoped project plans, milestones, implementation checkpoints, releases, and handoffs. Use for websites, applications, repositories, product features, migrations, deployments, and any work that must move from concept to usable outcome.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Delivery workflow

1. Clarify the user, problem, outcome, constraints, dependencies, and definition of done.
2. Inspect the current project and identify what already exists before proposing new infrastructure or code.
3. Split the work into vertical slices that each produce a testable outcome. Mark must-have, should-have, and optional scope.
4. Identify risks, assumptions, external dependencies, security concerns, and rollback points.
5. Implement in checkpoints, keeping each change reviewable and the project runnable.
6. Validate functionality, usability, accessibility, performance, security, and deployment behavior appropriate to the project.
7. Prepare release notes, configuration requirements, migration steps, and a concise handoff.

## Scope control

When a request is broad, deliver a useful first slice instead of silently expanding scope. Surface trade-offs between speed, quality, cost, and extensibility. Do not introduce a database, service, framework, or recurring expense unless the requirement justifies it.

## Definition-of-done template

A feature is done when its intended behavior works in the target environment, failure paths are handled, relevant tests or smoke checks pass, documentation and configuration are updated, no secrets are exposed, and the user can run or deploy it using the supplied instructions.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **project-delivery**, use this compact record:

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

## Handoff

State what is complete, where it lives, how to run or deploy it, how it was verified, what remains, and which assumptions the next contributor should know.


## Quality and safety rules

Do not silently expand scope, skip investigation or verification, expose secrets, or mark work complete without evidence. Escalate missing authorization, blocked dependencies, unresolved risks, and domain-specific professional requirements before irreversible actions.

## When not to use this skill

Do not use it as a substitute for a specialized implementation, research, security, finance, science, education, or deployment workflow. Use this skill to coordinate those workflows, not to replace their methods.
