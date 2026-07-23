---
title: "$n$ 阶行列式（完全展开定义）"
type: definition
id: ALG-DEF-010
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - n阶行列式
  - 完全展开
depends:
  - ALG-DEF-009
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.1"
difficulty: 3
related:
  - ALG-DEF-011
  - ALG-THM-010
applications:
  - "解析几何：二阶/三阶行列式对应有向面积/体积"
---

## 定义陈述

设 $A = (a_{ij})$ 是 $n$ 阶方阵。$A$ 的**行列式**（determinant），记作 $\det A$ 或 $|A|$，定义为

$$
\det A = \sum_{\pi \in S_n} \operatorname{sgn}(\pi) \, a_{1,\pi(1)} \, a_{2,\pi(2)} \, \cdots \, a_{n,\pi(n)},
$$

其中 $\pi$ 跑遍 $S_n$ 中所有 $n!$ 个排列，$\operatorname{sgn}(\pi) = (-1)^{\tau(\pi)}$ 是排列的符号（[[ALG-DEF-009]]）。

### 低阶展开

- $n = 1$：$\det(a) = a$。
- $n = 2$：$\det\begin{pmatrix}a&b\\c&d\end{pmatrix} = ad - bc$。
- $n = 3$：$\det\begin{pmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{pmatrix} = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33} - a_{13}a_{22}a_{31}$（Sarrus 法则）。

## 直觉理解

行列式的完全展开有 $n!$ 项，每项从每行每列各取一个元素相乘，再按列标的排列奇偶性赋予符号。

> $2$ 阶：$\det = ad - bc$——对角积减反对角积。
> $3$ 阶：可用 Sarrus 法则记忆——三条主对角线（加）和三条反对角线（减）。

**为什么 $n \geq 4$ 时不建议用定义直接计算**：$4! = 24$ 项尚可手工，$5! = 120$ 项已繁，$10! \approx 3.6 \times 10^6$——定义主要用于理论推导，实际计算用性质（[[ALG-THM-010]]）或展开公式。

## 链接

- 前置：[[ALG-DEF-009]] 排列与逆序数
- 核心性质：[[ALG-THM-010]] 行列式基本性质
- 展开工具：[[ALG-DEF-011]] 余子式与代数余子式
