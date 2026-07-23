---
title: "行秩 = 列秩 = 矩阵秩"
type: theorem
id: ALG-THM-022
subject: algebra
chapter: 03-linear-equations
tags:
  - 矩阵
  - 秩
  - 行秩
  - 列秩
depends:
  - ALG-THM-021
  - ALG-DEF-020
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.3"
difficulty: 3
related: []
corollaries: []
applications:
  - "数据科学：矩阵的低秩逼近基于行秩=列秩，SVD 截断最优"
---

## 条件

设 $A$ 是 $m \times n$ 矩阵。

## 结论

> $A$ 的行向量组的秩（**行秩**）等于列向量组的秩（**列秩**），统称为**矩阵的秩** $\operatorname{rank}(A)$。

## 直觉理解

为什么行数可以和列数相等？核心在于初等变换不改变行秩和列秩——阶梯形中非零行数 = 主元个数 = 列秩（主元所在的列线性无关）。

**几何**：线性变换 $x \mapsto Ax$ 的像空间维数（列秩）等于"有效行数"（行秩），因为它们描述的是同一个线性映射的秩。

## 证明思路

设 $\operatorname{rank}_{\text{row}}(A) = r$，取行向量组的极大无关组构成 $r \times n$ 矩阵 $B$。则 $A$ 的每行是 $B$ 的行的线性组合 ⇒ $A = CB$。由 D 的列秩 ≤ $r$，进而可得列秩 ≤ 行秩。对称地得行秩 ≤ 列秩。$\blacksquare$

## 链接

- 前置：[[ALG-THM-021]] 替换定理、[[ALG-DEF-020]] 矩阵的秩
- 用于：[[ALG-THM-023]] 秩的性质
