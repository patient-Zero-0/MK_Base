---
title: "维数公式应用"
type: problem
id: ALG-PROB-014
subject: algebra
chapter: 04-linear-spaces
tags:
  - 维数
  - 子空间
  - 直和
depends:
  - ALG-THM-030
  - ALG-DEF-029
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.5"
difficulty: 4
related: []
tests:
  - ALG-THM-030
prerequisites:
  - "维数公式"
  - "子空间的和"
---

## 题目

设 $U, W$ 是 $n$ 维线性空间 $V$ 的子空间，$\dim U = r$，$\dim W = s$，且 $r + s > n$。

1. 证明 $\dim(U \cap W) \geq r + s - n$。
2. 若 $r + s = n + 1$，证明 $U \cap W \neq \{0\}$。
3. 举例说明 $r + s = n$ 时 $U \cap W = \{0\}$ 可能成立。
