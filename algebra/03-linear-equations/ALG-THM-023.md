---
title: "秩的性质"
type: theorem
id: ALG-THM-023
subject: algebra
chapter: 03-linear-equations
tags:
  - 矩阵
  - 秩
  - 性质
depends:
  - ALG-THM-022
  - ALG-DEF-020
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.3"
difficulty: 3
related: []
corollaries: []
applications:
  - "数值线性代数：秩不等式用于分析算法稳定性"
---

## 条件

设 $A, B$ 是适当阶数的矩阵。

## 结论

> 1. **初等变换不改变秩**：若 $A \xrightarrow{\text{行变换}} B$，则 $\operatorname{rank}(A) = \operatorname{rank}(B)$。
> 2. **秩的乘法不等式**：$\operatorname{rank}(AB) \leq \min\{\operatorname{rank}(A), \operatorname{rank}(B)\}$。
> 3. **Sylvester 秩不等式**：$\operatorname{rank}(A) + \operatorname{rank}(B) - n \leq \operatorname{rank}(AB) \leq \operatorname{rank}(A) + \operatorname{rank}(B)$。
> 4. **Frobenius 秩不等式**：$\operatorname{rank}(AB) + \operatorname{rank}(BC) \leq \operatorname{rank}(B) + \operatorname{rank}(ABC)$。
> 5. **$k$ 阶子式刻画**：$\operatorname{rank}(A) \geq r \iff A$ 存在非零的 $r$ 阶子式，且所有 $r+1$ 阶子式为零。

## 直觉理解

秩衡量"信息维度"：矩阵乘法会丢失信息（维度只减不增），不等式给出了丢失的上界。

## 链接

- 前置：[[ALG-THM-022]] 行秩 = 列秩
- 用于：[[ALG-THM-024]] 齐次方程组
