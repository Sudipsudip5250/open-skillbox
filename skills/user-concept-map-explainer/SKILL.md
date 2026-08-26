---
name: user-concept-map-explainer
description: Explain a topic as connected concepts, relationships, examples, misconceptions, and progressive layers. Use for education, onboarding, documentation, and cross-domain learning.
---

# Concept Map Explainer

## Quick start

Use this skill when the request matches **Explain a topic as connected concepts, relationships, examples, misconceptions, and progressive layers. Use for education, onboarding, documentation, and cross-domain learning.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Define learner level, goal, prerequisite knowledge, scope, terminology, and whether the map is causal, hierarchical, procedural, comparative, or evidential.

## Workflow

Identify core nodes; group prerequisites and outcomes; label relationships with precise verbs; add examples and counterexamples; expose common misconceptions; sequence from simple to complex; render or describe the map; add retrieval questions and links to deeper skills.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Identify learner or reader level, objective, prerequisite knowledge, source quality, accessibility needs, and whether the task is explanation, practice, assessment, or decision support. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **concept-map-explainer**, use this compact record:

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

Check that every edge has a meaningful relation, no circular explanation hides a missing prerequisite, examples fit the concept, terminology is consistent, and the map supports the stated learning goal.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If the learner is stuck, diagnose the misconception and add a smaller hint or prerequisite explanation; do not shame the learner or imply professional certainty in regulated topics. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include unlabeled arrows, confusing correlation and causation, overcrowding, defining a concept with itself, and presenting a memorization list as a concept map.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For education and literacy, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not oversimplify safety-critical, medical, legal, or scientific claims. Mark uncertainty and route regulated or advanced questions to qualified sources. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return learner profile, map nodes and labeled edges, examples, misconceptions, explanation sequence, practice prompts, sources, and extension skills.
