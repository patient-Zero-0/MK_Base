---
title: "初等变换对行列式的影响"
type: theorem
id: ALG-THM-012
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - 初等变换
depends:
  - ALG-THM-010
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.2"
difficulty: 2
related: []
corollaries: []
applications: []
---

## 条件

设 $A$ 是 $n$ 阶方阵。对 $A$ 施行三种初等行变换。

## 结论

| 初等变换 | 行列式的变化 |
|---|---|
| 交换两行 | $\det \to -\det$ |
| 某行乘以非零常数 $k$ | $\det \to k\cdot \det$ |
| 某行的 $k$ 倍加到另一行 | $\det$ **不变** |

列变换同样适用（由转置不变性）。

## 直觉理解

这三种变换的效果加上三角化，给出了计算行列式的**实用算法**：

1. 用行变换（类型 3）将矩阵化为上三角；
2. 记录类型 1 的次数（每次 $-1$）和类型 2 的因子；
3. 上三角行列式 = 对角元乘积。

## 链接

- 前置：[[ALG-THM-010]] 行列式基本性质
- 用于：[[ALG-THM-013]] Vandermonde 行列式求值
