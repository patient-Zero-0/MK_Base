---
title: "积分基本性质：线性性、区间可加性、单调性"
type: theorem
id: ANL-THM-029
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 线性性
  - 性质
depends:
  - ANL-DEF-026
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §9.4"
difficulty: 3
related:
  - ANL-DEF-026
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设 $f, g$ 在 $[a, b]$ 上 Riemann 可积（[[ANL-DEF-026]]）。

## 结论

### 性质 1：线性性

> 对任意常数 $\alpha, \beta \in \mathbb{R}$，$\alpha f + \beta g$ 在 $[a, b]$ 上可积，且
> $$
> \int_a^b (\alpha f + \beta g) = \alpha \int_a^b f + \beta \int_a^b g.
> $$

### 性质 2：区间可加性

> 对任意 $c \in [a, b]$，$f$ 在 $[a, c]$ 与 $[c, b]$ 上分别可积，且
> $$
> \int_a^b f = \int_a^c f + \int_c^b f.
> $$
>
> （记号扩展：对任意三点 $a, b, c$，无须 $a < c < b$，公式形式上仍成立——用 $\int_b^a := -\int_a^b$ 约定）

### 性质 3：单调性

> 若 $f(x) \leq g(x)$ 对几乎所有 $x \in [a, b]$ 成立（特别地，在所有 $x$ 处），则
> $$
> \int_a^b f \leq \int_a^b g.
> $$

### 性质 4：绝对可积与三角不等式

> $|f|$ 在 $[a, b]$ 上可积，且
> $$
> \left| \int_a^b f \right| \leq \int_a^b |f|.
> $$

### 性质 5：积分均值

> 设 $m \leq f(x) \leq M$ 对所有 $x \in [a, b]$ 成立。则
> $$
> m(b-a) \leq \int_a^b f \leq M(b-a).
> $$

## 几何/直觉理解

> 这些性质都是 Riemann 和的对应性质在极限下的体现：
>
> - **线性性**：$\sum (\alpha f + \beta g)(\xi_i) \Delta x_i = \alpha \sum f(\xi_i) \Delta x_i + \beta \sum g(\xi_i) \Delta x_i$，取极限即得
> - **区间可加性**：在 $c$ 处插入分割点不改变 Riemann 和；
>   把 $[a, b]$ 切成 $[a, c]$ + $[c, b]$ 两段独立处理
> - **单调性**：逐点 $f \leq g$ ⇒ $\sum f(\xi_i) \Delta x_i \leq \sum g(\xi_i) \Delta x_i$
> - **三角不等式**：$|\sum f(\xi_i) \Delta x_i| \leq \sum |f(\xi_i)| \Delta x_i$

## 证明

> 仅证最重要的两条；其余类似。

### 证明（线性性）

**证明：** 任取分割 $P$ 与标记 $\boldsymbol{\xi}$。
$$
S(\alpha f, P, \boldsymbol{\xi}) = \sum (\alpha f)(\xi_i) \Delta x_i = \alpha \sum f(\xi_i) \Delta x_i = \alpha \cdot S(f, P, \boldsymbol{\xi}).
$$

当 $\|P\| \to 0$，$S(f, P, \boldsymbol{\xi}) \to \int_a^b f$（[[ANL-DEF-026]]）。
故 $S(\alpha f, P, \boldsymbol{\xi}) \to \alpha \int_a^b f$，即 $\alpha f$ 可积且 $\int (\alpha f) = \alpha \int f$。$\blacksquare$

> 类似地，$f + g$ 可积且 $\int (f + g) = \int f + \int g$（用 Riemann 和的可加性 + 极限的可加性 [[ANL-THM-009]]）。

### 证明（绝对可积与三角不等式）

**证明（$|f|$ 可积）**：用 [[ANL-THM-026]] Darboux 准则。关键不等式：对任 $x, y$,
$$
\big| |f(x)| - |f(y)| \big| \leq |f(x) - f(y)| \quad (\text{反三角不等式}).
$$

故在子区间 $[x_{i-1}, x_i]$ 上：
$$
\omega_i(|f|) = \sup |f(x)| - \inf |f(x)| \leq \sup_{x, y} \big| |f(x)| - |f(y)| \big| \leq \sup_{x, y} |f(x) - f(y)| = \omega_i(f).
$$

由 $f$ 可积 + Darboux 准则，$\sum \omega_i(f) \Delta x_i$ 可任意小；故 $\sum \omega_i(|f|) \Delta x_i$ 也可任意小。
故 $|f|$ 可积。

**证明（三角不等式）**：由 $-|f| \leq f \leq |f|$ 与单调性（性质 3）：
$$
-\int_a^b |f| \leq \int_a^b f \leq \int_a^b |f|,
$$
即 $\big| \int f \big| \leq \int |f|$。$\blacksquare$

## 常见错误

- ✗ 误以为"$f, g$ 都可积 ⇒ $f \cdot g$ 可积"是平凡的。
  事实上 $f \cdot g$ **可积**（用 Darboux 准则 + $\omega_i(fg) \leq M (\omega_i(f) + \omega_i(g))$ 估计），
  但**不要试图给出**像线性性那样简单的"积分公式"——
  $\int fg \neq (\int f)(\int g)$ 一般成立！
- ✗ 把单调性反向应用："$\int f \leq \int g \Rightarrow f \leq g$"。
  反例：$f(x) = \sin(2\pi x)$, $g(x) = 0$ 在 $[0, 1]$ 上 $\int f = 0 = \int g$，但 $f \neq g$。
  积分仅刻画"整体平均"，不能反推逐点关系。
- ✗ 三角不等式误用方向："$\int |f| \leq |\int f|$"。
  正确方向是 $|\int f| \leq \int |f|$（"先取绝对值再积分**至少** = 先积分再取绝对值"）。
  反例：$f$ 一半正一半负完全抵消时 $\int f = 0$ 但 $\int |f| > 0$。

## 推论与应用

- **推论 1**：可积函数的有限线性组合仍可积（线性性归纳）
- **推论 2**：$|f - g|$ 可积，故"距离"$\int_a^b |f - g| \, dx$ 良定义——这是 $L^1$ 范数的基础
- **应用**：积分中值定理（[[ANL-THM-030]]）的证明用性质 5 的 $m, M$ 夹逼

## 链接

- 前置：[[ANL-DEF-026]] Riemann 可积
- 应用：[[ANL-THM-030]] 积分中值定理（用性质 5）
- 进阶：积分作为线性泛函——是泛函分析的入门视角
