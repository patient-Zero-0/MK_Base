---
title: "Dirichlet 积分的收敛性"
type: example
id: ANL-EX-015
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 反常积分
  - 条件收敛
  - Dirichlet
depends:
  - ANL-DEF-029
  - ANL-THM-035
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §11.1 例题"
difficulty: 4
illustrates:
  - ANL-THM-035
related:
  - ANL-EX-014
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

证明：

1. **收敛性**：$\displaystyle \int_0^{+\infty} \frac{\sin x}{x} \, dx$ **收敛**。
2. **非绝对收敛**：$\displaystyle \int_0^{+\infty} \left| \frac{\sin x}{x} \right| \, dx = +\infty$。

即 Dirichlet 积分**条件收敛**而非绝对收敛。

> **附注**（不需证明）：$\displaystyle \int_0^{+\infty} \dfrac{\sin x}{x} dx = \dfrac{\pi}{2}$。
> 严格证明需复分析（contour integral）或 Fourier 变换技术，超出本知识库 M2 范围。

## 分析

- **第 1 题**：被积函数在 $0$ 附近**有可去间断**——$\lim_{x \to 0} \sin x / x = 1$（[[ANL-EX-008]]），延拓为 $f(0) = 1$ 后连续，故 $[0, 1]$ 上的积分**不是反常的**。
  问题归于无穷限部分 $\int_1^{+\infty} \dfrac{\sin x}{x} dx$。
  对此用 [[ANL-THM-035]] **Dirichlet 判别**：
  - $f(x) = 1/x$ 单调递减到 $0$
  - $g(x) = \sin x$，部分和 $\int_1^T \sin x \, dx = \cos 1 - \cos T$ 有界（$\leq 2$）

- **第 2 题**：用周期性把 $\int |sin x|/x$ 拆为 $[k\pi, (k+1)\pi]$ 上的小段，
  每段积分 $\geq \dfrac{c}{k+1}$（某常数 $c$），整体下界为发散调和级数

## 证明 / 解答

### 第 1 题：收敛性

**Step 1**：$0$ 处可去（不需用反常积分定义）。
$$
\lim_{x \to 0} \frac{\sin x}{x} = 1 \quad ([[ANL-EX-008]]).
$$
延拓 $f(0) := 1$，$f$ 在 $[0, 1]$ 上连续 ⇒ $\int_0^1 f(x) dx$ 是普通定积分（[[ANL-THM-027]]）。

**Step 2**：$\int_1^{+\infty} \dfrac{\sin x}{x} dx$ 收敛（Dirichlet 判别）。

- $f(x) := 1/x$ 在 $[1, +\infty)$ 上**单调递减**且 $\lim_{x \to \infty} 1/x = 0$ ✓
- $g(x) := \sin x$，对所有 $T \geq 1$：$\left| \int_1^T \sin x \, dx \right| = |\cos 1 - \cos T| \leq |\cos 1| + 1 \leq 2$ —— 部分和**有界** ✓

由 [[ANL-THM-035]] **Dirichlet 判别**，$\int_1^{+\infty} \dfrac{\sin x}{x} dx$ 收敛。

**Step 3**：合并 $\int_0^{+\infty} = \int_0^1 + \int_1^{+\infty}$，两边都收敛，故 $\int_0^{+\infty} \dfrac{\sin x}{x} dx$ 收敛。$\blacksquare$

### 第 2 题：非绝对收敛

**目标**：$\int_0^{+\infty} \left| \dfrac{\sin x}{x} \right| dx = +\infty$。

**Step 1**：把无穷区间分成 $\pi$ 周期段：
$$
\int_\pi^{+\infty} \left| \frac{\sin x}{x} \right| dx = \sum_{k=1}^{\infty} \int_{k\pi}^{(k+1)\pi} \left| \frac{\sin x}{x} \right| dx.
$$

**Step 2**：对每段下界估计。
在 $[k\pi, (k+1)\pi]$ 上 $1/x \geq \dfrac{1}{(k+1)\pi}$；故
$$
\int_{k\pi}^{(k+1)\pi} \frac{|\sin x|}{x} dx \geq \frac{1}{(k+1)\pi} \int_{k\pi}^{(k+1)\pi} |\sin x| dx.
$$

由周期性 $\int_{k\pi}^{(k+1)\pi} |\sin x| dx = \int_0^\pi \sin x \, dx = 2$（无论 $k$ 奇偶，因 $|\sin|$ 周期 $\pi$）。
故
$$
\int_{k\pi}^{(k+1)\pi} \frac{|\sin x|}{x} dx \geq \frac{2}{(k+1)\pi}.
$$

**Step 3**：求和。
$$
\int_\pi^{+\infty} \frac{|\sin x|}{x} dx \geq \sum_{k=1}^\infty \frac{2}{(k+1)\pi} = \frac{2}{\pi} \sum_{k=2}^\infty \frac{1}{k} = +\infty
$$
（**调和级数** $\sum 1/k$ 发散）。

故 $\int_0^{+\infty} \left| \dfrac{\sin x}{x} \right| dx \geq \int_\pi^\infty \left| \dfrac{\sin x}{x} \right| dx = +\infty$。$\blacksquare$

## 关键技巧

- **检查"$0$ 是真瑕点还是可去"**：$\sin x / x$ 在 $0$ 处实际不奇异
- **Dirichlet 判别的精髓**：$g$ 不必收敛，**部分和有界**即可——这是处理"衰减 $\times$ 振荡"积分的标准工具
- **绝对收敛的破坏机制**："$|\sin x|$ 不变号"消除了振荡的"自抵消"，于是 $1/x$ 衰减不够快（恰为分水岭）就发散了
- **周期分段 + 调和级数下界**：证明发散性的常见模板

## 变式

- **变式 1**：证明 $\int_0^{+\infty} \dfrac{\cos x}{x^p} dx$ 收敛 $\iff 0 < p \leq 1$ 时**条件**收敛、$p > 1$ 时**绝对**收敛。
  提示：$0$ 处 $1/x^p$ 是瑕（$p > 0$），用 Dirichlet（无穷处）+ 比较（$0$ 处）
- **变式 2**：证明 $\int_0^{+\infty} \dfrac{\sin x}{\sqrt{x}} dx$ 收敛。提示：仍用 Dirichlet + $\int_0^1 1/\sqrt{x}$（瑕收敛）
- **变式 3**：证明 $\int_0^{+\infty} \sin(x^2) dx$ 收敛（**Fresnel 积分**）。
  提示：换元 $u = x^2$（$du = 2x\,dx$），化为 $\int_0^\infty \dfrac{\sin u}{2\sqrt{u}} du$，再用 Dirichlet
- **变式 4**：构造一个**收敛**但 **$f(x)$ 在 $\infty$ 处不趋于 $0$** 的反常积分。
  反例：$f$ 在 $[n, n + 1/n^2]$ 上为 $1$，其余为 $0$。$\int f \leq \sum 1/n^2 < \infty$，但 $f$ 不趋于 $0$。
  这与"级数收敛 ⇒ $a_n \to 0$"的不同——积分区域可以"瘦尖塔"

## 反思

> Dirichlet 积分是**条件收敛**的代表性案例。它说明：
>
> - **绝对收敛 ≠ 收敛**：积分可能因"振荡自抵消"而收敛，即使绝对值积分发散
> - **Dirichlet 判别 ≠ 比较判别**：处理无定号被积函数时，比较判别完全失效
> - **$\int_0^\infty \sin x / x = \pi/2$** 是分析学中最美的"非平凡定值"之一
>
> 同样的现象在级数中出现：$\sum (-1)^n / n$ 条件收敛但非绝对收敛——
> Dirichlet 判别在级数（[[ANL-THM-043]]）有完全平行的形式。

## 链接

- 演示定理：[[ANL-THM-035]] 反常积分判别法
- 配合：[[ANL-DEF-029]] 无穷限反常积分
- 关联：[[ANL-EX-008]] $\sin x / x$ 极限、[[ANL-EX-014]] 反常积分判别综合
- 进阶：积分值 $\pi/2$ 的复分析证明（contour integral，超出 M2 范围）
- 平行：级数版 Dirichlet 判别 [[ANL-THM-043]]
