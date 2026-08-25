from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
errors = []
records = []

workflow_terms = ("workflow", "process", "method", "review", "diagnostic", "execution", "intake", "scope", "plan", "design", "engineering", "retrieval", "analytical", "editorial", "integration", "delivery", "test", "sequence", "layered")
rules_terms = ("rule", "quality", "safety", "handling", "guardrail", "reliability", "change", "integrity", "source", "constraint", "decision", "boundary", "check", "finding", "technical")
handoff_terms = ("handoff", "deliverable", "verdict", "failure", "finding", "output", "report", "record", "completion", "standard")

for path in sorted(SKILLS.glob("*/SKILL.md")):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not text.startswith("---\n"):
        errors.append(f"{path}: missing YAML frontmatter")
        continue
    frontmatter_match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not frontmatter_match:
        errors.append(f"{path}: malformed frontmatter block")
        continue
    frontmatter = frontmatter_match.group(1)
    name_match = re.search(r"^name:\s*([^\n]+)$", frontmatter, re.M)
    desc_match = re.search(r"^description:\s*(.+)$", frontmatter, re.M)
    if not name_match:
        errors.append(f"{path}: missing name")
        continue
    if not desc_match:
        errors.append(f"{path}: missing description")
        continue
    name = name_match.group(1).strip().strip('"\'')
    description = desc_match.group(1).strip().strip('"\'')
    if name != path.parent.name:
        errors.append(f"{path}: name {name!r} does not match directory {path.parent.name!r}")
    if not name.startswith("user-"):
        errors.append(f"{path}: name must use the user- prefix")
    if len(description) < 40:
        errors.append(f"{path}: description is too short to provide a useful trigger")
    if len(lines) >= 500:
        errors.append(f"{path}: SKILL.md must be under 500 lines")
    body = text[frontmatter_match.end():]
    if not re.search(r"^#\s+\S+", body, re.M):
        errors.append(f"{path}: missing top-level Markdown title")
    headings = [h.strip().lower() for h in re.findall(r"^##\s+(.+)$", body, re.M)]
    if len(headings) < 3:
        errors.append(f"{path}: expected at least three second-level headings")
    if not any(any(term in heading for term in workflow_terms) for heading in headings):
        errors.append(f"{path}: missing a workflow or process heading")
    if not any(any(term in heading for term in rules_terms) for heading in headings):
        errors.append(f"{path}: missing a rules, safety, quality, or boundary heading")
    if not any(any(term in heading for term in handoff_terms) for heading in headings):
        errors.append(f"{path}: missing a handoff, deliverable, report, or output heading")
    records.append((name, path))

names = [name for name, _ in records]

alias_path = ROOT / 'docs' / 'SKILL_ALIASES.json'
if not alias_path.is_file():
    errors.append(f'{alias_path}: generated alias manifest is missing')
else:
    try:
        aliases = json.loads(alias_path.read_text(encoding='utf-8'))
        expected_aliases = {name.removeprefix('user-') for name in names}
        if set(aliases) != expected_aliases:
            errors.append(f'{alias_path}: aliases do not match canonical skills')
        for alias, record in aliases.items():
            legacy = record.get('legacy_name')
            directory = record.get('directory')
            if legacy != f'user-{alias}' or directory != legacy:
                errors.append(f'{alias_path}: invalid mapping for {alias!r}')
    except (json.JSONDecodeError, OSError) as exc:
        errors.append(f'{alias_path}: invalid JSON manifest ({exc})')

for duplicate in sorted({name for name in names if names.count(name) > 1}):
    errors.append(f"duplicate skill name: {duplicate}")

for path in (ROOT / "docs").glob("*.md"):
    if "/home/ubuntu/" in path.read_text(encoding="utf-8"):
        errors.append(f"{path}: contains a sandbox-absolute path")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"Validated {len(records)} skills with metadata, structure, length, uniqueness, and public-path checks")
