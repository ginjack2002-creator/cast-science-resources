#!/usr/bin/env python3
"""Upload Grade 6 & 7 videos to GitHub Release and YouTube via Blotato."""
import os, sys, json, time, subprocess, requests
from pathlib import Path

import dotenv
dotenv.load_dotenv(Path.home() / '.env')

BLOTATO_API_KEY = os.environ.get('BLOTATO_API_KEY', '')
HEADERS = {'blotato-api-key': BLOTATO_API_KEY, 'Content-Type': 'application/json'}
BASE = 'https://backend.blotato.com/v2'
YOUTUBE_ACCOUNT = "28826"
VIDEOS_DIR = Path.home() / 'remotion-studio' / 'out'
PUBLIC_DIR = Path.home() / 'remotion-studio' / 'public'
CAST_DIR = Path.home() / 'cast-science-resources'
GITHUB_REPO = "alexandriasworld1234-source/remotion-studio"
RELEASE_TAG = "v1.1-cast-videos-g06-g07"

sys.path.insert(0, str(CAST_DIR / 'scripts'))


def load_lesson_data(grade):
    """Load lesson data for a grade."""
    data_file = CAST_DIR / 'scripts' / f'lesson_data_G{grade:02d}.py'
    ns = {}
    exec(data_file.read_text(encoding='utf-8'), ns)
    lessons = {}
    for i in range(1, 11):
        key = f"L{i:02d}"
        if key in ns:
            lessons[key] = ns[key]
    return lessons


def build_video_catalog():
    """Build video catalog from lesson data and narration JSONs."""
    catalog = {}

    for grade in [6, 7]:
        lessons = load_lesson_data(grade)
        for lesson_num, data in lessons.items():
            lesson_id = f"G{grade:02d}-{lesson_num}"
            filename = f"{lesson_id}.mp4"
            filepath = VIDEOS_DIR / filename

            if not filepath.exists():
                print(f"  [SKIP] {filename} not found")
                continue

            # Load narration data for career info
            narr_file = PUBLIC_DIR / 'system-videos' / lesson_id / 'narrations.json'
            narr_data = {}
            if narr_file.exists():
                narr_data = json.loads(narr_file.read_text(encoding='utf-8'))

            # Extract components as vocab
            vocab = [c[0] for c in data.get('components', [])]

            # Extract careers
            career_str = data.get('career', '')
            c1 = narr_data.get('career1_title', '')
            c2 = narr_data.get('career2_title', '')
            careers = [c for c in [c1, c2] if c]
            if not careers and career_str:
                careers = [career_str.split(' and ')[0].strip()[:30]]

            catalog[filename] = {
                "title": data.get('title', ''),
                "grade": f"Grade {grade}",
                "lesson": lesson_num,
                "ngss": data.get('ngss', ''),
                "topic": data.get('subtitle', ''),
                "vocab": vocab,
                "desc": data.get('answer', data.get('big_question', '')),
                "hook": data.get('big_question', ''),
                "careers": careers,
            }

    return catalog


def build_youtube_description(v):
    """Build SEO-optimized YouTube description."""
    lines = [
        f"{v['hook']}",
        "",
        f"{v['desc']}",
        "",
        f"NGSS Standard: {v['ngss']}",
        f"California CAST Aligned | Lesson available mid-March 2026",
        "",
        f"Key Vocabulary: {', '.join(v['vocab'])}",
        "",
        f"STEM Careers: {', '.join(v['careers'])}",
        "",
        "Build. Simulate. Understand.",
        "Try ModelIt! free: https://modelit.io",
        "",
        "#ModelIt #NGSS #STEM #Science #SystemsThinking #MiddleSchool",
        f"#{v['grade'].replace(' ', '')} #CASTeducation #ScienceEducation",
    ]
    return "\n".join(lines)


def get_release_url(filename):
    """Get the GitHub release download URL for a video file."""
    return f"https://github.com/{GITHUB_REPO}/releases/download/{RELEASE_TAG}/{filename}"


def create_release():
    """Create GitHub release for G06/G07 videos."""
    print("\n=== Creating GitHub Release ===")
    result = subprocess.run(
        ["gh", "release", "create", RELEASE_TAG,
         "--repo", GITHUB_REPO,
         "--title", "CAST Science Videos — Grade 6 & 7",
         "--notes", "Grade 6 and Grade 7 'Everything is a System!' lesson intro videos"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        print(f"  [OK] Release created: {RELEASE_TAG}")
        return True
    elif "already exists" in result.stderr:
        print(f"  [OK] Release already exists: {RELEASE_TAG}")
        return True
    else:
        print(f"  [ERROR] {result.stderr[:200]}")
        return False


def upload_to_release(catalog):
    """Upload video files to GitHub release."""
    print("\n=== Uploading to GitHub Release ===")
    files = list(catalog.keys())

    # Upload in batches of 5
    for i in range(0, len(files), 5):
        batch = files[i:i+5]
        paths = [str(VIDEOS_DIR / f) for f in batch]
        cmd = ["gh", "release", "upload", RELEASE_TAG, "--repo", GITHUB_REPO, "--clobber"] + paths

        print(f"  Batch {i//5 + 1}: {', '.join(batch)}")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        if result.returncode == 0:
            print(f"    [OK] Uploaded {len(batch)} files")
        else:
            print(f"    [ERROR] {result.stderr[:200]}")
        time.sleep(2)


def post_to_youtube(catalog):
    """Post videos to YouTube via Blotato."""
    print("\n=== Posting to YouTube ===")
    success = 0

    for i, (filename, v) in enumerate(catalog.items()):
        video_url = get_release_url(filename)
        yt_title = f"{v['title']} | {v['grade']} Science | {v['ngss']}"
        if len(yt_title) > 100:
            yt_title = f"{v['title']} | {v['grade']} | {v['ngss']}"
        if len(yt_title) > 100:
            yt_title = v['title'][:100]

        yt_desc = build_youtube_description(v)

        payload = {
            "post": {
                "accountId": YOUTUBE_ACCOUNT,
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
            }
        }

        resp = requests.post(f"{BASE}/posts", headers=HEADERS, json=payload, timeout=60)
        if resp.status_code in (200, 201):
            sid = resp.json().get("postSubmissionId", "")
            print(f"  [{i+1}/{len(catalog)}] POSTED: {filename} -> {sid}")
            success += 1
        else:
            err = resp.text[:150]
            if "maximum number" in err.lower() or "limit" in err.lower():
                print(f"  [{i+1}/{len(catalog)}] RATE LIMITED: {filename}")
                print(f"    Scheduling remaining videos for tomorrow...")
                schedule_remaining(catalog, list(catalog.keys())[i:])
                return success
            else:
                print(f"  [{i+1}/{len(catalog)}] ERROR: {resp.status_code} {err}")
        time.sleep(3)

    print(f"\n  YouTube: {success}/{len(catalog)} posted")
    return success


def schedule_remaining(catalog, remaining_files):
    """Schedule remaining videos for 25 hours from now."""
    from datetime import datetime, timedelta, timezone
    schedule_time = (datetime.now(timezone.utc) + timedelta(hours=25)).strftime('%Y-%m-%dT%H:%M:%SZ')
    print(f"\n  Scheduling {len(remaining_files)} videos for: {schedule_time}")

    success = 0
    for i, filename in enumerate(remaining_files):
        v = catalog[filename]
        video_url = get_release_url(filename)
        yt_title = f"{v['title']} | {v['grade']} Science | {v['ngss']}"
        if len(yt_title) > 100:
            yt_title = f"{v['title']} | {v['grade']} | {v['ngss']}"

        yt_desc = build_youtube_description(v)

        payload = {
            "post": {
                "accountId": YOUTUBE_ACCOUNT,
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
            print(f"    [{i+1}/{len(remaining_files)}] SCHEDULED: {filename} -> {sid}")
            success += 1
        else:
            print(f"    [{i+1}/{len(remaining_files)}] ERROR: {resp.status_code} {resp.text[:150]}")
        time.sleep(2)

    print(f"  Scheduled: {success}/{len(remaining_files)}")


if __name__ == '__main__':
    catalog = build_video_catalog()
    print(f"Video catalog: {len(catalog)} videos")
    for f, v in catalog.items():
        print(f"  {f}: {v['title']} ({v['grade']}, {v['ngss']})")

    # Step 1: Create GitHub release
    create_release()

    # Step 2: Upload videos to release
    upload_to_release(catalog)

    # Step 3: Post to YouTube
    post_to_youtube(catalog)

    print("\n=== DONE ===")
