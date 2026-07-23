---
title: "基变换与过渡矩阵计算"
type: example
id: ALG-EX-014
subject: algebra
chapter: 04-linear-spaces
tags:
  - 基变换
  - 过渡矩阵
depends:
  - ALG-DEF-028
  - ALG-THM-032
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.4"
difficulty: 3
illustrates:
  - ALG-DEF-028
related: []
---

## 题目

在 $\mathbb{R}^3$ 中有两组基：

$B = \{(1,0,0), (0,1,0), (0,0,1)\}$，
$B' = \{(1,1,0), (1,0,1), (0,1,1)\}$。

1. 求从 $B$ 到 $B'$ 的过渡矩阵。
2. 求向量 $v = (3,2,1)$ 在 $B'$ 下的坐标。

## 解答

**解：**

1. $B'$ 的向量在 $B$（标准基）下的坐标就是它们本身，排成列得过渡矩阵
   $P = \begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix}$。

2. $[v]_B = (3,2,1)^\top$。$[v]_{B'} = P^{-1}[v]_B$。

   计算 $P^{-1} = \frac12\begin{pmatrix}1&1&-1\\1&-1&1\\-1&1&1\end{pmatrix}$，得 $[v]_{B'} = (2,1,0)^\top$。

$\blacksquare$
