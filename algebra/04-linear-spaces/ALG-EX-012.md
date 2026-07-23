---
title: "验证线性空间 / 子空间"
type: example
id: ALG-EX-012
subject: algebra
chapter: 04-linear-spaces
tags:
  - 线性空间
  - 子空间
  - 验证
depends:
  - ALG-DEF-023
  - ALG-DEF-024
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.1-§4.2"
difficulty: 3
illustrates:
  - ALG-DEF-024
related: []
---

## 题目

判断下列集合是否构成 $\mathbb{R}^3$ 的子空间，并说明理由：

1. $W_1 = \{(x, y, z) \in \mathbb{R}^3 \mid x + y + z = 0\}$。
2. $W_2 = \{(x, y, z) \in \mathbb{R}^3 \mid x + y + z = 1\}$。
3. $W_3 = \{(x, y, z) \in \mathbb{R}^3 \mid x^2 + y^2 = z^2\}$。

## 解答

**解：**

1. $W_1$ 是子空间。验证：$(0,0,0) \in W_1$；设 $u, v \in W_1$，则坐标和为零，$u+v$ 的坐标和也为零；$a u$ 同理。

2. $W_2$ **不是**子空间。因为 $(0,0,0) \notin W_2$（原点不满足 $0+0+0=1$），子空间必须包含零向量。

3. $W_3$ **不是**子空间。虽然包含零向量且对数乘封闭（若 $(x,y,z)$ 满足 $x^2+y^2=z^2$，则 $(ax)^2+(ay)^2 = a^2(x^2+y^2) = a^2 z^2 = (az)^2$），但加法不封闭：$(1,0,1) \in W_3$，$(0,1,1) \in W_3$，但 $(1,1,2)$ 不满足 $1^2+1^2=2 \neq 4 = 2^2$。

$\blacksquare$
