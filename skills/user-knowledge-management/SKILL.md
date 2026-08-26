---
name: user-knowledge-management
description: Organize, retrieve, validate, and maintain durable user, project, domain, and reference knowledge without confusing it with procedural skills or temporary conversation context. Use when setting up knowledge bases, project memory, reusable preferences, repository context, or cross-task operating rules.
---

# Knowledge Management

## Quick start

Use this skill when the request matches **Organize, retrieve, validate, and maintain durable user, project, domain, and reference knowledge without confusing it with procedural skills or temporary conversation context. Use when setting up knowledge bases, project memory, reusable preferences, repository context, or cross-task operating rules.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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


## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the agent host, available tools, instruction precedence, context budget, data boundary, approval gates, expected output, and the smallest skill chain that can complete the task. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **knowledge-management**, use this compact record:

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

Report the knowledge layers and files consulted, relevance and freshness checks, conflicts found, project-isolation decisions, temporary assumptions, durable updates proposed, and which updates require user approval.
