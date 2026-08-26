---
name: user-health-information-literacy
description: Evaluate and explain health information, study quality, uncertainty, risk communication, and source credibility without diagnosing or prescribing. Use for educational health-literacy tasks.
---

# Health Information Literacy

## Quick start

Use this skill when the request matches **Evaluate and explain health information, study quality, uncertainty, risk communication, and source credibility without diagnosing or prescribing. Use for educational health-literacy tasks.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Clarify the question, audience, date, location, urgency, and whether the user needs general education or professional care; identify red flags that require immediate local help without diagnosing.

## Workflow

Find primary or authoritative sources; inspect study design, population, intervention or exposure, outcome, comparator, effect size, uncertainty, harms, conflicts, and applicability; translate absolute and relative risk; distinguish established, plausible, and unknown claims; suggest questions for a licensed clinician.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Identify learner or reader level, objective, prerequisite knowledge, source quality, accessibility needs, and whether the task is explanation, practice, assessment, or decision support. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **health-information-literacy**, use this compact record:

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

Check source date and authority, denominators, confidence intervals or limitations, contradictory evidence, marketing language, and whether the explanation overstates causation or individual applicability.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If the learner is stuck, diagnose the misconception and add a smaller hint or prerequisite explanation; do not shame the learner or imply professional certainty in regulated topics. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include treating correlation as cause, confusing relative and absolute risk, using animal or early evidence as treatment advice, ignoring harms, and presenting a population result as a personal diagnosis.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For education and literacy, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

This is educational information, not diagnosis, treatment, emergency triage, or personalized medical advice. Do not recommend changing medication or delaying care; protect health data and encourage qualified professional help. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return question scope, source table, evidence quality, plain-language explanation, uncertainty and harms, applicability limits, red flags, and clinician questions.
