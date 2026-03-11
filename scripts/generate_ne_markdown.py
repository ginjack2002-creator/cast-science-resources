#!/usr/bin/env python3
"""Generate markdown lesson files for Nature's Engineers series."""
import sys
import os
import re

# Add scripts dir to path so we can import the data
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lesson_data_natures_engineers import (
    L1_01, L1_02, L1_03, L1_04, L1_05, L1_06,
    L2_01, L2_02, L2_03, L2_04, L2_05, L2_06
)

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "lessons", "natures-engineers")

def slugify(title):
    """Convert title to URL-friendly slug."""
    s = title.lower()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'[\s]+', '-', s.strip())
    s = re.sub(r'-+', '-', s)
    return s

def fmt_grade(lesson):
    """Determine grade band from NGSS codes."""
    ngss = lesson["ngss"]
    if any(x in ngss for x in ["HS-", "hs-"]):
        return "High School (9-12)"
    elif any(x in ngss for x in ["MS-", "ms-"]):
        return "Middle School (6-8)"
    elif any(x.startswith(("6-","7-","8-")) for x in ngss.split(",")):
        return "Middle School (6-8)"
    elif any(x.strip().startswith(("3-","4-","5-")) for x in ngss.split(",")):
        return "Upper Elementary (3-5)"
    else:
        return "Elementary/Middle School"

def generate_markdown(lesson):
    """Generate full markdown for a lesson."""
    lid = lesson["id"]
    title = lesson["title"]
    subtitle = lesson["subtitle"]
    grade = fmt_grade(lesson)

    # Build vocabulary table
    vocab_rows = ""
    for term, defn in lesson["vocabulary"]:
        vocab_rows += f"| **{term}** | {defn} |\n"

    # Build components table
    comp_rows = ""
    for comp in lesson["components"]:
        name, desc, is_ext = comp[0], comp[1], comp[2]
        ctype = "External" if is_ext else "Internal"
        comp_rows += f"| {name} | {ctype} | {desc} |\n"

    # Build relationships section
    rel_lines = ""
    for rel in lesson["relationships"]:
        rel_name, rel_dir, rel_desc = rel[0], rel[1], rel[2]
        rel_lines += f"- **{rel_name}** = {rel_dir}\n  {rel_desc}\n\n"

    # Build scenarios section
    scen_lines = ""
    for i, sc in enumerate(lesson["sim_scenarios"]):
        name, settings, prediction_q = sc[0], sc[1], sc[2]
        scen_lines += f"**Scenario {i+1}: {name}**\n"
        scen_lines += f"- Settings: {settings}\n"
        scen_lines += f"- Prediction Question: {prediction_q}\n\n"

    # Build discoveries
    disc_lines = ""
    for d in lesson["discoveries"]:
        disc_lines += f"- {d}\n"

    # Build learning objectives
    obj_lines = ""
    for o in lesson["objectives"]:
        obj_lines += f"- {o}\n"

    # Build STEM challenge questions
    stem_q_lines = ""
    for q in lesson["stem_questions"]:
        stem_q_lines += f"- {q}\n"

    # Game section
    game = lesson.get("game", {})
    game_section = ""
    if game:
        game_section = f"""## Game: {game['title']}

**Type:** {game['type']}

{game['description']}

**Materials:**
"""
        for m in game.get("materials", []):
            game_section += f"- {m}\n"
        game_section += f"\n**Learning Connection:** {game.get('learning_connection', '')}\n"

    # STEAM activity section
    steam = lesson.get("steam_activity", {})
    steam_section = ""
    if steam:
        steam_section = f"""## STEAM Activity: {steam['title']}

**Type:** {steam['type']}

{steam['description']}

**Materials:**
"""
        for m in steam.get("materials", []):
            steam_section += f"- {m}\n"
        steam_section += f"\n**Learning Connection:** {steam.get('learning_connection', '')}\n"

    # Career section
    career = lesson.get("career", "")

    md = f"""# {title}

## {subtitle}

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | {lid} |
| **Grade Band** | {grade} |
| **Series** | Nature's Engineers |
| **Lesson Name** | {title} |
| **Status** | Template |

---

## Overview

### Big Question
**{lesson['big_question']}**

### NGSS Standards
**{lesson['ngss']}**: {lesson['ngss_desc']}

### Learning Objectives
{obj_lines}
---

## Vocabulary

| Term | Definition |
|------|-----------|
{vocab_rows}
---

## Model Components

| Component | Type | What It Represents |
|-----------|------|-------------------|
{comp_rows}
---

## Think About It

> {lesson['think_about_it']}

---

## Relationships

{rel_lines}
---

## Scenarios

{scen_lines}
---

## Key Discoveries

{disc_lines}
---

## Answer to Big Question

{lesson['answer']}

---

## STEM Challenge: {lesson['stem_title']}

**Mission:** {lesson['stem_mission']}

**Scenario:** {lesson['stem_scenario']}

**Guiding Questions:**
{stem_q_lines}
---

{game_section}
---

{steam_section}
---

## Career Connection

{career}

---

## Lesson Metadata

| Field | Value |
|-------|-------|
| Created | March 2026 |
| Author | Alexandria's Design |
| Series | Nature's Engineers |
| Platform | ModelIt (formerly Cell Collective) |
| Estimated Time | 35-45 minutes |
| Can Split Across | 2 class periods |
"""
    return md


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    lessons = [
        L1_01, L1_02, L1_03, L1_04, L1_05, L1_06,
        L2_01, L2_02, L2_03, L2_04, L2_05, L2_06
    ]

    for lesson in lessons:
        lid = lesson["id"]
        title = lesson["title"]
        slug = slugify(title)
        filename = f"{lid}-{slug}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)

        md = generate_markdown(lesson)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Created: {filename}")

    print(f"\nDone! {len(lessons)} lesson files created in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
