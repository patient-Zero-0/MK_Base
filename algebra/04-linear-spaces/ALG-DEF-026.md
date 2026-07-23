---
title: "基与维数"
type: definition
id: ALG-DEF-026
subject: algebra
chapter: 04-linear-spaces
tags:
  - 基
  - 维数
  - 线性空间
depends:
  - ALG-DEF-025
  - ALG-DEF-018
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.3"
difficulty: 2
related: []
applications:
  - "数据科学：PCA 中的主成分方向构成数据空间的基"
---

## 定义陈述

设 $V$ 是 $F$ 上的线性空间，$B = \{v_1, \ldots, v_n\} \subseteq V$ 是有限个向量。

若 $B$ 同时满足：

1. **线性无关**；
2. **张成** $V$，即 $\operatorname{span}(B) = V$，

则称 $B$ 是 $V$ 的一组**基**（basis）。基中向量的个数 $n$ 称为 $V$ 的**维数**（dimension），记作 $\dim_F V$ 或简写为 $\dim V$。

若 $V$ 没有有限基，则称为**无限维**线性空间。

## 直觉理解

基 = "最小生成集" = "最大无关组"。基里的每个向量都提供了新的方向（无关），且足够覆盖整个空间（张成）。

**例子**：$\mathbb{R}^n$ 的标准基 $e_1 = (1,0,\ldots,0), \ldots, e_n = (0,\ldots,0,1)$，$\dim \mathbb{R}^n = n$。

## 链接

- 前置：[[ALG-DEF-025]] 张成、[[ALG-DEF-018]] 线性无关
- 用于：[[ALG-DEF-027]] 向量的坐标、[[ALG-THM-028]] 基的存在性
