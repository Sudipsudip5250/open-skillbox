---
name: user-legal-document-literacy
description: Read, organize, compare, and summarize legal or policy documents for plain-language understanding while preserving clauses, definitions, obligations, dates, exceptions, and uncertainty. Use for informational document literacy, not legal advice.
---

# Legal-Document Literacy

## Quick start

Use this skill when the request matches **Read, organize, compare, and summarize legal or policy documents for plain-language understanding while preserving clauses, definitions, obligations, dates, exceptions, and uncertainty. Use for informational document literacy, not legal advice.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Help a reader understand what a document says, where obligations or risks appear, and which questions require a qualified lawyer or the relevant official authority. Read, organize, compare, and summarize legal or policy documents for plain-language understanding while preserving clauses, definitions, obligations, dates, exceptions, and uncertainty. Use for informational document literacy, not legal advice.

## Classification and inputs

Identify the request, audience, source materials, constraints, assumptions, permissions, version or jurisdiction, and required precision before selecting a method. Separate observed facts, user-provided inputs, calculations, model outputs, and interpretations.

## Workflow

1. Identify document type, jurisdiction, governing law, parties, version, effective date, intended audience, and the decision the reader is considering.
2. Extract definitions, scope, duties, permissions, prohibitions, representations, warranties, payment or termination terms, deadlines, dispute provisions, privacy clauses, and referenced exhibits.
3. Build a clause map linking plain-language summaries to exact section or page locations; preserve modal strength such as must, may, reasonable efforts, or subject to.
4. Compare versions or related documents clause by clause, marking additions, deletions, conflicts, undefined terms, and missing schedules.
5. Separate text-supported observations from interpretation; list ambiguities and questions for qualified legal review.
6. Provide a neutral summary and decision checklist without recommending that the user sign, waive, file, or rely on a legal position.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **legal-document-literacy**, use this compact record:

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

Check every material summary against the source text, preserve jurisdiction and version, verify dates and cross-references, distinguish obligation from possibility, note missing pages or exhibits, and request professional review for consequential decisions.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If information is missing or conflicting, state the uncertainty, ask only blocking questions, and avoid fabricating evidence, permissions, results, or completed actions. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include treating a summary as the contract, ignoring definitions or exhibits, assuming one jurisdiction’s rule applies elsewhere, overlooking renewal or termination dates, and converting ambiguity into certainty.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For general professional workflow, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

This skill is informational and is not legal advice. Do not impersonate counsel, draft deceptive evidence, advise evasion, or make a personalized legal conclusion. Protect confidential documents and redact personal data when sharing excerpts. Do not invent sources, data, results, approvals, or completed actions. Use the smallest relevant skill set and hand off to specialized research, security, data, accessibility, or implementation skills when the task crosses boundaries.

## Handoff

Return document identity and version, clause map, plain-language summary, obligations and deadlines, ambiguities and missing material, comparison findings, source locations, questions for counsel, and confidentiality caveats.
