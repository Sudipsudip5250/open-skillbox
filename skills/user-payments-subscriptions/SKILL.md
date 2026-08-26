---
name: user-payments-subscriptions
description: Build or review payments, billing, subscriptions, in-app purchases, entitlements, refunds, and payment webhooks for websites and mobile apps. Use for Stripe, Apple StoreKit, Google Play Billing, checkout, recurring billing, pricing plans, access control, or billing failures.
---

# Payments and Subscriptions

## Quick start

Use this skill when the request matches **Build or review payments, billing, subscriptions, in-app purchases, entitlements, refunds, and payment webhooks for websites and mobile apps. Use for Stripe, Apple StoreKit, Google Play Billing, checkout, recurring billing, pricing plans, access control, or billing failures.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Workflow

1. Define product, customer, geography, currencies, taxes, billing model, trial and offer rules, platform, entitlement, refund, dispute, and support requirements.
2. Choose the correct payment rail: web checkout or payment elements, platform in-app purchase, marketplace flow, or another approved provider. Verify current platform rules and version requirements.
3. Model products, prices, customers, subscriptions, purchases, invoices, transactions, entitlements, states, refunds, disputes, and audit records. Keep price and entitlement identity explicit.
4. Implement server-side verification and webhook or store-notification handling. Verify signatures, deduplicate events, process out of order safely, retry idempotently, persist event history, and reconcile with the provider.
5. Grant access from verified entitlement state, not from an untrusted client callback or redirect. Handle trial, active, grace, past-due, paused, canceled, expired, refunded, disputed, pending, and restored states.
6. Test successful and interrupted purchases, duplicate events, delayed events, failed payment, customer authentication, cancellation, upgrade, downgrade, renewal, refund, restore, device change, offline state, clock differences, and provider outage.
7. Protect keys, payment data, logs, webhooks, admin operations, user privacy, and support workflows. Monitor conversion, activation, churn, recovery, refunds, disputes, entitlement mismatches, and webhook failures.

## Rules

- Never store raw card data unless the project has the required compliant architecture; prefer provider-hosted or tokenized flows.
- Do not unlock paid features solely from client input, a success URL, or an unverifiable receipt.
- Do not silently change price, renew a canceled plan, block cancellation, hide fees, or make refunds impossible.
- Do not assume Stripe, Apple, Google Play, or another provider shares the same lifecycle, fee, tax, or store rules. Use version-matched documentation.
- Treat tax, consumer-protection, refund, and platform-policy requirements as jurisdiction- and product-specific; obtain qualified review for consequential launch decisions.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **payments-subscriptions**, use this compact record:

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

Report provider and platform assumptions, product and entitlement model, lifecycle state machine, webhook verification and idempotency, security and privacy controls, tests, refunds and disputes, monitoring, and unresolved compliance risks.
