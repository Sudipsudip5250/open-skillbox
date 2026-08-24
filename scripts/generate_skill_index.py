from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / 'skills'
OUT = ROOT / 'docs' / 'SKILL_INDEX.md'

CATEGORIES = [
    ('Meta and orchestration', ['orchestrator', 'context', 'knowledge', 'project-delivery', 'brainstorming', 'skill-authoring', 'skill-quality', 'cost-efficient', 'tool-selection', 'source-driven']),
    ('Software engineering and quality', ['software-engineering', 'code-review', 'code-simplification', 'codebase-modernization', 'debugging', 'testing', 'test-driven', 'dependency-migration', 'git-workflow', 'api-interface']),
    ('Frontend, design, accessibility, and media', ['frontend', 'react', 'typescript', 'javascript-node', 'ui-ux', 'responsive', 'accessibility', 'browser-testing', 'visual', 'motion', 'threejs', 'media', 'watermark', 'mobile-app']),
    ('Security, privacy, identity, and trust', ['security', 'privacy', 'identity', 'threat', 'vulnerability', 'authorized-security', 'prompt-injection', 'secrets', 'database-security', 'provenance']),
    ('Data, machine learning, analytics, and finance', ['data-analysis', 'data-engineering', 'ml-', 'ai-evaluation', 'growth-analytics', 'finance', 'finops', 'token-cost']),
    ('DevOps, cloud, reliability, and automation', ['docker', 'infrastructure', 'ci-cd', 'observability', 'performance', 'automation']),
    ('Technology foundations and systems', ['systems-design', 'computer-architecture', 'networking', 'operating-systems', 'embedded', 'electronics', 'technical-diagramming']),
    ('Research, science, and evidence', ['research', 'scientific', 'physics', 'chemistry', 'biology', 'earth', 'experimental', 'units', 'visualization-plotting', 'literature-review', 'citation']),
    ('Mathematics', ['math-', 'algebra', 'functions', 'polynomials', 'exponents', 'trigonometry', 'precalculus', 'limits', 'calculus', 'linear-algebra', 'probability', 'statistics', 'discrete', 'numerical', 'proof', 'word-problems', 'symbolic']),
    ('Education and tutoring', ['tutoring', 'curriculum', 'lesson', 'exam-prep']),
    ('Business, product, monetization, and communication', ['monetization', 'payments', 'product', 'writing', 'blog', 'documentation', 'document', 'citation', 'spreadsheet']),
]

def metadata(path):
    text = path.read_text(encoding='utf-8')
    name = re.search(r'^name:\s*(.+)$', text, re.M)
    desc = re.search(r'^description:\s*(.+)$', text, re.M)
    return (name.group(1).strip() if name else path.parent.name, desc.group(1).strip() if desc else '')

records = [metadata(p) + (p.parent.name,) for p in sorted(SKILLS.glob('*/SKILL.md'))]
assigned = set()
lines = ['# Skill Index', '', 'A grouped catalog of the modular skills in Agent Skill Kit. Each skill is independently installable. Load the smallest relevant set rather than the entire catalog.', '', f'**Current catalog:** {len(records)} skills.', '']
for category, terms in CATEGORIES:
    rows = []
    for name, desc, directory in records:
        hay = f'{name} {directory}'.lower()
        if any(term in hay for term in terms):
            rows.append((name, desc, directory))
            assigned.add(directory)
    if not rows:
        continue
    lines += [f'## {category}', '', '| Skill | Trigger-oriented description |', '|---|---|']
    for name, desc, directory in rows:
        lines.append(f'| [`{name}`](../skills/{directory}/SKILL.md) | {desc} |')
    lines.append('')

uncategorized = [(name, desc, directory) for name, desc, directory in records if directory not in assigned]
if uncategorized:
    lines += ['## Other or newly added skills', '', '| Skill | Trigger-oriented description |', '|---|---|']
    for name, desc, directory in uncategorized:
        lines.append(f'| [`{name}`](../skills/{directory}/SKILL.md) | {desc} |')
    lines.append('')

OUT.write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')
print(f'Generated {OUT} with {len(records)} skills')
