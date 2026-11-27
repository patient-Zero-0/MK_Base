---
title: "反常积分敛散性判别（含 Γ 函数引入）"
type: example
id: ANL-EX-014
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 反常积分
  - Gamma 函数
depends:
  - ANL-DEF-029
  - ANL-DEF-030
  - ANL-THM-035
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §11.1, §11.2 例题"
difficulty: 4
illustrates:
  - ANL-THM-035
related:
  - ANL-EX-015
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

判定下列反常积分的敛散性。前两题练习 p-判别与比较判别（[[ANL-THM-035]]），后两题引入 **Γ 函数**：

1. $\displaystyle \int_1^{+\infty} \frac{1}{x^p} dx$（讨论 $p$）—— 已在 [[ANL-DEF-029]] 给出，用作工具
2. $\displaystyle \int_1^{+\infty} \frac{x}{1 + x^4} dx$
3. $\displaystyle \Gamma(s) := \int_0^{+\infty} x^{s-1} e^{-x} dx$（讨论 $s$ 取值范围）
4. $\displaystyle \int_0^{+\infty} e^{-x^2} dx$

## 分析

- **第 1 题**：直接 p-判别（[[ANL-DEF-029]]）—— 收敛 $\iff p > 1$
- **第 2 题**：识别"$1/x^3$ 量级衰减"，用极限形比较判别归约到 p-判别
- **第 3 题**：拆为 $[0, 1]$ 瑕积分（在 $0$ 附近 $\sim x^{s-1}$）+ $[1, +\infty)$ 无穷限（被 $e^{-x}$ 控制）—— 双判
- **第 4 题**：高斯积分。$x^2$ 增长够快，$e^{-x^2}$ 衰减极快——用比较判别归约到 $\int e^{-x}$

## 证明 / 解答

### 第 1 题（p-判别复习）

由 [[ANL-DEF-029]]，$\displaystyle \int_1^{+\infty} \dfrac{dx}{x^p}$ 收敛 $\iff p > 1$，且收敛值 $\dfrac{1}{p - 1}$。

### 第 2 题

**解：** 当 $x \to +\infty$，$\dfrac{x}{1 + x^4} \sim \dfrac{x}{x^4} = \dfrac{1}{x^3}$。
即
$$
\lim_{x \to +\infty} \frac{x/(1+x^4)}{1/x^3} = \lim_{x \to +\infty} \frac{x^4}{1+x^4} = 1.
$$

由 [[ANL-THM-035]] 极限形比较判别（$c = 1 \in (0, +\infty)$），$\int_1^\infty \dfrac{x}{1+x^4} dx$ 与 $\int_1^\infty \dfrac{1}{x^3} dx$ 同时收敛或同时发散。

由 $p$-判别（$p = 3 > 1$），$\int_1^\infty \dfrac{1}{x^3} dx$ 收敛。故原积分**收敛**。$\blacksquare$

### 第 3 题：Γ 函数收敛域

**解：** $\Gamma(s) = \int_0^1 x^{s-1} e^{-x} dx + \int_1^{+\infty} x^{s-1} e^{-x} dx$（拆点 $1$ 任意）。

**$\int_1^{+\infty} x^{s-1} e^{-x} dx$**：由 $e^{-x}$ 衰减极快，对**任何** $s \in \mathbb{R}$ 都收敛。
具体：$\lim_{x \to \infty} x^{s+1} \cdot x^{s-1} e^{-x} / 1 = \lim x^{s+1} \cdot \text{(decreasing)}$ 不严谨，
更精确地：取 $N \in \mathbb{Z}^+$ with $N > s - 1$，对 $x$ 充分大 $x^{s-1} e^{-x} \leq x^N e^{-x}$，
而 $\lim_{x \to \infty} x^N e^{-x} = 0$（指数衰减压制多项式）。
具体地有 $x^N e^{-x} \leq e^{-x/2}$ 对充分大 $x$，由比较 + $\int e^{-x/2}$ 收敛得本积分收敛。

**$\int_0^1 x^{s-1} e^{-x} dx$**：在 $0$ 附近 $e^{-x} \to 1$，故 $x^{s-1} e^{-x} \sim x^{s-1}$。

由 [[ANL-DEF-030]] 瑕积分 p-判别（瑕点在 $0$，$\int_0^1 x^{s-1} dx = \int_0^1 \dfrac{1}{x^{1-s}} dx$ 收敛 $\iff 1 - s < 1 \iff s > 0$）。

**合并**：$\Gamma(s)$ 收敛 $\iff s > 0$。$\blacksquare$

> **Γ 函数的关键性质**（仅声明，证明留作变式）：
>
> | 性质 | 表达式 |
> |---|---|
> | 递推 | $\Gamma(s+1) = s \, \Gamma(s)$（用分部积分） |
> | 阶乘推广 | $\Gamma(n+1) = n!$（$n \in \mathbb{N}$） |
> | 半整数 | $\Gamma(1/2) = \sqrt{\pi}$（用第 4 题 + 换元） |

### 第 4 题

**解：** $e^{-x^2}$ 在 $[0, +\infty)$ 上连续有界（$\leq 1$），唯一可能"反常"的是 $x \to +\infty$ 处。

**比较**：$x \geq 1$ 时 $x^2 \geq x$，故 $e^{-x^2} \leq e^{-x}$。

由 $\int_1^\infty e^{-x} dx = e^{-1}$（收敛）+ [[ANL-THM-035]] 比较判别，$\int_1^{+\infty} e^{-x^2} dx$ 收敛。

加上 $\int_0^1 e^{-x^2} dx$（普通定积分，$e^{-x^2}$ 在 $[0, 1]$ 连续），$\int_0^{+\infty} e^{-x^2} dx$ **收敛**。

> **附注**（不证）：$\int_0^{+\infty} e^{-x^2} dx = \dfrac{\sqrt{\pi}}{2}$（**高斯积分**）。
> 证明需用 $\left( \int e^{-x^2} dx \right)^2 = \iint e^{-(x^2+y^2)} dx dy$ + 极坐标——属多元积分（M2+ 范围）。
> 这与 $\Gamma(1/2) = \sqrt{\pi}$ 关联：换元 $x = \sqrt{t}$ 得 $\int_0^\infty e^{-x^2} dx = \dfrac{1}{2}\Gamma(1/2)$。

$\blacksquare$

## 关键技巧

- **极限形比较判别**：把复杂被积函数与"$1/x^p$ 标准件"配对，看比值极限
- **拆区间处理 Γ 函数**：含瑕 + 含无穷的反常积分必须**分两段**判别——任一段发散整个发散
- **指数衰减压制一切多项式**：对任意 $s$，$x^s e^{-x} \to 0$（$x \to \infty$）。这是处理 $e^{-x}$、$e^{-x^2}$ 类积分的杀手锏
- **"标准件"工具箱**：$\int_1^\infty 1/x^p$, $\int_0^1 1/x^p$, $\int_0^\infty e^{-x}$ 是判别工具

## 变式

- **变式 1**：判定 $\int_1^{+\infty} \dfrac{\ln x}{x^2} dx$。提示：$\ln x \leq x^{1/2}$（充分大 $x$），归约到 $\int 1/x^{3/2}$
- **变式 2**：证明 $\Gamma(s+1) = s \Gamma(s)$。提示：$\Gamma(s+1) = \int_0^\infty x^s e^{-x} dx$，分部积分（$u = x^s, dv = e^{-x} dx$）
- **变式 3**：用变式 2 + $\Gamma(1) = 1$ 推 $\Gamma(n+1) = n!$。
- **变式 4**：判定 $\int_0^{+\infty} \dfrac{\ln(1 + x^2)}{x^2} dx$。提示：$0$ 处 $\sim 1$（无瑕），$\infty$ 处 $\sim 2 \ln x / x^2$
- **变式 5**（综合）：$\int_0^{+\infty} \dfrac{1}{x^p (1 + x)^q} dx$ 收敛条件—— $0$ 处 $\sim 1/x^p$，$\infty$ 处 $\sim 1/x^{p+q}$，故收敛 $\iff p < 1$ **且** $p + q > 1$

## 链接

- 演示定理：[[ANL-THM-035]] 反常积分判别法
- 配合定义：[[ANL-DEF-029]]、[[ANL-DEF-030]]
- 后续：[[ANL-EX-015]] $\int \sin x / x$（条件收敛例）
- 进阶：高斯积分的二维 + 极坐标证法（多元积分）
