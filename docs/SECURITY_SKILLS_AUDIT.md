# Defensive Security Skills Audit

## Audit scope

This audit compares the current public security catalog with the attached authorized-defensive-security brief. The audit baseline contained **12 security-focused skills** within a **106-skill** catalog. Existing modules were retained. After the implementation pass, the repository contains **19 security-focused skills** within a **113-skill** catalog: the original 12, plus seven narrowly scoped authorized-security modules.

## Current coverage

| Existing skill | Strong coverage already present | Gap against the brief |
|---|---|---|
| `user-authorized-security-testing` | Authorized test planning, ASVS/WSTG mapping, benign dynamic checks, evidence, remediation, and retest | Needs a fuller Rules-of-Engagement intake with explicit in/out-of-scope assets, forbidden actions, production-risk acceptance, and a reusable pre-test summary |
| `user-vulnerability-detection` | Layered SAST/SCA/SBOM/secret/IaC/container review, evidence, triage, remediation, and regression checks | Needs the same standardized authorization gate and findings/retest template used for active assessments |
| `user-threat-modeling` | Trust boundaries, STRIDE-style abuse cases, mitigations, owners, detection, and residual risk | Needs explicit scoped-assessment framing and a clearer handoff into authorized verification |
| `user-web-application-security` | Browser/server/API boundaries, AuthN/AuthZ, IDOR-style checks, injection classes, sessions, uploads, SSRF, WebSockets, GraphQL, webhooks, and benign negative-path testing | Needs shared Rules of Engagement output, explicit target inventory and stop conditions, and fix-first findings/retest structure |
| `user-ai-application-security` | Prompt injection, poisoning, tool permissions, excessive agency, privacy, output validation, approval gates, and benign regression evaluation | Needs authorized asset/scope intake and a dedicated handoff for tool-permission and exfiltration-path review |
| `user-prompt-injection-defense` | Defensive-only posture, provenance separation, architectural controls, benign regression cases, and monitoring | Needs the same authorization/scope convention when testing a user-owned agent application; must preserve its explicit no-bypass boundary |
| `user-database-security` | Network isolation, least privilege, query/ORM review, row-level controls, backups, restore tests, and negative cross-tenant checks | Needs scoped target inventory, forbidden/destructive-action list, stop conditions, and findings/retest handoff |
| `user-identity-access-security` | AuthN, MFA, sessions, tokens, OAuth/OIDC/SAML, server-side authorization, tenant isolation, replay and recovery tests | Needs the shared Rules-of-Engagement intake and an explicit findings table with evidence, remediation, retest status, and residual risk |
| `user-infrastructure-cloud-security` | Account/environment inventory, IAM, network exposure, IaC, Kubernetes, runtime verification, exceptions, and recovery | Needs explicit account ownership, in/out-of-scope resources, production-risk acceptance, forbidden changes, and stop conditions |
| `user-secrets-supply-chain-security` | Secret scanning and rotation, SBOM/dependencies, CI/CD permissions, provenance, artifact integrity, incident exercises | Needs scoped-assessment framing and a clearer safe handoff for evidence and rotation/retest status |
| `user-security-hardening` | Broad fix-first review of trust boundaries, auth, inputs, secrets, dependencies, logging, findings, and residual risk | Needs a standardized authorization gate and explicit Rules-of-Engagement summary before any active test |
| `user-security-risk-review` | Broad security/privacy/access/dependency review, authorized-vs-unauthorized flows, severity, remediation, and verification | Needs explicit asset/time/data/forbidden-action intake and a more complete findings handoff |

## Gap classification

The audit found that the repository already has substantive defensive coverage for the brief’s major areas: reconnaissance at a high level, access control, input and injection review, sessions and tokens, API abuse cases, cloud and IAM configuration, supply chain and secrets, AI-specific risks, evidence, remediation, and retesting. The principal cross-cutting gap is consistency: most specialized skills begin directly with a technical workflow instead of first producing a short authorization and Rules-of-Engagement record.

The second gap is decomposition. The existing umbrella skills are useful, but a user asking for a deep authorized assessment would benefit from dedicated modules for the intake gate, attack-surface mapping, access-control testing, API assessment, security findings reporting, remediation verification, and AI-agent tool-permission review. These modules should coordinate rather than duplicate the detailed domain checklists already present.

## Implemented focused modules

| New skill | Distinct purpose |
|---|---|
| `user-rules-of-engagement-security` | Authorization, scope, environment, controls, evidence, and stop-condition intake before active testing |
| `user-attack-surface-mapping-authorized` | Passive and controlled asset, entry-point, technology, identity, and trust-boundary mapping |
| `user-access-control-testing-authorized` | Test-account-based AuthN/AuthZ, IDOR-style, tenant, session, recovery, and negative-path verification |
| `user-api-security-assessment-authorized` | Scoped REST, GraphQL, webhook, validation, abuse-resistance, and data-exposure assessment |
| `user-security-findings-report` | Evidence-led severity, confidence, remediation, disclosure, and residual-risk reporting |
| `user-remediation-verification-retest` | Focused fix verification, regression checks, closure status, and residual-risk recording |
| `user-ai-agent-tool-permission-review` | Agent tool permissions, approval gates, data boundaries, and benign exfiltration-path evaluation |

These modules intentionally do not include `user-secure-code-review-deep` because the existing code-review, security-hardening, vulnerability-detection, and web/API modules already cover that boundary. Reconsider it only if later usage demonstrates a distinct unmet workflow.

## Prioritized plan

| Priority | Work | Rationale |
|---|---|---|
| Complete | Add a shared authorization/Rules-of-Engagement pattern to every security skill; strengthen the orchestrator | All 12 existing security skills now open with explicit authority, asset scope, environment, controls, data handling, and stop-condition guidance; routing now starts security assessments with the ROE module |
| Complete | Add `user-rules-of-engagement-security`, `user-security-findings-report`, and `user-remediation-verification-retest` | Cross-cutting workflow gaps are now separate, composable modules |
| Complete | Add `user-attack-surface-mapping-authorized`, `user-access-control-testing-authorized`, and `user-api-security-assessment-authorized` | High-value assessment stages now have focused authorized workflows |
| Complete | Add `user-ai-agent-tool-permission-review` and strengthen AI/prompt-injection routing | Agent permission review is discoverable while jailbreak and safeguard-bypass requests remain explicitly refused |
| Deferred | Consider `user-secure-code-review-deep` only if later repository use shows a real gap beyond existing code review, security hardening, and vulnerability-detection skills | Avoid creating a duplicate code-review umbrella before evidence justifies it |

## Safety conclusion

No jailbreak, unrestricted-mode, safeguard-bypass, unauthorized-intrusion, credential-theft, persistence, malware, anti-forensics, or third-party watermark/copyright-circumvention skill is warranted or permitted. The repository should maximize depth only after ownership or documented authorization, target inventory, environment preference, rate limits, evidence handling, and stop conditions are recorded. The preferred sequence remains **find → verify safely → report → fix → retest**.
