---
title: "莱布尼茨级数与阿贝尔极限定理"
type: example
id: ANL-EX-027
subject: analysis
chapter: 06-interesting-problems
tags:
  - 级数
  - 幂级数
  - 阿贝尔定理
  - 莱布尼茨级数
depends:
  - ANL-THM-042
  - ANL-THM-046
  - ANL-EX-019
  - ANL-THM-045
uses: []
status: stable
source: "经典问题（Abel）；参考华东师范大学《数学分析》第5版 §14.2"
difficulty: 3
illustrates:
  - ANL-THM-046
related:
  - ANL-EX-020
  - ANL-THM-043
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

证明 Leibniz 公式
$$
\frac{\pi}{4}=1-\frac13+\frac15-\frac17+\cdots=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}.
$$
把证明组织为三步：

1. 由 $\arctan x$ 的 Maclaurin 级数在 $|x|<1$ 上成立；
2. 用 Leibniz 判别法（[[ANL-THM-042]]）证明 $x=1$ 处对应的数项级数收敛；
3. 证明 **Abel 极限定理**：若 $\displaystyle\sum_{n=0}^{\infty}a_n$ 收敛于 $S$，则 $\displaystyle\lim_{r\to1^-}\sum_{n=0}^{\infty}a_nr^n=S$，据此把 $|x|<1$ 上的恒等式延伸到 $x=1$。

## 分析

$\arctan$ 的 Maclaurin 级数可由几何级数逐项积分得到，但只保证在收敛半径内成立（半径 $R=1$）。$x=1$ 恰在边界上，不能直接代入。另一方面，$x=1$ 处的数项级数 $\sum(-1)^n/(2n+1)$ 是交错级数、项的绝对值单调趋于零，由 Leibniz 判别法收敛。**Abel 定理的作用正是在"端点级数收敛"时，把幂级数的和函数在该端点的值与端点级数的和联系起来。**

Abel 定理证明的要点是**分部求和**：把 $\sum a_nr^n$ 改写成以部分和 $s_n$ 为系数的级数
$$
\sum_{n=0}^{\infty}a_nr^n=(1-r)\sum_{n=0}^{\infty}s_nr^n.
$$
当 $r\to1^-$ 时，权 $(1-r)r^n$ 的总和为 $(1-r)\sum r^n=1$，且质量集中在 $n\approx\dfrac1{1-r}$ 处；由于 $s_n\to S$，这个加权平均趋于 $S$。这就是"用部分和的收敛控制幂级数的端点行为"。

最后要讨论**前提不可省**：若端点级数发散，对和函数取极限会给出错误结果。

## 证明 / 解答

### 第一步：反正切的 Maclaurin 展开

在 $|x|<1$ 上，几何级数
$$
\frac{1}{1+x^2}=\sum_{n=0}^{\infty}(-1)^nx^{2n}
$$
成立。由幂级数逐项积分定理（[[ANL-THM-046]]，另见 [[ANL-EX-019]]），对 $|x|<1$ 有
$$
\arctan x=\int_0^x\frac{dt}{1+t^2}=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}x^{2n+1}. \tag{1}
$$

### 第二步：端点级数收敛

在 (1) 中取 $x=1$，记 $a_n=\dfrac{(-1)^n}{2n+1}$，并令 $b_n=\dfrac1{2n+1}$。则 $b_n>0$，$\{b_n\}$ 单调递减且 $\lim\limits_{n\to\infty}b_n=0$。由 Leibniz 判别法（[[ANL-THM-042]]），$\displaystyle\sum_{n=0}^{\infty}a_n$ 收敛。

注意它**不是绝对收敛**：$\sum|a_n|=\sum\dfrac1{2n+1}=+\infty$（与调和级数比较），故端点级数只是条件收敛。因此不能用 M-判别法一步证明幂级数在 $[0,1]$ 上一致收敛；要把 $|x|<1$ 上的恒等式延伸到 $x=1$，需要处理端点收敛的 Abel 定理（它保证端点收敛的幂级数在闭区间上一致收敛）。

### 第三步：Abel 极限定理

**定理**：设 $\displaystyle\sum_{n=0}^{\infty}a_n$ 收敛于 $S$，则 $\displaystyle\lim_{r\to1^-}\sum_{n=0}^{\infty}a_nr^n=S$。

**证明**：记部分和 $s_n=\sum_{k=0}^{n}a_k$，约定 $s_{-1}=0$。由 $\sum a_n$ 收敛，$\{s_n\}$ 收敛于 $S$，故有界。对 $0\le r<1$，级数 $\sum a_nr^n$ 绝对收敛（$\{a_n\}$ 有界，与 $\sum r^n$ 比较）。

**分部求和**：对有限和作变换，
$$
\sum_{n=0}^{N}a_nr^n=\sum_{n=0}^{N}(s_n-s_{n-1})r^n=s_Nr^N+(1-r)\sum_{n=0}^{N-1}s_nr^n.
$$
令 $N\to\infty$：$s_Nr^N\to0$（$s_N$ 有界、$r^N\to0$），且 $\sum s_nr^n$ 绝对收敛，故
$$
\sum_{n=0}^{\infty}a_nr^n=(1-r)\sum_{n=0}^{\infty}s_nr^n. \tag{2}
$$
又 $(1-r)\sum_{n=0}^{\infty}r^n=1$，故 $S=(1-r)\sum_{n=0}^{\infty}Sr^n$。由 (2)，
$$
\left|\sum_{n=0}^{\infty}a_nr^n-S\right|\le(1-r)\sum_{n=0}^{\infty}|s_n-S|r^n. \tag{3}
$$

任给 $\varepsilon>0$。由 $s_n\to S$，存在 $N$ 使 $n>N$ 时 $|s_n-S|<\dfrac{\varepsilon}{2}$。取 $M=\max\limits_{0\le n\le N}|s_n-S|$，则对 $0\le r<1$，
$$
(1-r)\sum_{n=0}^{\infty}|s_n-S|r^n\le(1-r)(N+1)M+\frac{\varepsilon}{2}(1-r)\sum_{n>N}r^n\le(1-r)(N+1)M+\frac{\varepsilon}{2}.
$$
于是存在 $r_0\in(0,1)$，使 $r\in(r_0,1)$ 时 $(1-r)(N+1)M<\dfrac{\varepsilon}{2}$，从而由 (3) 得
$$
\left|\sum_{n=0}^{\infty}a_nr^n-S\right|<\varepsilon.
$$
这就证明 $\displaystyle\lim_{r\to1^-}\sum_{n=0}^{\infty}a_nr^n=S$。$\blacksquare$

### 第四步：取极限得 Leibniz 公式

对 $0<r<1$，在 (1) 中取 $x=r$，得
$$
\arctan r=r\sum_{n=0}^{\infty}a_nr^{2n}=r\sum_{n=0}^{\infty}a_n(r^2)^n.
$$
记 $y=r^2$。当 $r\to1^-$ 时 $y\to1^-$，由第三步的 Abel 定理（以 $y$ 为变量），
$$
\lim_{r\to1^-}\sum_{n=0}^{\infty}a_nr^{2n}=\lim_{y\to1^-}\sum_{n=0}^{\infty}a_ny^n=S,
$$
其中 $S=\displaystyle\sum_{n=0}^{\infty}a_n$。又 $\arctan$ 在 $x=1$ 处连续，$\arctan1=\dfrac{\pi}{4}$，且 $r\to1$，故
$$
\frac{\pi}{4}=\lim_{r\to1^-}\arctan r=\lim_{r\to1^-}r\cdot\lim_{r\to1^-}\sum_{n=0}^{\infty}a_nr^{2n}=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}.
$$
$\blacksquare$

### 第五步：端点前提为什么不可省

**反例**：在 $|x|<1$ 上有
$$
\sum_{n=0}^{\infty}(-1)^nx^n=\frac{1}{1+x}.
$$
右端在 $x\to1^-$ 时趋于 $\dfrac12$，但左端的数项级数 $\sum(-1)^n$ 在 $x=1$ 处发散。若不做检验就令 $x\to1^-$，会得到错误的 $\sum(-1)^n=\dfrac12$。这说明 Abel 定理中"$\sum a_n$ 收敛"的前提不可省：取极限只能把**已经收敛的端点级数**与和函数在该点的值联系起来。

**缺项级数**也会失效：$\sum_{n\ge0}x^{2^n}$ 的收敛半径为 $1$，但在 $x=1$ 处通项不趋于零，级数发散，端点处没有可延拓的值。对本题而言，端点 $x=1$ 的收敛性由第二步的 Leibniz 判别法保证，这是可以取极限的关键。

## 关键技巧

- **内部展开 + 端点收敛 + Abel 定理**：幂级数在收敛区间内部给出的恒等式，可在端点级数收敛时延伸到端点，这是处理边界值的标准路线。
- **分部求和公式**：$\sum a_nr^n=(1-r)\sum s_nr^n$ 把"通项的级数"换成"部分和的加权平均"，是 Abel 型定理的通用形式。
- **权 $(1-r)r^n$ 的解释**：它是几何分布的权，$r\to1^-$ 时质量移向无穷远；由于 $s_n\to S$，加权平均趋于 $S$。
- **Leibniz 判别法给端点收敛**：$b_n=\dfrac1{2n+1}$ 单调趋于零，端点级数收敛但非绝对收敛。
- **先检验再取极限**：反例 $\sum(-1)^nx^n$ 说明跳过收敛性检验会得到错误等式。

## 变式

- **变式 1**：用同样的三步证明 $\displaystyle\ln2=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$。提示：$\ln(1+x)=\sum_{n\ge1}\dfrac{(-1)^{n-1}}{n}x^n$（$|x|<1$），端点 $x=1$ 处为交错调和级数，由 Leibniz 判别法收敛，再用 Abel 定理。
- **变式 2**：用 Leibniz 余项估计计算 $\dfrac{\pi}{4}$ 的近似值。取前 $4$ 项
    $$
    S_4=1-\frac13+\frac15-\frac17=\frac{76}{105}\approx0.7238,
    $$
    证明 $\left|S_4-\dfrac{\pi}{4}\right|\le\dfrac19\approx0.1111$，并与实际误差 $\approx0.0616$ 比较。
- **变式 3**：由 Abel 极限定理推出连续性形式：若幂级数 $\sum a_nx^n$ 在 $x=1$ 收敛，则其和函数在 $[0,1]$ 上连续。提示：在 $[0,r]$（$r<1$）上由内闭一致收敛（[[ANL-THM-046]]）得连续，在 $x=1$ 处由 Abel 定理得左连续。
- **变式 4**：证明 $\sum(-1)^n/(2n+1)$ 只是条件收敛；并说明条件收敛级数不能随意重排（本题取的是原顺序的和），这与绝对收敛级数的重排不变性形成对照。

## 链接

- 关键判别法：[[ANL-THM-042]] Leibniz 交错级数判别法
- 幂级数工具：[[ANL-THM-046]] Cauchy–Hadamard 公式与逐项运算、[[ANL-THM-045]] 一致收敛与极限交换
- 相关展开：[[ANL-EX-019]] 常见初等函数的 Maclaurin 展开
- 相邻条目：[[ANL-EX-020]] 巴塞尔问题、[[ANL-THM-043]] Abel 判别法与 Dirichlet 判别法（级数版）
- 方法对照：[[ANL-EX-021]] 欧拉常数（同为常数级数的精细估计）
