---
title: "Frullani 积分：两个指数函数之差"
type: example
id: ANL-EX-025
subject: analysis
chapter: 06-interesting-problems
tags:
  - 反常积分
  - Frullani
  - 累次积分
  - 换序
depends:
  - ANL-THM-035
  - ANL-DEF-029
  - ANL-PROB-016
  - ANL-EX-014
uses: []
status: stable
source: "经典问题（Frullani）；参考华东师范大学《数学分析》第5版 §11.3"
difficulty: 4
illustrates:
  - ANL-THM-035
related:
  - ANL-EX-015
  - ANL-PROB-019
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

设 $a,b>0$，证明 Frullani 积分
$$
\int_0^{+\infty}\frac{e^{-ax}-e^{-bx}}{x}\,dx=\ln\frac{b}{a}.
$$
特别地，取 $a=1$、$b=2$，得 $\displaystyle\int_0^{+\infty}\frac{e^{-x}-e^{-2x}}{x}\,dx=\ln 2$。

## 分析

先看被积函数 $f(x)=\dfrac{e^{-ax}-e^{-bx}}{x}$ 的两个端点。当 $x\to 0^+$ 时，由 $e^{-ax}=1-ax+O(x^2)$ 得
$$
e^{-ax}-e^{-bx}=(b-a)x+O(x^2),
$$
所以 $f(x)\to b-a$：$x=0$ 是**可去瑕点**，不是真瑕点。当 $x\to+\infty$ 时，在 $x\ge1$ 上有
$$
\left|\frac{e^{-ax}-e^{-bx}}{x}\right|\le e^{-ax}+e^{-bx},
$$
而 $\int_1^{+\infty}e^{-ax}\,dx$ 收敛，故积分在无穷远处**绝对收敛**。这两点用 [[ANL-DEF-029]] 的定义与 [[ANL-THM-035]] 的比较判别即可确认，难点不在收敛性。

真正的内容是**求值**。$f$ 没有初等原函数，但两个指数之差可以写成对参数 $t$ 的积分：
$$
e^{-ax}-e^{-bx}=\int_a^b x\,e^{-xt}\,dt,
$$
于是
$$
\frac{e^{-ax}-e^{-bx}}{x}=\int_a^b e^{-xt}\,dt\ge 0.
$$
被积函数由此化成了一个**非负二重积分的"先对 t 后对 x"形式**。如果允许交换次序，内层积分是 $\int_0^{+\infty}e^{-xt}\,dx=\dfrac1t$（由代换 $u=xt$ 得它等于 $\Gamma(1)/t$，见 [[ANL-EX-014]] 与 [[ANL-PROB-016]]），外层就只剩 $\int_a^b\dfrac{dt}{t}$。

所以路线是：先在**有限矩形** $[0,R]\times[a,b]$ 上证明累次积分可交换，再令 $R\to+\infty$。不能一上来就交换，因为 $x$ 的积分区间无界；也不能在 $x=0$ 处把原积分写成两个积分之差：$\int_0^\infty e^{-ax}/x\,dx$ 与 $\int_0^\infty e^{-bx}/x\,dx$ 各自在 $0$ 附近像 $1/x$ 一样发散，只有**差式**才有有限值。

## 证明 / 解答

### 第一步：积分收敛

$f$ 在 $(0,+\infty)$ 上连续，且由上面的展开 $\lim_{x\to0^+}f(x)=b-a$。补充定义 $f(0)=b-a$ 后，$f$ 在 $[0,1]$ 上连续，故 $\int_0^1 f\,dx$ 是通常的定积分，与反常性无关。

在 $[1,+\infty)$ 上，$|f(x)|\le e^{-ax}+e^{-bx}$，又
$$
\int_1^{+\infty}e^{-ax}\,dx=\frac{e^{-a}}{a}<+\infty,
$$
同理 $\int_1^{+\infty}e^{-bx}\,dx<+\infty$。由 [[ANL-THM-035]] 的比较判别法，$\int_1^{+\infty}f\,dx$ 绝对收敛。两段合并，原积分收敛。

### 第二步：有限矩形上的换序

对 $R>0$，记
$$
I(R)=\int_0^R f(x)\,dx,\qquad J(R)=\int_a^b\frac{1-e^{-Rt}}{t}\,dt,
$$
其中 $I(R)$ 用到 $f$ 在 $0$ 处的连续延拓。下面证明 $I(R)=J(R)$。

先对 $I$ 求导。由微积分基本定理（[[ANL-THM-032]]），
$$
I'(R)=f(R)=\frac{e^{-aR}-e^{-bR}}{R}.
$$

再对 $J$ 求导。对 $h\ne0$，
$$
\frac{J(R+h)-J(R)}{h}=\int_a^b e^{-Rt}\,\varphi_h(t)\,dt,\qquad \varphi_h(t)=\frac{1-e^{-ht}}{ht}.
$$
当 $h\to0$ 时 $\varphi_h(t)\to1$。又 $\varphi_h(t)$ 只依赖于乘积 $ht$，而 $ht$ 在 $t\in[a,b]$ 上一致地趋于 $0$，故 $\varphi_h\to1$ 在 $[a,b]$ 上**一致**。于是
$$
\left|\frac{J(R+h)-J(R)}{h}-\int_a^b e^{-Rt}\,dt\right|\le (b-a)\sup_{t\in[a,b]}\left|\varphi_h(t)-1\right|\longrightarrow0.
$$
所以
$$
J'(R)=\int_a^b e^{-Rt}\,dt=\frac{e^{-aR}-e^{-bR}}{R}=I'(R).
$$
又 $I(0)=J(0)=0$，故 $I(R)=J(R)$ 对一切 $R>0$ 成立。这一步正是"先截断到有限矩形、再交换累次积分"的严格实现：用对一个参数求导的方式比较两边的累次积分，不必引用多元微积分中的换序定理。

### 第三步：令截断尺度趋于无穷

由第一步，$\lim_{R\to+\infty}I(R)$ 存在，且等于原积分。对 $J(R)$，利用 $\int_a^b\dfrac{dt}{t}=\ln\dfrac{b}{a}$，有
$$
\left|J(R)-\ln\frac{b}{a}\right|
=\left|\int_a^b\frac{e^{-Rt}}{t}\,dt\right|
\le\frac1a\int_a^b e^{-Rt}\,dt
=\frac{e^{-aR}-e^{-bR}}{aR}\longrightarrow0\quad(R\to+\infty).
$$
所以
$$
\int_0^{+\infty}\frac{e^{-ax}-e^{-bx}}{x}\,dx=\lim_{R\to+\infty}I(R)=\lim_{R\to+\infty}J(R)=\int_a^b\frac{dt}{t}=\ln\frac{b}{a}.
$$
$\blacksquare$

## 关键技巧

- **参数化**：把指数差写成 $\int_a^b x e^{-xt}\,dt$，将"无初等原函数的积分"变成"非负核的二重积分"，这是 Frullani 型问题的通用入口。
- **先截断再取极限**：先在有限矩形上验证换序（本题用对 $R$ 求导比较两边），再让 $R\to+\infty$，避免无界区间上的换序困难。
- **端点分开处理**：$x=0$ 用 Taylor 展开判断为可去瑕点，$x\to+\infty$ 用指数衰减做比较，两段都收敛才能断言原积分收敛。
- **不能拆项**：$\int_0^\infty e^{-ax}/x\,dx$ 在 $0$ 处发散，差式的有限值来自两项发散部分的抵消，必须整体处理。
- **内层积分是 Γ 函数特例**：$\int_0^{+\infty}e^{-xt}\,dx=\dfrac1t$，见 [[ANL-EX-014]]。

## 变式

- **变式 1**：验证具体数值 $\displaystyle\int_0^\infty\frac{e^{-x}-e^{-2x}}{x}\,dx=\ln 2$；交换 $a,b$ 得相反数，故 $a=b$ 时积分为 $0$。
- **变式 2**（一般 Frullani 定理）：设 $f\in C^1[0,+\infty)$ 且 $\int_0^\infty|f'(s)|\,ds<+\infty$，则 $f(+\infty)$ 存在，且
    $$
    \int_0^\infty\frac{f(ax)-f(bx)}{x}\,dx=\big(f(0)-f(+\infty)\big)\ln\frac{b}{a}.
    $$
    提示：把 $f(ax)-f(bx)$ 写成 $-x\int_a^b f'(xt)\,dt$，重复本题"截断—换序—取极限"三步。
- **变式 3**：说明为什么不能把原积分写成 $\displaystyle\int_0^\infty\frac{e^{-ax}}{x}\,dx-\int_0^\infty\frac{e^{-bx}}{x}\,dx$。提示：两个积分在 $0$ 的邻域分别与 $\int_0^\varepsilon\frac{dx}{x}$ 同阶发散，而它们的差在 $0$ 处有有限极限。
- **变式 4**：说明 $a,b>0$ 不可去掉：若 $a<0<b$，则 $e^{-ax}$ 随 $x\to+\infty$ 指数增长，原积分发散。提示：此时被积函数在无穷远处无界且不衰减。

## 链接

- 演示定理：[[ANL-THM-035]] 反常积分收敛判别（比较判别）
- 定义：[[ANL-DEF-029]] 无穷限反常积分
- 相关例题：[[ANL-EX-015]] Dirichlet 积分（条件收敛与换序的另一典型）、[[ANL-EX-014]] 反常积分敛散与 Γ 函数
- 相关习题：[[ANL-PROB-016]] 高斯积分与 Γ 函数、[[ANL-PROB-019]] 变限积分求导
- 前置工具：[[ANL-THM-032]] Newton–Leibniz 公式、[[ANL-EX-012]] 换元积分
