---
title: "基的存在性与维数的唯一性"
type: theorem
id: ALG-THM-028
subject: algebra
chapter: 04-linear-spaces
tags:
  - 基
  - 维数
  - 存在性
depends:
  - ALG-DEF-026
  - ALG-THM-021
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.3"
difficulty: 3
related: []
corollaries: []
applications: []
---

## 条件

设 $V$ 是有限维线性空间（存在有限生成集）。

## 结论

> 1. **基的存在性**：$V$ 存在一组基。
> 2. **维数的唯一性**：$V$ 的任意两组基所含向量个数相同，因此 $\dim V$ 是良定义的。
> 3. **基扩充**：任意线性无关的向量组可扩充为一组基。

## 直觉理解

有限维空间总有一个"最小生成集"——它就是基。不管你怎么选基，个数都一样，这就是空间的"维度"。

## 证明思路

从有限生成集中逐步剔除"冗余"向量（可由其它线性表示），最后留下的就是基。唯一性由替换定理（[[ALG-THM-021]]）保证。$\blacksquare$

## 链接

- 前置：[[ALG-DEF-026]] 基与维数、[[ALG-THM-021]] 替换定理
- 用于：[[ALG-THM-029]] 基扩充定理
