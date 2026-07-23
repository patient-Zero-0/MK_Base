---
title: "Cramer 法则"
type: theorem
id: ALG-THM-016
subject: algebra
chapter: 02-determinants
tags:
  - 线性方程组
  - Cramer法则
depends:
  - ALG-THM-011
  - ALG-DEF-015
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.4"
difficulty: 3
related: []
corollaries: []
applications:
  - "理论上给出唯一解的行列式表达式，用于公式推导和理论分析"
---

## 条件

设 $Ax = b$ 是 $n$ 元 $n$ 个方程的线性方程组，系数矩阵 $A$ 可逆（$\det A \neq 0$）。

## 结论

> 方程组有唯一解，且解的第 $j$ 个分量为
>
> $$
> x_j = \frac{\det A_j}{\det A},
> $$
>
> 其中 $A_j$ 是将 $A$ 的第 $j$ 列替换为常数列 $b$ 所得的矩阵。

## 直觉理解

将解的第 $j$ 分量视为"将系数矩阵第 $j$ 列替换为 $b$ 后体积变化之比"——这等价于消元法中第 $j$ 个未知数的系数被 $b$ 取代。

## 证明

由 $A$ 可逆知 $x = A^{-1}b$。利用 $A^{-1} = A^*/\det A$：

$$
x_j = \frac{\sum_{k=1}^n A_{kj} b_k}{\det A}
= \frac{\det A_j}{\det A}.
$$

最后一个等式按第 $j$ 列展开 $\det A_j$ 即得。$\blacksquare$

## 常见错误

- ✗ 直接用 Cramer 法则做数值计算——$n$ 较大时计算量 $O(n!)$，远不如高斯消元 $O(n^3)$。
- ✗ 忘记分母 $\det A$，只会用 $\det A_j$ 当解。

## 链接

- 前置：[[ALG-THM-011]] 按一行展开、[[ALG-DEF-015]] 伴随矩阵
- 用于：[[ALG-THM-017]] 矩阵可逆的充要条件
