---
title: "幂级数收敛域与求和综合"
type: problem
id: ANL-PROB-023
subject: analysis
chapter: 05-series
tags:
  - 级数
  - 幂级数
  - 求和
  - 收敛域
depends:
  - ANL-DEF-038
  - ANL-THM-046
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §14 综合习题"
difficulty: 4
tests:
  - ANL-DEF-038
  - ANL-THM-046
related:
  - ANL-DEF-039
  - ANL-EX-019
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

1. 求幂级数 $\displaystyle\sum_{n=1}^{\infty} \frac{x^n}{n}$ 的收敛域（[[ANL-DEF-038]]）与和函数。
2. 求 $\displaystyle\sum_{n=1}^{\infty} n x^n$ 的收敛域与和函数。
3. 求数项级数 $\displaystyle\sum_{n=1}^{\infty} \frac{n}{2^n}$ 与 $\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n}$ 的和（借助第 1、2 题的和函数）。

## 提示

<details><summary>点击展开提示</summary>

- **第 1 题**：$R=1$；逐项求导（[[ANL-THM-046]]）得几何级数，求和后再积分回去。端点 $x=\pm1$ 单独判。
- **第 2 题**：$R=1$；由 $\sum x^n = \frac{x}{1-x}$ 逐项求导，或对 $\frac{1}{1-x}$ 求导再乘 $x$。
- **第 3 题**：把数值代入和函数——$\sum \frac{n}{2^n}$ 用第 2 题取 $x=\frac12$；$\sum\frac{(-1)^{n-1}}{n}$ 用第 1 题取 $x=1$（注意端点收敛与 Abel 连续性）。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题

**收敛半径**：$c_n = 1/n$，$\lim\left|\frac{c_n}{c_{n+1}}\right| = \lim\frac{n+1}{n} = 1$，故 $R=1$（[[ANL-DEF-038]]）。

**端点**：$x=1$ 得调和级数 $\sum\frac1n$ 发散；$x=-1$ 得 $\sum\frac{(-1)^n}{n}$ 收敛（Leibniz）。**收敛域 $[-1, 1)$**。

**和函数**：设 $S(x)=\sum_{n=1}^\infty \frac{x^n}{n}$（$|x|<1$）。逐项求导（[[ANL-THM-046]]）：
$$
S'(x) = \sum_{n=1}^\infty x^{n-1} = \frac{1}{1-x}.
$$
又 $S(0)=0$，积分回去：
$$
S(x) = \int_0^x \frac{dt}{1-t} = -\ln(1-x), \qquad x \in [-1, 1).
$$
（端点 $x=-1$：级数收敛且 $-\ln 2$，由 Abel 第二定理与和函数单侧连续吻合。）$\quad\blacksquare$

### 第 2 题

**收敛半径**：$c_n = n$，$\sqrt[n]{n}\to1$ 故 $R=1$。**端点** $x=\pm1$：通项 $n(\pm1)^n \not\to 0$，均发散。**收敛域 $(-1,1)$**。

**和函数**：由几何级数 $\sum_{n=0}^\infty x^n = \frac{1}{1-x}$ 逐项求导（[[ANL-THM-046]]）：
$$
\sum_{n=1}^\infty n x^{n-1} = \frac{1}{(1-x)^2}\ \Longrightarrow\ \sum_{n=1}^\infty n x^n = \frac{x}{(1-x)^2}, \qquad |x|<1.
$$
$\quad\blacksquare$

### 第 3 题：数项级数求和

**$\displaystyle\sum_{n=1}^\infty \frac{n}{2^n}$**：取第 2 题 $x=\frac12$（$\in(-1,1)$）：
$$
\sum_{n=1}^\infty \frac{n}{2^n} = \frac{1/2}{(1-1/2)^2} = \frac{1/2}{1/4} = 2.
$$

**$\displaystyle\sum_{n=1}^\infty \frac{(-1)^{n-1}}{n}$**：取第 1 题 $x=-1$。$S(-1) = -\ln(1-(-1)) = -\ln 2$，而 $S(-1)=\sum\frac{(-1)^n}{n} = -\sum\frac{(-1)^{n-1}}{n}$，故
$$
\sum_{n=1}^\infty \frac{(-1)^{n-1}}{n} = \ln 2.
$$
$\quad\blacksquare$

</details>

## 考察点

- [[ANL-DEF-038]] 收敛半径（比值 / 根值公式）与端点单独判定
- [[ANL-THM-046]] 逐项求导 / 积分求和函数（半径不变）
- 几何级数 $\frac{1}{1-x}$ 作为"母函数"，求导得 $\sum n x^n$、积分得 $-\ln(1-x)$
- Abel 第二定理：端点处和函数单侧连续，使 $x\to$ 端点的代入合法

## 备注

**幂级数求和的标准流程**：

1. 用比值 / 根值公式（[[ANL-DEF-038]]）定收敛半径 $R$；
2. 两端点 $x=x_0\pm R$ 各自代入，用数项级数判别法定收敛域；
3. 在 $(x_0-R, x_0+R)$ 内逐项求导 / 积分（[[ANL-THM-046]]）化归到几何级数等已知和；
4. 求出和函数后，**代入特定 $x$** 即得相关数项级数之和（注意端点需 Abel 连续性背书）。

**与 Maclaurin 展开互逆**（[[ANL-EX-019]]）：展开是"函数 $\to$ 级数"，本题求和是"级数 $\to$ 函数"，两者共享同一套逐项运算工具。
