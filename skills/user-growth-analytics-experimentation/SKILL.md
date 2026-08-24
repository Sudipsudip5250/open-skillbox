---
name: user-growth-analytics-experimentation
description: Measure and improve acquisition, activation, engagement, conversion, retention, monetization, and revenue experiments for websites, apps, and content channels. Use for funnels, attribution, cohorts, A/B tests, paywall experiments, pricing tests, ad-yield analysis, churn, or growth reporting.
---

# Growth Analytics and Experimentation

## Workflow

1. Define the business question, user segment, funnel, primary metric, guardrail metrics, time window, attribution window, sample assumptions, and decision threshold.
2. Instrument events with stable names, clear properties, consent-aware collection, identity rules, versioning, and a documented source of truth. Test event delivery, deduplication, time zones, bot filtering, and cross-device behavior.
3. Build a baseline for acquisition, activation, engagement, conversion, retention, churn, average revenue per user, lifetime value, acquisition cost, ad yield, refunds, support burden, and user-experience impact.
4. Choose an experiment or observational method appropriate to the question. Define eligibility, randomization or comparison group, exposure, duration, stopping rule, novelty effects, seasonality, interference, and privacy limits.
5. Analyze results with confidence and practical significance, segment checks, missing-data review, instrumentation validation, and guardrail outcomes. Do not overstate results from small or biased samples.
6. Decide whether to ship, iterate, stop, or roll back. Record the hypothesis, change, result, uncertainty, affected segments, revenue and retention trade-off, and follow-up measurement.

## Rules

- Do not use dark patterns, hidden consent, forced tracking, misleading attribution, fake urgency, or experiments that materially harm users without approved safeguards.
- Do not identify individuals unnecessarily or combine datasets beyond the approved purpose. Respect deletion, consent, retention, and access controls.
- Do not call correlation causal without a credible design. Do not optimize a local conversion metric while degrading trust, retention, accessibility, support, or net revenue.
- Do not fabricate traffic, conversions, revenue, statistical significance, or experiment results.
- Pair this skill with privacy, security, observability, data-analysis, monetization-strategy, and platform-policy skills as appropriate.

## Handoff

Report question and hypothesis, event schema, baseline, method, sample and time window, primary and guardrail metrics, results and uncertainty, segment effects, revenue and user trade-offs, decision, and follow-up plan.
