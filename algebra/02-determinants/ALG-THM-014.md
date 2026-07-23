---
title: "Laplace 定理（按 $k$ 行展开）"
type: theorem
id: ALG-THM-014
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - Laplace
  - 展开
depends:
  - ALG-DEF-012
  - ALG-THM-011
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.3"
difficulty: 4
related: []
corollaries: []
applications: []
---

## 条件

设 $A$ 是 $n$ 阶方阵。任选 $k$ 行（$1 \leq i_1 < \cdots < i_k \leq n$）。

## 结论

> $\det A$ 等于按这 $k$ 行展开的和：所有 $k$ 阶子式与其对应的代数余子式之积的和。
> 求和跑遍所有 $\binom{n}{k}$ 种列选择（$1 \leq j_1 < \cdots < j_k \leq n$）。

## 直觉理解

Laplace 定理是将按一行展开（[[ALG-THM-011]]）推广到按任意 $k$ 行同时展开。

当 $k = 1$ 时退化为按一行展开公式；当 $k = n$ 时只有一项，就是行列式本身。

## 链接

- 前置：[[ALG-DEF-012]] $k$ 阶子式
- 特例：[[ALG-THM-011]] 按一行展开
