---
title: "矩阵与矩阵的初等变换"
type: definition
id: ALG-DEF-016
subject: algebra
chapter: 03-linear-equations
tags:
  - 矩阵
  - 初等变换
depends: []
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.1"
difficulty: 1
related: []
applications:
  - "数值分析：LU 分解与 Gauss 消元都是初等变换的矩阵乘积"
---

## 定义陈述

**矩阵**是 $m \times n$ 个数排成的矩形阵列：

$$
A = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}.
$$

称 $m=n$ 时为**方阵**，$m=1$ 时为**行向量**，$n=1$ 时为**列向量**。

**矩阵的初等行变换**指以下三种操作：

1. **行交换**：交换两行的位置；
2. **行倍乘**：某行乘以非零常数；
3. **行倍加**：某行的 $k$ 倍加到另一行。

类似定义**初等列变换**。初等行 / 列变换统称**初等变换**。

## 直觉理解

初等变换是解线性方程组的"允许操作"——对应方程组中两个方程互换、方程两边同乘非零数、一个方程的 $k$ 倍加到另一个方程。这些操作不改变方程组的解，只是让形式更简单。

对应的矩阵就是**初等矩阵**（单位阵执行一次初等变换所得），左乘行变换、右乘列变换。

## 链接

- 用于：[[ALG-DEF-017]] 阶梯形、[[ALG-THM-019]] Gauss 消元法
