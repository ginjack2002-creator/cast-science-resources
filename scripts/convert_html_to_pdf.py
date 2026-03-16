#!/usr/bin/env python3
"""Batch convert all branded HTML materials to PDF using headless Chrome."""

import subprocess
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

MATERIALS_DIR = Path.home() / "cast-science-resources" / "materials"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


def convert_one(html_path: Path) -> tuple[str, bool]:
    """Convert a single HTML file to PDF. Returns (path, success)."""
    pdf_path = html_path.with_suffix(".pdf")

    # Skip if PDF already exists and is newer than HTML
    if pdf_path.exists() and pdf_path.stat().st_mtime > html_path.stat().st_mtime:
        return str(pdf_path), True

    # Use file:// URI for Chrome
    file_uri = html_path.as_uri()

    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-extensions",
        "--run-all-compositor-stages-before-draw",
        "--print-to-pdf=" + str(pdf_path),
        "--print-to-pdf-no-header",
        file_uri,
    ]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=30
        )
        if pdf_path.exists() and pdf_path.stat().st_size > 0:
            return str(pdf_path), True
        else:
            return str(html_path) + " FAILED: no output", False
    except subprocess.TimeoutExpired:
        return str(html_path) + " TIMEOUT", False
    except Exception as e:
        return str(html_path) + f" ERROR: {e}", False


def main():
    # Find all branded HTML files (Student-Activity-Pack and Teachers-Guide)
    html_files = []
    for html in MATERIALS_DIR.rglob("*.html"):
        name = html.name.lower()
        if "student-activity-pack" in name or "teachers-guide" in name:
            html_files.append(html)

    print(f"Found {len(html_files)} HTML files to convert")

    success = 0
    failed = 0

    # Process sequentially (Chrome headless doesn't parallelize well)
    for i, html in enumerate(sorted(html_files)):
        msg, ok = convert_one(html)
        if ok:
            success += 1
        else:
            failed += 1
            print(f"  FAIL: {msg}")

        if (i + 1) % 20 == 0:
            print(f"  Progress: {i+1}/{len(html_files)} ({success} ok, {failed} failed)")

    print(f"\nDONE: {success} converted, {failed} failed out of {len(html_files)} total")


if __name__ == "__main__":
    main()
