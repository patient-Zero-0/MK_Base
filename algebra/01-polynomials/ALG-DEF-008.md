---
title: "对称多项式与初等对称多项式"
type: definition
id: ALG-DEF-008
subject: algebra
chapter: 01-polynomials
tags:
  - 多项式
  - 对称多项式
  - 初等对称多项式
depends:
  - ALG-DEF-001
uses: []
status: draft
source: "丘维声《高等代数》第3版 §1.5"
difficulty: 3
related:
  - ALG-THM-002
applications:
  - "代数几何：对称多项式与代数簇的对称性描述"
  - "科学计算：由根的多项式计算系数（Vieta 公式反用）"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述

### 多元对称多项式

设 $f(x_1, x_2, \ldots, x_n) \in K[x_1, \ldots, x_n]$ 是 $n$ 元多项式。称 $f$ 是**对称多项式**，若对任意排列 $\sigma \in S_n$，

$$
f(x_{\sigma(1)}, x_{\sigma(2)}, \ldots, x_{\sigma(n)}) = f(x_1, x_2, \ldots, x_n).
$$

即 $f$ 在任意置换变量下保持不变。

### 初等对称多项式

$n$ 个变量上的**初等对称多项式**（elementary symmetric polynomials）定义为

$$
\begin{aligned}
\sigma_1 &= x_1 + x_2 + \cdots + x_n = \sum_{1 \leq i \leq n} x_i,\\[2pt]
\sigma_2 &= \sum_{1 \leq i < j \leq n} x_i x_j,\\[2pt]
\sigma_3 &= \sum_{1 \leq i < j < k \leq n} x_i x_j x_k,\\
&\ \; \vdots\\
\sigma_n &= x_1 x_2 \cdots x_n.
\end{aligned}
$$

更紧凑地：$\sigma_k$ 是所有 $k$ 个不同变量的乘积之和（共 $\binom{n}{k}$ 项）。

### 基本定理（陈述）

> **对称多项式基本定理**：$K[x_1, \ldots, x_n]$ 中**每一个**对称多项式都可以**唯一**地表示为初等对称多项式 $\sigma_1, \ldots, \sigma_n$ 的多项式。

换句话说，对称多项式环 $K[x_1, \ldots, x_n]^{S_n}$ 同构于 $K[\sigma_1, \ldots, \sigma_n]$。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 任意多项式 | 在变量置换下变化 |
| 对称多项式 | 在 $S_n$ 的所有置换下不变 |
| 初等对称多项式 $\sigma_k$ | 对称多项式的"生成元"——全部对称多项式由它们代数生成 |
| 齐次对称多项式 | 各单项式总次数相同的对称多项式（$\sigma_k$ 正是 $k$ 次齐次） |

## 直觉理解

**对称多项式** = "不管你怎么打乱变量名，表达式都一模一样"。

例如 $x^2 + y^2$ 是对称的（交换 $x$ 与 $y$ 得 $y^2 + x^2$，相同），而 $x - y$ 不是（交换得 $y - x = -(x - y)$）。

**初等对称多项式**是对称多项式的"积木"——每个对称多项式都是这些积木的组合。

最经典的应用是 **Vieta 公式**：若 $r_1, \ldots, r_n$ 是多项式

$$
f(x) = x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0
$$

的全部根（计重数），则

$$
\sigma_k(r_1, \ldots, r_n) = (-1)^k a_{n-k}, \quad 1 \leq k \leq n.
$$

这建立了**根 → 系数**的对称桥梁：根的各种对称组合恰好对应多项式的系数。

## 基本性质

1. **对称多项式的对称性**：对称多项式的和、积、复合仍是对称的。
2. **初等对称多项式** $\sigma_1, \ldots, \sigma_n$ 代数无关（它们之间没有非平凡的多项式关系）。
3. **次数约束**：$\sigma_k$ 是 $k$ 次齐次多项式，且 $\deg \sigma_k = k$。
4. **对称多项式基本定理**保证了表示的唯一性——可以用 $\sigma_i$ 的幂积展开任何对称多项式。

## 链接

- 前置：[[ALG-DEF-001]] 一元多项式
- 关联：[[ALG-THM-005]] 根的个数与 Vieta 公式、[[ALG-THM-002]] 唯一分解定理（根的对称函数与系数对应）
- 用于：后续方程论与 Galois 理论中构造预解式

## 跨专业应用

- **代数几何**：射影空间中点的坐标是齐次坐标的 $\sigma_k$，对称性知识是 Grasmann 簇、旗簇等研究对象的基础
- **科学计算**：已知根求多项式——由 $r_1, \ldots, r_n$ 构造 $f(x) = \prod (x - r_i)$ 展开时系数正是 $(-1)^k \sigma_k(r_1, \ldots, r_n)$
