---
name: user-iot-architecture-overview
description: Explain conceptual IoT architectures, device identity, sensing, connectivity, edge/cloud boundaries, updates, least privilege, and failure modes. Use for educational or authorized design work.
---

# IoT Architecture Overview

## Purpose and scope

Define device class, environment, data sensitivity, connectivity, operators, update authority, safety impact, lifecycle, and whether the task is conceptual or an authorized system review.

## Workflow

Map device, firmware, gateway, network, cloud, operator, and data flows; identify trust boundaries; describe provisioning, identity, telemetry, command, update, logging, recovery, and decommissioning; assess availability, privacy, safety, and supply-chain risks; propose least-privilege controls.

## Verification and quality checks

Check data and command paths, default credentials, update rollback, offline behavior, key rotation, fleet observability, physical access assumptions, and failure containment in a safe model or authorized test environment.

## Common errors

Common errors include treating the device as trusted, ignoring physical compromise, mixing control and telemetry paths, assuming connectivity, and recommending a control without lifecycle ownership.

## Rules, safety, and non-goals

Keep physical and security guidance conceptual or authorized. Do not provide unsafe electrical procedures, exploit instructions, credential bypass, or access to third-party devices. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return architecture diagram, actors and trust boundaries, data/command flows, lifecycle controls, risks, assumptions, safe tests, and handoff to security or embedded specialists.
