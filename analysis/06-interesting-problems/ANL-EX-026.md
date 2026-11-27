---
title: "大二之梦：幂塔的积分与级数"
type: example
id: ANL-EX-026
subject: analysis
chapter: 06-interesting-problems
tags:
  - 反常积分
  - 级数
  - 一致收敛
  - 幂级数
depends:
  - ANL-THM-044
  - ANL-THM-045
  - ANL-THM-034
  - ANL-EX-012
uses: []
status: stable
source: "经典问题（Johann Bernoulli）；参考华东师范大学《数学分析》第5版 §13.2、§11.3"
difficulty: 4
illustrates:
  - ANL-THM-045
related:
  - ANL-EX-022
  - ANL-EX-025
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

证明"大二之梦"（Sophomore's dream）：
$$
\int_0^1 x^{-x}\,dx=\sum_{n=1}^{\infty}\frac{1}{n^n},
$$
并给出数值估计 $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^n}\approx1.2912859$。

## 分析

被积函数 $x^{-x}=e^{-x\ln x}$ 在 $(0,1]$ 上连续；$x\to0^+$ 时 $x\ln x\to0$，故 $x^{-x}\to1$。补充定义后它在 $[0,1]$ 上连续，所以这是通常的定积分，而不是需要判敛的瑕积分。题目的实质是**函数项级数的逐项积分**。

路线分三步：

1. **展开**：指数函数的 Maclaurin 级数 $e^u=\sum_{k\ge0}\dfrac{u^k}{k!}$ 对一切实数 $u$ 成立，取 $u=-x\ln x$（[[ANL-EX-019]]）。
2. **验证一致收敛**：逐项积分要求一致收敛（[[ANL-THM-045]]）。关键观察是 $u=-x\ln x$ 在 $(0,1]$ 上**有界**：$x\ln x$ 的最小值是 $-\dfrac1e$，所以 $|x\ln x|\le\dfrac1e$。于是第 $k$ 项被 $\dfrac{(1/e)^k}{k!}$ 控制，而 $\sum\dfrac{(1/e)^k}{k!}=e^{1/e}$ 收敛，Weierstrass M-判别法（[[ANL-THM-044]]）正好可用。
3. **逐项计算**：$\int_0^1(-x\ln x)^k dx$ 用换元 $u=-\ln x$（[[ANL-EX-012]]）化为 $\int_0^{+\infty}u^k e^{-(k+1)u}du$，再用分部积分（[[ANL-THM-034]]）递推。整理指标即得 $\sum n^{-n}$。

为什么不能直接对 $x^{-x}$ 求原函数？因为它没有初等原函数；而"指数函数展开成级数"这条路恰好把超越的被积函数拆成可逐项计算的幂乘对数的积分，这是本题的技巧核心。

## 证明 / 解答

### 第一步：被积函数在零点的连续延拓

设 $f(x)=x^{-x}=e^{-x\ln x}$（$0<x\le1$）。先证 $\lim_{x\to0^+}x\ln x=0$：令 $u=-\ln x\to+\infty$，则 $x=e^{-u}$，
$$
x\ln x=-ue^{-u}.
$$
由 $e^u\ge\dfrac{u^2}{2}$（$u\ge0$）得 $0\le ue^{-u}\le\dfrac2u\to0$，故 $x\ln x\to0$，于是 $f(x)\to e^0=1$。

补充定义 $f(0)=1$。$f$ 在 $(0,1]$ 上由连续函数的复合与乘积保持连续可得连续；在 $x=0$ 处由上述极限连续。因此 $f$ 在 $[0,1]$ 上连续，$\int_0^1x^{-x}dx$ 是通常的定积分。

### 第二步：展开为函数项级数

对任意实数 $u$ 有 $e^u=\sum_{k=0}^{\infty}\dfrac{u^k}{k!}$（[[ANL-EX-019]]）。取 $u=-x\ln x$，得
$$
x^{-x}=\sum_{k=0}^{\infty}\frac{(-x\ln x)^k}{k!},\qquad 0<x\le1.
$$

### 第三步：用 M-判别法证明一致收敛

先估 $x\ln x$。设 $h(x)=x\ln x$，则 $h'(x)=\ln x+1$，故 $h$ 在 $x=\dfrac1e$ 处取最小值
$$
h\left(\frac1e\right)=\frac1e\ln\frac1e=-\frac1e.
$$
又 $h(0^+)=0$、$h(1)=0$，所以
$$
-\frac1e\le x\ln x\le0,\qquad |x\ln x|\le\frac1e.
$$
于是对 $0<x\le1$，
$$
\left|\frac{(-x\ln x)^k}{k!}\right|\le M_k:=\frac{(1/e)^k}{k!},\qquad \sum_{k=0}^{\infty}M_k=e^{1/e}<+\infty.
$$
在 $x=0$ 处把各项连续延拓：$k=0$ 的项取 $1$，$k\ge1$ 的项取 $0$，上式仍成立。由 Weierstrass M-判别法（[[ANL-THM-044]]），级数 $\sum\dfrac{(-x\ln x)^k}{k!}$ 在 $[0,1]$ 上一致收敛。

### 第四步：逐项积分

级数各项在 $[0,1]$ 上连续且一致收敛，由逐项积分定理（[[ANL-THM-045]]），
$$
\int_0^1x^{-x}\,dx=\sum_{k=0}^{\infty}\frac{1}{k!}\int_0^1(-x\ln x)^k\,dx.
$$

### 第五步：计算单项积分

记 $A_k=\displaystyle\int_0^1(-x\ln x)^k dx$。作换元 $u=-\ln x$，即 $x=e^{-u}$、$dx=-e^{-u}du$（[[ANL-EX-012]]）；当 $x:0\to1$ 时 $u:+\infty\to0$，且 $-x\ln x=e^{-u}\cdot u=ue^{-u}$。故
$$
A_k=\int_{+\infty}^{0}(ue^{-u})^k(-e^{-u})\,du=\int_0^{+\infty}u^k e^{-(k+1)u}\,du.
$$
对固定 $m>0$，记 $J_k(m)=\displaystyle\int_0^{+\infty}u^k e^{-mu}du$。由分部积分（[[ANL-THM-034]]），
$$
J_k(m)=\left[-\frac{u^k}{m}e^{-mu}\right]_0^{+\infty}+\frac{k}{m}\int_0^{+\infty}u^{k-1}e^{-mu}\,du=\frac{k}{m}J_{k-1}(m),
$$
其中边界项当 $u\to+\infty$ 时由指数衰减趋于零、在 $u=0$ 处为零。又 $J_0(m)=\dfrac1m$，递推得
$$
J_k(m)=\frac{k!}{m^{k+1}}.
$$
取 $m=k+1$，得
$$
A_k=\frac{k!}{(k+1)^{k+1}}.
$$

### 第六步：求和并平移指标

把第五步的结果代回第四步：
$$
\int_0^1x^{-x}\,dx=\sum_{k=0}^{\infty}\frac{1}{k!}\cdot\frac{k!}{(k+1)^{k+1}}
=\sum_{k=0}^{\infty}\frac{1}{(k+1)^{k+1}}
=\sum_{n=1}^{\infty}\frac{1}{n^n},
$$
最后一步令 $n=k+1$。$\blacksquare$

### 第七步：数值与收敛速度

数项级数 $\sum n^{-n}$ 收敛很快：由根值判别法，$\sqrt[n]{n^{-n}}=\dfrac1n\to0$。前几项为
$$
1+\frac14+\frac1{27}+\frac1{256}+\frac1{3125}+\cdots\approx1.2912859.
$$
第一项 $n=1$ 贡献 $1$，第二项贡献 $\dfrac14$，第三项贡献 $\dfrac1{27}\approx0.037$，其余项随 $n$ 迅速变小；因此这个级数是高精度计算该积分的实用公式。

## 关键技巧

- **找一致收敛的控制级数**：$|x\ln x|\le\dfrac1e$ 是本题最关键的一步估计，它把逐项积分的合法性一步落实。
- **指数展开 + 逐项积分**：没有初等原函数的 $x^{-x}$ 被拆成 $\sum(-x\ln x)^k/k!$，每一项都能显式计算。
- **换元 $x=e^{-u}$**：把 $\ln x$ 化成线性因子，把幂乘对数的积分变成 $\Gamma$ 型积分 $\int_0^\infty u^k e^{-(k+1)u}du$。
- **分部积分递推**：$J_k(m)=\dfrac{k}{m}J_{k-1}(m)$ 与 $J_0(m)=\dfrac1m$ 给出 $J_k(m)=\dfrac{k!}{m^{k+1}}$。
- **指标平移**：$\sum_{k\ge0}\dfrac1{(k+1)^{k+1}}=\sum_{n\ge1}\dfrac1{n^n}$，注意 $k$ 从 $0$ 开始，对应 $n$ 从 $1$ 开始。

## 变式

- **变式 1**：用同样的方法证明 $\displaystyle\int_0^1x^x\,dx=\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^n}\approx0.7834305$。提示：$x^x=e^{x\ln x}$，逐项积分后 $\int_0^1x^k(\ln x)^k dx=(-1)^k\dfrac{k!}{(k+1)^{k+1}}$，符号交替出现。
- **变式 2**：证明对任意实数 $\alpha$，$\displaystyle\int_0^1x^{\alpha x}\,dx=\sum_{n=1}^{\infty}\frac{(-\alpha)^{n-1}}{n^n}$。提示：把变式 1 的推导中的 $\alpha$ 保留为参数即可；$\alpha=-1$ 与 $\alpha=1$ 分别回到本题与变式 1。
- **变式 3**：由本题与变式 1 推出奇数项级数 $\displaystyle\sum_{n\text{ 为奇数}}\frac1{n^n}=\frac12\left(\sum_{n\ge1}n^{-n}+\sum_{n\ge1}(-1)^{n+1}n^{-n}\right)\approx1.0373583$。提示：两个级数相加时偶数项相消、奇数项加倍。
- **变式 4**：讨论本题的证明能否推广到 $\displaystyle\int_0^1x^{-ax}\,dx$（$a>0$ 为常数），并写出对应的级数。提示：$|ax\ln x|\le\dfrac{a}{e}$，M-判别法仍可用；答案为 $\sum_{n\ge1}\dfrac{a^{n-1}}{n^n}$。

## 链接

- 演示定理：[[ANL-THM-045]] 一致收敛与逐项积分
- 关键判别法：[[ANL-THM-044]] Weierstrass M-判别法
- 计算工具：[[ANL-THM-034]] 分部积分法、[[ANL-EX-012]] 换元积分典型范例
- 相关展开：[[ANL-EX-019]] 常见初等函数的 Maclaurin 展开
- 相邻条目：[[ANL-EX-022]] 斯特林公式、[[ANL-EX-025]] Frullani 积分
- 幂级数背景：[[ANL-THM-046]] 幂级数逐项求导与积分
