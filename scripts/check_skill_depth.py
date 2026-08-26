from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    '## Quick start',
    '## Inputs and decision points',
    '## Worked pattern',
    '## Verification and quality checks',
    '## Failure handling',
    '## Portability and maintenance',
)
MIN_LINES = 55
errors: list[str] = []
count = 0
for path in sorted((ROOT / 'skills').glob('*/SKILL.md')):
    count += 1
    text = path.read_text(encoding='utf-8')
    lines = len(text.splitlines())
    if lines < MIN_LINES:
        errors.append(f'{path}: {lines} lines; expected at least {MIN_LINES}')
    for heading in REQUIRED:
        if heading not in text:
            errors.append(f'{path}: missing {heading}')

if errors:
    print('\n'.join(errors))
    raise SystemExit(f'{len(errors)} skill-depth errors across {count} skills')
print(f'Checked durable depth structure for {count} skills (minimum {MIN_LINES} lines).')
