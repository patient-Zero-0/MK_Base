---
title: "用单调有界定理证明自然常数 e 的存在性"
type: example
id: ANL-EX-003
subject: analysis
chapter: 01-limits
tags:
  - 极限
  - 单调有界
  - 自然常数
  - 例题
depends:
  - ANL-DEF-009
  - ANL-THM-006
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §2.4 例 1"
difficulty: 3
illustrates:
  - ANL-THM-006
  - ANL-DEF-009
related:
  - ANL-EX-001
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

证明数列 $a_n = (1 + 1/n)^n$ 收敛，从而 [[ANL-DEF-009]] 中的极限存在。

## 分析

> **思路**：用 [[ANL-THM-006]] 单调有界定理。两步——
> 第一步证 $a_n$ 单调递增；第二步证 $a_n$ 有上界。
>
> **关键工具**：二项式展开，把 $(1 + 1/n)^n$ 化为有限和的形式
> $$
> a_n = \sum_{k=0}^{n} \binom{n}{k} \frac{1}{n^k}.
> $$
> 处理后**每一项**都能与 $a_{n+1}$ 对应项作比较，单调性立得；
> 同时通项可用 $\frac{1}{k!}$ 控制，得有界性。

## 证明 / 解答

**第 1 步：将 $a_n$ 化为可比形式。**

由二项式定理：
$$
a_n = \sum_{k=0}^{n} \binom{n}{k} \frac{1}{n^k}
    = \sum_{k=0}^{n} \frac{n(n-1)(n-2)\cdots(n-k+1)}{k! \, n^k}.
$$

把 $n^k$ 拆到分子各因子上：
$$
\frac{n(n-1)\cdots(n-k+1)}{n^k} = \prod_{j=0}^{k-1} \frac{n - j}{n} = \prod_{j=0}^{k-1} \left(1 - \frac{j}{n}\right).
$$

故
$$
a_n = \sum_{k=0}^{n} \frac{1}{k!} \prod_{j=0}^{k-1} \left(1 - \frac{j}{n}\right). \quad (\ast)
$$

**第 2 步：单调性 $a_n < a_{n+1}$。**

对比 $a_n$ 与 $a_{n+1}$：

- $a_{n+1}$ 共 $n + 2$ 项；$a_n$ 共 $n + 1$ 项——$a_{n+1}$ **多一项**（$k = n + 1$，正数）。
- 对相同的 $k$（$0 \leq k \leq n$），由 $\tfrac{j}{n + 1} < \tfrac{j}{n}$ 知 $1 - \tfrac{j}{n+1} > 1 - \tfrac{j}{n}$，
  故 $\prod_{j=0}^{k-1} (1 - \tfrac{j}{n+1}) > \prod_{j=0}^{k-1} (1 - \tfrac{j}{n})$。

两点合起来：$a_{n+1} > a_n$。$\{a_n\}$ 严格单调递增。

**第 3 步：有上界 $a_n < 3$。**

在 $(\ast)$ 中每个因子 $1 - \tfrac{j}{n} \in (0, 1)$，故
$$
a_n \leq \sum_{k=0}^{n} \frac{1}{k!}.
$$

而对 $k \geq 2$：$k! = 2 \cdot 3 \cdots k \geq 2 \cdot 2 \cdots 2 = 2^{k-1}$，故 $\tfrac{1}{k!} \leq \tfrac{1}{2^{k-1}}$。

$$
\sum_{k=0}^{n} \frac{1}{k!}
= 1 + 1 + \sum_{k=2}^{n} \frac{1}{k!}
\leq 2 + \sum_{k=2}^{n} \frac{1}{2^{k-1}}
< 2 + \sum_{k=1}^{\infty} \frac{1}{2^k}
= 2 + 1 = 3.
$$

故 $a_n < 3$ 对所有 $n$ 成立。

**第 4 步：应用单调有界定理。**

由 [[ANL-THM-006]]，单调递增 + 有上界 $\Rightarrow$ $\{a_n\}$ 收敛。
其极限即定义 [[ANL-DEF-009]] 中的自然常数 $e$，且 $2 \leq e \leq 3$。$\blacksquare$

## 关键技巧

- **二项式展开 + 因式重排**：把 $(1 + 1/n)^n$ 化为可与 $(1 + 1/(n+1))^{n+1}$ 逐项比较的形式，是处理"指数增长 vs 底接近 1"型不定型的标准武器。
- **逐项放大成阶乘倒数级数**：用 $\sum 1/k!$ 控制 $a_n$，这同时给出更精细的估计：实际上 $e = \sum_{k=0}^\infty \frac{1}{k!}$。
- **比较 $a_n$ 与 $a_{n+1}$ 时分两段**：相同下标项的因子比较 + $a_{n+1}$ 多出的正项。

## 变式

- **变式 1**：证明 $b_n = (1 + 1/n)^{n+1}$ 单调**递减**，且与 $a_n$ 同极限。这给出 $e$ 的"上下夹逼"估计：$a_n < e < b_n$。
- **变式 2**：证明 $\lim_n (1 + 1/n^2)^n = 1$（提示：用 $\ln(1 + x) \leq x$ 把指数表达式转到 $\sum 1/n$ 量级）。
- **变式 3**：证明 $\lim_n (1 + r/n)^n = e^r$ 对任意 $r \in \mathbb{R}$（提示：换元 $m = n/r$，分情况讨论 $r > 0, r < 0$）。
