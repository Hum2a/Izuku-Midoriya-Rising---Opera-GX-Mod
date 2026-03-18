#!/usr/bin/env python3
"""Extract first frame from video as PNG - no ffmpeg required."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIDEO = ROOT / "wallpaper" / "dark.webm"
OUT_DARK = ROOT / "wallpaper" / "dark.png"
OUT_LIGHT = ROOT / "wallpaper" / "light.png"


def main():
    try:
        import cv2
    except ImportError:
        print("Installing opencv-python...")
        import subprocess
        subprocess.check_call(["pip", "install", "opencv-python", "-q"])
        import cv2

    if not VIDEO.exists():
        print(f"Video not found: {VIDEO}")
        return

    cap = cv2.VideoCapture(str(VIDEO))
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Could not read frame from video")
        return

    cv2.imwrite(str(OUT_DARK), frame)
    cv2.imwrite(str(OUT_LIGHT), frame)
    print(f"Extracted first frame to {OUT_DARK.relative_to(ROOT)} and {OUT_LIGHT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
