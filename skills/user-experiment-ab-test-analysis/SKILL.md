---
name: user-experiment-ab-test-analysis
description: Design and analyze product A/B experiments with assignment, metrics, guardrails, uncertainty, and interpretation. Use for product experimentation, not medical trials.
---

# Experiment and A/B Test Analysis

## Quick start

Use this skill when the request matches **Design and analyze product A/B experiments with assignment, metrics, guardrails, uncertainty, and interpretation. Use for product experimentation, not medical trials.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

State the decision, eligible population, unit of randomization, variants, exposure window, primary metric, guardrails, minimum detectable effect, and stopping policy before looking at outcomes.

## Workflow

Check assignment and exposure; define numerator, denominator, and metric window; inspect balance and contamination; estimate lift with uncertainty; check guardrails, segments, missingness, and novelty effects; distinguish exploratory from confirmatory results; recommend ship, iterate, or continue.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **experiment-ab-test-analysis**, use this compact record:

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

## Verification and quality checks

Verify randomization, sample ratio, exposure integrity, pre-period comparability, multiple-testing treatment, interval assumptions, practical significance, and sensitivity to exclusions.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If the failure is not reproducible, capture environment and logs, reduce the case, state uncertainty, and avoid speculative rewrites or destructive recovery steps. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include peeking without a plan, changing the primary metric after results, ignoring interference, over-reading subgroups, using ratio metrics without denominator checks, and declaring success from statistical significance alone.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For software and systems, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not frame product experiments as medical evidence or use sensitive populations without appropriate governance. Protect user data and avoid manipulative experimentation. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return hypothesis, design, metric contract, assignment checks, estimates with uncertainty, guardrails, limitations, decision, and follow-up test.
