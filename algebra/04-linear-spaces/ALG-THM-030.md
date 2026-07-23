---
title: "维数公式（子空间的和）"
type: theorem
id: ALG-THM-030
subject: algebra
chapter: 04-linear-spaces
tags:
  - 维数
  - 子空间
  - 和
depends:
  - ALG-DEF-029
  - ALG-THM-029
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.5"
difficulty: 3
related: []
applications:
  - "微分方程：解空间维数的加减关系由维数公式控制"
---

## 条件

设 $V$ 是有限维线性空间，$U, W$ 是 $V$ 的子空间。

## 结论

> $$
> \dim(U + W) = \dim U + \dim W - \dim(U \cap W).
> $$

## 直觉理解

两个子空间之和的维数 = 各自维数之和减去重叠部分。重叠部分被重复计算了——这是集合论的容斥原理在线性空间中的体现。

## 证明

取 $U \cap W$ 的一组基，分别扩充为 $U$ 和 $W$ 的基。将这些基向量合并后验证线性无关且张成 $U+W$，即可数出维数。$\blacksquare$

## 链接

- 前置：[[ALG-DEF-029]] 子空间的和、[[ALG-THM-029]] 基扩充定理
- 用于：[[ALG-THM-031]] 直和判定
