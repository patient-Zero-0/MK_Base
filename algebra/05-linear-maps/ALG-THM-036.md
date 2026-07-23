---
title: "线性变换与矩阵一一对应"
type: theorem
id: ALG-THM-036
subject: algebra
chapter: 05-linear-maps
tags:
  - 线性变换
  - 矩阵
  - 对应
depends:
  - ALG-DEF-033
  - ALG-THM-033
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.2"
difficulty: 3
related: []
corollaries: []
applications: []
---

## 条件

设 $V, W$ 是有限维线性空间，$\dim V = n$，$\dim W = m$。

## 结论

> 固定基 $B$（$V$ 的基）和 $B'$（$W$ 的基）后，映射
>
> $$
> \Phi: \operatorname{Hom}(V, W) \to F^{m \times n}, \quad \varphi \mapsto [\varphi]_{B, B'}
> $$
>
> 是线性同构。即：
>
> 1. 每个线性映射对应唯一一个矩阵；
> 2. 每个矩阵对应唯一一个线性映射；
> 3. 映射的复合对应矩阵的乘法。

## 直觉理解

"选基之后，线性变换 = 矩阵"——这是线性代数最核心的思想之一。变换的复合转化为矩阵乘法，坐标变换对应相似变换。

## 链接

- 前置：[[ALG-DEF-033]] 矩阵表示、[[ALG-THM-033]] 同构
- 用于：[[ALG-THM-037]] 秩-零化度定理
