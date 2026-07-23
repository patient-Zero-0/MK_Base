---
title: "求特征值、特征向量并对角化"
type: example
id: ALG-EX-016
subject: algebra
chapter: 05-linear-maps
tags:
  - 特征值
  - 特征向量
  - 对角化
depends:
  - ALG-THM-040
  - ALG-DEF-038
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.4"
difficulty: 3
illustrates:
  - ALG-THM-040
related: []
---

## 题目

判断 $A = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$ 是否可对角化。若可，求 $P$ 和 $D$。

## 解答

**解：** 特征多项式：

$$
\det(\lambda I - A) = \det\begin{pmatrix} \lambda-2 & -1 & 0 \\ 0 & \lambda-2 & 0 \\ 0 & 0 & \lambda-3 \end{pmatrix} = (\lambda-2)^2(\lambda-3).
$$

特征值 $\lambda = 2$（代数重数 2），$\lambda = 3$（代数重数 1）。

对 $\lambda = 2$：解 $(A - 2I)v = 0$：

$$
\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}v = 0 \Rightarrow v = (1,0,0)^\top.
$$

几何重数 = 1 < 代数重数 2，所以 **不可对角化**。

$\blacksquare$
