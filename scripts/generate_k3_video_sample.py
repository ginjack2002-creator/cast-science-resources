#!/usr/bin/env python3
"""
Generate K-3 Lesson Companion Video Samples
Compares Veo 3.1 vs Grok Imagine Video for animated scenes.

Design principles applied:
- Blue's Clues: single warm narrator, direct-to-kid, pauses for response, 3-clue structure
- Sesame Street: comprehension-driven stickiness, Muppet color saturation
- Nickelodeon color science: warm saturated focal elements on calmer backgrounds
- Gladwell stickiness: simple packaging, active interaction, narrative over segmentation
- Pacing: ~120 wpm, 2-3 second pauses for questions
"""

import os, sys, json, time, base64, struct, requests

# Load API keys
from dotenv import load_dotenv
load_dotenv(os.path.expanduser("~/.env"))

GOOGLE_KEY = os.getenv("GOOGLE_AI_STUDIO_API_KEY")
GROK_KEY = os.getenv("GROK_API_KEY")
HUME_KEY = os.getenv("HUME_API_KEY")

SAMPLE_DIR = os.path.expanduser("~/cast-science-resources/videos/samples")

# ─── Nickelodeon-inspired color palette for image prompts ───
# Deep Saffron (#F69338), Process Cyan (#00BEF2), Slime Green (#78BE20)
# Pantone 021 Orange, Nick Jr soft pastels + saturated focal pops
NICK_STYLE = """
Style: Pixar-quality 3D animated illustration, vibrant saturated colors inspired by
Nickelodeon children's shows. Warm orange (#F69338) and sunny yellow accents,
sky blue (#00BEF2) backgrounds, slime green (#78BE20) highlights.
Soft rounded shapes, friendly big-eyed characters, clean composition.
Lighting: warm golden-hour feel with soft shadows, bright and inviting.
Characters: diverse group of animated kindergarten children (5-6 years old) with
different skin tones (dark brown, medium brown, light brown, tan, light),
varied hair textures (coils, curls, braids, straight), cute expressive faces.
Background: simple, uncluttered, gently blurred depth-of-field to focus on characters.
No text, no words, no labels in the image.
"""

# ─── Narration Script (Blue's Clues style) ───
# ~120 wpm, with [PAUSE] markers for 2-3 second pauses
NARRATION_SEGMENTS = [
    {
        "id": "intro",
        "text": "Hey there, friend! Have you ever held a ball way up high... and then let go? What happened? ... It fell DOWN, didn't it! But why does it always fall DOWN and never UP?",
        "scene_prompt": f"A warm, inviting animated classroom scene with a cute diverse group of kindergarten children (5-6 years old) sitting on a colorful rug in a circle, looking up excitedly at a bright orange rubber ball floating in mid-air above them. The classroom has big sunny windows, soft natural light, colorful decorations. One child with dark brown skin and natural coils is reaching up toward the ball with wonder on their face. {NICK_STYLE}",
        "duration_sec": 12
    },
    {
        "id": "question_pause",
        "text": "Do you know why? ... Think about it for a second. ... It's because of something called GRAVITY!",
        "scene_prompt": f"Close-up of an adorable animated kindergarten child (5-6 years old, medium brown skin, curly hair, big bright eyes) with a thinking expression, finger on chin, question marks and colorful stars floating around their head in a playful way. Warm orange and yellow background glow. {NICK_STYLE}",
        "duration_sec": 8
    },
    {
        "id": "explain_gravity",
        "text": "Gravity is like an invisible hug from the Earth! The Earth is always pulling everything down toward the ground — you, me, your toys, even raindrops! Gravity never takes a break!",
        "scene_prompt": f"A beautiful animated scene showing the Earth from a slight angle with cute colorful arrows gently curving down toward it from all directions. Small animated objects falling gently — a ball, a raindrop, a leaf, a toy block — each with a trail of sparkles. Warm saturated colors, the Earth shown with lush greens and deep blues. Soft golden light from the sun. {NICK_STYLE}",
        "duration_sec": 12
    },
    {
        "id": "experiment",
        "text": "Now here's the cool part! Watch what happens when we drop a ball from down LOW... it falls kind of slow. But when we drop it from way UP HIGH... WHOOOOSH! It falls super fast! The higher you drop it, the faster it goes!",
        "scene_prompt": f"A split-scene animated illustration. Left side: an animated child (dark skin, braids) holding an orange ball at knee height with a small gentle downward arrow. Right side: the same child holding the ball above their head with a big dramatic downward arrow and speed lines. Both scenes in a bright classroom. The arrows are bright green with sparkle effects. {NICK_STYLE}",
        "duration_sec": 14
    },
    {
        "id": "model_reveal",
        "text": "Scientists call this a MODEL! Drop Height goes UP... and Fall Speed goes UP too! They go the same way — that's called a POSITIVE connection! Can you say 'positive'? ... Great job!",
        "scene_prompt": f"A simple, beautiful animated diagram showing two big colorful circles — one orange labeled-concept circle on the left (representing Drop Height with an UP arrow inside) connected by a bright green sparkly arrow to a blue circle on the right (representing Fall Speed with an UP arrow inside). A big golden plus sign floats above the arrow. Background is a soft warm gradient. Everything is big, clear, and child-friendly. {NICK_STYLE}",
        "duration_sec": 13
    },
    {
        "id": "closing",
        "text": "Now YOU know a science secret! Gravity pulls everything down, and the higher you drop something, the faster it falls! Next time you drop a ball, you'll know exactly why. You're a scientist now! Bye, friend!",
        "scene_prompt": f"A joyful animated scene of diverse kindergarten children (5-6 years old, various skin tones and hair textures) jumping and celebrating with arms up, colorful confetti and stars bursting around them. One child in the center (dark brown skin, big afro) is holding a bright orange ball triumphantly. Warm golden light, vibrant colors, pure joy and excitement. {NICK_STYLE}",
        "duration_sec": 13
    }
]


def generate_hume_narration(text, voice_id, output_path):
    """Generate narration using Hume Octave TTS with Blue's Clues warm style."""
    # Replace ... with actual pause markers
    # Hume handles natural pausing with punctuation
    clean_text = text.replace(" ... ", "... ").strip()

    url = "https://api.hume.ai/v0/tts"
    headers = {
        "X-Hume-Api-Key": HUME_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "utterances": [
            {
                "text": clean_text,
                "description": "Warm, nurturing, excited children's show host. Speaking directly to one child. Slow pace, clear enunciation, genuine wonder and encouragement. Like a favorite teacher reading a story.",
                "voice": {"id": voice_id},
                "speed": 0.85  # Slightly slower for young kids
            }
        ],
        "format": {
            "type": "wav"
        }
    }

    print(f"  Generating narration: {output_path}")
    resp = requests.post(url, headers=headers, json=payload, timeout=60)
    if resp.status_code != 200:
        print(f"  ERROR: Hume TTS returned {resp.status_code}: {resp.text[:200]}")
        return False

    data = resp.json()
    audio_b64 = data["generations"][0]["audio"]
    audio_bytes = base64.b64decode(audio_b64)

    with open(output_path, "wb") as f:
        f.write(audio_bytes)
    print(f"  OK: {os.path.basename(output_path)} ({len(audio_bytes)} bytes)")
    return True


def generate_imagen_scene(prompt, output_path):
    """Generate a scene image using NanoBanana (Gemini 2.5 Flash Image) or Imagen 4."""
    # Primary: NanoBanana (gemini-2.5-flash-image) via generateContent
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent?key={GOOGLE_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": f"Generate this image: {prompt}"}]}],
        "generationConfig": {"responseModalities": ["IMAGE", "TEXT"]}
    }

    print(f"  Generating image: {os.path.basename(output_path)}")
    resp = requests.post(url, headers=headers, json=payload, timeout=120)
    if resp.status_code == 200:
        data = resp.json()
        for part in data.get("candidates", [{}])[0].get("content", {}).get("parts", []):
            if "inlineData" in part:
                img_bytes = base64.b64decode(part["inlineData"]["data"])
                with open(output_path, "wb") as f:
                    f.write(img_bytes)
                print(f"  OK (NanoBanana): {os.path.basename(output_path)} ({len(img_bytes)} bytes)")
                return True

    # Fallback: Imagen 4 via predict
    print(f"  NanoBanana failed ({resp.status_code}), trying Imagen 4...")
    url2 = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={GOOGLE_KEY}"
    payload2 = {
        "instances": [{"prompt": prompt}],
        "parameters": {
            "sampleCount": 1,
            "outputOptions": {"mimeType": "image/png"}
        }
    }
    resp2 = requests.post(url2, headers=headers, json=payload2, timeout=120)
    if resp2.status_code == 200:
        data = resp2.json()
        img_b64 = data["predictions"][0]["bytesBase64Encoded"]
        img_bytes = base64.b64decode(img_b64)
        with open(output_path, "wb") as f:
            f.write(img_bytes)
        print(f"  OK (Imagen 4): {os.path.basename(output_path)} ({len(img_bytes)} bytes)")
        return True

    print(f"  ERROR: Both image gens failed. NanoBanana: {resp.status_code}, Imagen4: {resp2.status_code}: {resp2.text[:200]}")
    return False


def animate_with_veo(image_path, prompt, output_path):
    """Animate a scene image using Google Veo 3.1."""
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()

    # Determine mime type
    mime = "image/png" if image_path.endswith(".png") else "image/jpeg"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/veo-3.1-generate-preview:predictLongRunning?key={GOOGLE_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "instances": [{
            "prompt": f"Gentle, smooth animation for children's educational show. {prompt} Slow, calming movement. No sudden jumps. Warm lighting.",
            "image": {
                "bytesBase64Encoded": img_b64,
                "mimeType": mime
            }
        }],
        "parameters": {
            "sampleCount": 1,
            "durationSeconds": 5,
            "aspectRatio": "16:9"
        }
    }

    print(f"  Submitting Veo animation: {os.path.basename(output_path)}")
    resp = requests.post(url, headers=headers, json=payload, timeout=120)
    if resp.status_code != 200:
        print(f"  ERROR: Veo returned {resp.status_code}: {resp.text[:300]}")
        return None

    data = resp.json()
    op_name = data.get("name")
    if not op_name:
        print(f"  ERROR: No operation name in Veo response: {json.dumps(data)[:300]}")
        return None

    print(f"  Veo operation: {op_name}")
    return op_name


def poll_veo(op_name, output_path, max_wait=600):
    """Poll for Veo operation completion."""
    url = f"https://generativelanguage.googleapis.com/v1beta/{op_name}?key={GOOGLE_KEY}"
    start = time.time()

    while time.time() - start < max_wait:
        resp = requests.get(url, timeout=30)
        data = resp.json()

        if data.get("done"):
            # Extract video
            vids = data.get("response", {}).get("generatedSamples", [])
            if vids:
                vid_b64 = vids[0].get("video", {}).get("bytesBase64Encoded")
                if vid_b64:
                    vid_bytes = base64.b64decode(vid_b64)
                    with open(output_path, "wb") as f:
                        f.write(vid_bytes)
                    print(f"  OK: {os.path.basename(output_path)} ({len(vid_bytes)} bytes)")
                    return True
                # Check for URI
                vid_uri = vids[0].get("video", {}).get("uri")
                if vid_uri:
                    print(f"  Video URI: {vid_uri}")
                    vid_resp = requests.get(vid_uri, timeout=120)
                    with open(output_path, "wb") as f:
                        f.write(vid_resp.content)
                    print(f"  OK: {os.path.basename(output_path)} ({len(vid_resp.content)} bytes)")
                    return True
            print(f"  ERROR: Veo done but no video data: {json.dumps(data)[:500]}")
            return False

        if data.get("error"):
            print(f"  ERROR: Veo operation failed: {data['error']}")
            return False

        progress = data.get("metadata", {}).get("progressPercent", "?")
        print(f"  Polling Veo... {progress}% ({int(time.time()-start)}s)")
        time.sleep(15)

    print(f"  ERROR: Veo timed out after {max_wait}s")
    return False


def animate_with_grok(image_path, prompt, output_path):
    """Animate a scene image using Grok Imagine Video."""
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()

    mime = "image/png" if image_path.endswith(".png") else "image/jpeg"

    url = "https://api.x.ai/v1/videos/generations"
    headers = {
        "Authorization": f"Bearer {GROK_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "grok-imagine-video",
        "prompt": f"Gentle, smooth animation for children's educational show. {prompt} Slow, calming movement. Warm lighting. High quality smooth animation.",
        "image": {
            "url": f"data:{mime};base64,{img_b64}"
        },
        "duration": 5,
        "aspect_ratio": "16:9",
        "resolution": "720p"
    }

    print(f"  Submitting Grok animation: {os.path.basename(output_path)}")
    resp = requests.post(url, headers=headers, json=payload, timeout=120)
    if resp.status_code not in (200, 202):
        print(f"  ERROR: Grok returned {resp.status_code}: {resp.text[:300]}")
        return None

    data = resp.json()
    request_id = data.get("request_id") or data.get("id")
    if not request_id:
        # Check if video is ready immediately
        vid_url = data.get("video", {}).get("url")
        if vid_url:
            vid_resp = requests.get(vid_url, timeout=120)
            with open(output_path, "wb") as f:
                f.write(vid_resp.content)
            print(f"  OK (immediate): {os.path.basename(output_path)}")
            return "done"
        print(f"  ERROR: No request_id: {json.dumps(data)[:300]}")
        return None

    print(f"  Grok request: {request_id}")
    return request_id


def poll_grok(request_id, output_path, max_wait=600):
    """Poll for Grok video completion."""
    if request_id == "done":
        return True

    url = f"https://api.x.ai/v1/videos/{request_id}"
    headers = {"Authorization": f"Bearer {GROK_KEY}"}
    start = time.time()

    while time.time() - start < max_wait:
        resp = requests.get(url, headers=headers, timeout=30)

        if resp.status_code == 200:
            data = resp.json()
            vid_url = data.get("video", {}).get("url")
            if vid_url:
                vid_resp = requests.get(vid_url, timeout=120)
                with open(output_path, "wb") as f:
                    f.write(vid_resp.content)
                print(f"  OK: {os.path.basename(output_path)} ({len(vid_resp.content)} bytes)")
                return True
            # Maybe still processing
            status = data.get("status", "unknown")
            print(f"  Grok status: {status} ({int(time.time()-start)}s)")
        elif resp.status_code == 202:
            print(f"  Grok still processing... ({int(time.time()-start)}s)")
        else:
            print(f"  Grok poll error {resp.status_code}: {resp.text[:200]}")

        time.sleep(15)

    print(f"  ERROR: Grok timed out after {max_wait}s")
    return False


def main():
    print("=" * 60)
    print("K-3 Video Sample Generator — GK-L01 'Why Do Things Fall Down?'")
    print("=" * 60)

    veo_dir = os.path.join(SAMPLE_DIR, "GK-L01-veo")
    grok_dir = os.path.join(SAMPLE_DIR, "GK-L01-grok")
    os.makedirs(veo_dir, exist_ok=True)
    os.makedirs(grok_dir, exist_ok=True)

    # Voice: Caring Mother (warm, American, mid-age — perfect for K)
    VOICE_ID = "97fe9008-8584-4d56-8453-bd8c7ead3663"

    # ─── Step 1: Generate narration for all segments ───
    print("\n[1/4] Generating Hume TTS narration (Caring Mother voice)...")
    narration_files = []
    for seg in NARRATION_SEGMENTS:
        wav_path = os.path.join(veo_dir, f"narration_{seg['id']}.wav")
        if os.path.exists(wav_path) and os.path.getsize(wav_path) > 1000:
            print(f"  SKIP (exists): {os.path.basename(wav_path)}")
        else:
            generate_hume_narration(seg["text"], VOICE_ID, wav_path)
        narration_files.append(wav_path)
        # Copy to grok dir too
        grok_wav = os.path.join(grok_dir, f"narration_{seg['id']}.wav")
        if os.path.exists(wav_path) and not os.path.exists(grok_wav):
            import shutil
            shutil.copy2(wav_path, grok_wav)

    # ─── Step 2: Generate scene images ───
    print("\n[2/4] Generating Nickelodeon-quality scene images (Imagen/Gemini)...")
    image_files = []
    for seg in NARRATION_SEGMENTS:
        img_path = os.path.join(veo_dir, f"scene_{seg['id']}.png")
        if os.path.exists(img_path) and os.path.getsize(img_path) > 10000:
            print(f"  SKIP (exists): {os.path.basename(img_path)}")
        else:
            generate_imagen_scene(seg["scene_prompt"], img_path)
            time.sleep(2)  # Rate limit courtesy
        image_files.append(img_path)

    # ─── Step 3: Animate with both Veo and Grok ───
    print("\n[3/4] Submitting animations to Veo 3.1 AND Grok Imagine Video...")

    animation_prompts = [
        "Children sitting in circle, one child reaches toward a floating ball. Camera slowly zooms in. Ball gently bobs.",
        "Child's face showing wonder, thinking expression. Subtle head tilt. Question marks gently float and sparkle.",
        "Earth slowly rotating. Small objects gently falling toward it with sparkle trails. Calm, mesmerizing motion.",
        "Side-by-side: ball dropping from low height slowly, ball dropping from high height quickly. Speed lines animate.",
        "Two colorful circles gently pulsing. Arrow between them glows and sparkles. Plus sign rotates slowly.",
        "Children jumping and celebrating. Confetti falling. Arms waving. Pure joy and movement. Ball bouncing."
    ]

    veo_ops = []
    grok_ops = []

    for i, seg in enumerate(NARRATION_SEGMENTS):
        img_path = os.path.join(veo_dir, f"scene_{seg['id']}.png")

        if not os.path.exists(img_path):
            print(f"  SKIP animation (no image): {seg['id']}")
            veo_ops.append(None)
            grok_ops.append(None)
            continue

        # Submit Veo
        veo_out = os.path.join(veo_dir, f"clip_{seg['id']}.mp4")
        if os.path.exists(veo_out) and os.path.getsize(veo_out) > 10000:
            print(f"  SKIP Veo (exists): clip_{seg['id']}.mp4")
            veo_ops.append("done")
        else:
            op = animate_with_veo(img_path, animation_prompts[i], veo_out)
            veo_ops.append(op)

        time.sleep(2)

        # Submit Grok
        grok_out = os.path.join(grok_dir, f"clip_{seg['id']}.mp4")
        if os.path.exists(grok_out) and os.path.getsize(grok_out) > 10000:
            print(f"  SKIP Grok (exists): clip_{seg['id']}.mp4")
            grok_ops.append("done")
        else:
            op = animate_with_grok(img_path, animation_prompts[i], grok_out)
            grok_ops.append(op)

        time.sleep(2)

    # ─── Step 4: Poll for completions ───
    print("\n[4/4] Waiting for animations to complete...")

    for i, seg in enumerate(NARRATION_SEGMENTS):
        # Poll Veo
        if veo_ops[i] and veo_ops[i] != "done":
            veo_out = os.path.join(veo_dir, f"clip_{seg['id']}.mp4")
            print(f"\n  Polling Veo clip: {seg['id']}")
            poll_veo(veo_ops[i], veo_out)

        # Poll Grok
        if grok_ops[i] and grok_ops[i] != "done":
            grok_out = os.path.join(grok_dir, f"clip_{seg['id']}.mp4")
            print(f"\n  Polling Grok clip: {seg['id']}")
            poll_grok(grok_ops[i], grok_out)

    # ─── Summary ───
    print("\n" + "=" * 60)
    print("GENERATION COMPLETE")
    print("=" * 60)

    for label, d in [("Veo 3.1", veo_dir), ("Grok", grok_dir)]:
        clips = [f for f in os.listdir(d) if f.startswith("clip_") and f.endswith(".mp4")]
        wavs = [f for f in os.listdir(d) if f.endswith(".wav")]
        imgs = [f for f in os.listdir(d) if f.endswith(".png")]
        print(f"\n{label} ({d}):")
        print(f"  Images: {len(imgs)}")
        print(f"  Narration: {len(wavs)} WAV files")
        print(f"  Video clips: {len(clips)} MP4 files")

    print("\nNext step: Use ffmpeg to combine clips + narration into final videos")
    print("Then serve via local HTTP server for direct links")


if __name__ == "__main__":
    main()
