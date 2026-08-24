---
name: user-payments-subscriptions
description: Build or review payments, billing, subscriptions, in-app purchases, entitlements, refunds, and payment webhooks for websites and mobile apps. Use for Stripe, Apple StoreKit, Google Play Billing, checkout, recurring billing, pricing plans, access control, or billing failures.
---

# Payments and Subscriptions

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

## Handoff

Report provider and platform assumptions, product and entitlement model, lifecycle state machine, webhook verification and idempotency, security and privacy controls, tests, refunds and disputes, monitoring, and unresolved compliance risks.
