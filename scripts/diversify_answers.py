#!/usr/bin/env python3
"""
Diversify Pre/Post Assessment Answer Keys
==========================================
Shuffles the correct answer positions across A/B/C/D so they're roughly
evenly distributed instead of ~80% being "B".

For each question:
1. Parses option lines (A., B., C., D.)
2. Identifies the correct answer
3. Shuffles options to new positions
4. Updates option text, Correct Answer line, Feedback references, and Answer Key

Ensures per-lesson distribution: with 5 questions, targets at least 1 each of
A/B/C (and D for 4-option questions), with the 5th randomly assigned.
"""

import os
import re
import random
import glob
import sys

# Seed for reproducibility (remove for true random)
random.seed(42)

LESSONS_DIR = os.path.expanduser("~/cast-science-resources/lessons")

# Stats tracking
stats = {"total_questions": 0, "changed": 0, "files_processed": 0}
answer_dist_before = {"A": 0, "B": 0, "C": 0, "D": 0}
answer_dist_after = {"A": 0, "B": 0, "C": 0, "D": 0}


def find_all_lesson_files():
    """Find all .md lesson files recursively."""
    files = []
    for root, dirs, filenames in os.walk(LESSONS_DIR):
        for f in filenames:
            if f.endswith(".md"):
                files.append(os.path.join(root, f))
    files.sort()
    return files


def parse_question_block(text, q_start, next_boundary):
    """Parse a single question block and extract options, correct answer, feedback."""
    block = text[q_start:next_boundary]

    # Find options (A., B., C., D.) - each on its own line
    option_pattern = re.compile(r'^([A-D])\.\s+(.+)$', re.MULTILINE)
    options = {}
    for m in option_pattern.finditer(block):
        options[m.group(1)] = m.group(2).strip()

    # Find correct answer
    correct_match = re.search(r'Correct Answer:\s*([A-D])', block)
    if not correct_match:
        return None
    correct_letter = correct_match.group(1)

    # Find feedback
    feedback_match = re.search(r'Feedback:\s*(.+?)(?=\n---|\n###|\Z)', block, re.DOTALL)
    feedback_text = feedback_match.group(1).strip() if feedback_match else ""

    return {
        "options": options,
        "correct": correct_letter,
        "feedback": feedback_text,
        "block_text": block,
        "block_start": q_start,
        "block_end": next_boundary,
    }


def generate_lesson_distribution(num_questions, num_options):
    """Generate a target answer distribution for a lesson's questions.
    Ensures roughly equal distribution across available letters."""
    letters = ["A", "B", "C", "D"][:num_options]
    # Start with one of each
    targets = list(letters)
    # Fill remaining slots
    remaining = num_questions - len(targets)
    for _ in range(remaining):
        targets.append(random.choice(letters))
    random.shuffle(targets)
    return targets[:num_questions]


def create_shuffle_mapping(options, target_letter):
    """Create a mapping that moves the correct answer to target_letter position.
    All other options are randomly distributed among remaining positions."""
    available_letters = sorted(options.keys())
    correct_letter = None
    for letter, text in options.items():
        # We'll get the correct letter from caller
        pass

    return None  # Placeholder - actual logic below


def shuffle_question(parsed_q, target_correct_letter):
    """Shuffle a question so the correct answer lands on target_correct_letter.
    Returns new option lines, new correct answer, and updated feedback."""
    options = parsed_q["options"]
    old_correct = parsed_q["correct"]
    feedback = parsed_q["feedback"]

    available_letters = sorted(options.keys())  # e.g., ['A', 'B', 'C'] or ['A', 'B', 'C', 'D']

    if target_correct_letter == old_correct and len(available_letters) <= 3:
        # For 3-option questions where correct is already target, still shuffle wrong answers
        pass

    # Build the mapping: old_letter -> new_letter
    # The correct answer must go to target_correct_letter
    mapping = {}
    mapping[old_correct] = target_correct_letter

    # Remaining old letters (wrong answers)
    remaining_old = [l for l in available_letters if l != old_correct]
    # Remaining new positions
    remaining_new = [l for l in available_letters if l != target_correct_letter]

    random.shuffle(remaining_new)
    for old_l, new_l in zip(remaining_old, remaining_new):
        mapping[old_l] = new_l

    # Build new options
    new_options = {}
    for old_letter, new_letter in mapping.items():
        new_options[new_letter] = options[old_letter]

    # Build reverse mapping: new_letter -> old_letter
    reverse_mapping = {v: k for k, v in mapping.items()}

    # Update feedback text - replace letter references
    new_feedback = remap_feedback(feedback, mapping, available_letters)

    return new_options, target_correct_letter, new_feedback, mapping


def remap_feedback(feedback, mapping, available_letters):
    """Remap letter references in feedback text.
    Handles patterns like 'If you chose A,' and 'If you chose B, you are correct.'
    Uses temporary placeholders to avoid double-replacement."""

    new_feedback = feedback

    # Use placeholders to avoid collision during replacement
    # First pass: replace old letters with placeholders
    for old_letter in available_letters:
        new_letter = mapping[old_letter]
        placeholder = f"__PLACEHOLDER_{new_letter}__"
        # Replace "If you chose X" patterns
        new_feedback = new_feedback.replace(f"If you chose {old_letter}", f"If you chose {placeholder}")

    # Second pass: replace placeholders with actual letters
    for letter in available_letters:
        placeholder = f"__PLACEHOLDER_{letter}__"
        new_feedback = new_feedback.replace(placeholder, letter)

    return new_feedback


def process_lesson_file(filepath):
    """Process a single lesson file, shuffling all assessment answers."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if file has assessment section
    if "## CAST-Aligned Pre/Post Assessment" not in content:
        return False

    # Find all question blocks
    question_starts = [(m.start(), m.group(1)) for m in re.finditer(r'### Question (\d+)', content)]
    if not question_starts:
        return False

    # Parse each question
    parsed_questions = []
    for i, (start, q_num) in enumerate(question_starts):
        # Find the end of this question block (next question or answer key)
        if i + 1 < len(question_starts):
            end = question_starts[i + 1][0]
        else:
            # Look for Answer Key section
            ak_match = re.search(r'### Answer Key', content[start:])
            if ak_match:
                end = start + ak_match.start()
            else:
                end = len(content)

        parsed = parse_question_block(content, start, end)
        if parsed:
            parsed["q_num"] = int(q_num)
            parsed_questions.append(parsed)

    if not parsed_questions:
        return False

    # Determine number of options (3 for K-2, 4 for others)
    num_options = len(parsed_questions[0]["options"])

    # Track original answers
    for pq in parsed_questions:
        answer_dist_before[pq["correct"]] += 1
        stats["total_questions"] += 1

    # Generate target distribution for this lesson
    target_answers = generate_lesson_distribution(len(parsed_questions), num_options)

    # Shuffle each question
    new_content = content
    # Process in reverse order to preserve string positions
    for i in range(len(parsed_questions) - 1, -1, -1):
        pq = parsed_questions[i]
        target = target_answers[i]

        new_options, new_correct, new_feedback, mapping = shuffle_question(pq, target)

        if new_correct != pq["correct"]:
            stats["changed"] += 1

        answer_dist_after[new_correct] += 1

        # Rebuild the question block
        old_block = pq["block_text"]
        new_block = old_block

        # Replace option lines
        for old_letter in sorted(pq["options"].keys()):
            old_line = f"{old_letter}. {pq['options'][old_letter]}"
            # We can't just replace because we need to put new letters
            # Instead, use a placeholder approach
            pass

        # More reliable: rebuild the block with regex substitutions
        # Replace each option line
        for old_letter in sorted(pq["options"].keys(), reverse=True):
            old_line_pattern = re.compile(
                rf'^{old_letter}\.\s+{re.escape(pq["options"][old_letter])}',
                re.MULTILINE
            )
            # Use placeholder
            new_block = old_line_pattern.sub(
                f"__OPT_{mapping[old_letter]}__. {pq['options'][old_letter]}",
                new_block
            )

        # Replace placeholders with actual letters, sorted by letter order
        # First collect all new options in order
        sorted_new = sorted(new_options.items())  # [(A, text), (B, text), ...]

        # Actually, let's use a cleaner approach - rebuild the options section
        # Find where options start and end in the block
        first_opt = re.search(r'^A\.\s+', old_block, re.MULTILINE)
        last_letter = sorted(pq["options"].keys())[-1]
        last_opt = re.search(
            rf'^{last_letter}\.\s+{re.escape(pq["options"][last_letter])}',
            old_block, re.MULTILINE
        )

        if first_opt and last_opt:
            opt_start = first_opt.start()
            opt_end = last_opt.end()

            # Build new options string in letter order
            new_opt_lines = []
            for letter in sorted(new_options.keys()):
                new_opt_lines.append(f"{letter}. {new_options[letter]}")
            new_opt_str = "\n".join(new_opt_lines)

            new_block = old_block[:opt_start] + new_opt_str + old_block[opt_end:]

        # Replace Correct Answer line
        new_block = re.sub(
            r'Correct Answer:\s*[A-D]',
            f'Correct Answer: {new_correct}',
            new_block
        )

        # Replace feedback
        old_feedback_match = re.search(r'(Feedback:\s*).+?(?=\n---|\n###|\Z)', new_block, re.DOTALL)
        if old_feedback_match:
            new_block = (
                new_block[:old_feedback_match.start()] +
                f"Feedback: {new_feedback}" +
                new_block[old_feedback_match.end():]
            )

        # Replace in full content
        new_content = new_content[:pq["block_start"]] + new_block + new_content[pq["block_end"]:]

    # Update Answer Key section
    ak_match = re.search(r'### Answer Key\n\n(.*?)(?=\n---|\n##|\Z)', new_content, re.DOTALL)
    if ak_match:
        ak_text = ak_match.group(1)
        new_ak_lines = []
        for pq, target in zip(parsed_questions, target_answers):
            # Find and update the answer key line for this question
            q_num = pq["q_num"]
            ak_line_pattern = re.compile(
                rf'Question {q_num}:\s*[A-D](\s*\(.+?\))'
            )
            ak_line_match = ak_line_pattern.search(ak_text)
            if ak_line_match:
                new_line = f"Question {q_num}: {target}{ak_line_match.group(1)}"
                ak_text = ak_line_pattern.sub(new_line, ak_text)

        new_content = (
            new_content[:ak_match.start(1)] +
            ak_text +
            new_content[ak_match.end(1):]
        )

    # Write updated content
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    stats["files_processed"] += 1
    return True


def main():
    print("=" * 60)
    print("DIVERSIFY PRE/POST ASSESSMENT ANSWER KEYS")
    print("=" * 60)

    # Check for --dry-run flag
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("\n*** DRY RUN MODE - No files will be modified ***\n")

    files = find_all_lesson_files()
    print(f"\nFound {len(files)} lesson files\n")

    for filepath in files:
        relpath = os.path.relpath(filepath, LESSONS_DIR)

        if dry_run:
            # Just count distributions
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            for m in re.finditer(r'Correct Answer:\s*([A-D])', content):
                answer_dist_before[m.group(1)] += 1
                stats["total_questions"] += 1
            stats["files_processed"] += 1
        else:
            result = process_lesson_file(filepath)
            if result:
                print(f"  [OK] {relpath}")
            else:
                print(f"  [SKIP] {relpath} (no assessment section)")

    print(f"\n{'=' * 60}")
    print("RESULTS")
    print(f"{'=' * 60}")
    print(f"Files processed: {stats['files_processed']}")
    print(f"Total questions: {stats['total_questions']}")

    if dry_run:
        print(f"\nCurrent answer distribution:")
        for letter in ["A", "B", "C", "D"]:
            count = answer_dist_before[letter]
            pct = (count / stats["total_questions"] * 100) if stats["total_questions"] > 0 else 0
            print(f"  {letter}: {count} ({pct:.1f}%)")
    else:
        print(f"Questions changed: {stats['changed']}")
        print(f"\nNew answer distribution:")
        for letter in ["A", "B", "C", "D"]:
            count = answer_dist_after[letter]
            pct = (count / stats["total_questions"] * 100) if stats["total_questions"] > 0 else 0
            print(f"  {letter}: {count} ({pct:.1f}%)")


if __name__ == "__main__":
    main()
