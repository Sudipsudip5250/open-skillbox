---
name: user-project-delivery
description: Turn ideas into scoped project plans, milestones, implementation checkpoints, releases, and handoffs. Use for websites, applications, repositories, product features, migrations, deployments, and any work that must move from concept to usable outcome.
---

# Project Delivery

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

## Handoff

State what is complete, where it lives, how to run or deploy it, how it was verified, what remains, and which assumptions the next contributor should know.
