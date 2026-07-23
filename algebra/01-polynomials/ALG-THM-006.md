---
title: "重因式判定（$\\gcd(f, f')$ 刻画）"
type: theorem
id: ALG-THM-006
subject: algebra
chapter: 01-polynomials
tags:
  - 多项式
  - 重因式
  - 形式导数
  - 最大公因式
depends:
  - ALG-DEF-005
  - ALG-THM-003
uses: []
status: draft
source: "丘维声《高等代数》第3版 §1.4"
difficulty: 3
related:
  - ALG-DEF-004
corollaries: []
applications:
  - "符号计算：多项式的无平方分解（square-free decomposition）"
  - "编码理论：BCH 码中判定多项式是否有重根"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设 $f(x) \in K[x]$ 是非零多项式，$f'(x)$ 是 $f$ 的形式导数（[[ALG-DEF-005]]），$\gcd(f, f')$ 是 $f$ 与 $f'$ 的首一最大公因式。

## 结论

> 设不可约多项式 $p(x) \mid f(x)$，则 $p$ 是 $f$ 的**重因式** $\iff$ $p$ 整除 $f$ 的形式导数 $f'$。即

$$
p^k \mid f,\; k \geq 2 \quad\Longleftrightarrow\quad p \mid f'.
$$

等价的全域表述：

> $f$ 有重因式 $\iff$ $\gcd(f, f') \neq 1$。

特别地，若 $\gcd(f, f') = 1$，则 $f$ 是**无平方的**（square-free，即没有重因式）。

## 几何/直觉理解

> 形式导数和重因式的关系是微积分中"重根处导数也为零"这一事实的**纯代数版本**。

在微积分中：若 $c$ 是 $f$ 的 $k \geq 2$ 重根，则 $f(c) = f'(c) = 0$。证明依赖乘积法则与极限。而本定理将这个关系**提升到因式层面**：

> 不依赖具体根的值，也不依赖域是否为 $\mathbb{R}$ 或 $\mathbb{C}$——在任意域 $K$ 上，形式导数 $f'$ 的整除性直接反映 $f$ 是否有重因式。

**核心观察**：若 $f = p^k \cdot g$，乘积法则给出

$$
f' = k p^{k-1} p' \cdot g + p^k \cdot g' = p^{k-1} \big( k p' g + p g' \big).
$$

当 $k \geq 2$ 时，$p^{k-1}$ 至少含一个 $p$，故 $p \mid f'$。反之，若 $p \mid f$ 且 $p \mid f'$，则 $p$ 必须至少是 $f$ 的 2 重因式——否在单因式情形下 $f'$ 的 $p$ 部分不会被消完。

## 证明

**($\Rightarrow$)** 设 $p^k \mid f$，$k \geq 2$。即 $f = p^k \cdot g$，$p \nmid g$。由乘积法则（[[ALG-DEF-005]] 性质条），

$$
f' = (p^k)' g + p^k g' = k p^{k-1} p' g + p^k g' = p^{k-1} (k p' g + p g').
$$

因 $k p^{k-1}$ 含有因子 $p$（注意 $k \geq 2$，故 $k-1 \geq 1$），所以 $p \mid f'$。

**($\Leftarrow$)** 设 $p \mid f$ 且 $p \mid f'$。将 $f$ 写为 $f = p^m \cdot g$，其中 $p \nmid g$，$m \geq 1$。需证 $m \geq 2$。

由上式计算

$$
f' = p^{m-1} (m p' g + p g').
$$

因 $p \mid f'$，而 $p^{m-1}$ 已有 $m-1$ 个 $p$ 因子，故 $p$ 必须整除 $m p' g + p g'$。当 $m = 1$ 时，

$$
f' = p^{0} (1 \cdot p' g + p g') = p' g + p g'.
$$

此时 $p \mid (p' g + p g')$。因 $p \mid p g'$，所以 $p \mid p' g$。而 $p$ 不可约（[[ALG-DEF-004]]），$p \nmid p'$（$\deg p' < \deg p$，除非 $p$ 是常数，但 $\deg p \geq 1$），且 $p \nmid g$（构造），故 $p \nmid p' g$，矛盾。

因此 $m \neq 1$，即 $m \geq 2$，故 $p$ 是 $f$ 的重因式。$\blacksquare$

## 常见错误

- ✗ 认为 $\gcd(f, f') \neq 1$ 等价于"$f$ 有重根"。在非代数闭域上，重因式不可约多项式的次数可以 $> 1$，不一定对应根。
  反例：$f(x) = (x^2+1)^2 (x+1)$ 在 $\mathbb{R}[x]$ 中，$(x^2+1)$ 是重因式（次数 2），但它在 $\mathbb{R}$ 中没有根——其根 $\pm i$ 不在 $\mathbb{R}$ 中。此时 $\gcd(f, f') \neq 1$ 仍然成立。
- ✗ 把定理理解为"$f'(c) = 0 \iff c$ 是 $f$ 的重根"。
  这个"重根"版本仅在 $\deg p = 1$（即 $p = (x-c)$）时才等价于 $f'(c) = f(c) = 0$。但本定理讨论的是**因式层面**的重数，不限于一次因式。
- ✗ 忘记特征 $p > 0$ 时的例外。若 $\operatorname{char} K = p$ 且 $f(x) = g(x^p)$，则 $f' = 0$。
  此时 $\gcd(f, f') = \gcd(f, 0) = f$（首一化），导致误判"$f$ 有重因式"——实际上 $f$ 可能是无平方的（如 $x^p - a$ 在 $\mathbb{F}_p$ 上）。本课程工作于特征 0，此问题不会出现。

## 推论与应用

1. **无平方分解**：反复取 $\gcd(f, f')$ 并将 $f / \gcd(f, f')$ 分离出去，可得到 $f$ 的"无平方部分"。这在符号计算中是多项式因式分解的第一步。
2. **重因式分离**：若 $\gcd(f, f') \neq 1$，令 $\tilde f = f / \gcd(f, f')$，则 $\tilde f$ 与 $f$ 有相同的**不可约因子**但全部为**单因式**——从而把重因式问题化为单因式情形。
3. **根的重数判定**：对一次因式 $(x-c)$，$c$ 是 $f$ 的重根 $\iff f(c) = f'(c) = 0$。

## 链接

- 前置：[[ALG-DEF-005]] 重因式与形式导数、[[ALG-THM-003]] 辗转相除法（用于计算 $\gcd$）
- 关联：[[ALG-DEF-004]] 不可约多项式（重因式的定义依赖于不可约性）
- 用于：后续方程论中判定方程是否有重根

## 跨专业应用

- **符号计算**：多项式的**无平方分解**（square-free decomposition）完全依赖本定理：反复 $f \mapsto f / \gcd(f, f')$ 直至 $\gcd = 1$。这是计算机代数系统多项式因式分解流水线的第一步（Yun 算法）。
- **编码理论**：BCH 码中，码字多项式在有限域 $\mathbb{F}_q$ 上的根决定纠错能力。判定多项式是否有重根即检查 $\gcd(f, f') = 1$，是设计高效译码算法的基础。
