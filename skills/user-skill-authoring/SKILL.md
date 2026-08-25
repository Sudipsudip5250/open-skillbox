---
name: user-skill-authoring
description: Create or revise repository-compatible modular skills with narrow triggers, progressive disclosure, safety boundaries, verification, and handoffs. Use when writing a new SKILL.md for this catalog.
---

# Skill Authoring

## Purpose and scope

Start by checking the existing index, taxonomy, overlap, audience, trigger, and whether an existing skill should be extended instead.

## Workflow

Define one task boundary; choose a `user-<kebab-case>` canonical directory for backward-compatible repository discovery; write frontmatter; add purpose, workflow, verification, common failures, rules/non-goals, composition, and handoff; keep content concise; add only useful references or scripts; update index and sources; run validators.

## Verification and quality checks

Test metadata and structure, inspect trigger distinctness, verify links and public paths, run representative scenarios, check safety boundaries, and review for secrets, copied text, unsupported claims, and overlap.

## Common errors

Common errors include vague triggers, giant umbrella skills, duplicated procedures, hidden assumptions, unbounded tool use, stale sources, and a handoff that does not describe the deliverable.

## Rules, safety, and non-goals

Do not put private project knowledge, credentials, proprietary prompts, copyrighted textbook dumps, or unsafe bypass instructions in a public skill. Preserve existing skills unless a documented surgical change is approved. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return skill directory, trigger rationale, overlap analysis, workflow, sources, validation output, scenario test, and follow-up improvements.
