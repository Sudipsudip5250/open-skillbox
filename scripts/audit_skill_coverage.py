from pathlib import Path
import re
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / 'skills'
CATEGORY_RULES = {
    'Meta & orchestration': ['orchestrator', 'context', 'knowledge', 'project-delivery', 'brainstorming'],
    'Software engineering & quality': ['software-engineering', 'code-review', 'code-simplification', 'codebase-modernization', 'debugging', 'test-driven', 'systematic-debugging', 'dependency-migration', 'git-workflow'],
    'Frontend, design & accessibility': ['frontend', 'react', 'typescript', 'javascript-node', 'ui-ux', 'responsive', 'accessibility', 'visual-quality', 'motion', 'browser-testing'],
    'Security, privacy & identity': ['security', 'privacy', 'identity', 'threat', 'vulnerability', 'authorized-security', 'prompt-injection', 'secrets', 'database-security'],
    'Data, ML & analytics': ['data-analysis', 'data-engineering', 'growth-analytics', 'ai-evaluation', 'ml-training'],
    'DevOps, cloud & reliability': ['docker', 'infrastructure', 'ci-cd', 'observability', 'performance', 'automation', 'incident-response', 'runbooks'],
    'Research, science & evidence': ['research', 'scientific', 'physics', 'chemistry', 'biology', 'earth', 'experimental', 'literature-review', 'citation', 'visualization'],
    'Business, product & monetization': ['monetization', 'payments', 'finops', 'cost-efficient', 'tool-selection', 'product-discovery', 'spreadsheet', 'legal-document'],
    'Creative, media & 3D': ['threejs', 'media', 'watermark'],
    'Writing & documentation': ['blog', 'humanized', 'documentation', 'document-remediation', 'citation', 'technical-diagramming', 'legal-document'],
    'Specialized domain coverage': ['math', 'physics', 'chemistry', 'biology', 'earth', 'tutoring', 'curriculum', 'lesson', 'exam-prep', 'electronics', 'networking', 'operating-systems', 'computer-architecture', 'embedded', 'ml-training', 'data-engineering', 'differential-equations', 'numerical', 'proof', 'symbolic', 'spreadsheet', 'product-discovery', 'incident-response', 'legal-document'],
}

records = []
for path in sorted(SKILLS.glob('*/SKILL.md')):
    text = path.read_text()
    name = re.search(r'^name:\s*(.+)$', text, re.M)
    desc = re.search(r'^description:\s*(.+)$', text, re.M)
    records.append((name.group(1).strip() if name else path.parent.name, desc.group(1).strip() if desc else '', path))

categories = defaultdict(list)
for name, desc, path in records:
    hay = f'{name} {desc}'.lower()
    matched = [cat for cat, terms in CATEGORY_RULES.items() if any(term in hay for term in terms)]
    if not matched:
        matched = ['Uncategorized / review']
    for cat in matched:
        categories[cat].append(name)

out = ['# Current Skill Coverage Audit', '', f'Baseline: **{len(records)} skills** found under `skills/*/SKILL.md`.', '', '## Coverage by category', '', '| Category | Count | Notes |', '|---|---:|---|']
for cat in CATEGORY_RULES:
    names = categories.get(cat, [])
    if cat == 'Specialized domain coverage':
        note = 'Heuristic inventory of chapter-level and specialized domain skills; overlaps are expected.'
    elif names:
        note = ', '.join(f'`{n}`' for n in names[:8]) + (' …' if len(names) > 8 else '')
    else:
        note = 'No matching skills detected.'
    out.append(f'| {cat} | {len(names)} | {note} |')

out += ['', '## Thin or overlapping areas', '', '- Category counts are heuristic and may overlap because one skill can serve several domains; use `docs/SKILL_INDEX.md` for exact discovery.', '- `user-software-engineering` remains the general implementation owner while focused review, debugging, testing, migration, security, and framework skills remain separate.', '- `user-research-fact-checking` and `user-scientific-research` remain distinct: general factual verification versus scientific evidence, reproducibility, and research reporting.', '- The orchestrator and validator now cover the expanded mathematics, science, education, systems, product, legal-literacy, incident-response, and security assessment routes.', '', '## Current prioritization', '', '| Priority | Focus | Status |', '|---|---|---|', '| Complete | Foundational mathematics, science, technology, education, research-depth, and authorized-security expansion | Published and validated |', '| Maintain | Keep triggers narrow, sources current, handoffs explicit, and public/private context separated | Ongoing |', '| Future | Add deeper domain modules only when usage demonstrates a distinct gap | Evidence-led backlog |', '', '## Skill inventory', '']
for name, desc, _ in records:
    out.append(f'- `{name}` — {desc}')

(ROOT / 'docs' / 'CURRENT_COVERAGE_AUDIT.md').write_text('\n'.join(out) + '\n')
print(f'Wrote docs/CURRENT_COVERAGE_AUDIT.md with {len(records)} skills')
