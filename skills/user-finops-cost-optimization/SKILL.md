---
name: user-finops-cost-optimization
description: Analyze and reduce recurring infrastructure, hosting, API, storage, database, observability, and project operating costs without violating reliability, security, privacy, or performance requirements. Use for cloud bills, resource right-sizing, provider comparisons, budget controls, or cost reviews.
---

# FinOps and Operating Cost Optimization

## Workflow

1. Define the budget, billing period, currency, environments, reliability and latency targets, data-retention needs, and costs that are fixed versus variable.
2. Inventory services, resources, regions, traffic, storage, database usage, observability, AI/API calls, licenses, idle capacity, data transfer, and human maintenance.
3. Attribute spend to projects and environments. Find waste through idle resources, overprovisioning, duplicate services, unnecessary retention, unbounded logs, unused reservations, noisy automation, and expensive failure or retry loops.
4. Compare options using total cost of ownership: setup, usage, egress, support, migration, lock-in, availability, security, compliance, performance, and rollback cost.
5. Apply reversible changes first: schedules, limits, autoscaling, retention, sampling, storage tiers, caching, batching, right-sizing, quotas, and environment cleanup. Protect production and recovery resources.
6. Verify the bill, service-level indicators, latency, error rate, data durability, security controls, and user behavior after the change. Set alerts and review cadence.

## Rules

- Do not delete resources, backups, logs, data, domains, certificates, or production capacity solely to save money without authorization and recovery evidence.
- Never trade away security, privacy, accessibility, durability, or required reliability without stating the risk and obtaining the necessary decision.
- Validate current provider pricing, discounts, taxes, currency, quotas, and regional differences instead of relying on old estimates.
- Separate confirmed savings from projections and state confidence and assumptions.

## Handoff

Report baseline spend and source, cost drivers, ranked opportunities, estimated versus measured savings, quality and risk trade-offs, implementation status, alerts, and next review date.
