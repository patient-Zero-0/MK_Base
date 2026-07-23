---
title: "线性空间（向量空间）公理"
type: definition
id: ALG-DEF-023
subject: algebra
chapter: 04-linear-spaces
tags:
  - 线性空间
  - 向量空间
  - 公理
depends: []
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.1"
difficulty: 2
related: []
applications:
  - "量子力学：态空间是 Hilbert 空间（带内积的线性空间）"
  - "信号处理：函数空间的基展开（Fourier 级数）"
---

## 定义陈述

设 $F$ 是一个域（通常取 $\mathbb{R}$ 或 $\mathbb{C}$），$V$ 是一个非空集合，其上定义了**加法** $+ : V \times V \to V$ 和**数乘** $\cdot : F \times V \to V$。若满足以下 8 条公理，则称 $V$ 是 $F$ 上的**线性空间**（或向量空间）：

**加法公理**（$u, v, w \in V$）：

1. 交换律：$u + v = v + u$
2. 结合律：$(u + v) + w = u + (v + w)$
3. 零元：存在 $0 \in V$ 使 $v + 0 = v$
4. 负元：对每个 $v$ 存在 $-v$ 使 $v + (-v) = 0$

**数乘公理**（$a, b \in F$）：
5. 结合律：$a(bv) = (ab)v$
6. 分配律 I：$(a + b)v = av + bv$
7. 分配律 II：$a(u + v) = au + av$
8. 单位元：$1 \cdot v = v$

## 直觉理解

线性空间是所有"可以加和可以乘标量"的对象的集合。$\mathbb{R}^n$ 是最典型的例子，但多项式、函数、矩阵等也构成线性空间。关键是两条运算**封闭**且满足这些自然的代数性质。

## 常见例子

- $\mathbb{R}^n$（实 $n$ 维向量空间）
- $F[x]$（系数在 $F$ 上的一元多项式全体）
- $M_{m \times n}(F)$（$m \times n$ 矩阵全体）
- $C[a,b]$（闭区间上连续函数全体）

## 链接

- 用于：[[ALG-DEF-024]] 子空间、[[ALG-DEF-030]] 线性空间的同构
