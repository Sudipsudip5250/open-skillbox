---
name: user-knowledge-management
description: Organize, retrieve, validate, and maintain durable user, project, domain, and reference knowledge without confusing it with procedural skills or temporary conversation context. Use when setting up knowledge bases, project memory, reusable preferences, repository context, or cross-task operating rules.
---

# Knowledge Management

## Core distinction

Treat **skills** as procedures and **knowledge** as context. Skills explain how to work; knowledge explains the user, project, domain, constraints, conventions, decisions, and trusted references. Keep them in separate files so either can change without duplicating the other.

## Knowledge layers

| Layer | Examples | Loading rule |
|---|---|---|
| Global preferences | Writing tone, coding style, budget sensitivity, preferred formats | Load when relevant across projects |
| Project profile | Repository purpose, stack, architecture, commands, conventions, deployment | Load only for that project |
| Domain knowledge | Business rules, product definitions, workflows, terminology | Load when the task touches that domain |
| Reference register | Official docs, standards, datasets, source hierarchy, version notes | Load when verification or implementation needs it |
| Decision memory | Approved choices, rejected alternatives, unresolved questions | Load when continuing or revisiting the decision |
| Task scratchpad | Temporary assumptions, intermediate findings, next steps | Use only during the active task; do not promote automatically |

## Personal knowledge-base workflow

For a durable personal knowledge base, define the purpose, audience, privacy level, source-of-truth locations, naming and tagging convention, review cadence, and deletion or export path. Separate stable facts, preferences, project context, decisions, references, and temporary notes. Store provenance, date, scope, confidence, and owner where they affect future decisions. Keep private personal information, credentials, and sensitive records out of public repositories; use the host’s protected Knowledge or local storage instead.

1. Capture only reusable information, not every conversation or transient thought.
2. Normalize duplicates and contradictions deliberately; preserve the source and record which item is authoritative.
3. Retrieve by task relevance and scope, then check freshness before relying on the result.
4. Review stale, unused, sensitive, or conflicting items on a defined cadence and remove or archive them safely.
5. Test retrieval with representative queries and verify that project or personal context does not leak across users or projects.

## Public-safe context packaging

Before exporting project context to another agent, create a minimal pack containing purpose, stack, entry points, commands, conventions, decision records, source register, and known constraints. Exclude credentials, personal preferences unless explicitly approved, private customer data, account-level memory, hidden prompts, and sensitive research. Add a scope, owner, date, freshness, and removal path to each durable item. Keep the source pack separate from procedural skills and test retrieval in a clean project context.

## Retrieval workflow

1. Identify the task domain, project, and required decision.
2. Select the relevant procedural skills.
3. Retrieve only knowledge files matching the project, domain, or decision.
4. Check freshness, ownership, scope, and whether the knowledge is user-approved.
5. Inspect the live project and current sources when knowledge may be stale.
6. Use knowledge as context, not as proof of changing facts.
7. Record durable updates only when the user states or approves them, or when the project’s authoritative source clearly establishes them.

## Update rules

Add a fact only when it is reusable, specific, and likely to remain valid. Include source, date, scope, confidence, and owner when those details matter. Replace contradictions deliberately; do not silently merge incompatible rules. Move temporary assumptions to the scratchpad rather than permanent knowledge.

## Routing statement

For every substantial task, internally apply this sequence: **identify task → load related skills → load relevant knowledge → inspect current sources → execute → verify → report whether durable knowledge should be updated**. Do not require the user to name a skill manually when the request is clear.

## Memory boundaries

Do not infer personal preferences from one isolated request. Do not treat prior chat context as permanent memory unless it is stored in an available project or knowledge file. Do not copy secrets, private credentials, or unnecessary personal data into knowledge. Keep project knowledge isolated so one repository’s conventions do not leak into another.

## Knowledge quality check

Before relying on a knowledge item, ask: Is it relevant? Is it authoritative? Is it current? Is its scope clear? Does it conflict with the current request or project? If any answer is uncertain and the item affects the result, verify it or state the uncertainty.


## Handoff

Report the knowledge layers and files consulted, relevance and freshness checks, conflicts found, project-isolation decisions, temporary assumptions, durable updates proposed, and which updates require user approval.
