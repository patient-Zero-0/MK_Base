---
title: "线性相关性判定（个数 > 维数 ⇒ 相关）"
type: theorem
id: ALG-THM-020
subject: algebra
chapter: 03-linear-equations
tags:
  - 向量组
  - 线性相关
  - 维数
depends:
  - ALG-DEF-018
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.3"
difficulty: 2
related: []
corollaries: []
applications:
  - "数值分析：$n$ 个 $m$ 维向量在 $n > m$ 时必然线性相关"
---

## 条件

设 $\alpha_1, \ldots, \alpha_s \in \mathbb{R}^n$（即 $s$ 个 $n$ 维向量）。

## 结论

> 若 $s > n$，则 $\alpha_1, \ldots, \alpha_s$ 必线性相关。
>
> 更一般地，若每个 $\alpha_i$ 可由 $r$ 个向量线性表示，且 $s > r$，则 $\alpha_1, \ldots, \alpha_s$ 线性相关。

## 直觉理解

$n$ 维空间最多只能有 $n$ 个线性无关的方向。如果有超过 $n$ 个向量，必然产生冗余——这就是"方向不够分"原理。

**例子**：在平面（2 维）上任意取 3 个向量，一定有一个是其他两个的组合（或零向量）。

## 证明

将 $\alpha_1, \ldots, \alpha_s$ 排成 $n \times s$ 矩阵 $A$。考虑 $A x = 0$，$s > n$ 时未知数多于方程数，必有非零解，系数即线性相关关系的系数。$\blacksquare$

## 链接

- 前置：[[ALG-DEF-018]] 线性相关与无关
- 用于：[[ALG-THM-021]] 替换定理
