---
title: "用 Cauchy 收敛准则证明数列收敛性"
type: problem
id: ANL-PROB-005
subject: analysis
chapter: 01-limits
tags:
  - Cauchy 准则
  - 收敛性
  - 反例构造
depends:
  - ANL-DEF-002
  - ANL-THM-007
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §2.3 习题"
difficulty: 4
tests:
  - ANL-DEF-002
  - ANL-THM-007
related:
  - ANL-THM-006
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

利用 [[ANL-THM-007]] Cauchy 收敛准则证明或反驳：

1. **证明收敛**：$\displaystyle a_n = \sum_{k=1}^{n} \frac{1}{k^2}$ 收敛。
2. **证明发散**：调和数列 $\displaystyle H_n = \sum_{k=1}^{n} \frac{1}{k}$ **不**是 Cauchy 列，从而**不**收敛。
3. **构造与判定**：$\displaystyle b_n = \sum_{k=1}^{n} \frac{(-1)^{k+1}}{k}$ 是否是 Cauchy 列？

## 提示

<details><summary>点击展开提示</summary>

- 第 1 题：估计 $|a_n - a_m|$ 当 $n > m$。利用 $\frac{1}{k^2} < \frac{1}{k(k-1)} = \frac{1}{k-1} - \frac{1}{k}$（裂项）。
- 第 2 题：取 $m = n$ 与 $2n$（具体配对），证明 $|H_{2n} - H_n| \geq 1/2$ 恒成立——直接违反 Cauchy 条件。
- 第 3 题：交错级数。配对相邻两项 $\frac{(-1)^{k+1}}{k} + \frac{(-1)^{k+2}}{k+1} = \frac{1}{k(k+1)}$（同号正），可估上界。或用 Leibniz 判别。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题

**证明：** 验证 $\{a_n\}$ 是 Cauchy 列。

任给 $\varepsilon > 0$。对 $n > m \geq 1$：
$$
|a_n - a_m| = \sum_{k=m+1}^{n} \frac{1}{k^2}.
$$

利用裂项不等式 $\frac{1}{k^2} < \frac{1}{k(k-1)} = \frac{1}{k-1} - \frac{1}{k}$（$k \geq 2$）：
$$
\sum_{k=m+1}^{n} \frac{1}{k^2} < \sum_{k=m+1}^{n} \left( \frac{1}{k-1} - \frac{1}{k} \right) = \frac{1}{m} - \frac{1}{n} < \frac{1}{m}.
$$

要使 $\frac{1}{m} < \varepsilon$，取 $N = \lceil 1/\varepsilon \rceil$。

对 $\forall m, n > N$（不妨设 $n > m$），$|a_n - a_m| < \frac{1}{m} < \frac{1}{N} \leq \varepsilon$。

故 $\{a_n\}$ 是 [[ANL-DEF-002]] Cauchy 列。由 [[ANL-THM-007]]，$\{a_n\}$ 收敛。$\blacksquare$

> 实际上 $\sum_{k=1}^\infty \frac{1}{k^2} = \frac{\pi^2}{6}$（Basel 问题，Euler 1735）。

### 第 2 题：调和数列发散

**证明：** 验证 $\{H_n\}$ **不**是 Cauchy 列。

取 $m = n, n' = 2n$（即 $|H_{2n} - H_n|$）。
$$
H_{2n} - H_n = \sum_{k=n+1}^{2n} \frac{1}{k}.
$$

共 $n$ 项，每项 $\geq \frac{1}{2n}$，故
$$
H_{2n} - H_n \geq n \cdot \frac{1}{2n} = \frac{1}{2}.
$$

取 $\varepsilon_0 = 1/2$。对**任何** $N$，可取 $m = n_1 = N + 1, n_2 = 2(N+1) > N$，
则 $|H_{n_2} - H_{n_1}| \geq 1/2 = \varepsilon_0$。

故 [[ANL-DEF-002]] Cauchy 条件失败，$\{H_n\}$ 不是 Cauchy 列；
由 [[ANL-THM-007]]，$\{H_n\}$ 不收敛（$H_n \to \infty$）。$\blacksquare$

### 第 3 题：交错调和级数是 Cauchy 列

**证明：** 验证 $\{b_n\}$ 是 Cauchy 列。

对 $n > m \geq 1$：
$$
b_n - b_m = \sum_{k=m+1}^{n} \frac{(-1)^{k+1}}{k}.
$$

**关键技巧（Abel 求和 / 配对）**：把相邻两项配对。不失一般性设 $n - m$ 为偶数（奇数情形类似处理多余的尾项）：

- 若 $m$ 为偶数：$(b_n - b_m) = \frac{1}{m+1} - \frac{1}{m+2} + \frac{1}{m+3} - \cdots$。配对相邻负正两项：
  $$
  \left( \frac{1}{m+1} - \frac{1}{m+2} \right) + \left( \frac{1}{m+3} - \frac{1}{m+4} \right) + \cdots
  $$
  每对都为正，且整体被 $\frac{1}{m+1}$ 控制（去掉所有负项后剩下首项加少量正项的上界）。

更简捷的估计：$|b_n - b_m| \leq \frac{1}{m + 1}$（交错级数余项的标准估计）。

证：把求和按 $\frac{1}{m+1} - \left( \frac{1}{m+2} - \frac{1}{m+3} \right) - \left(\frac{1}{m+4} - \frac{1}{m+5}\right) - \cdots$ 改写——除首项外每个括号都是正的，故 $|b_n - b_m| \leq \frac{1}{m+1}$。

任给 $\varepsilon > 0$，取 $N = \lceil 1/\varepsilon \rceil$，$\forall n > m > N$：
$|b_n - b_m| \leq \frac{1}{m + 1} < \frac{1}{N} \leq \varepsilon$。

故 $\{b_n\}$ 是 Cauchy 列，由 [[ANL-THM-007]] 收敛。$\blacksquare$

> 实际上 $\sum_{k=1}^\infty \frac{(-1)^{k+1}}{k} = \ln 2$。

</details>

## 考察点

- [[ANL-DEF-002]] Cauchy 列定义的"任意两项"理解（不是仅相邻两项）
- [[ANL-THM-007]] Cauchy 准则的**双向**应用
- 估计技巧：裂项、配对、放缩

## 备注

第 1、2 题对照说明 Cauchy 准则的强大：

- $1/k^2$ 比 $1/k$ 衰减"略快一点"，前者收敛后者发散——分水岭就在 $\sum 1/k^p$ 中 $p > 1$ vs $p \leq 1$。
- Cauchy 准则的优势：**无需先猜出极限值**就能判定收敛性。
