#!/usr/bin/env python3

from html import escape
from html.parser import HTMLParser
from pathlib import Path
import re
import textwrap
from urllib.request import Request, urlopen


MEMBER_NAME = "Timberkito"
MEMBER_ID = "1183020"
WIDGET_URL = (
    "https://www.worldcommunitygrid.org/getDynamicImage.do"
    f"?memberName={MEMBER_NAME}&mnOn=true&stat=1&imageNum=1"
    f"&rankOn=true&projectsOn=true&special=true&link=1&memberId={MEMBER_ID}"
)
OUTPUT_PATH = (
    Path(__file__).resolve().parents[1] / "assets" / "world-community-grid.svg"
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


def fetch_widget():
    request = Request(
        WIDGET_URL,
        headers={"User-Agent": "TimberKito-GitHub-Profile/2.0"},
    )
    with urlopen(request, timeout=30) as response:
        return response.read().decode("iso-8859-1")


def parse_widget(content):
    parser = WidgetParser()
    parser.feed(content)

    try:
        member_index = parser.items.index(MEMBER_NAME)
        stats_text = parser.items[member_index + 1]
        projects_index = parser.items.index("Help projects like:")
        projects = parser.items[projects_index + 1]
    except (ValueError, IndexError) as error:
        raise ValueError("WCG widget did not contain the expected member data") from error

    match = re.fullmatch(
        r":\s*([\d,]+)\s+Points\s+\(Rank:\s*#([\d,]+)\)",
        stats_text,
    )
    if not match:
        raise ValueError(f"Unexpected WCG statistics format: {stats_text!r}")

    return {
        "member": MEMBER_NAME,
        "points": match.group(1),
        "rank": match.group(2),
        "projects": projects,
    }


def render_card(stats):
    project_lines = textwrap.wrap(
        stats["projects"],
        width=76,
        break_long_words=False,
        break_on_hyphens=False,
    )[:2]
    projects_svg = "\n".join(
        f'<tspan x="42" dy="{0 if index == 0 else 20}">{escape(line)}</tspan>'
        for index, line in enumerate(project_lines)
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="720" height="260" viewBox="0 0 720 260" role="img" aria-labelledby="title description">
  <title id="title">{escape(stats["member"])} World Community Grid statistics</title>
  <desc id="description">{escape(stats["points"])} points, rank {escape(stats["rank"])}</desc>
  <rect x="1" y="1" width="718" height="258" rx="14" fill="#ffffff" stroke="#d0d7de" stroke-width="2"/>
  <circle cx="62" cy="62" r="29" fill="none" stroke="#161616" stroke-width="4"/>
  <circle cx="51" cy="69" r="21" fill="none" stroke="#161616" stroke-width="4"/>
  <circle cx="44" cy="77" r="13" fill="none" stroke="#161616" stroke-width="4"/>
  <text x="108" y="71" fill="#161616" font-family="Arial, sans-serif" font-size="30" font-weight="600">World Community Grid</text>
  <line x1="42" y1="104" x2="678" y2="104" stroke="#d0d7de"/>
  <text x="42" y="144" fill="#0969da" font-family="Arial, sans-serif" font-size="20" font-weight="600">{escape(stats["member"])}</text>
  <text x="42" y="181" fill="#161616" font-family="Arial, sans-serif" font-size="30" font-weight="700">{escape(stats["points"])} Points</text>
  <text x="300" y="181" fill="#57606a" font-family="Arial, sans-serif" font-size="18">Global rank #{escape(stats["rank"])}</text>
  <text x="42" y="216" fill="#57606a" font-family="Arial, sans-serif" font-size="15">{projects_svg}</text>
</svg>
"""


def main():
    stats = parse_widget(fetch_widget())
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(render_card(stats), encoding="utf-8", newline="\n")
    print(
        f'Updated {OUTPUT_PATH.name}: {stats["points"]} points, '
        f'rank #{stats["rank"]}'
    )


if __name__ == "__main__":
    main()
