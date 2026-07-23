---
title: "Cayley–Hamilton 应用 / Jordan 标准形"
type: example
id: ALG-EX-017
subject: algebra
chapter: 05-linear-maps
tags:
  - Cayley-Hamilton
  - Jordan
  - 矩阵幂
depends:
  - ALG-THM-041
  - ALG-THM-043
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.5-§5.6"
difficulty: 4
illustrates:
  - ALG-THM-041
related: []
---

## 题目

已知 $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$。

1. 求 $\chi_A(\lambda)$ 并验证 Cayley–Hamilton 定理。
2. 求 $A$ 的 Jordan 标准形。
3. 利用 Jordan 标准形求 $A^n$。

## 解答

**解：**

1. $\chi_A(\lambda) = (\lambda-2)^2$。验证：
   $(A-2I)^2 = \begin{pmatrix} 0&1\\0&0 \end{pmatrix}^2 = 0$。✓

2. $A$ 的特征值 $2$，代数重数 2，几何重数 1。Jordan 标准形：
   $J = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$（即 $A$ 本身就是 Jordan 块）。

3. 由 $A = 2I + N$，$N = \begin{pmatrix}0&1\\0&0\end{pmatrix}$，$N^2 = 0$：
   $A^n = (2I + N)^n = 2^n I + n 2^{n-1} N = \begin{pmatrix} 2^n & n2^{n-1} \\ 0 & 2^n \end{pmatrix}$。

$\blacksquare$
