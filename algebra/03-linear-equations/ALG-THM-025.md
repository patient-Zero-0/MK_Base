---
title: "齐次解空间维数 = n - rank(A)"
type: theorem
id: ALG-THM-025
subject: algebra
chapter: 03-linear-equations
tags:
  - 线性方程组
  - 解空间
  - 维数
depends:
  - ALG-THM-024
  - ALG-DEF-022
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.4"
difficulty: 3
related: []
corollaries: []
applications:
  - "优化理论：线性约束的可行域维数 = n - rank(A)"
---

## 条件

设 $A$ 是 $m \times n$ 矩阵，$\operatorname{rank}(A) = r$。

## 结论

> 齐次方程组 $Ax = 0$ 的解空间 $\operatorname{Ker}(A)$ 的维数为 $n - r$。
>
> 即 $\dim \operatorname{Ker}(A) = n - \operatorname{rank}(A)$。

## 直觉理解

每个线性无关的约束方程消除一个自由度。$r$ 个独立约束 ⇒ 剩下 $n - r$ 个自由变量 ⇒ 基础解系包含 $n - r$ 个向量。

## 证明

将 $A$ 化为 RREF，有 $r$ 个主元列，$n - r$ 个自由列。自由列对应的变量可作为自由参数。令每个自由参数取 1 其余取 0，得到 $n - r$ 个线性无关的解向量，构成基础解系。$\blacksquare$

## 链接

- 前置：[[ALG-THM-024]] 齐次非零解条件、[[ALG-DEF-022]] 基础解系
- 用于：[[ALG-THM-026]] 非齐次解结构
