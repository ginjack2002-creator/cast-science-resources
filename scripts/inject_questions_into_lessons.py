#!/usr/bin/env python3
"""
Inject CAST-Aligned Pre/Post Assessment questions into lesson markdown files.
Reads from lesson_questions_*.py files and appends formatted question sections
to each lesson .md file in the lessons/ directory.

Usage:
    python inject_questions_into_lessons.py           # Process all lessons
    python inject_questions_into_lessons.py --dry-run  # Preview without writing
"""

import os
import sys
import re
import importlib.util
import glob

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
LESSONS_DIR = os.path.join(os.path.dirname(SCRIPTS_DIR), "lessons")

# ============================================================
# Load all question data
# ============================================================

def load_all_questions():
    """Load all question files into a single dict keyed by lesson ID."""
    all_q = {}
    question_files = glob.glob(os.path.join(SCRIPTS_DIR, "lesson_questions_*.py"))

    for filepath in sorted(question_files):
        filename = os.path.basename(filepath)
        mod_name = filename[:-3]

        try:
            spec = importlib.util.spec_from_file_location(mod_name, filepath)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)

            if hasattr(mod, "ALL_QUESTIONS"):
                for lesson_id, questions in mod.ALL_QUESTIONS.items():
                    all_q[lesson_id] = questions
                print(f"  Loaded {len(mod.ALL_QUESTIONS)} lessons from {filename}")
        except Exception as e:
            print(f"  ERROR loading {filename}: {e}")

    return all_q


# ============================================================
# Extract lesson metadata from markdown
# ============================================================

def extract_lesson_id(content):
    """Extract Lesson ID from markdown content."""
    match = re.search(r'\*\*Lesson ID\*\*\s*\|\s*(\S+)', content)
    if match:
        return match.group(1).strip()
    return None


def extract_ngss(content):
    """Extract NGSS standard from markdown content."""
    # Look for the NGSS Standard section and the bold standard on the next line
    match = re.search(r'### NGSS Standard\s*\n\*\*([^*]+)\*\*', content)
    if match:
        return match.group(1).strip()
    # Fallback: look for pattern like 5-ESS2-1 anywhere near NGSS
    match = re.search(r'NGSS.*?\n.*?\*\*(\S+-\S+-\d+[^*]*)\*\*', content)
    if match:
        return match.group(1).strip()
    return "NGSS Standard"


def extract_ngss_desc(content):
    """Extract NGSS description text after the standard."""
    match = re.search(r'### NGSS Standard\s*\n\*\*[^*]+\*\*:?\s*(.*?)(?:\n\n|\n###)', content, re.DOTALL)
    if match:
        desc = match.group(1).strip()
        if desc:
            return desc
    return ""


# ============================================================
# Format questions as CAST-aligned markdown
# ============================================================

def format_assessment_section(lesson_id, ngss, questions):
    """Format MC questions into the CAST-aligned markdown section."""
    pre_qs = questions.get("mc_pre_assessment", [])
    post_qs = questions.get("mc_post_assessment", [])

    if not pre_qs and not post_qs:
        return ""

    # Use whichever list is longer for the combined pre/post set
    # The exemplar uses the SAME questions for both pre and post
    combined_qs = pre_qs if len(pre_qs) >= len(post_qs) else post_qs
    num_qs = len(combined_qs)

    lines = []
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## CAST-Aligned Pre/Post Assessment")
    lines.append("")
    lines.append("### Administration Instructions")
    lines.append("")
    lines.append(f"These {num_qs} multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of {num_qs}. Learning growth = post-score minus pre-score.")
    lines.append("")
    lines.append(f"Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to {ngss}.")
    lines.append("")

    # Pre-Assessment Questions
    lines.append("---")
    lines.append("")
    lines.append("### Pre-Assessment Questions")
    lines.append("")

    for i, q in enumerate(pre_qs, 1):
        lines.append(f"### Question {i}")
        lines.append("")
        lines.append(q["question"])
        lines.append("")

        for letter in ["A", "B", "C", "D"]:
            if letter in q.get("choices", {}):
                lines.append(f"{letter}. {q['choices'][letter]}")
        lines.append("")

        lines.append(f"Correct Answer: {q['correct']}")
        lines.append("")

        # Build feedback
        feedback_parts = []
        correct_letter = q["correct"]
        correct_text = q.get("choices", {}).get(correct_letter, "")
        feedback_correct = q.get("feedback_correct", "")
        feedback_incorrect = q.get("feedback_incorrect", "")

        feedback = f"Feedback: {feedback_correct}"
        if feedback_incorrect:
            feedback += f" {feedback_incorrect}"
        lines.append(feedback)
        lines.append("")
        lines.append("---")
        lines.append("")

    # Post-Assessment Questions
    lines.append("### Post-Assessment Questions")
    lines.append("")

    for i, q in enumerate(post_qs, 1):
        lines.append(f"### Question {i}")
        lines.append("")
        lines.append(q["question"])
        lines.append("")

        for letter in ["A", "B", "C", "D"]:
            if letter in q.get("choices", {}):
                lines.append(f"{letter}. {q['choices'][letter]}")
        lines.append("")

        lines.append(f"Correct Answer: {q['correct']}")
        lines.append("")

        feedback_correct = q.get("feedback_correct", "")
        feedback_incorrect = q.get("feedback_incorrect", "")

        feedback = f"Feedback: {feedback_correct}"
        if feedback_incorrect:
            feedback += f" {feedback_incorrect}"
        lines.append(feedback)
        lines.append("")
        lines.append("---")
        lines.append("")

    # Answer Key
    lines.append("### Answer Key")
    lines.append("")
    lines.append("**Pre-Assessment:**")
    for i, q in enumerate(pre_qs, 1):
        lines.append(f"Question {i}: {q['correct']}")
    lines.append("")
    lines.append("**Post-Assessment:**")
    for i, q in enumerate(post_qs, 1):
        lines.append(f"Question {i}: {q['correct']}")
    lines.append("")

    return "\n".join(lines)


# ============================================================
# Inject into lesson file
# ============================================================

def inject_into_lesson(filepath, all_questions, dry_run=False):
    """Inject assessment section into a single lesson markdown file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already has assessment section
    if "CAST-Aligned Pre/Post Assessment" in content:
        return "SKIP (already has assessment)"

    # Extract lesson ID
    lesson_id = extract_lesson_id(content)
    if not lesson_id:
        return "SKIP (no lesson ID found)"

    # Find matching questions
    questions = all_questions.get(lesson_id)
    if not questions:
        return f"SKIP (no questions for {lesson_id})"

    # Extract NGSS standard
    ngss = extract_ngss(content)

    # Format the assessment section
    assessment_md = format_assessment_section(lesson_id, ngss, questions)
    if not assessment_md:
        return f"SKIP (empty assessment for {lesson_id})"

    # Find insertion point: before "## Resources" if it exists, otherwise before "## Lesson Metadata", otherwise at end
    insertion_markers = ["## Resources", "## Lesson Metadata"]
    insert_pos = None

    for marker in insertion_markers:
        pos = content.find(marker)
        if pos != -1:
            # Back up to include the --- before the section
            prefix = content[:pos]
            last_divider = prefix.rfind("---")
            if last_divider != -1 and last_divider > pos - 20:
                insert_pos = last_divider
            else:
                insert_pos = pos
            break

    if insert_pos is None:
        # Append at end
        insert_pos = len(content)

    # Insert
    new_content = content[:insert_pos].rstrip() + "\n" + assessment_md + "\n" + content[insert_pos:]

    if not dry_run:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

    pre_count = len(questions.get("mc_pre_assessment", []))
    post_count = len(questions.get("mc_post_assessment", []))
    return f"OK ({lesson_id}: {pre_count} pre + {post_count} post)"


# ============================================================
# Main
# ============================================================

def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("=== DRY RUN MODE (no files will be modified) ===\n")

    print("Loading question data...")
    all_questions = load_all_questions()
    print(f"Total lessons with questions: {len(all_questions)}\n")

    # Find all lesson markdown files
    lesson_files = sorted(glob.glob(os.path.join(LESSONS_DIR, "**", "*.md"), recursive=True))
    print(f"Found {len(lesson_files)} lesson markdown files\n")

    stats = {"ok": 0, "skip_exists": 0, "skip_no_id": 0, "skip_no_q": 0, "error": 0}

    for filepath in lesson_files:
        rel_path = os.path.relpath(filepath, LESSONS_DIR)
        try:
            result = inject_into_lesson(filepath, all_questions, dry_run)
            print(f"  {rel_path}: {result}")

            if result.startswith("OK"):
                stats["ok"] += 1
            elif "already has" in result:
                stats["skip_exists"] += 1
            elif "no lesson ID" in result:
                stats["skip_no_id"] += 1
            elif "no questions" in result:
                stats["skip_no_q"] += 1
        except Exception as e:
            print(f"  {rel_path}: ERROR - {e}")
            stats["error"] += 1

    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Updated:              {stats['ok']}")
    print(f"Already had section:  {stats['skip_exists']}")
    print(f"No lesson ID:         {stats['skip_no_id']}")
    print(f"No matching questions: {stats['skip_no_q']}")
    print(f"Errors:               {stats['error']}")
    print(f"Total files:          {len(lesson_files)}")

    if dry_run:
        print(f"\nDRY RUN complete. No files were modified.")
        print(f"Run without --dry-run to apply changes.")


if __name__ == "__main__":
    main()
