---
title: "不同特征值的特征向量线性无关"
type: theorem
id: ALG-THM-039
subject: algebra
chapter: 05-linear-maps
tags:
  - 特征值
  - 特征向量
  - 线性无关
depends:
  - ALG-DEF-035
  - ALG-DEF-018
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.3"
difficulty: 3
related: []
corollaries: []
applications: []
---

## 条件

设 $\lambda_1, \ldots, \lambda_k$ 是线性变换 $\varphi$ 的互异特征值，$v_1, \ldots, v_k$ 是对应的特征向量。

## 结论

> $v_1, \ldots, v_k$ 线性无关。

## 直觉理解

不同特征方向不能互相表示——每个特征向量指向一个独立的"伸缩方向"。$n$ 个不同的特征值 ⇒ 有 $n$ 个线性无关的特征向量 ⇒ 可对角化。

## 证明

设 $a_1 v_1 + \cdots + a_k v_k = 0$。反复作用 $\varphi$ 得线性方程组，由 Vandermonde 行列式非零知系数全为零。$\blacksquare$

## 链接

- 前置：[[ALG-DEF-035]] 特征值、[[ALG-DEF-018]] 线性无关
- 用于：[[ALG-THM-040]] 可对角化
