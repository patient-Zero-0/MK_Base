---
title: "函数极限的 Heine 等价定理（完整版）"
type: theorem
id: ANL-THM-012
subject: analysis
chapter: 02-continuity
tags:
  - 函数极限
  - Heine
  - 数列
depends:
  - ANL-DEF-008
  - ANL-DEF-010
  - ANL-DEF-004
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §3.1"
difficulty: 3
related:
  - ANL-EX-004
applications:
  - "实变函数：极限的可数刻画"
  - "证明极限不存在的标准武器"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件与结论

设 $f$ 在 $x_0$ 的某去心邻域内有定义。下列两条**严格等价**：

1. **ε-δ 极限**（[[ANL-DEF-008]]）：$\displaystyle \lim_{x \to x_0} f(x) = L$。

2. **Heine 数列刻画**（[[ANL-DEF-010]]）：对任何满足
   $$
   x_n \to x_0 \quad \text{且} \quad x_n \neq x_0 \ (\forall n)
   $$
   的数列 $\{x_n\}$，都有 $f(x_n) \to L$（按 [[ANL-DEF-004]]）。

[[ANL-DEF-010]] 中已陈述此原则；本定理给出**完整证明**及标准应用。

## 直觉理解

ε-δ 视角："$x$ **连续地**接近 $x_0$ 时函数行为"。
Heine 视角："**任何离散路径**接近 $x_0$ 时函数行为"。

两条路径的等价性 = "连续逼近的全体行为，被任意离散路径完全采样"。

> 形象地说：把"$x \to x_0$"想成一束所有接近 $x_0$ 的轨迹。
> ε-δ 直接刻画整束的极限性质；
> Heine 把这束分解成无穷条数列轨迹，要求每条都到达同一终点 $L$。
> 这两种描述对应于"同一个连续过程"的两种数学语言。

## 完整证明

### （1 ⇒ 2）

设 $\lim_{x \to x_0} f(x) = L$，$\{x_n\}$ 满足 $x_n \to x_0, x_n \neq x_0$。

任给 $\varepsilon > 0$。

由 (1)：$\exists \delta > 0, \forall x : 0 < |x - x_0| < \delta \implies |f(x) - L| < \varepsilon$。

由 $x_n \to x_0$ 且 $x_n \neq x_0$：$\exists N, \forall n > N : 0 < |x_n - x_0| < \delta$。

故 $\forall n > N : |f(x_n) - L| < \varepsilon$，即 $f(x_n) \to L$。$\blacksquare$

### （2 ⇒ 1，反证）

设 (1) 不成立。则
$$
\exists \varepsilon_0 > 0, \forall \delta > 0, \exists x_\delta : 0 < |x_\delta - x_0| < \delta \text{ 但 } |f(x_\delta) - L| \geq \varepsilon_0.
$$

对每 $n \in \mathbb{N}^*$，取 $\delta = 1/n$，得到 $x_n$ 满足 $0 < |x_n - x_0| < 1/n$ 但 $|f(x_n) - L| \geq \varepsilon_0$。

构造完毕的 $\{x_n\}$ 满足 $x_n \to x_0$（由 $|x_n - x_0| < 1/n \to 0$）且 $x_n \neq x_0$。
但 $f(x_n) \not\to L$（因为 $|f(x_n) - L| \geq \varepsilon_0$ 对所有 $n$ 成立），与 (2) 矛盾。$\blacksquare$

## 用 Heine 证明极限不存在的标准套路

**步骤**：

1. 选两个不同的数列 $\{x_n\}, \{y_n\}$，都 $\to x_0$（且都 $\neq x_0$）。
2. 计算 $f(x_n)$ 和 $f(y_n)$，证明它们收敛于**不同**的极限 $L_1 \neq L_2$。
3. 由 Heine 反向：若 $\lim_{x \to x_0} f(x) = L$ 存在，则 $L = L_1$ 也 $L = L_2$，矛盾。

**例：$\lim_{x \to 0^+} \sin(1/x)$ 不存在**

- 取 $x_n = \tfrac{1}{n\pi} \to 0^+$：$f(x_n) = \sin(n\pi) = 0 \to 0$
- 取 $y_n = \tfrac{2}{(4n+1)\pi} \to 0^+$：$f(y_n) = \sin(\tfrac{(4n+1)\pi}{2}) = 1 \to 1$

两个数列像收敛到不同极限 ⇒ 原极限不存在。

## 常见错误

- ✗ **用单一收敛数列证明极限存在**。
  这只是必要条件。极限存在要求**所有**满足条件的数列像都收敛到同一 $L$。
- ✗ **遗漏 $x_n \neq x_0$ 条件**。
  若允许 $x_n = x_0$，等价定理对应的不再是极限而是"序列连续性"。
- ✗ **把数列像 $f(x_n)$ 与 $f$ 的"在 $x_n$ 处的取值"混淆**。
  Heine 关心的是**像数列**作为整体的极限，与每个 $f(x_n)$ 的具体形态无关。

## 链接

- 前置：[[ANL-DEF-008]]、[[ANL-DEF-010]]、[[ANL-DEF-004]]
- 应用例题：[[ANL-EX-004]] 用 Heine 证明极限不存在

## 跨专业应用

- **实变函数**：极限的可数刻画——用收敛数列的可数族刻画函数行为，是测度论的初阶基础
- **拓扑学**：序列连续与拓扑连续的等价性（在第一可数空间中成立）
