# State Persistence and Context Recovery Across Agent Hosts

## The short answer

A skill is a **procedure**, not a database and not a guarantee that an agent will remember a prior conversation. Agent Skill Kit keeps reusable instructions in canonical `SKILL.md` packages. Durable task state should be written to explicit project artifacts such as `todo.md`, `STATE.md`, decision records, test reports, source manifests, or Git commits.

The same skill can therefore work across Manus, Claude Code, Codex, Cursor, Replit, Kiro, Kilo, Antigravity, OpenCode, Mimo Code, and other hosts, but the host determines how instructions are discovered, how much context is loaded, what memory features exist, and which tools can execute the procedure.

## What persists and what does not

| Layer | Typical persistence | Portable recommendation |
|---|---|---|
| Canonical skill | Repository files under `skills/<id>/SKILL.md`, plus optional resources | Version-control the skill package and load it on demand. |
| Project instructions | Host files such as `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`, or equivalent | Keep shared, stable rules short; point to the canonical catalog instead of duplicating every skill. |
| Task state | Files, Git history, generated artifacts, test output, decision logs, and source registers | Write a small structured state file at milestones and include paths, status, assumptions, evidence, and next action. |
| Conversation context | Current session history and host-specific compaction summaries | Treat it as temporary working memory. Never rely on it as the only copy of a decision or result. |
| Private memory | Host-specific user or project memory, if enabled | Keep private preferences and confidential facts outside public skills; record only approved, public-safe summaries. |
| Tool state | Credentials, browser sessions, MCP connections, databases, deployment environments | Do not encode secrets in skills. Re-check access and authorization after a session change. |

## Manus pattern

Manus describes the filesystem as externalized context: the agent can write and read files on demand, preserve a restorable reference such as a file path or URL, and maintain a task list to keep objectives in recent attention.[1] This is a useful design pattern, not a promise that every Manus task automatically persists every conversation detail.

For a long Manus task, maintain a small state record such as:

```markdown
# STATE.md

## Objective
[One sentence describing the approved outcome]

## Scope and constraints
[Repository, files, environment, permissions, stop conditions]

## Completed
- [Milestone] — [artifact or commit]

## Decisions
- [Decision] — [reason and evidence]

## Open risks
- [Risk] — [owner or next verification]

## Next action
[One concrete next step]

## Evidence
- [Path, URL, command, or test result]
```

Update the record after inspection, each major implementation checkpoint, and verification. Keep raw logs and large source material in files; place only concise references and conclusions in the state record. A future Manus session can re-read the state file and the referenced artifacts instead of depending on a long chat transcript.

## Claude Code pattern

Claude Code starts each session with a fresh context window. Its documented persistent mechanisms are project or user `CLAUDE.md` files and auto memory; both are loaded as context, not as an unoverrideable enforcement mechanism.[2] `CLAUDE.md` is appropriate for stable project instructions, commands, architecture facts, and rules that teammates should share. Auto memory is intended for learnings and patterns; Claude Code documents a per-repository memory scope and a startup load limit of the first 200 lines or 25 KB.[2]

Claude Code also supports path-scoped rules and skills. Skills load when relevant rather than forcing the complete procedure into every session. Its context-window documentation explains that compaction summarizes a long conversation, restores important project instructions and recent working context, and can re-inject skills that were invoked in the session.[3] Compaction is therefore a recovery aid, not a replacement for explicit state artifacts.

Use this layout for a shared project:

```text
project/
├── AGENTS.md                 # Host-neutral project pointer
├── CLAUDE.md                 # Claude Code project instructions or import
├── .claude/rules/            # Optional path-scoped rules
├── .claude/skills/           # Optional local exports
├── STATE.md                  # Human- and agent-readable task state
├── docs/decisions/           # Durable decision records
└── skills/                   # Canonical or exported skill packages
```

Keep `CLAUDE.local.md` or equivalent personal files out of version control when they contain private preferences, local paths, or secrets. Use hooks, permission settings, or CI for hard enforcement; do not assume a Markdown instruction alone can block an unsafe action.[2]

## Cross-agent recovery protocol

1. **Discover.** Confirm the current repository, branch, host, skill path, available tools, and active instruction files.
2. **Read the state record.** Load `STATE.md`, the latest decision record, and the most recent verification output before reading the full conversation history.
3. **Reconcile.** Compare the state record with `git status`, the latest commit, generated artifacts, and the actual files. Mark discrepancies as unresolved rather than guessing.
4. **Reload minimally.** Load the orchestrator, the domain skill, and only the verification or delivery skills required by the next action.
5. **Recover safely.** Reproduce the last unfinished step in a bounded environment. Do not repeat an external or destructive action merely because the old context is missing.
6. **Continue and record.** Update the state record with the result, evidence, assumptions, and next action before moving to another milestone.
7. **Handoff.** Return changed paths, commands, tests, decisions, limitations, and whether deployment or other external action was performed.

## Failure cases and mitigations

| Failure | Why it happens | Recovery |
|---|---|---|
| A new session forgets a decision | Conversation history is not durable project state | Reconstruct from `STATE.md`, commits, decision records, and cited evidence. |
| Compaction loses a subtle detail | Summaries discard raw tool output and low-salience context | Preserve exact paths, identifiers, constraints, and unresolved questions in files before compaction. |
| A skill is not discovered | Host-specific skill directories or frontmatter differ | Use the exporter, verify the host’s current discovery path, and keep a manual invocation fallback. |
| Private context leaks into public work | Memory and repository files have different audiences | Separate public skill content from private Knowledge and local instruction files; run a secret scan. |
| Recovery repeats a risky action | The prior approval or stop condition is absent from the current context | Require an explicit authorization record and re-confirm scope before external, destructive, or high-impact actions. |
| State becomes stale | The agent writes notes but does not reconcile them with files | Include a timestamp or commit, run `git status`, and mark stale claims as unverified. |

## Design rule for skill authors

Write skills so that their outputs are recoverable: name the expected artifact, include a compact handoff schema, preserve uncertainty, and point to the next verification step. Do not claim that a skill remembers a user, a project, a browser session, a credential, or a previous conversation. The host may provide memory; the skill should provide a reliable procedure for reading and updating explicit state.

## References

[1]: https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus "Context Engineering for AI Agents: Lessons from Building Manus"

[2]: https://code.claude.com/docs/en/memory "How Claude remembers your project"

[3]: https://code.claude.com/docs/en/context-window "Explore the Claude Code context window"
