---
name: user-capacity-planning-basics
description: Estimate demand, resource needs, headroom, bottlenecks, load-test plans, uncertainty, and scaling triggers. Use for services, teams, infrastructure, or operational capacity.
---

# Capacity Planning Basics

## Purpose and scope

Define workload unit, forecast horizon, service target, current baseline, constraints, resource dimensions, seasonality, and acceptable risk.

## Workflow

Model demand scenarios; map workload to CPU, memory, storage, network, queue, dependency, and human capacity; identify bottleneck and scaling unit; estimate headroom; test with representative load; define trigger thresholds, procurement or staffing lead time, and rollback or fallback.

## Verification and quality checks

Reconcile forecast with historical data, test sensitivity, check saturation and tail latency, validate assumptions in a safe environment, and document uncertainty rather than reporting a single certain number.

## Common errors

Common errors include extrapolating linear growth, ignoring burstiness, sizing only the first bottleneck, using averages, forgetting dependency capacity, and confusing reserved capacity with usable headroom.

## Rules, safety, and non-goals

Do not run disruptive load tests against systems without authorization. Avoid using estimates as financial, staffing, or safety certainty without responsible review. Do not invent sources, data, results, approvals, or completed actions. Preserve privacy and use the smallest relevant skill composition.

## Handoff

Return demand scenarios, resource model, bottlenecks, headroom, test evidence, triggers, costs or constraints, uncertainty, and review date.
