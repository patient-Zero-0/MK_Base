---
title: "用夹逼定理求两个数列的极限"
type: example
id: ANL-EX-001
subject: analysis
chapter: 01-limits
tags:
  - 极限
  - 夹逼
  - 例题
depends:
  - ANL-THM-005
  - ANL-DEF-004
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §2.2 例 2、例 4"
difficulty: 2
illustrates:
  - ANL-THM-005
related:
  - ANL-THM-006
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

利用 [[ANL-THM-005]] 夹逼定理，证明：

1. $\displaystyle \lim_{n \to \infty} \frac{\sin n}{n} = 0$；
2. $\displaystyle \lim_{n \to \infty} \sqrt[n]{n} = 1$。

## 分析

> **第 1 题分析**：$\sin n$ 在 $[-1, 1]$ 间振荡——直接讨论极限困难。
> 但**绝对值**有简单上界 $|\sin n| \leq 1$，于是 $|\sin n / n| \leq 1/n$。
> 把"振荡的部分关进绝对值，转嫁到衰减的部分"——这是夹逼定理处理"振荡 × 衰减"的经典套路。

---

> **第 2 题分析**：$\sqrt[n]{n}$ 形如"$\infty^0$"不定型，须改写。
> 关键观察：$\sqrt[n]{n} \geq 1$（$n \geq 1$ 时显然），故只需上界。
> 设 $\sqrt[n]{n} = 1 + h_n$（$h_n \geq 0$），则 $n = (1 + h_n)^n$。
> 由二项式：$n \geq \binom{n}{2} h_n^2 = \tfrac{n(n-1)}{2} h_n^2$，
> 故 $h_n^2 \leq \tfrac{2}{n - 1}$，得 $0 \leq h_n \leq \sqrt{2 / (n - 1)} \to 0$。
> 这把"指数式渐近 1"化为"误差的代数上界"，再用夹逼定理。

## 证明 / 解答

### 第 1 题

**证明：** 对所有 $n \geq 1$，由 $|\sin n| \leq 1$：
$$
-\frac{1}{n} \leq \frac{\sin n}{n} \leq \frac{1}{n}.
$$

而 $-1/n \to 0$ 且 $1/n \to 0$。由 [[ANL-THM-005]]，$\displaystyle \lim_{n \to \infty} \frac{\sin n}{n} = 0$。$\blacksquare$

### 第 2 题

**证明：** 当 $n \geq 1$ 时 $\sqrt[n]{n} \geq 1$，故记 $h_n = \sqrt[n]{n} - 1 \geq 0$。

由 $n = (1 + h_n)^n$ 及二项式定理（$n \geq 2$ 时）：
$$
n = \sum_{k=0}^{n} \binom{n}{k} h_n^k \geq \binom{n}{2} h_n^2 = \frac{n(n-1)}{2} h_n^2.
$$

故 $h_n^2 \leq \tfrac{2}{n - 1}$，即 $0 \leq h_n \leq \sqrt{\tfrac{2}{n - 1}}$。

而 $0 \to 0$ 且 $\sqrt{2 / (n - 1)} \to 0$。由 [[ANL-THM-005]]，$h_n \to 0$，
从而 $\sqrt[n]{n} = 1 + h_n \to 1$。$\blacksquare$

## 关键技巧

- **绝对值消振荡**：$\sin / \cos$ 类振荡因子用 $|\cdot| \leq 1$ 转化为夹逼上界。
- **二项式控误差**：处理 $\sqrt[n]{a_n}$ 类极限的标准手法——设 $a_n = 1 + h_n$（或 $a_n = 1 - h_n$），用二项式从下方 / 上方提取主项。
- **从两端逼近 $L$**：构造夹逼时，下界 $a_n$ 与上界 $c_n$ 必须**都收敛于同一具体值** $L$。

## 变式

- **变式 1**：求 $\displaystyle \lim_{n \to \infty} \sqrt[n]{a}$（$a > 0$）。提示：分 $a > 1, a = 1, 0 < a < 1$ 三种情形。
- **变式 2**：求 $\displaystyle \lim_{n \to \infty} \frac{n}{2^n}$。提示：用 $2^n = (1 + 1)^n \geq \binom{n}{2}$。
- **变式 3**：证明 $\displaystyle \lim_{n \to \infty} \frac{\cos n + n^2}{n^2} = 1$。提示：把 $\cos n / n^2$ 单独夹逼到 0。
