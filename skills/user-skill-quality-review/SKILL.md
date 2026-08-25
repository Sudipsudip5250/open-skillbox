---
name: user-skill-quality-review
description: Grade and improve modular skills for trigger quality, boundary, workflow, verification, safety, composition, and maintainability. Use for repository skill reviews and pull requests.
---

# Skill Quality Review

## Purpose and scope

Review the skill as an agent-facing procedure: determine what task it triggers, what it excludes, and whether another skill already owns part of the work.

## Workflow

Check metadata, naming, scope, progressive disclosure, workflow actionability, assumptions, verification, failure modes, safety, source discipline, handoff, and composition. Assign an A–F grade with evidence; identify the smallest fixes that improve reliability; re-run validation; distinguish style preference from functional defect.

## Verification and quality checks

Use a representative prompt, compare routing against neighboring skills, inspect all relative links, check line count and headings, and verify that suggested fixes do not change intended behavior or erase safety boundaries.

## Common errors

Common errors include grading prose instead of behavior, rewarding length, overlooking unsafe ambiguity, demanding duplicated boilerplate, or recommending a rename that breaks users without a migration plan.

## Rules, safety, and non-goals

Do not expose private content, invent failures, or approve a skill that facilitates unauthorized access, bypass, deception, or harmful instructions. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return grade, evidence table, blockers, prioritized fixes, overlap decision, validation result, and maintainer recommendation.
