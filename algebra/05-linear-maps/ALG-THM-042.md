---
title: "最小多项式及其性质"
type: theorem
id: ALG-THM-042
subject: algebra
chapter: 05-linear-maps
tags:
  - 最小多项式
  - 特征多项式
depends:
  - ALG-THM-041
  - ALG-DEF-039
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.5"
difficulty: 4
related: []
corollaries: []
applications:
  - "判断矩阵可对角化：最小多项式无重根 ⇔ 矩阵可对角化"
---

## 条件

设 $A$ 是 $n$ 阶方阵，$m_A(\lambda)$ 是其最小多项式，$\chi_A(\lambda)$ 是特征多项式。

## 结论

> 1. $m_A(\lambda) \mid \chi_A(\lambda)$（最小多项式整除特征多项式）。
> 2. $\lambda_0$ 是 $A$ 的特征值 $\iff m_A(\lambda_0) = 0$（两者根相同）。
> 3. $A$ 可对角化 $\iff m_A(\lambda)$ 无重根（即所有根互异）。
> 4. 最小多项式唯一。

## 直觉理解

最小多项式是特征多项式的"精简版"——它只保留对零化必要的最低次信息。可对角化 ⇔ 最小多项式无重根，这说明每个特征值只要有"一个"特征向量就够了。

## 链接

- 前置：[[ALG-THM-041]] Cayley–Hamilton、[[ALG-DEF-039]] 最小多项式
- 用于：[[ALG-THM-043]] Jordan 标准形
