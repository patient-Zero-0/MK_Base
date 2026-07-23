---
title: "补空间的存在性"
type: theorem
id: ALG-THM-035
subject: algebra
chapter: 04-linear-spaces
tags:
  - 补空间
  - 子空间
  - 直和
depends:
  - ALG-THM-029
  - ALG-DEF-029
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.5"
difficulty: 4
related: []
corollaries: []
applications:
  - "泛函分析：有限维子空间在任意赋范空间中都有补（无限维不成立）"
---

## 条件

设 $V$ 是有限维线性空间，$W$ 是 $V$ 的子空间。

## 结论

> 存在子空间 $U \subseteq V$ 使 $V = W \oplus U$。称 $U$ 是 $W$ 的**补空间**（complementary subspace）。
>
> 补空间不唯一，但 $\dim U = \dim V - \dim W$ 唯一。

## 证明

取 $W$ 的一组基，扩充为 $V$ 的基。新增的基向量张成的子空间即为一个补空间。$\blacksquare$

## 链接

- 前置：[[ALG-THM-029]] 基扩充定理、[[ALG-DEF-029]] 直和
