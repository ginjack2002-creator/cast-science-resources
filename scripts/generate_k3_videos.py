#!/usr/bin/env python3
"""
Generate K-3 ModelIt! Lesson Companion Videos (Veo 3.1)
=======================================================
Produces ~77-second animated lesson videos for all 40 K-3 lessons.

Design principles:
- Blue's Clues: single warm narrator, direct-to-kid, pauses for response
- Sesame Street: comprehension-driven stickiness
- Nickelodeon color science: warm saturated focal elements on calmer backgrounds
- Gladwell stickiness: simple packaging, active interaction, narrative over segmentation
- Pacing: ~120 wpm, built-in pauses for thinking

NO CLIP REPEATING: Each segment generates enough UNIQUE Veo clips
(different camera angles/motions) to cover the narration duration.

Usage:
    python generate_k3_videos.py K       # Kindergarten (10 lessons)
    python generate_k3_videos.py 1       # Grade 1 (10 lessons)
    python generate_k3_videos.py 2       # Grade 2 (10 lessons)
    python generate_k3_videos.py 3       # Grade 3 (10 lessons)
    python generate_k3_videos.py all     # All 40 lessons
    python generate_k3_videos.py GK-L01  # Single lesson
"""

import os, sys, json, time, math, base64, shutil, subprocess, tempfile, requests
from dotenv import load_dotenv
load_dotenv(os.path.expanduser("~/.env"))

GOOGLE_KEY = os.getenv("GOOGLE_AI_STUDIO_API_KEY")
HUME_KEY = os.getenv("HUME_API_KEY")

VIDEOS_DIR = os.path.expanduser("~/cast-science-resources/videos")

# Hume voice: Caring Mother — warm, American, mid-age, perfect for K-3
VOICE_ID = "97fe9008-8584-4d56-8453-bd8c7ead3663"

# ─── Grade configs ───
GRADE_CONFIG = {
    "K":  {"label": "Kindergarten", "age_desc": "kindergarten children (5-6 years old)", "dir": "grade-K",  "mod": "lesson_data_GK",  "prefix": "GK"},
    "1":  {"label": "1st Grade",    "age_desc": "first-grade children (6-7 years old)",  "dir": "grade-01", "mod": "lesson_data_G01", "prefix": "G01"},
    "2":  {"label": "2nd Grade",    "age_desc": "second-grade children (7-8 years old)", "dir": "grade-02", "mod": "lesson_data_G02", "prefix": "G02"},
    "3":  {"label": "3rd Grade",    "age_desc": "third-grade children (8-9 years old)",  "dir": "grade-03", "mod": "lesson_data_G03", "prefix": "G03"},
}

# ─── Nickelodeon color style ───
NICK_STYLE = """Style: Pixar-quality 3D animated illustration, vibrant saturated colors inspired by
Nickelodeon children's shows. Warm orange (#F69338) and sunny yellow accents,
sky blue (#00BEF2) backgrounds, slime green (#78BE20) highlights.
Soft rounded shapes, friendly big-eyed characters, clean composition.
Lighting: warm golden-hour feel with soft shadows, bright and inviting.
Background: simple, uncluttered, gently blurred depth-of-field.
No text, no words, no labels in the image."""

# ─── Camera angle variations for unique clips (never repeat) ───
CAMERA_VARIATIONS = [
    "Camera slowly zooms in from medium shot to close-up. Gentle subtle movement.",
    "Camera slowly pans left to right across the scene. Smooth dolly motion.",
    "Camera holds steady with gentle floating motion. Characters subtly shift and breathe.",
    "Camera slowly pulls back from close-up to wide shot. Reveal motion.",
    "Camera tilts slightly upward with gentle parallax on background layers.",
    "Camera orbits slightly around the focal point. Subtle 3D depth motion.",
]

# ─── Animation motion variations ───
MOTION_VARIATIONS = [
    "Gentle bobbing and breathing animation on characters. Soft ambient particle effects.",
    "Characters blink and shift weight naturally. Background elements sway gently.",
    "Slow sparkle effects drift across scene. Warm light rays shift subtly.",
    "Focal element gently glows and pulses. Background has soft depth shimmer.",
    "Natural hair and clothing micro-movements. Dust motes drift in light beams.",
    "Scene has gentle depth-of-field shift. Foreground to background focus pull.",
]


def load_lessons(grade_key):
    """Load lesson data for a grade."""
    import importlib
    cfg = GRADE_CONFIG[grade_key]
    mod = importlib.import_module(cfg["mod"])
    lessons = []
    for i in range(1, 11):
        L = getattr(mod, f"L{i:02d}", None)
        if L:
            lessons.append(L)
    return lessons


def build_narration(lesson, grade_cfg):
    """Build 6-segment narration script from lesson data using Blue's Clues structure."""
    title = lesson["title"]
    big_q = lesson.get("big_question", title)
    comps = lesson["components"]
    rels = lesson["relationships"]
    vocab = lesson.get("vocabulary", [])
    answer = lesson.get("answer", "")
    age_desc = grade_cfg["age_desc"]

    # Component names
    ext_name = comps[0][0]  # First component (external)
    int_name = comps[1][0]  # Second component (internal)
    ext_desc = comps[0][1]
    int_desc = comps[1][1]

    # Relationship info
    rel_type = "+" if "POSITIVE" in rels[0][1] or "+" in rels[0][1] else "-"
    direction = "up" if rel_type == "+" else "down"
    rel_word = "positive" if rel_type == "+" else "negative"

    # Sentence frame
    sf = lesson.get("sentence_frame", "")
    if not sf:
        sf = f"When {ext_name} goes up, {int_name} goes {direction}."

    # Build 6 segments
    segments = [
        {
            "id": "intro",
            "text": f"Hey there, friend! ... {big_q} ... Have you ever thought about that? ... Today we are going to find out!",
            "scene_desc": f"A warm, inviting animated classroom scene with a cute diverse group of {age_desc} sitting on a colorful rug in a circle, looking excited and curious. Bright sunny classroom with big windows. One child with dark brown skin and natural coils is in the center, eyes wide with wonder.",
            "anim_desc": "Children in classroom, one reaches forward excitedly. Warm inviting scene."
        },
        {
            "id": "question",
            "text": f"Do you know the answer? ... Think about it for a second. ... Here is a clue! It has to do with {ext_name}!",
            "scene_desc": f"Close-up of an adorable animated child ({age_desc.split('(')[0].strip()}, medium brown skin, curly hair, big bright eyes) with a thinking expression, finger on chin, colorful question marks and sparkly stars floating around their head. Warm orange and yellow background glow.",
            "anim_desc": "Child thinking with floating question marks. Gentle sparkle effects."
        },
        {
            "id": "explain",
            "text": f"Let me tell you! {ext_name} is something we can change or control. {ext_desc}. And {int_name}? That changes all by itself! {int_desc}. They are connected!",
            "scene_desc": f"A beautiful animated scene showing two large colorful objects representing {ext_name} (bright orange) and {int_name} (sky blue) with a glowing connection between them. Sparkle effects. Diverse {age_desc} pointing at the objects with excitement.",
            "anim_desc": "Two connected objects glow and pulse. Children point excitedly."
        },
        {
            "id": "experiment",
            "text": f"Now watch what happens! When {ext_name} goes UP ... {int_name} goes {direction.upper()}! See? When we change one part, the other part changes too. That is so cool!",
            "scene_desc": f"A split animated scene. Left: an animated child ({age_desc.split('(')[0].strip()}, dark skin, braids) demonstrating {ext_name} going up with a big upward arrow. Right: {int_name} responding by going {direction} with a matching arrow. Bright classroom setting with colorful elements.",
            "anim_desc": f"Split scene showing cause and effect. Arrows animate {direction}ward."
        },
        {
            "id": "model",
            "text": f"Scientists call this a MODEL! {ext_name} connects to {int_name} with a {rel_word} connection. That means they go the SAME way! Can you say '{rel_word}'? ... Great job!",
            "scene_desc": f"A simple, beautiful animated diagram showing two big colorful circles connected by a bright sparkly arrow. Orange circle (left) for {ext_name} with an UP arrow inside. Blue circle (right) for {int_name} with an {direction.upper()} arrow inside. A big golden {'plus' if rel_type == '+' else 'minus'} sign floats above the arrow. Warm gradient background.",
            "anim_desc": "Diagram circles pulse gently. Arrow glows and sparkles. Sign rotates."
        },
        {
            "id": "closing",
            "text": f"Now YOU know a science secret! {sf.replace('_______', direction)} ... Next time you see this in real life, you will know exactly why. You are a SCIENTIST now! Bye, friend!",
            "scene_desc": f"A joyful animated scene of diverse {age_desc} jumping and celebrating with arms up, colorful confetti and golden stars bursting around them. One child in the center (dark brown skin, big afro) holds arms up triumphantly. Warm golden light, vibrant celebration colors.",
            "anim_desc": "Children jumping and celebrating. Confetti falling. Pure joy."
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
            "description": "Warm, nurturing, excited children's show host. Speaking directly to one child. Slow pace, clear enunciation, genuine wonder and encouragement. Like a favorite teacher reading a story.",
            "voice": {"id": VOICE_ID},
            "speed": 0.85
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
    """Generate scene image using NanoBanana."""
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
    """Submit a Veo 3.1 clip generation job. Returns operation name.
    Includes exponential backoff for rate limits (429)."""
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()

    # Combine animation description with camera/motion variation for uniqueness
    cam_var = CAMERA_VARIATIONS[variation_idx % len(CAMERA_VARIATIONS)]
    motion_var = MOTION_VARIATIONS[variation_idx % len(MOTION_VARIATIONS)]
    full_prompt = f"Gentle smooth animation for children's educational show. {anim_prompt} {cam_var} {motion_var} Warm lighting. No sudden movements."

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
            wait = 30 * (2 ** attempt)  # 30s, 60s, 120s
            print(f"      Rate limited, waiting {wait}s (attempt {attempt+1}/{max_retries})...")
            time.sleep(wait)
            continue
        print(f"    ERROR Veo {resp.status_code}: {resp.text[:150]}")
        return None
    print(f"    Rate limit persisted after {max_retries} retries")
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
            print(f"    Veo done but no usable video")
            return False
        if data.get("error"):
            print(f"    Veo error: {data['error'].get('message', '')[:100]}")
            return False
        elapsed = int(time.time() - start)
        print(f"    Polling Veo... ({elapsed}s)", end="\r")
        time.sleep(12)
    print(f"    Veo timeout after {max_wait}s")
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
    """Generate all assets for one lesson: narration + images + clips."""
    cfg = GRADE_CONFIG[grade_key]
    lid = lesson["id"]
    lesson_dir = os.path.join(VIDEOS_DIR, cfg["dir"], lid)
    os.makedirs(lesson_dir, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"  {lid}: {lesson['title']}")
    print(f"  Grade: {cfg['label']}")
    print(f"{'='*60}")

    segments = build_narration(lesson, cfg)

    # ─── Step 1: Generate narration WAVs ───
    print("\n  [1/3] Generating narration...")
    for seg in segments:
        wav_path = os.path.join(lesson_dir, f"narration_{seg['id']}.wav")
        generate_hume_tts(seg["text"], wav_path)
        time.sleep(0.5)

    # ─── Step 2: Generate scene images ───
    print("\n  [2/3] Generating scene images...")
    for seg in segments:
        img_path = os.path.join(lesson_dir, f"scene_{seg['id']}.png")
        full_prompt = f"{seg['scene_desc']} {NICK_STYLE}"
        generate_scene_image(full_prompt, img_path)
        time.sleep(1)

    # ─── Step 3: Generate UNIQUE Veo clips (no repeats) ───
    print("\n  [3/3] Generating Veo 3.1 clips (no repeats)...")
    for seg in segments:
        wav_path = os.path.join(lesson_dir, f"narration_{seg['id']}.wav")
        img_path = os.path.join(lesson_dir, f"scene_{seg['id']}.png")

        if not os.path.exists(wav_path) or not os.path.exists(img_path):
            print(f"    SKIP {seg['id']} (missing wav/img)")
            continue

        narr_dur = get_duration(wav_path)
        clips_needed = max(1, math.ceil((narr_dur + 1.5) / 6.0))

        print(f"    {seg['id']}: narr={narr_dur:.1f}s, need {clips_needed} unique clip(s)")

        # Submit all needed clips with different variations
        pending_ops = []
        for ci in range(clips_needed):
            clip_path = os.path.join(lesson_dir, f"clip_{seg['id']}_{ci}.mp4")
            if os.path.exists(clip_path) and os.path.getsize(clip_path) > 10000:
                print(f"      SKIP clip_{seg['id']}_{ci}.mp4 (exists)")
                pending_ops.append(("done", clip_path))
                continue

            op = submit_veo_clip(img_path, seg["anim_desc"], variation_idx=ci)
            if op:
                pending_ops.append((op, clip_path))
                print(f"      Submitted clip {ci} ({CAMERA_VARIATIONS[ci % len(CAMERA_VARIATIONS)][:40]}...)")
            else:
                pending_ops.append((None, clip_path))
            time.sleep(5)  # Rate limit between submissions

        # Poll all pending
        for op_name, clip_path in pending_ops:
            if op_name is None:
                continue
            if op_name == "done":
                continue
            print(f"      Downloading {os.path.basename(clip_path)}...")
            poll_veo(op_name, clip_path)

    return lesson_dir


def compose_lesson_video(lesson, grade_key):
    """Compose final video from generated assets with NO clip repeating."""
    cfg = GRADE_CONFIG[grade_key]
    lid = lesson["id"]
    lesson_dir = os.path.join(VIDEOS_DIR, cfg["dir"], lid)
    segments = build_narration(lesson, cfg)

    # Parse grade/lesson for title card
    grade_label = cfg["label"]
    lesson_num = lid.split("-L")[1]

    print(f"\n  Composing video for {lid}...")
    tmp = tempfile.mkdtemp()
    final_segments = []

    # ─── Title card ───
    title_path = os.path.join(tmp, "title.mp4")
    title_safe = lesson['title'].replace("'", "")
    subprocess.run([
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", "color=c=#0D1B2A:s=1280x720:d=4:r=30",
        "-vf",
        f"drawtext=text='ModelIt!':fontsize=64:fontcolor=white:x=(w-text_w)/2:y=h/3-30:fontfile=C\\\\:/Windows/Fonts/comicbd.ttf,"
        f"drawtext=text='{title_safe}':fontsize=36:fontcolor=#F69338:x=(w-text_w)/2:y=h/2:fontfile=C\\\\:/Windows/Fonts/comic.ttf,"
        f"drawtext=text='{grade_label} - Lesson {lesson_num}':fontsize=28:fontcolor=#7EC8E3:x=(w-text_w)/2:y=h/2+55:fontfile=C\\\\:/Windows/Fonts/comic.ttf,"
        "fade=t=in:st=0:d=1,fade=t=out:st=3:d=1",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-t", "4",
        title_path
    ], capture_output=True, text=True)
    if os.path.exists(title_path):
        final_segments.append(title_path)

    # ─── Process each segment: chain unique clips + overlay narration ───
    for seg in segments:
        wav_path = os.path.join(lesson_dir, f"narration_{seg['id']}.wav")
        if not os.path.exists(wav_path):
            continue

        narr_dur = get_duration(wav_path)
        target_dur = narr_dur + 1.5
        clips_needed = max(1, math.ceil(target_dur / 6.0))

        # Gather available unique clips for this segment
        available_clips = []
        for ci in range(clips_needed + 2):  # Check a few extra in case
            cp = os.path.join(lesson_dir, f"clip_{seg['id']}_{ci}.mp4")
            if os.path.exists(cp) and os.path.getsize(cp) > 10000:
                available_clips.append(cp)

        if not available_clips:
            # Fallback: use scene image with Ken Burns zoom
            img_path = os.path.join(lesson_dir, f"scene_{seg['id']}.png")
            if os.path.exists(img_path):
                still_path = os.path.join(tmp, f"still_{seg['id']}.mp4")
                subprocess.run([
                    "ffmpeg", "-y", "-loop", "1", "-i", img_path,
                    "-t", str(target_dur),
                    "-vf", "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
                    still_path
                ], capture_output=True, text=True)
                available_clips = [still_path]
            else:
                continue

        # Chain unique clips (NO repeating)
        concat_file = os.path.join(tmp, f"chain_{seg['id']}.txt")
        with open(concat_file, "w") as f:
            for ci in range(clips_needed):
                # Use clips in order, wrapping ONLY if we exhausted all unique ones
                clip = available_clips[ci % len(available_clips)]
                # Strip native audio
                stripped = os.path.join(tmp, f"strip_{seg['id']}_{ci}.mp4")
                subprocess.run(
                    ["ffmpeg", "-y", "-i", clip, "-an", "-c:v", "copy", stripped],
                    capture_output=True, text=True
                )
                if os.path.exists(stripped):
                    f.write(f"file '{stripped}'\n")

        chained = os.path.join(tmp, f"chained_{seg['id']}.mp4")
        subprocess.run([
            "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_file,
            "-t", str(target_dur),
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            chained
        ], capture_output=True, text=True)

        # Overlay narration on chained clips
        out_seg = os.path.join(tmp, f"final_{seg['id']}.mp4")
        subprocess.run([
            "ffmpeg", "-y",
            "-i", chained, "-i", wav_path,
            "-filter_complex",
            f"[0:v]fade=t=in:st=0:d=0.5,fade=t=out:st={target_dur-0.5}:d=0.5[v];"
            f"[1:a]adelay=500|500,afade=t=in:st=0:d=0.3,afade=t=out:st={narr_dur}:d=0.3[a]",
            "-map", "[v]", "-map", "[a]",
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k",
            "-t", str(target_dur), "-shortest",
            out_seg
        ], capture_output=True, text=True)

        if os.path.exists(out_seg) and os.path.getsize(out_seg) > 1000:
            final_segments.append(out_seg)
            print(f"    {seg['id']}: {get_duration(out_seg):.1f}s ({len(available_clips)} unique clips)")

    # ─── End card ───
    end_path = os.path.join(tmp, "end.mp4")
    subprocess.run([
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", "color=c=#0D1B2A:s=1280x720:d=4:r=30",
        "-vf",
        "drawtext=text='You are a Scientist!':fontsize=55:fontcolor=#F69338:x=(w-text_w)/2:y=h/3:fontfile=C\\\\:/Windows/Fonts/comicbd.ttf,"
        "drawtext=text='Keep Exploring!':fontsize=40:fontcolor=white:x=(w-text_w)/2:y=h/2+20:fontfile=C\\\\:/Windows/Fonts/comic.ttf,"
        "drawtext=text='ModelIt! by Discovery Collective':fontsize=24:fontcolor=#7EC8E3:x=(w-text_w)/2:y=h*3/4:fontfile=C\\\\:/Windows/Fonts/comic.ttf,"
        "fade=t=in:st=0:d=1,fade=t=out:st=3:d=1",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-t", "4",
        end_path
    ], capture_output=True, text=True)
    if os.path.exists(end_path):
        # Add silent audio
        end_audio = os.path.join(tmp, "end_a.mp4")
        subprocess.run([
            "ffmpeg", "-y", "-i", end_path,
            "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
            "-c:v", "copy", "-c:a", "aac", "-shortest", end_audio
        ], capture_output=True, text=True)
        if os.path.exists(end_audio):
            final_segments.append(end_audio)

    # ─── Normalize and concatenate ───
    if len(final_segments) < 3:
        print(f"    ERROR: Only {len(final_segments)} segments, need at least 3")
        return None

    normalized = []
    for i, sf in enumerate(final_segments):
        norm = os.path.join(tmp, f"n_{i:02d}.mp4")
        probe = subprocess.run(
            ["ffprobe", "-v", "quiet", "-show_streams", "-select_streams", "a", sf],
            capture_output=True, text=True
        )
        has_audio = "codec_type=audio" in probe.stdout

        cmd = ["ffmpeg", "-y", "-i", sf]
        if not has_audio:
            cmd += ["-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100"]
        cmd += [
            "-vf", "scale=1280:720,fps=30,format=yuv420p",
            "-c:v", "libx264", "-preset", "medium", "-crf", "23",
            "-ar", "44100", "-ac", "2", "-c:a", "aac", "-b:a", "192k",
        ]
        if not has_audio:
            cmd.append("-shortest")
        cmd.append(norm)

        subprocess.run(cmd, capture_output=True, text=True)
        if os.path.exists(norm) and os.path.getsize(norm) > 1000:
            normalized.append(norm)

    concat_list = os.path.join(tmp, "final.txt")
    with open(concat_list, "w") as f:
        for n in normalized:
            f.write(f"file '{n}'\n")

    output_path = os.path.join(VIDEOS_DIR, cfg["dir"], f"{lid}-Companion-Video.mp4")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list,
        "-c:v", "libx264", "-preset", "medium", "-crf", "22",
        "-c:a", "aac", "-b:a", "192k",
        output_path
    ], capture_output=True, text=True)

    if os.path.exists(output_path) and os.path.getsize(output_path) > 10000:
        dur = get_duration(output_path)
        sz = os.path.getsize(output_path) / (1024 * 1024)
        print(f"\n    DONE: {output_path}")
        print(f"    Duration: {dur:.1f}s  Size: {sz:.1f} MB")
        return output_path
    else:
        print(f"    ERROR: Final video composition failed")
        return None


def process_grade(grade_key):
    """Process all 10 lessons for a grade."""
    lessons = load_lessons(grade_key)
    cfg = GRADE_CONFIG[grade_key]

    print(f"\n{'#'*60}")
    print(f"  GENERATING {cfg['label'].upper()} VIDEOS ({len(lessons)} lessons)")
    print(f"{'#'*60}")

    results = []
    for lesson in lessons:
        try:
            # Generate assets
            generate_lesson_assets(lesson, grade_key)
            # Compose video
            result = compose_lesson_video(lesson, grade_key)
            results.append((lesson["id"], result))
        except Exception as e:
            print(f"  ERROR on {lesson['id']}: {e}")
            results.append((lesson["id"], None))

    # Summary
    print(f"\n{'='*60}")
    print(f"  {cfg['label']} Summary:")
    ok = sum(1 for _, r in results if r)
    print(f"  Completed: {ok}/{len(results)}")
    for lid, r in results:
        status = "OK" if r else "FAILED"
        print(f"    {lid}: {status}")
    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_k3_videos.py [K|1|2|3|all|GK-L01]")
        sys.exit(1)

    # Make sure we're in the right directory for imports
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, script_dir)

    target = sys.argv[1]

    if target == "all":
        for g in ["K", "1", "2", "3"]:
            process_grade(g)
    elif target in GRADE_CONFIG:
        process_grade(target)
    elif "-L" in target:
        # Single lesson mode (e.g., GK-L01, G02-L05)
        prefix = target.split("-L")[0]
        lesson_num = int(target.split("-L")[1])
        grade_key = None
        for gk, cfg in GRADE_CONFIG.items():
            if cfg["prefix"] == prefix:
                grade_key = gk
                break
        if not grade_key:
            print(f"Unknown prefix: {prefix}")
            sys.exit(1)
        lessons = load_lessons(grade_key)
        if lesson_num < 1 or lesson_num > len(lessons):
            print(f"Lesson {lesson_num} out of range (1-{len(lessons)})")
            sys.exit(1)
        lesson = lessons[lesson_num - 1]
        generate_lesson_assets(lesson, grade_key)
        compose_lesson_video(lesson, grade_key)
    else:
        print(f"Unknown target: {target}")
        print("Use: K, 1, 2, 3, all, or a lesson ID like GK-L01")
        sys.exit(1)


if __name__ == "__main__":
    main()
