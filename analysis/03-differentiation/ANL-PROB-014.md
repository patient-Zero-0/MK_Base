---
title: "Jensen 不等式与 AM-GM、幂平均不等式"
type: problem
id: ANL-PROB-014
subject: analysis
chapter: 03-differentiation
tags:
  - 微分
  - 凸性
  - 不等式
  - Jensen
depends:
  - ANL-DEF-019
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §6.4 综合习题"
difficulty: 4
tests:
  - ANL-DEF-019
related:
  - ANL-DEF-019
  - ANL-EX-010
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

1. **Jensen 不等式（离散版）**：设 $f : I \to \mathbb{R}$ 为凸函数（[[ANL-DEF-019]]）。证明：对任意 $x_1, \ldots, x_n \in I$ 与权重 $\lambda_1, \ldots, \lambda_n \geq 0$ 满足 $\sum_{i=1}^n \lambda_i = 1$，
    $$ f\left( \sum_{i=1}^n \lambda_i x_i \right) \leq \sum_{i=1}^n \lambda_i f(x_i). $$

2. **AM-GM 不等式**：用 Jensen 推出对任意 $x_1, \ldots, x_n > 0$，
    $$ \frac{x_1 + x_2 + \cdots + x_n}{n} \geq \sqrt[n]{x_1 x_2 \cdots x_n}. $$

3. **幂平均不等式**：对 $a, b > 0$ 与 $p \geq 1$，证明
    $$ \left( \frac{a + b}{2} \right)^p \leq \frac{a^p + b^p}{2}. $$

## 提示

<details><summary>点击展开提示</summary>

- **第 1 题**：对 $n$ 归纳。$n = 2$ 是凸函数定义本身。从 $n$ 到 $n+1$：把首 $n$ 个权重归一化后用归纳假设，再用 $n=2$ 凸性合并。
- **第 2 题**：取 $f(x) = -\ln x$（在 $(0, +\infty)$ 上凸），$\lambda_i = 1/n$。Jensen 给出 $-\ln(\bar x) \leq -\frac{1}{n} \sum \ln x_i$，即 $\ln(\bar x) \geq \frac{1}{n} \sum \ln x_i = \ln \sqrt[n]{\prod x_i}$。两边取指数。
- **第 3 题**：$f(x) = x^p$ 在 $(0, +\infty)$ 上凸（$p \geq 1$ 时 $f''(x) = p(p-1)x^{p-2} \geq 0$），直接 $n = 2$ 凸性。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题：Jensen 不等式归纳证明

**证明（对 $n$ 归纳）**：

**$n = 2$**：恰为 $f$ 凸函数定义（[[ANL-DEF-019]]）：$f(\lambda_1 x_1 + \lambda_2 x_2) \leq \lambda_1 f(x_1) + \lambda_2 f(x_2)$。

**$n \to n + 1$**：设结论对 $n$ 成立。给定 $x_1, \ldots, x_{n+1} \in I$ 与 $\lambda_1, \ldots, \lambda_{n+1} \geq 0$，$\sum \lambda_i = 1$。

不妨设 $\lambda_{n+1} \in [0, 1)$（$\lambda_{n+1} = 1$ 时其余 $\lambda_i = 0$，结论平凡）。设 $\Lambda := 1 - \lambda_{n+1} = \sum_{i=1}^n \lambda_i > 0$。

**关键改写**：
$$
\sum_{i=1}^{n+1} \lambda_i x_i = \Lambda \cdot \underbrace{\sum_{i=1}^n \frac{\lambda_i}{\Lambda} x_i}_{=: \bar x} + \lambda_{n+1} x_{n+1}.
$$

注意 $\dfrac{\lambda_i}{\Lambda}$（$i = 1, \ldots, n$）非负且和为 $1$，故 $\bar x \in I$（$I$ 区间，凸集）。

**应用 $n = 2$ 凸性**（权重 $\Lambda + \lambda_{n+1} = 1$）：
$$
f\left( \sum_{i=1}^{n+1} \lambda_i x_i \right) = f(\Lambda \bar x + \lambda_{n+1} x_{n+1}) \leq \Lambda f(\bar x) + \lambda_{n+1} f(x_{n+1}).
$$

**应用 $n$ 归纳假设**于 $\bar x$（权重 $\dfrac{\lambda_i}{\Lambda}$ 非负且和为 $1$）：
$$
f(\bar x) \leq \sum_{i=1}^n \frac{\lambda_i}{\Lambda} f(x_i).
$$

代入：
$$
f\left( \sum_{i=1}^{n+1} \lambda_i x_i \right) \leq \Lambda \cdot \sum_{i=1}^n \frac{\lambda_i}{\Lambda} f(x_i) + \lambda_{n+1} f(x_{n+1}) = \sum_{i=1}^{n+1} \lambda_i f(x_i). \quad\blacksquare
$$

### 第 2 题：AM-GM 不等式

**证明**：取 $f(x) = -\ln x$ 于 $(0, +\infty)$。由 $f''(x) = \dfrac{1}{x^2} > 0$（[[ANL-DEF-019]] 二阶导判定），$f$ 在 $(0, +\infty)$ 上严格凸。

对 $x_1, \ldots, x_n > 0$ 取等权重 $\lambda_i = \dfrac{1}{n}$，由第 1 题 Jensen：
$$
-\ln\left( \frac{x_1 + \cdots + x_n}{n} \right) \leq \frac{1}{n} \sum_{i=1}^n (-\ln x_i) = -\frac{1}{n} \ln(x_1 \cdots x_n) = -\ln \sqrt[n]{x_1 \cdots x_n}.
$$

两边取负后再取指数（$\ln$ 单调）：
$$
\frac{x_1 + \cdots + x_n}{n} \geq \sqrt[n]{x_1 x_2 \cdots x_n}. \quad\blacksquare
$$

> 等号成立 $\iff$ $-\ln$ 严格凸条件下所有 $x_i$ 相等。

### 第 3 题

**证明**：取 $f(x) = x^p$ 于 $(0, +\infty)$。

**$p > 1$**：$f''(x) = p(p-1) x^{p-2} > 0$ ⇒ $f$ 严格凸（[[ANL-DEF-019]]）。

**$p = 1$**：$f(x) = x$ 是线性函数，**既凸又凹**（不等式取等号）。

由 $f$ 凸，对 $a, b > 0$ 与权重 $\lambda_1 = \lambda_2 = 1/2$ 的 Jensen：
$$
f\left( \frac{a+b}{2} \right) \leq \frac{1}{2} f(a) + \frac{1}{2} f(b),
$$
即
$$
\left( \frac{a+b}{2} \right)^p \leq \frac{a^p + b^p}{2}. \quad\blacksquare
$$

> **几何含义**：算术平均 $\dfrac{a+b}{2}$ 经过凸映射 $x^p$ 后变小（$\leq$）；
> 而映射后再算术平均反而变大。这就是 Jensen 的视觉：**"凸映射会把弦压低"**。
> 当 $p < 1$（且 $> 0$）时 $x^p$ 凹，不等号反转。

</details>

## 考察点

- [[ANL-DEF-019]] 凸函数的定义与归纳推广
- 凸函数的二阶导判定 $f'' \geq 0$ 的应用
- 经典不等式（AM-GM、幂平均）的统一推导框架
- 选择合适凸函数 $f$（取 $\ln, x^p, e^x$ 等）"翻译"目标不等式

## 备注

**Jensen 不等式的"统一武器"性质**：

| 选择 $f$ | Jensen 给出 |
|---|---|
| $f(x) = -\ln x$（凸） | AM-GM：$\overline{x_i} \geq \sqrt[n]{\prod x_i}$ |
| $f(x) = x^p$（$p > 1$ 凸） | 幂平均不等式 $\overline{x_i}^p \leq \overline{x_i^p}$ |
| $f(x) = e^x$（凸） | $e^{\overline{x_i}} \leq \overline{e^{x_i}}$ |
| $f(x) = -\ln x$ + 概率分布 | 信息论基本不等式 $D_{\text{KL}}(p \| q) \geq 0$ |
| $f(x) = x \ln x$（凸 on $(0, \infty)$） | 熵的次可加性 |

**进一步推广**：

- **连续版 Jensen**：$f$ 凸，$X$ 随机变量 ⇒ $f(E[X]) \leq E[f(X)]$（概率论标配）
- **加权版**：权重不需等分，仅需非负 + 和为 $1$
- **多元版**：$f : \mathbb{R}^n \to \mathbb{R}$ 凸时类似
