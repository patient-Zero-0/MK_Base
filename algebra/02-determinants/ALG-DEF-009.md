---
title: "排列、逆序数与奇偶排列"
type: definition
id: ALG-DEF-009
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - 排列
  - 逆序数
  - 奇偶性
depends: []
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.1"
difficulty: 1
related:
  - ALG-DEF-010
applications:
  - "计算机科学：排序算法的逆序对计数（冒泡排序交换次数）"
---

## 定义陈述

### 排列

$n$ 个元素 $1, 2, \ldots, n$ 的一个**排列**（permutation）是它们的一个有序排布，记作 $(i_1, i_2, \ldots, i_n)$。全体 $n$ 元排列的集合记作 $S_n$，共有 $n!$ 个元素。

### 逆序与逆序数

在排列 $(i_1, i_2, \ldots, i_n)$ 中，若 $p < q$ 但 $i_p > i_q$，则称数对 $(i_p, i_q)$ 构成一个**逆序**（inversion）。排列的**逆序数**（inversion number）是其中逆序的总数，记作 $\tau(i_1, i_2, \ldots, i_n)$。

### 奇偶排列

- 若 $\tau$ 为偶数，称该排列为**偶排列**（even permutation）；
- 若 $\tau$ 为奇数，称该排列为**奇排列**（odd permutation）。

**符号**：排列 $\pi$ 的符号 $\operatorname{sgn}(\pi) = (-1)^{\tau(\pi)}$，即偶排列取 $+1$，奇排列取 $-1$。

### 对换

交换排列中两个元素的位置称为一次**对换**（transposition）。每次对换改变排列的奇偶性。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 排列 $\pi \in S_n$ | $1,\ldots,n$ 的有序排布 |
| 逆序数 $\tau(\pi)$ | 排列中大小次序颠倒的对数 |
| 符号 $\operatorname{sgn}(\pi)$ | $= (-1)^{\tau(\pi)}$：偶→$+1$，奇→$-1$ |
| 对换 | 交换两个元素的操作，改变奇偶性 |

## 直觉理解

**逆序数**衡量一个排列"乱序"的程度：$i_1, i_2, \ldots, i_n$ 是标准顺序，每有一对"大的在前、小的在后"就记一个逆序。

- 标准排列 $(1, 2, 3)$：逆序数 $0$，偶排列。
- $(3, 2, 1)$：逆序有 $(3,2), (3,1), (2,1)$，$\tau = 3$，奇排列。
- $(2, 3, 1)$：逆序有 $(2,1), (3,1)$，$\tau = 2$，偶排列。

**符号 $\operatorname{sgn}(\pi)$** 在行列式的完全展开定义（[[ALG-DEF-010]]）中扮演核心角色：每一项带 $\operatorname{sgn}(\pi)$ 的符号。

## 基本性质

1. $S_n$ 中奇偶排列各占一半（各 $n!/2$ 个，$n \geq 2$）。
2. 对换改变奇偶性：一次对换使 $\tau$ 变化 $\pm 1$（模 $2$ 意义下）。
3. $\operatorname{sgn}(\pi_1 \circ \pi_2) = \operatorname{sgn}(\pi_1) \cdot \operatorname{sgn}(\pi_2)$。
4. 偶排列可表示为偶数次对换的复合，奇排列可表示为奇数次对换的复合。

## 链接

- 用于：[[ALG-DEF-010]] $n$ 阶行列式的完全展开定义
- 关联：后续代数学中交错群的生成（$A_n = \{\text{偶排列}\}$）
