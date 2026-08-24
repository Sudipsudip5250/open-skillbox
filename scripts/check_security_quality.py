from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'skills'
MARKERS = (
    'security', 'vulnerability', 'threat', 'identity', 'secrets', 'prompt-injection',
    'attack-surface', 'access-control', 'api-security', 'remediation-verification',
    'agent-tool-permission', 'rules-of-engagement',
)

records = []
for path in sorted(ROOT.glob('user-*/SKILL.md')):
    name = path.parent.name
    if not any(marker in name for marker in MARKERS):
        continue
    text = path.read_text(encoding='utf-8')
    lower = text.lower()
    records.append((
        name,
        'authorized' in lower or 'owns' in lower,
        '## Handoff' in text,
        '## Safety' in text or '## Rules' in text,
        'remediat' in lower,
    ))

if len(records) != 19:
    raise SystemExit(f'Expected 19 security skills, found {len(records)}: {records}')
failures = [row for row in records if not all(row[1:])]
if failures:
    raise SystemExit(f'Security quality checks failed: {failures}')
print(f'Checked {len(records)} security skills for authorization, safety/rules, remediation, and handoff coverage.')
