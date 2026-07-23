---
title: "整除与互素综合"
type: problem
id: ALG-PROB-001
subject: algebra
chapter: 01-polynomials
tags:
  - 多项式
  - 整除
  - 互素
  - 综合
depends:
  - ALG-DEF-002
  - ALG-DEF-003
  - ALG-THM-003
uses: []
status: draft
source: "丘维声《高等代数》第3版 §1.3 习题"
difficulty: 3
tests:
  - ALG-DEF-002
  - ALG-DEF-003
  - ALG-THM-003
related: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

设 $f(x), g(x), h(x) \in K[x]$。

1. 若 $\gcd(f, g) = 1$ 且 $\gcd(f, h) = 1$，证明 $\gcd(f, gh) = 1$。
2. 若 $\gcd(f, g) = 1$ 且 $f \mid gh$，证明 $f \mid h$。（互素版 Euclid 引理）
3. 举例说明：若去掉 $\gcd(f, g) = 1$ 的条件，$f \mid gh$ 不能推出 $f \mid h$。

## 提示

<details><summary>点击展开提示</summary>

- **第 1 题**：用 Bézout 等式。存在 $u_1, v_1$ 使 $u_1 f + v_1 g = 1$，存在 $u_2, v_2$ 使 $u_2 f + v_2 h = 1$。将两个等式相乘。
- **第 2 题**：利用第 1 题的结论：$\gcd(f, gh) = 1$。结合 $f \mid gh$，由最大公因式的性质可得 $f$ 与 $gh$ 的关系。
- **第 3 题**：尝试在 $\mathbb{Q}[x]$ 中找简单的反例，让 $f$ 和 $g$ 有公因式。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题

因 $\gcd(f, g) = 1$，由 Bézout 等式（[[ALG-THM-003]]），存在 $u_1, v_1 \in K[x]$ 使

$$
u_1 f + v_1 g = 1.
$$

同理，存在 $u_2, v_2 \in K[x]$ 使

$$
u_2 f + v_2 h = 1.
$$

将两式相乘：

$$
1 = (u_1 f + v_1 g)(u_2 f + v_2 h) = (u_1 u_2 f + u_1 v_2 h + v_1 u_2 g) f + (v_1 v_2) (gh).
$$

即存在 $U, V \in K[x]$ 使 $U f + V (gh) = 1$。由互素的 Bézout 判据（[[ALG-THM-003]] 结论 3），$\gcd(f, gh) = 1$。$\blacksquare$

### 第 2 题

已知 $f \mid gh$，即存在 $q \in K[x]$ 使 $gh = f q$。又由第 1 题，$\gcd(f, gh) = 1$。但 $f \mid gh$ 且 $\gcd(f, gh) = 1$ 意味着 $f$ 是 $gh$ 的因式且与 $gh$ 互素——这只有在 $f$ 是常数（$\deg f = 0$）时才可能，但这里 $f$ 并非一定是常数。需要换一个思路。

**正确证法**：由 $\gcd(f, g) = 1$，存在 $u, v$ 使 $u f + v g = 1$。两边乘以 $h$：

$$
u f h + v g h = h.
$$

因 $f \mid gh$，设 $gh = f k$，代入：

$$
u f h + v (f k) = f (u h + v k) = h.
$$

故 $f \mid h$。$\blacksquare$

### 第 3 题

取 $K = \mathbb{Q}$，$f(x) = x$，$g(x) = x$，$h(x) = 1$。则 $\gcd(f, g) = x \neq 1$。$f \mid gh$ 即 $x \mid (x \cdot 1) = x$ 显然成立，但 $f \mid h$ 即 $x \mid 1$ 不成立。

更一般的反例：$f = g = (x-1)$，$h = 1$，同样 $f \mid gh$ 成立但 $f \nmid h$。

这说明"互素"条件是必不可少的——没有它，$f$ 的信息可能会被 $g$ "携带"进乘积中，但无法传递到 $h$。

</details>

## 考察点

- [[ALG-DEF-002]] 整除的基本性质
- [[ALG-DEF-003]] 互素的 Bézout 等式刻画
- [[ALG-THM-003]] 辗转相除法与 Bézout 等式的存在性
