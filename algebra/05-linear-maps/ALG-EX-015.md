---
title: "求线性变换的矩阵、核与像"
type: example
id: ALG-EX-015
subject: algebra
chapter: 05-linear-maps
tags:
  - 线性变换
  - 矩阵表示
  - 核
  - 像
depends:
  - ALG-DEF-033
  - ALG-DEF-034
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.2"
difficulty: 3
illustrates:
  - ALG-DEF-033
  - ALG-DEF-034
related: []
---

## 题目

设 $\varphi: \mathbb{R}^3 \to \mathbb{R}^3$ 定义为 $\varphi(x,y,z) = (x+y, y+z, z+x)$。

1. 求 $\varphi$ 在标准基下的矩阵 $A$。
2. 求 $\ker \varphi$ 和 $\operatorname{im} \varphi$ 的基与维数。
3. 验证秩-零化度定理。

## 解答

**解：**

1. $\varphi(1,0,0) = (1,0,1)$，$\varphi(0,1,0) = (1,1,0)$，$\varphi(0,0,1) = (0,1,1)$。
   所以 $A = \begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix}$。

2. 解 $Av = 0$ 得 $\ker \varphi = \operatorname{span}\{(1,-1,1)\}$，$\dim \ker \varphi = 1$。
   $\operatorname{im} \varphi = \operatorname{span}\{(1,0,1), (1,1,0), (0,1,1)\}$，$\dim \operatorname{im} \varphi = 2$。

3. $\dim \mathbb{R}^3 = 3 = 1 + 2 = \dim \ker \varphi + \dim \operatorname{im} \varphi$。✓

$\blacksquare$
