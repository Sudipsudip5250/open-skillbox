---
name: user-context-engineering
description: Improve agent performance by selecting, organizing, and loading the right task, project, skill, and reference context. Use when starting a complex task, switching repositories, context is large, output quality drops, or multiple skills and knowledge sources overlap.
---

# Context Engineering

## Quick start

Use this skill when the request matches **Improve agent performance by selecting, organizing, and loading the right task, project, skill, and reference context. Use when starting a complex task, switching repositories, context is large, output quality drops, or multiple skills and knowledge sources overlap.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Identify the current task, repository, audience, constraints, acceptance criteria, and required evidence. Do not assume context from an unrelated project.
2. Load only the smallest relevant set: task instructions first, project profile and current files second, triggered skills third, and detailed references or historical material only when needed.
3. Classify domain depth. For broad questions, use general routing; for mathematics, science, systems, education, ML, or other chapters, load the narrow domain skill after the coordinator.
4. Prefer progressive disclosure: keep metadata and routing concise, read the full skill only after it triggers, and load reference files only for the active variant or decision.
5. Build a compact working brief with facts, assumptions, decisions, open questions, commands, evidence, and verification targets. Remove duplicated or stale context.
6. After context compaction, re-check the project path, user requirements, modified files, test state, and unresolved risks before continuing.
7. At handoff, preserve only stable approved decisions, project conventions, and reusable facts in durable project knowledge. Keep temporary reasoning and task-specific noise out.

## Rules

- Do not load every available skill or repository document by default.
- Treat Knowledge as context and Skills as procedures; neither replaces current source inspection.
- Keep projects isolated. A preference may be global, but architecture, credentials, business rules, commands, and domain assumptions are project-specific unless explicitly approved otherwise.
- If a required source is unavailable, state the gap rather than filling it with plausible assumptions.
- Do not treat a skill’s existence in the repository as proof that it was loaded or that its guidance is current.

## When not to use this skill

Do not use it to avoid reading the files or sources required for correctness, to compress away safety or authorization constraints, or to replace a domain workflow when the task requires specialized methods. Do not load a broad chapter catalog when one focused procedure is sufficient.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the agent host, available tools, instruction precedence, context budget, data boundary, approval gates, expected output, and the smallest skill chain that can complete the task. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **context-engineering**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If a host cannot load the canonical format or a tool is unavailable, preserve the source skill and document a reversible adapter or manual fallback rather than claiming compatibility. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For agent workflow and governance, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

run a representative prompt, inspect tool traces and handoffs, test refusal and uncertainty behavior, verify no private context leaks, and compare against a fixed baseline when evaluating changes. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Handoff

Report the context used, active skills and knowledge, important assumptions, sources inspected, unresolved gaps, compaction recovery checks, and any durable Knowledge candidate that needs user approval.
