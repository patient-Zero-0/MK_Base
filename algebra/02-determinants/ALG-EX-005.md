---
title: "Vandermonde 行列式应用"
type: example
id: ALG-EX-005
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - Vandermonde
  - 应用
depends:
  - ALG-THM-013
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.2"
difficulty: 3
illustrates:
  - ALG-THM-013
related: []
---

## 题目

1. 证明：$\det\begin{pmatrix}1&a&a^2&a^4\\1&b&b^2&b^4\\1&c&c^2&c^4\\1&d&d^2&d^4\end{pmatrix} = (a+b+c+d+\cdots)\prod_{i<j}(x_j-x_i)$。
2. 求 $\det\begin{pmatrix}1&1&1\\x_1&x_2&x_3\\x_1^3&x_2^3&x_3^3\end{pmatrix}$。

## 分析

第 1 题不是标准 Vandermonde（幂次跳跃了 $x^3$），可通过补行/列凑成 Vandermonde 后比较系数。

## 解答

### 第 2 题

$$
\det\begin{pmatrix}1&1&1\\x_1&x_2&x_3\\x_1^3&x_2^3&x_3^3\end{pmatrix}
$$

补成 4 阶 Vandermonde：考虑 $V_4(x_1,x_2,x_3,y)$ 中 $y^2$ 的系数可得。结果为

$$
= (x_1+x_2+x_3)(x_1-x_2)(x_1-x_3)(x_2-x_3).
$$

## 关键技巧

- 补行/列法是 Vandermonde 应用的核心技巧。
