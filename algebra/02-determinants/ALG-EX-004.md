---
title: "用性质 + 降阶展开计算具体行列式"
type: example
id: ALG-EX-004
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - 计算
depends:
  - ALG-THM-010
  - ALG-THM-011
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.3"
difficulty: 3
illustrates:
  - ALG-THM-010
  - ALG-THM-011
related: []
---

## 题目

计算 $\det A = \det\begin{pmatrix}1&2&3&4\\2&3&4&1\\3&4&1&2\\4&1&2&3\end{pmatrix}$。

## 分析

直接计算 $4! = 24$ 项繁琐。用行变换化为上三角再乘对角元，或先用性质化简再展开。

关键观察：各行元素和相同（$1+2+3+4=10$），将第 2、3、4 列加到第 1 列可提取公因子。

## 解答

**解：** 将第 2、3、4 列加到第 1 列，行列式不变：

$$
\det A = \det\begin{pmatrix}10&2&3&4\\10&3&4&1\\10&4&1&2\\10&1&2&3\end{pmatrix}
= 10\cdot\det\begin{pmatrix}1&2&3&4\\1&3&4&1\\1&4&1&2\\1&1&2&3\end{pmatrix}.
$$

第 1 行 $\times (-1)$ 加到第 2、3、4 行：

$$
= 10\cdot\det\begin{pmatrix}1&2&3&4\\0&1&1&-3\\0&2&-2&-2\\0&-1&-1&-1\end{pmatrix}.
$$

按第 1 列展开得 $3$ 阶行列式：

$$
= 10\cdot\det\begin{pmatrix}1&1&-3\\2&-2&-2\\-1&-1&-1\end{pmatrix}.
$$

第 2 行提出 2，第 3 行提出 $-1$：

$$
= 10\cdot 2\cdot (-1)\cdot\det\begin{pmatrix}1&1&-3\\1&-1&-1\\1&1&1\end{pmatrix} = -20\cdot\det\begin{pmatrix}1&1&-3\\1&-1&-1\\1&1&1\end{pmatrix}.
$$

第 1 行 $\times (-1)$ 加到第 2、3 行：

$$
= -20\cdot\det\begin{pmatrix}1&1&-3\\0&-2&2\\0&0&4\end{pmatrix} = -20 \cdot 1 \cdot (-2) \cdot 4 = 160.
$$

$\blacksquare$

## 关键技巧

- **行和相等 ⇒ 加到第 1 列提取公因子**——循环矩阵的常见技巧。
- 每次变换后及时展开降阶，避免高维手算。

## 变式

- **变式 1**：$\det\begin{pmatrix}1&1&1\\1&2&4\\1&3&9\end{pmatrix}$——Vandermonde 行列式特例，直接代公式。
