---
title: "L'Hospital 法则"
type: theorem
id: ANL-THM-024
subject: analysis
chapter: 03-differentiation
tags:
  - 微分
  - 极限
  - 不定式
depends:
  - ANL-DEF-014
  - ANL-DEF-008
  - ANL-THM-023
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §6.2"
difficulty: 4
related:
  - ANL-THM-023
  - ANL-THM-025
applications:
  - "数值分析：奇异点处的函数极限计算"
  - "物理：极限过程中的渐近行为分析"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件与结论

### 形式 1（0/0 型）

**条件**：设 $f, g$ 在 $(a, b)$（$a$ 可为 $-\infty$）内可导，且：

1. $\displaystyle \lim_{x \to a^+} f(x) = \lim_{x \to a^+} g(x) = 0$；
2. $g'(x) \neq 0$ 在 $(a, b)$ 上恒成立；
3. $\displaystyle \lim_{x \to a^+} \dfrac{f'(x)}{g'(x)} = L$（$L \in \mathbb{R} \cup \{+\infty, -\infty\}$）。

**结论**：
$$
\lim_{x \to a^+} \frac{f(x)}{g(x)} = L.
$$

### 形式 2（∞/∞ 型）

**条件**：把上面条件 1 替换为 $\displaystyle \lim_{x \to a^+} g(x) = +\infty$（或 $-\infty$），其余不变。

**结论**：同上。

> 双侧极限 $x \to a$、$x \to \pm\infty$ 等情形可类推；只需把条件中的单侧极限改成对应形式。

## 几何/直觉理解

> 当 $x \to a$ 时 $f \to 0$ 且 $g \to 0$，$f/g$ 的"局部行为"由两者**接近 $0$ 的速度**决定。
>
> 一阶 Taylor（[[ANL-THM-025]]）告诉我们：
> $f(x) \approx f'(a)(x - a)$ 与 $g(x) \approx g'(a)(x - a)$（设 $f, g$ 在 $a$ 处可导且 $f(a) = g(a) = 0$）。
> 故
> $$
> \frac{f(x)}{g(x)} \approx \frac{f'(a)(x-a)}{g'(a)(x-a)} = \frac{f'(a)}{g'(a)}.
> $$
> "比的极限 = 导数比的极限"——这就是 L'Hospital 的直觉。
>
> 法则的强大在于**不要求 $f, g$ 在 $a$ 处可导甚至有定义**——
> 仅需要 $f'/g'$ 的极限存在即可，证明用 Cauchy 中值定理。

## 证明

### 形式 1 证明（0/0 型，有限极限）

**证明：** 由条件 1，可把 $f, g$ 连续延拓到 $[a, b)$，定义 $f(a) = g(a) = 0$（这两个点的连续延拓由极限存在性保证）。

对任一 $x \in (a, b)$，$f, g$ 在 $[a, x]$ 上连续、在 $(a, x)$ 内可导，且 $g'$ 在 $(a, x)$ 内不为零。
由 [[ANL-THM-023]] Cauchy 中值定理，$\exists \xi \in (a, x)$ 使
$$
\frac{f(x) - f(a)}{g(x) - g(a)} = \frac{f'(\xi)}{g'(\xi)}.
$$

代入 $f(a) = g(a) = 0$：
$$
\frac{f(x)}{g(x)} = \frac{f'(\xi)}{g'(\xi)}.
$$

当 $x \to a^+$，由 $a < \xi < x$，由夹逼 $\xi \to a^+$。
由条件 3，$\dfrac{f'(\xi)}{g'(\xi)} \to L$。故
$$
\lim_{x \to a^+} \frac{f(x)}{g(x)} = L. \quad\blacksquare
$$

> 当 $a = -\infty$、$L = \pm\infty$、或 $\infty/\infty$ 型时，证明需作适当修改但思路相同。
> 详见教材 §6.2。

## 常见错误

- ✗ **盲目套用**：未先验证条件就求导分子分母。
  反例：$\displaystyle \lim_{x \to 0} \frac{\sin x}{x + 1} = \frac{0}{1} = 0$。这**不是** $0/0$ 型！
  错误用 L'Hospital 得 $\dfrac{\cos x}{1} \to 1 \neq 0$。
- ✗ **重复套用直至发散**。
  反例：$\displaystyle \lim_{x \to 0} \frac{x^2 \sin(1/x)}{\sin x}$ 是 $0/0$ 型，但
  $\dfrac{f'}{g'} = \dfrac{2x \sin(1/x) - \cos(1/x)}{\cos x}$，分子在 $0$ 处极限**不存在**（$\cos(1/x)$ 振荡）。
  此时 L'Hospital **结论不成立**——但**原极限**实际为 $0$（用 $\sin x \sim x$ 与夹逼）。
  这说明法则的条件 3 是**必要的**：导数比极限不存在时不能反推原极限不存在。
- ✗ **用于"非不定式"**。
  L'Hospital 仅处理 $0/0$ 与 $\infty/\infty$ 两种不定式（其他不定式如 $0 \cdot \infty$、$\infty - \infty$、$1^\infty$ 需先化为这两种）。
- ✗ **漏掉 $g'(x) \neq 0$ 条件**。
  反例：取 $g(x) = x^2 \sin(1/x)$（$x \neq 0$, $g(0) = 0$）。$g'$ 在 $0$ 任何邻域内有零点，
  L'Hospital 不适用，需另寻方法。

## 推论与应用

- **常见不定式转化**：
    | 不定式 | 转为 |
    |---|---|
    | $0 \cdot \infty$ | $\dfrac{0}{1/\infty} = \dfrac{0}{0}$ 或 $\dfrac{\infty}{1/0}$ |
    | $\infty - \infty$ | 通分为 $\dfrac{\cdots}{\cdots}$ |
    | $1^\infty$, $0^0$, $\infty^0$ | 取对数化为 $0 \cdot \infty$ |

- **重要极限的快速验证**：$\displaystyle \lim_{x \to 0} \dfrac{\sin x}{x} = \lim \dfrac{\cos x}{1} = 1$（条件满足）；
  $\displaystyle \lim_{x \to 0} \dfrac{e^x - 1}{x} = \lim \dfrac{e^x}{1} = 1$
- **替代方法**：很多 $0/0$ 型用 [[ANL-THM-025]] Taylor 展开更直观且免重复求导

## 链接

- 前置：[[ANL-DEF-014]] 导数、[[ANL-DEF-008]] 函数极限、[[ANL-THM-023]] Cauchy 中值定理
- 关联：[[ANL-THM-025]] Taylor 公式（很多 L'Hospital 题用 Taylor 更快）

## 跨专业应用

- **数值分析**：奇异函数（如 $\dfrac{\sin x}{x}$ 在 $0$ 处）的连续延拓与数值稳定计算
- **物理**：临界过程的极限行为，如电阻 $R \to 0$ 时电流的极限分析
