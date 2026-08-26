---
name: user-attack-surface-mapping-authorized
description: Map the exposed assets, entry points, trust boundaries, technologies, identities, and sensitive workflows of systems the user owns or is contractually authorized to assess, using passive and controlled methods.
---

# Authorized Attack-Surface Mapping

## Quick start

Use this skill when the request matches **Map the exposed assets, entry points, trust boundaries, technologies, identities, and sensitive workflows of systems the user owns or is contractually authorized to assess, using passive and controlled methods.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Confirm ownership or written authorization, target scope, environment, evidence handling, rate limits, and stop conditions before active access or testing. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **attack-surface-mapping-authorized**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If authorization, scope, or safe evidence handling is missing, pause and provide a planning-only alternative rather than probing, bypassing, or guessing. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For security and trust, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

redact secrets and personal data; preserve evidence integrity; distinguish observation from inference; verify fixes with a bounded retest; and escalate when scope or authority is unclear. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Safety and non-goals

Do not scan arbitrary internet ranges, enumerate third-party infrastructure, bypass access controls, fingerprint covertly, collect unnecessary content, or turn mapping into exploitation or persistence. Never request or retain credentials when a safer user-side action is available. Redact secrets, tokens, PII, and private topology from reports.

## Remediation and retest

Prefer a narrow, owner-assigned fix at the boundary that enforces the security property. Record the change, regression or acceptance test, deployment or configuration version, rollback consideration, and residual risk. If this skill only produces intake, mapping, or evidence, hand the confirmed issue to the findings and remediation skills rather than claiming it is fixed.

## Handoff

Return the ROE reference, asset inventory, trust-boundary and data-flow map, exposure and identity summary, evidence and timestamps, uncertainty, prioritized test candidates, exclusions, and owner assignments.
