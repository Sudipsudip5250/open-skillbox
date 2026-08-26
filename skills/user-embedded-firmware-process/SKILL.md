---
name: user-embedded-firmware-process
description: Plan embedded-firmware build, test, release, update, rollback, observability, and supply-chain hygiene at a process level. Use for owned or authorized embedded systems.
---

# Embedded Firmware Process

## Quick start

Use this skill when the request matches **Plan embedded-firmware build, test, release, update, rollback, observability, and supply-chain hygiene at a process level. Use for owned or authorized embedded systems.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Define hardware revision, toolchain, boot and update model, safety impact, release authority, lab environment, test fixtures, and artifact provenance.

## Workflow

Specify reproducible builds, versioning, configuration separation, unit and hardware-in-loop tests, static analysis, fault injection in a safe lab, signed artifacts, staged deployment, rollback, field telemetry, vulnerability response, and end-of-life handling.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **embedded-firmware-process**, use this compact record:

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

Verify build reproducibility, hardware compatibility, boot recovery, update interruption, rollback, signing and key custody, logs, test coverage, and release approvals without exposing secrets.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If the failure is not reproducible, capture environment and logs, reduce the case, state uncertainty, and avoid speculative rewrites or destructive recovery steps. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include testing only the happy path, coupling firmware to untracked hardware, shipping unsigned artifacts, losing rollback, logging sensitive data, and treating a lab result as fleet readiness.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For software and systems, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Use only owned or authorized hardware and test environments. Do not provide destructive firmware, unauthorized device access, credential extraction, or unsafe physical instructions. Protect signing keys and private diagnostics. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return process map, artifact and version policy, test matrix, release gates, update/rollback plan, observability, incident path, ownership, and residual risk.
