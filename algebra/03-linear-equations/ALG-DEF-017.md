---
title: "阶梯形与行简化阶梯形"
type: definition
id: ALG-DEF-017
subject: algebra
chapter: 03-linear-equations
tags:
  - 矩阵
  - 阶梯形
  - 行简化
depends:
  - ALG-DEF-016
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.2"
difficulty: 2
related: []
applications:
  - "数值计算：行简化阶梯形是求解线性方程组的标准形式"
---

## 定义陈述

**行阶梯形矩阵**（row echelon form）满足：

1. 零行（全零的行）在矩阵底部；
2. 非零行的首个非零元（**主元**，pivot）的列标号随行号严格递增。

**行简化阶梯形**（reduced row echelon form, RREF）进一步要求：
3. 每个主元为 1；
4. 每个主元所在列的其余元素全为 0。

## 直觉理解

阶梯形像楼梯：每往下一行，第一个非零元素向右挪。RREF 则在每个台阶上只留一个 1，其余清零——Gauss-Jordan 消元的结果。

## 常见错误

- ✗ 认为阶梯形是唯一的——事实上只有 RREF 是唯一的，阶梯形可以有多个。

## 链接

- 前置：[[ALG-DEF-016]]
- 用于：[[ALG-THM-019]] Gauss 消元法、[[ALG-DEF-020]] 矩阵的秩
