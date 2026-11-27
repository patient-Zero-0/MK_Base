---
title: "斯特林公式：阶乘的渐近"
type: example
id: ANL-EX-022
subject: analysis
chapter: 06-interesting-problems
tags:
  - 级数
  - 斯特林公式
  - 渐近展开
  - Wallis
depends:
  - ANL-EX-013
  - ANL-THM-006
  - ANL-THM-041
  - ANL-DEF-029
uses: []
status: stable
source: "经典问题（de Moivre–Stirling）；参考华东师范大学《数学分析》第5版 §11.2、§12.2"
difficulty: 4
illustrates:
  - ANL-THM-006
related:
  - ANL-EX-021
  - ANL-EX-026
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

证明斯特林公式
$$
n!\sim\sqrt{2\pi n}\left(\frac{n}{e}\right)^n\qquad(n\to\infty),
$$
即 $\displaystyle\lim_{n\to\infty}\frac{n!}{\sqrt{2\pi n}\,(n/e)^n}=1$；并进一步证明
$$
n!=\sqrt{2\pi n}\left(\frac{n}{e}\right)^n\left(1+O\left(\frac1n\right)\right),
$$
再讨论中心二项式系数等变式。

## 分析

由 $\ln$ 的单调性，$\ln n!=\sum_{k=1}^{n}\ln k\approx\int_1^n\ln x\,dx=n\ln n-n+1$，所以 $n!$ 的主项应为 $n^ne^{-n}$；离散和与积分还差一个多项式因子，梯形公式的端点修正提示应有因子 $\sqrt n$。于是猜测 $n!\approx C\sqrt n\,(n/e)^n$，其中常数 $C>0$ 暂时未知。

把猜测"剥离"出来：令 $d_n=\ln n!-(n+\frac12)\ln n+n$。若能证明 $d_n$ 收敛到某常数 $C$，则 $n!\sim e^C\sqrt n\,(n/e)^n$，只剩确定 $e^C$。为什么 $d_n$ 会收敛？因为把 $\ln(1+1/n)$ 展开到三阶可得 $d_n-d_{n+1}=(n+\frac12)\ln(1+\frac1n)-1\approx\frac{1}{12n^2}$，这些正项之和收敛，故 $d_n$ 递减且有极限；用单调有界定理（[[ANL-THM-006]]）可把直觉变成证明。

常数 $C$ 需要第二个独立的渐近式来确定：Wallis 公式（[[ANL-EX-013]]）给出 $\frac{(2n)!!}{(2n-1)!!}\sim\sqrt{\pi n}$。同一个比值的另一表达式由 $n!$ 的待定渐近式给出，两边比较即解出 $e^C=\sqrt{2\pi}$。

## 证明 / 解答

### 第一步：构造待定常数的序列

令
$$
d_n=\ln n!-\left(n+\frac12\right)\ln n+n.
$$
由定义直接得到
$$
n!=e^{d_n}\,n^{n+\frac12}e^{-n}=e^{d_n}\sqrt n\left(\frac ne\right)^n, \tag{1}
$$
问题化为证明 $d_n$ 收敛并求出 $\lim e^{d_n}$。

### 第二步：序列单调递减

利用 $\ln(n+1)!=\ln n!+\ln(n+1)$ 化简：
$$
d_n-d_{n+1}=-\ln(n+1)-\left(n+\frac12\right)\ln n+\left(n+\frac32\right)\ln(n+1)-1
=\left(n+\frac12\right)\ln\left(1+\frac1n\right)-1. \tag{2}
$$
**关键不等式**：对 $t>0$，$\ln(1+t)>\frac{2t}{2+t}$。证明只需令 $\varphi(t)=\ln(1+t)-\frac{2t}{2+t}$，则 $\varphi(0)=0$，且
$\varphi'(t)=\frac{1}{1+t}-\frac{4}{(2+t)^2}=\frac{t^2}{(1+t)(2+t)^2}>0$，故 $\varphi(t)>0$。在 (2) 中取 $t=\frac1n$，得
$$
d_n-d_{n+1}>\left(n+\frac12\right)\cdot\frac{2}{2n+1}-1=0,
$$
故 $\{d_n\}$ 严格单调递减。

### 第三步：序列有下界

凹函数 $\ln x$ 在点 $k$ 处的切线在图像上方：$\ln x\le\ln k+\frac{x-k}{k}$（$x>0$）。在 $[k-\frac12,k+\frac12]$ 上积分，右端的线性项积分为零，于是
$$
\ln k\ge\int_{k-1/2}^{k+1/2}\ln x\,dx.
$$
对 $k=1,\dots,n$ 求和，并用 $\int\ln x\,dx=x\ln x-x$：
$$
\ln n!\ge\int_{1/2}^{n+1/2}\ln x\,dx
=\left(n+\frac12\right)\ln\left(n+\frac12\right)-n+\frac12\ln2.
$$
代回 $d_n$ 的定义，得
$$
d_n\ge\left(n+\frac12\right)\ln\frac{n+1/2}{n}+\frac12\ln2
>\frac12\ln2>0. \tag{3}
$$
由单调有界定理（[[ANL-THM-006]]），$C:=\lim d_n$ 存在，且 $C\ge\frac12\ln2$。记 $A=e^C$。

### 第四步：用 Wallis 公式定出常数

由 [[ANL-EX-013]] 的 Wallis 公式
$$
\lim_{n\to\infty}\frac{[(2n)!!]^2}{(2n-1)!!\,(2n+1)!!}=\frac{\pi}{2}.
$$
令 $W_n=\frac{(2n)!!}{(2n-1)!!}$，则 $\frac{W_n^2}{2n+1}\to\frac{\pi}{2}$，故
$$
W_n\sim\sqrt{\pi n}\qquad(n\to\infty). \tag{4}
$$
用阶乘表示双阶乘：$(2n)!!=2^n n!$，$(2n-1)!!=\frac{(2n)!}{2^n n!}$，所以
$$
W_n=\frac{2^{2n}(n!)^2}{(2n)!}. \tag{5}
$$
由 (1) 与 $e^{d_n}\to A$，有 $n!=A\sqrt n\left(\frac ne\right)^n(1+o(1))$。代入 (5)，并利用
$$
(n!)^2=A^2n\left(\frac ne\right)^{2n}(1+o(1)),\qquad
(2n)!=A\sqrt2\,\sqrt n\cdot2^{2n}\left(\frac ne\right)^{2n}(1+o(1)),
$$
得到
$$
W_n=\frac{A}{\sqrt2}\sqrt n\,(1+o(1)).
$$
与 (4) 比较得 $\frac{A}{\sqrt2}=\sqrt\pi$，即
$$
A=\sqrt{2\pi},\qquad C=\frac12\ln(2\pi)\approx0.9189385332. \tag{6}
$$
代回 (1) 即得斯特林公式。$\blacksquare$

### 第五步：误差量级

由 (2)，$d_n-C=\sum_{k=n}^{\infty}\tau_k$，其中
$$
\tau_k=\left(k+\frac12\right)\ln\left(1+\frac1k\right)-1>0.
$$
令 $t=\frac1k\in(0,1]$。由交错级数 $\ln(1+t)=t-\frac{t^2}{2}+\frac{t^3}{3}-\cdots$ 截断得 $\ln(1+t)\le t-\frac{t^2}{2}+\frac{t^3}{3}$，于是
$$
\tau_k\le\left(\frac1t+\frac12\right)\left(t-\frac{t^2}{2}+\frac{t^3}{3}\right)-1
=\frac{t^2}{12}+\frac{t^3}{6}\le\frac{t^2}{4}=\frac{1}{4k^2}.
$$
故
$$
0<d_n-C\le\sum_{k=n}^{\infty}\frac{1}{4k^2}\le\frac{1}{4(n-1)}=O\left(\frac1n\right)\qquad(n\ge2). \tag{7}
$$
于是 $e^{d_n}=\sqrt{2\pi}\left(1+O(1/n)\right)$，代回 (1) 得
$$
n!=\sqrt{2\pi n}\left(\frac ne\right)^n\left(1+O\left(\frac1n\right)\right). \tag{8}
$$
数值检验：$n=10$ 时 (8) 中比值为 $1.0083653\ldots$，与 $1+\frac{1}{12\cdot10}=1.0083333\ldots$ 相差约 $3.2\times10^{-5}$，与更精细的 Euler–Maclaurin 展开 $d_n=\frac12\ln(2\pi)+\frac{1}{12n}+O(n^{-3})$ 相符。$\blacksquare$

## 关键技巧

- **剥离主项构造收敛序列**：由积分估计猜出 $n!$ 的形状，再令 $d_n=\ln n!-(n+\frac12)\ln n+n$，把"求渐近"化归为"证数列收敛"。
- **用凸性/凹性比较离散与连续**：$\ln(1+1/n)$ 的估计来自积分，$1/x$ 的凸性与 $\ln x$ 的凹性分别给出单调性和下界。
- **单调有界定理**：$d_n$ 递减且 $>\frac12\ln2$，极限 $C$ 存在，先拿到常数存在性。
- **第二个渐近式定常数**：Wallis 公式给出双阶乘之比的渐近，把 $n!$ 的待定渐近代入同一量，比较即得 $e^C=\sqrt{2\pi}$。
- **余项估计**：用 $\ln(1+t)$ 的交错展开控制 $\tau_k$，得到 $1/n$ 阶误差。

## 变式

- **变式 1（中心二项式系数）**：证明 $\binom{2n}{n}\sim\frac{4^n}{\sqrt{\pi n}}$。提示：把 (8) 代入 $\binom{2n}{n}=\frac{(2n)!}{(n!)^2}$。
- **变式 2（根号下阶乘）**：证明 $\displaystyle\lim_{n\to\infty}\frac{(n!)^{1/n}}{n}=\frac1e$。提示：由 (8) 取 $n$ 次方根。
- **变式 3（反推 Wallis）**：把 (8) 代入 $W_n=\frac{2^{2n}(n!)^2}{(2n)!}$，证明 $W_n\sim\sqrt{\pi n}$，从而得到 Wallis 公式。这说明斯特林公式与 Wallis 公式在渐近意义下等价。
- **变式 4（Gamma 函数形式）**：设 $\Gamma(x)=\int_0^{\infty}t^{x-1}e^{-t}\,dt$（[[ANL-EX-014]]），证明 $\Gamma(x+1)\sim\sqrt{2\pi x}\,(x/e)^x$（$x\to+\infty$）。提示：先证 $\Gamma(n+1)=n!$，再用 Stirling 公式夹住一般实数 $x$。

## 链接

- 演示定理：[[ANL-THM-006]] 单调有界定理
- 依赖：[[ANL-EX-013]] 分部积分典型范例（含 Wallis 公式）、[[ANL-THM-041]] 积分判别法、[[ANL-DEF-029]] 反常积分（无穷限）
- 相关：[[ANL-EX-021]] 欧拉常数、[[ANL-EX-026]] 大二之梦：幂塔的积分与级数
- 延伸：[[ANL-EX-014]] 反常积分敛散性判别（含 Gamma 函数引入）、[[ANL-EX-020]] 巴塞尔问题
