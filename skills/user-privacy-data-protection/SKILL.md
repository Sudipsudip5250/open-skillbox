---
name: user-privacy-data-protection
description: Design, review, and improve privacy and data-protection controls in applications, APIs, databases, analytics, logs, and integrations. Use for personal data, consent, retention, deletion, encryption, data exports, tracking, privacy reviews, or privacy-aware production readiness.
---

# Privacy and Data Protection

## Quick start

Use this skill when the request matches **Design, review, and improve privacy and data-protection controls in applications, APIs, databases, analytics, logs, and integrations. Use for personal data, consent, retention, deletion, encryption, data exports, tracking, privacy reviews, or privacy-aware production readiness.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Inventory data categories, subjects, purpose, collection points, processors, destinations, access roles, retention, backups, logs, analytics, and deletion dependencies.
2. Minimize collection, default visibility, precision, retention, and copying. Separate identifiers from content where practical and document the purpose for each sensitive field.
3. Review consent or other approved processing basis, notice, user controls, access/export/correction/deletion behavior, account closure, and regional or contractual requirements. Do not give jurisdiction-specific legal conclusions without the applicable facts and qualified review.
4. Protect data in transit, at rest, in backups, and in non-production. Apply least privilege, tenant isolation, field-level masking, safe logs, redaction, access auditing, and key management.
5. Test unauthorized access, cross-tenant exposure, exports, deletion and restore behavior, retention jobs, analytics identifiers, error paths, uploads, and third-party sharing.
6. Document residual risk, data-flow assumptions, retention owners, incident notification path, and verification evidence.

## Rules

- Do not place personal data, credentials, payment data, or raw user content in prompts, screenshots, logs, fixtures, analytics labels, or public reports unless explicitly required and authorized.
- Do not treat anonymization, hashing, encryption, or deletion as automatically irreversible; assess linkage, backups, keys, and replicas.
- Avoid collecting more data merely because storage is cheap. Privacy and security requirements apply to copies and derived data too.
- Treat privacy requirements as both product behavior and technical controls; do not rely on a policy page alone.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Confirm ownership or written authorization, target scope, environment, evidence handling, rate limits, and stop conditions before active access or testing. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **privacy-data-protection**, use this compact record:

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

## Handoff

Report data flows, categories and purposes, controls, tests, retention and deletion behavior, access model, unresolved legal or policy questions, and residual privacy risk.
