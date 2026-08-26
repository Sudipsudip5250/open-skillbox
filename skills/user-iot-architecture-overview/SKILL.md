---
name: user-iot-architecture-overview
description: Explain conceptual IoT architectures, device identity, sensing, connectivity, edge/cloud boundaries, updates, least privilege, and failure modes. Use for educational or authorized design work.
---

# IoT Architecture Overview

## Quick start

Use this skill when the request matches **Explain conceptual IoT architectures, device identity, sensing, connectivity, edge/cloud boundaries, updates, least privilege, and failure modes. Use for educational or authorized design work.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Define device class, environment, data sensitivity, connectivity, operators, update authority, safety impact, lifecycle, and whether the task is conceptual or an authorized system review.

## Workflow

Map device, firmware, gateway, network, cloud, operator, and data flows; identify trust boundaries; describe provisioning, identity, telemetry, command, update, logging, recovery, and decommissioning; assess availability, privacy, safety, and supply-chain risks; propose least-privilege controls.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **iot-architecture-overview**, use this compact record:

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

Check data and command paths, default credentials, update rollback, offline behavior, key rotation, fleet observability, physical access assumptions, and failure containment in a safe model or authorized test environment.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If the failure is not reproducible, capture environment and logs, reduce the case, state uncertainty, and avoid speculative rewrites or destructive recovery steps. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include treating the device as trusted, ignoring physical compromise, mixing control and telemetry paths, assuming connectivity, and recommending a control without lifecycle ownership.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For software and systems, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Keep physical and security guidance conceptual or authorized. Do not provide unsafe electrical procedures, exploit instructions, credential bypass, or access to third-party devices. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return architecture diagram, actors and trust boundaries, data/command flows, lifecycle controls, risks, assumptions, safe tests, and handoff to security or embedded specialists.
