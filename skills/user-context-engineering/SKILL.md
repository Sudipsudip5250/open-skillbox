---
name: user-context-engineering
description: Improve agent performance by selecting, organizing, and loading the right task, project, skill, and reference context. Use when starting a complex task, switching repositories, context is large, output quality drops, or multiple skills and knowledge sources overlap.
---

# Context Engineering

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

## Handoff

Report the context used, active skills and knowledge, important assumptions, sources inspected, unresolved gaps, compaction recovery checks, and any durable Knowledge candidate that needs user approval.
