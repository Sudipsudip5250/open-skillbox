---
name: user-attack-surface-mapping-authorized
description: Map the exposed assets, entry points, trust boundaries, technologies, identities, and sensitive workflows of systems the user owns or is contractually authorized to assess, using passive and controlled methods.
---

# Authorized Attack-Surface Mapping

## Purpose

Use after the ROE gate when the assessment needs a defensible inventory and attack-surface map. The output is an asset and exposure model, not an invitation to explore outside scope.

## Authorization gate

Confirm ownership or documented contractual authorization before touching private or live assets. Load or create a short Rules-of-Engagement record with in-scope and out-of-scope assets, environment, time window, allowed methods, rate limits, data handling, notification contacts, and stop conditions. Prefer local review, fixtures, passive checks, and non-production. If authority or scope is ambiguous, stop active work and request the missing boundary.

## Workflow

1. Load the approved ROE and create an asset register with target, owner, environment, source, status, and in/out-of-scope state.
2. Start with passive sources: repository manifests, IaC, architecture documents, DNS or certificate records the user controls, logs, deployment metadata, and application routes.
3. Identify interfaces: browser pages, APIs, webhooks, uploads, admin paths, workers, queues, storage, databases, identity providers, third parties, CI/CD, and management planes.
4. Record technologies and versions only when observed or sourced; distinguish confirmed assets from inferred or stale entries.
5. Map trust boundaries, data flows, identities, tenants, privileged actions, public exposure, dependencies, and high-value workflows.
6. Use controlled active discovery only on approved assets, with conservative rate limits, benign requests, test accounts, and immediate stop conditions.
7. Prioritize follow-up by exposure, privilege, sensitivity, reachability, and uncertainty; link each map item to an owner and evidence.

## Verification

Reconcile the map against deployment and repository inventories, check that discovered hosts and routes are in scope, deduplicate aliases, timestamp observations, test representative benign reachability, and flag unverified assumptions.

## Safety and non-goals

Do not scan arbitrary internet ranges, enumerate third-party infrastructure, bypass access controls, fingerprint covertly, collect unnecessary content, or turn mapping into exploitation or persistence. Never request or retain credentials when a safer user-side action is available. Redact secrets, tokens, PII, and private topology from reports.

## Remediation and retest

Prefer a narrow, owner-assigned fix at the boundary that enforces the security property. Record the change, regression or acceptance test, deployment or configuration version, rollback consideration, and residual risk. If this skill only produces intake, mapping, or evidence, hand the confirmed issue to the findings and remediation skills rather than claiming it is fixed.

## Handoff

Return the ROE reference, asset inventory, trust-boundary and data-flow map, exposure and identity summary, evidence and timestamps, uncertainty, prioritized test candidates, exclusions, and owner assignments.
