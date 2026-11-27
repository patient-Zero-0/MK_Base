---
title: "用 ε-δ 验证导数定义"
type: problem
id: ANL-PROB-011
subject: analysis
chapter: 03-differentiation
tags:
  - 微分
  - ε-δ
  - 定义法
depends:
  - ANL-DEF-014
  - ANL-DEF-016
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §4.1 习题"
difficulty: 3
tests:
  - ANL-DEF-014
  - ANL-DEF-016
related:
  - ANL-EX-008
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

用导数的 ε-δ 等价定义（[[ANL-DEF-014]]）严格验证：

1. $f(x) = x^2$ 在 $x_0 = 3$ 处可导且 $f'(3) = 6$。
2. $f(x) = \dfrac{1}{x}$ 在 $x_0 = 2$ 处可导且 $f'(2) = -\dfrac{1}{4}$。
3. **边界判定**：$f(x) = x|x|$ 在 $x_0 = 0$ 处可导，求 $f'(0)$，并说明 $f$ 是否在 $0$ 处二阶可导。

## 提示

<details><summary>点击展开提示</summary>

- **第 1 题**：把 $\dfrac{f(3+\Delta x) - f(3)}{\Delta x} - 6$ 化简，找到含 $|\Delta x|$ 因子的简单形式，即可定 $\delta$。
- **第 2 题**：差商 $\dfrac{1/(2+\Delta x) - 1/2}{\Delta x}$ 通分后简化为 $\dfrac{-1}{2(2+\Delta x)}$。要令其逼近 $-1/4$ 需控制 $|\Delta x|$ 不太大（如 $|\Delta x| < 1$）。
- **第 3 题**：$f(x) = x|x|$ 是分段函数，须用[[ANL-DEF-016]]单侧导数；分别在 $x \to 0^+$ 与 $x \to 0^-$ 计算差商极限。
  二阶导考察 $f'$ 是否在 $0$ 处可导（即是否存在 $f''(0)$）。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题

**证明**：取 $\varepsilon > 0$。对 $\Delta x \neq 0$，
$$
\frac{f(3 + \Delta x) - f(3)}{\Delta x} - 6 = \frac{(3 + \Delta x)^2 - 9}{\Delta x} - 6 = \frac{6 \Delta x + (\Delta x)^2}{\Delta x} - 6 = \Delta x.
$$

故只需 $|\Delta x| < \varepsilon$ 即得
$$
\left| \frac{f(3 + \Delta x) - f(3)}{\Delta x} - 6 \right| = |\Delta x| < \varepsilon.
$$

取 $\delta = \varepsilon$ 即可。$\blacksquare$

### 第 2 题

**证明**：取 $\varepsilon > 0$。对 $\Delta x \neq 0$，$\Delta x > -2$（保证 $2 + \Delta x \neq 0$），
$$
\frac{f(2 + \Delta x) - f(2)}{\Delta x} = \frac{1}{\Delta x}\left( \frac{1}{2 + \Delta x} - \frac{1}{2} \right) = \frac{1}{\Delta x} \cdot \frac{2 - (2 + \Delta x)}{2(2 + \Delta x)} = \frac{-1}{2(2 + \Delta x)}.
$$

差与目标 $-1/4$ 之差：
$$
\frac{-1}{2(2 + \Delta x)} - \left( -\frac{1}{4} \right) = \frac{-1}{2(2+\Delta x)} + \frac{1}{4} = \frac{-2 + (2 + \Delta x)}{4(2+\Delta x)} = \frac{\Delta x}{4(2 + \Delta x)}.
$$

**控制 $|\Delta x|$**：先要求 $|\Delta x| < 1$，则 $2 + \Delta x \in (1, 3)$，故 $|2 + \Delta x| > 1$，
$$
\left| \frac{\Delta x}{4(2+\Delta x)} \right| < \frac{|\Delta x|}{4}.
$$

故只需 $\dfrac{|\Delta x|}{4} < \varepsilon$，即 $|\Delta x| < 4\varepsilon$。
**取 $\delta = \min(1, 4\varepsilon)$** 即可。$\blacksquare$

> **关键点**：分母 $2 + \Delta x$ 不为零是结构限制；用 $|\Delta x| < 1$ 圈出"安全邻域"是常见技巧。

### 第 3 题

**写明分段**：$f(x) = \begin{cases} x^2, & x \geq 0 \\ -x^2, & x < 0 \end{cases}$

**右导数**：
$$
f'_+(0) = \lim_{\Delta x \to 0^+} \frac{f(\Delta x) - f(0)}{\Delta x} = \lim_{\Delta x \to 0^+} \frac{(\Delta x)^2}{\Delta x} = \lim_{\Delta x \to 0^+} \Delta x = 0.
$$

**左导数**：
$$
f'_-(0) = \lim_{\Delta x \to 0^-} \frac{f(\Delta x) - f(0)}{\Delta x} = \lim_{\Delta x \to 0^-} \frac{-(\Delta x)^2}{\Delta x} = \lim_{\Delta x \to 0^-} (-\Delta x) = 0.
$$

由 [[ANL-DEF-016]]，$f'_+(0) = f'_-(0) = 0$，故 $f$ 在 $0$ 处可导，$f'(0) = 0$。

**二阶可导性分析**：先求 $f'(x)$ 全定义：

- $x > 0$：$f'(x) = 2x$
- $x < 0$：$f'(x) = -2x$
- $x = 0$：$f'(0) = 0$（已证）

合并：$f'(x) = 2|x|$。

**$f'$ 在 $0$ 处是否可导？** 即问 $|x|$ 在 $0$ 处是否可导。
由 [[ANL-DEF-016]] 经典结论，$|x|$ 在 $0$ 处**不可导**（左右导数 $\mp 1$ 不等）。
故 $f'$ 在 $0$ 处不可导，**$f$ 在 $0$ 处不二阶可导**。

> **几何解释**：$f(x) = x|x|$ 图像在 $0$ 处"光滑连接"两段抛物线（共享水平切线），
> 但二阶导数描述弯曲方向——左侧 $f'' = -2$（凹），右侧 $f'' = 2$（凸），不连续。
> 故 $0$ 处一阶导存在但二阶导不存在，是"光滑度恰好为 $C^1$ 而非 $C^2$"的典型例子。

$\blacksquare$

</details>

## 考察点

- [[ANL-DEF-014]] 导数的 ε-δ 等价定义的正向运用
- [[ANL-DEF-016]] 单侧导数（用于分段函数）
- 控制 $\delta$ 时的"先圈邻域再求 $\delta$"技巧（第 2 题）
- 一阶可导但不二阶可导的典型反例（第 3 题）

## 备注

**ε-δ 法的常见 $\delta$ 选取套路**：

| 差商化简形式 | $\delta$ 取法 |
|---|---|
| $\Delta x$ | $\delta = \varepsilon$ |
| $\dfrac{c \cdot \Delta x}{(\text{有界, 远离零})}$ | $\delta = \min(\text{邻域半径}, \varepsilon \cdot \text{下界}/c)$ |
| $(\Delta x)^2 / (\ldots)$ | 先圈邻域使分母有下界，再 $\delta = \min(\ldots, \sqrt{\varepsilon \cdot c})$ |
