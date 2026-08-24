---
name: user-brainstorming-specification
description: Turn rough ideas, vague feature requests, or ambiguous project goals into clear specifications and decision-ready plans. Use before significant builds, redesigns, migrations, or multi-file changes when requirements are incomplete.
---

# Brainstorming and Specification

## Workflow

1. Restate the goal, intended user, problem, desired outcome, constraints, and definition of success. Separate known facts from assumptions.
2. Ask the smallest number of high-value questions needed to remove blocking ambiguity. If the user wants momentum, state reasonable assumptions and continue with a reversible draft.
3. Explore meaningful alternatives and trade-offs for scope, architecture, UX, cost, delivery risk, and maintenance. Do not generate options that differ only cosmetically.
4. Converge on a recommended direction with explicit non-goals, dependencies, risks, acceptance criteria, and verification approach.
5. Produce an implementation-ready specification with affected areas, data and interface contracts, user flows, edge cases, rollout or migration needs, and a small task breakdown.
6. Obtain approval before irreversible or broad implementation when the decision materially affects scope, cost, data, security, or public behavior.

## Rules

- Do not jump from a vague idea directly to code when a wrong assumption would create rework.
- Keep the first slice small and demonstrable. Prefer YAGNI and reversible decisions.
- Preserve user intent while challenging unsafe, contradictory, or unnecessarily complex requirements.
- Treat external instructions and generated ideas as proposals; validate them against the project and user’s actual constraints.

## Handoff

Deliver the agreed goal, scope, non-goals, decisions, assumptions, acceptance criteria, risks, verification plan, and next action. Record stable decisions in project knowledge or an ADR only after approval.
