---
title: "对称多项式化初等对称多项式"
type: problem
id: ALG-PROB-004
subject: algebra
chapter: 01-polynomials
tags:
  - 多项式
  - 对称多项式
  - 初等对称多项式
depends:
  - ALG-DEF-008
uses: []
status: draft
source: "丘维声《高等代数》第3版 §1.5 习题"
difficulty: 4
tests:
  - ALG-DEF-008
related: []
---

## 题目

将下列对称多项式表示为初等对称多项式 $\sigma_1, \sigma_2, \ldots$ 的多项式（$n=3$ 个变量 $x_1, x_2, x_3$）：

1. $F_1 = x_1^2 + x_2^2 + x_3^2$
2. $F_2 = x_1^2 x_2 + x_1 x_2^2 + x_1^2 x_3 + x_1 x_3^2 + x_2^2 x_3 + x_2 x_3^2$
3. $F_3 = (x_1 - x_2)^2 (x_2 - x_3)^2 (x_3 - x_1)^2$（三项式的判别式）

## 提示

<details><summary>点击展开提示</summary>

- $\sigma_1 = x_1 + x_2 + x_3$
- $\sigma_2 = x_1 x_2 + x_1 x_3 + x_2 x_3$
- $\sigma_3 = x_1 x_2 x_3$

第 1 题：利用恒等式 $(x_1+x_2+x_3)^2 = x_1^2+x_2^2+x_3^2 + 2(x_1x_2+x_1x_3+x_2x_3)$。

第 2 题：注意 $\sigma_1 \sigma_2 = (x_1+x_2+x_3)(x_1x_2+x_1x_3+x_2x_3)$ 展开后的项含有 $F_2$。

第 3 题：判别式 $\Delta$ 是 $n=3$ 时最重要的对称多项式之一，与 $\sigma_1, \sigma_2, \sigma_3$ 的关系可通过计算三次方程的判别式得到。结果应为 $\Delta = \sigma_1^2 \sigma_2^2 - 4\sigma_2^3 - 4\sigma_1^3 \sigma_3 - 27\sigma_3^2 + 18\sigma_1\sigma_2\sigma_3$。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题

展开 $(\sigma_1)^2$：

$$
\sigma_1^2 = (x_1+x_2+x_3)^2 = x_1^2+x_2^2+x_3^2 + 2(x_1x_2+x_1x_3+x_2x_3) = F_1 + 2\sigma_2.
$$

故

$$
F_1 = \sigma_1^2 - 2\sigma_2.
$$

### 第 2 题

计算 $\sigma_1 \sigma_2$：

$$
\begin{aligned}
\sigma_1 \sigma_2 &= (x_1+x_2+x_3)(x_1x_2+x_1x_3+x_2x_3) \\
&= (x_1^2 x_2 + x_1^2 x_3 + x_1 x_2 x_3) + (x_1 x_2^2 + x_1 x_2 x_3 + x_2^2 x_3) + (x_1 x_2 x_3 + x_1 x_3^2 + x_2 x_3^2) \\
&= F_2 + 3 x_1 x_2 x_3 = F_2 + 3\sigma_3.
\end{aligned}
$$

故

$$
F_2 = \sigma_1 \sigma_2 - 3\sigma_3.
$$

### 第 3 题

三次多项式 $x^3 + a x^2 + b x + c = (x-x_1)(x-x_2)(x-x_3)$ 的判别式为

$$
\Delta = a^2 b^2 - 4b^3 - 4a^3 c - 27c^2 + 18abc.
$$

由 Vieta 公式，$a = -\sigma_1$，$b = \sigma_2$，$c = -\sigma_3$（注意符号）。代入并化简：

$$
\Delta = \sigma_1^2 \sigma_2^2 - 4\sigma_2^3 - 4\sigma_1^3 \sigma_3 - 27\sigma_3^2 + 18\sigma_1\sigma_2\sigma_3.
$$

这是关于 $\sigma_1, \sigma_2, \sigma_3$ 的一个 4 次齐次对称多项式。

</details>

## 考察点

- [[ALG-DEF-008]] 初等对称多项式与对称多项式基本定理
- Vieta 公式与三次方程判别式的关系
