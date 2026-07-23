---
title: "特征值与特征向量"
type: definition
id: ALG-DEF-035
subject: algebra
chapter: 05-linear-maps
tags:
  - 特征值
  - 特征向量
depends:
  - ALG-DEF-032
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.3"
difficulty: 2
related: []
applications:
  - "数据科学：PCA 将数据投影到协方差矩阵的特征向量方向降维"
  - "量子力学：可观测量本征值 = 测量结果，本征态 = 特征向量"
---

## 定义陈述

设 $\varphi: V \to V$ 是线性变换。若非零向量 $v \in V$ 和标量 $\lambda \in F$ 满足

$$
\varphi(v) = \lambda v,
$$

则称 $\lambda$ 是 $\varphi$ 的**特征值**（eigenvalue），$v$ 是对应于 $\lambda$ 的**特征向量**（eigenvector）。

特征值 $\lambda$ 对应的所有特征向量加上零向量构成子空间，称为**特征子空间**（eigenspace）$E_\lambda = \ker(\varphi - \lambda I)$。

## 直觉理解

特征向量 = 在变换 $\varphi$ 下"方向不变、只被拉伸/压缩"的向量。特征值 = 拉伸倍数。

**几何**：旋转 90° 在 $\mathbb{R}^2$ 上没有实特征向量（因为方向都变了），而伸缩变换 $\varphi(x,y) = (2x, y)$ 有特征值 2（对应 $x$-轴）和 1（对应 $y$-轴）。

## 链接

- 前置：[[ALG-DEF-032]] 线性变换
- 用于：[[ALG-DEF-036]] 特征多项式、[[ALG-THM-039]] 特征向量无关性
