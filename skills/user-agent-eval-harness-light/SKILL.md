---
name: user-agent-eval-harness-light
description: Design small repeatable evaluations for agents, skills, prompts, tool use, safety, regression, and handoff quality. Use for lightweight repository or project evals.
---

# Lightweight Agent Evaluation Harness

## Quick start

Use this skill when the request matches **Design small repeatable evaluations for agents, skills, prompts, tool use, safety, regression, and handoff quality. Use for lightweight repository or project evals.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Define task set, expected behavior, allowed tools, evaluator rubric, safety cases, failure severity, model or prompt version, and what counts as a meaningful regression.

## Workflow

Create representative and adversarial-but-safe prompts; define expected outputs and forbidden behavior; run fixed cases with captured inputs, outputs, tool traces, latency, and cost where available; score correctness, completeness, uncertainty, safety, and format; compare against a baseline; file actionable regressions.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the agent host, available tools, instruction precedence, context budget, data boundary, approval gates, expected output, and the smallest skill chain that can complete the task. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **agent-eval-harness-light**, use this compact record:

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

Repeat runs where variability matters, inspect false positives and false negatives, protect test data, separate judge agreement from model quality, and verify that an improved score did not weaken safety or factual honesty.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If a host cannot load the canonical format or a tool is unavailable, preserve the source skill and document a reversible adapter or manual fallback rather than claiming compatibility. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include tiny or unrepresentative test sets, judging style instead of behavior, leaking answers into prompts, changing the rubric mid-run, and treating one pass as proof of reliability.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For agent workflow and governance, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not use evaluation to bypass safeguards, probe unauthorized systems, or expose secrets. Red-team cases must remain safe, authorized, and focused on defensive behavior. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return eval purpose, cases, rubric, baseline, results, failures, safety findings, reproducibility metadata, and release recommendation.
