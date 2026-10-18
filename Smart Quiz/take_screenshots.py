"""
Smart Quiz - Automated Screenshot Capture Utility
Captures high-resolution, pixel-perfect screenshots of both:
1. PC / Desktop Version (1366x768 / 1280x800)
2. Android Mobile Version (412x915 Pixel/Galaxy viewport)
using the built-in Microsoft Edge / Google Chrome headless engine.
"""

import os
import subprocess
import time

SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# Find Edge or Chrome executable
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

BROWSER_EXE = EDGE_PATH if os.path.exists(EDGE_PATH) else CHROME_PATH

ANDROID_UA = (
    "Mozilla/5.0 (Linux; Android 14; Pixel 7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
)

SHOTS = [
    # PC / Desktop Screenshots (1280x850)
    {
        "name": "pc_home.png",
        "url": "http://127.0.0.1:5000/",
        "width": 1280,
        "height": 820,
        "mobile": False,
        "desc": "Desktop Home Page (Hero & Categories)"
    },
    {
        "name": "pc_quiz.png",
        "url": "http://127.0.0.1:5000/quiz/2?demo_student=Rohan+Sharma",
        "width": 1280,
        "height": 820,
        "mobile": False,
        "desc": "Desktop Interactive Quiz Interface"
    },
    {
        "name": "pc_leaderboard.png",
        "url": "http://127.0.0.1:5000/history",
        "width": 1280,
        "height": 850,
        "mobile": False,
        "desc": "Desktop Leaderboard & Quiz History"
    },
    {
        "name": "pc_result.png",
        "url": "http://127.0.0.1:5000/result/21",
        "width": 1280,
        "height": 900,
        "mobile": False,
        "desc": "Desktop Quiz Results, Score Card & Explanations"
    },
    {
        "name": "pc_about.png",
        "url": "http://127.0.0.1:5000/about",
        "width": 1280,
        "height": 850,
        "mobile": False,
        "desc": "Desktop DBMS Documentation & Viva Guide"
    },

    # Android Mobile Screenshots (412x915)
    {
        "name": "android_home.png",
        "url": "http://127.0.0.1:5000/",
        "width": 412,
        "height": 892,
        "mobile": True,
        "desc": "Android Mobile Home Screen with Hamburger Menu"
    },
    {
        "name": "android_quiz.png",
        "url": "http://127.0.0.1:5000/quiz/1?demo_student=Priya+Patel",
        "width": 412,
        "height": 892,
        "mobile": True,
        "desc": "Android Mobile Quiz Question & Options View"
    },
    {
        "name": "android_result.png",
        "url": "http://127.0.0.1:5000/result/21",
        "width": 412,
        "height": 892,
        "mobile": True,
        "desc": "Android Mobile Quiz Results & Performance Badges"
    },
    {
        "name": "android_leaderboard.png",
        "url": "http://127.0.0.1:5000/history",
        "width": 412,
        "height": 892,
        "mobile": True,
        "desc": "Android Mobile Leaderboard & Scores View"
    },
    {
        "name": "android_about.png",
        "url": "http://127.0.0.1:5000/about",
        "width": 412,
        "height": 892,
        "mobile": True,
        "desc": "Android Mobile DBMS Concepts View"
    }
]


def capture_all():
    print(f"[INFO] Using browser engine: {BROWSER_EXE}")
    print(f"[INFO] Saving screenshots to: {SCREENSHOT_DIR}")

    success_count = 0
    for s in SHOTS:
        out_path = os.path.join(SCREENSHOT_DIR, s["name"])
        cmd = [
            BROWSER_EXE,
            "--headless",
            "--disable-gpu",
            "--hide-scrollbars",
            f"--window-size={s['width']},{s['height']}",
            f"--screenshot={out_path}",
        ]

        if s["mobile"]:
            cmd.append(f"--user-agent={ANDROID_UA}")

        cmd.append(s["url"])

        try:
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15)
            if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
                print(f"[SUCCESS] Captured {s['name']} ({s['desc']}) - {os.path.getsize(out_path)} bytes")
                success_count += 1
            else:
                print(f"[ERROR] Failed to capture {s['name']}: {res.stderr.decode('utf-8', errors='ignore')}")
        except Exception as e:
            print(f"[ERROR] Exception during {s['name']}: {e}")

    print("=" * 60)
    print(f"Captured {success_count}/{len(SHOTS)} screenshots successfully.")
    print("=" * 60)


if __name__ == "__main__":
    capture_all()
