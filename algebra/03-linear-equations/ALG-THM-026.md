---
title: "非齐次解的结构（特解 + 齐次通解）"
type: theorem
id: ALG-THM-026
subject: algebra
chapter: 03-linear-equations
tags:
  - 线性方程组
  - 非齐次
  - 解的结构
depends:
  - ALG-THM-025
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.4"
difficulty: 3
related: []
corollaries: []
applications:
  - "微分方程：非齐次线性 ODE 通解 = 特解 + 齐次通解"
---

## 条件

设 $Ax = b$ 是相容（有解）的非齐次线性方程组，$x_0$ 是它的一个特解。

## 结论

> $Ax = b$ 的通解 = $x_0 + \operatorname{Ker}(A)$，即
>
> $$x = x_0 + c_1 \eta_1 + \cdots + c_{n-r} \eta_{n-r},$$
>
> 其中 $\eta_1, \ldots, \eta_{n-r}$ 是 $Ax = 0$ 的基础解系，$c_i$ 为任意常数。

## 直觉理解

非齐次解 = 一个"锚点"（特解）+ 齐次空间里任意游走。整体形状是齐次解空间平移了一个特解。

**几何**：$\mathbb{R}^n$ 中的仿射子空间（不过原点的"平面"）。

## 证明

若 $x_1, x_2$ 都是 $Ax = b$ 的解，则 $A(x_1 - x_2) = b - b = 0$，即差是齐次解。反之，特解加齐次解仍满足原方程。$\blacksquare$

## 链接

- 前置：[[ALG-THM-025]] 齐次解空间维数
- 用于：[[ALG-THM-027]] 相容性判定
