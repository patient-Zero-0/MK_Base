---
title: "基变换与过渡矩阵"
type: definition
id: ALG-DEF-028
subject: algebra
chapter: 04-linear-spaces
tags:
  - 基变换
  - 过渡矩阵
  - 坐标
depends:
  - ALG-DEF-027
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.4"
difficulty: 3
related: []
applications:
  - "计算机图形：不同坐标系间的变换矩阵就是过渡矩阵"
---

## 定义陈述

设 $B = \{v_1, \ldots, v_n\}$ 和 $B' = \{v'_1, \ldots, v'_n\}$ 是 $V$ 的两组基。将 $B'$ 的每个基向量用 $B$ 表示：

$$
v'_j = \sum_{i=1}^n p_{ij} v_i, \quad j = 1, \ldots, n.
$$

称矩阵 $P = (p_{ij})$ 为从基 $B$ 到基 $B'$ 的**过渡矩阵**（transition matrix）。

坐标变换公式：若 $[v]_B$ 和 $[v]_{B'}$ 是同一向量在不同基下的坐标，则

$$
[v]_B = P [v]_{B'}, \quad [v]_{B'} = P^{-1} [v]_B.
$$

## 直觉理解

过渡矩阵 $P$ 的 $j$ 列正是 $v'_j$ 在 $B$ 下的坐标。左乘 $P$ 表示"从新基坐标换算到旧基坐标"。

## 链接

- 前置：[[ALG-DEF-027]] 向量的坐标
- 用于：[[ALG-THM-032]] 坐标变换公式
