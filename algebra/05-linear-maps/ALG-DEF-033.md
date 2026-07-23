---
title: "线性变换的矩阵表示"
type: definition
id: ALG-DEF-033
subject: algebra
chapter: 05-linear-maps
tags:
  - 线性变换
  - 矩阵表示
depends:
  - ALG-DEF-032
  - ALG-DEF-028
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.2"
difficulty: 3
related: []
applications:
  - "计算机图形：所有 3D 变换（旋转/缩放/平移的齐次坐标）均由矩阵表示"
---

## 定义陈述

设 $\varphi: V \to W$ 是线性映射，$B = \{v_1, \ldots, v_n\}$ 是 $V$ 的基，$B' = \{w_1, \ldots, w_m\}$ 是 $W$ 的基。

$\varphi$ 在基对 $(B, B')$ 下的矩阵 $A \in F^{m \times n}$ 定义为：$A$ 的第 $j$ 列是 $\varphi(v_j)$ 在 $B'$ 下的坐标。

即若 $\varphi(v_j) = \sum_{i=1}^m a_{ij} w_i$，则 $A = (a_{ij})$。

对任意 $v \in V$，有坐标关系：

$$
[\varphi(v)]_{B'} = A [v]_B.
$$

## 直觉理解

矩阵就是线性变换的"坐标版本"——选好基后，变换完全由矩阵描述。矩阵的列是基向量像的坐标。

## 链接

- 前置：[[ALG-DEF-032]] 线性变换、[[ALG-DEF-028]] 基变换
- 用于：[[ALG-THM-036]] 线性变换与矩阵一一对应
