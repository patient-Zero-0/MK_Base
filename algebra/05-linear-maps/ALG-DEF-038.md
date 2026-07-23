---
title: "可对角化"
type: definition
id: ALG-DEF-038
subject: algebra
chapter: 05-linear-maps
tags:
  - 可对角化
  - 特征值
depends:
  - ALG-DEF-037
  - ALG-DEF-035
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.4"
difficulty: 3
related: []
applications:
  - "SVD：任何矩阵可通过正交变换对角化（推广到非方阵）"
---

## 定义陈述

$n$ 阶方阵 $A$ 称为**可对角化**（diagonalizable），若 $A$ 相似于某个对角矩阵 $D$，即存在可逆 $P$ 使

$$
P^{-1} A P = D = \operatorname{diag}(\lambda_1, \ldots, \lambda_n).
$$

等价地，线性变换 $\varphi$ 可对角化当且仅当存在一组由特征向量组成的基。

## 直觉理解

可对角化 = 能找到一组基，使变换在这组基下只是一个"伸缩"（对角矩阵）。在这组基下，每个坐标轴方向都是特征方向。

## 链接

- 前置：[[ALG-DEF-037]] 相似矩阵、[[ALG-DEF-035]] 特征值
- 用于：[[ALG-THM-040]] 可对角化充要条件
