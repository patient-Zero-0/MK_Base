---
title: "相似矩阵"
type: definition
id: ALG-DEF-037
subject: algebra
chapter: 05-linear-maps
tags:
  - 相似矩阵
  - 相似变换
depends:
  - ALG-DEF-033
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.3"
difficulty: 2
related: []
applications: []
---

## 定义陈述

设 $A, B$ 是 $n$ 阶方阵。若存在可逆矩阵 $P$ 使

$$
B = P^{-1} A P,
$$

则称 $A$ 与 $B$ **相似**（similar），记作 $A \sim B$。

相似关系是等价关系（自反、对称、传递）。相似矩阵视为同一线性变换在不同基下的矩阵。

## 直觉理解

相似 = "换基之后同一个变换"。矩阵的实质是线性变换在特定基下的"快照"，换基后快照变了，但变换本身没变。

## 链接

- 前置：[[ALG-DEF-033]] 矩阵表示
- 用于：[[ALG-THM-038]] 相似不变量、[[ALG-DEF-038]] 可对角化
