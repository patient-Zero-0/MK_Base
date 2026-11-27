---
title: "反常积分（无穷限）"
type: definition
id: ANL-DEF-029
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 反常积分
  - 无穷限
depends:
  - ANL-DEF-026
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §11.1"
difficulty: 3
related:
  - ANL-DEF-030
  - ANL-THM-035
applications:
  - "概率论：连续随机变量在 $(-\\infty, +\\infty)$ 上的分布与期望"
  - "物理：电场势 / 引力势的无穷远处计算"
  - "工程：长直导线 / 半无限介质问题"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述

### 上限为正无穷

设 $f$ 在 $[a, T]$ 上对**每个** $T > a$ 都 Riemann 可积（[[ANL-DEF-026]]）。**反常积分**
$$
\int_a^{+\infty} f(x) \, dx := \lim_{T \to +\infty} \int_a^T f(x) \, dx.
$$

若上述极限**存在**且**有限**，称反常积分**收敛**，其值即极限值；否则称**发散**。

### 下限为负无穷

类似地：
$$
\int_{-\infty}^b f(x) \, dx := \lim_{T \to -\infty} \int_T^b f(x) \, dx.
$$

### 双侧无穷

$$
\int_{-\infty}^{+\infty} f(x) \, dx := \int_{-\infty}^c f(x) \, dx + \int_c^{+\infty} f(x) \, dx,
$$
其中 $c \in \mathbb{R}$ 任意。**两边都收敛**才称双侧反常积分收敛——$c$ 的具体取值不影响结论。

> **重要**：$\int_{-\infty}^{+\infty}$ 收敛**不是** $\lim_{T \to \infty} \int_{-T}^T f$。
> 后者称为**主值积分**（Cauchy principal value），与本定义不一致。
> 反例：$f(x) = x$ 时主值为 $0$，但 $\int_0^\infty x \, dx$ 与 $\int_{-\infty}^0 x \, dx$ 都发散——故双侧反常积分发散。

## 经典：p-判别（无穷限）

> $\displaystyle \int_1^{+\infty} \frac{1}{x^p} \, dx$
> 收敛 $\iff p > 1$，且收敛值为 $\dfrac{1}{p - 1}$。

**证明**：对 $p \neq 1$，$\int_1^T \dfrac{dx}{x^p} = \dfrac{x^{1-p}}{1-p} \big|_1^T = \dfrac{T^{1-p} - 1}{1-p}$。

- $p > 1$：$T^{1-p} = T^{-(p-1)} \to 0$，故收敛于 $\dfrac{0 - 1}{1 - p} = \dfrac{1}{p-1}$
- $p < 1$：$T^{1-p} \to +\infty$，发散
- $p = 1$：$\int_1^T \dfrac{dx}{x} = \ln T \to +\infty$，发散 $\blacksquare$

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 定积分（[[ANL-DEF-026]]） | 有限闭区间 + 有界函数 |
| 反常积分（无穷限） | 区间无界（含 $\pm\infty$ 端点）+ 有限函数 |
| 反常积分（瑕积分，[[ANL-DEF-030]]） | 有限区间 + 函数无界 |
| 主值积分 (PV) | 对称取极限，比反常积分宽松 |

## 直觉理解

> 反常积分是"**把无穷区间用有限区间逼近，再取极限**"。
> 关键问题是：极限是否存在？是否有限？
>
> **几何画面**：曲线 $y = f(x)$ 与 $x$ 轴在 $[a, +\infty)$ 之间所夹"无穷长"的面积。
> 若曲线衰减得**够快**（如 $1/x^p$ with $p > 1$），无穷区域的面积仍是有限值；
> 若衰减不够快（$1/x$、$1/x^p$ with $p \leq 1$），面积"积累成无穷"。
>
> **临界**：$1/x$ 是分水岭——比 $1/x$ 衰减快即收敛，慢则发散。

## 性质

收敛的反常积分继承定积分的大部分性质（[[ANL-THM-029]]）：

- **线性性**：$\int_a^\infty (\alpha f + \beta g) = \alpha \int f + \beta \int g$（若两侧反常积分都收敛）
- **区间可加性**：$\int_a^\infty f = \int_a^c f + \int_c^\infty f$
- **单调性**：$f \leq g \Rightarrow \int f \leq \int g$（在收敛前提下）
- **绝对收敛**：若 $\int |f|$ 收敛，则 $\int f$ 收敛（反之不成立——见 [[ANL-EX-015]] $\int \sin x / x$）

## 链接

- 前置：[[ANL-DEF-026]] Riemann 可积
- 关联：[[ANL-DEF-030]] 瑕积分（另一种"反常"）
- 判别工具：[[ANL-THM-035]] 反常积分收敛判别
- 应用：[[ANL-EX-014]] Γ 函数、[[ANL-EX-015]] $\int \sin x / x$

## 跨专业应用

- **概率论**：正态分布 $\int_{-\infty}^{+\infty} \dfrac{1}{\sqrt{2\pi}} e^{-x^2/2} dx = 1$ 是无穷限反常积分
- **物理**：库仑势 $V = \int q/r^2 \, dr$ 在 $r \to \infty$ 处收敛（$1/r$ 衰减恰好是临界，$1/r^2$ 比临界快一阶）
- **工程**：Laplace 变换 $\mathcal{L}[f](s) = \int_0^\infty f(t) e^{-st} dt$ 是反常积分
