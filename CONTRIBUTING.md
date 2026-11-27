# CONTRIBUTING.md · 开发规范

> 所有内容建设者（包括 AI 工具）在新建或修改条目前必须阅读本文件。

---

## 目录

1. [条目模板规范](#1-条目模板规范)
2. [YAML frontmatter 字段说明](#2-yaml-frontmatter-字段说明)
3. [LaTeX 书写规范](#3-latex-书写规范)
4. [Git 工作流规范](#4-git-工作流规范)
5. [Commit Message 规范](#5-commit-message-规范)
6. [CI 质量闸门说明](#6-ci-质量闸门说明)
7. [内容审校标准](#7-内容审校标准)

---

## 1. 条目模板规范

四种条目类型各有独立模板，位于 `_templates/` 目录：

| 类型 | 模板文件 | 适用场景 |
|---|---|---|
| 定义 | `_templates/definition.md` | 数学概念、符号的严格定义 |
| 定理 | `_templates/theorem.md` | 命题、定理、推论、引理 |
| 例题 | `_templates/example.md` | 演示某定义/定理用法的示范题 |
| 习题 | `_templates/problem.md` | 供练习的题目，含折叠解答 |

**新建条目步骤：**

```bash
# 1. 从模板复制
cp _templates/theorem.md analysis/01-limits/ANL-THM-XXX.md

# 2. 填写所有必填字段
# 3. 检查 depends 中的 ID 是否全部已存在
# 4. 在 draft/* 分支提交
# 5. 发起 PR，等待 CI 通过
```

---

## 2. YAML frontmatter 字段说明

每条条目文件开头必须包含完整的 YAML frontmatter：

```yaml
---
title:        # 条目标题，简洁明确
type:         # definition | theorem | example | problem
id:           # 全库唯一标识，格式见下方
subject:      # analysis | algebra | cross
chapter:      # 所属章节目录名，如 01-limits
tags:         # 至少 2 个标签，列表格式
depends:      # 前置概念 ID 列表，允许为空列表 []
uses:         # 依赖的公理 ID（区别于 depends）
status:       # draft | review | stable
source:       # 来源教材，精确到节，如 "陈纪修《数学分析》第3版 §2.4"
difficulty:   # 1–5 整数（定义见下方）
# ── 以下为各类型专用字段 ──────────
related:      # 相关但非依赖的条目 ID（可选）
corollaries:  # 由本定理推出的推论 ID（theorem 专用，可选）
illustrates:  # 本例演示的定义/定理 ID（example 专用）
tests:        # 本题考察的知识点 ID（problem 专用）
applications: # 跨专业应用场景描述或链接（可选）
---
```

> **标题是纯文本**：`title` 会用于页面 H1、条目列表和搜索索引，Quartz 不会在 frontmatter 标题中渲染 KaTeX。请不要在标题里写 `$...$` 或 `^` 上标，保持自然语言；公式请放到正文中用 LaTeX 排版。

### ID 命名规则

```
{科目前缀}-{类型代码}-{三位编号}

科目前缀：ANL（数学分析）| ALG（高等代数）| CROSS（跨课）
类型代码：DEF | THM | EX | PROB | AX（公理）
编号：    三位数字，按章节顺序递增

示例：ANL-THM-006  ALG-DEF-012  ANL-AX-001  CROSS-003
```

#### type 字段与 ID 类型代码的特殊约定

frontmatter 的 `type` 字段当前仅取四个值：`definition | theorem | example | problem`。
对应不严格的两类条目，约定如下：

| ID 类型代码 | frontmatter `type` | 备注 |
|---|---|---|
| `AX`（公理） | `definition` | 公理是"被接受为真的命题"，结构上接近定义，统一以 `definition` 处理；建议在 tags 中加 `公理` 标签便于检索 |
| `CROSS`（跨课关联） | `definition`（默认）或 `example` | 跨课条目按内容主导形态选取——以"概念桥接"为主用 `definition`，以"具体场景演示"为主用 `example` |

未来若启用专用 `axiom` / `cross-link` 类型，将通过 `arch:` 提交同步迁移。

### 难度等级定义

| 等级 | 定义 | 典型示例 |
|---|---|---|
| 1 | 直接读定义，无需推导 | ε-N 定义陈述 |
| 2 | 理解含义，完成简单验证 | 用定义验证具体数列收敛 |
| 3 | 综合 2–3 概念，完成标准证明 | Lagrange 中值定理证明 |
| 4 | 需构造辅助对象或反例 | 证明 sin(x²) 非一致连续 |
| 5 | 跨章节综合，非平凡技巧 | Jordan 标准形存在性证明 |

### 必填字段一览

| 字段 | definition | theorem | example | problem |
|---|---|---|---|---|
| title / type / id / subject / chapter | ✅ | ✅ | ✅ | ✅ |
| tags（≥2）/ depends / status / source | ✅ | ✅ | ✅ | ✅ |
| difficulty | ✅ | ✅ | ✅ | ✅ |
| illustrates | — | — | ✅ | — |
| tests | — | — | — | ✅ |

---

## 3. LaTeX 书写规范

### 基本格式

```markdown
行内公式：$f(x) = x^2$
独立公式：$$\lim_{n \to \infty} a_n = L$$
```

### 强制统一写法

| 符号 | 正确写法 | 禁止写法 |
|---|---|---|
| 实数集 | `\mathbb{R}` | `ℝ`（Unicode） |
| 有理数集 | `\mathbb{Q}` | `ℚ` |
| 自然数集 | `\mathbb{N}` | `ℕ` |
| 全称量词 | `\forall` | `∀` |
| 存在量词 | `\exists` | `∃` |
| 证明结束 | `\blacksquare` | `■` / `QED` |
| 蕴含 | `\implies` | `=>` |
| 等价 | `\iff` | `<=>` |

### 习题折叠格式（problem 类型必须）

```markdown
## 提示

<details><summary>点击展开提示</summary>

提示内容……

</details>

## 解答

<details><summary>点击展开完整解答</summary>

解答内容……

</details>
```

---

## 4. Git 工作流规范

### 分支命名

```
draft/analysis-{主题}     # 数学分析新条目，如 draft/analysis-limits
draft/algebra-{主题}      # 高等代数新条目
fix/{条目ID}-{问题描述}    # 错误修正，如 fix/anl-thm-006-proof
arch/{变更描述}            # 架构变更，如 arch/migrate-to-meilisearch
status/{描述}             # 状态文件更新
```

### 标准操作流程

```bash
# 1. 从最新 main 创建分支
git checkout main && git pull
git checkout -b draft/analysis-limits

# 2. 创建条目（从模板复制）
cp _templates/theorem.md analysis/01-limits/ANL-THM-006.md

# 3. 编写内容，提交
git add analysis/01-limits/ANL-THM-006.md
git commit -m "feat(analysis): 新增 ANL-THM-006 单调有界定理"

# 4. 推送并发起 PR
git push origin draft/analysis-limits
# 在 GitHub 上开 PR → 等待 check.yml → code review → merge
```

### 禁止事项

- ❌ 直接向 `main` 分支 push（分支保护会拦截）
- ❌ 未经 CI 检查强制合并
- ❌ 在 `main` 分支上修改内容文件
- ❌ 删除或修改已 merge 的历史条目 ID

---

## 5. Commit Message 规范

格式：`{类型}({范围}): {描述}`

| 类型前缀 | 含义 | 示例 |
|---|---|---|
| `feat` | 新增条目 | `feat(analysis): 新增 ANL-DEF-024 一致连续定义` |
| `fix` | 修正内容错误 | `fix(ANL-THM-006): 修正 Lagrange 定理证明第 3 步` |
| `refactor` | 重组结构，不改内容 | `refactor(algebra): 将 Ch3 条目按依赖顺序重排` |
| `arch` | 架构变更 | `arch: 将部署平台从 GitHub Pages 迁移至 Cloudflare Pages` |
| `status` | 状态文件更新 | `status: M0 完成，进入 M1` |
| `ci` | CI 脚本变更 | `ci: 新增 LaTeX 语法检查步骤` |
| `docs` | 规范文件变更 | `docs: 更新 CONTRIBUTING.md 难度定义` |
| `chore` | 配置、依赖等 | `chore: 更新 Quartz 至 v4.3.0` |

**范围（可选）：** `analysis` | `algebra` | `cross` | `meta` | 具体条目 ID

---

## 6. CI 质量闸门说明

PR 发起后，`check.yml` 自动运行以下四项检查，**任一失败则阻断合并**：

### ① frontmatter 完整性（`scripts/check_frontmatter.py`）

检查所有新增/修改的 `.md` 文件是否包含全部必填字段，且字段值非空。

```bash
# 本地运行
python3 scripts/check_frontmatter.py analysis/01-limits/ANL-THM-006.md
```

### ② 悬空引用扫描（`scripts/check_dangling_refs.py`）

扫描 `depends`、`uses`、`illustrates`、`tests` 字段中的所有 ID，确认对应文件存在于仓库中。

```bash
# 本地运行（扫描全库）
python3 scripts/check_dangling_refs.py
```

### ③ LaTeX 语法验证（node-katex）

对所有 `$…$` 和 `$$…$$` 中的公式尝试 KaTeX 渲染，报告无法解析的公式。

```bash
# 本地运行
node scripts/check_katex.js analysis/01-limits/ANL-THM-006.md
```

### ④ Markdown 格式规范（markdownlint）

按 `.markdownlint.json` 配置检查 Markdown 格式，包括标题层级、列表缩进、空行等。

```bash
# 本地运行
npx markdownlint analysis/01-limits/ANL-THM-006.md
```

### 本地一键检查

```bash
# 在提交前运行，等同于 CI 检查
make check
# 或逐步运行
python3 scripts/check_frontmatter.py --all
python3 scripts/check_dangling_refs.py
node scripts/check_katex.js --all
npx markdownlint '**/*.md' --ignore node_modules
```

---

## 7. 内容审校标准

条目从 `draft` 升为 `review` 须满足：

- [ ] 所有必填字段填写完整
- [ ] `depends` 引用的所有 ID 已存在于仓库
- [ ] 所有 LaTeX 公式本地渲染无报错
- [ ] 定义/定理条目包含「直觉理解」板块
- [ ] 定理条目包含「常见错误」板块（难度 ≥ 3）
- [ ] `source` 字段精确到节（如 `§2.4`）

条目从 `review` 升为 `stable` 须满足：

- [ ] 经第二人（或 AI + 人工）审校，内容准确无误
- [ ] PR 的 CI 检查全部通过
- [ ] 如有跨专业 `applications` 字段，示例描述准确

---

*如有疑问，优先查阅 `refs/prd-v1.5-summary.md`，或参考 `analysis/01-limits/` 下的示范条目。*
