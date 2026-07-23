---
title: "不可约性与唯一分解证明"
type: problem
id: ALG-PROB-002
subject: algebra
chapter: 01-polynomials
tags:
  - 多项式
  - 不可约
  - 唯一分解
depends:
  - ALG-DEF-004
  - ALG-THM-002
  - ALG-THM-003
uses: []
status: draft
source: "丘维声《高等代数》第3版 §1.5 习题"
difficulty: 4
tests:
  - ALG-DEF-004
  - ALG-THM-002
  - ALG-THM-003
related: []
---

## 题目

1. 设 $p(x) \in K[x]$ 不可约。证明：对任意 $f(x) \in K[x]$，要么 $p \mid f$，要么 $\gcd(p, f) = 1$。
2. 利用 (1) 证明：若不可约多项式 $p$ 满足 $p \mid fg$，则 $p \mid f$ 或 $p \mid g$。（不可约 ⇒ 素性）
3. 在 $\mathbb{Q}[x]$ 中，判断 $f(x) = x^4 + 2x^2 + 1$ 是否可约。若可约，给出分解。

## 提示

<details><summary>点击展开提示</summary>

- **第 1 题**：设 $d = \gcd(p, f)$。由于 $p$ 不可约，$d$ 只能是 $1$ 或 $p$ 的常数倍。
- **第 2 题**：若 $p \nmid f$，由第 1 题知 $\gcd(p, f)=1$，存在 $u, v$ 使 $u p + v f = 1$，乘以 $g$ 后利用 $p \mid fg$。
- **第 3 题**：令 $y = x^2$，则 $f = y^2 + 2y + 1 = (y+1)^2$，代回 $x$。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题

因为 $p$ 不可约（[[ALG-DEF-004]]），其因式只有非零常数和 $p$ 的非零常数倍。设 $d = \gcd(p, f)$（首一化），则 $d \mid p$。故 $d$ 要么是 1，要么是 $p$（首一化后）。

- 若 $d = 1$，则 $\gcd(p, f)=1$。
- 若 $d = p$，则 $p \mid f$。$\blacksquare$

### 第 2 题

设 $p \mid fg$。若 $p \mid f$，结论已成立。若 $p \nmid f$，由第 1 题知 $\gcd(p, f)=1$。由 Bézout 等式（[[ALG-THM-003]]），存在 $u, v \in K[x]$ 使

$$
u p + v f = 1.
$$

两边乘以 $g$：

$$
u p g + v f g = g.
$$

因为 $p \mid fg$，设 $fg = p h$，代入得 $g = p (u g + v h)$，故 $p \mid g$。$\blacksquare$

### 第 3 题

令 $y = x^2$，则

$$
f(x) = x^4 + 2x^2 + 1 = y^2 + 2y + 1 = (y+1)^2 = (x^2+1)^2.
$$

在 $\mathbb{Q}[x]$ 中，$x^2+1$ 是**不可约**的（无有理根，$\deg=2$），故 $f = (x^2+1)^2$ 是 $f$ 在 $\mathbb{Q}[x]$ 中的标准分解。$f$ 在 $\mathbb{Q}[x]$ 中**可约**（分解为两个二次式的乘积），且有重因式 $(x^2+1)$（2重）。

在 $\mathbb{C}[x]$ 中进一步分解：$x^2+1 = (x-\mathrm{i})(x+\mathrm{i})$，故 $f = (x-\mathrm{i})^2 (x+\mathrm{i})^2$。

</details>

## 考察点

- [[ALG-DEF-004]] 不可约多项式的性质
- [[ALG-THM-002]] 唯一分解定理的证明思路
- [[ALG-THM-003]] Bézout 等式的应用
