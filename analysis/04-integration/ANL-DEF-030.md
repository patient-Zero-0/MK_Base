---
title: "反常积分（瑕积分 / 无界函数）"
type: definition
id: ANL-DEF-030
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 反常积分
  - 瑕积分
depends:
  - ANL-DEF-026
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §11.2"
difficulty: 3
related:
  - ANL-DEF-029
  - ANL-THM-035
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述

设 $f : (a, b] \to \mathbb{R}$（或 $[a, b)$），$f$ 在 $a$ 附近**无界**——即 $\displaystyle \lim_{x \to a^+} |f(x)| = +\infty$。
此时称 $a$ 为 $f$ 的**瑕点**（singular point）。
设 $f$ 在 $[a + \varepsilon, b]$ 上对**每个** $\varepsilon > 0$ 都 Riemann 可积（[[ANL-DEF-026]]）。**瑕积分**
$$
\int_a^b f(x) \, dx := \lim_{\varepsilon \to 0^+} \int_{a + \varepsilon}^b f(x) \, dx.
$$

若极限存在且有限，称瑕积分**收敛**；否则**发散**。

### 瑕点在右端点

类似地：
$$
\int_a^b f(x) \, dx := \lim_{\varepsilon \to 0^+} \int_a^{b - \varepsilon} f(x) \, dx.
$$

### 瑕点在内部

若 $c \in (a, b)$ 是瑕点：
$$
\int_a^b f \, dx := \int_a^c f \, dx + \int_c^b f \, dx,
$$
其中右边两个分别是相应端点处的瑕积分。**两边都收敛**才称内点瑕积分收敛。

> 与无穷限反常积分（[[ANL-DEF-029]]）的双侧收敛要求完全平行。

## 经典：p-判别（瑕积分）

> $\displaystyle \int_0^1 \frac{1}{x^p} \, dx$
> 收敛 $\iff p < 1$，且收敛值为 $\dfrac{1}{1 - p}$。

**证明**：对 $p \neq 1$，$\int_\varepsilon^1 \dfrac{dx}{x^p} = \dfrac{x^{1-p}}{1-p} \big|_\varepsilon^1 = \dfrac{1 - \varepsilon^{1-p}}{1 - p}$。

- $p < 1$：$\varepsilon^{1-p} \to 0$（$\varepsilon \to 0^+$），故收敛于 $\dfrac{1}{1-p}$
- $p > 1$：$\varepsilon^{1-p} = \varepsilon^{-(p-1)} \to +\infty$，发散
- $p = 1$：$\int_\varepsilon^1 \dfrac{dx}{x} = -\ln \varepsilon \to +\infty$，发散 $\blacksquare$

> **关键对比**（与 [[ANL-DEF-029]] 无穷限的 p-判别恰好**反向**）：
>
> | 形式 | 收敛条件 |
> |---|---|
> | $\int_1^{+\infty} \dfrac{1}{x^p} dx$ | $p > 1$ |
> | $\int_0^1 \dfrac{1}{x^p} dx$ | $p < 1$ |
>
> 直觉：瑕点处需衰减"够慢"（$p$ 小），无穷处需衰减"够快"（$p$ 大）。

## 与相近概念的区别

| 概念 | 区间 | 函数 |
|---|---|---|
| 定积分（[[ANL-DEF-026]]） | 有限 | 有界 |
| 反常积分（无穷限，[[ANL-DEF-029]]） | 无界 | 有界（在每个有限子区间上） |
| 瑕积分（本条目） | 有限 | 在某点附近无界 |

## 直觉理解

> 瑕积分是"**避开瑕点取极限**"——从 $a + \varepsilon$ 出发计算定积分（$f$ 在 $[a + \varepsilon, b]$ 上有界可积），
> 然后让 $\varepsilon \to 0^+$ 看是否收敛。
>
> **几何画面**：曲线 $y = f(x)$ 在瑕点附近"飙到无穷"，曲线下方面积可能是有限或无穷。
> 若 $f$ 在瑕点附近**奇异度不太强**（如 $1/x^p$ with $p < 1$），尽管函数无界，所夹面积仍有限；
> 反之（如 $1/x$、$1/x^2$）面积无穷。
>
> **临界**：$p = 1$ 是分水岭——$1/x$ 在 $0$ 附近发散。

## 复合反常积分

若区间**既无穷又含瑕点**（例如 $\int_0^{+\infty}$ + $f$ 在 $0$ 附近无界），
需把区间拆为多段，每段单独处理。

**Γ 函数即此例**：
$$
\Gamma(s) := \int_0^{+\infty} x^{s-1} e^{-x} \, dx = \int_0^1 + \int_1^{+\infty}.
$$

- $\int_0^1 x^{s-1} e^{-x} dx$：瑕积分，$x \to 0^+$ 时 $\sim x^{s-1}$，由 $p$-判别收敛 $\iff s > 0$
- $\int_1^{+\infty} x^{s-1} e^{-x} dx$：无穷限，$x \to \infty$ 时被 $e^{-x}$ 控制，**对一切实 $s$ 收敛**
- 合并：$\Gamma(s)$ 收敛 $\iff s > 0$（详见 [[ANL-EX-014]]）

## 链接

- 前置：[[ANL-DEF-026]] Riemann 可积
- 平行概念：[[ANL-DEF-029]] 反常积分（无穷限）
- 判别工具：[[ANL-THM-035]] 反常积分收敛判别
- 应用：[[ANL-EX-014]] Γ 函数（含瑕 + 无穷限的复合反常积分）
