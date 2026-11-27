---
title: "证明复合函数在实数集上非一致连续"
type: problem
id: ANL-PROB-031
subject: analysis
chapter: 02-continuity
tags:
  - 一致连续
  - 反例构造
  - ε-δ
depends:
  - ANL-DEF-024
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §4.2 习题"
difficulty: 4
tests:
  - ANL-DEF-024
related:
  - ANL-EX-007
---

## 题目

> 证明函数 $f(x) = \sin(x^2)$ 在 $\mathbb{R}$ 上每点连续，但**不**一致连续。

## 提示

<details><summary>点击展开提示</summary>

- 一致连续的反命题：存在某 $\varepsilon_0 > 0$，对任意 $\delta > 0$，可找出一对 $x_1, x_2 \in \mathbb{R}$ 使 $|x_1 - x_2| < \delta$ 但 $|f(x_1) - f(x_2)| \geq \varepsilon_0$。
- 直觉：在大 $x$ 附近，$\sin(x^2)$ 完成一次整周期所需的 $\Delta x$ 越来越小（因为 $x^2$ 增长越来越快），故无论 $\delta$ 取多小，总有相距 $< \delta$ 的两点跨越大段振荡。
- 构造**两组同时趋于无穷**的点列 $\{x_n\}, \{y_n\}$，使 $|x_n - y_n| \to 0$ 但 $|f(x_n) - f(y_n)|$ 不趋于 0。
- 函数值差能直接做到 $1$ 或更大的简单方法：让 $x_n^2$ 取 $2n\pi$ 类型，让 $y_n^2$ 取 $2n\pi + \pi/2$ 类型。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

**逐点连续**：$x \mapsto x^2$ 在 $\mathbb{R}$ 上连续，$\sin$ 在 $\mathbb{R}$ 上连续，由复合函数连续性 $f$ 在 $\mathbb{R}$ 上每点连续。

**非一致连续**：取 $\varepsilon_0 = 1$。下证：对任意 $\delta > 0$，可构造 $x_1, x_2 \in \mathbb{R}$ 使 $|x_1 - x_2| < \delta$ 但 $|f(x_1) - f(x_2)| \geq 1$。

对 $n \in \mathbb{N}^*$，令
$$
x_n = \sqrt{2n\pi + \pi / 2}, \qquad y_n = \sqrt{2n\pi}.
$$

则
$$
f(x_n) = \sin(2n\pi + \pi / 2) = 1, \qquad f(y_n) = \sin(2n\pi) = 0,
$$
故 $|f(x_n) - f(y_n)| = 1$ 对所有 $n$ 成立。

另一方面，
$$
x_n - y_n = \sqrt{2n\pi + \pi / 2} - \sqrt{2n\pi}
        = \frac{\pi / 2}{\sqrt{2n\pi + \pi / 2} + \sqrt{2n\pi}}
        \to 0 \quad (n \to \infty).
$$

故对任意 $\delta > 0$，存在 $N$ 使 $\forall n > N: |x_n - y_n| < \delta$。
取 $x_1 := x_{N+1}, x_2 := y_{N+1}$ 即得反例。

依 [[ANL-DEF-024]] 的反命题，$f$ 在 $\mathbb{R}$ 上非一致连续。$\blacksquare$

</details>

## 考察点

- [[ANL-DEF-024]] 一致连续定义的反命题构造
- 对实数列差的"分子有理化"技巧

## 备注

- 与之对比：$f$ 在任何**有界**闭区间 $[a, b]$ 上一致连续（[[ANL-THM-015]] Cantor 定理）。
- 关键症结在于"无界域 + 局部斜率无界"，常出现在 $\sin(x^k)\,(k \geq 2)$、$x \sin x$ 等函数上。
