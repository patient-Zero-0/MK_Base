---
title: "相似矩阵的不变量"
type: theorem
id: ALG-THM-038
subject: algebra
chapter: 05-linear-maps
tags:
  - 相似
  - 不变量
  - 特征多项式
depends:
  - ALG-DEF-037
  - ALG-DEF-036
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.3"
difficulty: 2
related: []
corollaries: []
applications:
  - "数值线性代数：QR 算法通过相似变换（不改变特征值）求特征值"
---

## 条件

设 $A \sim B$（$B = P^{-1}AP$）。

## 结论

> 相似矩阵有相同的：
>
> 1. **特征多项式**：$\chi_A(\lambda) = \chi_B(\lambda)$
> 2. **行列式**：$\det A = \det B$
> 3. **迹**：$\operatorname{tr}(A) = \operatorname{tr}(B)$
> 4. **秩**：$\operatorname{rank}(A) = \operatorname{rank}(B)$
>
> 反之不成立——这些不变量相同不能推出相似。

## 直觉理解

相似矩阵是同一线性变换的不同"视角"，所以行列式（体积缩放因子）、迹（特征值之和）、特征多项式等"固有属性"不变。

## 链接

- 前置：[[ALG-DEF-037]] 相似矩阵
- 用于：[[ALG-THM-040]] 可对角化
