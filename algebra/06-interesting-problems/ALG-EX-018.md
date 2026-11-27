---
title: "斐波那契数列的矩阵解法与通项公式"
type: example
id: ALG-EX-018
subject: algebra
chapter: 06-interesting-problems
tags:
  - 矩阵
  - 特征值
  - 斐波那契
  - 递推
depends:
  - ALG-DEF-035
  - ALG-DEF-038
  - ALG-THM-040
  - ALG-THM-036
uses: []
status: stable
source: "经典问题；参考丘维声《高等代数》第3版 §5.3"
difficulty: 3
illustrates:
  - ALG-THM-040
related:
  - ALG-EX-016
  - ANL-DEF-037
---

## 题目

斐波那契数列 $\{F_n\}$ 由初值 $F_0 = 0$、$F_1 = 1$ 与递推关系 $F_{n+1} = F_n + F_{n-1}$（$n \ge 1$）确定。记

$$
M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}.
$$

1. 证明对一切 $n \ge 1$ 有 $(F_{n+1}, F_n)^{\mathsf T} = M^n (1, 0)^{\mathsf T}$，并求出 $M^n$ 的显式表达式；
2. 求 $M$ 的特征值 $\varphi$ 与 $\psi$，把 $M$ 对角化，并导出 Binet 公式 $F_n = (\varphi^n - \psi^n)/\sqrt{5}$；
3. 利用 $\det(M^n) = (\det M)^n$ 证明 Cassini 恒等式 $F_{n+1}F_{n-1} - F_n^2 = (-1)^n$。

## 分析

递推式 $F_{n+1} = F_n + F_{n-1}$ 同时用到前两项，单独看一项无法推进；但把相邻两项打包成状态向量 $(F_{n+1}, F_n)^{\mathsf T}$，递推就变成固定矩阵的乘法：

$$
\begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} F_n \\ F_{n-1} \end{pmatrix}.
$$

于是 $n$ 步之后的状态等于 $M^n$ 作用在初始状态上。求 $M^n$ 的标准办法是对角化：$M$ 的特征方程恰好是递推的"试解 $r^n$"给出的方程 $r^2 = r + 1$，两个特征值互异，由 [[ALG-THM-040]] 知 $M$ 可对角化。Binet 公式就是把 $M^n = P D^n P^{-1}$ 代回初始状态。Cassini 恒等式则利用行列式的乘法性质：$\det(M^n)$ 一方面等于 $(\det M)^n$，另一方面可从 $M^n$ 的元素直接读出。

## 证明 / 解答

### 第一步：状态转移与矩阵幂

直接计算给出

$$
M \begin{pmatrix} F_n \\ F_{n-1} \end{pmatrix} = \begin{pmatrix} F_n + F_{n-1} \\ F_n \end{pmatrix} = \begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix}.
$$

初始状态为 $(F_1, F_0)^{\mathsf T} = (1,0)^{\mathsf T}$，故反复使用上式得 $(F_{n+1}, F_n)^{\mathsf T} = M^n (1,0)^{\mathsf T}$（$n \ge 1$）。对 $n$ 归纳可验证：$n = 1$ 时左边是 $(F_2, F_1)^{\mathsf T} = (1,1)^{\mathsf T}$，右边是 $M(1,0)^{\mathsf T}$，二者相等；若对 $n$ 成立，两边左乘 $M$ 并用状态转移即得 $n+1$ 的情形。

### 第二步：特征值与特征向量

$$
\chi_M(\lambda) = \det(\lambda I - M) = \det\begin{pmatrix} \lambda - 1 & -1 \\ -1 & \lambda \end{pmatrix} = \lambda(\lambda - 1) - 1 = \lambda^2 - \lambda - 1.
$$

特征值为 $\varphi = (1 + \sqrt{5})/2$ 与 $\psi = (1 - \sqrt{5})/2$，它们满足 $\varphi + \psi = 1$、$\varphi\psi = -1$。对 $\lambda \in \{\varphi, \psi\}$，由 $\lambda^2 = \lambda + 1$ 得

$$
M \begin{pmatrix} \lambda \\ 1 \end{pmatrix} = \begin{pmatrix} \lambda + 1 \\ \lambda \end{pmatrix} = \begin{pmatrix} \lambda^2 \\ \lambda \end{pmatrix} = \lambda \begin{pmatrix} \lambda \\ 1 \end{pmatrix},
$$

所以 $(\varphi, 1)^{\mathsf T}$ 与 $(\psi, 1)^{\mathsf T}$ 分别是两个特征值对应的特征向量。两个特征值互异，由 [[ALG-THM-040]]，$M$ 可对角化。令 $P = \begin{pmatrix} \varphi & \psi \\ 1 & 1 \end{pmatrix}$，则 $\det P = \varphi - \psi = \sqrt{5}$，

$$
P^{-1} = \frac{1}{\sqrt{5}}\begin{pmatrix} 1 & -\psi \\ -1 & \varphi \end{pmatrix}, \qquad M = P \begin{pmatrix} \varphi & 0 \\ 0 & \psi \end{pmatrix} P^{-1}.
$$

### 第三步：Binet 公式

由 $M^n = P \operatorname{diag}(\varphi^n, \psi^n) P^{-1}$ 以及 $P^{-1}(1,0)^{\mathsf T} = \frac{1}{\sqrt{5}}(1,-1)^{\mathsf T}$，得到

$$
\begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix} = \frac{1}{\sqrt{5}}\begin{pmatrix} \varphi & \psi \\ 1 & 1 \end{pmatrix}\begin{pmatrix} \varphi^n \\ -\psi^n \end{pmatrix} = \frac{1}{\sqrt{5}}\begin{pmatrix} \varphi^{n+1} - \psi^{n+1} \\ \varphi^n - \psi^n \end{pmatrix}.
$$

取第二行即得 Binet 公式

$$
F_n = \frac{\varphi^n - \psi^n}{\sqrt{5}} \qquad (n \ge 0).
$$

检验：$n = 0$ 时右边为 $0$；$n = 1$ 时 $(\varphi - \psi)/\sqrt{5} = 1$；$n = 2$ 时 $(\varphi^2 - \psi^2)/\sqrt{5} = (\varphi + \psi)(\varphi - \psi)/\sqrt{5} = 1$，都与数列一致。又因 $\lvert\psi\rvert = (\sqrt{5} - 1)/2 < 1$，当 $n \ge 1$ 时 $\lvert\psi\rvert^n/\sqrt{5} < 1/2$，故 $F_n$ 是 $\varphi^n/\sqrt{5}$ 最接近的整数，这解释了 $F_n$ 的指数增长速率 $\varphi \approx 1.618034$。

### 第四步：Cassini 恒等式

先证明矩阵幂的元素形式：对 $n \ge 1$ 有

$$
M^n = \begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix}.
$$

$n = 1$ 时两边都是 $M$。若对 $n$ 成立，则

$$
M^{n+1} = M^n M = \begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} F_{n+1} + F_n & F_{n+1} \\ F_n + F_{n-1} & F_n \end{pmatrix} = \begin{pmatrix} F_{n+2} & F_{n+1} \\ F_{n+1} & F_n \end{pmatrix},
$$

即 $n+1$ 的情形。另一方面 $\det M = -1$，所以 $\det(M^n) = (-1)^n$。比较两边的行列式：

$$
F_{n+1}F_{n-1} - F_n^2 = (-1)^n \qquad (n \ge 1).
$$

这就是 Cassini 恒等式。取 $n = 2$ 检验：$F_3F_1 - F_2^2 = 2 \cdot 1 - 1 = 1 = (-1)^2$；取 $n = 3$ 检验：$F_4F_2 - F_3^2 = 3 \cdot 1 - 4 = -1 = (-1)^3$。

$\blacksquare$

## 关键技巧

- **状态向量化**：把二阶递推的两个相邻项打包成二维向量，递推变为矩阵乘法，$F_n$ 成为 $M^n$ 的矩阵元素。
- **特征值即递推的特征根**：特征方程 $\lambda^2 = \lambda + 1$ 与"试解 $r^n$"得到的方程完全一致，这是常系数线性递推的通用现象。
- **对角化求幂**：$M^n = P D^n P^{-1}$ 把矩阵乘法的困难转移到对角阵的 $n$ 次幂；特征值互异是可对角化的充分条件（[[ALG-THM-040]]）。
- **行列式的乘法性**：$\det(M^n) = (\det M)^n$ 把矩阵恒等式翻译成数列恒等式，是证明 Cassini 这类双线性恒等式的捷径。
- **数值检验**：先用 $n = 1, 2, 3$ 代入检验，再写一般证明，可以及时发现符号错误。

## 变式

- **变式 1（生成函数）**：设 $F(x) = \sum_{n \ge 0} F_n x^n$。由递推得 $F(x) = x/(1 - x - x^2)$，拆成部分分式即可重新得到 Binet 公式（参见 [[ANL-DEF-037]] 幂级数）。
- **变式 2（模周期）**：对正整数 $m$，把 $M$ 与状态向量看成 $\mathbb{Z}/m\mathbb{Z}$ 上的对象。因 $\det M = -1$ 在 $\mathbb{Z}/m\mathbb{Z}$ 中可逆，$M$ 是有限集 $(\mathbb{Z}/m\mathbb{Z})^2$ 上的可逆映射，故状态序列从初始状态起是纯周期的，其最小正周期称为 Pisano 周期 $\pi(m)$；例如 $\pi(2) = 3$、$\pi(3) = 8$、$\pi(10) = 60$。
- **变式 3（一般二阶线性递推）**：设 $a_{n+1} = p a_n + q a_{n-1}$，转移矩阵为 $\begin{pmatrix} p & q \\ 1 & 0 \end{pmatrix}$，特征多项式为 $\lambda^2 - p\lambda - q$。两个特征根互异时可按同样方法求通项；重根时 $M$ 不可对角化，需要若尔当块（[[ALG-THM-043]]）。
- **变式 4（d'Ocagne 恒等式）**：用 $M^{m+n} = M^m M^n$ 证明 $F_{m+n} = F_{m+1}F_n + F_mF_{n-1}$。

## 链接

- 演示定理：[[ALG-THM-040]] 可对角化充要条件
- 前置：[[ALG-DEF-035]] 特征值与特征向量、[[ALG-DEF-038]] 可对角化、[[ALG-THM-036]] 线性变换与矩阵一一对应
- 相关例题：[[ALG-EX-016]] 求特征值、特征向量并对角化
- 生成函数视角：[[ANL-DEF-037]] 幂级数
