#!/usr/bin/env python3

from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.request import Request, urlopen
from xml.etree import ElementTree


MEMBER_NAME = "Timberkito"
MEMBER_ID = "1183020"
MEMBER_URL = (
    "https://www.worldcommunitygrid.org/stat/"
    f"viewMemberInfo.do?userName={MEMBER_NAME}"
)
BOINC_URL = (
    "https://www.worldcommunitygrid.org/boinc/"
    f"show_user.php?userid={MEMBER_ID}&format=xml"
)
START_MARKER = "<!-- WCG-STATS:START -->"
END_MARKER = "<!-- WCG-STATS:END -->"


class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.items = []

    def handle_data(self, data):
        text = " ".join(data.split())
        if text:
            self.items.append(text)


def fetch(url):
    request = Request(url, headers={"User-Agent": "TimberKito-GitHub-Profile/1.0"})
    with urlopen(request, timeout=30) as response:
        return response.read()


def value_after(items, label, offset=1):
    return items[items.index(label) + offset]


def existing_stats(content):
    labels = {
        "runtime": r"WCG 总运行时长 `\(y:d:h:m:s\)`",
        "points": "WCG 生成积分",
        "results": "WCG 已返回结果",
        "last_result": "最近返回结果",
        "devices": "设备安装数",
        "total_credit": "BOINC Total Credit",
        "recent_credit": "BOINC Recent Average Credit",
        "registered": "注册日期",
    }
    stats = {}
    for key, label in labels.items():
        match = re.search(rf"\| {label} \| `([^`]*)` \|", content)
        if match:
            stats[key] = match.group(1)
    return stats


def badge(label, value):
    encoded_label = label.replace("-", "--").replace(" ", "%20")
    encoded_value = value.replace("-", "--").replace(" ", "%20")
    return (
        f"![{label}](https://img.shields.io/badge/"
        f"{encoded_label}-{encoded_value}-00a1e0?style=flat-square)"
    )


def get_stats(fallback):
    stats = fallback.copy()

    parser = TextParser()
    parser.feed(fetch(MEMBER_URL).decode("utf-8", errors="replace"))
    if "Total run time (y:d:h:m:s) (Rank)" in parser.items:
        stats.update(
            {
                "runtime": value_after(
                    parser.items, "Total run time (y:d:h:m:s) (Rank)"
                ),
                "points": value_after(parser.items, "Points generated (rank)"),
                "results": value_after(parser.items, "Results returned (rank)"),
                "last_result": value_after(parser.items, "Last result returned (", 3),
                "devices": value_after(parser.items, "Device installations"),
                "registered": value_after(parser.items, "Registered member since"),
            }
        )

    root = ElementTree.fromstring(fetch(BOINC_URL))
    stats["total_credit"] = f"{float(root.findtext('total_credit')):.2f}"
    stats["recent_credit"] = f"{float(root.findtext('expavg_credit')):.2f}"
    return stats


def render(stats):
    return "\n".join(
        [
            START_MARKER,
            (
                f"[![WCG User](https://img.shields.io/badge/WCG-{MEMBER_NAME}"
                f"-00a1e0?style=flat-square)]({MEMBER_URL})"
            ),
            badge("BOINC Total Credit", stats["total_credit"]),
            badge("BOINC RAC", stats["recent_credit"]),
            "",
            "| 数据 | 当前值 |",
            "| --- | ---: |",
            f'| WCG 总运行时长 `(y:d:h:m:s)` | `{stats["runtime"]}` |',
            f'| WCG 生成积分 | `{stats["points"]}` |',
            f'| WCG 已返回结果 | `{stats["results"]}` |',
            f'| 最近返回结果 | `{stats["last_result"]}` |',
            f'| 设备安装数 | `{stats["devices"]}` |',
            f'| BOINC Total Credit | `{stats["total_credit"]}` |',
            f'| BOINC Recent Average Credit | `{stats["recent_credit"]}` |',
            f'| 注册日期 | `{stats["registered"]}` |',
            "",
            f"账号 ID：`{MEMBER_ID}`",
            END_MARKER,
        ]
    )


def main():
    readme = Path(__file__).resolve().parents[1] / "README.md"
    content = readme.read_text(encoding="utf-8")
    before, remainder = content.split(START_MARKER, 1)
    _, after = remainder.split(END_MARKER, 1)
    readme.write_text(
        before + render(get_stats(existing_stats(content))) + after,
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
