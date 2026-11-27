---
title: "欧拉常数：调和级数与对数的差"
type: example
id: ANL-EX-021
subject: analysis
chapter: 06-interesting-problems
tags:
  - 数列
  - 调和级数
  - 欧拉常数
  - 单调有界
depends:
  - ANL-THM-006
  - ANL-THM-041
  - ANL-EX-016
uses: []
status: stable
source: "经典问题（Euler–Mascheroni）；参考华东师范大学《数学分析》第5版 §12.2"
difficulty: 3
illustrates:
  - ANL-THM-006
related:
  - ANL-EX-022
  - ANL-EX-029
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

令 $H_n=\sum_{k=1}^{n}\frac1k$、$a_n=H_n-\ln n$。证明：

1. $a_n$ 单调递减且有下界，故 $\gamma=\lim_{n\to\infty}a_n$ 存在（此即欧拉常数）；
2. $0<\gamma<1$，并且可以精确到 $\frac12<\gamma<1$；
3. 给出 $\gamma\approx0.57721$ 的数值、部分和的误差估计，并讨论 $\gamma$ 是否为无理数。

## 分析

调和级数 $\sum1/k$ 发散（[[ANL-EX-016]]），但它与 $\ln n$ 同阶：由积分判别法（[[ANL-THM-041]]）的矩形比较，$H_n$ 与 $\ln n$ 只差一个"常数级"的量。为什么这个差会收敛？每增加一项，$H_n$ 增加 $\frac1{n+1}$，而 $\ln n$ 增加 $\ln(1+\frac1n)$，两者之差约为 $-\frac{1}{2n^2}$；其绝对值累计起来 $\sum\frac{1}{2n^2}$ 收敛，所以差应趋于有限值。这是"两个都趋于无穷的量，其差却收敛"的标准范例。

**存在性策略**：直接用单调有界定理（[[ANL-THM-006]]）。单调性归结为不等式 $\frac1{n+1}<\ln(1+\frac1n)$，它来自积分表示 $\ln(1+t)=\int_0^t\frac{du}{1+u}$；下界则来自 $H_n>\int_1^{n+1}\frac{dx}{x}=\ln(n+1)>\ln n$。

**精细下界策略**：单调有界只能给出 $\gamma\ge0$ 和 $\gamma<1$。要得到 $\gamma>\frac12$，关键是把 $a_n$ 改写成"$1$ 减去一串正项之和"：
$$
a_n=1-\sum_{k=1}^{n-1}\left[\ln\left(1+\frac1k\right)-\frac1{k+1}\right].
$$
这串正项每项约 $\frac{1}{2k^2}$，但其和可以精确地用一个更强的对数不等式压到 $\frac12$ 以下——这就是 $\gamma>\frac12$ 的来源。为什么恰好是 $\frac12$？因为 $a_n$ 的误差主项是 $\frac1{2n}$，$\gamma$ 相当于把这条下降曲线"外推"到 $n=\infty$ 后留下的常数部分；真实值 $0.5772\ldots$ 确实在 $\frac12$ 与 $1$ 之间。

## 证明 / 解答

### 第一步：两个对数不等式

**引理 1**：对一切 $t>0$，$\frac{t}{1+t}<\ln(1+t)<t$。**证明：** 由 $\ln(1+t)=\int_0^t\frac{du}{1+u}$，当 $0\le u\le t$ 时 $\frac{1}{1+t}\le\frac{1}{1+u}\le1$，两端积分即得（左端严格，因为被积函数在 $[0,t]$ 上不恒等于 $\frac1{1+t}$）。$\blacksquare$

取 $t=\frac1k$ 得
$$
\frac{1}{k+1}<\ln\left(1+\frac1k\right)<\frac1k. \tag{1}
$$

**引理 2**：对 $0<u\le1$，$\ln(1+u)<\frac{u}{1+u}+\frac{u^2}{2(1+u)}$。**证明：** 令 $h(u)=\frac{u}{1+u}+\frac{u^2}{2(1+u)}-\ln(1+u)$，则 $h(0)=0$，且
$$
h'(u)=\frac{1}{(1+u)^2}+\frac{2u+u^2}{2(1+u)^2}-\frac{1}{1+u}=\frac{u^2}{2(1+u)^2}>0\qquad(0<u\le1).
$$
故 $h$ 在 $[0,1]$ 上严格递增，$h(u)>0$。$\blacksquare$

在引理 2 中取 $u=\frac1k$，并记 $c_k:=\ln\left(1+\frac1k\right)-\frac1{k+1}$，则
$$
c_k<\frac{u^2}{2(1+u)}=\frac{1}{2k(k+1)},\qquad k\ge1. \tag{2}
$$
同时由 (1) 左半知 $c_k>0$。

### 第二步：单调有界，极限存在

由 $H_{n+1}-H_n=\frac1{n+1}$ 与 $\ln(n+1)-\ln n=\ln\left(1+\frac1n\right)$，
$$
a_{n+1}-a_n=\frac1{n+1}-\ln\left(1+\frac1n\right)<0,
$$
最后一步用了 (1) 的左半。故 $\{a_n\}$ 严格单调递减。另一方面，对每个 $k\ge1$，$\frac1k>\int_k^{k+1}\frac{dx}{x}$（因为 $\frac1x$ 在 $[k,k+1]$ 上严格小于 $\frac1k$），求和得 $H_n>\int_1^{n+1}\frac{dx}{x}=\ln(n+1)>\ln n$，故 $a_n=H_n-\ln n>0$。于是 $\{a_n\}$ 单调递减且有下界 $0$，由单调有界定理（[[ANL-THM-006]]），极限 $\gamma:=\lim_{n\to\infty}a_n=\inf_{n\ge1}a_n$ 存在，且 $\gamma\ge0$。又 $a_1=1$ 且 $a_2<a_1$，故 $\gamma\le a_2<1$。$\blacksquare$

### 第三步：望远镜重写与精细估计

把 $\ln n$ 按 $k$ 的差拆开：$\ln n=\sum_{k=2}^{n}\ln\frac{k}{k-1}=\sum_{j=1}^{n-1}\ln\left(1+\frac1j\right)$，而 $H_n=1+\sum_{j=1}^{n-1}\frac1{j+1}$。两式相减得望远镜形式
$$
a_n=1-\sum_{j=1}^{n-1}\left[\ln\left(1+\frac1j\right)-\frac1{j+1}\right]=1-\sum_{j=1}^{n-1}c_j. \tag{3}
$$
于是部分和 $C_{n-1}:=\sum_{j=1}^{n-1}c_j$ 满足 $C_{n-1}=1-a_n<1$。由于 $c_j>0$，正项级数 $\sum c_j$ 的部分和递增且有上界 $1$，故 $S:=\sum_{j=1}^{\infty}c_j\le1$。在 (3) 中令 $n\to\infty$，得
$$
\gamma=1-S. \tag{4}
$$
由 (2) 估计这个和：
$$
S<\sum_{j=1}^{\infty}\frac{1}{2j(j+1)}
=\frac12\sum_{j=1}^{\infty}\left(\frac1j-\frac1{j+1}\right)
=\frac12.
$$
再由 $S>0$，从 (4) 得到
$$
\frac12<\gamma<1. \tag{5}
$$
$\blacksquare$

### 第四步：数值、误差与无理性

由 (3)(4)，$a_n-\gamma=S-\sum_{j=1}^{n-1}c_j=\sum_{j=n}^{\infty}c_j$，用 (2) 得
$$
0<a_n-\gamma\le\sum_{j=n}^{\infty}\frac{1}{2j(j+1)}=\frac{1}{2n}. \tag{6}
$$
因此 $\gamma<a_n$ 且 $\gamma>a_n-\frac1{2n}$，把 $n$ 取大就能得到任意精度的区间估计。例如 $a_{10}=0.6263831609\ldots$、$a_{100}=0.5822073317\ldots$、$a_{1000}=0.5777155816\ldots$、$a_{10000}=0.5772656641\ldots$。用 $n=10000$ 的 (6) 得 $\gamma\in(0.57721566,0.57726567)$，取更精细的展开可得
$$
\gamma=0.5772156649015329\ldots
$$
（欧拉–马歇罗尼常数）。更精细的 Euler–Maclaurin 展开为
$$
a_n=\gamma+\frac{1}{2n}-\frac{1}{12n^2}+O\left(\frac{1}{n^3}\right), \tag{7}
$$
它说明了为什么 $\{a_n\}$ 收敛很慢（误差主项为 $\frac{1}{2n}$）。以 $n=10$ 检验：$a_{10}=0.6263831609\ldots$，而 $\gamma+\frac1{20}-\frac1{1200}=0.6263823316\ldots$，两者相差约 $8.3\times10^{-7}$，与 (7) 中 $O(n^{-3})$ 的项相符。

**关于无理性**：目前仍然不知道 $\gamma$ 是否为无理数，甚至不知道它是否为有理数；这是数学中著名的未解决问题之一。可以确定的是 $\frac12<\gamma<1$，且 $\gamma$ 与 $\Gamma$ 函数在 $1$ 处的取值有关：$\gamma=-\Gamma'(1)$（见变式 3）。

## 关键技巧

- **积分表示证对数不等式**：$\ln(1+t)=\int_0^t\frac{du}{1+u}$ 把比较两个数的大小转成比较被积函数的大小，是处理 $\ln(1+1/k)$ 的标准方法。
- **单调有界定理**：证明"两个发散量之差"收敛时，先证单调（比较增量），再证有界（与积分比较）。
- **望远镜重写**：把 $a_n$ 写成 $1-\sum c_k$，把一个"下界估计"问题转化为"正项级数的和小于 $\frac12$"，这是获得精细下界的关键一步。
- **用导数证明加强不等式**：引理 2 的证明只用到"构造辅助函数 + 求导判单调"，这类方法可系统地把 $\ln(1+u)$ 估计到二阶。
- **尾巴估计控制数值精度**：正项级数的 tail 被 $\frac1{2n}$ 控制，从而每一步都有严格的误差界。

## 变式

- **变式 1（另一个级数表示）**：证明 $\gamma=\sum_{k=1}^{\infty}\left(\frac1k-\ln\left(1+\frac1k\right)\right)$。提示：把 $\ln n$ 写成 $\sum_{k=1}^{n-1}\ln(1+1/k)$，则 $a_n=\sum_{k=1}^{n-1}\left[\frac1k-\ln(1+1/k)\right]+\frac1n$，再令 $n\to\infty$。
- **变式 2（部分和之差）**：证明 $\displaystyle\lim_{n\to\infty}(H_{2n}-H_n)=\ln2$。提示：用积分夹住 $\ln\frac{2n+1}{n+1}\le H_{2n}-H_n\le\ln2$，两端都趋于 $\ln2$，再用夹逼定理。这说明虽然 $H_n-\ln n$ 收敛，但"隔一段取差"仍会留下对数因子。
- **变式 3（更快的逼近与 Gamma 函数）**：证明 $\displaystyle\lim_{n\to\infty}\left(H_n-\ln\left(n+\frac12\right)\right)=\gamma$ 且误差为 $O(n^{-2})$；再证明 $\gamma=-\Gamma'(1)=-\int_0^{\infty}e^{-t}\ln t\,dt$（$\Gamma$ 见 [[ANL-EX-014]]）。提示：$\ln(n+\frac12)-\ln n=\ln\left(1+\frac1{2n}\right)$ 展开到二阶后与 (7) 比较；对 $\Gamma(x)=\int_0^{\infty}t^{x-1}e^{-t}\,dt$ 在 $x=1$ 处求导并展开 $\int_0^1 e^{-t}\ln t\,dt$。

## 链接

- 演示定理：[[ANL-THM-006]] 单调有界定理
- 依赖：[[ANL-THM-041]] 积分判别法、[[ANL-EX-016]] 调和级数发散与 p-级数敛散
- 相关：[[ANL-EX-022]] 斯特林公式、[[ANL-EX-029]] 肯普纳级数
- 延伸：[[ANL-EX-014]] 反常积分敛散性判别（含 Gamma 函数引入）、[[ANL-EX-020]] 巴塞尔问题
