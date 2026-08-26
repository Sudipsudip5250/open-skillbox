---
name: user-research-fact-checking
description: Conduct focused, source-based research, verify claims, compare evidence, and produce transparent citations. Use for factual questions, market or domain investigation, comparisons, current information, and decisions that depend on external evidence.
---

# Research and Fact-Checking

## Quick start

Use this skill when the request matches **Conduct focused, source-based research, verify claims, compare evidence, and produce transparent citations. Use for factual questions, market or domain investigation, comparisons, current information, and decisions that depend on external evidence.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Research workflow

1. Define the precise question, date boundary, geography, audience, and decision the research must support.
2. Break the question into verifiable subclaims and identify what would count as strong evidence.
3. Search authoritative primary sources first: official documentation, filings, datasets, standards, academic papers, and direct statements. Use reputable secondary sources for context and discovery.
4. Open and inspect the source itself; do not rely on search snippets. Record publication date, update date, scope, methodology, and limitations.
5. Cross-check material claims with independent sources, especially claims involving price, performance, safety, law, finance, or rapidly changing products.
6. Separate observed facts, source-reported claims, calculations, interpretations, and recommendations.
7. Cite claims close to where they appear and include a references list. Do not cite a source for a claim it does not support.
8. State uncertainty, disagreement, missing data, and the date the research was current.

## Source hierarchy

Prefer primary and official sources, then high-quality independent research, then specialist reporting, and finally community material for leads or practical context. Match source strength to claim importance. Use multiple sources when a single source may be biased, incomplete, or stale.

## Routing boundary

Use this skill for general factual investigation, comparisons, current information, and source verification. Defer to scientific research for literature reviews, experimental evidence, reproducibility, or scientific synthesis; to mathematics skills for derivations; to domain science skills for chapter-level problem solving; to data analysis for calculations and datasets; and to documentation for publication formatting.

## Evidence table

| Claim | Evidence | Source/date | Confidence | Limitation |
|---|---|---|---|---|
| The precise statement being evaluated | What the source actually shows | URL or citation and date | High/medium/low | Scope, freshness, or methodological caveat |

## When not to use this skill

Do not use it as a substitute for a specialized scientific, legal, medical, financial, or security workflow when the request depends on domain-specific standards. Do not present search discovery, a single weak source, or a plausible explanation as verified fact.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **research-fact-checking**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If information is missing or conflicting, state the uncertainty, ask only blocking questions, and avoid fabricating evidence, permissions, results, or completed actions. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For general professional workflow, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

verify assumptions, important claims, edge cases, usability, safety, reproducibility, and whether the handoff contains enough information for another person or agent to continue. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Handoff

Report the question and subclaims, search scope, source hierarchy, evidence table, verified findings, calculations, interpretations, uncertainty, limitations, date current, and references. Do not fill evidence gaps with plausible wording; state what would resolve them.
