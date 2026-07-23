---
title: "Vandermonde 行列式求值"
type: theorem
id: ALG-THM-013
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - Vandermonde
  - 求值公式
depends:
  - ALG-DEF-014
  - ALG-THM-012
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.2"
difficulty: 3
related: []
corollaries: []
applications:
  - "数值分析：多项式插值存在唯一性的理论保证"
---

## 条件

设 $x_1, x_2, \ldots, x_n$ 是 $n$ 个数。

## 结论

$$
V_n(x_1, \ldots, x_n) = \det\begin{pmatrix}
1 & x_1 & \cdots & x_1^{n-1} \\
\vdots & \vdots & \ddots & \vdots \\
1 & x_n & \cdots & x_n^{n-1}
\end{pmatrix} = \prod_{1 \leq i < j \leq n} (x_j - x_i).
$$

## 证明

对 $n$ 用归纳。$n=2$ 时 $V_2 = x_2 - x_1$ 成立。

假设对 $n-1$ 成立。对 $V_n$ 从最后一行起，每行减去上一行的 $x_1$ 倍，然后按第一行展开，提取公因式后得到 $V_n = (x_2-x_1)\cdots(x_n-x_1) \cdot V_{n-1}(x_2,\ldots,x_n)$。由归纳假设即得。$\blacksquare$

## 常见错误

- ✗ 混淆 $x_j - x_i$ 的顺序。注意 $i < j$，差为后减前。

## 链接

- 前置：[[ALG-DEF-014]]、[[ALG-THM-012]]
