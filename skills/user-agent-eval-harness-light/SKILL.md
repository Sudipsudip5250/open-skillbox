---
name: user-agent-eval-harness-light
description: Design small repeatable evaluations for agents, skills, prompts, tool use, safety, regression, and handoff quality. Use for lightweight repository or project evals.
---

# Lightweight Agent Evaluation Harness

## Purpose and scope

Define task set, expected behavior, allowed tools, evaluator rubric, safety cases, failure severity, model or prompt version, and what counts as a meaningful regression.

## Workflow

Create representative and adversarial-but-safe prompts; define expected outputs and forbidden behavior; run fixed cases with captured inputs, outputs, tool traces, latency, and cost where available; score correctness, completeness, uncertainty, safety, and format; compare against a baseline; file actionable regressions.

## Verification and quality checks

Repeat runs where variability matters, inspect false positives and false negatives, protect test data, separate judge agreement from model quality, and verify that an improved score did not weaken safety or factual honesty.

## Common errors

Common errors include tiny or unrepresentative test sets, judging style instead of behavior, leaking answers into prompts, changing the rubric mid-run, and treating one pass as proof of reliability.

## Rules, safety, and non-goals

Do not use evaluation to bypass safeguards, probe unauthorized systems, or expose secrets. Red-team cases must remain safe, authorized, and focused on defensive behavior. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return eval purpose, cases, rubric, baseline, results, failures, safety findings, reproducibility metadata, and release recommendation.
