---
title: "Rolle 与 Lagrange 中值定理综合应用"
type: problem
id: ANL-PROB-012
subject: analysis
chapter: 03-differentiation
tags:
  - 微分
  - 中值定理
  - 综合应用
depends:
  - ANL-THM-021
  - ANL-THM-022
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §6.1 综合习题"
difficulty: 4
tests:
  - ANL-THM-021
  - ANL-THM-022
related:
  - ANL-EX-010
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

1. **函数估计**：设 $f$ 在 $[a, b]$ 上连续、$(a, b)$ 内可导，$f(a) = f(b) = 0$，$|f'(x)| \leq M$ 在 $(a, b)$ 上恒成立。证明
    $$ |f(x)| \leq \frac{M(b - a)}{2}, \quad \forall x \in [a, b]. $$
2. **零点夹逼**：设 $f$ 在 $\mathbb{R}$ 上可导。证明 $f$ 与 $f'$ 的零点"交错"——
    若 $f(x_1) = f(x_2) = 0$（$x_1 < x_2$），则 $f'$ 在 $(x_1, x_2)$ 内**至少有一个**零点。
    用此推出：若 $f$ 在 $\mathbb{R}$ 上有 $k$ 个零点，则 $f'$ 至少有 $k - 1$ 个零点。
3. **多项式根数判定**：证明 $p(x) = x^3 - 3x + a$（$a \in \mathbb{R}$ 为常数）在 $\mathbb{R}$ 上**至多** $3$ 个实根，并讨论 $a$ 取值与实根个数的对应。

## 提示

<details><summary>点击展开提示</summary>

- **第 1 题**：固定 $x \in (a, b)$，对 $[a, x]$ 和 $[x, b]$ 分别用 [[ANL-THM-022]] Lagrange，
  把 $|f(x)|$ 表为两个端点处的差分形式，再夹逼。结论中的 $(b - a) / 2$ 暗示对两段距离取最小。
- **第 2 题**：直接套用 [[ANL-THM-021]] Rolle 定理。
- **第 3 题**：反证 + Rolle。若 $p$ 有 $\geq 4$ 个实根，则 $p'$ 至少 $\geq 3$ 个；但 $p'(x) = 3x^2 - 3$ 至多 $2$ 个实根，矛盾。
  实根数随 $a$ 的讨论用 $p$ 的极值（[[ANL-DEF-018]]）。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题

**证明**：固定 $x \in (a, b)$。对 $[a, x]$ 应用 [[ANL-THM-022]] Lagrange：
$\exists \xi_1 \in (a, x)$ 使 $f(x) - f(a) = f'(\xi_1)(x - a)$。代入 $f(a) = 0$：
$$
|f(x)| = |f'(\xi_1)| \cdot (x - a) \leq M(x - a). \quad (*)
$$

对 $[x, b]$ 应用 Lagrange：$\exists \xi_2 \in (x, b)$ 使 $f(b) - f(x) = f'(\xi_2)(b - x)$。代入 $f(b) = 0$：
$$
|f(x)| = |f'(\xi_2)| \cdot (b - x) \leq M(b - x). \quad (**)
$$

合并 $(*)$ 与 $(**)$：
$$
|f(x)| \leq M \min(x - a, b - x).
$$

由几何观察（或 AM-GM），$\min(x-a, b-x) \leq \dfrac{(x-a) + (b-x)}{2} = \dfrac{b-a}{2}$。

故 $|f(x)| \leq M(b - a)/2$。在端点 $x = a$ 或 $b$，$|f| = 0 \leq M(b-a)/2$。$\blacksquare$

> **强化版**（紧致估计）：本题的最优常数 $M(b-a)/2$ 在 $f(x) = M \cdot \dfrac{(x-a)(b-x)}{(b-a)/2 \cdot \text{合适缩放}}$
> 这种"屋顶函数"上达到——但严格紧致估计需 Taylor 展开（[[ANL-THM-025]]）。

### 第 2 题：零点交错

**证明**：由 $f(x_1) = f(x_2) = 0 = $ 两端值相等，且 $f$ 在 $[x_1, x_2]$ 上连续、$(x_1, x_2)$ 内可导，
[[ANL-THM-021]] Rolle 定理给出 $\exists \xi \in (x_1, x_2)$ 使 $f'(\xi) = 0$。

**推广**（$k$ 个零点 ⇒ $f'$ 至少 $k - 1$ 个零点）：设 $f$ 的 $k$ 个零点按升序为 $x_1 < x_2 < \cdots < x_k$。
对每个相邻对 $(x_i, x_{i+1})$（$i = 1, \ldots, k-1$）应用 Rolle，得 $f'$ 在 $(x_i, x_{i+1})$ 内有零点 $\xi_i$。
$\xi_1 < \xi_2 < \cdots < \xi_{k-1}$ 互不相同（位于不交的区间内），故 $f'$ 至少有 $k-1$ 个不同零点。$\blacksquare$

### 第 3 题

**证明（至多 $3$ 实根）**：反证，假设 $p$ 有 $\geq 4$ 个实根。由第 2 题推论，$p'$ 至少有 $3$ 个实根。
但 $p'(x) = 3x^2 - 3 = 3(x-1)(x+1)$，**恰好** $2$ 个实根 $\pm 1$。矛盾。故 $p$ 至多 $3$ 实根。$\blacksquare$

**实根个数随 $a$ 的讨论**：求 $p$ 的极值。$p'(x) = 0 \iff x = \pm 1$。

| $x$ | $p(x)$ | 类型 |
|---|---|---|
| $x = -1$ | $-1 + 3 + a = 2 + a$ | 局部极大（$p'' = 6x = -6 < 0$） |
| $x = 1$ | $1 - 3 + a = -2 + a$ | 局部极小（$p'' = 6 > 0$） |

$p(\pm \infty) = \pm \infty$（三次多项式首项系数为正）。结合极值，$p$ 的实根个数：

| 条件 | 实根数 | 几何 |
|---|---|---|
| $a > 2$（极大值 $< 0$） | 1 | 极大极小都 $< 0$，仅在 $+\infty$ 一侧穿过 $x$ 轴 |
| $a = 2$（极大值 $= 0$） | 2（其中 $x = -1$ 重根） | 极大值正好触轴 |
| $-2 < a < 2$ | 3 | 极大 $> 0$，极小 $< 0$，三处穿轴 |
| $a = -2$（极小值 $= 0$） | 2（$x = 1$ 重根） | 极小正好触轴 |
| $a < -2$ | 1 | 极大极小都 $> 0$ |

> 推论：方程 $x^3 - 3x = c$（$c = -a$）有三个实根 $\iff |c| < 2$。$\blacksquare$

</details>

## 考察点

- [[ANL-THM-021]] Rolle 定理在零点夹逼中的标准应用
- [[ANL-THM-022]] Lagrange 中值定理的"双向 Lagrange"技巧（第 1 题）
- 反证 + Rolle 用于多项式根数估计
- 极值分析与方程求根的综合（第 3 题）

## 备注

**中值定理在不等式与方程理论中的工具图谱**：

```text
         证明等式             证明不等式             根数估计
            │                    │                     │
  ┌─────────┴──────────┐         │                     │
  │                    │         │                     │
单点 ξ：Lagrange    比例 ξ：Cauchy     |f'| 上界估计     反证 + Rolle
                                   ↓
                            Lipschitz 估计 / 误差控制
```
