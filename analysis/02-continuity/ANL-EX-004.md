---
title: "用 Heine 归结原则证明函数极限不存在"
type: example
id: ANL-EX-004
subject: analysis
chapter: 02-continuity
tags:
  - 函数极限
  - Heine
  - 反例构造
  - 例题
depends:
  - ANL-DEF-010
  - ANL-THM-012
  - ANL-DEF-004
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §3.1 例 6"
difficulty: 3
illustrates:
  - ANL-THM-012
related:
  - ANL-DEF-013
  - ANL-PROB-001
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

证明 $\displaystyle \lim_{x \to 0} \sin(1/x)$ **不存在**。

## 分析

> 直接用 ε-δ 反推太麻烦——需要构造对所有 $\delta > 0$ 都失效的反例。
> **更简洁的路径**：[[ANL-THM-012]] Heine 等价定理的反向用法。
>
> **核心思路**：找两个数列 $\{x_n\}, \{y_n\}$ 都 $\to 0$（且都 $\neq 0$），
> 但 $\sin(1/x_n)$ 与 $\sin(1/y_n)$ 收敛于**不同**的极限。
>
> **构造关键**：让 $1/x_n$ 落在 $\sin$ 的"同一相位"，使 $\sin(1/x_n)$ 全是同一值。
> 取 $1/x_n = n\pi$（$\sin = 0$ 的零点）和 $1/y_n = (4n+1)\pi/2$（$\sin = 1$ 的最大值点）即可。

## 证明

**证明：** 取两个数列：
$$
x_n = \frac{1}{n\pi}, \qquad y_n = \frac{2}{(4n+1)\pi}, \qquad n \in \mathbb{N}^*.
$$

**第 1 步：两数列都 $\to 0$ 且 $\neq 0$。**

$x_n = 1/(n\pi) > 0$ 且 $x_n \to 0$（因 $1/n \to 0$）。
$y_n = 2/((4n+1)\pi) > 0$ 且 $y_n \to 0$。
均满足 Heine 条件。

**第 2 步：计算两数列的像。**

$$
\sin(1/x_n) = \sin(n\pi) = 0 \quad (\forall n) \implies \lim_n \sin(1/x_n) = 0.
$$

$$
\sin(1/y_n) = \sin\left(\frac{(4n+1)\pi}{2}\right) = \sin\left(2n\pi + \frac{\pi}{2}\right) = \sin\frac{\pi}{2} = 1.
$$
故 $\lim_n \sin(1/y_n) = 1$。

**第 3 步：反向应用 Heine。**

假设 $\displaystyle \lim_{x \to 0} \sin(1/x) = L$ 存在。
由 [[ANL-THM-012]] Heine 等价：

- $x_n \to 0, x_n \neq 0 \implies \sin(1/x_n) \to L$，故 $L = 0$。
- $y_n \to 0, y_n \neq 0 \implies \sin(1/y_n) \to L$，故 $L = 1$。

得 $0 = L = 1$，矛盾。

故 $\displaystyle \lim_{x \to 0} \sin(1/x)$ **不存在**。$\blacksquare$

## 关键技巧

- **"双数列反证"模板**：用 Heine 反向证明极限不存在的标准武器。
  关键是构造的两个数列必须**都满足 $\to x_0$ 且 $\neq x_0$**，但像列收敛到不同值。
- **零点 vs 极值点**：振荡函数的"最便利反例对"——零点列让函数值恒为 0，极值点列让函数值恒为 ±1。
- **可推广到其他振荡极限**：$\cos(1/x), \sin(1/x^2), \tan(1/x)$ 等当 $x \to 0$ 时极限不存在，证明结构完全平行。

## 变式

- **变式 1**：证明 $\displaystyle \lim_{x \to 0} \cos(1/x)$ 不存在。
  提示：取 $x_n = 1/(2n\pi), y_n = 1/((2n+1)\pi)$。
- **变式 2**：证明 $\displaystyle \lim_{x \to +\infty} \sin x$ 不存在。
  提示：取 $x_n = n\pi, y_n = 2n\pi + \pi/2$（注意此处 $\to +\infty$ 不是 $\to x_0$，需用 $\lim_{x \to \infty}$ 的 Heine 版本）。
- **变式 3**：分析 $\lim_{x \to 0} x \sin(1/x)$。提示：与本题对比——这次极限**存在**为 $0$（用夹逼 $|x\sin(1/x)| \leq |x|$）。说明"局部振荡 + 衰减"vs"局部振荡 + 不衰减"的核心差别。
