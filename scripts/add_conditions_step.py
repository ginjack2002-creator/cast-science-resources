#!/usr/bin/env python3
"""
Batch Add "Set the Conditions" Step to All Flagged Lessons
==========================================================
Reads the conditional audit CSV and inserts an age-appropriate
"Set the Conditions" task into Step 4 of each flagged lesson.

Condition text is customized per lesson based on:
- Specific components and relationships
- Grade-appropriate reading level
- Scientific context from the lesson
"""

import os
import re
import csv
import ast
import sys

BASE_DIR = os.path.expanduser("~/cast-science-resources")
LESSONS_DIR = os.path.join(BASE_DIR, "lessons")
AUDIT_CSV = os.path.join(BASE_DIR, "scripts", "output", "conditional_audit_report.csv")

stats = {"updated": 0, "skipped": 0, "already_done": 0, "errors": 0}


def get_grade_band(grade_str, lesson_id):
    """Determine grade band for age-appropriate language."""
    g = grade_str.lower()
    lid = lesson_id.upper()

    if any(x in g for x in ["kinder", "k "]) or lid.startswith("GK"):
        return "K"
    elif any(x in g for x in ["1st", "1 "]) or lid.startswith("G01"):
        return "1"
    elif any(x in g for x in ["2nd", "2 "]) or lid.startswith("G02"):
        return "2"
    elif any(x in g for x in ["3rd", "3 "]) or lid.startswith("G03"):
        return "3"
    elif any(x in g for x in ["4th", "4 "]) or lid.startswith("G04"):
        return "4-5"
    elif any(x in g for x in ["5th", "5 "]) or lid.startswith("G05"):
        return "4-5"
    elif any(x in g for x in ["6th", "6 "]) or lid.startswith("G06"):
        return "6-8"
    elif any(x in g for x in ["7th", "7 "]) or lid.startswith("G07"):
        return "6-8"
    elif any(x in g for x in ["8th", "8 "]) or lid.startswith("G08"):
        return "6-8"
    elif lid.startswith(("G09", "G10", "G11", "G12")):
        return "9-12"
    elif lid.startswith("NE"):
        return "6-8"  # Natures Engineers targets middle school
    return "4-5"  # fallback


def generate_conditions_text(conditions_data, grade_band, title):
    """Generate age-appropriate 'Set the Conditions' text for a lesson."""
    if not conditions_data:
        return None

    # Parse the conditions (stored as string repr of list of dicts)
    try:
        conditions = ast.literal_eval(conditions_data)
    except (ValueError, SyntaxError):
        return None

    if not conditions:
        return None

    # Get the primary condition (first one)
    primary = conditions[0]
    conn_parts = primary["connection"].split(" → ")
    if len(conn_parts) < 2:
        return None

    amplifier = conn_parts[0].strip()
    target = conn_parts[1].strip().replace(" (feedback loop)", "")
    cond_text = primary["condition_text"]  # e.g., "IF Dry Vegetation is ON"

    # Extract the condition component name
    cond_match = re.match(r'IF (.+?) is (ON|OFF)', cond_text)
    if not cond_match:
        return None
    condition_component = cond_match.group(1)
    condition_state = cond_match.group(2)

    # Build additional conditions if present (up to 2 more)
    extra_conditions = []
    for c in conditions[1:3]:
        c_parts = c["connection"].split(" → ")
        if len(c_parts) >= 2:
            c_amp = c_parts[0].strip()
            c_target = c_parts[1].strip().replace(" (feedback loop)", "")
            c_match = re.match(r'IF (.+?) is (ON|OFF)', c["condition_text"])
            if c_match and c_amp != amplifier:
                extra_conditions.append({
                    "amplifier": c_amp,
                    "target": c_target,
                    "condition_component": c_match.group(1),
                    "condition_state": c_match.group(2)
                })

    # Generate text based on grade band
    if grade_band in ("K", "1", "2", "3"):
        text = generate_k3_text(amplifier, target, condition_component, condition_state, title, extra_conditions)
    elif grade_band == "4-5":
        text = generate_45_text(amplifier, target, condition_component, condition_state, title, extra_conditions)
    elif grade_band == "6-8":
        text = generate_68_text(amplifier, target, condition_component, condition_state, title, extra_conditions)
    else:  # 9-12
        text = generate_912_text(amplifier, target, condition_component, condition_state, title, extra_conditions)

    return text


def generate_k3_text(amp, target, cond_comp, cond_state, title, extras):
    """K-3: Simple, playful language."""
    state_word = "happening" if cond_state == "ON" else "NOT happening"
    lines = [
        f"TEACH YOUR MODEL A RULE!",
        f"",
        f"Look at your model. Right now, when {amp} is ON, {target}",
        f"goes way up — even when it shouldn't!",
        f"",
        f"In the real world, {amp} only changes {target} when",
        f"{cond_comp} is {state_word}. Let's teach your model this rule!",
        f"",
        f"Task A: ADD THE RULE",
        f"   \u2022 Click on the arrow from {amp} to {target}",
        f"   \u2022 Click \"Conditions\" in the toolbar",
        f"   \u2022 Set: IF {cond_comp} is {cond_state}",
        f"   \u2022 Click \"Save Conditions\"",
        f"",
        f"Task B: TEST IT",
        f"   \u2022 Run your simulation again",
        f"   \u2022 Does it make more sense now?",
        f"   \u2022 Try turning {cond_comp} ON and OFF — see what changes!",
    ]

    # Add extra conditions
    for i, ec in enumerate(extras):
        lines.extend([
            f"",
            f"Task {chr(67 + i)}: ADD ANOTHER RULE",
            f"   \u2022 Click on the arrow from {ec['amplifier']} to {ec['target']}",
            f"   \u2022 Click \"Conditions\"",
            f"   \u2022 Set: IF {ec['condition_component']} is {ec['condition_state']}",
            f"   \u2022 Click \"Save Conditions\"",
        ])

    lines.extend([
        f"",
        f"Now your model is SMARTER! It knows the rules of the real world.",
    ])

    return "\n".join(lines)


def generate_45_text(amp, target, cond_comp, cond_state, title, extras):
    """Grades 4-5: Clear, engaging language."""
    state_word = "active" if cond_state == "ON" else "inactive"
    lines = [
        f"SET THE CONDITIONS — MAKE YOUR MODEL SMARTER",
        f"",
        f"Your model works, but something isn't quite right. When {amp}",
        f"is at 100%, {target} shoots up — even when it shouldn't!",
        f"",
        f"In the real world, {amp} only affects {target} when {cond_comp}",
        f"is {state_word}. Without {cond_comp}, {amp} alone can't change {target}.",
        f"Let's teach your model this rule.",
        f"",
        f"Task A: FIND THE PROBLEM",
        f"   \u2022 Run your simulation and watch {target}",
        f"   \u2022 Notice how {amp} pushes {target} up even when",
        f"     {cond_comp} is OFF — that's not right!",
        f"",
        f"Task B: ADD THE RULE",
        f"   \u2022 Click on the arrow from {amp} to {target}",
        f"   \u2022 In the toolbar that pops up, click \"Conditions\"",
        f"   \u2022 A panel opens. Set: IF {cond_comp} is {cond_state}",
        f"   \u2022 Click \"Save Conditions\"",
        f"   \u2022 This tells the model: \"{amp} only affects {target}",
        f"     when {cond_comp} is {state_word}\"",
        f"",
        f"Task C: TEST YOUR SMARTER MODEL",
        f"   \u2022 Re-run the simulation",
        f"   \u2022 Try different combinations of {amp} and {cond_comp}",
        f"   \u2022 Does the model match the real world now?",
    ]

    for i, ec in enumerate(extras):
        ec_state = "active" if ec["condition_state"] == "ON" else "inactive"
        lines.extend([
            f"",
            f"Task {chr(68 + i)}: ADD ANOTHER RULE",
            f"   \u2022 Click on the arrow from {ec['amplifier']} to {ec['target']}",
            f"   \u2022 Click \"Conditions\"",
            f"   \u2022 Set: IF {ec['condition_component']} is {ec['condition_state']}",
            f"   \u2022 Click \"Save Conditions\"",
            f"   \u2022 {ec['amplifier']} only affects {ec['target']} when",
            f"     {ec['condition_component']} is {ec_state}",
        ])

    lines.extend([
        f"",
        f"Your model is SMARTER now — it knows the rules!",
    ])

    return "\n".join(lines)


def generate_68_text(amp, target, cond_comp, cond_state, title, extras):
    """Grades 6-8: More direct, scientific language."""
    state_word = "active" if cond_state == "ON" else "inactive"
    lines = [
        f"SET THE CONDITIONS — REFINE YOUR MODEL",
        f"",
        f"Your model shows a relationship between {amp} and {target},",
        f"but right now that relationship applies ALL the time. In the",
        f"real system, {amp} only affects {target} when {cond_comp} is {state_word}.",
        f"",
        f"This is called a CONDITIONAL RELATIONSHIP — the connection",
        f"between two components depends on a third component's state.",
        f"",
        f"Task A: SET THE CONDITION",
        f"   \u2022 Click on the connection arrow from {amp} to {target}",
        f"   \u2022 In the toolbar, click \"Conditions\"",
        f"   \u2022 In the conditions panel, set: IF {cond_comp} is {cond_state}",
        f"   \u2022 Click \"Save Conditions\"",
        f"",
        f"Task B: VERIFY THE MODEL",
        f"   \u2022 Run the simulation with {cond_comp} OFF and {amp} ON",
        f"   \u2022 {target} should NOT respond to {amp} alone",
        f"   \u2022 Now turn {cond_comp} ON — {amp}'s effect on {target} activates",
        f"   \u2022 This matches how the real system behaves",
    ]

    for i, ec in enumerate(extras):
        ec_state = "active" if ec["condition_state"] == "ON" else "inactive"
        lines.extend([
            f"",
            f"Task {chr(67 + i)}: SET ADDITIONAL CONDITION",
            f"   \u2022 Click on the arrow from {ec['amplifier']} to {ec['target']}",
            f"   \u2022 Click \"Conditions\" and set: IF {ec['condition_component']} is {ec['condition_state']}",
            f"   \u2022 Save — {ec['amplifier']} now only affects {ec['target']} when",
            f"     {ec['condition_component']} is {ec_state}",
        ])

    lines.extend([
        f"",
        f"Your model now captures the conditional logic of the real system.",
        f"Not all relationships are always active — some depend on conditions.",
    ])

    return "\n".join(lines)


def generate_912_text(amp, target, cond_comp, cond_state, title, extras):
    """Grades 9-12: Technical, precise language."""
    state_word = "active" if cond_state == "ON" else "inactive"
    lines = [
        f"CONFIGURE CONNECTION CONDITIONS — MODEL REFINEMENT",
        f"",
        f"Your current model treats the {amp} \u2192 {target} relationship as",
        f"unconditional. However, this relationship is scientifically",
        f"contingent on {cond_comp} being {state_word}. Without this condition,",
        f"the simulation produces inaccurate results: {amp} drives {target}",
        f"even when the prerequisite state is not met.",
        f"",
        f"Task A: CONFIGURE THE CONNECTION CONDITION",
        f"   \u2022 Select the connection arrow: {amp} \u2192 {target}",
        f"   \u2022 Click \"Conditions\" in the connection toolbar",
        f"   \u2022 Set the regulator condition: IF {cond_comp} is {cond_state}",
        f"   \u2022 Click \"Save Conditions\"",
        f"",
        f"Task B: VALIDATE THE CONDITIONAL MODEL",
        f"   \u2022 Run the simulation with {cond_comp} {state_word} and observe",
        f"     how {amp}'s effect on {target} is now gated",
        f"   \u2022 Toggle {cond_comp} ON/OFF while {amp} remains constant",
        f"   \u2022 Verify that {target} only responds to {amp} when the",
        f"     condition is satisfied",
    ]

    for i, ec in enumerate(extras):
        ec_state = "active" if ec["condition_state"] == "ON" else "inactive"
        lines.extend([
            f"",
            f"Task {chr(67 + i)}: ADDITIONAL CONDITION",
            f"   \u2022 Select: {ec['amplifier']} \u2192 {ec['target']}",
            f"   \u2022 Set condition: IF {ec['condition_component']} is {ec['condition_state']}",
            f"   \u2022 This ensures {ec['amplifier']}'s effect on {ec['target']}",
            f"     is contingent on {ec['condition_component']} being {ec_state}",
        ])

    lines.extend([
        f"",
        f"These conditional relationships capture critical system behavior:",
        f"not all connections operate continuously. Some are gated by the",
        f"state of other components, creating the non-linear dynamics that",
        f"characterize real-world complex systems.",
    ])

    return "\n".join(lines)


def find_lesson_file(lesson_id):
    """Find the .md file for a given lesson ID."""
    for root, dirs, filenames in os.walk(LESSONS_DIR):
        for f in filenames:
            if f.endswith(".md") and lesson_id in f:
                return os.path.join(root, f)

    # Try more flexible matching
    clean_id = lesson_id.replace("-", "").replace("L", "L")
    for root, dirs, filenames in os.walk(LESSONS_DIR):
        for f in filenames:
            clean_f = f.replace("-", "")
            if f.endswith(".md") and clean_id in clean_f:
                return os.path.join(root, f)

    return None


def insert_conditions_into_step4(filepath, conditions_text):
    """Insert the conditions text at the beginning of Step 4's text editor block."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if already has conditions
    if "SET THE CONDITIONS" in content or "CONFIGURE CONNECTION CONDITIONS" in content or "TEACH YOUR MODEL A RULE" in content:
        return False  # Already updated

    # Find Step 4 text editor block
    # Pattern: ## Step 4: ... ### Text Editor ... ```
    step4_match = re.search(
        r'(## Step 4.*?### Text Editor\s*\n\s*```\s*\n)',
        content, re.DOTALL
    )

    if not step4_match:
        return None  # Couldn't find Step 4

    insert_point = step4_match.end()

    # Find the existing content start (the title line after ```)
    # We'll look for the first non-empty line
    remaining = content[insert_point:]

    # Find the first line of existing content
    first_line_match = re.match(r'([A-Z].*?\n)', remaining)
    if not first_line_match:
        return None

    # Build the insertion block
    insertion = (
        f"{conditions_text}\n\n"
        f"\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501"
        f"\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501"
        f"\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\n\n"
        f"NOW LET'S PLAY AND EXPLORE\n\n"
    )

    new_content = content[:insert_point] + insertion + content[insert_point:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def main():
    print("=" * 70)
    print("BATCH ADD 'SET THE CONDITIONS' TO ALL FLAGGED LESSONS")
    print("=" * 70)

    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("\n*** DRY RUN MODE ***\n")

    # Read audit CSV
    with open(AUDIT_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    flagged = [r for r in rows if r["needs_conditions"] == "Yes"]
    print(f"Total lessons in audit: {len(rows)}")
    print(f"Lessons flagged for conditions: {len(flagged)}\n")

    for row in flagged:
        lesson_id = row["lesson_id"]
        grade = row["grade"]
        title = row["title"]
        conditions_json = row["all_conditions_json"]

        grade_band = get_grade_band(grade, lesson_id)

        # Generate conditions text
        conditions_text = generate_conditions_text(conditions_json, grade_band, title)
        if not conditions_text:
            print(f"  [SKIP-GEN ] {lesson_id} - Could not generate conditions text")
            stats["skipped"] += 1
            continue

        # Find the lesson file
        filepath = find_lesson_file(lesson_id)
        if not filepath:
            print(f"  [SKIP-FILE] {lesson_id} - File not found")
            stats["skipped"] += 1
            continue

        if dry_run:
            print(f"  [DRY-RUN  ] {lesson_id} ({grade_band}) - {title}")
            stats["updated"] += 1
            continue

        # Insert into Step 4
        result = insert_conditions_into_step4(filepath, conditions_text)
        if result is True:
            relpath = os.path.relpath(filepath, LESSONS_DIR)
            print(f"  [UPDATED  ] {lesson_id} ({grade_band}) - {relpath}")
            stats["updated"] += 1
        elif result is False:
            print(f"  [ALREADY  ] {lesson_id} - Already has conditions")
            stats["already_done"] += 1
        else:
            print(f"  [ERROR    ] {lesson_id} - Could not find Step 4")
            stats["errors"] += 1

    print(f"\n{'=' * 70}")
    print("RESULTS")
    print(f"{'=' * 70}")
    print(f"Updated: {stats['updated']}")
    print(f"Already done: {stats['already_done']}")
    print(f"Skipped: {stats['skipped']}")
    print(f"Errors: {stats['errors']}")


if __name__ == "__main__":
    main()
