---
title: "伴随矩阵与逆矩阵"
type: problem
id: ALG-PROB-006
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - 伴随矩阵
  - 逆矩阵
depends:
  - ALG-DEF-015
  - ALG-THM-017
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.4"
difficulty: 3
related: []
tests:
  - ALG-DEF-015
  - ALG-THM-017
prerequisites:
  - "伴随矩阵定义"
  - "矩阵可逆性"
---

## 题目

1. 证明：若 $A$ 是 $n$ 阶可逆矩阵（$n \geq 2$），则 $(A^*)^{-1} = (A^{-1})^* = \frac{1}{\det A} A$。

2. 证明：$\operatorname{rank}(A^*) = \begin{cases}
n, & \operatorname{rank}(A) = n, \\
1, & \operatorname{rank}(A) = n-1, \\
0, & \operatorname{rank}(A) \leq n-2.
\end{cases}$

3. 已知 $A$ 是 $3$ 阶方阵且 $|A| = 2$，求 $|(2A)^{-1} - A^*|$。

## 提示

1. 利用 $AA^* = (\det A)I$，对两边取逆或转置。
2. 分情况讨论 $\det A \neq 0$、$\operatorname{rank}(A) = n-1$、$\operatorname{rank}(A) \leq n-2$。
3. 用 $A^* = |A|A^{-1}$ 化简表达式，再求行列式。
