---
title: "换元积分典型范例"
type: example
id: ANL-EX-012
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 换元积分
  - 综合应用
depends:
  - ANL-THM-033
  - ANL-THM-032
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §8.2 例题"
difficulty: 3
illustrates:
  - ANL-THM-033
related:
  - ANL-THM-033
  - ANL-EX-013
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

用[[ANL-THM-033]]换元积分法计算下列积分：

1. **凑微分（第一类）**：$\displaystyle \int 2x \, e^{x^2} \, dx$
2. **三角代换（第二类）**：$\displaystyle \int_0^1 \sqrt{1 - x^2} \, dx$
3. **三角代换**：$\displaystyle \int \frac{1}{1 + x^2} \, dx$
4. **倒代换**：$\displaystyle \int \frac{dx}{x \sqrt{x^2 - 1}} \quad (x > 1)$

## 分析

**识别换元类型**：

- 第 1 题：被积函数中 $2x$ 是 $x^2$ 的导数 ⇒ 凑微分 $u = x^2$
- 第 2 题：$\sqrt{1 - x^2}$ 形式 ⇒ 三角代换 $x = \sin t$ 令 $1 - x^2 = \cos^2 t$
- 第 3 题：$1 + x^2$ 形式 ⇒ 三角代换 $x = \tan t$ 令 $1 + x^2 = \sec^2 t$
- 第 4 题：$\sqrt{x^2 - 1}$ 形式 + $1/x$ 因子 ⇒ 倒代换 $x = 1/t$（避免 $\sec$ 代换的繁琐）

## 证明 / 解答

### 第 1 题

**解：** 令 $u = x^2$，则 $du = 2x \, dx$。直接代入：
$$
\int 2x e^{x^2} \, dx = \int e^u \, du = e^u + C = e^{x^2} + C. \quad\blacksquare
$$

### 第 2 题

**解：** 令 $x = \sin t$，$t \in [0, \pi/2]$，$dx = \cos t \, dt$。

**上下限**：$x = 0 \mapsto t = 0$；$x = 1 \mapsto t = \pi/2$。

**化简被积函数**：$\sqrt{1 - \sin^2 t} = |\cos t| = \cos t$（$t \in [0, \pi/2] \Rightarrow \cos t \geq 0$）。

代入：
$$
\int_0^1 \sqrt{1-x^2} \, dx = \int_0^{\pi/2} \cos t \cdot \cos t \, dt = \int_0^{\pi/2} \cos^2 t \, dt.
$$

用 $\cos^2 t = \dfrac{1 + \cos 2t}{2}$：
$$
= \int_0^{\pi/2} \frac{1 + \cos 2t}{2} \, dt = \left[ \frac{t}{2} + \frac{\sin 2t}{4} \right]_0^{\pi/2} = \frac{\pi}{4} + 0 = \frac{\pi}{4}. \quad\blacksquare
$$

> **几何验证**：$\int_0^1 \sqrt{1-x^2} dx$ 是单位圆第一象限部分的面积 $= \pi/4$ ✓

### 第 3 题

**解：** 令 $x = \tan t$，$t \in (-\pi/2, \pi/2)$，$dx = \sec^2 t \, dt$。
$$
\int \frac{dx}{1 + x^2} = \int \frac{\sec^2 t \, dt}{1 + \tan^2 t} = \int \frac{\sec^2 t}{\sec^2 t} \, dt = \int dt = t + C = \arctan x + C. \quad\blacksquare
$$

> **第二种解法**（直接由原函数表）：$(\arctan x)' = \dfrac{1}{1+x^2}$，故 $\int \dfrac{dx}{1+x^2} = \arctan x + C$ ✓
> **本题展示了"反证"**——通过换元法**重新发现** $\arctan$ 为什么是 $\dfrac{1}{1+x^2}$ 的原函数。

### 第 4 题

**解（倒代换）**：令 $x = \dfrac{1}{t}$，$t \in (0, 1)$，$dx = -\dfrac{1}{t^2} dt$。

化简：
$$
x^2 - 1 = \frac{1}{t^2} - 1 = \frac{1 - t^2}{t^2}, \quad \sqrt{x^2 - 1} = \frac{\sqrt{1-t^2}}{t} \quad (t > 0).
$$

$$
\frac{1}{x \sqrt{x^2 - 1}} = \frac{1}{(1/t) \cdot \sqrt{1-t^2}/t} = \frac{t^2}{\sqrt{1-t^2}}.
$$

代入：
$$
\int \frac{dx}{x \sqrt{x^2-1}} = \int \frac{t^2}{\sqrt{1-t^2}} \cdot \left(-\frac{1}{t^2}\right) dt = -\int \frac{dt}{\sqrt{1-t^2}} = -\arcsin t + C.
$$

回代 $t = 1/x$：
$$
\int \frac{dx}{x\sqrt{x^2-1}} = -\arcsin \frac{1}{x} + C. \quad\blacksquare
$$

> **检验**：$\dfrac{d}{dx}\left[-\arcsin \dfrac{1}{x}\right] = -\dfrac{1}{\sqrt{1 - 1/x^2}} \cdot \left(-\dfrac{1}{x^2}\right) = \dfrac{1}{x^2 \sqrt{1 - 1/x^2}} = \dfrac{1}{x^2 \cdot \sqrt{x^2-1}/|x|} = \dfrac{|x|}{x^2 \sqrt{x^2-1}} = \dfrac{1}{x\sqrt{x^2-1}}$（$x > 0$）✓
>
> **替代答案**：$-\arcsin(1/x) = \text{arcsec}(x) - \pi/2$ 也可写作 $\text{arcsec}(x) + C'$。

## 关键技巧

- **凑微分识别"$g'(x)$ 因子"**：若被积函数包含 $g(x)$ 与 $g'(x)$，立即考虑 $u = g(x)$
- **三角代换的诱因**：被积函数含 $\sqrt{a^2 \pm x^2}$ 或 $\sqrt{x^2 - a^2}$
    | 形式 | 代换 | 三角恒等式 |
    |---|---|---|
    | $\sqrt{a^2 - x^2}$ | $x = a \sin t$ | $1 - \sin^2 = \cos^2$ |
    | $\sqrt{a^2 + x^2}$ | $x = a \tan t$ | $1 + \tan^2 = \sec^2$ |
    | $\sqrt{x^2 - a^2}$ | $x = a \sec t$（或倒代换） | $\sec^2 - 1 = \tan^2$ |
- **倒代换 $x = 1/t$ 的适用场景**：被积函数含 $\dfrac{1}{x^k}$ 因子且换元后简化（如第 4 题）
- **回代检查**：定积分**直接换上下限**；不定积分**最后回代回原变量**

## 变式

- **变式 1**：$\int \dfrac{2x+1}{x^2 + x + 1} dx$。提示：分子是分母的导数，凑微分 $u = x^2 + x + 1$
- **变式 2**：$\int \sqrt{4 - x^2} dx$。提示：$x = 2\sin t$
- **变式 3**：$\int \dfrac{dx}{\sqrt{x^2 + 4}}$。提示：$x = 2\tan t$，结果含反双曲函数 $\sinh^{-1}$
- **变式 4**：$\int_0^a \sqrt{a^2 - x^2} dx$（$a > 0$）。提示：$x = a \sin t$，结果 $\pi a^2/4$（圆面积四分之一）

## 链接

- 演示定理：[[ANL-THM-033]] 换元积分法
- 配合定理：[[ANL-THM-032]] N-L 公式（用于定积分）
- 后续：[[ANL-EX-013]] 分部积分典型范例
