---
title: "特征多项式"
type: definition
id: ALG-DEF-036
subject: algebra
chapter: 05-linear-maps
tags:
  - 特征多项式
  - 特征值
depends:
  - ALG-DEF-035
  - ALG-DEF-010
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.3"
difficulty: 2
related: []
applications:
  - "动力系统：特征多项式根的位置决定系统稳定性"
---

## 定义陈述

设 $A$ 是 $n$ 阶方阵。$A$ 的**特征多项式**（characteristic polynomial）定义为

$$
\chi_A(\lambda) = \det(\lambda I - A).
$$

若 $\varphi$ 是 $V$ 上的线性变换，任选一组基 $B$，则 $\varphi$ 的特征多项式为 $\chi_\varphi(\lambda) = \det(\lambda I - [\varphi]_B)$。特征多项式与基的选取无关。

特征值 = 特征多项式的根（在代数闭包中）。

## 直觉理解

特征多项式将"求特征值"转化为"求多项式根"——解 $\det(\lambda I - A) = 0$。这是一个 $n$ 次多项式，其根（含重根）正好是所有特征值。

## 常见错误

- ✗ 混淆 $\det(\lambda I - A)$ 和 $\det(A - \lambda I)$——两者差 $(-1)^n$，在偶阶时符号一致，奇阶时互为相反数。

## 链接

- 前置：[[ALG-DEF-035]] 特征值、[[ALG-DEF-010]] 行列式
- 用于：[[ALG-THM-041]] Cayley–Hamilton 定理
