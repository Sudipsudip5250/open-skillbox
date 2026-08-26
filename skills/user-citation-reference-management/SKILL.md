---
name: user-citation-reference-management
description: Collect, normalize, verify, deduplicate, format, and maintain citations, bibliographies, identifiers, and source provenance. Use for research, documentation, and evidence-based writing.
---

# Citation and Reference Management

## Quick start

Use this skill when the request matches **Collect, normalize, verify, deduplicate, format, and maintain citations, bibliographies, identifiers, and source provenance. Use for research, documentation, and evidence-based writing.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Scope and classification

Collect, normalize, verify, deduplicate, format, and maintain citations, bibliographies, identifiers, and source provenance. Use for research, documentation, and evidence-based writing. Begin by identifying the system, objects, evidence, constraints, and expected level of precision.

## Method-selection workflow

1. Define citation style and source policy; capture title, author, date, version, URL or DOI, access date, license, and claim linkage; verify metadata at the source; deduplicate; format; and preserve a change log.
2. Write definitions, governing relationships, interfaces, or evidence criteria before applying them.
3. Work from the representation that exposes structure: diagram, table, equation, state model, data schema, or source record.
4. Keep units, domains, assumptions, uncertainty, permissions, and exact-versus-approximate status visible.
5. Interpret the result in the original context and identify what would change the conclusion.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **citation-reference-management**, use this compact record:

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

Open the cited source, verify that it supports the claim, check DOI or URL resolution, distinguish version and publication dates, detect retractions or superseded docs where relevant, and keep citations reproducible. Also perform an independent spot check, counterexample, replay, rendering, or alternate calculation whenever practical.

## Cross-domain quality rules

State the scope, assumptions, version or context, and intended audience before applying the method. Prefer a simple model that is explicit about what it omits. Separate observations, calculations, model outputs, interpretations, and recommendations. Preserve provenance for data, code, diagrams, and sources, and make important results reproducible.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If information is missing or conflicting, state the uncertainty, ask only blocking questions, and avoid fabricating evidence, permissions, results, or completed actions. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For general professional workflow, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Safety and non-goals

These skills are educational and engineering aids, not substitutes for qualified professional review. Do not fabricate studies, measurements, citations, experimental results, or system behavior. Do not provide unsafe wet-lab, high-voltage, hazardous-material, medical, environmental-release, or physical-intervention instructions; keep procedures at a safe planning and analysis level and require appropriate institutional controls. Networking, systems, embedded, and architecture guidance assumes authorization and must not be used for credential theft, destructive exploitation, evasion, or unauthorized access. Do not expose secrets, private data, private infrastructure, or live exam answers.

## Composition and handoff

Compose with `user-task-orchestrator` for routing, `user-scientific-research` for evidence and reproducibility, `user-data-analysis-reporting` for structured data, and focused engineering or security skills when implementation or risk review is required.

## Handoff

Return: classification and scope; inputs, assumptions, and constraints; selected method; actionable steps or worked reasoning; verification and quality checks; limitations and safety boundary; and a concise final answer or artifact description. Name the next specialized skill when the task crosses domains.
