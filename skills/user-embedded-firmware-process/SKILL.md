---
name: user-embedded-firmware-process
description: Plan embedded-firmware build, test, release, update, rollback, observability, and supply-chain hygiene at a process level. Use for owned or authorized embedded systems.
---

# Embedded Firmware Process

## Purpose and scope

Define hardware revision, toolchain, boot and update model, safety impact, release authority, lab environment, test fixtures, and artifact provenance.

## Workflow

Specify reproducible builds, versioning, configuration separation, unit and hardware-in-loop tests, static analysis, fault injection in a safe lab, signed artifacts, staged deployment, rollback, field telemetry, vulnerability response, and end-of-life handling.

## Verification and quality checks

Verify build reproducibility, hardware compatibility, boot recovery, update interruption, rollback, signing and key custody, logs, test coverage, and release approvals without exposing secrets.

## Common errors

Common errors include testing only the happy path, coupling firmware to untracked hardware, shipping unsigned artifacts, losing rollback, logging sensitive data, and treating a lab result as fleet readiness.

## Rules, safety, and non-goals

Use only owned or authorized hardware and test environments. Do not provide destructive firmware, unauthorized device access, credential extraction, or unsafe physical instructions. Protect signing keys and private diagnostics. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return process map, artifact and version policy, test matrix, release gates, update/rollback plan, observability, incident path, ownership, and residual risk.
