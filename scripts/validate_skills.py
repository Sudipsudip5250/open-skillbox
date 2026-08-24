from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1] / "skills"
errors = []
count = 0
for path in sorted(root.glob("*/SKILL.md")):
    count += 1
    text = path.read_text()
    if not text.startswith("---\n"):
        errors.append(f"{path}: missing YAML frontmatter")
        continue
    if not re.search(r"^name:\s*\S+", text, re.M):
        errors.append(f"{path}: missing name")
    if not re.search(r"^description:\s*.+", text, re.M):
        errors.append(f"{path}: missing description")
    if len(text.splitlines()) >= 500:
        errors.append(f"{path}: too long")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"Validated {count} skills")
