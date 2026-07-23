---
title: "Cayley–Hamilton 定理"
type: theorem
id: ALG-THM-041
subject: algebra
chapter: 05-linear-maps
tags:
  - Cayley-Hamilton
  - 特征多项式
depends:
  - ALG-DEF-036
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.5"
difficulty: 4
related: []
corollaries: []
applications:
  - '控制理论：通过 Cayley–Hamilton 计算矩阵幂 $A^k$（化归为 $I,A,\ldots,A^{n-1}$ 的组合）'
---

## 条件

设 $A$ 是 $n$ 阶方阵，$\chi_A(\lambda) = \lambda^n + c_{n-1}\lambda^{n-1} + \cdots + c_0$ 是其特征多项式。

## 结论

> $$
> \chi_A(A) = A^n + c_{n-1}A^{n-1} + \cdots + c_0 I = 0.
> $$

## 直觉理解

矩阵满足自己的特征多项式——这是一个"自我指涉"的深刻结论。它将 $A^n$ 表示为更低次幂的线性组合，可用于简化 $A^k$ 的计算。

## 链接

- 前置：[[ALG-DEF-036]] 特征多项式
- 用于：[[ALG-THM-042]] 最小多项式
