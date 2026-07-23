---
title: "余子式与代数余子式"
type: definition
id: ALG-DEF-011
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - 余子式
  - 代数余子式
depends:
  - ALG-DEF-010
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.3"
difficulty: 2
related: []
applications: []
---

## 定义陈述

设 $A = (a_{ij})$ 是 $n$ 阶方阵。$A$ 的 $(i, j)$**-余子式**（minor）$M_{ij}$ 定义为**删去第 $i$ 行和第 $j$ 列**后得到的 $(n-1)$ 阶子式的行列式。

$A$ 的 $(i, j)$**-代数余子式**（cofactor）$A_{ij}$ 定义为

$$
A_{ij} = (-1)^{i+j} M_{ij}.
$$

## 直觉理解

余子式 $M_{ij}$ 就是"去掉 $a_{ij}$ 所在的行和列后剩下的小矩阵的行列式"。

代数余子式 $A_{ij}$ 在余子式基础上加了符号 $(-1)^{i+j}$——这个符号由位置 $(i,j)$ 的"棋盘染色"决定：$(-1)^{1+1} = +1$，$(-1)^{1+2} = -1$，$(-1)^{1+3} = +1$，依此类推。

**核心应用**：按行（列）展开公式（[[ALG-THM-011]]）将 $n$ 阶行列式降为 $(n-1)$ 阶行列式的线性组合，是行列式计算的核心递推工具。

## 链接

- 前置：[[ALG-DEF-010]] $n$ 阶行列式
- 用于：[[ALG-THM-011]] 按行（列）展开、[[ALG-DEF-015]] 伴随矩阵
- 推广：[[ALG-DEF-012]] $k$ 阶子式与 Laplace 定理
