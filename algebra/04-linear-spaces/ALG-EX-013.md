---
title: "求基、维数与坐标"
type: example
id: ALG-EX-013
subject: algebra
chapter: 04-linear-spaces
tags:
  - 基
  - 维数
  - 坐标
depends:
  - ALG-DEF-026
  - ALG-DEF-027
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.3"
difficulty: 3
illustrates:
  - ALG-DEF-026
related: []
---

## 题目

设 $V = \{(x_1, x_2, x_3, x_4) \in \mathbb{R}^4 \mid x_1 + x_2 + x_3 + x_4 = 0\}$。

1. 证明 $V$ 是 $\mathbb{R}^4$ 的子空间，并求 $\dim V$。
2. 求 $V$ 的一组基，并求向量 $(1, -1, 1, -1)$ 在这组基下的坐标。

## 解答

**解：**

1. $0 \in V$；对 $u, v \in V$，$(u+v)$ 的分量和也为零；数乘同理。$\dim V = 4 - 1 = 3$。

2. 取自由变量 $x_2, x_3, x_4$，令 $x_1 = -(x_2+x_3+x_4)$。令三个自由变量分别取 $(1,0,0), (0,1,0), (0,0,1)$ 得基：
   $B = \{\alpha_1 = (-1,1,0,0), \alpha_2 = (-1,0,1,0), \alpha_3 = (-1,0,0,1)\}$。

   解 $v = x_1\alpha_1 + x_2\alpha_2 + x_3\alpha_3$ 得 $v$ 的坐标为 $[v]_B = (2, 0, -1)$。

$\blacksquare$
