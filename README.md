# Agent Skill Kit

**Agent Skill Kit** is a curated, modular, open-source library of reusable `SKILL.md` workflows for AI agents and coding assistants. It helps agents choose the right method for a task, load only relevant guidance, work from evidence, verify changes, and keep security and project boundaries explicit.

The repository is organized as independent skills rather than one oversized instruction file. Each skill has a clear trigger description and focused workflow. Install only the modules that match your agent, project, or domain.

## What is included

The library covers project planning, context engineering, cost and token optimization, software engineering, code quality, debugging, testing, Git, APIs, databases, web and mobile applications, React, TypeScript, JavaScript and Node.js, CSS and Tailwind, UI/UX, responsive design, accessibility, browser testing, visual quality, motion, Three.js, games, Docker, infrastructure, CI/CD, performance, observability, research, scientific research, writing, documents, data, finance, automation, monetization, privacy, identity, threat modeling, vulnerability detection, authorized security testing, AI application security, prompt-injection defense, media provenance, and watermark rights management.

See the generated [skill index](docs/SKILL_INDEX.md) for the complete catalog.

## Installation

Each skill is self-contained. Copy the selected skill directory into the skill directory supported by your agent, or copy its `SKILL.md` into the corresponding project or user-level skills location. Keep the directory name and `SKILL.md` together so the trigger metadata remains available.

Before installing a skill into an automated agent, review its scope, tool assumptions, safety boundaries, and compatibility with the target agent. Do not enable every skill by default when a smaller set will solve the task.

## How skills should be used

A capable agent should classify the request, select the smallest relevant skill set, load project-specific context only when needed, inspect the repository and current sources, execute the workflow, validate the result, and report evidence and uncertainty. Skills are procedural guidance; project facts, user preferences, business rules, and trusted references belong in separate knowledge or project-context files.

## Safety and responsible use

This project supports authorized development, testing, privacy protection, and production readiness. It does not provide instructions for credential theft, unauthorized access, destructive exploitation, persistence, evasion, anti-forensics, watermark removal from third-party media, copyright bypass, invalid advertising traffic, deceptive monetization, prompt-injection bypass, or safeguard circumvention.

Security-testing skills require an explicitly authorized target, defined scope, a safe environment where possible, rate limits, evidence handling, and responsible reporting. Media skills require ownership or permission and preserve originals and provenance where appropriate.

## Quality principles

Skills should be concise, actionable, version-aware, evidence-led, and independently useful. New skills should avoid duplicating an existing module, state assumptions, define verification, protect secrets and personal data, and include rollback or recovery where changes are risky.

## Status

This is a community-maintained collection. Platform documentation, package APIs, security guidance, and policies change over time. Check authoritative documentation before using a skill for a production, financial, privacy, security, or platform-policy decision.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Skill proposals should include a clear trigger, scope, non-goals, workflow, verification steps, safety considerations, and evidence for version-sensitive guidance.

## License

Released under the [MIT License](LICENSE).
