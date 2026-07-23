---
title: "不变子空间、最小多项式与 Jordan 标准形"
type: definition
id: ALG-DEF-039
subject: algebra
chapter: 05-linear-maps
tags:
  - 不变子空间
  - 最小多项式
  - Jordan
depends:
  - ALG-DEF-035
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.5-§5.6"
difficulty: 4
related: []
applications:
  - "动力系统：Jordan 标准形直接显示系统的模态分解"
---

## 定义陈述

### 不变子空间

设 $\varphi: V \to V$ 是线性变换，$W \subseteq V$ 是子空间。若 $\varphi(W) \subseteq W$，则称 $W$ 是 $\varphi$ 的**不变子空间**（invariant subspace）。

### 最小多项式

$A$ 的**最小多项式**（minimal polynomial）$m_A(\lambda)$ 是使得 $m_A(A) = 0$ 的次数最低的首一多项式。$m_A(\lambda)$ 整除 $\chi_A(\lambda)$。

### Jordan 标准形

若 $\chi_A(\lambda)$ 在 $F$ 上可分解为一次因式之积，则 $A$ 相似于**Jordan 标准形**（Jordan canonical form）——由 Jordan 块 $\begin{pmatrix} \lambda & 1 & \\ & \lambda & \ddots \\ & & \ddots & 1 \\ & & & \lambda \end{pmatrix}$ 组成的块对角矩阵。

## 直觉理解

- **不变子空间**：变换后还在自己里面的方向——对特征向量的推广。
- **最小多项式**：使矩阵"归零"的最低次多项式——比特征多项式更精细。
- **Jordan 标准形**：几乎所有矩阵（在代数闭域上）在对角化失败时的"最佳替代"——尽量对角化，剩余部分用 1 处理。

## 链接

- 前置：[[ALG-DEF-035]] 特征值
- 用于：[[ALG-THM-042]] 最小多项式、[[ALG-THM-043]] Jordan 标准形
