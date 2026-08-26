---
name: user-skill-authoring
description: Create or revise repository-compatible modular skills with narrow triggers, progressive disclosure, safety boundaries, verification, and handoffs. Use when writing a new SKILL.md for this catalog.
---

# Skill Authoring

## Quick start

Use this skill when the request matches **Create or revise repository-compatible modular skills with narrow triggers, progressive disclosure, safety boundaries, verification, and handoffs. Use when writing a new SKILL.md for this catalog.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Start by checking the existing index, taxonomy, overlap, audience, trigger, and whether an existing skill should be extended instead.

## Workflow

Define one task boundary; choose a `user-<kebab-case>` canonical directory for backward-compatible repository discovery; write frontmatter; add purpose, workflow, verification, common failures, rules/non-goals, composition, and handoff; keep content concise; add only useful references or scripts; update index and sources; run validators.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the agent host, available tools, instruction precedence, context budget, data boundary, approval gates, expected output, and the smallest skill chain that can complete the task. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **skill-authoring**, use this compact record:

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

Test metadata and structure, inspect trigger distinctness, verify links and public paths, run representative scenarios, check safety boundaries, and review for secrets, copied text, unsupported claims, and overlap.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If a host cannot load the canonical format or a tool is unavailable, preserve the source skill and document a reversible adapter or manual fallback rather than claiming compatibility. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include vague triggers, giant umbrella skills, duplicated procedures, hidden assumptions, unbounded tool use, stale sources, and a handoff that does not describe the deliverable.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For agent workflow and governance, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not put private project knowledge, credentials, proprietary prompts, copyrighted textbook dumps, or unsafe bypass instructions in a public skill. Preserve existing skills unless a documented surgical change is approved. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return skill directory, trigger rationale, overlap analysis, workflow, sources, validation output, scenario test, and follow-up improvements.
