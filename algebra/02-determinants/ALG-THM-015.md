---
title: "行列式乘法定理"
type: theorem
id: ALG-THM-015
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - 乘法
depends:
  - ALG-DEF-010
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.4"
difficulty: 2
related: []
corollaries: []
applications:
  - "矩阵乘积的行列式 = 行列式的乘积，这是线性代数中最基本的性质之一"
---

## 条件

设 $A, B$ 是 $n$ 阶方阵。

## 结论

> $$\\det(AB) = (\\det A)(\\det B).$$

## 直觉理解

行列式是衡量线性变换"体积缩放因子"的。复合变换 $AB$ 先做 $B$ 再做 $A$，总体积缩放因子自然是两个缩放因子的乘积。

## 证明思路

对 $A$ 做初等行变换化为对角形 $PAQ = D$，则 $\\det A = \\det P^{-1} \\det D \\det Q^{-1}$。利用初等矩阵与行列式的关系计算 $\\det(AB) = (\\det A)(\\det B)$。$\\blacksquare$

## 常见错误

- ✗ 以为 $\\det(A+B) = \\det A + \\det B$——行列式对加法**不**线性。
