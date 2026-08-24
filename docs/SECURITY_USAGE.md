# Using the Defensive Security Skills Safely

The security modules are designed for systems the user owns or is contractually authorized to assess. A public URL, repository visibility, or a general request to “find vulnerabilities” is not sufficient authorization for intrusive activity. When authority or scope is ambiguous, an agent should limit itself to passive review, local code and configuration analysis, or a safe fixture until the missing boundary is supplied.

## Recommended authorization statement

Users can provide a statement in this form, adapted to their engagement:

> I own or am authorized by **[organization/person]** to assess **[named applications, APIs, repositories, cloud projects, hosts, CIDRs, tenants, or environments]** from **[start time]** through **[end time]**. Approved activities are **[passive review, staging tests, specified benign dynamic checks]**. The following are out of scope: **[assets, accounts, data, techniques, and production actions]**. Use **[test accounts and synthetic data]**, limit traffic to **[rate/concurrency]**, retain only **[approved redacted evidence]**, notify **[contact]**, and stop on **[PII/secrets, instability, destructive impact, scope drift, or other stop conditions]**. Production testing is **[not allowed / explicitly accepted by named approver]**.

Do not send passwords, API keys, private tokens, personal data, or confidential evidence in a chat request when a safer user-side action or redacted artifact is available. Provide identifiers, roles, synthetic records, fingerprints, and locations instead.

## What the agent should produce before active testing

| Required item | Example content |
|---|---|
| Authority | Owner or engagement reference and scope-change approver |
| In scope | Exact URLs, API hosts, repositories, accounts, environments, tenants, cloud projects, or CIDRs |
| Out of scope | Third parties, excluded assets, production actions, sensitive data, and forbidden techniques |
| Window and controls | Dates, test accounts, tools, rate limits, notification contact, and evidence retention |
| Environment | Local fixture, development, staging, or explicitly risk-accepted production |
| Stop conditions | Unexpected PII or secrets, instability, destructive effect, scope drift, or policy uncertainty |
| Handoff | Findings, severity, evidence, remediation, retest status, residual risk, and owner |

The preferred sequence is **find → verify safely → report → fix → retest**. The kit does not provide jailbreak, unrestricted-mode, safeguard-bypass, unauthorized-intrusion, credential-theft, persistence, malware, anti-forensics, or third-party copyright/watermark-circumvention skills.
