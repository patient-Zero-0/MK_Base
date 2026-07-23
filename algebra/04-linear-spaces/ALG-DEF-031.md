---
title: "商空间（进阶）"
type: definition
id: ALG-DEF-031
subject: algebra
chapter: 04-linear-spaces
tags:
  - 商空间
  - 子空间
depends:
  - ALG-DEF-024
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.5"
difficulty: 4
related: []
applications:
  - "泛函分析：Banach 空间的商空间用于研究闭子空间的补"
---

## 定义陈述

设 $V$ 是线性空间，$W$ 是 $V$ 的子空间。定义 $V$ 上的等价关系：$u \sim v \iff u - v \in W$。

记 $v + W = \{v + w \mid w \in W\}$ 为等价类。所有等价类的集合记为 $V/W$，称为 $V$ 模 $W$ 的**商空间**（quotient space）。

在 $V/W$ 上定义加法和数乘：

$$
(v_1 + W) + (v_2 + W) = (v_1 + v_2) + W, \quad
a(v + W) = av + W.
$$

$V/W$ 构成线性空间，且 $\dim(V/W) = \dim V - \dim W$。

## 直觉理解

商空间把 $W$ 的方向全部"压缩为零"，只保留垂直于 $W$ 的方向。相当于把 $V$ 按 $W$ 折叠——平行于 $W$ 的向量被识别为同一个点。

## 链接

- 前置：[[ALG-DEF-024]] 子空间
- 用于：[[ALG-THM-035]] 补空间的存在性
