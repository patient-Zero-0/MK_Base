---
title: "相容性判定（系数秩 = 增广秩）"
type: theorem
id: ALG-THM-027
subject: algebra
chapter: 03-linear-equations
tags:
  - 线性方程组
  - 相容性
  - 增广矩阵
depends:
  - ALG-DEF-020
  - ALG-DEF-021
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.4"
difficulty: 2
related: []
corollaries: []
applications:
  - "工程：任何物理系统的可解性等价于约束的相容性检查"
---

## 条件

设 $Ax = b$ 是 $m$ 个方程 $n$ 个未知数的非齐次线性方程组，$(A \mid b)$ 是增广矩阵。

## 结论

> $Ax = b$ 有解 $\iff \operatorname{rank}(A) = \operatorname{rank}(A \mid b)$。
>
> 此时：
>
> - 若 $\operatorname{rank}(A) = n$，则唯一解；
> - 若 $\operatorname{rank}(A) < n$，则无穷多解（自由度 $n - r$）。

## 直觉理解

增广矩阵加了一列 $b$。如果 $b$ 不在 $A$ 的列空间中，相容性就破坏了——增加这一列"撑"大了秩。增广秩 = 原秩 ⇔ $b$ 在列空间中 ⇔ 可解。

## 常见错误

- ✗ 只检查方程数 $m$ 与未知数 $n$ 的关系来判断解的存在性——关键看秩，不是方程个数。

## 链接

- 前置：[[ALG-DEF-020]] 矩阵的秩、[[ALG-DEF-021]] 齐次/非齐次方程组
