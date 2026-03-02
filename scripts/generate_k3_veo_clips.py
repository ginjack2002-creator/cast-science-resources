#!/usr/bin/env python3
"""
Phase 2: Generate Veo 3.1 clips for ALL K-3 lessons.
Submits clips with 10-second spacing and handles rate limits gracefully.
Resumes from where it left off (skips existing clips).

Usage:
    python generate_k3_veo_clips.py K       # Kindergarten
    python generate_k3_veo_clips.py all     # All grades
"""

import os, sys, math, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generate_k3_videos import (
    GRADE_CONFIG, VIDEOS_DIR, load_lessons, build_narration,
    submit_veo_clip, poll_veo, get_duration
)


def generate_clips_for_grade(grade_key):
    """Generate all Veo clips for a grade with smart pacing."""
    lessons = load_lessons(grade_key)
    cfg = GRADE_CONFIG[grade_key]

    print(f"\n{'#'*60}")
    print(f"  PHASE 2: Veo 3.1 Clips for {cfg['label']} ({len(lessons)} lessons)")
    print(f"{'#'*60}")

    total_submitted = 0
    total_existing = 0
    total_failed = 0

    for lesson in lessons:
        lid = lesson["id"]
        lesson_dir = os.path.join(VIDEOS_DIR, cfg["dir"], lid)
        segments = build_narration(lesson, cfg)

        print(f"\n  {lid}: {lesson['title']}")

        for seg in segments:
            wav_path = os.path.join(lesson_dir, f"narration_{seg['id']}.wav")
            img_path = os.path.join(lesson_dir, f"scene_{seg['id']}.png")

            if not os.path.exists(wav_path) or not os.path.exists(img_path):
                print(f"    SKIP {seg['id']} (missing assets)")
                continue

            narr_dur = get_duration(wav_path)
            clips_needed = max(1, math.ceil((narr_dur + 1.5) / 6.0))

            # Check which clips already exist
            existing = 0
            needed_indices = []
            for ci in range(clips_needed):
                clip_path = os.path.join(lesson_dir, f"clip_{seg['id']}_{ci}.mp4")
                if os.path.exists(clip_path) and os.path.getsize(clip_path) > 10000:
                    existing += 1
                    total_existing += 1
                else:
                    needed_indices.append(ci)

            if not needed_indices:
                continue

            print(f"    {seg['id']}: need {len(needed_indices)} clip(s) (have {existing}/{clips_needed})")

            # Submit and poll each clip sequentially to manage rate limits
            for ci in needed_indices:
                clip_path = os.path.join(lesson_dir, f"clip_{seg['id']}_{ci}.mp4")
                print(f"      Submitting clip {ci}...")
                op = submit_veo_clip(img_path, seg["anim_desc"], variation_idx=ci)

                if op:
                    print(f"      Polling...")
                    success = poll_veo(op, clip_path)
                    if success:
                        total_submitted += 1
                    else:
                        total_failed += 1
                else:
                    total_failed += 1

                # Wait between submissions to respect rate limits
                time.sleep(8)

    print(f"\n  {cfg['label']} Veo Summary:")
    print(f"    Already existed: {total_existing}")
    print(f"    Newly generated: {total_submitted}")
    print(f"    Failed: {total_failed}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_k3_veo_clips.py [K|1|2|3|all]")
        sys.exit(1)

    target = sys.argv[1]
    if target == "all":
        for g in ["K", "1", "2", "3"]:
            generate_clips_for_grade(g)
    elif target in GRADE_CONFIG:
        generate_clips_for_grade(target)
    else:
        print(f"Unknown: {target}. Use K, 1, 2, 3, or all")


if __name__ == "__main__":
    main()
