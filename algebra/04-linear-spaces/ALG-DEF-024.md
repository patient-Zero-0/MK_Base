---
title: "子空间"
type: definition
id: ALG-DEF-024
subject: algebra
chapter: 04-linear-spaces
tags:
  - 子空间
  - 线性空间
depends:
  - ALG-DEF-023
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.2"
difficulty: 2
related: []
applications:
  - '编码理论：线性码是 $\mathbb{F}_q^n$ 的子空间'
---

## 定义陈述

设 $V$ 是 $F$ 上的线性空间，$W \subseteq V$ 是非空子集。若 $W$ 对 $V$ 的加法和数乘运算也构成 $F$ 上的线性空间，则称 $W$ 是 $V$ 的**子空间**（subspace）。

等价判定（**子空间判别法**）：$W \subseteq V$ 是子空间 $\iff$

1. $0 \in W$；
2. 对任意 $u, v \in W$，$u + v \in W$（加法封闭）；
3. 对任意 $a \in F$，$v \in W$，$a v \in W$（数乘封闭）。

## 直觉理解

子空间 = 包含在原空间里的"更小的线性空间"——必须过原点，且对加法和数乘封闭。比如 $\mathbb{R}^3$ 中过原点的直线和平面都是子空间。

## 链接

- 前置：[[ALG-DEF-023]] 线性空间
- 用于：[[ALG-DEF-025]] 生成子空间、[[ALG-DEF-029]] 子空间的和与直和
