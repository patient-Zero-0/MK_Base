---
title: "用定义计算幂函数的定积分"
type: example
id: ANL-EX-011
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - Riemann 和
  - 定义法
depends:
  - ANL-DEF-022
  - ANL-DEF-023
  - ANL-DEF-026
  - ANL-THM-027
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §9.1 例题"
difficulty: 3
illustrates:
  - ANL-DEF-026
related:
  - ANL-DEF-023
  - ANL-THM-032
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

直接由 Riemann 积分定义（[[ANL-DEF-026]]）计算
$$
\int_0^1 x^2 \, dx.
$$

要求用 Riemann 和的极限论证（**不**直接用 [[ANL-THM-032]] N-L 公式）。

## 分析

虽然 $\int_0^1 x^2 dx$ 可用 N-L 一秒得出 $1/3$，但本题旨在**展示定义如何工作**：

1. 取**等距分割** $P_n: x_i = i/n$（$i = 0, 1, \ldots, n$），$\Delta x_i = 1/n$
2. 选**右端点标记** $\xi_i = x_i = i/n$
3. 计算 Riemann 和 $S_n = \sum_{i=1}^n f(\xi_i) \Delta x_i = \sum_{i=1}^n (i/n)^2 \cdot (1/n)$
4. 用平方求和公式 $\sum_{i=1}^n i^2 = \dfrac{n(n+1)(2n+1)}{6}$ 化简
5. 取 $n \to \infty$ 极限得 $1/3$
6. **关键**：证明对**任意**分割与标记结果一致——这才是 Riemann 可积的精确含义。
   由 $f(x) = x^2$ 在 $[0, 1]$ 上**连续**（[[ANL-THM-027]] 保证可积），
   只需对一个特殊序列（等距 + 右端点）算出极限即可——其他分割与标记由可积性自动收敛到同一值。

## 证明 / 解答

**解：** $f(x) = x^2$ 在 $[0, 1]$ 上连续，由 [[ANL-THM-027]]，$f$ Riemann 可积。
故对任意分割 $P_n$（$\|P_n\| \to 0$）与任意标记，Riemann 和都收敛到同一极限 $\int_0^1 x^2 dx$。

**取等距分割 + 右端点标记**：$P_n: x_i = i/n$，$\xi_i = i/n$，$\Delta x_i = 1/n$。

Riemann 和：
$$
S_n = \sum_{i=1}^n \left( \frac{i}{n} \right)^2 \cdot \frac{1}{n} = \frac{1}{n^3} \sum_{i=1}^n i^2.
$$

代入平方求和公式 $\displaystyle \sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$：
$$
S_n = \frac{1}{n^3} \cdot \frac{n(n+1)(2n+1)}{6} = \frac{(n+1)(2n+1)}{6 n^2} = \frac{2n^2 + 3n + 1}{6 n^2}.
$$

化简：
$$
S_n = \frac{1}{3} + \frac{1}{2n} + \frac{1}{6n^2}.
$$

故
$$
\int_0^1 x^2 \, dx = \lim_{n \to \infty} S_n = \frac{1}{3}. \quad\blacksquare
$$

## 验证（用 Darboux 上下和夹逼）

> 严谨者通常希望验证：上下和都收敛到 $1/3$。

**下和**（左端点标记，对 $f$ 递增的函数等于下确界标记）：
$$
L_n = \sum_{i=1}^n \left( \frac{i-1}{n} \right)^2 \cdot \frac{1}{n} = \frac{1}{n^3} \sum_{i=0}^{n-1} i^2 = \frac{(n-1)n(2n-1)}{6 n^3} \to \frac{1}{3}.
$$

**上和**（右端点 = 上确界，由 $f$ 递增）：
$$
U_n = S_n = \frac{1}{n^3} \cdot \frac{n(n+1)(2n+1)}{6} \to \frac{1}{3}.
$$

$U_n - L_n = \dfrac{1}{n^3} \cdot \dfrac{[n(n+1)(2n+1) - (n-1)n(2n-1)]}{6} = \dfrac{1}{n^3} \cdot n^2 = \dfrac{1}{n} \to 0$，
故由 [[ANL-THM-026]] Darboux 准则确认可积，且两侧极限同为 $1/3$。$\blacksquare$

## 关键技巧

- **平方求和公式**：$\sum_{i=1}^n i^2 = \dfrac{n(n+1)(2n+1)}{6}$（高中代数 / 数学归纳法可证）
  类似地 $\sum_{i=1}^n i = \dfrac{n(n+1)}{2}$、$\sum_{i=1}^n i^3 = \left[\dfrac{n(n+1)}{2}\right]^2$
- **等距分割是计算 Riemann 和的标准选择**：让所有 $\Delta x_i$ 化为常数 $1/n$，可提到求和外部
- **"$\|P\| \to 0$"在等距分割下退化为"$n \to \infty$"**——把"分割模"问题转化为"自然数极限"问题

## 变式

- **变式 1**：用定义计算 $\int_0^1 x \, dx = 1/2$。提示：$\sum i = n(n+1)/2$
- **变式 2**：用定义计算 $\int_0^1 x^3 \, dx = 1/4$。提示：$\sum i^3 = [n(n+1)/2]^2$
- **变式 3**：用定义计算 $\int_a^b x^2 \, dx = (b^3 - a^3)/3$。提示：等距 $x_i = a + i(b-a)/n$
- **变式 4**：用定义计算 $\int_0^1 e^x \, dx = e - 1$。
  提示：$\xi_i = i/n$，Riemann 和 $\sum_{i=1}^n e^{i/n} \cdot (1/n)$ = $(1/n) \cdot \dfrac{e^{1/n}(e - 1)}{e^{1/n} - 1}$（等比求和）；
  用 $\dfrac{e^{1/n} - 1}{1/n} \to 1$（$n \to \infty$）
- **变式 5**：用定义计算 $\int_0^{\pi/2} \sin x \, dx = 1$。提示：用三角和差化积公式求和

## 反思

> 用定义计算积分**只在简单函数上可行**——一般函数的 Riemann 和形式未必能写成闭式。
> 这正凸显 [[ANL-THM-032]] **N-L 公式的价值**：将"求和取极限"转化为"找原函数取端点差"。
>
> 但是定义法仍重要：
>
> - 用于**理论**论证（如证明可积性、积分性质）
> - 用于**数值近似**（数值积分本质就是计算 Riemann 和）
> - 用于**理解原理**——离开了定义，N-L 公式就成了纯粹的"操作技巧"

## 链接

- 演示定义：[[ANL-DEF-026]] Riemann 可积
- 配合定义：[[ANL-DEF-023]] Riemann 和、[[ANL-DEF-022]] 分割
- 对比方法：[[ANL-THM-032]] N-L 公式（更快但脱离定义）
- 后续：[[ANL-EX-012]]、[[ANL-EX-013]] 用 N-L 与计算法则求积分
