---
title: "可对角化充要条件"
type: theorem
id: ALG-THM-040
subject: algebra
chapter: 05-linear-maps
tags:
  - 可对角化
  - 充要条件
  - 几何重数
  - 代数重数
depends:
  - ALG-THM-039
  - ALG-DEF-038
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.4"
difficulty: 4
related: []
corollaries: []
applications:
  - "若 $A$ 有 $n$ 个不同特征值则必可对角化。实对称矩阵正交对角化由谱定理保证"
---

## 条件

设 $A$ 是 $n$ 阶方阵，$\lambda_i$ 是特征值。

## 结论

> $A$ 可对角化 $\iff$ 每个特征值的**几何重数**等于**代数重数**。
>
> - **代数重数**（algebraic multiplicity）：$\lambda_i$ 作为特征多项式根的重数。
> - **几何重数**（geometric multiplicity）：$\dim \ker(A - \lambda_i I)$。
>
> 特别地，若 $A$ 有 $n$ 个互异的特征值，则 $A$ 必可对角化。

## 直觉理解

几何重数 ≤ 代数重数总是成立。可对角化要求每个特征值有"足够多"的线性无关特征向量（几何重数 = 代数重数），这样才能凑满 $n$ 个特征向量构成基。

## 链接

- 前置：[[ALG-THM-039]] 特征向量无关性、[[ALG-DEF-038]] 可对角化
