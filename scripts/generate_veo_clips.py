#!/usr/bin/env python3
"""Generate all 6 Veo 3.1 clips for GK-L01 sample video."""
import os, requests, base64, json, time
from dotenv import load_dotenv
load_dotenv(os.path.expanduser("~/.env"))

KEY = os.getenv("GOOGLE_AI_STUDIO_API_KEY")
VEO_DIR = os.path.expanduser("~/cast-science-resources/videos/samples/GK-L01-veo")

SEGMENTS = [
    ("intro", "Gentle smooth animation. Children sitting in circle, one child reaches toward a floating ball. Camera slowly zooms in. Ball gently bobs. Warm lighting."),
    ("question_pause", "Gentle animation. Child's thinking face. Subtle head tilt. Question marks and stars gently float and sparkle around their head."),
    ("explain_gravity", "Smooth gentle animation. Earth slowly rotating. Small colorful objects falling gently toward it with sparkle trails. Calm, mesmerizing motion."),
    ("experiment", "Smooth animation. Side-by-side: ball dropping from low height slowly on left, ball dropping from high height quickly on right. Speed lines animate."),
    ("model_reveal", "Gentle animation. Two colorful circles gently pulsing. Arrow between them glows and sparkles. Plus sign rotates slowly. Diagram comes alive."),
    ("closing", "Joyful animation. Children jumping and celebrating. Confetti falling. Arms waving. Pure joy and movement. Ball bouncing.")
]

def submit_veo(img_path, prompt):
    with open(img_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()

    url = f"https://generativelanguage.googleapis.com/v1beta/models/veo-3.1-generate-preview:predictLongRunning?key={KEY}"
    payload = {
        "instances": [{
            "prompt": prompt,
            "image": {"bytesBase64Encoded": img_b64, "mimeType": "image/png"}
        }],
        "parameters": {"sampleCount": 1, "durationSeconds": 6, "aspectRatio": "16:9"}
    }
    resp = requests.post(url, json=payload, timeout=120)
    if resp.status_code != 200:
        print(f"  ERROR: {resp.status_code}: {resp.text[:200]}")
        return None
    return resp.json().get("name")

def poll_and_download(op_name, output_path, max_wait=300):
    start = time.time()
    while time.time() - start < max_wait:
        resp = requests.get(f"https://generativelanguage.googleapis.com/v1beta/{op_name}?key={KEY}", timeout=30)
        data = resp.json()
        if data.get("done"):
            # Navigate to video URI
            samples = data.get("response", {}).get("generateVideoResponse", {}).get("generatedSamples", [])
            if not samples:
                samples = data.get("response", {}).get("generatedSamples", [])
            if samples:
                uri = samples[0].get("video", {}).get("uri")
                if uri:
                    dl_url = f"{uri}&key={KEY}"
                    vid_resp = requests.get(dl_url, timeout=120, allow_redirects=True)
                    with open(output_path, "wb") as f:
                        f.write(vid_resp.content)
                    print(f"  OK: {os.path.basename(output_path)} ({len(vid_resp.content)} bytes)")
                    return True
                b64 = samples[0].get("video", {}).get("bytesBase64Encoded")
                if b64:
                    with open(output_path, "wb") as f:
                        f.write(base64.b64decode(b64))
                    print(f"  OK (b64): {os.path.basename(output_path)}")
                    return True
            print(f"  ERROR: Done but no video. Response keys: {list(data.get('response', {}).keys())}")
            print(f"  Full response: {json.dumps(data, indent=2)[:500]}")
            return False
        if data.get("error"):
            print(f"  ERROR: {data['error']}")
            return False
        elapsed = int(time.time() - start)
        print(f"  Polling... ({elapsed}s)")
        time.sleep(15)
    print(f"  TIMEOUT after {max_wait}s")
    return False

def main():
    print("Generating 6 Veo 3.1 clips for GK-L01...")

    # Submit all, then poll
    operations = []
    for seg_id, prompt in SEGMENTS:
        clip_path = os.path.join(VEO_DIR, f"clip_{seg_id}.mp4")
        img_path = os.path.join(VEO_DIR, f"scene_{seg_id}.png")

        if os.path.exists(clip_path) and os.path.getsize(clip_path) > 10000:
            print(f"  SKIP (exists): clip_{seg_id}.mp4 ({os.path.getsize(clip_path)} bytes)")
            operations.append(("done", seg_id))
            continue

        if not os.path.exists(img_path):
            print(f"  SKIP (no image): {seg_id}")
            operations.append((None, seg_id))
            continue

        print(f"  Submitting: {seg_id}")
        op = submit_veo(img_path, prompt)
        operations.append((op, seg_id))
        time.sleep(3)  # Rate limit

    # Poll for all pending operations
    print("\nPolling for completions...")
    for op_name, seg_id in operations:
        if op_name is None or op_name == "done":
            continue
        clip_path = os.path.join(VEO_DIR, f"clip_{seg_id}.mp4")
        print(f"\n  Waiting for: {seg_id} ({op_name})")
        poll_and_download(op_name, clip_path)

    # Summary
    clips = [f for f in os.listdir(VEO_DIR) if f.startswith("clip_") and f.endswith(".mp4") and os.path.getsize(os.path.join(VEO_DIR, f)) > 10000]
    print(f"\nComplete: {len(clips)}/6 Veo clips ready")
    for c in sorted(clips):
        sz = os.path.getsize(os.path.join(VEO_DIR, c))
        print(f"  {c}: {sz/1024:.0f} KB")

if __name__ == "__main__":
    main()
