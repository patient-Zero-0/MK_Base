---
title: "行列式的加边法（升阶法）"
type: theorem
id: ALG-THM-018
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - 计算技巧
  - 加边法
depends:
  - ALG-THM-010
  - ALG-THM-011
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.2"
difficulty: 3
related: []
corollaries: []
applications:
  - "某些 n 阶循环行列式和三对角行列式的计算"
---

## 条件

设 $D_n = \det(A)$ 是 $n$ 阶行列式。**加边法**指给 $D_n$ 加一行和一列（称为"边"）构造 $n+1$ 阶行列式，使其值不变但结构更易计算。

## 结论

> 若 $A$ 的每一行都可以表示为某个"基向量"的线性组合，则可构造
>
> $$
> \widetilde D = \det\begin{pmatrix}
> 1 & \alpha^T \\
> \beta & A
> \end{pmatrix}
> $$
>
> 使得 $\widetilde D = D_n$（选择合适的 $\alpha, \beta$），然后利用分块或初等变换求 $\widetilde D$。

## 直觉理解

加边法技巧：给行列式"补一行一列"，将 $\det A$ 嵌入到一个更大的行列式中。选择的 $\alpha$ 和 $\beta$ 使新增行/列与 $A$ 的行/列相消后，新行列式退化为原行列式，但中间步骤可利用新结构的对称性。

## 常见技巧

**常见形式**：若 $A$ 的 $(i,j)$ 元形如 $a_{ij} = u_i v_j$（秩 1 矩阵），可构造

$$
\det\begin{pmatrix}
1 & v_1 & \cdots & v_n \\
-u_1 & & & \\
\vdots & & A & \\
-u_n & & &
\end{pmatrix} = \det A.
$$

## 链接

- 前置：[[ALG-THM-010]] 行列式基本性质、[[ALG-THM-011]] 按一行展开
