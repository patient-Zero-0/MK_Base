---
title: "基础解系"
type: definition
id: ALG-DEF-022
subject: algebra
chapter: 03-linear-equations
tags:
  - 线性方程组
  - 基础解系
  - 解空间
depends:
  - ALG-DEF-021
  - ALG-DEF-019
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.4"
difficulty: 3
related: []
applications: []
---

## 定义陈述

设 $Ax = 0$ 是 $m \times n$ 齐次线性方程组，其解集构成 $\mathbb{R}^n$ 的一个子空间，称为**解空间**（null space / kernel）。

解空间的**基础解系**（fundamental system of solutions）是解空间的一组基——即一组线性无关的解向量 $\eta_1, \ldots, \eta_t$，使得每个解都可唯一表示为它们的线性组合。

## 直觉理解

基础解系 = 解空间的"骨架"。找到基础解系 = 完全描述所有解。如果 $\operatorname{rank}(A) = r$，则解空间维数 $= n - r$，基础解系包含 $n-r$ 个向量。

## 链接

- 前置：[[ALG-DEF-021]] 齐次方程组、[[ALG-DEF-019]] 极大无关组
- 用于：[[ALG-THM-025]] 齐次解空间维数
