---
title: "伴随矩阵求逆应用"
type: example
id: ALG-EX-007
subject: algebra
chapter: 02-determinants
tags:
  - 矩阵
  - 伴随矩阵
  - 逆矩阵
depends:
  - ALG-DEF-015
  - ALG-THM-017
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.4"
difficulty: 3
illustrates:
  - ALG-DEF-015
related: []
---

## 题目

已知 $A = \begin{pmatrix} 1 & 2 & -1 \\ 3 & 1 & 0 \\ -1 & 0 & 2 \end{pmatrix}$，求 $A^{-1}$。

## 分析

用公式 $A^{-1} = \dfrac{1}{\det A} A^*$。先计算 $\det A$，再计算所有 9 个代数余子式并构造 $A^*$。

## 解答

**解：** 先计算 $\det A$（按第 3 行展开方便）：

$$
\det A = (-1)\cdot\det\begin{pmatrix}2&-1\\1&0\end{pmatrix} + 0\cdot(\cdots) + 2\cdot\det\begin{pmatrix}1&2\\3&1\end{pmatrix} = (-1)(1) + 2(1-6) = -1 - 10 = -11.
$$

计算代数余子式 $A_{ij} = (-1)^{i+j} M_{ij}$：

$$
\begin{aligned}
A_{11} &= \det\begin{pmatrix}1&0\\0&2\end{pmatrix} = 2, &
A_{12} &= -\det\begin{pmatrix}3&0\\-1&2\end{pmatrix} = -6, &
A_{13} &= \det\begin{pmatrix}3&1\\-1&0\end{pmatrix} = 1, \\\\
A_{21} &= -\det\begin{pmatrix}2&-1\\0&2\end{pmatrix} = -4, &
A_{22} &= \det\begin{pmatrix}1&-1\\-1&2\end{pmatrix} = 1, &
A_{23} &= -\det\begin{pmatrix}1&2\\-1&0\end{pmatrix} = -2, \\\\
A_{31} &= \det\begin{pmatrix}2&-1\\1&0\end{pmatrix} = 1, &
A_{32} &= -\det\begin{pmatrix}1&-1\\3&0\end{pmatrix} = -3, &
A_{33} &= \det\begin{pmatrix}1&2\\3&1\end{pmatrix} = -5.
\end{aligned}
$$

伴随矩阵（**注意转置**）：

$$
A^* = \begin{pmatrix}
2 & -4 & 1 \\
-6 & 1 & -3 \\
1 & -2 & -5
\end{pmatrix}.
$$

所以

$$
A^{-1} = \frac{1}{-11} \begin{pmatrix}
2 & -4 & 1 \\
-6 & 1 & -3 \\
1 & -2 & -5
\end{pmatrix}
= \begin{pmatrix}
-\frac{2}{11} & \frac{4}{11} & -\frac{1}{11} \\
\frac{6}{11} & -\frac{1}{11} & \frac{3}{11} \\
-\frac{1}{11} & \frac{2}{11} & \frac{5}{11}
\end{pmatrix}.
$$

验证 $A A^{-1} = I$ 留给读者。

$\blacksquare$

## 关键技巧

- 伴随矩阵求逆理论价值高，实际 $n \geq 4$ 时计算量大，实践用高斯消元。
- 验证公式：$A \cdot A^* = (\det A) I$——正确性的保险丝。
