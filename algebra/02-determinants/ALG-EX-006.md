---
title: "Cramer 法则应用"
type: example
id: ALG-EX-006
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - Cramer法则
  - 线性方程组
depends:
  - ALG-THM-016
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.4"
difficulty: 3
illustrates:
  - ALG-THM-016
related: []
---

## 题目

用 Cramer 法则解方程组：

$$
\begin{cases}
x_1 + x_2 + x_3 = 6, \\
2x_1 - x_2 + x_3 = 3, \\
x_1 + 3x_2 - 2x_3 = 1.
\end{cases}
$$

## 解答

**解：** 系数矩阵

$$
A = \begin{pmatrix}
1 & 1 & 1 \\
2 & -1 & 1 \\
1 & 3 & -2
\end{pmatrix},
\quad \det A = \det\begin{pmatrix}
1 & 1 & 1 \\
2 & -1 & 1 \\
1 & 3 & -2
\end{pmatrix}.
$$

计算 $\det A$（将第 1 行 $\times (-2), (-1)$ 加到第 2、3 行，再按第 1 列展开）：

$$
\det A = \det\begin{pmatrix}
1 & 1 & 1 \\
0 & -3 & -1 \\
0 & 2 & -3
\end{pmatrix}
= 1\cdot[(-3)(-3) - (-1)(2)] = 9 + 2 = 11 \neq 0.
$$

分别计算：

$$
A_1 = \begin{pmatrix}
6 & 1 & 1 \\
3 & -1 & 1 \\
1 & 3 & -2
\end{pmatrix},\quad
A_2 = \begin{pmatrix}
1 & 6 & 1 \\
2 & 3 & 1 \\
1 & 1 & -2
\end{pmatrix},\quad
A_3 = \begin{pmatrix}
1 & 1 & 6 \\
2 & -1 & 3 \\
1 & 3 & 1
\end{pmatrix}.
$$

计算得：

$$
\det A_1 = \det\begin{pmatrix}
6 & 1 & 1 \\
3 & -1 & 1 \\
1 & 3 & -2
\end{pmatrix} = 33,\quad
\det A_2 = \det\begin{pmatrix}
1 & 6 & 1 \\
2 & 3 & 1 \\
1 & 1 & -2
\end{pmatrix} = 22,\quad
\det A_3 = \det\begin{pmatrix}
1 & 1 & 6 \\
2 & -1 & 3 \\
1 & 3 & 1
\end{pmatrix} = 11.
$$

因此

$$
x_1 = \frac{33}{11} = 3,\quad
x_2 = \frac{22}{11} = 2,\quad
x_3 = \frac{11}{11} = 1.
$$

$\blacksquare$

## 关键技巧

- 用 Cramer 法则验证解的存在唯一性比实际求解更方便（$n \geq 4$ 时计算量大）。
- 本例展示 $\det A \neq 0$ 保证唯一解，实际计算 $3 \times 3$ 系统已属边缘适用场景。
