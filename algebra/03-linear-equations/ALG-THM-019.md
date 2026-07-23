---
title: "Gauss 消元法"
type: theorem
id: ALG-THM-019
subject: algebra
chapter: 03-linear-equations
tags:
  - 线性方程组
  - Gauss消元
depends:
  - ALG-DEF-017
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.1"
difficulty: 2
related: []
corollaries: []
applications:
  - "数值计算：Gauss 消元是所有直接法求解线性方程组的基础（$O(n^3)$）"
---

## 条件

对任意 $m \times n$ 矩阵 $A$。

## 结论

> 通过有限次初等行变换，总可以将 $A$ 化为行阶梯形。继续变换则可化为**行简化阶梯形（RREF）**，且 RREF 唯一。

## 直觉理解

Gauss 消元就是"从左上到右下，逐列清零"的过程：

1. 找主元（当前列第一个非零位置）；
2. 若没有非零元素则跳到下一列；
3. 将主元行换到当前位置；
4. 用主元将下方所有元素消为零。

## 算法简述

```text
For 列 j = 1..n:
    在行 i..m 中找 a_{ij} ≠ 0
    若找到则交换到第 i 行，用 a_{ij} 消去下方元素，i++
```

## 链接

- 前置：[[ALG-DEF-017]] 阶梯形
- 用于：[[ALG-THM-024]] 齐次方程组解的存在性
