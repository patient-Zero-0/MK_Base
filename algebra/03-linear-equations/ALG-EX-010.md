---
title: "求齐次方程组的基础解系"
type: example
id: ALG-EX-010
subject: algebra
chapter: 03-linear-equations
tags:
  - 线性方程组
  - 基础解系
  - 解空间
depends:
  - ALG-THM-025
  - ALG-DEF-022
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.4"
difficulty: 3
illustrates:
  - ALG-THM-025
related: []
---

## 题目

求齐次方程组 $Ax = 0$ 的基础解系，其中

$$
A = \begin{pmatrix}
1 & 2 & -1 & 1 \\
2 & 4 & -2 & 2 \\
-1 & -2 & 1 & -1
\end{pmatrix}.
$$

## 解答

**解：** 化为行阶梯形：

$$
\begin{pmatrix}
1 & 2 & -1 & 1 \\
2 & 4 & -2 & 2 \\
-1 & -2 & 1 & -1
\end{pmatrix}
\rightarrow \begin{pmatrix}
1 & 2 & -1 & 1 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}.
$$

所以 $\operatorname{rank}(A) = 1$，基础解系含 $n - r = 4 - 1 = 3$ 个向量。

自由变量为 $x_2, x_3, x_4$，取 $(x_2, x_3, x_4) = (1,0,0), (0,1,0), (0,0,1)$，得：

$$
\eta_1 = (-2, 1, 0, 0),\quad
\eta_2 = (1, 0, 1, 0),\quad
\eta_3 = (-1, 0, 0, 1).
$$

通解：$x = c_1 \eta_1 + c_2 \eta_2 + c_3 \eta_3$，$c_i \in \mathbb{R}$。

$\blacksquare$
