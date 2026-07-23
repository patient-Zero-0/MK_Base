---
title: "线性变换（线性映射）"
type: definition
id: ALG-DEF-032
subject: algebra
chapter: 05-linear-maps
tags:
  - 线性变换
  - 线性映射
depends:
  - ALG-DEF-023
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.1"
difficulty: 2
related: []
applications:
  - "量子力学：可观测量由自伴算子（一种线性变换）表示"
---

## 定义陈述

设 $V, W$ 是域 $F$ 上的线性空间。映射 $\varphi: V \to W$ 称为**线性映射**（linear map），若满足：

1. **加法保持**：$\varphi(u + v) = \varphi(u) + \varphi(v)$；
2. **数乘保持**：$\varphi(au) = a\varphi(u)$。

当 $V = W$ 时，称 $\varphi$ 为 $V$ 上的**线性变换**（linear transformation）。

记 $\operatorname{Hom}(V, W)$ 为 $V$ 到 $W$ 的所有线性映射的集合，它本身构成线性空间。

## 直觉理解

线性变换 = 保持线性结构的映射。它把直线映成直线（过原点的直线映成过原点的直线），把平行四边形映成平行四边形。

## 例子

- 旋转、缩放、剪切都是 $\mathbb{R}^2$ 上的线性变换
- 求导是 $C^\infty(\mathbb{R})$ 上的线性变换：$(f+g)' = f' + g'$
- 矩阵乘法 $x \mapsto Ax$ 是 $\mathbb{R}^n \to \mathbb{R}^m$ 的线性映射

## 链接

- 前置：[[ALG-DEF-023]] 线性空间
- 用于：[[ALG-DEF-033]] 矩阵表示、[[ALG-DEF-034]] 核与像
