# Manus Example Workflow: Repair an Accessible React Form

This example shows how to compose a small, portable subset of Agent Skill Kit for a realistic repository task. It is intentionally bounded: no deployment, external service changes, or private data export.

## Scenario

The user asks:

> In this repository, fix the profile form so keyboard users can submit it reliably, validation errors are announced, and the loading state cannot submit twice. Preserve the existing API contract. Add or update tests, run the project checks, and summarize the evidence. Do not deploy.

## Selected skills

| Order | Skill | Why it is loaded |
|---|---|---|
| 1 | `user-task-orchestrator` | Classifies scope, constraints, acceptance criteria, and handoffs. |
| 2 | `user-react-development` | Owns component state, event handling, and composition. |
| 3 | `user-typescript-development` | Checks type contracts and compiler behavior. |
| 4 | `user-accessibility-audit` | Covers keyboard paths, semantics, labels, focus, and announcements. |
| 5 | `user-test-driven-development` | Drives regression coverage and red-green-refactor verification. |
| 6 | `user-browser-testing` | Verifies the actual form flow in a browser when the repository supports it. |

Do not load unrelated math, finance, media, security-assessment, or deployment modules. Add a security or privacy module only if the change touches sensitive data, authentication, authorization, or an external system.

## Workflow

### 1. Intake and inspection

The orchestrator records:

| Field | Example decision |
|---|---|
| Outcome | Accessible, single-submit profile form with preserved API contract |
| Scope | Existing form component, validation logic, tests, and relevant styles |
| Constraints | No API changes, no deployment, preserve existing visual language |
| Acceptance | Keyboard submission works; errors are announced; duplicate submits are blocked; tests pass |
| Evidence | Current component, types, tests, browser behavior, project commands |
| Stop conditions | Missing authorization for external changes, unclear API contract, or unsafe private data exposure |

Inspect the component, form library, request client, types, tests, package scripts, and existing accessibility patterns before editing. Avoid assuming that a visually hidden error is announced or that a disabled button alone prevents duplicate requests.

### 2. Write behavior-first tests

Add or update tests for:

1. A keyboard user reaching every field and the submit control in a logical order.
2. An invalid submission producing an associated, screen-reader-visible error and a predictable focus target.
3. A valid submission calling the existing API shape exactly once.
4. A second submit during the pending state being ignored or rejected safely.
5. A server error returning the form to an actionable state without losing the user’s input.
6. A successful response clearing or confirming state according to the existing product behavior.

Record the expected behavior before implementation. If the test environment cannot verify assistive-technology announcements directly, use semantic and accessibility-tree checks plus a manual review note instead of claiming full screen-reader verification.

### 3. Implement the smallest fix

Preserve the component’s public props and API request shape. Prefer a single source of truth for submission state, explicit validation state, and an accessible status or error region. Ensure the submit handler cannot start a second request while the first is pending, and ensure error recovery resets only the state that should change.

Avoid unrelated refactors. If the existing form library has version-specific behavior, inspect its installed documentation or source and record the version in the handoff rather than relying on memory.

### 4. Verify

Run the repository’s documented formatter, type check, unit tests, and browser test command. Inspect the rendered form at keyboard-only, narrow-width, zoomed, and reduced-motion settings when relevant. Confirm that:

- labels and instructions are associated with controls;
- focus is visible and not trapped incorrectly;
- errors are specific and announced through supported semantics;
- loading and failure states are distinguishable;
- no request is duplicated;
- the existing API contract and privacy boundary remain unchanged;
- the diff contains no secrets, generated artifacts, or unrelated rewrites.

Separate verified results from manual checks and unavailable checks.

### 5. Handoff

Return:

```text
Outcome: [one sentence]
Files changed: [paths and purpose]
Skills used: [selected canonical IDs]
Tests/checks: [exact commands and results]
Accessibility evidence: [automated and manual checks]
API compatibility: [what was preserved and how checked]
Assumptions: [versions, unavailable environments, or inferred behavior]
Remaining risks: [known limitations]
Deployment: not performed
Next action: [review, merge, or follow-up]
```

This same workflow can be exported for another host. Keep the canonical skill IDs and instructions unchanged; only adapt the host-specific discovery or permission step documented in [CROSS_AGENT_COMPATIBILITY.md](CROSS_AGENT_COMPATIBILITY.md).
