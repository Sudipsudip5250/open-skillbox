from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / 'skills'


def metadata(text: str, directory: str) -> tuple[str, str]:
    name = re.search(r'^name:\s*(.+)$', text, re.MULTILINE)
    desc = re.search(r'^description:\s*(.+)$', text, re.MULTILINE)
    return (name.group(1).strip() if name else directory, desc.group(1).strip() if desc else '')


def family(name: str) -> str:
    key = name.lower()
    if any(t in key for t in ('security', 'vulnerability', 'threat', 'identity', 'privacy', 'secret', 'provenance', 'authorized', 'attack-surface', 'access-control', 'prompt-injection', 'agent-tool-permission')):
        return 'security and trust'
    if any(t in key for t in ('software', 'code', 'debug', 'test', 'typescript', 'javascript', 'react', 'frontend', 'api-', 'git-', 'dependency', 'docker', 'browser', 'web-', 'mobile', 'threejs', 'system', 'architecture', 'network', 'operating', 'embedded', 'electronics')):
        return 'software and systems'
    if any(t in key for t in ('data', 'sql', 'dashboard', 'analytics', 'machine', 'ml-', 'model', 'spreadsheet', 'finance', 'experiment', 'statistic')):
        return 'data and quantitative work'
    if any(t in key for t in ('math', 'algebra', 'calculus', 'probability', 'discrete', 'trigonometry', 'numerical', 'proof', 'physics', 'chemistry', 'biology', 'earth', 'science', 'units')):
        return 'mathematics and science'
    if any(t in key for t in ('tutor', 'curriculum', 'lesson', 'exam', 'concept-map', 'health-information')):
        return 'education and literacy'
    if any(t in key for t in ('product', 'prd', 'roadmap', 'support', 'capacity', 'slo', 'incident', 'backup', 'feature-flag', 'meeting', 'stakeholder')):
        return 'product and operations'
    if any(t in key for t in ('blog', 'writing', 'documentation', 'rfc', 'changelog', 'localization', 'video', 'slide', 'podcast', 'brand', 'image', 'presentation', 'humanized')):
        return 'writing and creative production'
    if any(t in key for t in ('skill-', 'agent-', 'context', 'knowledge', 'orchestrator', 'prompt', 'evaluation', 'tool-selection')):
        return 'agent workflow and governance'
    return 'general professional workflow'


FAMILY_GUIDANCE = {
    'security and trust': {
        'decision': 'Confirm ownership or written authorization, target scope, environment, evidence handling, rate limits, and stop conditions before active access or testing.',
        'checks': 'redact secrets and personal data; preserve evidence integrity; distinguish observation from inference; verify fixes with a bounded retest; and escalate when scope or authority is unclear.',
        'failure': 'If authorization, scope, or safe evidence handling is missing, pause and provide a planning-only alternative rather than probing, bypassing, or guessing.',
    },
    'software and systems': {
        'decision': 'Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path.',
        'checks': 'run the narrowest relevant tests, type/build checks, runtime reproduction, compatibility checks, rollback review, and an inspection of the final diff for unintended behavior.',
        'failure': 'If the failure is not reproducible, capture environment and logs, reduce the case, state uncertainty, and avoid speculative rewrites or destructive recovery steps.',
    },
    'data and quantitative work': {
        'decision': 'Declare unit of analysis, grain, schema, population, time window, denominator, provenance, missingness, and the decision the result must support before calculating.',
        'checks': 'reconcile totals, inspect nulls and duplicates, test boundary dates and exclusions, compare with an alternate calculation or baseline, and report uncertainty and data freshness.',
        'failure': 'If data is incomplete or definitions conflict, preserve the ambiguity, show the affected result, and request a source-of-truth decision instead of silently coercing values.',
    },
    'mathematics and science': {
        'decision': 'Classify the problem, state variables and units, select a method that matches the assumptions, and separate exact reasoning, approximations, measurements, and interpretation.',
        'checks': 'check units, signs, dimensions, limiting cases, edge cases, order of magnitude, reproducibility, and whether the conclusion exceeds the evidence or educational scope.',
        'failure': 'If a premise, measurement, or notation is ambiguous, state the ambiguity and solve the defensible cases separately rather than inventing a value or experimental result.',
    },
    'education and literacy': {
        'decision': 'Identify learner or reader level, objective, prerequisite knowledge, source quality, accessibility needs, and whether the task is explanation, practice, assessment, or decision support.',
        'checks': 'test understanding with retrieval or transfer, use an unseen variation, check source quality and uncertainty, and ensure the response teaches reasoning rather than supplying an answer-only shortcut.',
        'failure': 'If the learner is stuck, diagnose the misconception and add a smaller hint or prerequisite explanation; do not shame the learner or imply professional certainty in regulated topics.',
    },
    'product and operations': {
        'decision': 'State the user or service outcome, decision owner, evidence, time horizon, capacity, dependencies, risk, and explicit non-goals before recommending a plan.',
        'checks': 'verify ownership, feasibility, observability, rollback or recovery, stakeholder agreement, and whether success is defined by outcomes rather than activity or vanity metrics.',
        'failure': 'If evidence or ownership is missing, mark the item as a hypothesis, decision needed, or escalation rather than presenting a speculative commitment as a plan.',
    },
    'writing and creative production': {
        'decision': 'Define audience, purpose, format, voice, source material, version or jurisdiction, accessibility, asset rights, review owner, and the claims the deliverable is allowed to make.',
        'checks': 'review factual claims and citations, structure, readability, accessibility, timing or rendering, rights and attribution, placeholders, and whether the final wording overstates certainty.',
        'failure': 'If the source is incomplete or an asset is not clearly permitted, mark the gap and use a placeholder or original alternative instead of inventing, copying, or removing rights information.',
    },
    'agent workflow and governance': {
        'decision': 'Define the agent host, available tools, instruction precedence, context budget, data boundary, approval gates, expected output, and the smallest skill chain that can complete the task.',
        'checks': 'run a representative prompt, inspect tool traces and handoffs, test refusal and uncertainty behavior, verify no private context leaks, and compare against a fixed baseline when evaluating changes.',
        'failure': 'If a host cannot load the canonical format or a tool is unavailable, preserve the source skill and document a reversible adapter or manual fallback rather than claiming compatibility.',
    },
    'general professional workflow': {
        'decision': 'Define the request, audience, inputs, constraints, authority, expected precision, and decision or artifact that the work must support before selecting a method.',
        'checks': 'verify assumptions, important claims, edge cases, usability, safety, reproducibility, and whether the handoff contains enough information for another person or agent to continue.',
        'failure': 'If information is missing or conflicting, state the uncertainty, ask only blocking questions, and avoid fabricating evidence, permissions, results, or completed actions.',
    },
}


def insert_before(text: str, marker: str, block: str) -> str:
    if marker in text:
        return text.replace(marker, block + marker, 1)
    for fallback in ('## Rules, safety, and non-goals\n', '## Safety and non-goals\n', '## Handoff\n'):
        if fallback in text:
            return text.replace(fallback, block + fallback, 1)
    return text.rstrip() + '\n\n' + block


def deepen(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')
    required = ('## Quick start', '## Inputs and decision points', '## Worked pattern', '## Verification and quality checks', '## Failure handling', '## Portability and maintenance')
    if len(text.splitlines()) >= 90 and all(section in text for section in required):
        return False
    name, desc = metadata(text, path.parent.name)
    if '## Quick start' not in text:
        quick = f'''## Quick start\n\nUse this skill when the request matches **{desc or name}**. Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.\n\n'''
        heading = re.search(r'^# .+$\n', text, re.MULTILINE)
        if heading:
            text = text[:heading.end()] + '\n' + quick + text[heading.end():]
        else:
            text = quick + text
    group = family(name)
    guide = FAMILY_GUIDANCE[group]
    if '## Inputs and decision points' not in text:
        block = f'''## Inputs and decision points\n\n| Stage | Required record | Decision or escalation |\n|---|---|---|\n| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |\n| Select | Applicable method, alternatives considered, and why the selected path fits | {guide['decision']} |\n| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |\n| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |\n\n'''
        text = insert_before(text, '## Verification and quality checks\n', block)
    if '## Worked pattern' not in text:
        block = f'''## Worked pattern\n\nFor a request involving **{name.removeprefix('user-')}**, use this compact record:\n\n```text\nRequest: [the concrete task and intended outcome]\nScope and inputs: [files, data, versions, permissions, audience]\nClassification: [task type, risk, and relevant branch]\nMethod: [selected procedure and why alternatives were rejected]\nSteps: [ordered actions with intermediate outputs]\nResult: [answer or artifact, separated from interpretation]\nChecks: [independent verification, edge cases, safety, accessibility, or reproducibility]\nHandoff: [files, owners, limitations, and next action]\n```\n\nDo not fill this pattern with invented evidence. If the task is underspecified, keep placeholders visible or ask for the missing decision.\n\n'''
        text = insert_before(text, '## Verification and quality checks\n', block)
    if '## Verification and quality checks' not in text:
        block = f'''## Verification and quality checks\n\n{guide['checks']} Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.\n\n'''
        text = insert_before(text, '## Common errors\n', block)
    if '## Failure handling' not in text:
        block = f'''## Failure handling\n\nWhen the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. {guide['failure']} If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.\n\n'''
        text = insert_before(text, '## Common errors\n', block)
    if '## Portability and maintenance' not in text:
        block = f'''## Portability and maintenance\n\nKeep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For {group}, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.\n\n'''
        text = insert_before(text, '## Safety and non-goals\n', block)
    path.write_text(text.rstrip() + '\n', encoding='utf-8')
    return True


def main() -> None:
    changed = 0
    for path in sorted(SKILLS.glob('*/SKILL.md')):
        changed += deepen(path)
    print(f'Deepened {changed} skills; left already-detailed skills unchanged.')


if __name__ == '__main__':
    main()
