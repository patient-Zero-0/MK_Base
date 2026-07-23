---
title: "基扩充定理"
type: theorem
id: ALG-THM-029
subject: algebra
chapter: 04-linear-spaces
tags:
  - 基
  - 扩充
  - 子空间
depends:
  - ALG-THM-028
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.3"
difficulty: 3
related: []
corollaries: []
applications: []
---

## 条件

设 $V$ 是 $n$ 维线性空间，$S = \{v_1, \ldots, v_r\}$ 是 $V$ 中线性无关的向量组（$r < n$）。

## 结论

> 存在向量 $v_{r+1}, \ldots, v_n \in V$ 使得 $\{v_1, \ldots, v_r, v_{r+1}, \ldots, v_n\}$ 成为 $V$ 的一组基。

## 直觉理解

任何无关组都可以"扩展"成一组基——缺几个就补几个方向，直到铺满整个空间。这保证我们可以从任意一个"干净的起点"构建基。

## 链接

- 前置：[[ALG-THM-028]] 基的存在性
- 用于：[[ALG-THM-030]] 维数公式、[[ALG-THM-035]] 补空间
