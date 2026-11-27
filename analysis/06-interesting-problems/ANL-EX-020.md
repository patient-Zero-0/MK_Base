---
title: "巴塞尔问题：自然数平方倒数和"
type: example
id: ANL-EX-020
subject: analysis
chapter: 06-interesting-problems
tags:
  - 级数
  - 巴塞尔问题
  - 无穷乘积
  - 幂级数
depends:
  - ANL-DEF-037
  - ANL-EX-019
  - ANL-THM-045
  - ANL-THM-046
uses: []
status: stable
source: "经典问题（Euler, 1735）；参考华东师范大学《数学分析》第5版 §14.2"
difficulty: 4
illustrates:
  - ANL-THM-046
related:
  - ANL-EX-013
  - ANL-EX-027
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

证明 $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{\pi^2}{6}$，并说清两条思路：Euler 怎样由正弦的无穷乘积比较系数猜出这个值，以及一条不依赖无穷乘积的完整严格推导。最后给出数值、收敛速度与若干变式。

## 分析

这个级数收敛并不难：$p=2>1$，由 [[ANL-EX-016]] 的 $p$-级数结论即可。难的是**和等于多少**。前几项部分和 $S_{10}\approx 1.5498$、$S_{100}\approx 1.63498$，增长极慢，凭数值看不出 $\pi^2/6\approx 1.6449$ 这样的答案。

Euler 的出发点是**多项式根与系数的关系**。若一个常数项为 $1$ 的多项式以 $\pm x_1,\dots,\pm x_N$ 为零点，则
$$
p(x)=\prod_{k=1}^{N}\left(1-\frac{x^2}{x_k^2}\right)=1-\left(\sum_{k=1}^{N}\frac{1}{x_k^2}\right)x^2+\cdots,
$$
于是 $x^2$ 的系数就是各零点平方倒数之和的相反数。而 $\sin(\pi x)/(\pi x)$ 的零点恰为 $x=\pm1,\pm2,\dots$，它在 $x=0$ 处取值 $1$，形式上就像一个常数项为 $1$ 的「无穷次多项式」。把上述关系照搬过去得到 $\frac{\sin\pi x}{\pi x}=\prod_{n=1}^{\infty}\left(1-\frac{x^2}{n^2}\right)$；左边在 $x=0$ 附近的 Maclaurin 展开（[[ANL-EX-019]]）是 $1-\frac{\pi^2}{6}x^2+\cdots$，比较 $x^2$ 的系数立即得到答案。

这条推导有两处要落实：其一，无穷乘积本身不是多项式，恒等式必须交代来源；其二，把无穷乘积乘开再比较系数，需要级数 $\sum 1/n^2$ 的绝对收敛性（它确实收敛）。下面第一步把乘积的来源说清楚——它可由 Fourier 级数得到的部分分式展开逐项积分验证；但从第二步起给出一条完全独立的严格证明，不再依赖乘积。

严格路线来自一个漂亮的二重积分表示。对 $|t|<1$ 有几何级数 $\frac{1}{1-t}=\sum_{n\ge0}t^n$；在正方形 $[0,r]^2$（$r<1$）上取 $t=xy$，则
$$
\iint_{[0,r]^2}(xy)^n\,dx\,dy=\left(\int_0^r x^n\,dx\right)^2=\frac{r^{2n+2}}{(n+1)^2},
$$
求和得 $I_r:=\sum_{k\ge1}\frac{r^{2k}}{k^2}$，再令 $r\to1^-$ 即得 $\sum 1/k^2$。剩下的任务是把 $I=\iint_{[0,1]^2}\frac{dx\,dy}{1-xy}$ 算出来。直接对 $x$ 积分会得到 $\int_0^1-\ln(1-y)/y\,dy$，又回到原级数；改用对称换元 $x=u+v$、$y=u-v$，分母变成 $1-u^2+v^2$，对 $v$ 积分出现反正切，再按 $u\le1/2$ 与 $u\ge1/2$ 分段，分别化成反正弦积分与简单的角积分，两段之和恰为 $\pi^2/6$。想到这个换元的原因是它把乘积 $xy$ 变成平方差 $u^2-v^2$，从而分母成为 $a^2+v^2$ 的标准形式。

## 证明 / 解答

### 第一步：Euler 的无穷乘积与系数比较

Euler 使用的恒等式是
$$
\frac{\sin\pi x}{\pi x}=\prod_{n=1}^{\infty}\left(1-\frac{x^2}{n^2}\right),\qquad |x|<1. \tag{1}
$$
它的一个可查验来源如下。由 $\cos(tx)$ 在 $[0,\pi]$ 上的 Fourier 余弦级数在 $t=\pi$ 处取值，可得部分分式展开
$$
\pi\cot(\pi x)=\frac1x+\sum_{n=1}^{\infty}\frac{2x}{x^2-n^2},\qquad x\notin\mathbb{Z}. \tag{2}
$$
固定 $r\in(0,1)$。当 $|x|\le r$ 时 $\left|\frac{2x}{x^2-n^2}\right|\le\frac{2r}{n^2-r^2}$（$n\ge2$），而 $\sum_{n\ge2}\frac{1}{n^2-r^2}$ 收敛，故 (2) 右端级数在 $[-r,r]$ 上一致收敛，可以逐项积分（[[ANL-THM-045]]）。对 $0<x\le r$，由 $\pi\cot(\pi t)-\frac1t=\frac{d}{dt}\ln\frac{\sin\pi t}{\pi t}$ 得
$$
\ln\frac{\sin\pi x}{\pi x}=\int_0^x\left(\pi\cot(\pi t)-\frac1t\right)dt=\sum_{n=1}^{\infty}\int_0^x\frac{2t}{t^2-n^2}\,dt=\sum_{n=1}^{\infty}\ln\left(1-\frac{x^2}{n^2}\right),
$$
两边取指数即得 (1)；（该恒等式事实上对整个实轴成立，但下面的系数比较只需要 $|x|<1$。）右端逐项积分由上述一致收敛保证，且被积函数在 $t=0$ 处连续延拓为 $0$。

现在比较系数。由 $\sum 1/n^2$ 收敛，乘积可以乘开：
$$
\prod_{n=1}^{\infty}\left(1-\frac{x^2}{n^2}\right)=1-\left(\sum_{n=1}^{\infty}\frac1{n^2}\right)x^2+\cdots.
$$
另一方面（[[ANL-EX-019]]）
$$
\frac{\sin\pi x}{\pi x}=\sum_{k=0}^{\infty}\frac{(-1)^k\pi^{2k}}{(2k+1)!}x^{2k}=1-\frac{\pi^2}{6}x^2+\frac{\pi^4}{120}x^4-\cdots.
$$
比较 $x^2$ 项的系数，得到 $\displaystyle\sum_{n=1}^{\infty}\frac1{n^2}=\frac{\pi^2}{6}$。这一步的合法性在于：乘积展开式中 $x^2$ 的系数是绝对收敛级数 $\sum1/n^2$ 的和，与展开次序无关。于是只要乘积恒等式成立，答案就确定了；下面给出一条不依赖 (1) 的证明。

### 第二步：把级数写成二重积分

设 $0<r<1$，$D_r=[0,r]\times[0,r]$。在 $D_r$ 上 $0\le xy\le r^2<1$，故 $\frac{1}{1-xy}=\sum_{n=0}^{\infty}(xy)^n$，且余项满足
$$
\left|\sum_{n=0}^{N}(xy)^n-\frac{1}{1-xy}\right|=\frac{(xy)^{N+1}}{1-xy}\le\frac{r^{2N+2}}{1-r^2},
$$
右端与 $(x,y)$ 无关，故级数在 $D_r$ 上一致收敛。逐项积分得
$$
I_r:=\iint_{D_r}\frac{dx\,dy}{1-xy}
=\sum_{n=0}^{\infty}\frac{r^{2n+2}}{(n+1)^2}
=\sum_{k=1}^{\infty}\frac{r^{2k}}{k^2}. \tag{3}
$$
右端对每个 $r\in(0,1)$ 收敛（与 [[ANL-EX-016]] 中 $p=2$ 的级数比较即可）。被积函数非负，$I_r$ 随 $r$ 增大而上升；令 $r\to1^-$，左端趋于二重反常积分 $I:=\iint_{[0,1]^2}\frac{dx\,dy}{1-xy}$，右端则对每个固定的 $N$ 有 $\sum_{k=1}^{N}\frac{r^{2k}}{k^2}\to\sum_{k=1}^{N}\frac1{k^2}$，再让 $N\to\infty$，由 $\sum1/k^2$ 收敛与非负性得右端趋于 $\sum_{k=1}^{\infty}1/k^2$。因此
$$
I=\sum_{k=1}^{\infty}\frac{1}{k^2}. \tag{4}
$$

### 第三步：对称换元计算积分

作换元 $x=u+v$、$y=u-v$，其雅可比行列式为 $\frac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}1&1\\1&-1\end{vmatrix}=-2$，绝对值为 $2$。正方形 $[0,1]^2$ 被映为区域
$$
\Delta=\{(u,v):0\le u\le1,\ -\min(u,1-u)\le v\le\min(u,1-u)\},
$$
并且 $xy=u^2-v^2$。于是
$$
I=\iint_{\Delta}\frac{2\,du\,dv}{1-u^2+v^2}. \tag{5}
$$
被积函数只在 $(u,v)=(1,0)$ 附近无界，但下面算出的累次积分有限，故按反常二重积分理解即可。

当 $0\le u\le\frac12$ 时，$v$ 的范围是 $[-u,u]$。记 $a=\sqrt{1-u^2}$，则
$$
\int_{-u}^{u}\frac{2\,dv}{a^2+v^2}=\frac{4}{a}\arctan\frac{u}{a}=\frac{4\arcsin u}{\sqrt{1-u^2}},
$$
其中用了 $\arctan\left(u/\sqrt{1-u^2}\right)=\arcsin u$。这一段贡献为
$$
I_1=\int_0^{1/2}\frac{4\arcsin u}{\sqrt{1-u^2}}\,du
=2\Big[(\arcsin u)^2\Big]_0^{1/2}
=2\left(\frac{\pi}{6}\right)^2=\frac{\pi^2}{18}.
$$
当 $\frac12\le u\le1$ 时，$v$ 的范围是 $[u-1,1-u]$，同理
$$
\int_{u-1}^{1-u}\frac{2\,dv}{1-u^2+v^2}=\frac{4}{\sqrt{1-u^2}}\arctan\sqrt{\frac{1-u}{1+u}}.
$$
作代换 $u=\cos\theta$（$\theta\in[0,\pi/3]$），则 $\sqrt{1-u^2}=\sin\theta$，$\arctan\sqrt{(1-u)/(1+u)}=\arctan\tan(\theta/2)=\theta/2$，$du=-\sin\theta\,d\theta$，于是
$$
I_2=\int_0^{\pi/3}2\theta\,d\theta=\frac{\pi^2}{9}.
$$
合并得 $I=I_1+I_2=\frac{\pi^2}{18}+\frac{\pi^2}{9}=\frac{\pi^2}{6}$；结合 (4) 即证。$\blacksquare$

### 第四步：数值与收敛速度

由上式，$\pi^2/6=1.6449340668\ldots$。部分和 $S_N=\sum_{n=1}^{N}1/n^2$ 的误差可由积分夹住：$\frac{1}{N+1}<\frac{\pi^2}{6}-S_N<\frac1N$，因为对递减函数 $1/x^2$ 有 $\int_{N+1}^{\infty}x^{-2}\,dx\le\sum_{n=N+1}^{\infty}n^{-2}\le\int_N^{\infty}x^{-2}\,dx$。例如 $S_{10}=1.5497677\ldots$，误差介于 $1/11$ 与 $1/10$ 之间；$S_{100}=1.6349839\ldots$，误差约为 $0.00995$。可见收敛速度只有 $O(1/N)$。

## 关键技巧

- **无穷乘积与系数比较**：抓住 $\sin(\pi x)/(\pi x)$ 的零点，把「无穷次多项式」的根与系数关系当作发现工具，这是 Euler 原始思路的核心。
- **部分分式到乘积**：$\pi\cot(\pi x)$ 的展开（由 Fourier 级数得到）逐项积分给出乘积恒等式，说明乘积不是凭空假设，而是可逐项查验的。
- **二重积分表示**：把 $1/(1-xy)$ 展开成几何级数，使数项级数 $\sum1/n^2$ 变成可积函数的积分，把求和问题转成计算面积。
- **对称换元与分段**：$x=u+v$、$y=u-v$ 把 $xy$ 变成平方差 $u^2-v^2$，分母成为 $a^2+v^2$；按 $u\le1/2$ 与 $u\ge1/2$ 分段，是因为 $v$ 的上下界表达式在中点改变。
- **用积分估计尾巴**：单调函数的和与积分互相夹住，既能证明收敛，也能给出部分和误差的量级。

## 变式

- **变式 1（奇数平方倒数和）**：由偶数项之和 $\sum_{n\ge1}(2n)^{-2}=\frac14\sum1/n^2=\frac{\pi^2}{24}$，得 $\sum_{n=1}^{\infty}\frac{1}{(2n-1)^2}=\frac{\pi^2}{6}-\frac{\pi^2}{24}=\frac{\pi^2}{8}$。
- **变式 2（$\zeta(4)$）**：用乘积 (1) 中 $x^4$ 的系数。左边展开的 $x^4$ 系数为 $\frac{\pi^4}{120}$，右边乘积的 $x^4$ 系数为 $\sum_{m<n}\frac{1}{m^2n^2}=\frac12\left[\left(\sum\frac1{n^2}\right)^2-\sum\frac1{n^4}\right]$。代入 $\sum1/n^2=\pi^2/6$：
  $$
  \frac{\pi^4}{120}=\frac12\left(\frac{\pi^4}{36}-\zeta(4)\right)
  \implies
  \zeta(4)=\frac{\pi^4}{36}-\frac{\pi^4}{60}=\frac{\pi^4}{90}.
  $$
- **变式 3（交错平方级数）**：奇数项和减偶数项和，得 $\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^2}=\frac{\pi^2}{8}-\frac{\pi^2}{24}=\frac{\pi^2}{12}$。
- **变式 4（同类积分）**：用同样的几何级数方法证明 $\iint_{[0,1]^2}\frac{dx\,dy}{1-x^2y^2}=\sum_{n=0}^{\infty}\frac{1}{(2n+1)^2}=\frac{\pi^2}{8}$。提示：把 $x^2y^2$ 看作新的乘积变量，所得级数正是变式 1 的奇数平方倒数和。

## 链接

- 演示定理：[[ANL-THM-046]] Cauchy–Hadamard 公式与幂级数逐项求导、积分
- 依赖与前置：[[ANL-DEF-037]] 幂级数、[[ANL-EX-019]] 常见初等函数的 Maclaurin 展开
- 相关：[[ANL-EX-013]] 分部积分典型范例（含 Wallis 公式）、[[ANL-EX-027]] 莱布尼茨级数与阿贝尔极限定理
- 后续：[[ANL-EX-021]] 欧拉常数、[[ANL-EX-022]] 斯特林公式
- 级数判别：[[ANL-EX-016]] 调和级数发散与 p-级数敛散
