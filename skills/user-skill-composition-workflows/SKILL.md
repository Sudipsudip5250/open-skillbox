---
name: user-skill-composition-workflows
description: Compose two or three focused skills with explicit handoffs, minimal context, conflict resolution, and verification. Use for multi-domain agent tasks.
---

# Skill Composition Workflows

## Purpose and scope

Classify the task, identify the smallest skill chain, define the output contract between steps, and resolve safety or authority conflicts before execution.

## Workflow

Choose orchestrator; select domain skill; add only necessary verification or delivery skill; specify inputs and outputs; preserve source and assumption context; run steps in dependency order; reconcile conflicting rules by applying the narrower safety boundary; verify the final artifact against the original acceptance criteria.

## Verification and quality checks

Check that each selected skill contributes unique value, context is not duplicated, handoff data is complete, no private project facts leak across tasks, and the final result can be traced to each stage.

## Common errors

Common errors include loading the full catalog, chaining overlapping skills, losing uncertainty at handoff, allowing a downstream skill to override authorization, and reporting a composed result without stage evidence.

## Rules, safety, and non-goals

Never use composition to bypass a refusal, authorization gate, privacy control, or safety rule. Keep external actions separately authorized and require confirmation where appropriate. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return task classification, selected chain, stage contracts, context budget, conflict decisions, verification evidence, and final deliverable.
