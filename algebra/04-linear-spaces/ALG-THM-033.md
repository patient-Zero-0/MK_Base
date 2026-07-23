---
title: "有限维线性空间同构 ⇔ 维数相等"
type: theorem
id: ALG-THM-033
subject: algebra
chapter: 04-linear-spaces
tags:
  - 同构
  - 维数
  - 有限维
depends:
  - ALG-DEF-030
  - ALG-THM-028
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.6"
difficulty: 3
related: []
corollaries: []
applications:
  - '任何 $n$ 维实线性空间都同构于 $\mathbb{R}^n$——维数是有限维空间的唯一不变量'
---

## 条件

设 $V, W$ 是域 $F$ 上的有限维线性空间。

## 结论

> $V \cong W \iff \dim V = \dim W$。
>
> 特别地，任何 $n$ 维 $F$-线性空间都同构于 $F^n$。

## 直觉理解

有限维线性空间"本质上就是 $F^n$"——选一组基，坐标映射 $\varphi(v) = [v]_B$ 就是到 $F^n$ 的同构。维数相同的两个空间通过"都同构于同一个 $F^n$"而互相同构。

## 证明

($\Rightarrow$) 同构保持基的个数，所以维数相等。
($\Leftarrow$) 取 $V$ 的基 $B$，$W$ 的基 $B'$，定义 $\varphi(v) = [v]_B \mapsto [v]_B$ 在 $B'$ 下的线性组合，易验证为同构。$\blacksquare$

## 链接

- 前置：[[ALG-DEF-030]] 同构、[[ALG-THM-028]] 基
