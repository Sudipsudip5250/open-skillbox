---
name: user-backup-restore-drill
description: Plan and verify authorized backup and restore drills with recovery objectives, dependency order, integrity checks, access control, and evidence. Use for owned systems and approved test environments.
---

# Backup and Restore Drill

## Purpose and scope

Confirm authority, target environment, data classification, RPO/RTO, backup source, restore destination, dependency order, communications, and stop conditions before touching data.

## Workflow

Select a representative restore; verify backup age, integrity, encryption, access, and chain; restore into an isolated environment; replay dependencies in order; validate data and application behavior; measure RTO/RPO; record failures; clean up test artifacts; assign remediation.

## Verification and quality checks

Compare restored data with checksums or reconciliations, verify permissions and secrets rotation, test monitoring and rollback, document missing data or configuration, and confirm no production impact.

## Common errors

Common errors include testing only that a backup file exists, restoring over production, ignoring application dependencies, leaking restored PII, and declaring success without user-level validation.

## Rules, safety, and non-goals

Use only owned or explicitly authorized systems, protect sensitive data, and never overwrite production during a drill without separately approved change control. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return authorization and scope, backup/version, restore plan, evidence, RPO/RTO results, integrity and permission checks, failures, cleanup, remediation, and next drill date.
