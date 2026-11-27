#!/usr/bin/env python3
"""
build_index.py
根据全库条目的 frontmatter 重新生成 `_meta/index.md`（站点首页的全库条目索引）。

只收录 `status: stable` 的条目；按 subject → chapter → type 分组。
用法：
  python scripts/build_index.py
  python scripts/build_index.py --output _meta/index.md
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

CONTENT_DIRS = ["analysis", "algebra", "_cross"]

SUBJECT_TITLES = {
    "analysis": "数学分析",
    "algebra": "高等代数",
    "cross": "跨课关联",
}

TYPE_TITLES = {
    "definition": "定义",
    "theorem": "定理",
    "example": "例题",
    "problem": "习题",
}
TYPE_ORDER = ["definition", "theorem", "example", "problem"]

# 章节在首页显示的附加说明（只影响显示，不改变目录名）
CHAPTER_NOTES = {
    "06-interesting-problems": "有意思的数学问题",
}

HEADER = """---
title: "全库条目索引"
description: "MK_Base 数学专业知识库的全库条目索引：按学科、章节与条目类型分组。"
---

> 自动生成。手工编辑会被 `scripts/build_index.py` 覆盖。
>
> 本文件按 `subject → chapter → 类型` 分组列出全库 stable 条目。
> draft / review 状态的条目不出现于此索引，但通过 PR CI 仍受悬空引用扫描约束。

---
"""


def extract_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def collect_entries() -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for content_dir in CONTENT_DIRS:
        root = Path(content_dir)
        if not root.exists():
            continue
        for md in sorted(root.rglob("*.md")):
            fm = extract_frontmatter(md)
            if not fm.get("id") or fm.get("status") != "stable":
                continue
            entries.append(fm)
    return entries


def id_sort_key(entry_id: str) -> tuple[str, int]:
    match = re.match(r"^[A-Z]+-[A-Z]+-(\d+)$", str(entry_id))
    return (str(entry_id), int(match.group(1)) if match else 0)


def render(entries: list[dict[str, Any]]) -> str:
    grouped: dict[str, dict[str, dict[str, list[dict[str, Any]]]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(list))
    )
    for entry in entries:
        grouped[str(entry.get("subject"))][str(entry.get("chapter"))][
            str(entry.get("type"))
        ].append(entry)

    lines: list[str] = [HEADER]
    subject_order = ["analysis", "algebra", "cross"]
    for subject in subject_order:
        subject_title = SUBJECT_TITLES[subject]
        lines.append(f"## {subject_title}\n")
        if subject == "cross":
            lines.append("### 跨课条目\n")
            by_type = (
                grouped.get("cross", {}).get("_cross", {})
                if grouped.get("cross")
                else {}
            )
            has_any = False
            for entry_type in TYPE_ORDER:
                items = sorted(
                    by_type.get(entry_type, []), key=lambda e: id_sort_key(str(e["id"]))
                )
                if not items:
                    continue
                has_any = True
                lines.append(f"#### {TYPE_TITLES[entry_type]}（{len(items)} 条）\n")
                for item in items:
                    lines.append(f"- [[{item['id']}]] {item.get('title', '')}")
                lines.append("")
            if not has_any:
                lines.append("_暂无 stable 条目。_\n")
            lines.append("---\n")
            continue

        # analysis / algebra：按磁盘上的章节目录逐一列出，保证目录完整
        chapter_dirs = sorted(
            p.name for p in Path(subject).iterdir() if p.is_dir()
        )
        chapters = grouped.get(subject, {})
        for chapter in chapter_dirs:
            note = CHAPTER_NOTES.get(chapter)
            heading = f"### {chapter}"
            if note:
                heading += f"（{note}）"
            lines.append(heading + "\n")

            by_type = chapters.get(chapter, {})
            has_any = False
            for entry_type in TYPE_ORDER:
                items = sorted(
                    by_type.get(entry_type, []), key=lambda e: id_sort_key(str(e["id"]))
                )
                if not items:
                    continue
                has_any = True
                lines.append(f"#### {TYPE_TITLES[entry_type]}（{len(items)} 条）\n")
                for item in items:
                    lines.append(f"- [[{item['id']}]] {item.get('title', '')}")
                lines.append("")
            if not has_any:
                lines.append("_暂无 stable 条目。_\n")

        lines.append("---\n")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="生成 _meta/index.md 全库索引")
    parser.add_argument("--output", default="_meta/index.md", help="输出路径")
    args = parser.parse_args()

    entries = collect_entries()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(entries), encoding="utf-8", newline="\n")
    print(f"✅ 已写入 {output}（stable 条目 {len(entries)} 个）")


if __name__ == "__main__":
    main()
