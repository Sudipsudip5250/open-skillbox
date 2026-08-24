---
name: user-dependency-migration
description: Upgrade, replace, deprecate, or migrate libraries, runtimes, frameworks, APIs, schemas, and infrastructure dependencies safely. Use for version bumps, breaking changes, end-of-life packages, lockfile updates, compatibility work, or migration planning.
---

# Dependency and Migration Work

## Workflow

1. Inventory direct and transitive dependencies, versions, runtime constraints, consumers, configuration, generated clients, and deployment environments.
2. Read official release notes, migration guides, changelogs, deprecation notices, security advisories, and compatibility matrices for the exact versions involved.
3. Define the target state, non-goals, behavior compatibility, data migration, rollback or forward-fix plan, and acceptance criteria.
4. Upgrade one dependency or coherent group at a time. Update code and configuration using supported APIs; do not silently preserve deprecated behavior without documenting it.
5. Review the lockfile diff, licenses, transitive graph, bundle/image impact, and supply-chain provenance. Never hand-edit a lockfile.
6. Run focused tests, migration checks, full suite, type/lint checks, build, staging or runtime smoke tests, and rollback rehearsal when risk warrants it.

## Rules

- Do not upgrade everything in one untraceable change merely to save time.
- Do not infer compatibility from semver alone. Verify changelogs and actual behavior.
- Preserve backups and compatibility windows before destructive data or API migrations.
- If the dependency is unmaintained or risky, compare replacement, containment, or removal rather than assuming the newest alternative is best.

## Handoff

Report current and target versions, sources, breaking changes, files and lockfile changes, tests, migration and rollback plan, security/license findings, and remaining compatibility risk.
