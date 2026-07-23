---
title: "向量的坐标"
type: definition
id: ALG-DEF-027
subject: algebra
chapter: 04-linear-spaces
tags:
  - 坐标
  - 基
  - 线性空间
depends:
  - ALG-DEF-026
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.3"
difficulty: 2
related: []
applications:
  - "计算机图形：模型顶点坐标是相对于局部基的表示"
---

## 定义陈述

设 $B = \{v_1, \ldots, v_n\}$ 是 $n$ 维线性空间 $V$ 的一组基。对任意 $v \in V$，存在唯一的一组系数 $(a_1, \ldots, a_n) \in F^n$ 使

$$
v = a_1 v_1 + \cdots + a_n v_n.
$$

这组系数称为 $v$ 在基 $B$ 下的**坐标**（coordinates），记为 $[v]_B = (a_1, \ldots, a_n)^\top$。

## 直觉理解

坐标 = "用基的语言描述向量"。选不同的基，同一向量的坐标不同。标准基下的坐标就是我们通常说的"分量"。

## 链接

- 前置：[[ALG-DEF-026]] 基与维数
- 用于：[[ALG-DEF-028]] 基变换与过渡矩阵
