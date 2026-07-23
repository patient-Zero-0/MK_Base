---
title: "齐次方程组有非零解的充要条件"
type: theorem
id: ALG-THM-024
subject: algebra
chapter: 03-linear-equations
tags:
  - 线性方程组
  - 齐次
  - 解的存在性
depends:
  - ALG-THM-019
  - ALG-DEF-020
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.4"
difficulty: 2
related: []
corollaries: []
applications:
  - "微分方程：齐次线性 ODE 解空间维数由系数矩阵秩决定"
---

## 条件

设 $A$ 是 $m \times n$ 矩阵，考虑齐次方程组 $Ax = 0$。

## 结论

> $Ax = 0$ 有非零解 $\iff \operatorname{rank}(A) < n$（即未知数个数 > 系数矩阵的秩）。

特别地，当 $m < n$（方程数 < 未知数个数）时，齐次方程组必有非零解。

## 直觉理解

$n$ 个未知数只有 $r$ 个有效约束（$\operatorname{rank} = r$），则有 $n - r$ 个自由度——有剩余自由度时必然存在非零解。

## 链接

- 前置：[[ALG-THM-019]] Gauss 消元法、[[ALG-DEF-020]] 矩阵的秩
- 用于：[[ALG-THM-025]] 齐次解空间维数
