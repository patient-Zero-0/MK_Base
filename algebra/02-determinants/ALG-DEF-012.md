---
title: "$k$ 阶子式与 Laplace 定理"
type: definition
id: ALG-DEF-012
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - k阶子式
  - Laplace
depends:
  - ALG-DEF-010
  - ALG-DEF-011
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.3"
difficulty: 3
related: []
applications: []
---

## 定义陈述

设 $A$ 是 $n$ 阶方阵。任选 $k$ 行（$1 \leq i_1 < \cdots < i_k \leq n$）和 $k$ 列（$1 \leq j_1 < \cdots < j_k \leq n$），这些行和列交叉处的 $k^2$ 个元素按原顺序构成的 $k$ 阶行列式称为 $A$ 的一个 **$k$ 阶子式**（$k$-minor），记作 $M\begin{pmatrix}i_1,\ldots,i_k\\j_1,\ldots,j_k\end{pmatrix}$。

删去这 $k$ 行和 $k$ 列后得到的 $(n-k)$ 阶子式乘以 $(-1)^{\sum i_p + \sum j_p}$ 称为对应的**代数余子式**。

## 直觉理解

$k$ 阶子式是行列式的"子块"行列式——任选 $k$ 行 $k$ 列，取出交叉位置的元素构成小方阵求行列式。$k=1$ 时就是元素本身，$k=n$ 时就是原行列式。

**Laplace 定理**（[[ALG-THM-014]]）是将按一行展开推广到按任意 $k$ 行展开的通用工具。

## 链接

- 前置：[[ALG-DEF-010]] $n$ 阶行列式、[[ALG-DEF-011]] 余子式
- 用于：[[ALG-THM-014]] Laplace 定理（按 $k$ 行展开）
