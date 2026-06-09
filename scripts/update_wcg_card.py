#!/usr/bin/env python3

from html.parser import HTMLParser
from pathlib import Path
import os
import shutil
import struct
import subprocess
import tempfile
from urllib.request import Request, urlopen


MEMBER_NAME = "Timberkito"
MEMBER_ID = "1183020"
WIDGET_URL = (
    "https://www.worldcommunitygrid.org/getDynamicImage.do"
    f"?memberName={MEMBER_NAME}&mnOn=true&stat=1&imageNum=1"
    f"&rankOn=true&projectsOn=true&special=true&link=1&memberId={MEMBER_ID}"
)
CARD_SIZE = (406, 208)
OUTPUT_PATH = (
    Path(__file__).resolve().parents[1] / "assets" / "world-community-grid.png"
)


class WidgetParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ignored_depth = 0
        self.items = []

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.ignored_depth += 1

    def handle_endtag(self, tag):
        if tag in {"script", "style"} and self.ignored_depth:
            self.ignored_depth -= 1

    def handle_data(self, data):
        if self.ignored_depth:
            return
        text = " ".join(data.split())
        if text:
            self.items.append(text)


def fetch_stats_text():
    request = Request(
        WIDGET_URL,
        headers={"User-Agent": "TimberKito-GitHub-Profile/3.0"},
    )
    with urlopen(request, timeout=30) as response:
        content = response.read().decode("iso-8859-1")

    parser = WidgetParser()
    parser.feed(content)
    try:
        member_index = parser.items.index(MEMBER_NAME)
        return parser.items[member_index + 1].removeprefix(":").strip()
    except (ValueError, IndexError) as error:
        raise ValueError("WCG widget did not contain the expected member data") from error


def find_chrome():
    configured_path = os.environ.get("CHROME_PATH")
    candidates = [
        configured_path,
        shutil.which("google-chrome"),
        shutil.which("google-chrome-stable"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return Path(candidate)
    raise FileNotFoundError("Chrome or Chromium was not found")


def png_size(path):
    with path.open("rb") as image:
        header = image.read(24)
    if header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError("Chrome did not produce a valid PNG")
    return struct.unpack(">II", header[16:24])


def capture_widget(chrome):
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="wcg-chrome-") as profile:
        screenshot_path = Path(profile) / OUTPUT_PATH.name
        command = [
            str(chrome),
            "--headless",
            "--no-sandbox",
            "--disable-gpu",
            "--disable-background-networking",
            "--disable-component-update",
            "--disable-sync",
            "--hide-scrollbars",
            "--no-first-run",
            "--force-device-scale-factor=1",
            f"--window-size={CARD_SIZE[0]},{CARD_SIZE[1]}",
            "--virtual-time-budget=5000",
            f"--user-data-dir={profile}",
            f"--screenshot={screenshot_path}",
            WIDGET_URL,
        ]
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=60,
            check=False,
        )
        if result.returncode:
            raise RuntimeError(
                f"Chrome screenshot failed with exit code {result.returncode}"
            )

        actual_size = png_size(screenshot_path)
        if actual_size != CARD_SIZE:
            raise ValueError(
                f"Unexpected screenshot size: {actual_size}; expected {CARD_SIZE}"
            )
        shutil.copyfile(screenshot_path, OUTPUT_PATH)


def main():
    stats_text = fetch_stats_text()
    chrome = find_chrome()
    capture_widget(chrome)
    print(f"Updated {OUTPUT_PATH.name} from WCG official widget: {stats_text}")


if __name__ == "__main__":
    main()
