---
title: "秩不等式证明"
type: problem
id: ALG-PROB-012
subject: algebra
chapter: 03-linear-equations
tags:
  - 秩
  - 不等式
  - 证明
depends:
  - ALG-THM-023
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.3"
difficulty: 5
related: []
tests:
  - ALG-THM-023
prerequisites:
  - "Sylvester不等式"
  - "Frobenius不等式"
---

## 题目

设 $A$ 是 $m \times n$ 矩阵，$B$ 是 $n \times p$ 矩阵，$C$ 是 $p \times q$ 矩阵。

1. 证明 Sylvester 秩不等式：$\operatorname{rank}(A) + \operatorname{rank}(B) - n \leq \operatorname{rank}(AB)$。
2. 证明 Frobenius 秩不等式：$\operatorname{rank}(AB) + \operatorname{rank}(BC) \leq \operatorname{rank}(B) + \operatorname{rank}(ABC)$。

## 提示

1. 考虑分块矩阵 $\begin{pmatrix} A & 0 \\ I & B \end{pmatrix}$ 的秩，通过初等变换得到 $\begin{pmatrix} 0 & -AB \\ I & B \end{pmatrix}$。
2. 对分块阵 $\begin{pmatrix} ABC & 0 \\ 0 & B \end{pmatrix}$ 做初等变换；或用线性映射的维数公式。
