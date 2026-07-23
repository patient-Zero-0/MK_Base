---
title: "含参数方程组分类讨论"
type: problem
id: ALG-PROB-011
subject: algebra
chapter: 03-linear-equations
tags:
  - 线性方程组
  - 含参数
  - 分类讨论
depends:
  - ALG-THM-027
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.4"
difficulty: 4
related: []
tests:
  - ALG-THM-027
prerequisites:
  - "相容性判定"
  - "秩不等式"
---

## 题目

讨论 $\lambda$ 取何值时方程组有唯一解、无解、无穷多解：

$$
\begin{cases}
\lambda x + y + z = 1, \\
x + \lambda y + z = \lambda, \\
x + y + \lambda z = \lambda^2.
\end{cases}
$$

## 提示

系数矩阵 $A$ 的行列式 $\det A = (\lambda + 2)(\lambda - 1)^2$。分 $\lambda \neq 1, -2$、$\lambda = 1$、$\lambda = -2$ 三种情况讨论增广矩阵的秩。
