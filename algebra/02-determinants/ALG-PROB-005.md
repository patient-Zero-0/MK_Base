---
title: "行列式计算综合"
type: problem
id: ALG-PROB-005
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - 计算
  - 递推
depends:
  - ALG-THM-010
  - ALG-THM-011
uses:
  - ALG-DEF-014
  - ALG-THM-013
status: draft
source: "丘维声《高等代数》第3版 §2.2-§2.3"
difficulty: 4
related:
  - ALG-THM-018
tests:
  - ALG-THM-013
  - ALG-THM-011
prerequisites:
  - "行列式基本性质"
  - "Laplace展开"
---

## 题目

计算以下 $n$ 阶行列式：

1. **三对角行列式**：$D_n = \det\begin{pmatrix}
a & b & 0 & \cdots & 0 \\
c & a & b & \cdots & 0 \\
0 & c & a & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & a
\end{pmatrix}$。

2. **循环行列式**：$C_n = \det\begin{pmatrix}
x_1 & x_2 & x_3 & \cdots & x_n \\
x_n & x_1 & x_2 & \cdots & x_{n-1} \\
x_{n-1} & x_n & x_1 & \cdots & x_{n-2} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
x_2 & x_3 & x_4 & \cdots & x_1
\end{pmatrix}$。

## 提示

1. 三对角行列式：按第 1 行展开，得到递推关系 $D_n = a D_{n-1} - bc D_{n-2}$。解特征方程 $t^2 - at + bc = 0$。

2. 循环行列式：利用单位根 $\omega = e^{2\pi i/n}$，构造 $f(\omega^k) = \sum_{j=1}^n x_j \omega^{k(j-1)}$，则 $C_n = \prod_{k=0}^{n-1} f(\omega^k)$。

## 参考解答

### 1. 三对角行列式

按第一行展开：
$$
D_n = a \cdot D_{n-1} - b \cdot \det\begin{pmatrix}
c & b & 0 \\
0 & a & b \\
\vdots & \vdots & \ddots
\end{pmatrix} = a D_{n-1} - bc D_{n-2}.
$$

解特征方程 $t^2 - at + bc = 0$，设两根为 $\alpha, \beta$。

若 $\alpha \neq \beta$：$D_n = \frac{\alpha^{n+1} - \beta^{n+1}}{\alpha - \beta}$。
若 $\alpha = \beta$：$D_n = (n+1)\alpha^n$。

### 2. 循环行列式

令 $f(x) = x_1 + x_2 x + \cdots + x_n x^{n-1}$，$\omega = e^{2\pi i/n}$。则 $C_n = \prod_{k=0}^{n-1} f(\omega^k)$。
