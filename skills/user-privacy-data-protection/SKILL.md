---
name: user-privacy-data-protection
description: Design, review, and improve privacy and data-protection controls in applications, APIs, databases, analytics, logs, and integrations. Use for personal data, consent, retention, deletion, encryption, data exports, tracking, privacy reviews, or privacy-aware production readiness.
---

# Privacy and Data Protection

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

## Handoff

Report data flows, categories and purposes, controls, tests, retention and deletion behavior, access model, unresolved legal or policy questions, and residual privacy risk.
