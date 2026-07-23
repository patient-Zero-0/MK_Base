---
title: "Gauss 消元求解线性方程组"
type: example
id: ALG-EX-008
subject: algebra
chapter: 03-linear-equations
tags:
  - 线性方程组
  - Gauss消元
  - 阶梯形
depends:
  - ALG-THM-019
  - ALG-DEF-021
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.2"
difficulty: 2
illustrates:
  - ALG-THM-019
related: []
---

## 题目

用 Gauss 消元法解线性方程组：

$$
\begin{cases}
x_1 + 2x_2 + x_3 = 8, \\
2x_1 + 3x_2 + 4x_3 = 20, \\
3x_1 + x_2 + 2x_3 = 11.
\end{cases}
$$

## 解答

**解：** 写出增广矩阵 $(A \mid b)$：

$$
\begin{pmatrix}
1 & 2 & 1 & 8 \\
2 & 3 & 4 & 20 \\
3 & 1 & 2 & 11
\end{pmatrix}.
$$

第 1 行 $\times(-2)$ 加到第 2 行，$\times(-3)$ 加到第 3 行：

$$
\rightarrow \begin{pmatrix}
1 & 2 & 1 & 8 \\
0 & -1 & 2 & 4 \\
0 & -5 & -1 & -13
\end{pmatrix}.
$$

第 2 行 $\times(-5)$ 加到第 3 行：

$$
\rightarrow \begin{pmatrix}
1 & 2 & 1 & 8 \\
0 & -1 & 2 & 4 \\
0 & 0 & -11 & -33
\end{pmatrix}.
$$

回代：$x_3 = 3$，$x_2 = 2$，$x_1 = 1$。解为 $(1, 2, 3)$。

$\blacksquare$
