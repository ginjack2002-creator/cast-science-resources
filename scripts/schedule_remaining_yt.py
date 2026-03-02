#!/usr/bin/env python3
"""Schedule the 18 remaining YouTube videos for tomorrow (after daily limit resets)."""
import os, sys, requests, time, dotenv
from pathlib import Path
from datetime import datetime, timedelta, timezone

sys.path.insert(0, str(Path(__file__).parent))
dotenv.load_dotenv(Path.home() / '.env')

from post_videos_blotato import VIDEOS, ACCOUNTS, get_release_url, build_youtube_description

BLOTATO_API_KEY = os.environ.get('BLOTATO_API_KEY', '')
HEADERS = {'blotato-api-key': BLOTATO_API_KEY, 'Content-Type': 'application/json'}
BASE = 'https://backend.blotato.com/v2'

# Videos that already published (10 of 28)
ALREADY_LIVE = {
    'G05-L01-wildfires.mp4', 'G05-L02-natures-recycling.mp4',
    'G05-L03-powered-by-sun.mp4', 'G05-L04-earths-hidden-water.mp4',
    'G05-L05-disappearing-act.mp4', 'G05-L06-tree-mass.mp4',
    'G05-L07-mushroom-network.mp4', 'G05-L08-soap-destroys-viruses.mp4',
    'G05-L09-whose-air.mp4', 'G08-L01-superbugs.mp4',
}

# Schedule 25 hours from now
schedule_time = (datetime.now(timezone.utc) + timedelta(hours=25)).strftime('%Y-%m-%dT%H:%M:%SZ')
print(f"Scheduling remaining videos for: {schedule_time}")
print(f"(That's ~25 hours from now to clear the 24h YouTube limit)\n")

remaining = [(f, v) for f, v in VIDEOS.items() if f not in ALREADY_LIVE]
print(f"Videos to schedule: {len(remaining)}\n")

success = 0
for i, (filename, v) in enumerate(remaining):
    video_url = get_release_url(filename)
    yt_title = f"{v['title']} | {v['grade']} Science | {v['ngss']}"
    if len(yt_title) > 100:
        yt_title = f"{v['title']} | {v['grade']} | {v['ngss']}"
    if len(yt_title) > 100:
        yt_title = v['title'][:100]

    yt_desc = build_youtube_description(v)

    payload = {
        "post": {
            "accountId": ACCOUNTS["youtube"],
            "content": {
                "text": yt_desc,
                "mediaUrls": [video_url],
                "platform": "youtube"
            },
            "target": {
                "targetType": "youtube",
                "title": yt_title,
                "privacyStatus": "public",
                "shouldNotifySubscribers": True
            }
        },
        "scheduledTime": schedule_time
    }

    resp = requests.post(f"{BASE}/posts", headers=HEADERS, json=payload, timeout=60)
    if resp.status_code in (200, 201):
        sid = resp.json().get("postSubmissionId", "")
        print(f"  [{i+1}/{len(remaining)}] SCHEDULED: {filename} -> {sid}")
        success += 1
    else:
        print(f"  [{i+1}/{len(remaining)}] ERROR: {resp.status_code} {resp.text[:150]}")

    time.sleep(2)

print(f"\nScheduled: {success}/{len(remaining)}")
