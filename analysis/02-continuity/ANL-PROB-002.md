---
title: "一致连续判定（综合练习）"
type: problem
id: ANL-PROB-002
subject: analysis
chapter: 02-continuity
tags:
  - 一致连续
  - 综合练习
  - 反例构造
depends:
  - ANL-DEF-024
  - ANL-THM-015
  - ANL-DEF-012
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §4.2 习题"
difficulty: 4
tests:
  - ANL-DEF-024
  - ANL-THM-015
related:
  - ANL-PROB-031
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

判断下列函数在指定区间上**是否一致连续**，给出严格证明或反例：

1. $f(x) = \sqrt{x}$ 在 $[0, +\infty)$ 上。
2. $f(x) = x^2$ 在 $[0, +\infty)$ 上。
3. $f(x) = \dfrac{1}{x}$ 在 $(0, 1]$ 上。
4. $f(x) = x \sin x$ 在 $\mathbb{R}$ 上。

## 提示

<details><summary>点击展开提示</summary>

- 第 1 题：$\sqrt{x}$ 在 $[0, +\infty)$ 上单调连续，但定义域无界——直觉上 $\sqrt{x}$ 增长很慢（导数 $\to 0$），可能一致连续。试用 $|\sqrt{a} - \sqrt{b}| \leq \sqrt{|a - b|}$。
- 第 2 题：在无界域上"局部斜率"$|2x|$ 无界——典型一致连续反例。构造 $x_n, y_n \to \infty$ 使 $|x_n - y_n| \to 0$ 但 $|x_n^2 - y_n^2| \not\to 0$。
- 第 3 题：定义域 $(0, 1]$ 不闭——端点 $0$ 处 $f \to \infty$，[[ANL-THM-015]] Cantor 不适用。构造 $x_n, y_n \to 0^+$ 反例。
- 第 4 题：$x \sin x$ 在大 $x$ 时局部斜率 $|\sin x + x \cos x|$ 包含 $x \cos x$，无界——预期非一致连续。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题

**证明（用代数不等式）**：对 $a, b \geq 0$，有
$$
|\sqrt{a} - \sqrt{b}| \leq \sqrt{|a - b|}.
$$
（证：不妨设 $a \geq b$，$|\sqrt{a} - \sqrt{b}|^2 = a - 2\sqrt{ab} + b \leq a - 2b + b = a - b$，因 $\sqrt{ab} \geq b$。）

任给 $\varepsilon > 0$，取 $\delta = \varepsilon^2$。对任意 $x_1, x_2 \in [0, +\infty), |x_1 - x_2| < \delta$：
$$
|\sqrt{x_1} - \sqrt{x_2}| \leq \sqrt{|x_1 - x_2|} < \sqrt{\delta} = \varepsilon.
$$
故 $\sqrt{x}$ 一致连续。$\blacksquare$

> **关键观察**：尽管定义域无界，但 $\sqrt{x}$ 增长速度衰减（$\sqrt{x}' = 1/(2\sqrt{x}) \to 0$），故"局部抖动幅度"可被全局 $\delta$ 控制。

### 第 2 题

**证明（构造反例）**：取
$$
x_n = n, \qquad y_n = n + \frac{1}{n}.
$$

- $|x_n - y_n| = 1/n \to 0$。
- $|x_n^2 - y_n^2| = |n^2 - (n + 1/n)^2| = |2 + 1/n^2| > 2$ 对所有 $n$。

由 [[ANL-DEF-024]] 反命题：取 $\varepsilon_0 = 2$，对任意 $\delta > 0$ 总能找到 $n$ 使 $1/n < \delta$ 但 $|x_n^2 - y_n^2| > 2 = \varepsilon_0$。
故 $x^2$ 在 $[0, +\infty)$ 非一致连续。$\blacksquare$

### 第 3 题

**证明（构造反例）**：取
$$
x_n = \frac{1}{n}, \qquad y_n = \frac{1}{n + 1}, \qquad n \geq 1.
$$

- $x_n, y_n \in (0, 1]$ 且 $|x_n - y_n| = \frac{1}{n(n+1)} \to 0$。
- $|f(x_n) - f(y_n)| = |n - (n + 1)| = 1$ 对所有 $n$。

取 $\varepsilon_0 = 1$，反命题成立 ⇒ 非一致连续。$\blacksquare$

> 验证 [[ANL-THM-015]] 不适用的原因：定义域 $(0, 1]$ **不闭**（端点 $0$ 不在内）；事实上 $f \to \infty$ 当 $x \to 0^+$，"局部斜率"$|f'(x)| = 1/x^2$ 在 $0$ 附近无界。

### 第 4 题

**证明（构造反例）**：取
$$
x_n = 2n\pi + \frac{1}{n}, \qquad y_n = 2n\pi.
$$

- $|x_n - y_n| = 1/n \to 0$。
- 计算 $f(x_n) - f(y_n) = (2n\pi + 1/n) \sin(1/n) - 0$。
  当 $n$ 大时 $\sin(1/n) \approx 1/n$，故
  $$
  f(x_n) - f(y_n) \approx (2n\pi + 1/n) \cdot 1/n = 2\pi + 1/n^2 \to 2\pi.
  $$
- 严格估计：$\sin(1/n) \geq 1/n - 1/(6n^3)$（Taylor 展开余项），故 $f(x_n) - f(y_n) \geq (2n\pi + 1/n)(1/n - 1/(6n^3)) > 2\pi - O(1/n^2)$。
  对充分大 $n$，$|f(x_n) - f(y_n)| > \pi$。

取 $\varepsilon_0 = \pi$，反命题成立 ⇒ 非一致连续。$\blacksquare$

</details>

## 考察点

- [[ANL-DEF-024]] 一致连续定义的正用与反用
- [[ANL-THM-015]] Cantor 定理的**前提**："闭区间"和"有界"缺一不可
- 反例构造的标准两步法：选 $x_n, y_n$ 使 $|x_n - y_n| \to 0$；证 $|f(x_n) - f(y_n)| \not\to 0$

## 备注

四种典型情形对照：

| 函数 | 域 | 一致连续？| 失败/成功原因 |
|---|---|---|---|
| $\sqrt{x}$ | $[0, +\infty)$ | ✅ | 增长率 $\to 0$ |
| $x^2$ | $[0, +\infty)$ | ❌ | 局部斜率 $\to \infty$，**域无界** |
| $1/x$ | $(0, 1]$ | ❌ | $x \to 0^+$ 时斜率 $\to \infty$，**域不闭** |
| $x \sin x$ | $\mathbb{R}$ | ❌ | 局部斜率 $\to \infty$，**域无界** |

记忆要点：**Cantor 定理 [[ANL-THM-015]] 给出充分条件（闭区间 + 连续 ⇒ 一致连续），但反例集中出现在"无界域 + 局部斜率无界"或"非闭域 + 端点处斜率爆炸"两类**。
