# Presentation Script: Agent Skill Kit Across Agents

**Suggested duration:** 10–12 minutes  
**Audience:** Developers, AI-agent builders, technical leads, and maintainers  
**Purpose:** Explain how open-skillbox packages, composes, exports, and maintains reusable skills across Manus and other agent hosts.

## Slide 1 — From one agent setup to a portable skill kit

**On-slide message:**

> One canonical skill catalog. Many agent hosts. Explicit portability boundaries.

**Speaker script:**

Agent Skill Kit began as a Manus-oriented collection of reusable `SKILL.md` procedures. It has evolved into a host-neutral, modular catalog for agents that can read filesystem-based instructions. The key design decision is separation: the repository stores canonical procedures, while adapters and exporters handle host-specific discovery. That lets the same reasoning workflow move between Manus, Claude Code, Codex, Cursor, Replit, Kiro, Kilo, Antigravity, OpenCode, Mimo Code, and future hosts without pretending that their runtimes or permissions are identical.

## Slide 2 — The architecture in one picture

**On-slide diagram:**

```text
User request
     |
     v
Orchestrator and routing
     |
     +--> Canonical SKILL.md package
     |         |
     |         +--> Optional references, scripts, templates, assets
     |
     +--> Verification and safety gates
     |
     v
Portable exporter and host adapter
     |
     +--> Manus project skill location
     +--> Claude Code / .claude/skills/
     +--> Cursor / .cursor/skills/ or .agents/skills/
     +--> Other host-specific directory or manual import
     |
     v
Artifact, evidence, and recoverable handoff
```

**Speaker script:**

The architecture has five layers. The user request enters the orchestrator, which selects the smallest useful skill chain. The canonical skill owns the procedure and its boundaries. Optional resources provide detail only when needed. Verification and safety gates protect the workflow. Finally, the exporter copies the unchanged canonical package into an explicit host destination. The output is not merely an answer; it is an artifact with evidence, assumptions, limitations, and a next action.

## Slide 3 — What a canonical skill contains

**On-slide table:**

| Layer | Role |
|---|---|
| Metadata | Precise trigger and activation boundary |
| Quick start | Immediate orientation for the agent |
| Inputs and decisions | Required context and method selection |
| Workflow | Ordered, actionable procedure |
| Worked pattern | Reusable record or example |
| Verification | Correctness, safety, quality, and reproducibility checks |
| Failure handling | Diagnosis, recovery, escalation, and stop conditions |
| Portability and maintenance | Host-neutral behavior and update triggers |
| Handoff | Deliverable, evidence, limitations, and next step |

**Speaker script:**

A skill is not a long essay and it is not a vague prompt. It is an operational playbook. The metadata helps the agent discover it. The body tells the agent what to do, how to choose a method, how to verify the result, and how to hand the work to another agent or person. The new depth standard requires these parts for every module, but it does not require every module to become a textbook. High-risk or version-sensitive topics can move detailed material into optional references and scripts.

## Slide 4 — Creating a custom multi-domain starter pack

**On-slide command:**

```bash
python scripts/export_skills.py \
  --skill user-task-orchestrator \
  --skill user-product-discovery \
  --skill user-prd-spec-writing \
  --skill user-react-development \
  --skill user-typescript-development \
  --skill user-dashboard-metrics-definition \
  --skill user-accessibility-audit \
  --skill user-test-driven-development \
  --destination /path/to/host/skills
```

**Speaker script:**

A custom pack should be composed in layers. Start with one coordinator. Add the primary domain owner. Add verification and only the risk or delivery skills triggered by the task. In this example, product discovery and the PRD define the outcome, React and TypeScript own implementation, dashboard metrics protect data meaning, accessibility and testing verify behavior, and the orchestrator maintains the chain. The exporter accepts repeated `--skill` options, deduplicates IDs, verifies each package, and copies the canonical content without rewriting it.

## Slide 5 — The five built-in starter packs

**On-slide table:**

| Pack | Focus |
|---|---|
| `web-app-team` | Frontend, APIs, browser testing, accessibility, security, debugging |
| `solo-indie-hacker` | Product discovery, PRDs, roadmaps, frontend, monetization, spreadsheets |
| `security-review` | Authorized assessment, findings, remediation, and retesting |
| `student-stem` | Tutoring, mathematics, physics, chemistry, units, and exam practice |
| `content-creator` | Technical writing, video, slides, podcast, brand, image, localization |

**Speaker script:**

These five packs are starting points, not universal bundles. A team can combine packs and add individual skills. The exporter supports repeated `--pack` arguments, and its deduplication prevents overlapping skills from being copied twice. The important practice is review: do not load the entire 155-skill catalog when a focused chain will do. Smaller context improves routing, reviewability, and cost control.

## Slide 6 — Cross-agent compatibility is a common denominator

**On-slide message:**

> Canonical content stays stable; discovery, metadata, permissions, and runtime are adapted per host.

**Speaker script:**

Vercel’s public Agent Skills documentation describes skills as modular packages that can be installed across many agents.[1] Claude’s documentation describes filesystem-based skills with progressive disclosure: metadata first, instructions when triggered, and optional resources on demand.[2] Cursor documents project and user skill directories, optional path scoping, explicit invocation, and scripts or references.[3] Agent Skill Kit follows the common denominator: a directory containing `SKILL.md`, with optional resources. Its compatibility guide then documents where an adapter may be needed.

The repository does not promise identical behavior. A host may use a different directory, ignore optional frontmatter, limit network access, require manual activation, or provide different tool permissions. The exporter is a packaging step, not proof of native invocation.

## Slide 7 — State persistence is externalized, not magical

**On-slide diagram:**

```text
Conversation context: temporary working memory
              |
              v
STATE.md + todo.md + decisions + test evidence + Git history
              |
              v
Next session or another host reconstructs the task
```

**Speaker script:**

A skill does not remember a previous conversation. Durable state belongs in explicit artifacts. Manus describes using the filesystem as structured, externalized context and maintaining a task list to keep objectives visible.[4] Claude Code begins sessions with fresh context and uses `CLAUDE.md` files and auto memory as persistent context mechanisms.[5] Its compaction system summarizes long sessions and restores selected context, but compaction is not a replacement for exact decisions, evidence, or credentials stored safely outside the conversation.[6]

The portable protocol is simple: discover the host, read the state record, reconcile it with the repository and Git status, reload the minimum skill chain, reproduce the last unfinished step safely, update the state record, and hand off evidence. This works even when the next session runs on a different agent.

## Slide 8 — What the deepening pass changed

**On-slide metrics:**

- **155 canonical skills preserved**
- **154 previously thin modules enriched**
- **55-line minimum durable structure gate**
- **19 security modules retain authorization and retest checks**
- **0 existing skill directories deleted or renamed**

**Speaker script:**

The catalog was not made stronger by adding random paragraphs. The deepening pass added a consistent operational skeleton while preserving each skill’s original domain content and safety boundaries. Every module now has a quick start, decision points, a worked record, verification, failure handling, portability, and maintenance guidance. Existing detailed modules were preserved, and canonical `user-` IDs remain stable for backward compatibility. The quality gate prevents future additions from returning to one-paragraph summaries.

## Slide 9 — Safety, trust, and responsible composition

**On-slide checklist:**

```text
Scope first
Authorization before impact
Private context stays private
Sources and uncertainty remain visible
Verify before claiming success
Never compose skills to bypass a refusal or control
```

**Speaker script:**

Composition increases capability, so it must also preserve boundaries. Security skills require authorized targets, scope, rate limits, evidence handling, and stop conditions. Science, education, health, legal, and finance modules are informational and do not replace qualified professional judgment. Public skills must not contain credentials, private project facts, copied textbook material, safeguard-bypass recipes, or deceptive instructions. A downstream skill cannot override a narrower safety rule from an upstream skill.

## Slide 10 — Maintainer workflow and next steps

**On-slide command:**

```bash
python scripts/generate_skill_index.py
python scripts/validate_skills.py
python scripts/check_skill_depth.py
python scripts/check_security_quality.py
python scripts/export_skills.py --pack web-app-team --destination /tmp/skill-smoke
python -m py_compile scripts/*.py
git diff --check
```

**Speaker script:**

Maintainers should add or extend one focused module at a time, inspect overlap, use authoritative sources for changing claims, regenerate the index and alias manifest, run the depth and security gates, smoke-test an export, and review the diff for secrets or unrelated changes. Contributors should update the source register and explain compatibility assumptions. The result is a skill powerhouse that can grow without becoming an unreviewable prompt dump.

## Closing message

**On-slide message:**

> Build once as a portable procedure. Load only what the task needs. Persist state in explicit artifacts. Verify every handoff.

**Speaker script:**

The long-term value of Agent Skill Kit is not the number 155. It is the architecture around those skills: modular boundaries, progressive disclosure, safe composition, deterministic export, honest host compatibility, durable state artifacts, and quality gates that keep the catalog usable as it grows.

## References

[1]: https://vercel.com/docs/agent-resources/skills "Vercel Agent Skills documentation"

[2]: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview "Claude Agent Skills overview"

[3]: https://cursor.com/docs/skills "Cursor Agent Skills documentation"

[4]: https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus "Context Engineering for AI Agents: Lessons from Building Manus"

[5]: https://code.claude.com/docs/en/memory "How Claude remembers your project"

[6]: https://code.claude.com/docs/en/context-window "Explore the Claude Code context window"
