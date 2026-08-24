---
name: user-ad-monetization
description: Design, integrate, test, or optimize advertising on websites, mobile apps, and content channels. Use for AdSense, AdMob, ad managers, mediation, ad placement, consent, viewability, fill, eCPM, invalid traffic, or ad-policy compliance.
---

# Advertising Monetization

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

## Handoff

Report platform and policy assumptions, placements, consent behavior, responsive and app tests, metrics, net-revenue impact, invalid-traffic controls, privacy risks, and rollback steps.
