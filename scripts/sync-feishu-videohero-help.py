#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = ROOT / "src" / "content" / "docs"
ASSET_ROOT = ROOT / "public" / "help-assets" / "videohero"

ENV = {
    **os.environ,
    "LARKSUITE_CLI_NO_UPDATE_NOTIFIER": "1",
    "LARKSUITE_CLI_NO_SKILLS_NOTIFIER": "1",
}


PAGES = [
    {
        "lang": "zh",
        "token": "ALPdwy7gni0G3RkqGI3cfe5cn3a",
        "slug": "index",
        "path": "zh/help/videohero/index.md",
        "title": "VideoHero 介绍",
        "description": "VideoHero 技术支持与帮助中心。",
    },
    {
        "lang": "zh",
        "token": "DFwgw1hfIiIFdCk7vgpc7UNUnlb",
        "slug": "settings",
        "path": "zh/help/videohero/settings.md",
        "title": "设置页面",
        "description": "VideoHero 的 App 级别设置说明。",
    },
    {
        "lang": "zh",
        "token": "QK8dwLh3PiiIPNkjZsPcJdJunlh",
        "slug": "talking-head-video-repair",
        "path": "zh/help/videohero/talking-head-video-repair.md",
        "title": "口播视频修复",
        "description": "VideoHero 口播视频修复功能说明。",
    },
    {
        "lang": "zh",
        "token": "LubFwpDd3i2B0jkjcZfciG0Inah",
        "slug": "import-models",
        "path": "zh/help/videohero/import-models.md",
        "title": "如何导入模型",
        "description": "手动导入 VideoHero 模型文件。",
    },
    {
        "lang": "zh",
        "token": "XJI2wD3wUiMYGEkmkqTci5yvnbg",
        "slug": "voice-cloning",
        "path": "zh/help/videohero/voice-cloning.md",
        "title": "模拟原声",
        "description": "VideoHero 模拟原声功能说明。",
    },
    {
        "lang": "en",
        "token": "I9OZwfOUvi7xBDkkjW8c4JyknMd",
        "slug": "index",
        "path": "help/videohero/index.md",
        "title": "VideoHero Introduction",
        "description": "VideoHero technical support and help center.",
    },
    {
        "lang": "en",
        "token": "SURSwIu2LiLrhokJ3lwc6DIRntH",
        "slug": "settings",
        "path": "help/videohero/settings.md",
        "title": "Settings",
        "description": "App-level settings in VideoHero.",
    },
    {
        "lang": "en",
        "token": "Jbglwu81PiWlI6k9cHScNKi1nm5",
        "slug": "talking-head-video-repair",
        "path": "help/videohero/talking-head-video-repair.md",
        "title": "Talking-head Video Repair",
        "description": "Talking-head video repair notes for VideoHero.",
    },
    {
        "lang": "en",
        "token": "AZBEw9QCqiPSIQkg8MbccNyjnHb",
        "slug": "import-models",
        "path": "help/videohero/import-models.md",
        "title": "How to Import Models",
        "description": "Manually import VideoHero model files.",
    },
    {
        "lang": "en",
        "token": "UHAmwWt6FizE7NkvxC9cd4shnFd",
        "slug": "voice-cloning",
        "path": "help/videohero/voice-cloning.md",
        "title": "Voice Cloning",
        "description": "Voice cloning notes for VideoHero.",
    },
]


DOC_LINKS: Dict[str, Dict[str, str]] = {
    "DFwgw1hfIiIFdCk7vgpc7UNUnlb": {"zh": "/zh/help/videohero/settings/", "en": "/help/videohero/settings/"},
    "QK8dwLh3PiiIPNkjZsPcJdJunlh": {"zh": "/zh/help/videohero/talking-head-video-repair/", "en": "/help/videohero/talking-head-video-repair/"},
    "LubFwpDd3i2B0jkjcZfciG0Inah": {"zh": "/zh/help/videohero/import-models/", "en": "/help/videohero/import-models/"},
    "XJI2wD3wUiMYGEkmkqTci5yvnbg": {"zh": "/zh/help/videohero/voice-cloning/", "en": "/help/videohero/voice-cloning/"},
    "SURSwIu2LiLrhokJ3lwc6DIRntH": {"zh": "/zh/help/videohero/settings/", "en": "/help/videohero/settings/"},
    "Jbglwu81PiWlI6k9cHScNKi1nm5": {"zh": "/zh/help/videohero/talking-head-video-repair/", "en": "/help/videohero/talking-head-video-repair/"},
    "AZBEw9QCqiPSIQkg8MbccNyjnHb": {"zh": "/zh/help/videohero/import-models/", "en": "/help/videohero/import-models/"},
    "UHAmwWt6FizE7NkvxC9cd4shnFd": {"zh": "/zh/help/videohero/voice-cloning/", "en": "/help/videohero/voice-cloning/"},
}


def run_fetch(token: str) -> str:
    cmd = [
        "lark-cli",
        "docs",
        "+fetch",
        "--doc",
        token,
        "--doc-format",
        "markdown",
        "--as",
        "user",
        "--format",
        "json",
    ]
    proc = subprocess.run(cmd, env=ENV, text=True, capture_output=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr)
        raise SystemExit(proc.returncode)
    data = json.loads(proc.stdout)
    return data["data"]["document"]["content"]


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def normalize_markdown(raw: str, page: Dict[str, str]) -> str:
    text = raw.strip()
    text = re.sub(r"^<title>.*?</title>\s*", "", text, flags=re.S)
    text = re.sub(rf"^#\s+{re.escape(page['title'])}\s*", "", text).strip()
    text = re.sub(r"\n{3,}", "\n\n", text)

    if page["lang"] == "zh" and page["slug"] == "index":
        text = re.sub(
            r"English version: \[VideoHero tech support & Help Center\]\([^)]+\)",
            "English version: [VideoHero tech support & Help Center](/help/videohero/)",
            text,
        )
        text = text.replace("Mac 和Windows用户", "Mac 和 Windows 用户")
    if page["lang"] == "en" and page["slug"] == "index":
        text = "Chinese version: [VideoHero 技术支持与帮助中心](/zh/help/videohero/)\n\n" + text

    text = convert_callouts(text)
    text = convert_cites(text, page["lang"])
    text = convert_feishu_wiki_links(text, page["lang"])
    text = download_images(text, page)
    text = text.replace("\\*", "*")

    frontmatter = "\n".join(
        [
            "---",
            f"title: {yaml_quote(page['title'])}",
            f"description: {yaml_quote(page['description'])}",
            "---",
            "",
        ]
    )
    return frontmatter + text.strip() + "\n"


def convert_callouts(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        body = match.group(1).strip()
        body = re.sub(r"^>\s*", "", body, flags=re.M)
        quoted = "\n".join(f"> {line}" if line else ">" for line in body.splitlines())
        return f"\n{quoted}\n"

    return re.sub(r"<callout[^>]*>(.*?)</callout>", repl, text, flags=re.S)


def convert_cites(text: str, lang: str) -> str:
    def repl(match: re.Match[str]) -> str:
        attrs = match.group(1)
        doc_id = attr(attrs, "doc-id")
        title = attr(attrs, "title") or "Related page"
        href = DOC_LINKS.get(doc_id, {}).get(lang)
        if not href:
            return title
        return f"[{title}]({href})"

    return re.sub(r"<cite\s+([^>]*)></cite>", repl, text)


def convert_feishu_wiki_links(text: str, lang: str) -> str:
    def repl(match: re.Match[str]) -> str:
        label = match.group(1)
        token = match.group(2)
        href = DOC_LINKS.get(token, {}).get(lang)
        return f"[{label}]({href})" if href else match.group(0)

    return re.sub(r"\[([^\]]+)\]\(https://my\.feishu\.cn/wiki/([A-Za-z0-9]+)[^)]+\)", repl, text)


def attr(attrs: str, name: str) -> str | None:
    m = re.search(rf'{name}="([^"]*)"', attrs)
    return m.group(1) if m else None


def download_images(text: str, page: Dict[str, str]) -> str:
    matches = list(re.finditer(r"!\[\]\((https://internal-api-drive-stream\.feishu\.cn/[^)]+)\)", text))
    if not matches:
        return text

    page_asset_dir = ASSET_ROOT / page["lang"] / page["slug"]
    page_asset_dir.mkdir(parents=True, exist_ok=True)

    replacements: List[tuple[str, str]] = []
    for index, match in enumerate(matches, start=1):
        url = match.group(1)
        filename = f"{page['slug']}-{index:02d}.png"
        dest = page_asset_dir / filename
        if not dest.exists():
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(request, timeout=60) as response:
                dest.write_bytes(response.read())
        public_path = f"/help-assets/videohero/{page['lang']}/{page['slug']}/{filename}"
        replacements.append((match.group(0), f"![{page['title']} screenshot]({public_path})"))

    for old, new in replacements:
        text = text.replace(old, new, 1)
    return text


def main() -> None:
    written = []
    for page in PAGES:
        raw = run_fetch(page["token"])
        out = DOCS_ROOT / page["path"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(normalize_markdown(raw, page), encoding="utf-8")
        written.append(str(out.relative_to(ROOT)))
    print(json.dumps({"written": written}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
