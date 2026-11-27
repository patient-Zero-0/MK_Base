---
title: "用 Lagrange 中值定理证明经典不等式"
type: example
id: ANL-EX-010
subject: analysis
chapter: 03-differentiation
tags:
  - 微分
  - 不等式
  - 中值定理
depends:
  - ANL-THM-022
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §6.1 例题"
difficulty: 3
illustrates:
  - ANL-THM-022
related:
  - ANL-THM-022
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

用 [[ANL-THM-022]] Lagrange 中值定理证明下列经典不等式：

1. **对数夹逼**：对一切 $x > 0$，
    $$ \frac{x}{1+x} < \ln(1+x) < x. $$
2. **正弦 Lipschitz**：对任意 $a, b \in \mathbb{R}$，
    $$ |\sin a - \sin b| \leq |a - b|. $$
3. **指数线性下界**：对一切 $x \neq 0$，
    $$ e^x > 1 + x. $$

## 分析

每题的核心思路相同：**把不等式两端写成 $f(b) - f(a)$ 形式，再用 Lagrange 把它换成 $f'(\xi)(b-a)$，对 $\xi$ 所在区间估计 $f'$ 的范围**。

- **第 1 题**：$\ln(1+x) - \ln 1 = \ln(1+x)$，对应 $f(t) = \ln(1+t)$ 在 $[0, x]$ 上
- **第 2 题**：差直接套用 $f(t) = \sin t$，由 $|\cos| \leq 1$ 得 Lipschitz 常数 $1$
- **第 3 题**：$e^x - 1 = e^x - e^0$，对应 $f(t) = e^t$ 在 $[0, x]$ 或 $[x, 0]$；
  关键是分 $x > 0$ 与 $x < 0$ 讨论 $\xi$ 所处位置

## 证明 / 解答

### 第 1 题

**证明：** 设 $f(t) = \ln(1+t)$，$t \in [0, x]$。$f$ 连续可导，$f'(t) = \dfrac{1}{1+t}$。

由 [[ANL-THM-022]] Lagrange 中值定理，$\exists \xi \in (0, x)$ 使
$$
\ln(1+x) - \ln 1 = f'(\xi) \cdot (x - 0) = \frac{x}{1 + \xi}.
$$

由 $0 < \xi < x$，
$$
1 < 1 + \xi < 1 + x \implies \frac{1}{1+x} < \frac{1}{1+\xi} < 1.
$$

两端乘以 $x > 0$：
$$
\frac{x}{1+x} < \frac{x}{1+\xi} < x.
$$

代入 Lagrange 等式即得 $\dfrac{x}{1+x} < \ln(1+x) < x$。$\blacksquare$

### 第 2 题

**证明：** 不妨 $a \neq b$（$a = b$ 平凡）。设 $f(t) = \sin t$，应用 Lagrange 于 $[\min(a,b), \max(a,b)]$：
$$
\exists \xi \text{ 介于 } a, b \text{ 之间}: \quad \sin a - \sin b = \cos \xi \cdot (a - b).
$$

由 $|\cos \xi| \leq 1$，
$$
|\sin a - \sin b| = |\cos \xi| \cdot |a - b| \leq |a - b|. \quad\blacksquare
$$

> **拓展**：本不等式说明 $\sin$ 在 $\mathbb{R}$ 上 **Lipschitz 连续**，Lipschitz 常数为 $1$。
> 由此推出 $\sin$ 在 $\mathbb{R}$ 上**一致连续**（[[ANL-DEF-024]]）——
> 这是另一个独立证明，与 Cantor 定理形成对比（Cantor 仅适用于闭区间，$\sin$ 整个 $\mathbb{R}$ 上的一致连续来自 Lipschitz）。

### 第 3 题

**证明：** 设 $f(t) = e^t$。$f$ 在 $\mathbb{R}$ 上可导，$f'(t) = e^t$。

**情形 1：$x > 0$**。Lagrange 于 $[0, x]$：$\exists \xi \in (0, x)$ 使
$$
e^x - 1 = e^x - e^0 = e^\xi \cdot x.
$$
由 $\xi > 0$，$e^\xi > e^0 = 1$。故 $e^x - 1 = e^\xi \cdot x > 1 \cdot x = x$，即 $e^x > 1 + x$。

**情形 2：$x < 0$**。Lagrange 于 $[x, 0]$：$\exists \xi \in (x, 0)$ 使
$$
e^0 - e^x = e^\xi \cdot (0 - x) \implies e^x - 1 = -e^\xi \cdot (-x) = e^\xi \cdot x.
$$
由 $\xi < 0$，$e^\xi < 1$。又 $x < 0$，故 $e^\xi \cdot x > 1 \cdot x = x$（"较小的正数乘负数得较大的负数"）。
即 $e^x - 1 > x$，亦即 $e^x > 1 + x$。

合并两情形：$e^x > 1 + x$ 对一切 $x \neq 0$ 成立。$\blacksquare$

## 关键技巧

- **构造 $f(b) - f(a)$ 形式**：把不等式中的"对数 / 三角 / 指数"识别为某可导函数在端点的差
- **估计 $\xi$ 范围内 $f'$ 的取值**：$\xi$ 不可指定，但其所在的区间确定，故 $f'(\xi)$ 有明确的上下界
- **正负号讨论**：第 3 题 $x$ 正负影响 $\xi$ 范围与不等号方向，必须分情形
- **强弱不等式区分**：本例三题都是**严格**不等（$\xi$ 是开区间内点，$f'$ 严格递增/有界）

## 变式

- **变式 1**（第 1 题加强）：证明对一切 $-1 < x < 0$，
    $\dfrac{x}{1+x} > \ln(1+x) > x$（不等号方向反转！）
    提示：当 $x < 0$ 时 $\xi \in (x, 0)$，$1+\xi \in (1+x, 1) \subset (0, 1)$，$1/(1+\xi) > 1$。

- **变式 2**：证明 $\arctan x < x$（$x > 0$）。提示：$f(t) = \arctan t$，$f'(t) = 1/(1+t^2) < 1$（$t > 0$）。

- **变式 3**：证明对 $0 < a < b$，$\dfrac{b-a}{b} < \ln \dfrac{b}{a} < \dfrac{b-a}{a}$。
    提示：$\ln(b/a) = \ln b - \ln a$，对 $\ln$ 用 Lagrange。

- **变式 4**：证明对 $x > 0$，$\dfrac{x}{1+x} \leq 1 - e^{-x} \leq x$。
    提示：对 $f(t) = 1 - e^{-t}$ 用 Lagrange 或直接用第 3 题 $e^x \geq 1+x$ 改写。

## 链接

- 演示定理：[[ANL-THM-022]] Lagrange 中值定理
- 进阶：[[ANL-THM-025]] Taylor 公式给出更精细的不等式（更高阶余项）
- 应用：[[ANL-PROB-012]]、[[ANL-PROB-013]]、[[ANL-PROB-014]]
