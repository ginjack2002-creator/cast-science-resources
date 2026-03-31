#!/usr/bin/env python3
"""
Generate L2 ModelIt! Lesson Companion Videos (Grades 4-8)
=========================================================
Produces ~90-second companion videos for all 35 L2 lessons.

Uses photorealistic Imagen prompts (not cartoon) for grades 4-8.
Same pipeline as K-3 videos: Hume TTS → Imagen → Veo 3.1 → FFmpeg

Usage:
    python generate_l2_videos.py 04_L2       # Grade 4 Level 2 (7 lessons)
    python generate_l2_videos.py 06_L2       # Grade 6 Level 2 (7 lessons)
    python generate_l2_videos.py all         # All 35 L2 lessons
    python generate_l2_videos.py G06L2-L01   # Single lesson
"""

import os, sys, json, time, math, base64, shutil, subprocess, tempfile, requests
import importlib.util
from dotenv import load_dotenv
load_dotenv(os.path.expanduser("~/.env"))

GOOGLE_KEY = os.getenv("GOOGLE_AI_STUDIO_API_KEY")
HUME_KEY = os.getenv("HUME_API_KEY")

VIDEOS_DIR = os.path.expanduser("~/cast-science-resources/videos")
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

# Hume voice: Inspiring Woman (Marie's preference)
VOICE_ID = "b201d214-914c-4d0a-b8e4-54adfc14a0dd"

# ─── Grade configs ───
GRADE_CONFIG = {
    "04_L2": {"label": "4th Grade Level 2", "age_desc": "4th grade students (9-10 years old)", "dir": "grade-04/level-2", "mod": "lesson_data_G04_L2", "prefix": "G04L2", "count": 7},
    "05_L2": {"label": "5th Grade Level 2", "age_desc": "5th grade students (10-11 years old)", "dir": "grade-05/level-2", "mod": "lesson_data_G05_L2", "prefix": "G05L2", "count": 7},
    "06_L2": {"label": "6th Grade Level 2", "age_desc": "6th grade students (11-12 years old)", "dir": "grade-06/level-2", "mod": "lesson_data_G06_L2", "prefix": "G06L2", "count": 7},
    "07_L2": {"label": "7th Grade Level 2", "age_desc": "7th grade students (12-13 years old)", "dir": "grade-07/level-2", "mod": "lesson_data_G07_L2", "prefix": "G07L2", "count": 7},
    "08_L2": {"label": "8th Grade Level 2", "age_desc": "8th grade students (13-14 years old)", "dir": "grade-08/level-2", "mod": "lesson_data_G08_L2", "prefix": "G08L2", "count": 7},
}

# ─── Photorealistic style for grades 4-8 (NOT cartoon) ───
PHOTO_STYLE = """Style: Photorealistic, cinematic, editorial quality photograph.
Soft natural window light with gentle fill, shallow depth of field, 35mm/50mm lens look.
High dynamic range, sharp eyes, realistic skin texture, crisp edges, minimal noise.
Modern classroom or lab setting. Genuinely diverse group reflecting US public school diversity.
Balanced representation of White, Asian/AAPI, Black, and Latino students.
Modern everyday clothing (hoodies, t-shirts, jeans, sneakers). No cultural/traditional outfits.
Varied facial features, different hairstyles. No text, no words, no labels in the image."""

# ─── Camera variations ───
CAMERA_VARIATIONS = [
    "Camera slowly zooms in from medium shot to close-up. Subtle smooth motion.",
    "Camera slowly pans left to right. Smooth dolly motion.",
    "Camera holds steady with gentle ambient movement.",
    "Camera slowly pulls back from close-up to wide shot.",
    "Camera tilts slightly upward with gentle parallax.",
    "Camera orbits slightly around the focal point.",
]

MOTION_VARIATIONS = [
    "Gentle natural movement. Subtle breathing animation on people.",
    "Students shift weight and gesture naturally. Background stays stable.",
    "Soft ambient light shifts. Warm natural classroom lighting.",
    "Focal subject gestures while explaining. Others lean in listening.",
    "Natural hair and clothing micro-movements. Realistic physics.",
    "Scene has gentle depth-of-field shift. Professional documentary feel.",
]


def load_lessons(grade_key):
    """Load lesson data for a grade."""
    cfg = GRADE_CONFIG[grade_key]
    filepath = os.path.join(SCRIPTS_DIR, f"{cfg['mod']}.py")
    spec = importlib.util.spec_from_file_location(cfg['mod'], filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    lessons = []
    for i in range(1, cfg['count'] + 1):
        L = getattr(mod, f"L{i:02d}", None)
        if L:
            lessons.append(L)
    return lessons


def build_narration(lesson, grade_cfg):
    """Build 6-segment narration script for grades 4-8."""
    title = lesson["title"]
    big_q = lesson.get("big_question", title)
    comps = lesson["components"]
    rels = lesson["relationships"]
    answer = lesson.get("answer", "")
    age_desc = grade_cfg["age_desc"]
    discoveries = lesson.get("discoveries", [])

    # External and internal component names
    ext_comps = [c for c in comps if c[2]]
    int_comps = [c for c in comps if not c[2]]
    ext_names = ", ".join(c[0] for c in ext_comps)
    int_names = ", ".join(c[0] for c in int_comps)

    # First relationship
    rel_desc = rels[0][2] if len(rels) > 0 and len(rels[0]) > 2 else ""
    rel_type = "positive" if "+" in rels[0][1] or "POSITIVE" in rels[0][1] else "negative"

    segments = [
        {
            "id": "intro",
            "text": f"Here is a question that might surprise you. {big_q} Think about it for a moment. Today we are going to build a computational model to figure this out.",
            "scene_desc": f"A photorealistic scene of diverse {age_desc} in a modern science classroom, looking at a laptop screen with curiosity. One White student with light brown hair and one Asian American student with glasses are at the center, leaning in toward the screen. A Latino student and a Black student stand behind them, engaged. Natural window light, editorial photo quality.",
            "anim_desc": "Students in classroom looking at screen with curiosity. Natural movement."
        },
        {
            "id": "question",
            "text": f"To answer this question, we need to think about systems. A system has parts that are connected and affect each other. In our model, we have external components like {ext_names} that we can control, and internal components like {int_names} that respond automatically.",
            "scene_desc": f"Close-up of a {age_desc.split('(')[0].strip()} student (Asian American girl, dark hair, focused expression) examining a diagram on a tablet. The diagram shows connected circles representing system components. Modern classroom background, warm lighting.",
            "anim_desc": "Student examining diagram on tablet. Subtle hand movement and focus shift."
        },
        {
            "id": "explain",
            "text": f"Here is how the components are connected. {rel_desc}. This is a {rel_type} relationship. When you change the external component, watch what happens to the internal components. The connections create a chain of cause and effect.",
            "scene_desc": f"A diverse group of {age_desc} around a whiteboard with a diagram showing arrows connecting components. A Black male student is drawing an arrow while a White female student and Latino male student watch. Scientific diagram visible on the board. Professional classroom setting.",
            "anim_desc": "Student drawing on whiteboard while others watch. Collaborative learning scene."
        },
        {
            "id": "experiment",
            "text": f"Now run the simulation. Change the external components by sliding them up or down. Watch the graph. Do you see how the internal components respond? This is your model predicting what will happen in the real world.",
            "scene_desc": f"Over-the-shoulder shot of {age_desc.split('(')[0].strip()} students (White boy and Black girl side by side) looking at a computer screen showing a simulation graph with colored lines moving. Modern classroom with natural light. Realistic computer screen glow on their faces.",
            "anim_desc": "Students watching simulation graph on computer. Lines moving on screen. Engaged expressions."
        },
        {
            "id": "model",
            "text": f"Here is what your model reveals. {answer[:200]}",
            "scene_desc": f"A clear diagram showing the computational model with labeled components and arrows. Clean white background with purple and teal colored elements. Professional infographic style. No people in this shot, just the scientific diagram.",
            "anim_desc": "Diagram with components and arrows. Clean animation of connections highlighting."
        },
        {
            "id": "closing",
            "text": f"You just built and tested a real scientific model. You identified the parts of a system, connected them with relationships, ran simulations, and discovered something powerful. That is exactly what real scientists do. Keep modeling, keep questioning, keep discovering.",
            "scene_desc": f"A joyful group of diverse {age_desc} giving high-fives and smiling in a modern classroom. Balanced mix: White, Asian, Black, and Latino students all celebrating together. Golden afternoon light through windows. Professional editorial photo quality. Confident, aspirational mood.",
            "anim_desc": "Students celebrating together. High-fives and smiles. Warm golden light."
        }
    ]
    return segments


def generate_hume_tts(text, output_path):
    """Generate narration using Hume Octave TTS."""
    if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
        return True

    clean_text = text.replace(" ... ", "... ").strip()
    url = "https://api.hume.ai/v0/tts"
    headers = {"X-Hume-Api-Key": HUME_KEY, "Content-Type": "application/json"}
    payload = {
        "utterances": [{
            "text": clean_text,
            "description": "Confident, warm, inspiring science educator. Clear enunciation, moderate pace. Professional but approachable. Like a favorite science teacher who makes complex ideas click.",
            "voice": {"id": VOICE_ID},
            "speed": 0.90
        }],
        "format": {"type": "wav"}
    }

    print(f"    TTS: {os.path.basename(output_path)}")
    resp = requests.post(url, headers=headers, json=payload, timeout=60)
    if resp.status_code != 200:
        print(f"    ERROR TTS {resp.status_code}: {resp.text[:150]}")
        return False

    audio_b64 = resp.json()["generations"][0]["audio"]
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(audio_b64))
    return True


def generate_scene_image(prompt, output_path):
    """Generate scene image using NanoBanana (Gemini Flash Image)."""
    if os.path.exists(output_path) and os.path.getsize(output_path) > 10000:
        return True

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent?key={GOOGLE_KEY}"
    payload = {
        "contents": [{"parts": [{"text": f"Generate this image: {prompt}"}]}],
        "generationConfig": {"responseModalities": ["IMAGE", "TEXT"]}
    }

    print(f"    IMG: {os.path.basename(output_path)}")
    resp = requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=120)
    if resp.status_code == 200:
        for part in resp.json().get("candidates", [{}])[0].get("content", {}).get("parts", []):
            if "inlineData" in part:
                with open(output_path, "wb") as f:
                    f.write(base64.b64decode(part["inlineData"]["data"]))
                return True
    print(f"    ERROR IMG {resp.status_code}: {resp.text[:150]}")
    return False


def submit_veo_clip(image_path, anim_prompt, variation_idx=0, max_retries=3):
    """Submit a Veo 3.1 clip generation job."""
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()

    cam_var = CAMERA_VARIATIONS[variation_idx % len(CAMERA_VARIATIONS)]
    motion_var = MOTION_VARIATIONS[variation_idx % len(MOTION_VARIATIONS)]
    full_prompt = f"Smooth cinematic animation. {anim_prompt} {cam_var} {motion_var} Professional documentary quality. No sudden movements."

    url = f"https://generativelanguage.googleapis.com/v1beta/models/veo-3.1-generate-preview:predictLongRunning?key={GOOGLE_KEY}"
    payload = {
        "instances": [{
            "prompt": full_prompt,
            "image": {"bytesBase64Encoded": img_b64, "mimeType": "image/png"}
        }],
        "parameters": {"sampleCount": 1, "durationSeconds": 6, "aspectRatio": "16:9"}
    }

    for attempt in range(max_retries):
        resp = requests.post(url, json=payload, timeout=120)
        if resp.status_code == 200:
            return resp.json().get("name")
        if resp.status_code == 429:
            wait = 30 * (2 ** attempt)
            print(f"      Rate limited, waiting {wait}s...")
            time.sleep(wait)
            continue
        print(f"    ERROR Veo {resp.status_code}: {resp.text[:150]}")
        return None
    return None


def poll_veo(op_name, output_path, max_wait=300):
    """Poll Veo operation and download result."""
    start = time.time()
    while time.time() - start < max_wait:
        resp = requests.get(f"https://generativelanguage.googleapis.com/v1beta/{op_name}?key={GOOGLE_KEY}", timeout=30)
        data = resp.json()
        if data.get("done"):
            samples = data.get("response", {}).get("generateVideoResponse", {}).get("generatedSamples", [])
            if not samples:
                samples = data.get("response", {}).get("generatedSamples", [])
            if samples:
                uri = samples[0].get("video", {}).get("uri")
                if uri:
                    vr = requests.get(f"{uri}&key={GOOGLE_KEY}", timeout=120, allow_redirects=True)
                    if len(vr.content) > 10000:
                        with open(output_path, "wb") as f:
                            f.write(vr.content)
                        return True
            return False
        if data.get("error"):
            print(f"    Veo error: {data['error'].get('message', '')[:100]}")
            return False
        time.sleep(12)
    return False


def get_duration(path):
    """Get media file duration in seconds."""
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0", path],
        capture_output=True, text=True
    )
    try:
        return float(result.stdout.strip())
    except:
        return 0.0


def generate_lesson_assets(lesson, grade_key):
    """Generate all assets for one lesson."""
    cfg = GRADE_CONFIG[grade_key]
    lid = lesson["id"]
    lesson_dir = os.path.join(VIDEOS_DIR, cfg["dir"], lid)
    os.makedirs(lesson_dir, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"  {lid}: {lesson['title']}")
    print(f"  Grade: {cfg['label']}")
    print(f"{'='*60}")

    segments = build_narration(lesson, cfg)

    # Step 1: TTS
    print("\n  [1/3] Generating narration...")
    for seg in segments:
        wav_path = os.path.join(lesson_dir, f"narration_{seg['id']}.wav")
        generate_hume_tts(seg["text"], wav_path)
        time.sleep(0.5)

    # Step 2: Images
    print("\n  [2/3] Generating scene images...")
    for seg in segments:
        img_path = os.path.join(lesson_dir, f"scene_{seg['id']}.png")
        full_prompt = f"{seg['scene_desc']} {PHOTO_STYLE}"
        generate_scene_image(full_prompt, img_path)
        time.sleep(2)

    # Step 3: Veo clips
    print("\n  [3/3] Generating Veo 3.1 clips...")
    for seg in segments:
        wav_path = os.path.join(lesson_dir, f"narration_{seg['id']}.wav")
        img_path = os.path.join(lesson_dir, f"scene_{seg['id']}.png")

        if not os.path.exists(wav_path) or not os.path.exists(img_path):
            print(f"    SKIP {seg['id']} (missing wav/img)")
            continue

        narr_dur = get_duration(wav_path)
        clips_needed = max(1, math.ceil((narr_dur + 1.5) / 6.0))

        print(f"    {seg['id']}: narr={narr_dur:.1f}s, need {clips_needed} clip(s)")

        pending_ops = []
        for ci in range(clips_needed):
            clip_path = os.path.join(lesson_dir, f"clip_{seg['id']}_{ci}.mp4")
            if os.path.exists(clip_path) and os.path.getsize(clip_path) > 10000:
                pending_ops.append(("done", clip_path))
                continue

            op = submit_veo_clip(img_path, seg["anim_desc"], variation_idx=ci)
            if op:
                pending_ops.append((op, clip_path))
            else:
                pending_ops.append((None, clip_path))
            time.sleep(5)

        for op_name, clip_path in pending_ops:
            if op_name in (None, "done"):
                continue
            poll_veo(op_name, clip_path)

    return lesson_dir


def compose_lesson_video(lesson, grade_key):
    """Compose final video from generated assets."""
    cfg = GRADE_CONFIG[grade_key]
    lid = lesson["id"]
    lesson_dir = os.path.join(VIDEOS_DIR, cfg["dir"], lid)
    segments = build_narration(lesson, cfg)

    print(f"\n  Composing video for {lid}...")
    tmp = tempfile.mkdtemp()
    final_segments = []

    # Title card
    title_path = os.path.join(tmp, "title.mp4")
    title_safe = lesson['title'].replace("'", "").replace('"', '')
    grade_label = cfg["label"]
    subprocess.run([
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", "color=c=#1E1B4B:s=1280x720:d=4:r=30",
        "-vf",
        f"drawtext=text='ModelIt!':fontsize=56:fontcolor=#5BBFCF:x=(w-text_w)/2:y=h/3-30,"
        f"drawtext=text='{title_safe[:50]}':fontsize=30:fontcolor=white:x=(w-text_w)/2:y=h/2,"
        f"drawtext=text='{grade_label}':fontsize=24:fontcolor=#B8A9D4:x=(w-text_w)/2:y=h/2+45,"
        "fade=t=in:st=0:d=1,fade=t=out:st=3:d=1",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-t", "4",
        title_path
    ], capture_output=True, text=True)
    if os.path.exists(title_path):
        final_segments.append(title_path)

    # Process each segment
    for seg in segments:
        wav_path = os.path.join(lesson_dir, f"narration_{seg['id']}.wav")
        if not os.path.exists(wav_path):
            continue

        narr_dur = get_duration(wav_path)
        if narr_dur <= 0:
            continue

        # Find clips for this segment
        clips = sorted([
            os.path.join(lesson_dir, f) for f in os.listdir(lesson_dir)
            if f.startswith(f"clip_{seg['id']}_") and f.endswith(".mp4")
        ])

        if not clips:
            # Fallback: use scene image as still frame
            img_path = os.path.join(lesson_dir, f"scene_{seg['id']}.png")
            if os.path.exists(img_path):
                still_path = os.path.join(tmp, f"still_{seg['id']}.mp4")
                subprocess.run([
                    "ffmpeg", "-y",
                    "-loop", "1", "-i", img_path,
                    "-c:v", "libx264", "-t", str(narr_dur + 1),
                    "-pix_fmt", "yuv420p", "-vf", "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2",
                    still_path
                ], capture_output=True, text=True)
                clips = [still_path] if os.path.exists(still_path) else []

        if not clips:
            continue

        # Concatenate clips if multiple
        if len(clips) == 1:
            video_source = clips[0]
        else:
            concat_list = os.path.join(tmp, f"concat_{seg['id']}.txt")
            with open(concat_list, "w") as f:
                for c in clips:
                    f.write(f"file '{c}'\n")
            concat_path = os.path.join(tmp, f"concat_{seg['id']}.mp4")
            subprocess.run([
                "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list,
                "-c:v", "libx264", "-pix_fmt", "yuv420p", concat_path
            ], capture_output=True, text=True)
            video_source = concat_path if os.path.exists(concat_path) else clips[0]

        # Overlay narration on video, trim to narration length
        seg_path = os.path.join(tmp, f"seg_{seg['id']}.mp4")
        subprocess.run([
            "ffmpeg", "-y",
            "-i", video_source, "-i", wav_path,
            "-c:v", "libx264", "-c:a", "aac", "-b:a", "128k",
            "-t", str(narr_dur + 0.5),
            "-vf", "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2",
            "-pix_fmt", "yuv420p", "-shortest",
            seg_path
        ], capture_output=True, text=True)

        if os.path.exists(seg_path) and os.path.getsize(seg_path) > 5000:
            final_segments.append(seg_path)

    if not final_segments:
        print(f"    No segments to compose for {lid}")
        shutil.rmtree(tmp, ignore_errors=True)
        return None

    # Final concatenation
    final_list = os.path.join(tmp, "final.txt")
    with open(final_list, "w") as f:
        for seg_path in final_segments:
            f.write(f"file '{seg_path}'\n")

    output_path = os.path.join(VIDEOS_DIR, cfg["dir"], f"{lid}-Companion-Video.mp4")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", final_list,
        "-c:v", "libx264", "-c:a", "aac", "-pix_fmt", "yuv420p",
        output_path
    ], capture_output=True, text=True)

    shutil.rmtree(tmp, ignore_errors=True)

    if os.path.exists(output_path):
        dur = get_duration(output_path)
        size_mb = os.path.getsize(output_path) / (1024 * 1024)
        print(f"    [OK] {output_path} ({dur:.1f}s, {size_mb:.1f}MB)")
        return output_path
    return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_l2_videos.py <grade_key|all|lesson_id>")
        print("  Examples: 04_L2, 06_L2, all, G06L2-L01")
        sys.exit(1)

    target = sys.argv[1]

    if target.lower() == "all":
        grade_keys = list(GRADE_CONFIG.keys())
    elif target in GRADE_CONFIG:
        grade_keys = [target]
    else:
        # Try to find specific lesson ID like G06L2-L01
        found = False
        for gk, cfg in GRADE_CONFIG.items():
            if target.startswith(cfg["prefix"]):
                lessons = load_lessons(gk)
                for lesson in lessons:
                    if lesson["id"] == target:
                        print(f"Processing single lesson: {target}")
                        generate_lesson_assets(lesson, gk)
                        compose_lesson_video(lesson, gk)
                        found = True
                        break
                if found:
                    break
        if not found:
            print(f"ERROR: Unknown target '{target}'")
        sys.exit(0)

    for grade_key in grade_keys:
        print(f"\n{'#'*60}")
        print(f"# {GRADE_CONFIG[grade_key]['label']}")
        print(f"{'#'*60}")

        lessons = load_lessons(grade_key)
        for lesson in lessons:
            generate_lesson_assets(lesson, grade_key)
            compose_lesson_video(lesson, grade_key)

    print("\n\nDone! All videos generated.")


if __name__ == "__main__":
    main()
