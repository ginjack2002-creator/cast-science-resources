"""
Rename Activities → Steps and STEPs → Tasks across all ModelIt! lesson files.

Platform alignment:
  - "Activity 1/2/3/4" → "Step 1/2/3/4" (top-level sections)
  - "STEP 1/2/3/4/5" → "Task A/B/C/D/E" (sub-instructions within each step)
  - Natural-language references updated in video scripts and prose

Safety:
  - STOPS processing at "## CAST-Aligned" to avoid touching assessment questions
  - Only processes .md files in the lessons/ and templates/ directories
"""

import re
import os
import sys
from pathlib import Path

# Fix Windows console encoding
sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).parent.parent
LESSONS_DIR = REPO_ROOT / "lessons"
TEMPLATES_DIR = REPO_ROOT / "templates"

STEP_MAP = {
    "STEP 1:": "Task A:",
    "STEP 2:": "Task B:",
    "STEP 3:": "Task C:",
    "STEP 4:": "Task D:",
    "STEP 5:": "Task E:",
    "STEP 6:": "Task F:",
    "STEP 7:": "Task G:",
}


def process_file(filepath, dry_run=False):
    """Process a single markdown file. Returns (changed: bool, changes: list[str])."""
    with open(filepath, "r", encoding="utf-8") as f:
        original = f.read()

    # Split at CAST-Aligned section to protect it
    cast_marker = "## CAST-Aligned"
    if cast_marker in original:
        parts = original.split(cast_marker, 1)
        content = parts[0]
        protected = cast_marker + parts[1]
    else:
        content = original
        protected = ""

    changes = []

    # --- Top-level: Activity N → Step N (markdown headers) ---
    for n in range(1, 5):
        old = f"## Activity {n}:"
        new = f"## Step {n}:"
        if old in content:
            content = content.replace(old, new)
            changes.append(f"  Header: '{old}' → '{new}'")

    # --- Sub-steps: STEP N: → Task X: ---
    for old, new in STEP_MAP.items():
        if old in content:
            count = content.count(old)
            content = content.replace(old, new)
            changes.append(f"  Sub-step: '{old}' → '{new}' ({count}x)")

    # --- Natural-language references in video scripts and prose ---
    # "the next activity" → "the next step" (case-insensitive)
    pattern_next = re.compile(r'\b(the next|The next|THE NEXT) activity\b', re.IGNORECASE)
    matches = pattern_next.findall(content)
    if matches:
        content = pattern_next.sub(lambda m: f"{m.group(1)} step", content)
        changes.append(f"  Prose: 'the next activity' → 'the next step' ({len(matches)}x)")

    # "In the next activity" → "In the next step"
    pattern_in_next = re.compile(r'\b(In the next|in the next) activity\b')
    matches = pattern_in_next.findall(content)
    if matches:
        content = pattern_in_next.sub(lambda m: f"{m.group(1)} step", content)
        changes.append(f"  Prose: 'In the next activity' → 'In the next step' ({len(matches)}x)")

    # "Activity 1" etc. in prose (not already caught by header replacement)
    # Only match when NOT at start of line with ## (those were already handled)
    for n in range(1, 5):
        # Match "Activity N" in prose (not markdown headers)
        pattern = re.compile(rf'(?<!## )Activity {n}\b')
        found = pattern.findall(content)
        if found:
            content = pattern.sub(f"Step {n}", content)
            changes.append(f"  Prose: 'Activity {n}' → 'Step {n}' ({len(found)}x)")

    # "this activity" → "this step"
    pattern_this = re.compile(r'\bthis activity\b', re.IGNORECASE)
    matches = pattern_this.findall(content)
    if matches:
        content = pattern_this.sub(lambda m: "this step" if m.group()[0].islower() else "This step", content)
        changes.append(f"  Prose: 'this activity' → 'this step' ({len(matches)}x)")

    # "each activity" → "each step"
    pattern_each = re.compile(r'\beach activity\b', re.IGNORECASE)
    matches = pattern_each.findall(content)
    if matches:
        content = pattern_each.sub(lambda m: "each step" if m.group()[0].islower() else "Each step", content)
        changes.append(f"  Prose: 'each activity' → 'each step' ({len(matches)}x)")

    # Reassemble with protected section
    result = content + protected

    if result != original:
        if not dry_run:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(result)
        return True, changes
    return False, changes


def find_lesson_files():
    """Find all lesson markdown files."""
    files = []
    for md_file in LESSONS_DIR.rglob("*.md"):
        files.append(md_file)
    # Also include template
    template = TEMPLATES_DIR / "lesson-template.md"
    if template.exists():
        files.append(template)
    return sorted(files)


def main():
    dry_run = "--dry-run" in sys.argv
    single_file = None

    # Allow targeting a single file for testing
    for arg in sys.argv[1:]:
        if arg != "--dry-run" and os.path.isfile(arg):
            single_file = Path(arg).resolve()

    if single_file:
        files = [single_file]
    else:
        files = find_lesson_files()

    if dry_run:
        print("=== DRY RUN (no files will be modified) ===\n")

    total_changed = 0
    total_files = len(files)

    for filepath in files:
        changed, changes = process_file(filepath, dry_run=dry_run)
        if changed:
            total_changed += 1
            rel = filepath.relative_to(REPO_ROOT)
            print(f"{'[DRY] ' if dry_run else ''}Modified: {rel}")
            for c in changes:
                print(c)
            print()

    print(f"\n{'[DRY RUN] ' if dry_run else ''}Summary: {total_changed}/{total_files} files {'would be ' if dry_run else ''}modified")


if __name__ == "__main__":
    main()
