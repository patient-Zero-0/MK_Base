---
title: "齐次 / 非齐次线性方程组与解集"
type: definition
id: ALG-DEF-021
subject: algebra
chapter: 03-linear-equations
tags:
  - 线性方程组
  - 齐次
  - 非齐次
  - 解集
depends:
  - ALG-DEF-016
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.4"
difficulty: 1
related: []
applications:
  - "计算机图形：透视投影中的齐次坐标对应齐次方程组求解"
---

## 定义陈述

**齐次线性方程组**——形如 $Ax = 0$，其中 $A$ 为 $m \times n$ 系数矩阵，$x$ 为 $n \times 1$ 未知列向量。

**非齐次线性方程组**——形如 $Ax = b$，其中 $b \neq 0$。

方程组的**解集**（solution set）是所有满足方程组的 $x$ 的集合。

## 直觉理解

- 齐次：只关心"比例关系"，总有零解 $x=0$，重点是有无非零解。
- 非齐次：关心"具体数值"，可能无解、唯一解或无穷多解。
- 两者的关系：非齐次解 = 一个特解 + 对应齐次通解。

## 链接

- 前置：[[ALG-DEF-016]] 矩阵
- 用于：[[ALG-DEF-022]] 基础解系、[[ALG-THM-024]] 齐次方程组
