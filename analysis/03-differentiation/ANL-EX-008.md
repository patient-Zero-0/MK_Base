---
title: "用定义求三类初等函数的导数"
type: example
id: ANL-EX-008
subject: analysis
chapter: 03-differentiation
tags:
  - 微分
  - 定义法
  - 初等函数
depends:
  - ANL-DEF-014
  - ANL-DEF-009
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §4.1"
difficulty: 2
illustrates:
  - ANL-DEF-014
related:
  - ANL-THM-017
  - ANL-THM-018
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

用导数定义（[[ANL-DEF-014]]）求下列函数在任意 $x \in \mathbb{R}$ 的导数：

1. $f(x) = x^n$（$n \in \mathbb{N}^*$）
2. $f(x) = e^x$
3. $f(x) = \sin x$

## 分析

定义法的核心是计算差商的极限：
$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}.
$$

每题的技巧不同：

- **$x^n$**：用二项式展开 $(x+h)^n$，主项 $x^n$ 抵消，剩余项含 $h$ 的因子
- **$e^x$**：分离 $e^x$ 因子，归结到 $\lim_{h \to 0} \dfrac{e^h - 1}{h} = 1$（与 $e$ 的极限定义 [[ANL-DEF-009]] 直接关联）
- **$\sin x$**：用和差化积公式 $\sin(x+h) - \sin x = 2 \cos\left(x + \tfrac{h}{2}\right) \sin\tfrac{h}{2}$，归结到 $\lim_{h \to 0} \dfrac{\sin h}{h} = 1$

## 证明 / 解答

### 第 1 题：幂函数的导数

**解：** 由二项式定理，
$$
(x+h)^n = x^n + n x^{n-1} h + \binom{n}{2} x^{n-2} h^2 + \cdots + h^n.
$$

故
$$
\frac{(x+h)^n - x^n}{h} = n x^{n-1} + \binom{n}{2} x^{n-2} h + \cdots + h^{n-1}.
$$

除第一项外，其余各项均含因子 $h$。当 $h \to 0$，
$$
f'(x) = \lim_{h \to 0} \frac{(x+h)^n - x^n}{h} = n x^{n-1}. \quad\blacksquare
$$

### 第 2 题：指数函数的导数

**解：** 由 $e^{x+h} = e^x \cdot e^h$，
$$
\frac{e^{x+h} - e^x}{h} = e^x \cdot \frac{e^h - 1}{h}.
$$

**关键极限**：$\displaystyle \lim_{h \to 0} \frac{e^h - 1}{h} = 1$。

> **快速论证**（依赖 [[ANL-DEF-009]] 自然常数 $e$ 的极限定义）：
> 由 $e^h = \lim_{n \to \infty} \left(1 + \frac{h}{n}\right)^n$ 出发，
> 配合 $e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n$，
> 经初等估计可得 $e^h = 1 + h + o(h)$（$h \to 0$）。
> 整理即得上述极限。

故
$$
f'(x) = \lim_{h \to 0} \frac{e^{x+h} - e^x}{h} = e^x \cdot 1 = e^x. \quad\blacksquare
$$

### 第 3 题：正弦函数的导数

**解：** 用和差化积：
$$
\sin(x+h) - \sin x = 2 \cos\left(x + \tfrac{h}{2}\right) \sin\tfrac{h}{2}.
$$

故
$$
\frac{\sin(x+h) - \sin x}{h} = \cos\left(x + \tfrac{h}{2}\right) \cdot \frac{\sin(h/2)}{h/2}.
$$

由经典极限 $\displaystyle \lim_{u \to 0} \frac{\sin u}{u} = 1$ 与 $\cos$ 的连续性：
$$
\lim_{h \to 0} \cos\left(x + \tfrac{h}{2}\right) = \cos x, \qquad \lim_{h \to 0} \frac{\sin(h/2)}{h/2} = 1.
$$

由 [[ANL-THM-009]] 极限的乘积法则，
$$
f'(x) = \cos x \cdot 1 = \cos x. \quad\blacksquare
$$

## 关键技巧

- **二项式展开 + 主项抵消**：求 $x^n$ 时通用模板，可推广到任意多项式
- **乘性分解**：$e^{x+h} = e^x e^h$ 把 $x$ 与 $h$ 分离，归结到 $h \to 0$ 的"局部"极限
- **和差化积**：处理三角函数的"差"必备工具，与 $\sin / \tan / \cot$ 求导通用
- **归结到经典极限**：$\frac{e^h - 1}{h} \to 1$ 与 $\frac{\sin h}{h} \to 1$ 是初等函数求导的两个核心"原子极限"

## 变式

- **变式 1**：用定义证明 $(\cos x)' = -\sin x$。提示：用 $\cos(x+h) - \cos x = -2 \sin(x + h/2) \sin(h/2)$
- **变式 2**：用定义证明 $(a^x)' = a^x \ln a$（$a > 0, a \neq 1$）。提示：$a^x = e^{x \ln a}$ + 链式法则；
  或直接 $\frac{a^h - 1}{h} \to \ln a$
- **变式 3**：将第 1 题推广至有理指数 $(x^\alpha)' = \alpha x^{\alpha - 1}$（$x > 0$, $\alpha \in \mathbb{Q}$）。
  提示：$\alpha = p/q$ 时设 $y = x^{1/q}$ 用反函数求导
- **变式 4**：求 $f(x) = x|x|$ 在 $x_0 = 0$ 的导数。提示：用单侧导数 [[ANL-DEF-016]]，验证左右一致

## 链接

- 演示定义：[[ANL-DEF-014]]
- 配合定理：[[ANL-THM-017]] 求导四则、[[ANL-THM-018]] 链式法则
- 后续例题：[[ANL-EX-009]] 链式法则与隐函数求导综合
