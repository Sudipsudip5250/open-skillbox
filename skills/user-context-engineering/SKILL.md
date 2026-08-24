---
name: user-context-engineering
description: Improve agent performance by selecting, organizing, and loading the right task, project, skill, and reference context. Use when starting a complex task, switching repositories, context is large, output quality drops, or multiple skills and knowledge sources overlap.
---

# Context Engineering

## Workflow

1. Identify the current task, repository, audience, constraints, acceptance criteria, and required evidence. Do not assume context from an unrelated project.
2. Load only the smallest relevant set: task instructions first, project profile and current files second, triggered Skills third, and detailed references or historical material only when needed.
3. Prefer progressive disclosure: keep metadata and routing concise, read the full skill only after it triggers, and load reference files only for the active variant or decision.
4. Build a compact working brief with facts, assumptions, decisions, open questions, commands, and verification targets. Remove duplicated or stale context.
5. After context compaction, re-check the project path, user requirements, modified files, test state, and unresolved risks before continuing.
6. At handoff, preserve only stable approved decisions, project conventions, and reusable facts in durable project knowledge. Keep temporary reasoning and task-specific noise out.

## Rules

- Do not load every available Skill or repository document by default.
- Treat Knowledge as context and Skills as procedures; never replace current source inspection with either.
- Keep projects isolated. A preference may be global, but architecture, credentials, business rules, and commands are project-specific unless explicitly approved otherwise.
- If a required source is unavailable, state the gap rather than filling it with plausible assumptions.

## Handoff

Report the context used, important assumptions, sources inspected, unresolved gaps, and any durable Knowledge candidate that needs user approval.
