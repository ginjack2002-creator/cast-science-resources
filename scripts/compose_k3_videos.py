#!/usr/bin/env python3
"""
Phase 3: Compose final K-3 companion videos from generated assets.
Uses whatever clips are available, falls back to scene images when needed.
No clip repeating — chains unique clips or uses Ken Burns on stills.

Usage:
    python compose_k3_videos.py K       # Kindergarten
    python compose_k3_videos.py all     # All grades
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generate_k3_videos import (
    GRADE_CONFIG, VIDEOS_DIR, load_lessons, compose_lesson_video
)


def compose_grade(grade_key):
    """Compose all videos for a grade."""
    lessons = load_lessons(grade_key)
    cfg = GRADE_CONFIG[grade_key]

    print(f"\n{'#'*60}")
    print(f"  PHASE 3: Composing {cfg['label']} Videos ({len(lessons)} lessons)")
    print(f"{'#'*60}")

    results = []
    for lesson in lessons:
        try:
            result = compose_lesson_video(lesson, grade_key)
            results.append((lesson["id"], result))
        except Exception as e:
            print(f"  ERROR {lesson['id']}: {e}")
            results.append((lesson["id"], None))

    print(f"\n  {cfg['label']} Compose Summary:")
    ok = sum(1 for _, r in results if r)
    print(f"    Completed: {ok}/{len(results)}")
    for lid, r in results:
        if r:
            sz = os.path.getsize(r) / (1024*1024)
            print(f"    {lid}: OK ({sz:.1f} MB)")
        else:
            print(f"    {lid}: FAILED")


def main():
    if len(sys.argv) < 2:
        print("Usage: python compose_k3_videos.py [K|1|2|3|all]")
        sys.exit(1)

    target = sys.argv[1]
    if target == "all":
        for g in ["K", "1", "2", "3"]:
            compose_grade(g)
    elif target in GRADE_CONFIG:
        compose_grade(target)
    else:
        print(f"Unknown: {target}. Use K, 1, 2, 3, or all")


if __name__ == "__main__":
    main()
