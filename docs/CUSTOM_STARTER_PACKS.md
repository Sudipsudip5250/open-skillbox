# Custom Multi-Domain Starter Packs

A starter pack is a small, repeatable set of canonical skills selected for one type of work. The repository’s built-in packs are named presets, but you can create a custom pack without changing the catalog: select individual canonical IDs with repeated `--skill` arguments, save the selection in your project documentation or script, and export it to the host-specific skill directory.

## Selection method

Build the pack in layers:

| Layer | Purpose | Example |
|---|---|---|
| Coordinator | Classify the task and keep the chain minimal | `user-task-orchestrator` |
| Primary domain | Own the main work | `user-react-development` |
| Verification | Test correctness or quality | `user-test-driven-development`, `user-browser-testing` |
| Risk or constraint | Add only when triggered | `user-accessibility-audit`, `user-security-risk-review` |
| Delivery | Package the result or communicate the handoff | `user-documentation-communication` |

Avoid loading two skills that own the same decision unless one is explicitly a verifier or handoff stage. A custom pack should explain why each skill is present and what it receives from the previous stage.

## Example: accessible data-backed web feature

Suppose a team is building a React dashboard that reads an API, defines business metrics, and must be released safely. A focused cross-domain pack could be:

```text
user-task-orchestrator
user-product-discovery
user-prd-spec-writing
user-api-interface-design
user-react-development
user-typescript-development
user-sql-analytics-workflows
user-dashboard-metrics-definition
user-accessibility-audit
user-test-driven-development
user-browser-testing
user-security-risk-review
user-changelog-release-notes
```

The composition is intentional. Product discovery and the PRD define the outcome; API, React, and TypeScript own implementation; SQL and metrics define trustworthy data; accessibility and testing verify the experience; security is included because the feature crosses data boundaries; release notes provide the final handoff. Do not load every skill for every request: a small bug fix might need only the coordinator, React, TypeScript, and testing skills.

## Export with the current repository tool

The exporter accepts repeated `--skill` options and writes either directory packages or flattened Markdown files:

```bash
python scripts/export_skills.py \
  --skill user-task-orchestrator \
  --skill user-product-discovery \
  --skill user-prd-spec-writing \
  --skill user-api-interface-design \
  --skill user-react-development \
  --skill user-typescript-development \
  --skill user-sql-analytics-workflows \
  --skill user-dashboard-metrics-definition \
  --skill user-accessibility-audit \
  --skill user-test-driven-development \
  --skill user-browser-testing \
  --skill user-security-risk-review \
  --skill user-changelog-release-notes \
  --destination /path/to/host/skills
```

The exporter deduplicates repeated IDs, verifies that every selected directory contains `SKILL.md`, and copies the canonical package without rewriting its content. Use an explicit destination chosen for the target host. The exporter does not activate skills, change permissions, install dependencies, or upload data.

For a host that only accepts individual Markdown files:

```bash
python scripts/export_skills.py \
  --skill user-task-orchestrator \
  --skill user-react-development \
  --skill user-accessibility-audit \
  --destination /path/to/host/rules \
  --flatten
```

## Combine built-in packs

The same interface can combine named presets and individual additions:

```bash
python scripts/export_skills.py \
  --pack web-app-team \
  --pack security-review \
  --skill user-dashboard-metrics-definition \
  --skill user-prd-spec-writing \
  --destination /path/to/host/skills
```

Because packs can overlap, the exporter’s deduplication prevents duplicate copies. Review the resulting list before installation so the host receives only the context that is relevant to the project.

## Make a custom pack reproducible

Keep the selection in a version-controlled shell script or project document, for example:

```bash
#!/usr/bin/env bash
set -euo pipefail

DESTINATION="${1:?provide the host skill destination}"
python scripts/export_skills.py \
  --skill user-task-orchestrator \
  --skill user-product-discovery \
  --skill user-prd-spec-writing \
  --skill user-react-development \
  --skill user-typescript-development \
  --skill user-test-driven-development \
  --skill user-browser-testing \
  --destination "$DESTINATION"
```

Pin the repository revision in the surrounding project or lockfile when reproducibility matters. After changing the selection, run the exporter in a temporary directory and inspect the copied tree before replacing an active host directory.

## Cross-agent mapping

The content remains canonical, but installation paths differ. Manus can use the repository’s explicit export destination and project context. Claude Code commonly discovers project skills under `.claude/skills/` and project instructions through `CLAUDE.md`; Cursor supports `.agents/skills/` and `.cursor/skills/` as well as compatible Claude and Codex locations. Other hosts may use `.agents/`, an application-specific folder, a plugin package, or a manual prompt attachment. Confirm the current host documentation before copying.

If the host supports native Agent Skills discovery, export directory mode. If it only supports rules or prompt files, use `--flatten` and inspect whether the host accepts YAML frontmatter. If it has no filesystem skill support, load the relevant `SKILL.md` content manually or use the host’s documented import mechanism. Never claim that an export alone proves the host will automatically invoke a skill.

## Review checklist

Before using a custom pack, confirm that it has one coordinator, one primary domain owner, no accidental duplicates, explicit verification coverage, no unnecessary high-risk capabilities, and a clear handoff. Check that each selected skill is from a trusted revision, contains no secrets or private project facts, and is compatible with the host’s runtime and permissions.
