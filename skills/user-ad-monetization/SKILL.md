---
name: user-ad-monetization
description: Design, integrate, test, or optimize advertising on websites, mobile apps, and content channels. Use for AdSense, AdMob, ad managers, mediation, ad placement, consent, viewability, fill, eCPM, invalid traffic, or ad-policy compliance.
---

# Advertising Monetization

## Quick start

Use this skill when the request matches **Design, integrate, test, or optimize advertising on websites, mobile apps, and content channels. Use for AdSense, AdMob, ad managers, mediation, ad placement, consent, viewability, fill, eCPM, invalid traffic, or ad-policy compliance.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Define channel, audience, regions, age profile, content, traffic sources, device matrix, user experience limits, privacy requirements, and target platform policies.
2. Select the least complex suitable model: direct sponsorship, contextual ads, publisher network, app SDK, mediation, rewarded inventory, or a private marketplace. Verify current eligibility, revenue share, policy, SDK, and reporting terms.
3. Design ad slots that are clearly identifiable, do not obstruct navigation, preserve content hierarchy, avoid accidental clicks, respect safe areas, and degrade gracefully when no ad fills or consent is unavailable.
4. Implement consent and privacy signals before personalized advertising. Use a platform-supported or certified consent flow where required, support non-personalized or limited ads, and record consent state without storing unnecessary personal data.
5. Instrument impressions, viewability, fill, eCPM or equivalent yield, latency, errors, layout shift, session engagement, retention, complaints, invalid activity, and policy events. Separate estimates from finalized earnings.
6. Test responsive placement, app lifecycle, WebView or SDK behavior, ad refresh, no-fill, offline, slow network, child-directed treatment, consent changes, deep links, and policy-safe navigation.
7. Optimize one variable at a time and compare net revenue and user outcomes. Maintain a policy review and rollback path.

## Rules

- Never click your own ads, encourage clicks or views, buy invalid traffic, use deceptive placement, or create accidental-click layouts.
- Do not use pop-ups, redirects, fake buttons, hidden ads, or ad designs that users can confuse with navigation or downloads.
- Do not personalize ads before lawful and platform-required consent. Treat children and age-restricted audiences separately.
- Do not claim high revenue from placement changes without measured traffic, fill, yield, geography, platform fee, and retention data.
- Keep ad scripts, SDKs, third-party vendors, and data flows inside the security, privacy, performance, and supply-chain review.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **ad-monetization**, use this compact record:

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

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If information is missing or conflicting, state the uncertainty, ask only blocking questions, and avoid fabricating evidence, permissions, results, or completed actions. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For general professional workflow, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

verify assumptions, important claims, edge cases, usability, safety, reproducibility, and whether the handoff contains enough information for another person or agent to continue. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Handoff

Report platform and policy assumptions, placements, consent behavior, responsive and app tests, metrics, net-revenue impact, invalid-traffic controls, privacy risks, and rollback steps.
