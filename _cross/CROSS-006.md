---
title: "矩阵指数与常系数线性微分方程组"
type: definition
id: CROSS-006
subject: cross
chapter: _cross
tags:
  - 跨课
  - 矩阵指数
  - 微分方程组
  - 若尔当标准形
depends:
  - ALG-THM-043
  - ANL-THM-046
  - ANL-DEF-037
uses: []
status: stable
source: "综合：华东师范大学《数学分析》第5版 §14.1–§14.2 + 丘维声《高等代数》第3版 §5.6"
difficulty: 4
related:
  - ALG-EX-019
  - CROSS-004
---

## 关联说明

常系数线性微分方程组的初值问题
$$
x'(t)=Ax(t),\qquad x(0)=x_0,\qquad A\in\mathbb{R}^{n\times n},
$$
的解可以写成 $x(t)=e^{At}x_0$，其中矩阵指数由幂级数
$$
e^{At}=\sum_{k=0}^{\infty}\frac{A^kt^k}{k!}
$$
定义。分析课负责说明这个级数为什么合法、为什么给出解；代数课负责把它算出来。

| 问题 | 分析视角（级数与极限） | 代数视角（矩阵结构） |
|---|---|---|
| 矩阵指数的合法性 | 幂级数对每个 $t$ 绝对收敛 | 方阵多项式，对任意方阵有定义 |
| 求解初值问题 | 验证 $\frac{d}{dt}e^{At}=Ae^{At}$，由解的唯一性得解 | 对角化或 Jordan 分解 |
| 解的函数形态 | $t^ke^{\lambda t}$ 型函数的线性组合 | Jordan 块 $\lambda I+N$，$N$ 幂零 |
| 基本解组的行列式 | $\det e^{At}=e^{t\operatorname{tr}A}$ | 特征值之积 $=e^{t\sum\lambda_i}$ |

收敛性由范数估计给出：$\lVert A^kt^k/k!\rVert\le\lVert A\rVert^k\lvert t\rvert^k/k!$，右端是收敛的数项级数（[[ANL-DEF-037]] 的幂级数），故 $e^{At}$ 对每个 $t$ 绝对收敛，且在任意有界时间区间上一致收敛；于是可以逐项求导（[[ANL-THM-046]]）：
$$
\frac{d}{dt}e^{At}=\sum_{k=1}^{\infty}\frac{A^k\,kt^{k-1}}{k!}=A\sum_{k=0}^{\infty}\frac{A^kt^k}{k!}=Ae^{At}.
$$
又 $e^{A\cdot0}=I$，所以 $X(t)=e^{At}$ 是基本解矩阵；由线性方程组解的存在唯一性，$x(t)=e^{At}x_0$ 是唯一解。

代数侧的算法是：对 $A$ 作 Jordan 分解 $A=PJP^{-1}$（[[ALG-THM-043]]），则 $e^{At}=Pe^{Jt}P^{-1}$。对每个 Jordan 块 $J=\lambda I+N$（$N^m=0$，$N$ 与 $\lambda I$ 可交换），
$$
e^{Jt}=e^{\lambda t}e^{Nt}=e^{\lambda t}\sum_{k=0}^{m-1}\frac{(Nt)^k}{k!}.
$$
由于 $N$ 幂零，和是有限和，其元素是 $t$ 的多项式；所以 $e^{At}$ 的元素都是 $t^ke^{\lambda t}$ 的线性组合。这就是"特征值决定指数部分、Jordan 块大小决定多项式次数"的来历。

特别地，若 $A$ 可对角化，则 $e^{At}=P\operatorname{diag}(e^{\lambda_1t},\dots,e^{\lambda_nt})P^{-1}$，各特征方向独立地按 $e^{\lambda_it}$ 演化；Jordan 块是这一公式在不可对角化时的替代品。

## 直觉理解

矩阵指数是"连续时间的矩阵幂"：$t$ 很小时 $e^{At}=I+At+O(t^2)$，即一次显式 Euler 步；把 $[0,t]$ 分成 $m$ 份并令 $m\to\infty$，就得到 $\left(I+\frac{t}{m}A\right)^m\to e^{At}$。对对角矩阵 $A=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$，$e^{At}=\operatorname{diag}(e^{\lambda_1t},\dots,e^{\lambda_nt})$，每个分量独立地指数增长或衰减。

耦合项由 Jordan 块处理：$\lambda I$ 部分给出纯指数 $e^{\lambda t}$，幂零部分 $N$ 给出 $t$ 的多项式因子。直观上，$N$ 表示"剪切方向"，重复作用有限次就归零，但每一次作用引入一个 $t$ 的幂，于是出现 $te^{\lambda t}$、$t^2e^{\lambda t}$ 这类函数——这也是线性 ODE 中"重根对应多项式因子"的结构性原因。

几何上，$e^{At}$ 把初始点沿线性向量场 $x\mapsto Ax$ 流动 $t$ 时间。若 $A$ 的特征值实部为负，所有轨道衰减到原点；实部为正则发散；纯虚特征值对应振荡（如旋转）。允许复特征值时，共轭对 $\lambda=\alpha\pm i\beta$ 贡献 $e^{\alpha t}\cos\beta t$ 与 $e^{\alpha t}\sin\beta t$：实部控制增长或衰减，虚部控制振荡频率，旋转例子正是 $\lambda=\pm i$ 的纯振荡。

## 一个具体例子

取 $A=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$，则 $A^2=-I$，故
$$
e^{At}=I\cos t+A\sin t=\begin{pmatrix}\cos t&\sin t\\-\sin t&\cos t\end{pmatrix}.
$$
从 $x_0=(1,0)^\top$ 出发得 $x(t)=(\cos t,-\sin t)^\top$：轨道是单位圆，解是旋转。验证：$x'(t)=(-\sin t,-\cos t)^\top$，而 $Ax(t)=(-\sin t,-\cos t)^\top$，两者一致。这里 $\operatorname{tr}A=0$，故 $\det e^{At}=e^{0}=1$，与旋转矩阵行列式为 $1$ 相符。

再看 Jordan 块 $A=\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix}=\lambda I+N$，$N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ 满足 $N^2=0$，于是
$$
e^{At}=e^{\lambda t}(I+Nt)=e^{\lambda t}\begin{pmatrix}1&t\\0&1\end{pmatrix}.
$$
特别地取 $\lambda=0$、$x_0=(0,1)^\top$，得 $x(t)=(t,1)^\top$：$x_1$ 线性增长，$x_2$ 保持常数，验证 $x'=(1,0)^\top$ 与 $Ax=(1,0)^\top$ 一致。$t$ 因子正是幂零部分贡献的。

高阶方程可以化为一阶方程组：$y''+py'+qy=0$ 令 $x=(y,y')^\top$，得 $x'=Ax$，$A=\begin{pmatrix}0&1\\-q&-p\end{pmatrix}$。其基本解组的朗斯基行列式为 $\det e^{At}=e^{-pt}$，恰好是 [[CROSS-004]] 中 Liouville 公式 $W'=-pW$ 的解。

## 常见误区

- ✗ **认为 $e^{A+B}=e^Ae^B$ 对任意矩阵成立。** 该等式只对可交换的 $A,B$（$AB=BA$）成立。反例：$A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$、$B=\begin{pmatrix}0&0\\1&0\end{pmatrix}$，则 $e^Ae^B=(I+A)(I+B)=\begin{pmatrix}2&1\\1&1\end{pmatrix}$；而 $A+B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$，$e^{A+B}=\cosh1\cdot I+\sinh1\cdot(A+B)\approx\begin{pmatrix}1.543&1.175\\1.175&1.543\end{pmatrix}$，两者不相等。
- ✗ **认为变系数方程组也有 $x(t)=e^{\int_0^tA(s)ds}x(0)$。** 这要求不同时刻的 $A(t)$ 彼此可交换，一般不对。反例：$A(t)=\begin{pmatrix}0&1\\0&t\end{pmatrix}$，此时 $\exp\left(\int_0^tA(s)ds\right)=\exp\begin{pmatrix}0&t\\0&t^2/2\end{pmatrix}$ 的 $(1,2)$ 元素为 $t+\frac14t^3+O(t^5)$；而真解满足 $x_2'=tx_2$、$x_1'=x_2$，从 $x_0=(0,1)^\top$ 出发有 $x_1(t)=\int_0^te^{s^2/2}ds=t+\frac16t^3+O(t^5)$，三次项系数不同，故公式不成立。

## 链接

- 代数工具：[[ALG-THM-043]] Jordan 标准形、[[ALG-EX-019]] Cayley–Hamilton 定理的若干妙用
- 分析工具：[[ANL-THM-046]] 幂级数逐项求导与积分、[[ANL-DEF-037]] 幂级数
- 相邻跨课条目：[[CROSS-004]] 朗斯基行列式与函数的线性无关（$\det e^{At}$ 即基本解组的 Wronskian）
