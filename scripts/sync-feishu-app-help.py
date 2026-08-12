#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional


ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = ROOT / "src" / "content" / "docs"
ASSET_ROOT = ROOT / "public" / "help-assets"

ENV = {
    **os.environ,
    "LARKSUITE_CLI_NO_UPDATE_NOTIFIER": "1",
    "LARKSUITE_CLI_NO_SKILLS_NOTIFIER": "1",
}


@dataclass
class SpaceConfig:
    app: str
    lang: str
    space_id: str
    description: str


SPACES = [
    SpaceConfig("rightclickmate", "zh", "7627471106487684306", "RightClickMate 中文帮助中心"),
    SpaceConfig("rightclickmate", "en", "7628986117458496700", "RightClickMate English Help Center"),
    SpaceConfig("ttsmate", "zh", "7640309492462128321", "TTSMate 中文帮助中心"),
    SpaceConfig("ttsmate", "en", "7641047470172032197", "TTSMate English Help Center"),
    SpaceConfig("songjing", "zh", "7627881223175589052", "诵经助手中文帮助中心"),
]


TITLE_SLUGS = {
    "首页（中文）": "index",
    "首页": "index",
    "Home": "index",
    "通用设置": "general-settings",
    "General Settings": "general-settings",
    "常见问题列表": "faq-list",
    "快速新建文件": "quick-new-file",
    "Quick New File": "quick-new-file",
    "一键复制路径": "copy-path",
    "Copy Path": "copy-path",
    "在当前位置打开终端": "open-terminal",
    "Open Terminal": "open-terminal",
    "批量修改文件名": "batch-rename-files",
    "Batch Rename Files": "batch-rename-files",
    "批量调整图片尺寸": "batch-resize-images",
    "Batch Resize Images": "batch-resize-images",
    "文件复制到指定目录": "copy-to-folder",
    "Copy to Folder": "copy-to-folder",
    "复制目录树": "copy-directory-tree",
    "Copy Directory Tree": "copy-directory-tree",
    "禅桌面（录屏 / 演讲模式）": "zen-desktop",
    "Zen Desktop": "zen-desktop",
    "隐私橡皮擦": "privacy-eraser",
    "Privacy Eraser": "privacy-eraser",
    "RightClickMate(右键助手)功能介绍一页纸": "feature-overview",
    "RightClickMate Feature Overview": "feature-overview",
    "更新历史": "release-notes",
    "Release Notes": "release-notes",
    "常用目录": "favorite-folders",
    "Favorite Folders": "favorite-folders",
    "快捷应用": "quick-apps",
    "Quick Apps": "quick-apps",
    "图片快速标注": "quick-image-annotation",
    "Quick Image Annotation": "quick-image-annotation",
    "格式转换": "format-conversion",
    "Format Conversion": "format-conversion",
    "Q&A": "qa",
    "主要界面": "main-interface",
    "Main Interface": "main-interface",
    "TTS 设置": "tts-settings",
    "TTS Settings": "tts-settings",
    "发音字典": "pronunciation-dictionary",
    "Pronunciation Dictionary": "pronunciation-dictionary",
    "双人对话拆分": "two-person-dialogue-split",
    "Two-Person Dialogue Split": "two-person-dialogue-split",
    "多人对话语音生成": "multi-person-dialogue-generation",
    "Multi-Person Dialogue Generation": "multi-person-dialogue-generation",
    "文档格式要求": "document-format-requirements",
    "常见问题": "faq",
}


DESCRIPTIONS = {
    ("rightclickmate", "zh"): "RightClickMate 技术支持与帮助中心。",
    ("rightclickmate", "en"): "RightClickMate technical support and help center.",
    ("ttsmate", "zh"): "TTSMate 技术支持与帮助中心。",
    ("ttsmate", "en"): "TTSMate technical support and help center.",
    ("songjing", "zh"): "诵经助手技术支持与帮助中心。",
}


def run_json(cmd: List[str]) -> dict:
    proc = subprocess.run(cmd, env=ENV, text=True, capture_output=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr)
        raise SystemExit(proc.returncode)
    return json.loads(proc.stdout)


def list_children(space_id: str, parent_node_token: Optional[str] = None) -> List[dict]:
    cmd = [
        "lark-cli",
        "wiki",
        "+node-list",
        "--space-id",
        space_id,
        "--as",
        "user",
        "--page-all",
        "--format",
        "json",
    ]
    if parent_node_token:
        cmd.extend(["--parent-node-token", parent_node_token])
    data = run_json(cmd)
    return data["data"]["nodes"]


def fetch_markdown(token: str) -> str:
    data = run_json(
        [
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
    )
    return data["data"]["document"]["content"]


def walk_space(config: SpaceConfig) -> List[dict]:
    root_nodes = list_children(config.space_id)
    pages: List[dict] = []

    def visit(node: dict, depth: int, parent_path: List[str]) -> None:
        pages.append(
            {
                "app": config.app,
                "lang": config.lang,
                "space_id": config.space_id,
                "node_token": node["node_token"],
                "obj_token": node["obj_token"],
                "title": node["title"],
                "depth": depth,
                "parent_path": parent_path,
                "has_child": node.get("has_child", False),
            }
        )
        if node.get("has_child"):
            for child in list_children(config.space_id, node["node_token"]):
                visit(child, depth + 1, parent_path + [node["title"]])

    for node in root_nodes:
        visit(node, 0, [])
    return pages


def slug_for(page: dict) -> str:
    title = page["title"].strip()
    if title in TITLE_SLUGS:
        return TITLE_SLUGS[title]
    ascii_slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return ascii_slug or f"page-{page['node_token'][:8]}"


def public_href(page: dict) -> str:
    prefix = "/zh/help" if page["lang"] == "zh" else "/help"
    slug = slug_for(page)
    if slug == "index" or page["depth"] == 0:
        return f"{prefix}/{page['app']}/"
    return f"{prefix}/{page['app']}/{slug}/"


def out_path(page: dict) -> Path:
    prefix = "zh/help" if page["lang"] == "zh" else "help"
    slug = slug_for(page)
    if slug == "index" or page["depth"] == 0:
        return DOCS_ROOT / prefix / page["app"] / "index.md"
    return DOCS_ROOT / prefix / page["app"] / f"{slug}.md"


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def normalize(raw: str, page: dict, token_href: Dict[str, str]) -> str:
    text = raw.strip()
    title = page["title"].strip()
    text = re.sub(r"^<title>.*?</title>\s*", "", text, flags=re.S).strip()
    text = re.sub(rf"^#\s+{re.escape(title)}\s*", "", text).strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = convert_callouts(text)
    text = convert_cites(text, page["lang"], token_href)
    text = convert_feishu_wiki_links(text, token_href)
    text = download_images(text, page)
    text = text.replace("\\*", "*")

    description = DESCRIPTIONS.get((page["app"], page["lang"]), f"{title} help page.")
    frontmatter = "\n".join(
        [
            "---",
            f"title: {yaml_quote(title)}",
            f"description: {yaml_quote(description)}",
            "---",
            "",
        ]
    )
    return frontmatter + text.strip() + "\n"


def convert_callouts(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        body = match.group(1).strip()
        body = re.sub(r"^>\s*", "", body, flags=re.M)
        return "\n" + "\n".join(f"> {line}" if line else ">" for line in body.splitlines()) + "\n"

    return re.sub(r"<callout[^>]*>(.*?)</callout>", repl, text, flags=re.S)


def convert_cites(text: str, lang: str, token_href: Dict[str, str]) -> str:
    def repl(match: re.Match[str]) -> str:
        attrs = match.group(1)
        doc_id = attr(attrs, "doc-id")
        title = attr(attrs, "title") or "Related page"
        href = token_href.get(doc_id or "")
        return f"[{title}]({href})" if href else title

    return re.sub(r"<cite\s+([^>]*)></cite>", repl, text)


def convert_feishu_wiki_links(text: str, token_href: Dict[str, str]) -> str:
    def repl(match: re.Match[str]) -> str:
        label = match.group(1)
        token = match.group(2)
        href = token_href.get(token)
        return f"[{label}]({href})" if href else match.group(0)

    return re.sub(r"\[([^\]]+)\]\(https://my\.feishu\.cn/wiki/([A-Za-z0-9]+)[^)]+\)", repl, text)


def attr(attrs: str, name: str) -> Optional[str]:
    match = re.search(rf'{name}="([^"]*)"', attrs)
    return match.group(1) if match else None


def download_images(text: str, page: dict) -> str:
    matches = list(re.finditer(r"!\[\]\((https://internal-api-drive-stream\.feishu\.cn/[^)]+)\)", text))
    if not matches:
        return text

    slug = slug_for(page)
    page_asset_dir = ASSET_ROOT / page["app"] / page["lang"] / slug
    page_asset_dir.mkdir(parents=True, exist_ok=True)
    replacements = []

    for index, match in enumerate(matches, start=1):
        url = match.group(1)
        filename = f"{slug}-{index:02d}.png"
        dest = page_asset_dir / filename
        if not dest.exists():
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(request, timeout=60) as response:
                dest.write_bytes(response.read())
        public_path = f"/help-assets/{page['app']}/{page['lang']}/{slug}/{filename}"
        replacements.append((match.group(0), f"![{page['title']} screenshot]({public_path})"))

    for old, new in replacements:
        text = text.replace(old, new, 1)
    return text


def main() -> None:
    all_pages: List[dict] = []
    for config in SPACES:
        all_pages.extend(walk_space(config))

    token_href = {}
    for page in all_pages:
        token_href[page["node_token"]] = public_href(page)
        token_href[page["obj_token"]] = public_href(page)

    written = []
    inventory = []
    for page in all_pages:
        if page.get("obj_type", "docx") not in ("docx", "doc"):
            continue
        raw = fetch_markdown(page["node_token"])
        target = out_path(page)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(normalize(raw, page, token_href), encoding="utf-8")
        written.append(str(target.relative_to(ROOT)))
        inventory.append(
            {
                "app": page["app"],
                "lang": page["lang"],
                "title": page["title"],
                "path": str(target.relative_to(ROOT)),
                "href": public_href(page),
                "depth": page["depth"],
            }
        )

    print(json.dumps({"count": len(written), "written": written, "inventory": inventory}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
