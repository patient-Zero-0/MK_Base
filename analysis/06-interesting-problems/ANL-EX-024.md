---
title: "魏尔斯特拉斯函数：处处连续却处处不可导"
type: example
id: ANL-EX-024
subject: analysis
chapter: 06-interesting-problems
tags:
  - 连续
  - 不可导
  - 一致收敛
  - 反例
depends:
  - ANL-THM-044
  - ANL-THM-045
  - ANL-DEF-014
  - ANL-THM-017
uses: []
status: stable
source: "Weierstrass (1872)；参考华东师范大学《数学分析》第5版 §13.2"
difficulty: 5
illustrates:
  - ANL-THM-045
related:
  - ANL-EX-023
  - ANL-EX-008
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

设 $0<a<1$，$b$ 为奇数且为正整数，满足 $ab>1+\frac{3\pi}{2}$。定义
$$
f(x)=\sum_{n=0}^{\infty}a^n\cos\left(b^n\pi x\right),\qquad x\in\mathbb{R}.
$$
证明：

1. $f$ 在 $\mathbb{R}$ 上连续（事实上由 Weierstrass 判别法一致收敛）；
2. 对任意 $x\in\mathbb{R}$，$f$ 在 $x$ 处不可导，即 $f$ 处处连续却处处不可导。

## 分析

连续性是 Weierstrass 判别法（[[ANL-THM-044]]）的直接应用：通项被 $a^n$ 控制，而 $\sum a^n$ 收敛。真正的困难在于不可导。

形式上逐项求导会得到
$$
\sum_{n=0}^{\infty}-\pi(ab)^n\sin\left(b^n\pi x\right),
$$
它的通项振幅 $\pi(ab)^n$ 指数增长（$ab>1$），所以导数级数根本不可能一致收敛。这正说明逐项求导定理（[[ANL-THM-045]] 的第三条）不能使用，也暗示原函数可能根本不可导。因此必须回到导数的定义（[[ANL-DEF-014]]）：对固定的 $x$，构造一列 $h_m\to0$（$h_m\ne0$）使差商无界。

构造 $h_m$ 的思想是"让高频项对齐"。$f$ 的第 $n$ 项是振幅 $a^n$、频率 $b^n$ 的余弦波。若取 $h_m$ 使 $b^m(x+h_m)$ 为整数，则对一切 $n\ge m$ 都有 $b^n(x+h_m)\in\mathbb{Z}$，这些高频项在 $x+h_m$ 处取 $\pm1$；而 $x$ 处的对应值可写成 $\pm\cos\left(\pi b^{n-m}r_m\right)$，两者之差的绝对值为 $1+\cos\left(\pi b^{n-m}r_m\right)$。由于 $b$ 是奇数，所有 $n\ge m$ 项的差还共享同一个符号因子，可以相加而不是相消；其中 $n=m$ 这一项就贡献了至少 $a^m$。低频项（$n<m$）的振幅小、频率也小，用中值不等式即可控制。条件 $ab>1+\frac{3\pi}{2}$ 恰好保证"高频项给出的 $a^m$ 增益"大于"低频项的总误差"，同时 $|h_m|$ 又足够小，使差商按 $(ab)^m\to\infty$ 增长。

## 证明 / 解答

### 第一步：一致收敛与连续性

对一切 $x\in\mathbb{R}$ 和 $n\ge0$，
$$
\left|a^n\cos\left(b^n\pi x\right)\right|\le a^n,
$$
而 $\sum_{n=0}^{\infty}a^n=\frac{1}{1-a}$ 收敛。由 Weierstrass 判别法（[[ANL-THM-044]]），级数在 $\mathbb{R}$ 上一致（且绝对）收敛。每个通项连续，由一致收敛与连续性的交换（[[ANL-THM-045]] 第一条），和函数 $f$ 在 $\mathbb{R}$ 上连续。同时 $|f(x)|\le\frac{1}{1-a}$。

### 第二步：逐项求导不可用

由求导四则运算（[[ANL-THM-017]]），第 $n$ 项的形式导数为 $-\pi(ab)^n\sin\left(b^n\pi x\right)$，它在 $\mathbb{R}$ 上的振幅为 $\pi(ab)^n\to\infty$（因 $ab>1$）。一致收敛的必要条件是通项一致趋于零，而这里 $\sup_x\left|\pi(ab)^n\sin(b^n\pi x)\right|=\pi(ab)^n$ 不趋于零，故导数级数不可能一致收敛。因此不能使用逐项求导定理（[[ANL-THM-045]] 第三条）来断言 $f$ 可导。下面直接从差商定义出发处理。

### 第三步：构造逼近序列

固定 $x\in\mathbb{R}$。对每个 $m\ge1$，取整数 $k_m$ 使 $\left|b^mx-k_m\right|\le\frac12$，并记 $r_m=b^mx-k_m\in\left[-\frac12,\frac12\right]$。令 $h_m=\frac{k_m+1-b^mx}{b^m}=\frac{1-r_m}{b^m}$，则
$$
b^m(x+h_m)=k_m+1\in\mathbb{Z},\qquad
\frac{1}{2b^m}\le|h_m|\le\frac{3}{2b^m}. \tag{1}
$$
特别地 $h_m\ne0$ 且 $h_m\to0$。

### 第四步：高频项的符号对齐

设 $n\ge m$。记 $b^n(x+h_m)=b^{n-m}(k_m+1)$，它是整数。由于 $b$ 为奇数，$b^{n-m}$ 也是奇数，故
$$
\cos\left(b^n\pi(x+h_m)\right)=(-1)^{b^{n-m}(k_m+1)}=(-1)^{k_m+1}.
$$
另一方面，
$$
\cos\left(b^n\pi x\right)=\cos\left(\pi b^{n-m}(k_m+r_m)\right)
=(-1)^{k_m}\cos\left(\pi b^{n-m}r_m\right),
$$
其中用了 $b^{n-m}k_m$ 为整数。两式相减：
$$
\cos\left(b^n\pi(x+h_m)\right)-\cos\left(b^n\pi x\right)
=(-1)^{k_m+1}\left[1+\cos\left(\pi b^{n-m}r_m\right)\right]. \tag{2}
$$
关键在于 (2) 右端方括号内的因子非负，且前面的符号因子 $(-1)^{k_m+1}$ 与 $n$ 无关。因此对 $n\ge m$ 求和时，各项同号，可以取绝对值并把每一项都放大：
$$
\left|\sum_{n=m}^{\infty}a^n\left[\cos\left(b^n\pi(x+h_m)\right)-\cos\left(b^n\pi x\right)\right]\right|
=\sum_{n=m}^{\infty}a^n\left[1+\cos\left(\pi b^{n-m}r_m\right)\right].
$$
只保留 $n=m$ 这一项，并注意 $|r_m|\le\frac12$ 推出 $\cos(\pi r_m)\ge0$，得
$$
\left|\sum_{n=m}^{\infty}a^n\left[\cdots\right]\right|
\ge a^m\left[1+\cos(\pi r_m)\right]\ge a^m. \tag{3}
$$

### 第五步：低频项的误差控制

设 $n<m$。由中值定理与 $|\sin u|\le1$ 得 $\left|\cos u-\cos v\right|\le|u-v|$，于是
$$
\left|\sum_{n=0}^{m-1}a^n\left[\cos\left(b^n\pi(x+h_m)\right)-\cos\left(b^n\pi x\right)\right]\right|
\le\pi|h_m|\sum_{n=0}^{m-1}(ab)^n
\le\pi|h_m|\frac{(ab)^m}{ab-1}.
$$
再用 (1) 中 $|h_m|\le\frac{3}{2b^m}$：
$$
\left|\sum_{n=0}^{m-1}a^n\left[\cdots\right]\right|
\le\frac{3\pi}{2}\cdot\frac{a^m}{ab-1}. \tag{4}
$$

### 第六步：差商无界，故处处不可导

把 (3) 与 (4) 合并，利用三角不等式（把整个级数拆成 $n<m$ 与 $n\ge m$ 两段）：
$$
\left|f(x+h_m)-f(x)\right|
\ge a^m-\frac{3\pi}{2}\cdot\frac{a^m}{ab-1}
=a^m\left(1-\frac{3\pi}{2(ab-1)}\right).
$$
由条件 $ab>1+\frac{3\pi}{2}$ 得 $ab-1>\frac{3\pi}{2}$，故
$$
c:=1-\frac{3\pi}{2(ab-1)}>0.
$$
于是
$$
\left|\frac{f(x+h_m)-f(x)}{h_m}\right|
\ge\frac{c\,a^m}{|h_m|}
\ge\frac{2c}{3}(ab)^m\longrightarrow+\infty,
$$
最后一步用了 (1) 中 $|h_m|\le\frac{3}{2b^m}$。由 $ab>1$，右端趋于无穷。即沿 $h_m\to0$ 的差商无界，故 $f$ 在 $x$ 处不可导（否则差商应收敛到有限数 $f'(x)$，[[ANL-DEF-014]]）。由 $x$ 的任意性，$f$ 处处不可导。$\blacksquare$

## 关键技巧

- **M-判别法先解决连续性**：把"一致收敛"与"连续性"两件事拆开，先证级数一致收敛，再用一致收敛的连续性定理。
- **从差商定义出发**：当逐项求导无望（导数级数振幅发散）时，直接构造使差商无界的点列。
- **相位对齐**：取 $h_m$ 使 $b^m(x+h_m)$ 成为整数，从而对一切 $n\ge m$ 都有 $b^n(x+h_m)\in\mathbb{Z}$，让高频项在 $x+h_m$ 处取 $\pm1$；其中 $n=m$ 这一项与 $x$ 处的值反号，单独就贡献 $a^m$。
- **利用奇偶性统一符号**：$b$ 为奇数保证 $(-1)^{b^{n-m}(k_m+1)}=(-1)^{k_m+1}$ 与 $n$ 无关，使高频项同号、不会相互抵消。
- **低频项用中值不等式**：$|\cos u-\cos v|\le|u-v|$ 把低频误差压到 $O(a^m)$，再由 $ab>1+\frac{3\pi}{2}$ 保证主项胜出。

## 变式

- **变式 1（临界情形）**：若 $ab<1$，证明 $f$ 在 $\mathbb{R}$ 上连续可导，且
  $$
  f'(x)=-\pi\sum_{n=0}^{\infty}(ab)^n\sin\left(b^n\pi x\right).
  $$
  提示：此时 $\sum(ab)^n$ 收敛，导数级数由 M-判别法一致收敛，再用逐项求导定理（[[ANL-THM-045]] 第三条）。这说明 $ab<1$ 时 $f$ 还是连续可导的，而 $ab$ 足够大时它处处不可导；$ab>1+\frac{3\pi}{2}$ 只是 Weierstrass 原证明所需的偏强充分条件。
- **变式 2（Hölder 连续性）**：证明存在常数 $C>0$ 使
  $$
  |f(x)-f(y)|\le C|x-y|^{\alpha},\qquad \alpha=\frac{\log(1/a)}{\log b}.
  $$
  提示：取 $m$ 使 $b^{-m-1}<|x-y|\le b^{-m}$，把级数按 $n\le m$ 与 $n>m$ 拆开：前者用中值不等式得 $O((ab)^m|x-y|)$，后者用 $|f_n|\le a^n$ 得 $O(a^m)$，再利用 $a^m\approx|x-y|^{\alpha}$。
- **变式 3（在原点处直接验证）**：取 $h_m=b^{-m}$，证明
  $$
  \lim_{m\to\infty}\frac{f(h_m)-f(0)}{h_m}=-\infty,
  $$
  从而 $f'(0)$ 不存在。提示：对 $n\ge m$，$b^nh_m=b^{n-m}$ 为奇数，故 $\cos(b^n\pi h_m)=-1$，这些项求和得 $-\frac{2a^m}{1-a}$；对 $n<m$，由 $1-\cos u\le\frac{u^2}{2}$ 得 $\left|\cos(b^n\pi h_m)-1\right|\le\frac{\pi^2}{2}b^{-2(m-n)}$，故第一段之和为 $O(a^m)$（这里用到条件可推出 $ab^2>1$）。乘以 $b^m$ 后，第二段给出 $-\frac{2(ab)^m}{1-a}$，是趋于负无穷的主项。

## 链接

- 演示定理：[[ANL-THM-045]] 一致收敛与连续、可积、可导的交换
- 依赖：[[ANL-THM-044]] Weierstrass 判别法、[[ANL-DEF-014]] 导数、[[ANL-THM-017]] 求导四则运算
- 相关：[[ANL-EX-023]] 康托集与康托函数（另一种连续但"病态"的函数）、[[ANL-EX-008]] 用定义求三类初等函数的导数
- 延伸：[[ANL-THM-022]] Lagrange 中值定理、[[ANL-DEF-024]] 一致连续、[[ANL-THM-015]] Cantor 定理
