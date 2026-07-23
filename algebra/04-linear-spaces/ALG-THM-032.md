---
title: "坐标变换公式"
type: theorem
id: ALG-THM-032
subject: algebra
chapter: 04-linear-spaces
tags:
  - 坐标变换
  - 过渡矩阵
depends:
  - ALG-DEF-028
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.4"
difficulty: 3
related: []
corollaries: []
applications:
  - "计算机图形：视图矩阵 = 从世界坐标系到相机坐标系的过渡矩阵"
---

## 条件

设 $B, B'$ 是 $V$ 的两组基，$P$ 是从 $B$ 到 $B'$ 的过渡矩阵。

## 结论

> 对任意 $v \in V$，有
>
> $$[v]_B = P [v]_{B'}, \qquad [v]_{B'} = P^{-1} [v]_B.$$
>
> 若 $\varphi: V \to V$ 是线性变换，其在 $B$ 下的矩阵为 $A$，在 $B'$ 下的矩阵为 $A'$，则
>
> $$A' = P^{-1} A P.$$

## 直觉理解

坐标变换分两层：向量的坐标用 $P$ 换基，线性变换的矩阵用 $P^{-1}AP$ 换基（相似变换）。

## 链接

- 前置：[[ALG-DEF-028]] 基变换与过渡矩阵
- 用于：[[ALG-THM-036]] 线性变换与矩阵
