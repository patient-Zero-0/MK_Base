---
title: "重根与导数综合"
type: problem
id: ALG-PROB-003
subject: algebra
chapter: 01-polynomials
tags:
  - 多项式
  - 重根
  - 形式导数
depends:
  - ALG-DEF-005
  - ALG-THM-006
  - ALG-DEF-006
uses: []
status: draft
source: "丘维声《高等代数》第3版 §1.4 习题"
difficulty: 3
tests:
  - ALG-DEF-005
  - ALG-THM-006
  - ALG-DEF-006
related: []
---

## 题目

1. 设 $f(x) \in K[x]$，$c \in K$。证明：$c$ 是 $f$ 的 $k$ 重根 $\iff f(c) = f'(c) = \cdots = f^{(k-1)}(c) = 0$ 且 $f^{(k)}(c) \neq 0$。
2. 求多项式 $f(x) = (x-1)^3 (x+2)^2$ 的 $f'$ 和 $f''$，验证上述结论。
3. 证明：若 $f(x) \in \mathbb{R}[x]$ 无重根，则 $f$ 与 $f'$ 互素。

## 提示

<details><summary>点击展开提示</summary>

- **第 1 题**：对 $k$ 用归纳法，结合因式定理和形式导数的乘积法则。
- **第 2 题**：先展开 $(x-1)^3(x+2)^2$ 再求导，或直接用乘积法则计算。
- **第 3 题**：由重因式判定定理，$f$ 无重因式 $\iff \gcd(f, f') = 1$。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题

**归纳基础**（$k = 1$）：$c$ 是单根 $\iff f(c) = 0$ 且 $f'(c) \neq 0$。由因式定理，$c$ 是根 $\iff f(c)=0$。由重因式判定定理（[[ALG-THM-006]]），$k=1$ 时 $(x-c)$ 不是 $f$ 的重因式 $\iff f'(c) \neq 0$。成立。

**归纳步骤**：假设结论对 $k-1$ 成立。设 $c$ 是 $f$ 的 $k$ 重根，则 $f(x) = (x-c)^k g(x)$，$g(c) \neq 0$。求导：

$$
f'(x) = k(x-c)^{k-1} g(x) + (x-c)^k g'(x) = (x-c)^{k-1} [k g(x) + (x-c) g'(x)].
$$

令 $h(x) = k g(x) + (x-c) g'(x)$，则 $h(c) = k g(c) \neq 0$。故 $c$ 是 $f'$ 的 $k-1$ 重根。由归纳假设，$f'(c) = \cdots = f'^{(k-2)}(c) = 0$ 且 $f'^{(k-1)}(c) \neq 0$，即 $f^{(j)}(c) = 0$（$1 \leq j \leq k-1$）且 $f^{(k)}(c) \neq 0$。$\blacksquare$

### 第 2 题

$f(x) = (x-1)^3 (x+2)^2$。用乘积法则：

$$
f'(x) = 3(x-1)^2 (x+2)^2 + (x-1)^3 \cdot 2(x+2) = (x-1)^2 (x+2)\bigl[3(x+2) + 2(x-1)\bigr] = (x-1)^2 (x+2)(5x+4).
$$

验证：$f(1)=0$，$f'(1)=0$，但 $f''(1)$ 应非零（1 是 3 重根，$f''(1)$ 是第一个非零导数）。$f(-2)=0$，$f'(-2)=0$，但 $f''(-2)$ 也为零吗？$-2$ 是 2 重根，所以 $f''(-2)\neq 0$。

### 第 3 题

$f$ 无重根 $\iff$ $f$ 的每个不可约因式都是一次的且重数为 1 $\iff$ $f$ 无重因式。由重因式判定定理（[[ALG-THM-006]]），$f$ 无重因式 $\iff \gcd(f, f') = 1$。$\blacksquare$

</details>

## 考察点

- [[ALG-DEF-005]] 形式导数与重因式
- [[ALG-THM-006]] 重因式判定
- [[ALG-DEF-006]] 根的重数概念
