#!/usr/bin/env python3
"""Quick test of Veo 3.1 API with image-to-video."""
import os, requests, base64, json, time
from dotenv import load_dotenv
load_dotenv(os.path.expanduser("~/.env"))

KEY = os.getenv("GOOGLE_AI_STUDIO_API_KEY")
img_path = os.path.expanduser("~/cast-science-resources/videos/samples/GK-L01-veo/scene_intro.png")

with open(img_path, "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode()

print(f"Image size: {len(img_b64)} chars base64")

# Try Veo 3.1
url = f"https://generativelanguage.googleapis.com/v1beta/models/veo-3.1-generate-preview:predictLongRunning?key={KEY}"
payload = {
    "instances": [{
        "prompt": "Gentle smooth animation. Children sitting in circle, one child reaches toward a floating ball. Camera slowly zooms in. Ball gently bobs. Warm lighting.",
        "image": {
            "bytesBase64Encoded": img_b64,
            "mimeType": "image/png"
        }
    }],
    "parameters": {
        "sampleCount": 1,
        "durationSeconds": 6,
        "aspectRatio": "16:9"
    }
}

print("Submitting to Veo 3.1...")
resp = requests.post(url, json=payload, timeout=120)
print(f"Status: {resp.status_code}")
data = resp.json()
print(json.dumps(data, indent=2)[:1000])

if resp.status_code == 200:
    op_name = data.get("name")
    print(f"\nOperation: {op_name}")

    # Poll
    for i in range(40):
        time.sleep(15)
        poll_url = f"https://generativelanguage.googleapis.com/v1beta/{op_name}?key={KEY}"
        pr = requests.get(poll_url, timeout=30)
        pd = pr.json()
        if pd.get("done"):
            print("DONE!")
            vids = pd.get("response", {}).get("generatedSamples", [])
            if vids:
                vid_b64 = vids[0].get("video", {}).get("bytesBase64Encoded")
                if vid_b64:
                    out = os.path.expanduser("~/cast-science-resources/videos/samples/GK-L01-veo/clip_intro.mp4")
                    with open(out, "wb") as f:
                        f.write(base64.b64decode(vid_b64))
                    print(f"Saved: {out}")
                else:
                    print(f"No b64 data. Keys: {list(vids[0].get('video', {}).keys())}")
                    print(json.dumps(pd, indent=2)[:2000])
            else:
                print(f"No samples. Response: {json.dumps(pd, indent=2)[:2000]}")
            break
        if pd.get("error"):
            print(f"ERROR: {pd['error']}")
            break
        pct = pd.get("metadata", {}).get("progressPercent", "?")
        print(f"  Polling... {pct}% ({(i+1)*15}s)")
