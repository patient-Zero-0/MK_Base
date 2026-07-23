---
title: "伴随矩阵"
type: definition
id: ALG-DEF-015
subject: algebra
chapter: 02-determinants
tags:
  - 矩阵
  - 伴随矩阵
  - 逆矩阵
depends:
  - ALG-DEF-011
  - ALG-THM-011
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.3"
difficulty: 2
related: []
applications:
  - '逆矩阵公式 $A^{-1} = A^* / \det A$'
---

## 定义陈述

设 $A = (a_{ij})$ 是 $n$ 阶方阵，$A_{ij}$ 是 $a_{ij}$ 的代数余子式（[[ALG-DEF-011]]）。**伴随矩阵**（adjugate matrix）$A^*$ 定义为

$$
A^* =
\begin{pmatrix}
A_{11} & A_{21} & \cdots & A_{n1} \\
A_{12} & A_{22} & \cdots & A_{n2} \\
\vdots & \vdots & \ddots & \vdots \\
A_{1n} & A_{2n} & \cdots & A_{nn}
\end{pmatrix}.
$$

即 $A^*$ 的第 $(i,j)$ 元是 $a_{ji}$ 的代数余子式 $A_{ji}$——注意**下标转置**。

## 直觉理解

伴随矩阵是将 $A$ 的每个元素换成代数余子式后转置得到的矩阵。它的核心性质是：

$$
A \cdot A^* = A^* \cdot A = (\det A) \cdot I_n.
$$

当 $\det A \neq 0$ 时，即得 $A^{-1} = \dfrac{1}{\det A} A^*$.

## 常见错误

- ✗ 忘记转置：直接把 $A_{ij}$ 放在 $(i,j)$ 位置，而不是 $(j,i)$ 位置。

## 链接

- 前置：[[ALG-DEF-011]] 代数余子式、[[ALG-THM-011]] 按一行展开
- 用于：[[ALG-THM-017]] 矩阵可逆的充要条件
