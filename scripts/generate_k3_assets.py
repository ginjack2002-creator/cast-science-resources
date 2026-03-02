#!/usr/bin/env python3
"""
Phase 1: Generate narration (Hume TTS) + scene images (NanoBanana) for ALL K-3 lessons.
These are fast and don't hit Veo rate limits.

Usage:
    python generate_k3_assets.py K       # Kindergarten
    python generate_k3_assets.py all     # All grades
"""

import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generate_k3_videos import (
    GRADE_CONFIG, VIDEOS_DIR, load_lessons, build_narration,
    generate_hume_tts, generate_scene_image, NICK_STYLE
)


def generate_assets_only(grade_key):
    """Generate narration + images for all lessons in a grade (no Veo)."""
    lessons = load_lessons(grade_key)
    cfg = GRADE_CONFIG[grade_key]

    print(f"\n{'#'*60}")
    print(f"  PHASE 1: Narration + Images for {cfg['label']} ({len(lessons)} lessons)")
    print(f"{'#'*60}")

    for lesson in lessons:
        lid = lesson["id"]
        lesson_dir = os.path.join(VIDEOS_DIR, cfg["dir"], lid)
        os.makedirs(lesson_dir, exist_ok=True)

        segments = build_narration(lesson, cfg)

        print(f"\n  {lid}: {lesson['title']}")

        # Narration
        for seg in segments:
            wav_path = os.path.join(lesson_dir, f"narration_{seg['id']}.wav")
            generate_hume_tts(seg["text"], wav_path)
            time.sleep(0.3)

        # Images
        for seg in segments:
            img_path = os.path.join(lesson_dir, f"scene_{seg['id']}.png")
            full_prompt = f"{seg['scene_desc']} {NICK_STYLE}"
            generate_scene_image(full_prompt, img_path)
            time.sleep(1)

    # Summary
    total_wavs = 0
    total_imgs = 0
    for lesson in lessons:
        lid = lesson["id"]
        d = os.path.join(VIDEOS_DIR, cfg["dir"], lid)
        if os.path.exists(d):
            total_wavs += len([f for f in os.listdir(d) if f.endswith('.wav')])
            total_imgs += len([f for f in os.listdir(d) if f.endswith('.png')])

    print(f"\n  {cfg['label']} complete: {total_wavs} WAVs, {total_imgs} images")


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_k3_assets.py [K|1|2|3|all]")
        sys.exit(1)

    target = sys.argv[1]
    if target == "all":
        for g in ["K", "1", "2", "3"]:
            generate_assets_only(g)
    elif target in GRADE_CONFIG:
        generate_assets_only(target)
    else:
        print(f"Unknown: {target}. Use K, 1, 2, 3, or all")


if __name__ == "__main__":
    main()
