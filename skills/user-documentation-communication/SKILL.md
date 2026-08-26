---
name: user-documentation-communication
description: Produce clear, accurate, audience-appropriate documentation and communication artifacts, including READMEs, specifications, SOPs, proposals, reports, release notes, and handoffs. Use whenever technical or project work must be understood or operated by someone else.
---

# Documentation and Communication

## Quick start

Use this skill when the request matches **Produce clear, accurate, audience-appropriate documentation and communication artifacts, including READMEs, specifications, SOPs, proposals, reports, release notes, and handoffs. Use whenever technical or project work must be understood or operated by someone else.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Writing workflow

1. Identify the audience, purpose, decision or action required, existing knowledge, and preferred format.
2. Lead with the answer or outcome. Organize from essential information to supporting detail.
3. Define terms before using them and state prerequisites, assumptions, ownership, and boundaries.
4. Use examples, commands, tables, diagrams, or checklists when they reduce ambiguity.
5. Keep instructions executable: specify inputs, expected outputs, error handling, and verification.
6. Review for factual accuracy, stale references, contradictory steps, accessibility, tone, and unnecessary repetition.
7. Make the artifact self-contained enough for its intended audience while linking to deeper references when appropriate.

## Document patterns

| Artifact | Must answer |
|---|---|
| README | What it is, who it is for, prerequisites, setup, usage, tests, and support |
| Specification | Problem, users, requirements, non-goals, interfaces, acceptance criteria, and risks |
| SOP/runbook | Trigger, owner, exact steps, checks, failure recovery, and escalation |
| Proposal | Context, options, recommendation, trade-offs, cost, risks, and decision requested |
| Release notes | What changed, impact, migration, known issues, and rollback or support path |
| Report | Question, method, evidence, findings, limitations, and implications |

Do not document behavior that was not verified. Prefer direct language and concrete examples over vague promises.


## Quality and safety rules

Do not document unverified behavior, expose secrets or personal data, silently change operational instructions, or present regulated guidance as professional advice. Mark drafts, assumptions, owners, dates, version requirements, and review status when they affect safe use.

## When not to use this skill

Do not use it as a substitute for domain research, code implementation, security review, legal review, or document remediation when the task requires those specialized methods.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define audience, purpose, format, voice, source material, version or jurisdiction, accessibility, asset rights, review owner, and the claims the deliverable is allowed to make. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **documentation-communication**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If the source is incomplete or an asset is not clearly permitted, mark the gap and use a placeholder or original alternative instead of inventing, copying, or removing rights information. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For writing and creative production, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

review factual claims and citations, structure, readability, accessibility, timing or rendering, rights and attribution, placeholders, and whether the final wording overstates certainty. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Handoff

Report the artifact type, audience, source material, assumptions, files changed, verification performed, owner, version or date, known limitations, and next review point.
