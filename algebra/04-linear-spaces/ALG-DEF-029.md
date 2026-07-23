---
title: "子空间的和与直和"
type: definition
id: ALG-DEF-029
subject: algebra
chapter: 04-linear-spaces
tags:
  - 子空间
  - 和
  - 直和
depends:
  - ALG-DEF-024
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.5"
difficulty: 3
related: []
applications:
  - "量子力学：多粒子系统的 Hilbert 空间是单粒子空间的张量积（而非直和），但正交补分解是直和"
---

## 定义陈述

设 $U, W$ 是 $V$ 的子空间。定义它们的**和**（sum）为

$$
U + W = \{u + w \mid u \in U, w \in W\}.
$$

若 $U \cap W = \{0\}$，则称 $U + W$ 为**直和**（direct sum），记作 $U \oplus W$。

直和等价刻画：和 $U + W$ 中每个向量可**唯一**地表示为 $u + w$。

## 直觉理解

- **和**：两个子空间所有可能加法的集合。
- **直和**：两个子空间互不相交（只在 0 相交），此时和是"无冗余"的。

**几何**：$\mathbb{R}^3$ 中 $xy$-平面与 $z$-轴的和是 $\mathbb{R}^3$，且是直和（交只有原点）。

## 链接

- 前置：[[ALG-DEF-024]] 子空间
- 用于：[[ALG-THM-030]] 维数公式、[[ALG-THM-031]] 直和判定
