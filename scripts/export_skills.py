from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / 'skills'
PACKS = {
    'web-app-team': [
        'user-task-orchestrator', 'user-software-engineering', 'user-react-development',
        'user-typescript-development', 'user-api-interface-design', 'user-browser-testing',
        'user-accessibility-audit', 'user-security-risk-review', 'user-debugging-testing',
    ],
    'solo-indie-hacker': [
        'user-task-orchestrator', 'user-project-delivery', 'user-product-discovery',
        'user-prd-spec-writing', 'user-roadmap-prioritization', 'user-frontend-styling',
        'user-monetization-revenue-strategy', 'user-advanced-spreadsheet-modeling',
    ],
    'security-review': [
        'user-task-orchestrator', 'user-rules-of-engagement-security',
        'user-attack-surface-mapping-authorized', 'user-authorized-security-testing',
        'user-security-findings-report', 'user-remediation-verification-retest',
        'user-security-risk-review', 'user-vulnerability-detection',
    ],
    'student-stem': [
        'user-task-orchestrator', 'user-tutoring-socratic-method', 'user-math-foundations',
        'user-differential-calculus', 'user-physics-mechanics', 'user-chemistry-stoichiometry',
        'user-units-dimensional-analysis', 'user-exam-prep-practice-problems',
    ],
    'content-creator': [
        'user-task-orchestrator', 'user-technical-blog-deep-dive', 'user-video-script-storyboard',
        'user-slide-deck-structure', 'user-podcast-show-notes-transcript-cleanup',
        'user-brand-style-guide-application', 'user-image-prompt-engineering',
        'user-multilingual-localization-review',
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Copy canonical Agent Skill Kit modules to an explicit host destination.')
    parser.add_argument('--skill', action='append', default=[], help='Canonical skill directory name; repeatable.')
    parser.add_argument('--pack', choices=sorted(PACKS), action='append', default=[], help='Starter pack name; repeatable.')
    parser.add_argument('--destination', required=True, type=Path, help='Explicit destination selected for the target host.')
    parser.add_argument('--flatten', action='store_true', help='Copy SKILL.md files as <skill-name>.md instead of directories.')
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    names = list(dict.fromkeys(args.skill + [name for pack in args.pack for name in PACKS[pack]]))
    if not names:
        raise SystemExit('Select at least one --skill or --pack.')
    missing = [name for name in names if not (SKILLS / name / 'SKILL.md').is_file()]
    if missing:
        raise SystemExit('Unknown or incomplete skills: ' + ', '.join(missing))
    args.destination.mkdir(parents=True, exist_ok=True)
    for name in names:
        source = SKILLS / name
        if args.flatten:
            shutil.copy2(source / 'SKILL.md', args.destination / f'{name}.md')
        else:
            shutil.copytree(source, args.destination / name, dirs_exist_ok=True)
    print(f'Exported {len(names)} canonical skills to {args.destination}')


if __name__ == '__main__':
    main()
