---
name: user-experiment-ab-test-analysis
description: Design and analyze product A/B experiments with assignment, metrics, guardrails, uncertainty, and interpretation. Use for product experimentation, not medical trials.
---

# Experiment and A/B Test Analysis

## Purpose and scope

State the decision, eligible population, unit of randomization, variants, exposure window, primary metric, guardrails, minimum detectable effect, and stopping policy before looking at outcomes.

## Workflow

Check assignment and exposure; define numerator, denominator, and metric window; inspect balance and contamination; estimate lift with uncertainty; check guardrails, segments, missingness, and novelty effects; distinguish exploratory from confirmatory results; recommend ship, iterate, or continue.

## Verification and quality checks

Verify randomization, sample ratio, exposure integrity, pre-period comparability, multiple-testing treatment, interval assumptions, practical significance, and sensitivity to exclusions.

## Common errors

Common errors include peeking without a plan, changing the primary metric after results, ignoring interference, over-reading subgroups, using ratio metrics without denominator checks, and declaring success from statistical significance alone.

## Rules, safety, and non-goals

Do not frame product experiments as medical evidence or use sensitive populations without appropriate governance. Protect user data and avoid manipulative experimentation. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return hypothesis, design, metric contract, assignment checks, estimates with uncertainty, guardrails, limitations, decision, and follow-up test.
