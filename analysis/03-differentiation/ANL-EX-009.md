---
title: "链式法则与隐函数求导综合"
type: example
id: ANL-EX-009
subject: analysis
chapter: 03-differentiation
tags:
  - 微分
  - 链式法则
  - 隐函数
  - 综合应用
depends:
  - ANL-THM-018
  - ANL-THM-017
  - ANL-DEF-014
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §4.2 综合习题"
difficulty: 3
illustrates:
  - ANL-THM-018
related:
  - ANL-THM-017
  - ANL-EX-008
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

下列 4 道综合演示链式法则（[[ANL-THM-018]]）与隐函数求导的典型套路：

1. **多层复合**：求 $f(x) = \sin\big(\cos(x^2)\big)$ 的导数。
2. **隐函数求导**：方程 $x^2 + y^2 = 1$ 隐式定义 $y = y(x)$，求 $y'(x)$ 与 $y''(x)$。
3. **对数复合**：求 $f(x) = \ln\big(x + \sqrt{x^2 + 1}\big)$ 的导数（即 $\sinh^{-1} x$ 的导数）。
4. **组合应用**：$y = e^{\sin(x^2)}$，求 $y'(0)$ 与 $y''(0)$。

## 分析

- **第 1 题**：三层复合，依链式法则**逐层求导**——外、中、内三个因子相乘
- **第 2 题**：方程两边对 $x$ 求导（把 $y$ 当作 $x$ 的函数，应用链式法则到 $y$ 项），解出 $y'$；
  二阶导对 $y'$ 表达式再求导（继续把 $y$ 当作 $x$ 的函数）
- **第 3 题**：先求 $\sqrt{x^2+1}$ 的导数（链式 + 平方根），再求 $\ln(\cdot)$ 的导数；化简验证
- **第 4 题**：双层复合 $e^{\sin(x^2)}$，先求一阶导（链式），再代入 $x = 0$；二阶导用乘积法则 + 链式

## 证明 / 解答

### 第 1 题

**解：** 三层复合 $f = h(g(k(x)))$，其中 $k(x) = x^2$, $g(u) = \cos u$, $h(v) = \sin v$。
由[[ANL-THM-018]]链式法则：
$$
f'(x) = h'(g(k(x))) \cdot g'(k(x)) \cdot k'(x) = \cos(\cos(x^2)) \cdot \big(-\sin(x^2)\big) \cdot 2x.
$$
$$
\boxed{f'(x) = -2x \sin(x^2) \cos\big(\cos(x^2)\big).}
$$

### 第 2 题

**解（一阶）：** 对方程两边对 $x$ 求导（把 $y = y(x)$）：
$$
2x + 2y \cdot y' = 0 \quad\Longrightarrow\quad y' = -\frac{x}{y}, \quad (y \neq 0).
$$

**解（二阶）：** 对 $y' = -x/y$ 再对 $x$ 求导（用商法则 + 把 $y$ 看作 $x$ 的函数）：
$$
y'' = -\frac{1 \cdot y - x \cdot y'}{y^2} = -\frac{y - x y'}{y^2}.
$$

代入 $y' = -x/y$：
$$
y'' = -\frac{y - x \cdot (-x/y)}{y^2} = -\frac{y + x^2/y}{y^2} = -\frac{y^2 + x^2}{y^3} = -\frac{1}{y^3},
$$
最后一步用了 $x^2 + y^2 = 1$。

$$
\boxed{y' = -\frac{x}{y}, \qquad y'' = -\frac{1}{y^3}.}
$$

> **几何验证**：单位圆上点 $(x, y)$ 处切线斜率 $-x/y$ 与几何直观一致（半径 $\perp$ 切线，半径斜率 $y/x$，切线斜率 $-x/y$）。

### 第 3 题

**解：** 设 $u(x) = x + \sqrt{x^2 + 1}$。先求 $u'(x)$：
$$
u'(x) = 1 + \frac{1}{2\sqrt{x^2 + 1}} \cdot 2x = 1 + \frac{x}{\sqrt{x^2 + 1}} = \frac{\sqrt{x^2+1} + x}{\sqrt{x^2+1}}.
$$

由链式法则：
$$
f'(x) = \frac{u'(x)}{u(x)} = \frac{1}{x + \sqrt{x^2+1}} \cdot \frac{\sqrt{x^2+1} + x}{\sqrt{x^2+1}}.
$$

注意分子的 $\sqrt{x^2+1} + x$ 与分母的 $x + \sqrt{x^2+1}$ 相同，约去：
$$
\boxed{f'(x) = \frac{1}{\sqrt{x^2 + 1}}.}
$$

> **附注**：此即反双曲正弦函数的导数，$\sinh^{-1}(x) = \ln(x + \sqrt{x^2+1})$。
> 与 $(\arctan x)' = \dfrac{1}{1 + x^2}$ 对偶。

### 第 4 题

**解（一阶）：** 设 $g(x) = \sin(x^2)$, $f(u) = e^u$。
$$
y' = e^{\sin(x^2)} \cdot \cos(x^2) \cdot 2x.
$$
代入 $x = 0$：
$$
y'(0) = e^0 \cdot 1 \cdot 0 = 0.
$$

**解（二阶）：** 写 $y' = 2x \cos(x^2) e^{\sin(x^2)}$，应用[[ANL-THM-017]]乘积法则（三因子归纳到二因子嵌套）：

记 $A = 2x$, $B = \cos(x^2) e^{\sin(x^2)}$。
$$
y'' = A' B + A B'.
$$

- $A' = 2$
- $B = \cos(x^2) \cdot e^{\sin(x^2)}$，再用乘积法则 + 链式：
    $B' = -\sin(x^2) \cdot 2x \cdot e^{\sin(x^2)} + \cos(x^2) \cdot e^{\sin(x^2)} \cdot \cos(x^2) \cdot 2x$
    $= 2x \cdot e^{\sin(x^2)} \cdot \big[ \cos^2(x^2) - \sin(x^2) \big]$

代入 $x = 0$（关键观察：含 $2x$ 的项均为 $0$）：

- $A'(0) B(0) = 2 \cdot \cos 0 \cdot e^{\sin 0} = 2 \cdot 1 \cdot 1 = 2$
- $A(0) B'(0) = 0 \cdot (\ldots) = 0$

故
$$
\boxed{y'(0) = 0, \qquad y''(0) = 2.}
$$

$\blacksquare$

## 关键技巧

- **逐层求导**：多层复合时，从最外层开始逐层向内，每层"暂停"求导（外层 $\times$ 中层 $\times$ 内层）
- **隐函数求导双重身份**：方程中的 $y$ 既是被解的量又是 $x$ 的函数——求导时**两者都用**
- **代数化简的契机**：第 2 题用 $x^2 + y^2 = 1$ 化简 $y''$；第 3 题用约分化简 $f'$
- **代入特殊值**：第 4 题在 $x = 0$ 处计算时，含 $2x$ 因子的项立即归零，避免冗余计算

## 变式

- **变式 1**：求 $f(x) = \tan(\sin(\sqrt{x}))$ 的导数（四层复合）
- **变式 2**：方程 $e^{xy} + \sin(x + y) = x^2$ 求 $\dfrac{dy}{dx}$
- **变式 3**：参数方程 $\begin{cases} x = t - \sin t \\ y = 1 - \cos t \end{cases}$（旋轮线）求 $\dfrac{dy}{dx}$ 与 $\dfrac{d^2 y}{dx^2}$
- **变式 4**：对数求导法：求 $y = x^x$（$x > 0$）的导数。
  提示：取对数 $\ln y = x \ln x$，两边对 $x$ 求导（左边用链式 + 隐函数）

## 链接

- 演示定理：[[ANL-THM-018]] 链式法则
- 配合：[[ANL-THM-017]] 求导四则、[[ANL-EX-008]] 用定义求初等函数导数
- 关联：[[ANL-THM-019]] 反函数求导（含反三角函数导数表）
