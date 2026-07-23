---
title: "线性组合与张成（生成子空间）"
type: definition
id: ALG-DEF-025
subject: algebra
chapter: 04-linear-spaces
tags:
  - 线性组合
  - 张成
  - 生成子空间
depends:
  - ALG-DEF-024
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.2"
difficulty: 2
related: []
applications:
  - "机器学习：核方法中特征空间的张成决定了模型的表达能力"
---

## 定义陈述

设 $V$ 是 $F$ 上的线性空间，$S = \{v_1, \ldots, v_s\} \subseteq V$。$S$ 的**线性组合**（linear combination）指形式为

$$
a_1 v_1 + \cdots + a_s v_s, \quad a_i \in F
$$

的向量。$S$ 的**张成**（span）是所有线性组合的集合：

$$
\operatorname{span}(S) = \left\{\sum_{i=1}^s a_i v_i \,\middle|\, a_i \in F\right\}.
$$

$\operatorname{span}(S)$ 是 $V$ 的子空间，称为 $S$ 的**生成子空间**（或线性包）。

## 直觉理解

张成 = 把 $S$ 里的向量"尽情组合"能得到的所有可能的向量。如果 $S$ 张成了整个 $V$，就说 $S$ 是 $V$ 的生成集。

## 常见错误

- ✗ 认为 $\operatorname{span}(S)$ 中的向量必须包含 $S$ 本身——它包含所有线性组合，但 $S$ 只是"原料"。

## 链接

- 前置：[[ALG-DEF-024]] 子空间
- 用于：[[ALG-DEF-026]] 基与维数
