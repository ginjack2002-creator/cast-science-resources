#!/usr/bin/env python3
"""
Comprehensive Conditional Relationship Audit
=============================================
Parses all lesson .md files and generates a CSV spreadsheet cataloging:
- All components (name, type)
- All relationships (source → target, +/-)
- Shared targets (2+ inputs to same component)
- Feedback loops (reinforcing/balancing)
- Condition types needed (AMP, MUT, INH, FBG, CAS, 2EX)
- Sub-if-then chains
- Scientific justification for each condition

Output: scripts/output/conditional_audit_report.csv
"""

import os
import re
import csv
import sys
from collections import defaultdict

BASE_DIR = os.path.expanduser("~/cast-science-resources")
LESSONS_DIR = os.path.join(BASE_DIR, "lessons")
OUTPUT_DIR = os.path.join(BASE_DIR, "scripts", "output")


def find_all_lesson_files():
    """Find all .md lesson files recursively."""
    files = []
    for root, dirs, filenames in os.walk(LESSONS_DIR):
        for f in sorted(filenames):
            if f.endswith(".md"):
                files.append(os.path.join(root, f))
    files.sort()
    return files


def parse_lesson_metadata(content):
    """Extract lesson ID, grade, and title from header."""
    lesson_id = ""
    grade = ""
    title = ""

    id_match = re.search(r'\*\*Lesson ID\*\*\s*\|\s*(\S+)', content)
    if id_match:
        lesson_id = id_match.group(1)

    grade_match = re.search(r'\*\*Grade\*\*\s*\|\s*(.+?)(?:\s*\||\s*$)', content, re.MULTILINE)
    if grade_match:
        grade = grade_match.group(1).strip()

    title_match = re.search(r'^# Lesson:\s*(.+)$', content, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()

    return lesson_id, grade, title


def determine_level(filepath, lesson_id):
    """Determine the level (1, 2, 3) from filepath or lesson ID."""
    if "level-3" in filepath or "L3-" in lesson_id:
        return "3"
    elif "level-2" in filepath or "L2-" in lesson_id:
        return "2"
    elif "level-1" in filepath or "L1-" in lesson_id:
        return "1"
    elif "natures-engineers" in filepath:
        # Check lesson ID for level
        if "L2-" in lesson_id:
            return "2"
        elif "L1-" in lesson_id:
            return "1"
        return "1"
    else:
        return "1"  # K-3 and original 4-8 are level 1


def parse_components(content):
    """Extract components from the Component List table."""
    components = {}

    # Find component table
    table_match = re.search(
        r'### Component List.*?\n\n(.*?)(?=\n###|\n---|\n## )',
        content, re.DOTALL
    )
    if not table_match:
        return components

    table_text = table_match.group(1)

    # Parse table rows: | Component | Type | What It Represents |
    for line in table_text.split("\n"):
        line = line.strip()
        if line.startswith("|") and not line.startswith("|-") and "Component" not in line:
            parts = [p.strip() for p in line.split("|")]
            parts = [p for p in parts if p]  # Remove empty strings
            if len(parts) >= 2:
                name = parts[0].strip()
                comp_type = parts[1].strip().lower()
                description = parts[2].strip() if len(parts) >= 3 else ""
                if name and comp_type:
                    components[name] = {
                        "type": "External" if "external" in comp_type else "Internal",
                        "description": description
                    }

    return components


def parse_relationships(content):
    """Extract relationships from Step 2 Task B and Task C."""
    relationships = []

    # Find Step 2 section
    step2_match = re.search(
        r'## Step 2.*?(?=## Step 3|\Z)',
        content, re.DOTALL
    )
    if not step2_match:
        return relationships

    step2_text = step2_match.group(0)

    # Parse relationship descriptions from Task C
    # Pattern: ○ Source → Target = POSITIVE/NEGATIVE (+/-)
    rel_pattern = re.compile(
        r'[○•]\s*(.+?)\s*→\s*(.+?)\s*=\s*(POSITIVE|NEGATIVE)\s*\([+−\-]\)',
        re.IGNORECASE
    )

    for m in rel_pattern.finditer(step2_text):
        source = m.group(1).strip().strip('"\'')
        target = m.group(2).strip().strip('"\'')
        sign = "+" if "positive" in m.group(3).lower() else "-"

        # Get the description (text after the +/- designation, before the next ○ or Task)
        desc_start = m.end()
        desc_end = step2_text.find("○", desc_start)
        if desc_end == -1:
            desc_end = step2_text.find("•", desc_start)
        if desc_end == -1:
            desc_end = step2_text.find("Task", desc_start)
        if desc_end == -1:
            desc_end = min(desc_start + 500, len(step2_text))

        description = step2_text[desc_start:desc_end].strip()
        # Clean up description - get first sentence or two
        description = re.sub(r'\n\s*\n', ' ', description)
        description = re.sub(r'\s+', ' ', description).strip()
        if len(description) > 300:
            description = description[:300] + "..."

        relationships.append({
            "source": source,
            "target": target,
            "sign": sign,
            "description": description
        })

    # Also try to parse from Task B drag instructions as fallback
    if not relationships:
        drag_pattern = re.compile(
            r'Click on ["\']?(.+?)["\']?\s+and drag.*?to ["\']?(.+?)["\']?\s*$',
            re.MULTILINE | re.IGNORECASE
        )
        for m in drag_pattern.finditer(step2_text):
            source = m.group(1).strip().strip('"\'')
            target = m.group(2).strip().strip('"\'')
            relationships.append({
                "source": source,
                "target": target,
                "sign": "?",
                "description": ""
            })

    return relationships


def find_shared_targets(relationships):
    """Find components that receive 2+ input arrows."""
    target_sources = defaultdict(list)
    for rel in relationships:
        target_sources[rel["target"]].append(rel)

    shared = {}
    for target, rels in target_sources.items():
        if len(rels) >= 2:
            shared[target] = rels

    return shared


def find_feedback_loops(relationships):
    """Detect cycles in the relationship graph using DFS."""
    # Build adjacency list
    graph = defaultdict(list)
    edge_signs = {}
    for rel in relationships:
        graph[rel["source"]].append(rel["target"])
        edge_signs[(rel["source"], rel["target"])] = rel["sign"]

    loops = []
    all_nodes = set()
    for rel in relationships:
        all_nodes.add(rel["source"])
        all_nodes.add(rel["target"])

    # DFS for each node
    for start in all_nodes:
        visited = set()
        stack = [(start, [start])]
        while stack:
            node, path = stack.pop()
            for neighbor in graph.get(node, []):
                if neighbor == start and len(path) > 1:
                    # Found a cycle
                    cycle = path + [neighbor]
                    # Determine if reinforcing or balancing
                    neg_count = 0
                    for i in range(len(cycle) - 1):
                        sign = edge_signs.get((cycle[i], cycle[i+1]), "?")
                        if sign == "-":
                            neg_count += 1
                    # Even number of negatives = reinforcing, odd = balancing
                    loop_type = "Balancing (-)" if neg_count % 2 == 1 else "Reinforcing (+)"

                    # Normalize cycle (start from alphabetically first)
                    cycle_nodes = cycle[:-1]  # Remove duplicate end node
                    min_idx = cycle_nodes.index(min(cycle_nodes))
                    normalized = cycle_nodes[min_idx:] + cycle_nodes[:min_idx]

                    loop_key = " → ".join(normalized) + " → " + normalized[0]
                    if loop_key not in [l["path"] for l in loops]:
                        loops.append({
                            "path": loop_key,
                            "type": loop_type,
                            "components": normalized,
                            "neg_count": neg_count
                        })
                elif neighbor not in visited and len(path) < 10:
                    visited.add(neighbor)
                    stack.append((neighbor, path + [neighbor]))

    return loops


def determine_conditions(components, relationships, shared_targets, feedback_loops):
    """Determine what conditions are needed based on scientific analysis."""
    conditions = []

    for target, input_rels in shared_targets.items():
        target_type = components.get(target, {}).get("type", "Unknown")

        # Classify each input
        external_inputs = []
        internal_inputs = []

        for rel in input_rels:
            src_type = components.get(rel["source"], {}).get("type", "Unknown")
            if src_type == "External":
                external_inputs.append(rel)
            else:
                internal_inputs.append(rel)

        # Determine condition type based on input pattern
        if len(external_inputs) >= 2:
            # Two externals → same target: 2EX pattern
            # Usually one is the primary cause, the other is the amplifier
            for i, ext_rel in enumerate(external_inputs):
                other_rels = [r for j, r in enumerate(external_inputs) if j != i]
                other_names = [r["source"] for r in other_rels]

                # Heuristic: the one with positive sign is more likely the amplifier
                # The one with negative sign is more likely the primary (inverse) cause
                # But both may need conditions on each other
                for other in other_rels:
                    conditions.append({
                        "connection": f"{ext_rel['source']} → {target}",
                        "type": "2EX",
                        "condition_text": f"IF {other['source']} is ON" if other["sign"] == "+" else f"IF {other['source']} is OFF",
                        "scientific_justification": (
                            f"{ext_rel['source']} only affects {target} when "
                            f"{other['source']} creates the right conditions. "
                            f"Without {other['source']}, {ext_rel['source']} alone "
                            f"cannot drive {target}."
                        ),
                        "sign": ext_rel["sign"]
                    })

        if len(external_inputs) >= 1 and len(internal_inputs) >= 1:
            # External + Internal → same target: AMP pattern
            for ext_rel in external_inputs:
                for int_rel in internal_inputs:
                    # External amplifies the internal's effect
                    conditions.append({
                        "connection": f"{ext_rel['source']} → {target}",
                        "type": "AMP",
                        "condition_text": f"IF {int_rel['source']} is ON",
                        "scientific_justification": (
                            f"{ext_rel['source']} amplifies the effect on {target}, "
                            f"but only when {int_rel['source']} is active. "
                            f"Without {int_rel['source']}, {ext_rel['source']} alone "
                            f"cannot cause changes in {target}."
                        ),
                        "sign": ext_rel["sign"]
                    })

        if len(internal_inputs) >= 2:
            # Two internals → same target: MUT pattern
            for i, int_rel in enumerate(internal_inputs):
                others = [r for j, r in enumerate(internal_inputs) if j != i]
                for other in others:
                    conditions.append({
                        "connection": f"{int_rel['source']} → {target}",
                        "type": "MUT",
                        "condition_text": f"IF {other['source']} is ON",
                        "scientific_justification": (
                            f"{int_rel['source']} and {other['source']} both affect "
                            f"{target}, but {int_rel['source']}'s effect depends on "
                            f"{other['source']} being active in the system."
                        ),
                        "sign": int_rel["sign"]
                    })

    # Check for feedback loop gates
    for loop in feedback_loops:
        if loop["type"] == "Reinforcing (+)":
            # In reinforcing loops, at least one connection may need a gate
            loop_components = loop["components"]
            for i in range(len(loop_components)):
                src = loop_components[i]
                tgt = loop_components[(i + 1) % len(loop_components)]
                # Check if this connection has external enablers
                for rel in relationships:
                    if rel["source"] != src and rel["target"] == tgt:
                        # External input to a loop node
                        src_type = components.get(rel["source"], {}).get("type", "Unknown")
                        if src_type == "External":
                            conditions.append({
                                "connection": f"{src} → {tgt} (feedback loop)",
                                "type": "FBG",
                                "condition_text": f"IF {rel['source']} meets threshold",
                                "scientific_justification": (
                                    f"The reinforcing loop {loop['path']} is gated by "
                                    f"{rel['source']}. The loop only activates when "
                                    f"{rel['source']} creates enabling conditions."
                                ),
                                "sign": "loop"
                            })

    # Deduplicate conditions
    seen = set()
    unique_conditions = []
    for c in conditions:
        key = (c["connection"], c["condition_text"])
        if key not in seen:
            seen.add(key)
            unique_conditions.append(c)

    return unique_conditions


def find_sub_if_thens(conditions, relationships, components):
    """Identify nested conditional chains."""
    sub_chains = []

    # For each condition, check if the condition component is itself conditional
    condition_targets = set()
    for c in conditions:
        # Extract the condition component name
        match = re.search(r'IF (.+?) is', c["condition_text"])
        if match:
            condition_targets.add(match.group(1))

    for comp_name in condition_targets:
        # Is this component the TARGET of another relationship?
        upstream = [r for r in relationships if r["target"] == comp_name]
        if upstream:
            chain_parts = []
            for up in upstream:
                chain_parts.append(f"{up['source']} ({up['sign']})→ {comp_name}")

            # Find which conditions depend on this component
            dependent_conditions = [
                c for c in conditions
                if comp_name in c["condition_text"]
            ]

            for dc in dependent_conditions:
                sub_chains.append(
                    f"{dc['connection']}: {dc['condition_text']}, "
                    f"BUT {comp_name} depends on: {'; '.join(chain_parts)}"
                )

    return sub_chains


def process_lesson(filepath):
    """Process a single lesson file and return audit data."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lesson_id, grade, title = parse_lesson_metadata(content)
    level = determine_level(filepath, lesson_id)
    components = parse_components(content)
    relationships = parse_relationships(content)

    if not components or not relationships:
        return None

    shared_targets = find_shared_targets(relationships)
    feedback_loops = find_feedback_loops(relationships)
    conditions = determine_conditions(components, relationships, shared_targets, feedback_loops)
    sub_if_thens = find_sub_if_thens(conditions, relationships, components)

    # Count component types
    ext_count = sum(1 for c in components.values() if c["type"] == "External")
    int_count = sum(1 for c in components.values() if c["type"] == "Internal")

    # Format relationships
    rel_str = "; ".join([
        f"{r['source']} ({r['sign']})→ {r['target']}"
        for r in relationships
    ])

    # Format shared targets
    shared_str = "; ".join([
        f"{target} ← [{', '.join(r['source'] for r in rels)}]"
        for target, rels in shared_targets.items()
    ])

    # Format feedback loops
    loop_str = "; ".join([
        f"{l['type']}: {l['path']}"
        for l in feedback_loops
    ]) if feedback_loops else "None"

    # Format conditions (up to 3)
    cond_data = []
    for i in range(3):
        if i < len(conditions):
            c = conditions[i]
            cond_data.append({
                "connection": c["connection"],
                "type": c["type"],
                "condition_text": c["condition_text"],
                "justification": c["scientific_justification"]
            })
        else:
            cond_data.append({
                "connection": "",
                "type": "",
                "condition_text": "",
                "justification": ""
            })

    # Sub-if-thens
    sub_str = "; ".join(sub_if_thens) if sub_if_thens else "None"

    # Has conditions needed?
    needs_conditions = len(conditions) > 0

    return {
        "lesson_id": lesson_id,
        "grade": grade,
        "level": level,
        "title": title,
        "total_components": len(components),
        "external_count": ext_count,
        "internal_count": int_count,
        "relationships": rel_str,
        "shared_targets": shared_str,
        "has_shared_targets": "Yes" if shared_targets else "No",
        "feedback_loops": loop_str,
        "has_feedback_loops": "Yes" if feedback_loops else "No",
        "needs_conditions": "Yes" if needs_conditions else "No",
        "total_conditions": len(conditions),
        "condition_1_connection": cond_data[0]["connection"],
        "condition_1_type": cond_data[0]["type"],
        "condition_1_text": cond_data[0]["condition_text"],
        "condition_1_justification": cond_data[0]["justification"],
        "condition_2_connection": cond_data[1]["connection"],
        "condition_2_type": cond_data[1]["type"],
        "condition_2_text": cond_data[1]["condition_text"],
        "condition_2_justification": cond_data[1]["justification"],
        "condition_3_connection": cond_data[2]["connection"],
        "condition_3_type": cond_data[2]["type"],
        "condition_3_text": cond_data[2]["condition_text"],
        "condition_3_justification": cond_data[2]["justification"],
        "sub_if_thens": sub_str,
        "all_conditions_json": str(conditions),  # Full data for batch script
    }


def main():
    print("=" * 70)
    print("COMPREHENSIVE CONDITIONAL RELATIONSHIP AUDIT")
    print("=" * 70)

    files = find_all_lesson_files()
    print(f"\nFound {len(files)} lesson files\n")

    results = []
    skipped = 0

    for filepath in files:
        relpath = os.path.relpath(filepath, LESSONS_DIR)
        result = process_lesson(filepath)
        if result:
            results.append(result)
            status = "CONDITIONS" if result["needs_conditions"] == "Yes" else "simple"
            print(f"  [{status:10s}] {relpath}")
        else:
            skipped += 1
            print(f"  [SKIP      ] {relpath}")

    # Write CSV
    output_path = os.path.join(OUTPUT_DIR, "conditional_audit_report.csv")
    fieldnames = [
        "lesson_id", "grade", "level", "title",
        "total_components", "external_count", "internal_count",
        "relationships", "shared_targets", "has_shared_targets",
        "feedback_loops", "has_feedback_loops",
        "needs_conditions", "total_conditions",
        "condition_1_connection", "condition_1_type", "condition_1_text", "condition_1_justification",
        "condition_2_connection", "condition_2_type", "condition_2_text", "condition_2_justification",
        "condition_3_connection", "condition_3_type", "condition_3_text", "condition_3_justification",
        "sub_if_thens", "all_conditions_json"
    ]

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            writer.writerow(r)

    # Print summary
    needs_cond = [r for r in results if r["needs_conditions"] == "Yes"]
    has_loops = [r for r in results if r["has_feedback_loops"] == "Yes"]

    print(f"\n{'=' * 70}")
    print("SUMMARY")
    print(f"{'=' * 70}")
    print(f"Total lessons processed: {len(results)} (skipped: {skipped})")
    print(f"Lessons needing conditions: {len(needs_cond)}")
    print(f"Lessons with feedback loops: {len(has_loops)}")

    # Breakdown by grade band
    grade_bands = {
        "K-3": [], "4-8 L1": [], "4-8 L2": [],
        "9-12 L1": [], "9-12 L2": [], "9-12 L3": [],
        "NE": []
    }

    for r in results:
        g = r["grade"].lower()
        lid = r["lesson_id"]
        level = r["level"]

        if "natures" in g or lid.startswith("NE"):
            band = "NE"
        elif any(x in g for x in ["kinder", "1st", "2nd", "3rd"]) or lid[:3] in ["GK-", "G01", "G02", "G03"]:
            band = "K-3"
        elif any(x in g for x in ["4th", "5th", "6th", "7th", "8th"]) or lid[:3] in ["G04", "G05", "G06", "G07", "G08"]:
            band = f"4-8 L{level}"
        elif any(x in g for x in ["9th", "10th", "11th", "12th"]) or lid[:3] in ["G09", "G10", "G11", "G12"]:
            band = f"9-12 L{level}"
        else:
            band = "K-3"  # fallback

        if band in grade_bands:
            grade_bands[band].append(r)

    print(f"\nBy grade band:")
    for band, lessons in grade_bands.items():
        total = len(lessons)
        with_cond = sum(1 for l in lessons if l["needs_conditions"] == "Yes")
        with_loops = sum(1 for l in lessons if l["has_feedback_loops"] == "Yes")
        print(f"  {band:10s}: {with_cond}/{total} need conditions, {with_loops} have feedback loops")

    # Condition type breakdown
    type_counts = defaultdict(int)
    for r in needs_cond:
        for i in range(1, 4):
            t = r.get(f"condition_{i}_type", "")
            if t:
                type_counts[t] += 1

    print(f"\nCondition types found:")
    type_names = {
        "AMP": "Amplifier + Prerequisite",
        "MUT": "Mutual Prerequisite",
        "INH": "Inhibitor Override (UNLESS)",
        "FBG": "Feedback Loop Gate",
        "CAS": "Cascade Enable",
        "2EX": "2 External -> 1 Internal"
    }
    for code, count in sorted(type_counts.items()):
        name = type_names.get(code, code)
        print(f"  {code}: {count} ({name})")

    print(f"\nCSV report saved to: {output_path}")
    print(f"Open in Excel/Google Sheets for full review.")


if __name__ == "__main__":
    main()
