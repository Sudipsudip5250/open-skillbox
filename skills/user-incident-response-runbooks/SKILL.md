---
name: user-incident-response-runbooks
description: Create and execute safe, authorized incident-response runbooks for owned systems, covering preparation, detection, analysis, containment, eradication, recovery, communications, and lessons learned.
---

# Incident Response Runbooks

## Purpose and scope

Turn incident signals into coordinated, reversible actions with clear authority, evidence handling, service-protection priorities, and post-incident improvement. Create and execute safe, authorized incident-response runbooks for owned systems, covering preparation, detection, analysis, containment, eradication, recovery, communications, and lessons learned.

## Classification and inputs

Identify the request, audience, source materials, constraints, assumptions, permissions, version or jurisdiction, and required precision before selecting a method. Separate observed facts, user-provided inputs, calculations, model outputs, and interpretations.

## Workflow

1. Confirm the incident channel, incident commander, affected owner, authorization to act, severity criteria, communication contacts, and safety or legal constraints.
2. Record the initial signal, time, affected assets, current impact, confidence, evidence location, and what is not yet known; preserve volatile evidence without exposing secrets or PII.
3. Triage scope and business impact, protect people and critical services, and choose the least disruptive containment that limits further harm.
4. Coordinate eradication and recovery with system owners; preserve rollback, backups, change records, validation gates, and a decision log.
5. Communicate factual status, uncertainty, user impact, and next update time to the right audiences; do not speculate or disclose sensitive technical detail unnecessarily.
6. Verify recovery with health, security, data-integrity, monitoring, and access checks; then conduct a blameless review and track corrective actions.

## Runbook template

For each action, record **precondition → owner → command or decision → expected result → evidence → rollback or stop condition**. Keep preparation, detection, containment, recovery, communication, and closure steps separately addressable. Mark destructive or externally visible actions as approval-gated and define a safe dry run where practical.

## Verification and quality checks

Check authority and approvals, timeline consistency, evidence integrity, containment side effects, recovery health, credential rotation or access changes where applicable, monitoring coverage, and closure criteria.

## Common errors

Common errors include deleting evidence, making uncontrolled changes, confusing symptoms with root cause, communicating unverified claims, restoring a compromised artifact, and closing without monitoring or follow-up owners.

## Rules, safety, and non-goals

Use only on incidents involving systems or organizations the user owns or is authorized to operate. Do not provide retaliation, unauthorized intrusion, destructive cleanup, anti-forensics, or public disclosure instructions. Follow the organization’s legal, privacy, safety, and regulatory process. Do not invent sources, data, results, approvals, or completed actions. Use the smallest relevant skill set and hand off to specialized research, security, data, accessibility, or implementation skills when the task crosses boundaries.

## Handoff

Return incident authority and severity, timeline, affected assets, evidence and limitations, decisions and approvals, containment/recovery status, communications, residual risk, corrective actions, owners, and next review date.
