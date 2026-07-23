---
title: "替换定理（Steinitz exchange）"
type: theorem
id: ALG-THM-021
subject: algebra
chapter: 03-linear-equations
tags:
  - 向量组
  - 替换定理
  - 秩
depends:
  - ALG-DEF-019
  - ALG-THM-020
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.3"
difficulty: 4
related: []
corollaries: []
applications: []
---

## 条件

设向量组 (I) $\alpha_1, \ldots, \alpha_r$ 线性无关，且可由向量组 (II) $\beta_1, \ldots, \beta_s$ 线性表示。

## 结论

> $r \leq s$，且可以用 (I) 替换掉 (II) 中的 $r$ 个向量，使替换后的向量组仍与 (II) 等价（即张成同一子空间）。

## 直觉理解

替换定理是线性代数中最核心的组合工具：如果一个无关组能被另一组表示，那么无关组的向量个数不超过另一组的个数（"不能用更少的维度表示更多无关方向"）。

**类比**：$r$ 个不冗余的核心成员能做的事，如果 $s$ 个人都能做，那至少需要 $s \geq r$ 个人。

## 链接

- 前置：[[ALG-DEF-019]] 极大无关组、[[ALG-THM-020]] 相关性判定
- 用于：[[ALG-THM-022]] 行秩 = 列秩
