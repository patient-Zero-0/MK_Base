---
title: "Vandermonde 行列式"
type: definition
id: ALG-DEF-014
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - Vandermonde
depends:
  - ALG-DEF-010
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.2"
difficulty: 2
related: []
applications:
  - "数值分析：多项式插值的存在唯一性由Vandermonde行列式非零保证"
---

## 定义陈述

设 $x_1, x_2, \ldots, x_n$ 是 $n$ 个数。**Vandermonde 行列式**定义为

$$
V_n(x_1, \ldots, x_n) = \det\begin{pmatrix}
1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\
1 & x_2 & x_2^2 & \cdots & x_2^{n-1} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_n & x_n^2 & \cdots & x_n^{n-1}
\end{pmatrix}.
$$

## 直觉理解

Vandermonde 行列式是"用幂函数构造的矩阵"的行列式，第 $i$ 行是 $(1, x_i, x_i^2, \ldots, x_i^{n-1})$。

其求值公式（[[ALG-THM-013]]）给出：
$$
V_n = \prod_{1 \leq i < j \leq n} (x_j - x_i).
$$

当且仅当 $x_i$ 互不相同时 $V_n \neq 0$——这正是多项式插值问题有唯一解的条件。

## 链接

- 前置：[[ALG-DEF-010]]
- 求值公式：[[ALG-THM-013]] Vandermonde 行列式求值
