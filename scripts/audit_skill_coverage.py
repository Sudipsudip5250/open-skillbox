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
    'Data, ML & analytics': ['data-analysis', 'growth-analytics', 'ai-evaluation'],
    'DevOps, cloud & reliability': ['docker', 'infrastructure', 'ci-cd', 'observability', 'performance', 'automation'],
    'Research, science & evidence': ['research', 'scientific'],
    'Business, product & monetization': ['monetization', 'payments', 'finops', 'cost-efficient', 'tool-selection'],
    'Creative, media & 3D': ['threejs', 'media', 'watermark'],
    'Writing & documentation': ['blog', 'humanized', 'documentation', 'document-remediation'],
    'Domain chapters not yet present': ['math', 'physics', 'chemistry', 'biology', 'earth', 'tutoring', 'curriculum', 'lesson', 'electronics', 'networking', 'operating-systems', 'computer-architecture', 'embedded', 'ml-training', 'data-engineering'],
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
    if cat == 'Domain chapters not yet present':
        note = 'No matching chapter-level skills are present in the current baseline.'
    elif names:
        note = ', '.join(f'`{n}`' for n in names[:8]) + (' …' if len(names) > 8 else '')
    else:
        note = 'No matching skills detected.'
    out.append(f'| {cat} | {len(names)} | {note} |')

out += ['', '## Thin or overlapping areas', '', '- The orchestrator is the main routing layer but currently routes only broad categories and does not mention math, science, education, ML, systems, or document-specific routes.', '- `user-software-engineering` is intentionally broad and should gain explicit non-goals and routing handoffs rather than being merged with code review, debugging, simplification, modernization, or testing.', '- `user-research-fact-checking` and `user-scientific-research` overlap in evidence discipline; they should remain separate with a clearer boundary between general factual research and scientific/literature workflows.', '- The generated index currently uses absolute sandbox paths in links, which are broken on GitHub and must be regenerated with repository-relative links.', '- The validator currently checks frontmatter presence and maximum length but not unique names, expected headings, description quality, broken links, or category metadata.', '- The current repository has no chapter-level mathematics, science, technology fundamentals, tutoring, curriculum, citation-management, or technical-diagramming skills.', '', '## Recommended prioritization', '', '| Priority | Focus | Rationale |', '|---|---|---|', '| P0 | Fix index links; expand orchestrator routing; strengthen validator; add math foundations through calculus, linear algebra, probability/statistics, and discrete math; add units and experimental-design skills. | These are explicitly requested, high-reuse, and foundational for later domain modules. |', '| P1 | Add physics, chemistry, biology, earth/environmental science, data engineering, ML evaluation/training, systems fundamentals, tutoring, curriculum planning, citation management, and Mermaid diagramming. | These create the first credible science/technology/education layer without attempting a full encyclopedia. |', '| P2 | Add deeper mathematics, engineering specialties, electronics/IoT, OS and architecture chapters, advanced spreadsheet modeling, product strategy, incident runbooks, legal-document literacy, and personal knowledge-base workflows. | Valuable extensions that should follow the foundational routing and quality gates. |', '', '## Baseline inventory', '']
for name, desc, _ in records:
    out.append(f'- `{name}` — {desc}')

(ROOT / 'docs' / 'CURRENT_COVERAGE_AUDIT.md').write_text('\n'.join(out) + '\n')
print(f'Wrote docs/CURRENT_COVERAGE_AUDIT.md with {len(records)} skills')
