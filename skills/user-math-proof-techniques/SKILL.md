---
name: user-math-proof-techniques
description: Construct, inspect, and explain mathematical proofs using direct proof, contradiction, contrapositive, induction, cases, construction, invariants, and counterexamples. Use for discrete and theoretical reasoning.
---

# Mathematical Proof Techniques

## Quick start

Use this skill when the request matches **Construct, inspect, and explain mathematical proofs using direct proof, contradiction, contrapositive, induction, cases, construction, invariants, and counterexamples. Use for discrete and theoretical reasoning.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


## Purpose and scope

Convert an informal claim into a precise proposition and select a proof strategy that establishes exactly the stated quantifiers and assumptions. Construct, inspect, and explain mathematical proofs using direct proof, contradiction, contrapositive, induction, cases, construction, invariants, and counterexamples. Use for discrete and theoretical reasoning.

## Classification and inputs

Identify the request, audience, source materials, constraints, assumptions, permissions, version or jurisdiction, and required precision before selecting a method. Separate observed facts, user-provided inputs, calculations, model outputs, and interpretations.

## Workflow

1. Rewrite the claim with definitions, domains, quantifiers, hypotheses, conclusion, and notation made explicit.
2. Test small cases and search for counterexamples before committing to a proof; distinguish a conjecture from a theorem.
3. Choose direct proof, contrapositive, contradiction, induction, strong induction, cases, construction, invariant, extremal argument, or counterexample according to the claim’s structure.
4. Write each implication or equality with its justification; in induction, state the base case, inductive hypothesis, and exact step domain.
5. Conclude with the original claim, not a stronger or weaker statement, and note any assumptions used implicitly.

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Classify the problem, state variables and units, select a method that matches the assumptions, and separate exact reasoning, approximations, measurements, and interpretation. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **math-proof-techniques**, use this compact record:

```text
Request: [the concrete task and intended outcome]
Scope and inputs: [files, data, versions, permissions, audience]
Classification: [task type, risk, and relevant branch]
Method: [selected procedure and why alternatives were rejected]
Steps: [ordered actions with intermediate outputs]
Result: [answer or artifact, separated from interpretation]
Checks: [independent verification, edge cases, safety, accessibility, or reproducibility]
Handoff: [files, owners, limitations, and next action]
```

Do not fill this pattern with invented evidence. If the task is underspecified, keep placeholders visible or ask for the missing decision.

## Verification and quality checks

Check quantifier scope, base cases, domain boundaries, reversibility of implications, definitions, hidden division by zero, and whether a counterexample actually satisfies the hypotheses.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If a premise, measurement, or notation is ambiguous, state the ambiguity and solve the defensible cases separately rather than inventing a value or experimental result. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Common errors

Common errors include proving examples instead of a universal claim, assuming the conclusion, reversing implications, using induction with an incomplete base range, and confusing a failed proof attempt with a disproof.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For mathematics and science, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Rules, safety, and non-goals

Do not present an intuition, analogy, numerical pattern, or computer check as a proof. If the claim is false, provide a valid counterexample and say which hypothesis fails. Do not invent sources, data, results, approvals, or completed actions. Use the smallest relevant skill set and hand off to specialized research, security, data, accessibility, or implementation skills when the task crosses boundaries.

## Handoff

Return formal claim, definitions and assumptions, strategy choice, complete proof or counterexample, verification of logical scope, common pitfall avoided, and any open conjecture.
