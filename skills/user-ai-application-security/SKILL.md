---
name: user-ai-application-security
description: Secure AI-enabled applications, agents, RAG systems, model integrations, and tool-using workflows. Use for prompt injection, data poisoning, unsafe tool calls, model-output validation, agent permissions, AI privacy, or AI production-readiness reviews.
---

# AI Application Security

## Workflow

1. Map users, models, prompts, retrieved data, tools, plugins, memory, files, external APIs, secrets, outputs, and approval boundaries.
2. Identify threats: direct and indirect prompt injection, data poisoning, sensitive-data disclosure, insecure tool use, excessive agency, privilege escalation, output injection, denial of service, model supply chain, and unsafe automation.
3. Separate instructions from untrusted content. Label source provenance, constrain retrieval scope, isolate tenants, validate tool arguments and model outputs, and enforce authorization outside the model.
4. Give agents the minimum tools and permissions required. Use allowlists, schemas, sandboxing, timeouts, rate limits, human approval for consequential actions, and deterministic policy checks before execution.
5. Protect prompts, memory, logs, files, embeddings, model keys, and user data. Minimize retention, redact sensitive content, and prevent cross-user or cross-project recall.
6. Evaluate with benign adversarial test cases, policy tests, data-leakage checks, tool-call validation, refusal and escalation paths, cost/latency limits, and regression suites. Repeat after model, prompt, tool, or retrieval changes.

## Rules

- Treat model output as untrusted data, not authority. Never let it bypass application authorization or security policy.
- Do not paste secrets or private data into a model or external provider unless the user and system policy explicitly authorize it.
- Do not build or test malware, credential theft, evasion, autonomous exploitation, or unauthorized access under the label of AI security.
- Do not claim an AI system is safe from prompt tests alone. State model, tool, data, environment, and evaluator limitations.

## Handoff

Report system boundaries, threats, controls, allowed tools, approval gates, evaluation cases and results, privacy handling, model/provider assumptions, residual risk, and monitoring plan.
