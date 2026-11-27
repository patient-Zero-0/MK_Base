---
title: "分部积分典型范例（含递推与 Wallis）"
type: example
id: ANL-EX-013
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 分部积分
  - 递推积分
  - Wallis 公式
depends:
  - ANL-THM-034
  - ANL-THM-032
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §8.3 例题"
difficulty: 3
illustrates:
  - ANL-THM-034
related:
  - ANL-EX-012
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

用[[ANL-THM-034]]分部积分法计算下列积分：

1. **基础**：$\displaystyle \int x e^x \, dx$
2. **对数型**：$\displaystyle \int \ln x \, dx$
3. **重复分部**：$\displaystyle \int x^2 e^x \, dx$
4. **递推（Wallis 公式构造）**：建立 $\displaystyle I_n = \int_0^{\pi/2} \sin^n x \, dx$ 的递推公式

## 分析

按 LIATE 选 $u$ 经验法则（[[ANL-THM-034]]）选择：

- **第 1 题**：$x \cdot e^x$ 中代数 (A) > 指数 (E)，选 $u = x$, $dv = e^x dx$
- **第 2 题**：$\ln x$ 单独看，选 $u = \ln x$, $dv = dx$（凑出"原函数为 $x$"）
- **第 3 题**：连续两次 LIATE，每次代数项的"次数"降一阶
- **第 4 题**：递推积分的标准模式——"分部一次，把 $n$ 阶降到 $n-2$ 阶"

## 证明 / 解答

### 第 1 题

**解：** 选 $u = x$, $dv = e^x dx$ ⇒ $du = dx$, $v = e^x$。
$$
\int x e^x \, dx = x e^x - \int e^x \, dx = x e^x - e^x + C = (x - 1) e^x + C. \quad\blacksquare
$$

> **检验**：$[(x - 1) e^x]' = e^x + (x - 1) e^x = x e^x$ ✓

### 第 2 题

**解：** 选 $u = \ln x$, $dv = dx$ ⇒ $du = \dfrac{1}{x} dx$, $v = x$。
$$
\int \ln x \, dx = x \ln x - \int x \cdot \frac{1}{x} \, dx = x \ln x - \int dx = x \ln x - x + C. \quad\blacksquare
$$

> **教训**：当被积函数是单个对数 / 反三角函数（无显式 $dv$）时，选 $dv = dx$（即 $v = x$）。
> 这是 LIATE 法则中"L 优先"的典型应用。

### 第 3 题

**解：** 选 $u = x^2$, $dv = e^x dx$ ⇒ $du = 2x dx$, $v = e^x$。
$$
\int x^2 e^x dx = x^2 e^x - \int 2x e^x dx.
$$

剩下的 $\int 2x e^x dx = 2(x - 1)e^x + C'$（由第 1 题）。代入：
$$
\int x^2 e^x dx = x^2 e^x - 2(x - 1)e^x + C = (x^2 - 2x + 2) e^x + C. \quad\blacksquare
$$

> **关键**：每分部一次代数次数 $n \to n - 1$；$n$ 阶代数 $\times$ 指数 / 三角的积分需**分部 $n$ 次**。
> 用**表格法**可加速：交替微分 $x^n$ 列与积分 $e^x$ 列，对角相乘求和。

### 第 4 题

**解：** 写 $\sin^n x = \sin^{n-1} x \cdot \sin x$。选
$$
u = \sin^{n-1} x, \quad dv = \sin x \, dx \quad \Rightarrow \quad du = (n-1) \sin^{n-2} x \cos x \, dx, \quad v = -\cos x.
$$

定积分分部：
$$
I_n = \big[ -\sin^{n-1} x \cdot \cos x \big]_0^{\pi/2} + (n-1) \int_0^{\pi/2} \sin^{n-2} x \cos^2 x \, dx.
$$

**端点值**：$x = \pi/2$ 时 $\cos x = 0$；$x = 0$ 时 $\sin x = 0$（$n \geq 2$ ⇒ $\sin^{n-1} 0 = 0$）。两端都为 $0$。

故
$$
I_n = (n-1) \int_0^{\pi/2} \sin^{n-2} x \cdot (1 - \sin^2 x) \, dx = (n-1) [I_{n-2} - I_n].
$$

整理：
$$
I_n + (n-1) I_n = (n-1) I_{n-2} \quad \Rightarrow \quad \boxed{I_n = \frac{n-1}{n} \cdot I_{n-2}.}
$$

**初值**：

- $I_0 = \int_0^{\pi/2} 1 \, dx = \pi/2$
- $I_1 = \int_0^{\pi/2} \sin x \, dx = 1$

**展开**（$n$ 偶，$n = 2k$）：
$$
I_{2k} = \frac{2k-1}{2k} \cdot \frac{2k-3}{2k-2} \cdots \frac{1}{2} \cdot \frac{\pi}{2} = \frac{(2k-1)!!}{(2k)!!} \cdot \frac{\pi}{2}.
$$

**展开**（$n$ 奇，$n = 2k+1$）：
$$
I_{2k+1} = \frac{2k}{2k+1} \cdot \frac{2k-2}{2k-1} \cdots \frac{2}{3} \cdot 1 = \frac{(2k)!!}{(2k+1)!!}.
$$

> **Wallis 公式**：由 $I_n$ 单调（$\sin^n x \in [0, 1] \Rightarrow \sin^{n+1} \leq \sin^n$）⇒ $I_{2k+1} \leq I_{2k} \leq I_{2k-1}$。
> 取比值并令 $k \to \infty$ 得：
> $$
> \frac{\pi}{2} = \lim_{k \to \infty} \frac{(2k)!! \cdot (2k)!!}{(2k-1)!! \cdot (2k+1)!!} = \prod_{k=1}^{\infty} \frac{(2k)^2}{(2k-1)(2k+1)}.
> $$
> 这就是著名的 **Wallis 乘积公式**。$\blacksquare$

## 关键技巧

- **LIATE 选 $u$**：Logarithm > Inverse trig > Algebraic > Trig > Exponential 优先级
- **"凑出 $dv = dx$"**：单个 $\ln x, \arctan x$ 等无显式 $dv$ 时的标准技巧
- **重复分部**：代数项次数为 $n$ 时分部 $n$ 次（或用表格法加速）
- **递推积分**：把 $\sin^n / x^n / \ln^n$ 等"指数变量"化为递推关系，是 $I_n$ 系列的核心方法
- **"$\sin^n + \cos^n$ 平方关系"**：第 4 题中 $\sin^{n-2} \cos^2 = \sin^{n-2} - \sin^n$ 的拆解是关键

## 变式

- **变式 1**：$\int x \sin x \, dx$。答案：$-x \cos x + \sin x + C$（同 LIATE）
- **变式 2**：$\int x^2 \cos x \, dx$。重复分部两次，得 $(x^2 - 2)\sin x + 2x \cos x + C$
- **变式 3**：$\int e^x \sin x \, dx$ —— 两次分部后**回到原积分**（用解方程法）。
  设 $J = \int e^x \sin x dx$。分部两次：$J = e^x \sin x - e^x \cos x - J \Rightarrow J = \dfrac{e^x(\sin x - \cos x)}{2} + C$
- **变式 4**：建立 $J_n = \int x^n e^x dx$ 的递推。提示：$J_n = x^n e^x - n J_{n-1}$
- **变式 5**：建立 $K_n = \int_0^{\pi/2} \cos^n x \, dx$ 的递推 — 由对称性 $K_n = I_n$
- **变式 6**（高阶）：用 Wallis 公式证 $n! \sim \sqrt{2\pi n} (n/e)^n$（Stirling 公式的弱形式）

## 链接

- 演示定理：[[ANL-THM-034]] 分部积分法
- 配合定理：[[ANL-THM-032]] N-L 公式
- 关联：[[ANL-EX-012]] 换元积分典型范例
- 进阶：Wallis 公式 → Stirling 渐近公式（不在本知识库范围）
