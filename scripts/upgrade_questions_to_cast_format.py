#!/usr/bin/env python3
"""
Upgrade all lesson markdown files to use proper CAST stimulus-response format.
Reads existing lesson content and question data, generates CAST-formatted questions
with alignment tags, stimulus paragraphs, per-answer feedback, and cognitive levels.
Replaces the old simple MC section in each lesson .md file.
"""

import os
import re
import sys
import glob
import importlib.util

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
LESSONS_DIR = os.path.join(os.path.dirname(SCRIPTS_DIR), "lessons")

# ============================================================
# Load question data
# ============================================================

def load_all_questions():
    all_q = {}
    for filepath in sorted(glob.glob(os.path.join(SCRIPTS_DIR, "lesson_questions_*.py"))):
        filename = os.path.basename(filepath)
        mod_name = filename[:-3]
        try:
            spec = importlib.util.spec_from_file_location(mod_name, filepath)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            if hasattr(mod, "ALL_QUESTIONS"):
                for lid, qs in mod.ALL_QUESTIONS.items():
                    all_q[lid] = qs
        except Exception as e:
            print(f"  ERROR loading {filename}: {e}")
    return all_q


def load_lesson_data():
    """Load lesson data dictionaries for component/relationship info."""
    all_data = {}
    for filepath in sorted(glob.glob(os.path.join(SCRIPTS_DIR, "lesson_data_*.py"))):
        filename = os.path.basename(filepath)
        mod_name = filename[:-3]
        try:
            spec = importlib.util.spec_from_file_location(mod_name, filepath)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            # Collect all lesson dicts from module-level variables
            for attr_name in dir(mod):
                obj = getattr(mod, attr_name)
                if isinstance(obj, dict) and "id" in obj and "title" in obj:
                    all_data[obj["id"]] = obj
                elif isinstance(obj, list):
                    for item in obj:
                        if isinstance(item, dict) and "id" in item and "title" in item:
                            all_data[item["id"]] = item
        except Exception:
            pass
    return all_data


# ============================================================
# Extract metadata from markdown
# ============================================================

def extract_lesson_id(content):
    match = re.search(r'\*\*Lesson ID\*\*\s*\|\s*(\S+)', content)
    if match:
        return match.group(1).strip()
    return None


def extract_ngss(content):
    match = re.search(r'### NGSS Standard\s*\n\*\*([^*]+)\*\*', content)
    if match:
        return match.group(1).strip()
    match = re.search(r'NGSS.*?\|\s*(\S+-\S+-\d+)', content)
    if match:
        return match.group(1).strip()
    return "NGSS Standard"


def extract_title(content):
    match = re.search(r'^# (.+)', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return "Lesson"


def extract_components(content):
    """Extract component names and types from the Component List table."""
    components = []
    in_table = False
    for line in content.split("\n"):
        if "Component" in line and "Type" in line and "What It Represents" in line:
            in_table = True
            continue
        if in_table:
            if line.startswith("|") or ("|" in line and "---" not in line):
                parts = [p.strip() for p in line.split("|") if p.strip()]
                if len(parts) >= 2 and parts[0] != "---" and "---" not in parts[0]:
                    comp_name = parts[0]
                    comp_type = parts[1] if len(parts) > 1 else ""
                    components.append((comp_name, comp_type))
            elif line.strip() == "":
                if components:
                    break
    return components


def extract_relationships(content):
    """Extract relationships from Step 2 content."""
    relationships = []
    # Look for patterns like "Rainfall → Dry Vegetation = NEGATIVE" or "positive"
    pattern = r'["""]?(\w[\w\s]*?)["""]?\s*(?:→|->|to)\s*["""]?(\w[\w\s]*?)["""]?\s*=\s*(POSITIVE|NEGATIVE|positive|negative|\+|\-|pos|neg)'
    for match in re.finditer(pattern, content):
        source = match.group(1).strip()
        target = match.group(2).strip()
        rel_type = match.group(3).strip().upper()
        if rel_type in ("+", "POS"):
            rel_type = "POSITIVE"
        elif rel_type in ("-", "NEG"):
            rel_type = "NEGATIVE"
        relationships.append((source, target, rel_type))
    return relationships


# ============================================================
# SEP/DCI/CCC Mapping
# ============================================================

# CAST SEP codes for modeling
SEP_CODES = [
    ("SEP 2.1.1", "Determine components of a system"),
    ("SEP 2.1.2", "Determine relationships among components"),
    ("SEP 2.1.3", "Evaluate a model's accuracy"),
    ("SEP 2.1.4", "Represent mechanisms to explain/predict events"),
    ("SEP 2.1.5", "Apply a model to make predictions"),
]

# Common CCC codes
CCC_MAP = {
    "cause": ("CCC2", "Cause and Effect"),
    "system": ("CCC4", "Systems and System Models"),
    "energy": ("CCC5", "Energy and Matter"),
    "pattern": ("CCC1", "Patterns"),
    "scale": ("CCC3", "Scale, Proportion, and Quantity"),
    "structure": ("CCC6", "Structure and Function"),
    "stability": ("CCC7", "Stability and Change"),
}

# Cognitive levels
COG_LEVELS = [
    "Identify",
    "Reason",
    "Reason",
    "Reason + Evidence",
    "Predict + Apply",
]


def get_dci_from_ngss(ngss):
    """Extract DCI code from NGSS standard string like '5-ESS2-1'."""
    match = re.match(r'(?:\d+|K|HS)-([A-Z]+\d+[A-Za-z]*)-(\d+)', ngss)
    if match:
        domain = match.group(1)
        num = match.group(2)
        return f"{domain}.{num}"
    return ngss


# ============================================================
# Generate CAST-format questions
# ============================================================

def generate_cast_section(lesson_id, ngss, title, components, relationships, questions, content):
    """Generate a complete CAST-Aligned Pre/Post Assessment section."""

    # Use post-assessment questions as the basis (they test lesson content)
    post_qs = questions.get("mc_post_assessment", [])
    pre_qs = questions.get("mc_pre_assessment", [])

    # Combine: take up to 5 questions, preferring post then pre
    combined = post_qs[:5]
    if len(combined) < 5:
        for q in pre_qs:
            if len(combined) >= 5:
                break
            # Don't duplicate
            if q["question"] not in [c["question"] for c in combined]:
                combined.append(q)

    # Pad to 5 if needed
    num_qs = min(5, len(combined))
    if num_qs == 0:
        return None

    dci_code = get_dci_from_ngss(ngss)

    # Build external/internal component lists for stimulus context
    ext_comps = [c[0] for c in components if c[1].lower() in ("external", "ext")]
    int_comps = [c[0] for c in components if c[1].lower() in ("internal", "int")]

    lines = []
    lines.append("## CAST-Aligned Pre/Post Assessment")
    lines.append("")
    lines.append("### Administration Instructions")
    lines.append("")
    lines.append(f"These {num_qs} multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of {num_qs}. Learning growth = post-score minus pre-score.")
    lines.append("")
    lines.append(f"Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to {ngss}.")
    lines.append("")
    lines.append("---")
    lines.append("")

    for i, q in enumerate(combined[:num_qs]):
        sep_code, sep_desc = SEP_CODES[min(i, len(SEP_CODES) - 1)]

        # Pick appropriate CCC based on question content
        q_lower = q["question"].lower()
        ccc_code, ccc_desc = "CCC4", "Systems and System Models"
        for keyword, (code, desc) in CCC_MAP.items():
            if keyword in q_lower:
                ccc_code, ccc_desc = code, desc
                break

        cog_level = COG_LEVELS[min(i, len(COG_LEVELS) - 1)]

        lines.append(f"### Question {i + 1}")
        lines.append("")
        lines.append(f"CAST Alignment: {sep_code} ({sep_desc}) + DCI {dci_code} + {ccc_code} ({ccc_desc})")
        lines.append("")

        # Generate stimulus paragraph from lesson context
        stimulus = _generate_stimulus(i, q, lesson_id, title, components, relationships, ext_comps, int_comps)
        lines.append(stimulus)
        lines.append("")

        # Question stem
        lines.append(q["question"])
        lines.append("")

        # Choices
        for letter in ["A", "B", "C", "D"]:
            if letter in q.get("choices", {}):
                lines.append(f"{letter}. {q['choices'][letter]}")
        lines.append("")

        lines.append(f"Correct Answer: {q['correct']}")
        lines.append("")

        # Build per-answer feedback
        correct_letter = q["correct"]
        feedback_correct = q.get("feedback_correct", "Correct!")
        feedback_incorrect = q.get("feedback_incorrect", "")

        feedback_parts = [feedback_correct]
        for letter in ["A", "B", "C", "D"]:
            if letter in q.get("choices", {}) and letter != correct_letter:
                wrong_text = q["choices"][letter]
                feedback_parts.append(f"If you chose {letter}, {_explain_wrong(letter, wrong_text, q, correct_letter)}")

        lines.append(f"Feedback: {' '.join(feedback_parts)}")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Answer Key
    lines.append("### Answer Key")
    lines.append("")
    for i, q in enumerate(combined[:num_qs]):
        sep_code, sep_desc = SEP_CODES[min(i, len(SEP_CODES) - 1)]
        q_lower = q["question"].lower()
        ccc_code = "CCC4"
        for keyword, (code, _) in CCC_MAP.items():
            if keyword in q_lower:
                ccc_code = code
                break
        cog_level = COG_LEVELS[min(i, len(COG_LEVELS) - 1)]
        dci = dci_code
        lines.append(f"Question {i + 1}: {q['correct']} (Cognitive Level: {cog_level} — {sep_code}, DCI {dci}, {ccc_code})")
    lines.append("")

    return "\n".join(lines)


def _generate_stimulus(idx, q, lesson_id, title, components, relationships, ext_comps, int_comps):
    """Generate a stimulus paragraph based on question index and lesson context."""
    comp_names = [c[0] for c in components]
    comp_str = ", ".join(comp_names) if comp_names else "the system components"
    ext_str = ", ".join(ext_comps) if ext_comps else "external factors"
    int_str = ", ".join(int_comps) if int_comps else "internal factors"

    rel_descriptions = []
    for src, tgt, rtype in relationships:
        direction = "increases" if rtype == "POSITIVE" else "decreases"
        rel_descriptions.append(f"when {src} increases, {tgt} {direction}")

    if idx == 0:
        return f"A student is using the ModelIt platform to study the system in this lesson. The model includes these components: {comp_str}. Some components are external ({ext_str}) and some are internal ({int_str}). The student needs to understand what each component represents and how they are organized."
    elif idx == 1:
        rel_text = "; ".join(rel_descriptions[:2]) if rel_descriptions else "components affect each other through positive and negative relationships"
        return f"In the computational model for this lesson, a student draws arrows between components to show relationships. The model shows that {rel_text}. The student is trying to understand why these relationships are positive or negative."
    elif idx == 2:
        rel_text = " and ".join(rel_descriptions[:3]) if rel_descriptions else "components interact through cause-and-effect chains"
        return f"A student runs a simulation of the model. The model shows that {rel_text}. The student changes one variable to see how the whole system responds."
    elif idx == 3:
        return f"Scientists are studying data related to this system. They collected observations over time and noticed patterns in how the components change. The data shows how changes in one part of the system cascade through the other parts."
    else:
        return f"A team wants to use the model to solve a real-world problem related to this system. They know they cannot control the external components ({ext_str}), but they can take action on internal components ({int_str}). They need to decide which action would be most effective based on what the model shows."


def _explain_wrong(letter, wrong_text, q, correct_letter):
    """Generate a brief explanation for why a wrong answer is incorrect."""
    correct_text = q.get("choices", {}).get(correct_letter, "")
    wrong_lower = wrong_text.lower()

    # Generate specific explanations based on wrong answer content
    if any(w in wrong_lower for w in ["destroy", "disappear", "gone", "lost", "nothing"]):
        return "this reflects a common misconception. Matter cannot be created or destroyed — it can only change form. The total amount of matter in the system stays the same."
    elif any(w in wrong_lower for w in ["more", "increase", "extra", "heavier", "bigger"]):
        return "this answer suggests something is being added to the system. Look carefully at the model — the total amount stays the same even when components change. The system is conserving matter or energy."
    elif any(w in wrong_lower for w in ["no ", "not ", "none", "independent", "unrelated"]):
        return "the model shows these components ARE connected. When one changes, it affects the others through the relationships (positive or negative) that you mapped in the model."
    elif any(w in wrong_lower for w in ["random", "depends", "sometimes", "maybe"]):
        return "the model shows a clear, predictable pattern. The relationships between components are consistent — they always work the same way when conditions change."
    elif any(w in wrong_lower for w in ["external", "outside", "control"]):
        return "look at whether this is an external component (we can't control it) or an internal component (it changes based on other things in the system). The model makes this distinction clear."
    else:
        return f"look at the evidence from the model. The correct answer ({correct_letter}) is supported by the relationships between components. This answer does not match what the simulation data shows."


# ============================================================
# Replace section in markdown file
# ============================================================

def replace_cast_section(filepath, new_section):
    """Replace the CAST assessment section in a lesson markdown file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the CAST section
    cast_start = content.find("## CAST-Aligned Pre/Post Assessment")
    if cast_start == -1:
        return False, "No CAST section found"

    # Find the next ## section after CAST (should be Resources)
    after_cast = content[cast_start + 1:]
    next_section = re.search(r'\n## (?!CAST)', after_cast)
    if next_section:
        cast_end = cast_start + 1 + next_section.start()
    else:
        cast_end = len(content)

    # Build new content
    new_content = content[:cast_start] + new_section + "\n\n" + content[cast_end:].lstrip("\n")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True, "OK"


# ============================================================
# Main
# ============================================================

def main():
    dry_run = "--dry-run" in sys.argv

    print("Loading question data...")
    all_questions = load_all_questions()
    print(f"  {len(all_questions)} lessons with questions")

    print("Loading lesson data...")
    all_lesson_data = load_lesson_data()
    print(f"  {len(all_lesson_data)} lesson data entries")

    lesson_files = sorted(glob.glob(os.path.join(LESSONS_DIR, "**", "*.md"), recursive=True))
    print(f"Found {len(lesson_files)} lesson files\n")

    # Skip the exemplar
    exemplar = "G05-L01-when-trees-become-matches.md"

    stats = {"ok": 0, "skip": 0, "error": 0}

    for filepath in lesson_files:
        rel_path = os.path.relpath(filepath, LESSONS_DIR)
        basename = os.path.basename(filepath)

        if basename == exemplar:
            print(f"  {rel_path}: SKIP (exemplar)")
            stats["skip"] += 1
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        lesson_id = extract_lesson_id(content)
        if not lesson_id:
            print(f"  {rel_path}: SKIP (no lesson ID)")
            stats["skip"] += 1
            continue

        questions = all_questions.get(lesson_id)
        if not questions:
            print(f"  {rel_path}: SKIP (no questions for {lesson_id})")
            stats["skip"] += 1
            continue

        ngss = extract_ngss(content)
        title = extract_title(content)
        components = extract_components(content)
        relationships = extract_relationships(content)

        # Also try lesson data for components/relationships
        ld = all_lesson_data.get(lesson_id, {})
        if not components and "components" in ld:
            for c in ld["components"]:
                comp_type = "External" if c[2] else "Internal"
                components.append((c[0], comp_type))
        if not relationships and "relationships" in ld:
            for r in ld["relationships"]:
                rel_type = "POSITIVE" if "+" in r[1] else "NEGATIVE"
                parts = r[0].split(" to ")
                if len(parts) == 2:
                    relationships.append((parts[0].strip(), parts[1].strip(), rel_type))

        new_section = generate_cast_section(lesson_id, ngss, title, components, relationships, questions, content)
        if not new_section:
            print(f"  {rel_path}: SKIP (empty section for {lesson_id})")
            stats["skip"] += 1
            continue

        if not dry_run:
            ok, msg = replace_cast_section(filepath, new_section)
            if ok:
                print(f"  {rel_path}: OK ({lesson_id})")
                stats["ok"] += 1
            else:
                print(f"  {rel_path}: ERROR - {msg}")
                stats["error"] += 1
        else:
            print(f"  {rel_path}: WOULD UPDATE ({lesson_id})")
            stats["ok"] += 1

    print(f"\n{'='*60}")
    print(f"Updated: {stats['ok']}")
    print(f"Skipped: {stats['skip']}")
    print(f"Errors:  {stats['error']}")
    if dry_run:
        print("DRY RUN — no files modified")


if __name__ == "__main__":
    main()
