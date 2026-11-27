---
title: "范数等价性与极限"
type: definition
id: CROSS-008
subject: cross
chapter: _cross
tags:
  - 跨课
  - 范数
  - 等价性
  - 极限
depends:
  - ANL-DEF-004
  - ANL-THM-005
  - ALG-DEF-026
uses: []
status: stable
source: "综合：华东师范大学《数学分析》第5版 §2.1–§2.2 + 丘维声《高等代数》第3版 §3.3、§5.3"
difficulty: 3
related:
  - CROSS-002
  - ALG-THM-038
---

## 关联说明

在 $\mathbb{R}^n$ 上常用的三个范数是
$$
\lVert x\rVert_\infty=\max_{1\le i\le n}\lvert x_i\rvert,\qquad
\lVert x\rVert_2=\Bigl(\sum_{i=1}^{n}x_i^2\Bigr)^{1/2},\qquad
\lVert x\rVert_1=\sum_{i=1}^{n}\lvert x_i\rvert .
$$
它们满足一组夹逼关系：
$$
\lVert x\rVert_\infty\le\lVert x\rVert_2\le\sqrt n\,\lVert x\rVert_\infty,\qquad
\lVert x\rVert_\infty\le\lVert x\rVert_1\le n\,\lVert x\rVert_\infty .
$$
第一组不等式的证明只需平方：对每个 $i$ 有 $x_i^2\le\sum_jx_j^2\le n\max_jx_j^2$，开方即得。由此立即得到：按坐标收敛、按 $\lVert\cdot\rVert_\infty$ 收敛、按 $\lVert\cdot\rVert_2$ 收敛、按 $\lVert\cdot\rVert_1$ 收敛，这四件事彼此等价——用夹逼定理（[[ANL-THM-005]]）把待证序列夹在两个 $\lVert\cdot\rVert_\infty$ 表达之间即可。

| 视角 | 课程 | 关注对象 | 核心结论 |
|---|---|---|---|
| 分析视角 | 数学分析 | 数列与向量序列的极限 | 按范数收敛等价于按坐标收敛；误差估计靠夹逼 |
| 代数视角 | 高等代数 | 有限维空间的结构与矩阵不变量 | 任意两种范数等价；谱半径是相似不变量 |
| 无穷维对照 | 泛函分析初步 | 函数空间中的收敛 | 范数可以不等价，有限维是本质条件 |

更一般地，$\mathbb{R}^n$ 上任意两种范数都等价：存在常数 $c_2\ge c_1>0$ 使
$$
c_1\lVert x\rVert\le\lVert x\rVert'\le c_2\lVert x\rVert\qquad(\forall x\in\mathbb{R}^n).
$$
证明思路是取一组基 $e_1,\dots,e_n$（[[ALG-DEF-026]]），把 $x=\sum\xi_ie_i$ 与坐标向量 $\xi$ 联系起来：一边用三角不等式得 $\lVert x\rVert\le\bigl(\sum\lVert e_i\rVert\bigr)\lVert\xi\rVert_\infty$，另一边用单位球面（按 $\lVert\cdot\rVert_\infty$）的紧性与范数的连续性得到反向估计。这个论证用到了"有限维"：基只有有限个，单位球面才紧。

对矩阵，算子范数定义为
$$
\lVert A\rVert=\max_{x\ne0}\frac{\lVert Ax\rVert}{\lVert x\rVert},
$$
于是 $\lVert Ax\rVert\le\lVert A\rVert\,\lVert x\rVert$。若 $Av=\lambda v$（$v\ne0$），则
$$
\lvert\lambda\rvert\,\lVert v\rVert=\lVert Av\rVert\le\lVert A\rVert\,\lVert v\rVert
\implies \rho(A)\le\lVert A\rVert .
$$
即谱半径不超过任意算子范数。谱半径是相似不变量（[[ALG-THM-038]]），而算子范数不是：同一个线性变换在不同基下的矩阵范数可以不同。这正是 [[CROSS-002]] 中"范数管一步、谱半径管长期"的量化版本。

## 直觉理解

范数是"测量长度"的尺子。在有限维空间里，换一把尺子只会把所有长度同时放缩有界倍：坐标系之间的转换是线性同构，单位球面的紧性给出任意两种范数互相夹逼，所以"点列靠得越来越近"这种拓扑性质与尺子无关。这是有限维空间送给分析学的礼物：讨论 $\mathbb{R}^n$ 中的极限时可以任选最好算的范数。

无限维就没有这份礼物。在 $C[0,1]$ 上，$\lVert f\rVert_\infty$ 与 $\lVert f\rVert_1=\int_0^1\lvert f\rvert$ 不等价：取 $f_n(x)=x^n$，则 $\lVert f_n\rVert_\infty=1$ 恒成立，而 $\lVert f_n\rVert_1=1/(n+1)\to0$。同一个序列在一种尺子下趋于零、在另一种尺子下不趋于零，收敛性依赖于范数。所以"范数等价"不是分析学的普适事实，而是有限维线性空间的特权。

矩阵的算子范数与谱半径的关系也是同一道理：范数是"最坏情况下的单步放大率"，谱半径是"长期平均每步放大率"。对正规矩阵（特别地实对称矩阵），两者相等（[[ALG-THM-044]] 的正交对角化给出 $\lVert A\rVert_2=\rho(A)$）；对非正规矩阵，范数可以比谱半径大很多。

## 一个具体例子

向量 $x=(1,-2,2)$ 的三种范数为
$$
\lVert x\rVert_\infty=2,\qquad\lVert x\rVert_2=\sqrt{1+4+4}=3,\qquad\lVert x\rVert_1=1+2+2=5 .
$$
验证夹逼：$2\le3\le2\sqrt3\approx3.464$；$2\le5\le6$；$3\le5\le3\sqrt3\approx5.196$，全部成立。

矩阵取 $A=\begin{pmatrix}1&2\\0&1\end{pmatrix}$。它的特征值都是 $1$，故 $\rho(A)=1$。而
$$
\lVert A\rVert_\infty=\max\{1+2,\,0+1\}=3,\qquad
\lVert A\rVert_1=\max\{1+0,\,2+1\}=3,
$$
欧氏算子范数由 $A^\top A=\begin{pmatrix}1&2\\2&5\end{pmatrix}$ 的最大特征值 $3+2\sqrt2$ 给出，故 $\lVert A\rVert_2=\sqrt{3+2\sqrt2}=1+\sqrt2\approx2.414$。于是
$$
\rho(A)=1<2.414\approx\lVert A\rVert_2<3=\lVert A\rVert_\infty=\lVert A\rVert_1 .
$$
这个例子说明：范数可以远大于谱半径，但绝不会小于谱半径。

## 常见误区

- ✗ **认为谱半径是一种范数，可以像范数一样做估计。** 谱半径不满足范数公理。反例一（正定性）：$A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ 非零但 $\rho(A)=0$。反例二（三角不等式）：$A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$、$B=\begin{pmatrix}0&0\\1&0\end{pmatrix}$ 都满足 $\rho=0$，但 $A+B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ 的特征值为 $\pm1$，$\rho(A+B)=1>0=\rho(A)+\rho(B)$。
- ✗ **认为欧氏算子范数等于最大特征值的绝对值。** 这只对正常矩阵成立。反例即上面的 $A=\begin{pmatrix}1&2\\0&1\end{pmatrix}$：$\rho(A)=1$，但 $\lVert A\rVert_2=1+\sqrt2\approx2.414$。对正规矩阵（含实对称矩阵这一特例，[[ALG-THM-044]] 的正交对角化给出）才有 $\lVert A\rVert_2=\max_i\lvert\lambda_i\rvert$。

## 链接

- 极限与夹逼：[[ANL-DEF-004]] 数列收敛（ε-N 定义）、[[ANL-THM-005]] 数列夹逼定理
- 线性结构：[[ALG-DEF-026]] 基与维数、[[ALG-THM-038]] 相似矩阵的不变量
- 相邻跨课条目：[[CROSS-002]] 线性方程组的迭代解法（谱半径与范数的分工）
