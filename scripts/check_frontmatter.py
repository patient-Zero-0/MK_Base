#!/usr/bin/env python3
"""
check_frontmatter.py
检查 Markdown 文件的 YAML frontmatter 必填字段完整性。

用法：
  python3 scripts/check_frontmatter.py path/to/file.md
  python3 scripts/check_frontmatter.py --all
  python3 scripts/check_frontmatter.py --changed-only --base <sha>
"""

import sys
import os
import re
import yaml
import subprocess
import argparse
from pathlib import Path

# ── 必填字段定义 ─────────────────────────────────────────────────────────────

COMMON_REQUIRED = [
    "title", "type", "id", "subject", "chapter",
    "tags", "depends", "status", "source", "difficulty"
]

# CONTRIBUTING.md § 2 显式允许 depends 为空列表（公理类条目无前置概念）。
# tags 单独有 ≥2 校验，故此处也跳过空检查。
EMPTY_LIST_ALLOWED = {"depends"}

TYPE_REQUIRED = {
    "definition": [],
    "theorem":    [],
    "example":    ["illustrates"],
    "problem":    ["tests"],
}

VALID_TYPES    = {"definition", "theorem", "example", "problem"}
VALID_SUBJECTS = {"analysis", "algebra", "cross"}
VALID_STATUSES = {"draft", "review", "stable"}

# ── 工具函数 ─────────────────────────────────────────────────────────────────

def extract_frontmatter(path: Path) -> dict | None:
    """从 Markdown 文件中提取 YAML frontmatter，失败返回 None。"""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as e:
        print(f"  ⚠ YAML 解析失败：{e}")
        return None

def check_file(path: Path) -> list[str]:
    """检查单个文件，返回错误列表。"""
    errors = []

    fm = extract_frontmatter(path)
    if fm is None:
        return [f"缺少 YAML frontmatter 或格式错误"]

    # 公共必填字段
    for field in COMMON_REQUIRED:
        val = fm.get(field)
        if val is None:
            errors.append(f"缺少必填字段：{field}")
        elif val == "":
            errors.append(f"必填字段为空：{field}")
        elif (val == [] or val == {}) and field not in EMPTY_LIST_ALLOWED:
            errors.append(f"必填字段为空：{field}")

    # 标题排版：Quartz 不会在 frontmatter 标题中渲染 KaTeX，
    # 写 $...$ 或 x^n 会原样出现在页面 H1、列表与搜索索引中。
    title = fm.get("title")
    if isinstance(title, str):
        if "$" in title or "\\" in title:
            errors.append("title 不得包含 LaTeX 或 $ 符号；请把公式移到正文并用 LaTeX 排版")
        elif re.search(r"[A-Za-z0-9)\]]\s*\^", title):
            errors.append("title 不得使用 ^ 表示上标；请把公式移到正文并用 LaTeX 排版")

    # 类型检查
    entry_type = fm.get("type")
    if entry_type not in VALID_TYPES:
        errors.append(f"type 值无效：{entry_type!r}，应为 {VALID_TYPES}")
        return errors  # 类型未知，无法继续检查类型专属字段

    # 类型专属必填字段
    for field in TYPE_REQUIRED.get(entry_type, []):
        if field not in fm or fm[field] in (None, "", [], {}):
            errors.append(f"{entry_type} 类型缺少必填字段：{field}")

    # 枚举值校验
    if fm.get("subject") not in VALID_SUBJECTS:
        errors.append(f"subject 值无效：{fm.get('subject')!r}，应为 {VALID_SUBJECTS}")

    if fm.get("status") not in VALID_STATUSES:
        errors.append(f"status 值无效：{fm.get('status')!r}，应为 {VALID_STATUSES}")

    difficulty = fm.get("difficulty")
    if difficulty is not None and not (isinstance(difficulty, int) and 1 <= difficulty <= 5):
        errors.append(f"difficulty 应为 1–5 的整数，当前值：{difficulty!r}")

    # tags 至少 2 个
    tags = fm.get("tags", [])
    if isinstance(tags, list) and len(tags) < 2:
        errors.append(f"tags 至少需要 2 个，当前：{len(tags)} 个")

    return errors

def get_changed_files(base_sha: str) -> list[Path]:
    """获取相对于 base_sha 变更的 .md 文件列表。"""
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=AM", base_sha, "HEAD"],
        capture_output=True, text=True
    )
    files = []
    for line in result.stdout.strip().splitlines():
        p = Path(line)
        if p.suffix == ".md" and any(
            p.parts[0] in ("analysis", "algebra", "_cross", "_templates")
            for _ in [1]
        ):
            if p.exists():
                files.append(p)
    return files

def get_all_content_files() -> list[Path]:
    """获取全库所有内容 .md 文件。"""
    dirs = ["analysis", "algebra", "_cross"]
    files = []
    for d in dirs:
        files.extend(Path(d).rglob("*.md"))
    return files

# ── 主程序 ───────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="检查 frontmatter 必填字段")
    parser.add_argument("files", nargs="*", help="指定文件路径")
    parser.add_argument("--all", action="store_true", help="扫描全库所有内容文件")
    parser.add_argument("--changed-only", action="store_true", help="仅检查 PR 变更文件")
    parser.add_argument("--base", help="基准 commit SHA（与 --changed-only 配合使用）")
    args = parser.parse_args()

    if args.changed_only and args.base:
        files = get_changed_files(args.base)
    elif args.all:
        files = get_all_content_files()
    elif args.files:
        files = [Path(f) for f in args.files]
    else:
        parser.print_help()
        sys.exit(0)

    if not files:
        print("✅ 无需检查的文件")
        sys.exit(0)

    total_errors = 0
    for path in files:
        errors = check_file(path)
        if errors:
            print(f"\n❌ {path}")
            for e in errors:
                print(f"   · {e}")
            total_errors += len(errors)
        else:
            print(f"✅ {path}")

    print(f"\n{'─' * 50}")
    if total_errors:
        print(f"共发现 {total_errors} 个错误，请修复后重新提交。")
        sys.exit(1)
    else:
        print(f"检查通过（共 {len(files)} 个文件）")
        sys.exit(0)

if __name__ == "__main__":
    main()
