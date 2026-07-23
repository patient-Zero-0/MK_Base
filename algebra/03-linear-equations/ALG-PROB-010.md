---
title: "解的结构证明"
type: problem
id: ALG-PROB-010
subject: algebra
chapter: 03-linear-equations
tags:
  - 线性方程组
  - 解的结构
  - 证明
depends:
  - ALG-THM-026
  - ALG-THM-025
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.4"
difficulty: 4
related: []
tests:
  - ALG-THM-026
prerequisites:
  - "非齐次解的结构"
  - "解空间维数公式"
---

## 题目

1. 设 $x_1, x_2$ 是 $Ax = b$ 的两个解。证明 $\frac{x_1 + x_2}{2}$ 也是解当且仅当 $b=0$（即齐次）。
2. 设 $Ax = b$ 有无穷多解且 $b \neq 0$，证明这些解的任意线性组合仍是解当且仅当系数之和为 1。

## 提示

1. 直接代入，利用 $A(x_1+x_2)/2 = b$ 推出条件。
2. 设 $x = \sum \lambda_i x_i$，代入 $A$ 得 $(\sum \lambda_i) b = b$。
