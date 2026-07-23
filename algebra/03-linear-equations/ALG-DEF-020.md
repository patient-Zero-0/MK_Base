---
title: "矩阵的秩"
type: definition
id: ALG-DEF-020
subject: algebra
chapter: 03-linear-equations
tags:
  - 矩阵
  - 秩
depends:
  - ALG-DEF-019
  - ALG-DEF-017
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.3"
difficulty: 2
related: []
applications:
  - "机器学习：低秩矩阵分解推荐系统利用秩远低于维度"
---

## 定义陈述

矩阵 $A$ 的**秩**（rank）定义为 $A$ 的行向量组的秩（行秩）或列向量组的秩（列秩）——由 [[ALG-THM-022]] 保证两者相等。

等价定义为 $A$ 通过初等变换化为行阶梯形后，非零行的个数（即主元的个数），记作 $\operatorname{rank}(A)$。

## 直觉理解

矩阵的秩衡量矩阵中"真正独立的行/列数"。秩为 $r$ 的 $m \times n$ 矩阵，其行空间和列空间都是 $r$ 维的。

**几何意义**: 线性变换 $x \mapsto Ax$ 的像空间的维数。

## 常见错误

- ✗ 认为方阵的秩等于行列式非零的阶数——这对，但阶梯形法更通用，适合任意大小矩阵。

## 链接

- 前置：[[ALG-DEF-017]] 阶梯形、[[ALG-DEF-019]] 向量组的秩
- 用于：[[ALG-THM-022]] 行秩 = 列秩、[[ALG-THM-023]] 秩的性质、[[ALG-THM-024]] 齐次方程组
