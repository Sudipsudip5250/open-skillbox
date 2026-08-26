---
name: user-scientific-research
description: Conduct structured scientific and technical research, literature reviews, evidence synthesis, reproducible analysis, and research reporting. Use for papers, systematic or scoping reviews, experimental design, scientific databases, technical claims, or research-backed conclusions.
---

# Scientific Research

## Quick start

Use this skill when the request matches **Conduct structured scientific and technical research, literature reviews, evidence synthesis, reproducible analysis, and research reporting. Use for papers, systematic or scoping reviews, experimental design, scientific databases, technical claims, or research-backed conclusions.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Research workflow

1. Define the question, population or system, intervention or comparison, outcomes, date and language limits, inclusion and exclusion criteria, and intended use of the evidence.
2. Choose the appropriate mode: focused evidence lookup, scoping review, systematic review, experimental design, reproducibility audit, or technical synthesis. Load a chapter-level science skill when the subject requires domain methods.
3. Search authoritative databases, primary studies, standards, official datasets, and high-quality reviews. Record query, source, date, version, identifiers, and access limits.
4. Screen evidence for relevance, methods, sample or dataset quality, bias, conflicts, reproducibility, statistical validity, and whether conclusions match the evidence.
5. Extract claims into a structured evidence table with source, method, result, limitation, confidence, and applicability. Separate primary evidence, review evidence, expert opinion, and speculation.
6. Synthesize cautiously. Explain agreement, disagreement, uncertainty, missing data, effect size or practical significance, and what would change the conclusion.
7. Make the analysis reproducible: preserve source references, code or calculation assumptions, data provenance, transformations, and validation checks.
8. Write a report with a direct answer, methods, evidence, limitations, conclusion, and references. Do not turn correlation into causation or preliminary findings into established fact.

## Routing and boundaries

Use this skill for scientific evidence and research method. Use general research and fact-checking for ordinary factual investigation, mathematics skills for mathematical derivations, chapter-level physics/chemistry/biology/earth skills for domain problem solving, experimental-design skills for study or lab planning, scientific-visualization skills for plots, citation-management skills for bibliography workflows, and tutoring skills for teaching.

## Rules

- Do not fabricate papers, DOIs, datasets, statistics, quotes, citations, or experimental results.
- Prefer primary sources and version-matched official documentation for technical claims. Verify important facts at the source rather than relying on search snippets.
- Treat unpublished, preprint, generated, and model-produced material as lower-confidence until independently verified.
- Do not convert general research into medical, legal, financial, or other regulated personal advice. State when qualified professional review is required.
- Do not provide unsafe experimental instructions. Identify hazards, controls, permissions, and appropriate supervision before discussing laboratory or hardware procedures.

## When not to use this skill

Do not use it for a simple stable explanation that needs no evidence synthesis, for routine code implementation, or for personal regulated decisions without the appropriate safeguards. Do not call a literature search systematic unless the search and screening process supports that label.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **scientific-research**, use this compact record:

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

Report research mode, search scope, sources, screening criteria, evidence table, synthesis, limitations, reproducibility artifacts, uncertainty, and references. State which claims are directly supported and which are interpretations.
