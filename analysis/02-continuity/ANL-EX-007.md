---
title: "用 ε-δ 定义证明二次函数的极限"
type: example
id: ANL-EX-007
subject: analysis
chapter: 02-continuity
tags:
  - 极限
  - ε-δ
  - 例题
depends:
  - ANL-DEF-008
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §3.1 例 3"
difficulty: 2
illustrates:
  - ANL-DEF-008
related:
  - ANL-PROB-031
---

## 题目

> 利用函数极限的 ε-δ 定义证明 $\displaystyle \lim_{x \to 2} x^2 = 4$。

## 分析

> 目标是把 $|x^2 - 4|$ 用 $|x - 2|$ 控住。

由 $x^2 - 4 = (x - 2)(x + 2)$，立刻有
$$
|x^2 - 4| = |x - 2| \cdot |x + 2|.
$$

困难在于因子 $|x + 2|$ 不被自身控住——它取决于 $x$。
**关键观察**：在 $x_0 = 2$ 附近，$|x + 2|$ 是有界的。
若先**预先约束** $|x - 2| < 1$，则 $1 < x < 3$，从而 $|x + 2| < 5$。
于是 $|x^2 - 4| < 5|x - 2|$。再让 $5|x - 2| < \varepsilon$ 即 $|x - 2| < \varepsilon / 5$。

合并两层约束：取 $\delta = \min\{1, \varepsilon / 5\}$。

> 这是 ε-δ 证明的标准技巧——**"先用一个临时半径限制 $x$ 范围以控制噪声因子，再由 ε 决定真正的 δ"**。

## 证明

**解：** 任给 $\varepsilon > 0$。取 $\delta = \min\{1, \varepsilon / 5\} > 0$。
对任何满足 $0 < |x - 2| < \delta$ 的 $x$：

由 $|x - 2| < 1$，知 $1 < x < 3$，故 $|x + 2| < 5$。

因此
$$
|x^2 - 4| = |x - 2| \cdot |x + 2| < |x - 2| \cdot 5 \leq 5 \cdot \frac{\varepsilon}{5} = \varepsilon.
$$

依 [[ANL-DEF-008]]，$\displaystyle \lim_{x \to 2} x^2 = 4$。$\blacksquare$

## 关键技巧

- **双层 δ 取 min**：第一层（如 $\delta \leq 1$）用来控制噪声因子的范围，第二层用来满足 ε 要求。
- **因式分解**：$|f(x) - L|$ 出现 $(x - x_0)$ 因式时，剩余因子常常可在邻域内有界化。
- **常数 5 不是唯一选择**：取 $\delta \leq 1/2$ 也能得 $|x + 2| < 4.5$，进而 $\delta = \min\{1/2, \varepsilon / 4.5\}$。技巧无标准答案，只要逻辑闭合。

## 变式

- **变式 1**：证明 $\displaystyle \lim_{x \to a} x^2 = a^2$ 对任意 $a \in \mathbb{R}$（提示：$|x + a| \leq |x - a| + 2|a|$，先约束 $|x - a| < 1$，得 $|x + a| < 2|a| + 1$）。
- **变式 2**：证明 $\displaystyle \lim_{x \to 0} \sin x = 0$（提示：$|\sin x| \leq |x|$，可直接取 $\delta = \varepsilon$）。
- **变式 3**：证明 $\displaystyle \lim_{x \to 1} 1/x = 1$（提示：先约束 $|x - 1| < 1/2$ 以保证 $x > 1/2$，再控制 $|1 - 1/x| = |x - 1|/|x|$）。
