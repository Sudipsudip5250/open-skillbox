---
name: user-changelog-release-notes
description: Produce accurate changelogs and release notes with user impact, migration notes, known issues, and version traceability. Use for software, content, or product releases.
---

# Changelog and Release Notes

## Purpose and scope

Identify release version, audience, date, change source, compatibility promise, and whether the note is public, internal, or customer-specific.

## Workflow

Collect merged changes and verified fixes; classify added, changed, fixed, deprecated, removed, security, and known issues; describe user impact; add migration or rollback notes; link relevant tickets or docs; state limitations and support path; preserve semantic versioning or the project’s own convention.

## Verification and quality checks

Cross-check each statement against the release artifact, test upgrade paths, verify links and versions, distinguish planned from shipped changes, and confirm that security details follow disclosure policy.

## Common errors

Common errors include documenting unreleased work, overstating compatibility, omitting breaking changes, hiding known issues, and mixing internal implementation details with user-relevant impact.

## Rules, safety, and non-goals

Do not fabricate fixes, security claims, or support commitments. Redact private tickets, secrets, and exploit-enabling details. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return versioned notes, change categories, migration steps, known issues, references, verification status, and owner.
