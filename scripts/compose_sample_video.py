#!/usr/bin/env python3
"""
Compose K-3 sample lesson video from clips + narration.
Creates a polished video with:
- Title card
- Scene clips (looped to match narration)
- Warm narration overlay
- Smooth transitions
"""

import os, subprocess, math, tempfile

BASE = os.path.expanduser("~/cast-science-resources/videos/samples")

SEGMENTS = ["intro", "question_pause", "explain_gravity", "experiment", "model_reveal", "closing"]

def get_duration(path):
    """Get media duration in seconds."""
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0", path],
        capture_output=True, text=True
    )
    return float(result.stdout.strip())

def create_title_card(output_path, duration=4):
    """Create an animated title card with CAST brand colors."""
    # Use ffmpeg to generate a title card
    subprocess.run([
        "ffmpeg", "-y",
        "-f", "lavfi", "-i",
        f"color=c=#0D1B2A:s=1280x720:d={duration}:r=30",
        "-vf",
        "drawtext=text='ModelIt! Science':fontsize=60:fontcolor=white:x=(w-text_w)/2:y=h/3-30:fontfile=C\\\\:/Windows/Fonts/comicbd.ttf,"
        "drawtext=text='Why Do Things Fall Down?':fontsize=40:fontcolor=#F69338:x=(w-text_w)/2:y=h/2:fontfile=C\\\\:/Windows/Fonts/comic.ttf,"
        "drawtext=text='Kindergarten - Lesson 1':fontsize=30:fontcolor=#7EC8E3:x=(w-text_w)/2:y=h/2+60:fontfile=C\\\\:/Windows/Fonts/comic.ttf,"
        "fade=t=in:st=0:d=1,fade=t=out:st=3:d=1",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-t", str(duration),
        output_path
    ], capture_output=True, text=True)
    return os.path.exists(output_path)

def create_end_card(output_path, duration=4):
    """Create ending card."""
    subprocess.run([
        "ffmpeg", "-y",
        "-f", "lavfi", "-i",
        f"color=c=#0D1B2A:s=1280x720:d={duration}:r=30",
        "-vf",
        "drawtext=text='You are a Scientist!':fontsize=55:fontcolor=#F69338:x=(w-text_w)/2:y=h/3:fontfile=C\\\\:/Windows/Fonts/comicbd.ttf,"
        "drawtext=text='Keep Exploring!':fontsize=40:fontcolor=white:x=(w-text_w)/2:y=h/2+20:fontfile=C\\\\:/Windows/Fonts/comic.ttf,"
        "drawtext=text='ModelIt! by Discovery Collective':fontsize=24:fontcolor=#7EC8E3:x=(w-text_w)/2:y=h*3/4:fontfile=C\\\\:/Windows/Fonts/comic.ttf,"
        "fade=t=in:st=0:d=1,fade=t=out:st=3:d=1",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-t", str(duration),
        output_path
    ], capture_output=True, text=True)
    return os.path.exists(output_path)

def compose_video(source_dir, output_name):
    """Compose full video from clips + narration in source_dir."""
    print(f"\n{'='*60}")
    print(f"Composing: {output_name}")
    print(f"Source: {source_dir}")
    print(f"{'='*60}")

    tmp = tempfile.mkdtemp()
    segment_files = []

    # Create title card
    title_path = os.path.join(tmp, "title.mp4")
    print("  Creating title card...")
    create_title_card(title_path)
    if os.path.exists(title_path):
        segment_files.append(title_path)
        print(f"  OK: title card ({get_duration(title_path):.1f}s)")

    # Process each segment
    for seg_name in SEGMENTS:
        clip_path = os.path.join(source_dir, f"clip_{seg_name}.mp4")
        narr_path = os.path.join(source_dir, f"narration_{seg_name}.wav")

        if not os.path.exists(clip_path):
            # If no clip (Veo might not have clips yet), use scene image as still
            img_path = os.path.join(BASE, "GK-L01-veo", f"scene_{seg_name}.png")
            if os.path.exists(img_path) and os.path.exists(narr_path):
                narr_dur = get_duration(narr_path)
                still_path = os.path.join(tmp, f"still_{seg_name}.mp4")
                # Create video from still image
                subprocess.run([
                    "ffmpeg", "-y",
                    "-loop", "1", "-i", img_path,
                    "-t", str(narr_dur + 1),
                    "-vf", "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,zoompan=z='min(zoom+0.001,1.15)':d=1:s=1280x720:fps=30",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
                    still_path
                ], capture_output=True, text=True)
                clip_path = still_path
            else:
                print(f"  SKIP: {seg_name} (no clip or image)")
                continue

        if not os.path.exists(narr_path):
            print(f"  SKIP: {seg_name} (no narration)")
            continue

        narr_dur = get_duration(narr_path)
        clip_dur = get_duration(clip_path)

        # Calculate how many loops needed (add 1.5s buffer for transition)
        target_dur = narr_dur + 1.5
        loops = max(1, math.ceil(target_dur / clip_dur))

        out_segment = os.path.join(tmp, f"segment_{seg_name}.mp4")

        print(f"  Processing {seg_name}: clip={clip_dur:.1f}s, narr={narr_dur:.1f}s, loops={loops}")

        # Step 1: Strip native audio from clip and loop it
        looped_clip = os.path.join(tmp, f"looped_{seg_name}.mp4")

        if loops > 1:
            # Create concat file for looping
            concat_file = os.path.join(tmp, f"concat_{seg_name}.txt")
            # First strip audio from clip
            stripped = os.path.join(tmp, f"stripped_{seg_name}.mp4")
            subprocess.run([
                "ffmpeg", "-y", "-i", clip_path, "-an", "-c:v", "copy", stripped
            ], capture_output=True, text=True)

            with open(concat_file, "w") as f:
                for _ in range(loops):
                    f.write(f"file '{stripped}'\n")

            subprocess.run([
                "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_file,
                "-t", str(target_dur),
                "-c:v", "libx264", "-pix_fmt", "yuv420p",
                looped_clip
            ], capture_output=True, text=True)
        else:
            # Just strip audio
            subprocess.run([
                "ffmpeg", "-y", "-i", clip_path, "-an",
                "-t", str(target_dur),
                "-c:v", "libx264", "-pix_fmt", "yuv420p",
                looped_clip
            ], capture_output=True, text=True)

        # Step 2: Overlay narration on looped clip with crossfade
        subprocess.run([
            "ffmpeg", "-y",
            "-i", looped_clip,
            "-i", narr_path,
            "-filter_complex",
            f"[0:v]fade=t=in:st=0:d=0.5,fade=t=out:st={target_dur-0.5}:d=0.5[v];"
            f"[1:a]adelay=500|500,afade=t=in:st=0:d=0.3,afade=t=out:st={narr_dur}:d=0.3[a]",
            "-map", "[v]", "-map", "[a]",
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k",
            "-t", str(target_dur),
            "-shortest",
            out_segment
        ], capture_output=True, text=True)

        if os.path.exists(out_segment) and os.path.getsize(out_segment) > 1000:
            segment_files.append(out_segment)
            print(f"  OK: {seg_name} segment ({get_duration(out_segment):.1f}s)")
        else:
            print(f"  ERROR: Failed to create {seg_name} segment")

    # Create end card
    end_path = os.path.join(tmp, "end.mp4")
    print("  Creating end card...")
    create_end_card(end_path)
    if os.path.exists(end_path):
        # Add silent audio track for concatenation
        end_with_audio = os.path.join(tmp, "end_audio.mp4")
        subprocess.run([
            "ffmpeg", "-y", "-i", end_path,
            "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
            "-c:v", "copy", "-c:a", "aac", "-shortest",
            end_with_audio
        ], capture_output=True, text=True)
        if os.path.exists(end_with_audio):
            segment_files.append(end_with_audio)

    # Concatenate all segments
    if len(segment_files) < 2:
        print("  ERROR: Not enough segments to concatenate")
        return None

    # Need to re-encode all to same format first
    normalized = []
    for i, sf in enumerate(segment_files):
        norm_path = os.path.join(tmp, f"norm_{i:02d}.mp4")
        # Check if file has audio
        probe = subprocess.run(
            ["ffprobe", "-v", "quiet", "-show_streams", "-select_streams", "a", sf],
            capture_output=True, text=True
        )
        has_audio = "codec_type=audio" in probe.stdout

        if has_audio:
            subprocess.run([
                "ffmpeg", "-y", "-i", sf,
                "-vf", "scale=1280:720,fps=30,format=yuv420p",
                "-c:v", "libx264", "-preset", "medium", "-crf", "23",
                "-ar", "44100", "-ac", "2", "-c:a", "aac", "-b:a", "192k",
                norm_path
            ], capture_output=True, text=True)
        else:
            subprocess.run([
                "ffmpeg", "-y", "-i", sf,
                "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
                "-vf", "scale=1280:720,fps=30,format=yuv420p",
                "-c:v", "libx264", "-preset", "medium", "-crf", "23",
                "-ar", "44100", "-ac", "2", "-c:a", "aac", "-b:a", "192k",
                "-shortest",
                norm_path
            ], capture_output=True, text=True)

        if os.path.exists(norm_path) and os.path.getsize(norm_path) > 1000:
            normalized.append(norm_path)

    concat_list = os.path.join(tmp, "final_concat.txt")
    with open(concat_list, "w") as f:
        for nf in normalized:
            f.write(f"file '{nf}'\n")

    output_path = os.path.join(BASE, output_name)
    print(f"\n  Concatenating {len(normalized)} segments into final video...")
    result = subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list,
        "-c:v", "libx264", "-preset", "medium", "-crf", "22",
        "-c:a", "aac", "-b:a", "192k",
        output_path
    ], capture_output=True, text=True)

    if os.path.exists(output_path) and os.path.getsize(output_path) > 10000:
        final_dur = get_duration(output_path)
        size_mb = os.path.getsize(output_path) / (1024*1024)
        print(f"\n  FINAL VIDEO: {output_path}")
        print(f"  Duration: {final_dur:.1f}s ({final_dur/60:.1f} min)")
        print(f"  Size: {size_mb:.1f} MB")
        return output_path
    else:
        print(f"  ERROR: Final concatenation failed")
        if result.stderr:
            print(f"  stderr: {result.stderr[:500]}")
        return None


if __name__ == "__main__":
    # Compose Grok version
    grok_dir = os.path.join(BASE, "GK-L01-grok")
    compose_video(grok_dir, "GK-L01-Grok-Sample.mp4")

    # Compose Veo version (if clips exist)
    veo_dir = os.path.join(BASE, "GK-L01-veo")
    veo_clips = [f for f in os.listdir(veo_dir) if f.startswith("clip_") and f.endswith(".mp4")]
    if veo_clips:
        compose_video(veo_dir, "GK-L01-Veo-Sample.mp4")
    else:
        print("\nVeo clips not yet ready - composing still-image version from scene images...")
        compose_video(veo_dir, "GK-L01-Veo-StillImage-Sample.mp4")
