---
title: "Cramer 法则综合应用"
type: problem
id: ALG-PROB-007
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - Cramer法则
  - 线性方程组
depends:
  - ALG-THM-016
  - ALG-THM-011
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.4"
difficulty: 4
related: []
tests:
  - ALG-THM-016
prerequisites:
  - "Cramer法则"
  - "Laplace展开"
---

## 题目

### 1. 含参方程组

$k$ 取何值时

$$
\begin{cases}
kx + y + z = 1, \\
x + ky + z = k, \\
x + y + kz = k^2
\end{cases}
$$

有唯一解？求该解。

### 2. 多项式插值

求不超过 2 次的多项式 $p(x)$ 使得 $p(1) = 2$, $p(2) = 3$, $p(3) = 6$。

## 提示

- 系数矩阵的行列式 $\det A = (k+2)(k-1)^2$。由 Cramer 法则，$\det A \neq 0$ 时有唯一解，即 $k \neq 1$ 且 $k \neq -2$。分别计算 $x, y, z$。
- 设 $p(x) = a_0 + a_1 x + a_2 x^2$，代入三点得 Vandermonde 型方程组，用 Cramer 法则求系数。

## 参考解答

### 解答 1. 含参方程组

系数矩阵 $A = \begin{pmatrix} k & 1 & 1 \\ 1 & k & 1 \\ 1 & 1 & k \end{pmatrix}$，$\det A = (k+2)(k-1)^2$。

唯一解条件：$k \neq 1$ 且 $k \neq -2$。

$$x = \frac{k^2 + k - 2}{(k+2)(k-1)^2}, \quad
y = \frac{-k^2 + k + 2}{(k+2)(k-1)^2}, \quad
z = \frac{(k-1)(k+1)}{(k+2)(k-1)^2}.$$

### 解答 2. 多项式插值

由 Vandermonde 行列式 $\det \begin{pmatrix}1&1&1\\1&2&4\\1&3&9\end{pmatrix} = (3-1)(3-2)(2-1) = 2$，

用 Cramer 法则解得 $p(x) = 1 - \frac{1}{2}x + \frac{1}{2}x^2$。

验证：$p(1)=2, p(2)=3, p(3)=6$ 成立。
