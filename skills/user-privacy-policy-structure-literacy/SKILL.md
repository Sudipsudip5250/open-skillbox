---
name: user-privacy-policy-structure-literacy
description: Explain the structure and meaning of privacy-policy sections, data flows, rights, retention, sharing, and choices. Use for neutral policy literacy, not legal evasion or compliance certification.
---

# Privacy Policy Structure Literacy

## Quick start

Use this skill when the request matches **Explain the structure and meaning of privacy-policy sections, data flows, rights, retention, sharing, and choices. Use for neutral policy literacy, not legal evasion or compliance certification.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Identify policy version, jurisdiction, audience, service context, and whether the goal is reading comprehension, comparison, or a question list for counsel or privacy staff.

## Workflow

Map sections such as collection, purposes, legal or policy basis, sharing, retention, security, international transfer, rights, cookies, children, changes, and contact; trace each statement to data flow; flag ambiguity, missing scope, inconsistent definitions, and user-action consequences.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Confirm ownership or written authorization, target scope, environment, evidence handling, rate limits, and stop conditions before active access or testing. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **privacy-policy-structure-literacy**, use this compact record:

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

Compare policy text with product behavior or official settings when authorized, check dates and linked notices, preserve modal language, and mark claims that require legal or privacy review.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If authorization, scope, or safe evidence handling is missing, pause and provide a planning-only alternative rather than probing, bypassing, or guessing. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include treating a policy as proof of compliance, ignoring linked notices, confusing service providers with sale or sharing, overlooking retention, and turning ambiguity into certainty.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For security and trust, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not draft language to evade law, conceal collection, or mislead users. This is informational literacy, not legal advice or certification; protect confidential policy drafts and personal data. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return policy identity, section map, data-flow observations, user choices and rights, ambiguity list, comparison evidence, questions for review, and version/date.
