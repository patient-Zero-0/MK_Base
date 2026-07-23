---
title: "实对称矩阵正交对角化（谱定理）"
type: theorem
id: ALG-THM-044
subject: algebra
chapter: 05-linear-maps
tags:
  - 实对称矩阵
  - 正交对角化
  - 谱定理
depends:
  - ALG-THM-040
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.4"
difficulty: 4
related: []
corollaries: []
applications:
  - "数据科学：PCA = 协方差矩阵（实对称）正交对角化"
  - "量子力学：自伴算子的谱定理保证实特征值和正交本征态"
---

## 条件

设 $A$ 是 $n$ 阶实对称矩阵（$A^\top = A$）。

## 结论

> 存在正交矩阵 $Q$（$Q^\top Q = I$）和对角矩阵 $D$，使
>
> $$
> Q^\top A Q = D = \operatorname{diag}(\lambda_1, \ldots, \lambda_n),
> $$
>
> 其中 $\lambda_i$ 全是实数，$Q$ 的列是相互正交的单位特征向量。
>
> 即：实对称矩阵可被正交矩阵对角化为实对角矩阵。

## 直觉理解

实对称矩阵的好性质：特征值全是实数，不同特征值的特征向量自动正交，总有一组正交的单位特征向量基。这是线性代数中最优美也最实用的结果之一——SVD、PCA、谱聚类都源于此。

## 链接

- 前置：[[ALG-THM-040]] 可对角化充要条件
- 跨课：[[CROSS-003]] 二次型与极值
