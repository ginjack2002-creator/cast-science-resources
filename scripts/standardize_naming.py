#!/usr/bin/env python3
"""
Standardize Grades 4-8 Naming Convention to Match Grades 9-12
=============================================================

Grades 9-12 structure:
  lessons/grade-09/level-1/G09L1-L01-slug.md
  materials/grade-09/level-1/G09L1-L01/G09L1-L01-*.ext

Grades 4-8 CURRENT structure:
  lessons/grade-04/G04-L01-slug.md          (original/level-1)
  lessons/grade-04/G04-L2-01-slug.md        (level 2)
  materials/grade-04/G04-L01/G04-L01-*.ext  (original/level-1)
  materials/grade-04/level-2/G04L2-L01/...  (level 2 - already correct!)

Grades 4-8 TARGET structure:
  lessons/grade-04/level-1/G04L1-L01-slug.md
  lessons/grade-04/level-2/G04L2-L01-slug.md
  materials/grade-04/level-1/G04L1-L01/G04L1-L01-*.ext
  materials/grade-04/level-2/G04L2-L01/...  (unchanged)

Changes:
1. Create level-1/ and level-2/ subdirs in lessons/grade-0X/
2. Move & rename lesson files
3. Create level-1/ in materials/grade-0X/
4. Move & rename materials folders and files
5. Update internal Lesson IDs and resource paths in lesson markdown files
"""

import os
import re
import shutil
import sys

BASE_DIR = os.path.expanduser("~/cast-science-resources")
LESSONS_DIR = os.path.join(BASE_DIR, "lessons")
MATERIALS_DIR = os.path.join(BASE_DIR, "materials")

GRADES = ["04", "05", "06", "07", "08"]

dry_run = "--dry-run" in sys.argv
stats = {"lessons_moved": 0, "materials_moved": 0, "files_renamed": 0, "content_updated": 0}


def log(msg):
    print(f"  {msg}")


def ensure_dir(path):
    if dry_run:
        log(f"[DRY] mkdir: {os.path.relpath(path, BASE_DIR)}")
    else:
        os.makedirs(path, exist_ok=True)


def move_file(src, dst):
    if dry_run:
        log(f"[DRY] move: {os.path.relpath(src, BASE_DIR)} -> {os.path.relpath(dst, BASE_DIR)}")
    else:
        shutil.move(src, dst)


def process_lessons(grade):
    """Move and rename lesson files for a grade."""
    grade_dir = os.path.join(LESSONS_DIR, f"grade-{grade}")
    if not os.path.exists(grade_dir):
        log(f"WARNING: {grade_dir} not found, skipping")
        return

    level1_dir = os.path.join(grade_dir, "level-1")
    level2_dir = os.path.join(grade_dir, "level-2")
    ensure_dir(level1_dir)
    ensure_dir(level2_dir)

    files = [f for f in os.listdir(grade_dir) if f.endswith(".md")]

    for filename in sorted(files):
        filepath = os.path.join(grade_dir, filename)

        # Check if this is a Level 2 file: G0X-L2-YY-slug.md
        l2_match = re.match(rf'G{grade}-L2-(\d{{2}})-(.+\.md)', filename)
        if l2_match:
            lesson_num = l2_match.group(1)
            slug = l2_match.group(2)
            new_filename = f"G{grade}L2-L{lesson_num}-{slug}"
            new_filepath = os.path.join(level2_dir, new_filename)

            move_file(filepath, new_filepath)
            stats["lessons_moved"] += 1

            # Update internal content
            if not dry_run:
                update_lesson_content_l2(new_filepath, grade, lesson_num)
            continue

        # Check if this is an original (Level 1) file: G0X-LYY-slug.md
        l1_match = re.match(rf'G{grade}-L(\d{{2}})-(.+\.md)', filename)
        if l1_match:
            lesson_num = l1_match.group(1)
            slug = l1_match.group(2)
            new_filename = f"G{grade}L1-L{lesson_num}-{slug}"
            new_filepath = os.path.join(level1_dir, new_filename)

            move_file(filepath, new_filepath)
            stats["lessons_moved"] += 1

            # Update internal content
            if not dry_run:
                update_lesson_content_l1(new_filepath, grade, lesson_num)
            continue

        log(f"SKIPPING unrecognized file: {filename}")


def update_lesson_content_l1(filepath, grade, lesson_num):
    """Update internal references in a Level 1 lesson file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    old_id = f"G{grade}-L{lesson_num}"
    new_id = f"G{grade}L1-L{lesson_num}"

    # Update Lesson ID
    content = content.replace(
        f"| **Lesson ID** | {old_id} |",
        f"| **Lesson ID** | {new_id} |"
    )

    # Update resource paths: materials/grade-0X/G0X-LYY/ -> materials/grade-0X/level-1/G0XL1-LYY/
    content = content.replace(
        f"materials/grade-{grade}/{old_id}/{old_id}-",
        f"materials/grade-{grade}/level-1/{new_id}/{new_id}-"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    stats["content_updated"] += 1


def update_lesson_content_l2(filepath, grade, lesson_num):
    """Update internal references in a Level 2 lesson file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    new_id = f"G{grade}L2-L{lesson_num}"

    # The internal Lesson ID is likely already G0XL2-L0Y based on what we saw
    # But check for any old-format references and fix resource paths
    old_path_pattern = f"materials/grade-{grade}/G{grade}-L2-{lesson_num}"
    new_path = f"materials/grade-{grade}/level-2/{new_id}"

    if old_path_pattern in content:
        content = content.replace(old_path_pattern, new_path)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        stats["content_updated"] += 1


def process_materials(grade):
    """Move and rename materials folders for a grade."""
    grade_dir = os.path.join(MATERIALS_DIR, f"grade-{grade}")
    if not os.path.exists(grade_dir):
        log(f"WARNING: {grade_dir} materials not found, skipping")
        return

    level1_dir = os.path.join(grade_dir, "level-1")
    ensure_dir(level1_dir)

    # Find original lesson material folders (G0X-LYY format, not level-2 dir)
    entries = os.listdir(grade_dir)

    for entry in sorted(entries):
        entry_path = os.path.join(grade_dir, entry)

        # Skip level-2 directory (already correct)
        if entry in ("level-1", "level-2", "level-3"):
            continue

        # Match G0X-LYY folders
        m = re.match(rf'G{grade}-L(\d{{2}})$', entry)
        if m and os.path.isdir(entry_path):
            lesson_num = m.group(1)
            old_id = f"G{grade}-L{lesson_num}"
            new_id = f"G{grade}L1-L{lesson_num}"
            new_folder = os.path.join(level1_dir, new_id)

            # Move the folder
            move_file(entry_path, new_folder)
            stats["materials_moved"] += 1

            # Rename files inside the folder
            if not dry_run and os.path.exists(new_folder):
                rename_material_files(new_folder, old_id, new_id)


def rename_material_files(folder_path, old_id, new_id):
    """Rename files inside a materials folder from old_id to new_id prefix."""
    if not os.path.exists(folder_path):
        return

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path) and item.startswith(old_id):
            new_name = item.replace(old_id, new_id, 1)
            new_path = os.path.join(folder_path, new_name)
            os.rename(item_path, new_path)
            stats["files_renamed"] += 1
        elif os.path.isdir(item_path):
            # Recurse into subdirectories (e.g., images/)
            pass  # images/ folder doesn't need renaming


def main():
    print("=" * 60)
    print("STANDARDIZE GRADES 4-8 NAMING CONVENTION")
    print("=" * 60)

    if dry_run:
        print("\n*** DRY RUN MODE - No files will be modified ***\n")

    for grade in GRADES:
        print(f"\n--- Grade {grade} ---")

        print(f"  Processing lessons...")
        process_lessons(grade)

        print(f"  Processing materials...")
        process_materials(grade)

    print(f"\n{'=' * 60}")
    print("RESULTS")
    print(f"{'=' * 60}")
    print(f"Lesson files moved & renamed: {stats['lessons_moved']}")
    print(f"Material folders moved: {stats['materials_moved']}")
    print(f"Material files renamed: {stats['files_renamed']}")
    print(f"Lesson content updated: {stats['content_updated']}")


if __name__ == "__main__":
    main()
