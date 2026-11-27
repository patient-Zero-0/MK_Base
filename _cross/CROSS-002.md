---
title: "线性方程组的迭代解法：压缩映射与谱半径"
type: definition
id: CROSS-002
subject: cross
chapter: _cross
tags:
  - 跨课
  - 迭代法
  - 谱半径
  - 收敛性
depends:
  - ANL-THM-007
  - ANL-THM-006
  - ALG-THM-043
  - ALG-THM-041
uses: []
status: stable
source: "综合：华东师范大学《数学分析》第5版 §2.3–§2.4 + 丘维声《高等代数》第3版 §5.3、§5.6"
difficulty: 4
related:
  - CROSS-001
  - CROSS-008
  - ALG-EX-018
---

## 关联说明

解线性方程组 $Ax=b$（$A\in\mathbb{R}^{n\times n}$ 可逆）时，把 $A$ 分裂为 $A=M-N$（$M$ 可逆），原方程组等价于不动点方程
$$
x=M^{-1}Nx+M^{-1}b=:Bx+c,
$$
于是可以用迭代 $x_{k+1}=Bx_k+c$ 逐步逼近解。两门课从不同层面回答同一个问题：这个迭代何时收敛、收敛多快？

| 视角 | 课程 | 核心工具 | 收敛条件 | 结论形式 |
|---|---|---|---|---|
| 分析视角 | 数学分析 | 压缩映射、几何级数、Cauchy 准则 | 存在某个范数使 $\lVert B\rVert=q<1$ | 误差按 $q^k$ 衰减，有显式误差界 |
| 代数视角 | 高等代数 | Jordan 标准形、谱半径 | $\rho(B)<1$ | 对任意初值收敛，$x_k\to x^*$ |
| 综合结论 | 两课 | 两条路径本质等价 | $\rho(B)<1$ 是充要条件 | 长期收敛速度由谱半径控制 |

代数方向的完整论证如下。误差 $e_k=x_k-x^*$ 满足 $e_{k+1}=Be_k$，故 $e_k=B^ke_0$，所以"对一切初值收敛"等价于 $B^k\to0$。设 $B=PJP^{-1}$ 是 Jordan 分解（[[ALG-THM-043]]），每个 Jordan 块形如 $J_\lambda=\lambda I+N$，其中 $N$ 幂零，由二项式定理
$$
J_\lambda^k=\sum_{j=0}^{m-1}\binom{k}{j}\lambda^{k-j}N^j .
$$
若 $|\lambda|<1$，则 $k^{m-1}|\lambda|^k\to0$，从而 $J_\lambda^k\to0$；反之若某个 $|\lambda|\ge1$，取对应特征向量 $v$，则 $B^kv=\lambda^kv$ 不趋于 $0$。这就证明了
$$
B^k\to0\iff\rho(B)<1 .
$$
此时 $I-B$ 必可逆（否则 $1$ 是 $B$ 的特征值），不动点 $x^*=(I-B)^{-1}c=A^{-1}b$ 唯一，且 $x_k-x^*=B^k(x_0-x^*)$；逆矩阵还可由 [[ALG-THM-041]] 写成 $B$ 的多项式。

## 直觉理解

把迭代看成不断把向量送进同一台机器 $x\mapsto Bx+c$。若这台机器每一步都把任意两点的距离按同一比例 $q<1$ 缩短，那么所有轨道互相靠拢，终点由几何级数 $\sum q^k$ 保证存在——这是分析视角的压缩映射图像。

代数的视角更细：$B$ 未必在所有方向同比例缩短。沿特征方向，第 $k$ 步的放大率是 $\lambda^k$；只要所有 $|\lambda|<1$，长期看每个方向都衰减。但非对角部分（Jordan 块中的 $N$）会带来 $k^{m-1}$ 型多项式因子，使某些方向在最初几步先膨胀再衰减——这正是单步范数可能大于 $1$ 而迭代仍然收敛的原因。

一句话：范数管一步，谱半径管一辈子。范数是"最坏单步放大率"，谱半径是"长期平均每步放大率"，后者才真正决定收敛性。

## 一个具体例子

用 Jacobi 迭代解
$$
A=\begin{pmatrix}4&1\\1&3\end{pmatrix},\qquad b=\begin{pmatrix}1\\2\end{pmatrix}.
$$
Jacobi 迭代为 $x_1^{(k+1)}=(1-x_2^{(k)})/4$、$x_2^{(k+1)}=(2-x_1^{(k)})/3$，即
$$
B=\begin{pmatrix}0&-\frac14\\-\frac13&0\end{pmatrix},\qquad c=\begin{pmatrix}\frac14\\\frac23\end{pmatrix}.
$$
$B$ 的特征值为 $\pm1/(2\sqrt3)$，故 $\rho(B)=1/(2\sqrt3)\approx0.2887$。由于这个 $2\times2$ 的迭代矩阵每行、每列都只有一个非零元，三个常用算子范数相等：
$$
\lVert B\rVert_\infty=\max\left\{\tfrac14,\tfrac13\right\}=\tfrac13,\qquad
\lVert B\rVert_1=\max\left\{\tfrac13,\tfrac14\right\}=\tfrac13,\qquad
\lVert B\rVert_2=\tfrac13 .
$$
它们都小于 $1$，故迭代对任意初值收敛。精确解为 $x^*=A^{-1}b=\frac{1}{11}(1,7)^\top\approx(0.0909,0.6364)$。取 $x_0=(0,0)^\top$，则 $x_1=(\tfrac14,\tfrac23)^\top$，由误差界
$$
\lVert x_k-x^*\rVert_\infty\le\frac{q^k}{1-q}\lVert x_1-x_0\rVert_\infty=\left(\frac13\right)^k,\qquad q=\lVert B\rVert_\infty=\frac13 .
$$
实测：$\lVert x_1-x^*\rVert_\infty\approx0.159\le0.333$，而 $x_2=(1/12,7/12)^\top$ 给出 $\lVert x_2-x^*\rVert_\infty=7/132\approx0.0530\le0.111$。实际误差衰减率约为 $0.2887$，比 $\infty$ 范数预测的 $1/3$ 略快：谱半径给出的速度更准确。

## 常见误区

- ✗ **认为"某个范数小于 $1$"是收敛的必要条件，或误以为 $\lVert B\rVert_\infty\ge1$ 就发散。** 收敛的充要条件只是 $\rho(B)<1$。反例：$B=\begin{pmatrix}0&2\\0&0\end{pmatrix}$ 满足 $B^2=0$，故 $\rho(B)=0$，迭代至多两步就精确到达不动点；但 $\lVert B\rVert_\infty=\lVert B\rVert_2=2>1$。所以"一个容易计算的范数 $<1$"只是充分条件。（理论上 $\rho(B)<1$ 确实等价于存在某个范数使 $\lVert B\rVert<1$，只是这个范数依赖 $B$，未必好算。）
- ✗ **认为 Jacobi 迭代收敛等价于 $A$ 严格对角占优。** 对角占优只是充分条件。反例：$A=\begin{pmatrix}1&2\\1&4\end{pmatrix}$ 的第一行不占优（$2>1$），但相应的 Jacobi 矩阵谱半径为 $\rho(B)=\sqrt{2/4}\approx0.707<1$，迭代仍然收敛。

## 链接

- 收敛性的标量基础：[[ANL-THM-007]] Cauchy 收敛准则、[[ANL-THM-006]] 单调有界定理
- 代数工具：[[ALG-THM-043]] Jordan 标准形、[[ALG-THM-041]] Cayley–Hamilton 定理
- 相邻跨课条目：[[CROSS-001]] 数列收敛与线性递推、[[CROSS-008]] 范数等价性与极限
- 相关例题：[[ALG-EX-018]] 斐波那契数列的矩阵解法（同样由矩阵幂 $B^k$ 控制）
