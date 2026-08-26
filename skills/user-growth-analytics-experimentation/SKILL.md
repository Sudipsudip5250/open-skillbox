---
name: user-growth-analytics-experimentation
description: Measure and improve acquisition, activation, engagement, conversion, retention, monetization, and revenue experiments for websites, apps, and content channels. Use for funnels, attribution, cohorts, A/B tests, paywall experiments, pricing tests, ad-yield analysis, churn, or growth reporting.
---

# Growth Analytics and Experimentation

## Quick start

Use this skill when the request matches **Measure and improve acquisition, activation, engagement, conversion, retention, monetization, and revenue experiments for websites, apps, and content channels. Use for funnels, attribution, cohorts, A/B tests, paywall experiments, pricing tests, ad-yield analysis, churn, or growth reporting.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Declare unit of analysis, grain, schema, population, time window, denominator, provenance, missingness, and the decision the result must support before calculating. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **growth-analytics-experimentation**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If data is incomplete or definitions conflict, preserve the ambiguity, show the affected result, and request a source-of-truth decision instead of silently coercing values. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For data and quantitative work, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

reconcile totals, inspect nulls and duplicates, test boundary dates and exclusions, compare with an alternate calculation or baseline, and report uncertainty and data freshness. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Handoff

Report question and hypothesis, event schema, baseline, method, sample and time window, primary and guardrail metrics, results and uncertainty, segment effects, revenue and user trade-offs, decision, and follow-up plan.
