---
title: "Jordan 标准形的存在与唯一"
type: theorem
id: ALG-THM-043
subject: algebra
chapter: 05-linear-maps
tags:
  - Jordan标准形
  - 存在性
depends:
  - ALG-DEF-039
  - ALG-THM-042
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.6"
difficulty: 5
related: []
corollaries: []
applications:
  - "微分方程：$e^{At}$ 的显式表达式可通过 Jordan 标准形求得"
---

## 条件

设 $A$ 是 $n$ 阶复方阵（或 $\chi_A(\lambda)$ 在 $F$ 上可分解为一次因式之积）。

## 结论

> $A$ 相似于唯一的 Jordan 标准形 $J$（不计 Jordan 块排列次序）：
>
> $$
> J = \operatorname{diag}(J_1, J_2, \ldots, J_k),
> $$
>
> 其中每个 $J_i$ 是 Jordan 块 $J(\lambda_i) = \begin{pmatrix} \lambda_i & 1 & & \\ & \lambda_i & \ddots & \\ & & \ddots & 1 \\ & & & \lambda_i \end{pmatrix}$。
>
> 特征值 $\lambda_i$ 的 Jordan 块的个数 = $\dim \ker(A - \lambda_i I)$（几何重数），
> 总大小 = 代数重数。

## 直觉理解

Jordan 标准形是"最佳近似对角化"——特征向量不够时，用"广义特征向量"（链式）填补。每个 Jordan 块对应一条 eigen-chain。Jordan 标准形唯一确定变换的全部结构信息。

## 链接

- 前置：[[ALG-DEF-039]] Jordan 标准形、[[ALG-THM-042]] 最小多项式
