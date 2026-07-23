---
title: "向量组的秩与极大线性无关组"
type: definition
id: ALG-DEF-019
subject: algebra
chapter: 03-linear-equations
tags:
  - 向量组
  - 秩
  - 极大无关组
depends:
  - ALG-DEF-018
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.3"
difficulty: 3
related: []
applications:
  - "数据科学：主成分分析中主成分数量 = 数据向量组的秩"
---

## 定义陈述

设 $\alpha_1, \ldots, \alpha_s \in V$ 是一组向量。若其中某 $r$ 个向量

1. 线性无关；
2. 任意一个向量均可由这 $r$ 个向量线性表示。

则这 $r$ 个向量称为**极大线性无关组**（maximal linearly independent subset）。

向量组的**秩**（rank）就是极大线性无关组中向量的个数，记作 $\operatorname{rank}(\alpha_1, \ldots, \alpha_s)$。

## 直觉理解

极大无关组是向量组的"骨干"——去掉它们就丢了信息，但加上任何其他向量就会产生冗余（相关）。所有极大无关组的向量个数相同，这个数就是秩。

**类比**：一个团队里的"核心成员"——缺了他们团队做不了事，但加上其他人只是锦上添花。

## 常见错误

- ✗ 认为极大无关组唯一——实际上可以有多个不同的极大无关组，但它们的向量个数相同。

## 链接

- 前置：[[ALG-DEF-018]] 线性相关与无关
- 用于：[[ALG-DEF-020]] 矩阵的秩、[[ALG-THM-021]] 替换定理
