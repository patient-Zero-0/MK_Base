---
title: "数列收敛与线性递推：单调有界与矩阵谱半径的桥接"
type: definition
id: CROSS-001
subject: cross
chapter: _cross
tags:
  - 跨课
  - 极限
  - 线性递推
  - 谱半径
depends:
  - ANL-THM-006
  - ANL-DEF-004
  - ALG-THM-043
  - ALG-THM-041
uses: []
status: stable
source: "综合：华东师范大学《数学分析》第5版 §2.4 + 丘维声《高等代数》第3版 §5.4"
difficulty: 3
related:
  - CROSS-002
  - CROSS-010
  - ALG-EX-018
applications:
  - "PageRank：迭代算法收敛性的两类视角"
  - "经济学：投入产出模型长期均衡的存在性"
---

## 关联说明

线性递推 $\mathbf{x}_{n+1} = A \mathbf{x}_n + \mathbf{b}$（$A$ 为方阵）的收敛性，在两门课程中有**两条独立但最终等价**的论证路径：

| 视角 | 课程 | 工具 | 关键结论 |
|---|---|---|---|
| 标量分量论证 | 数学分析 | 单调有界、压缩估计、Cauchy 准则 | 每个分量 $x_n^{(i)}$ 是收敛数列（[[ANL-THM-006]]、[[ANL-DEF-004]]） |
| 矩阵整体论证 | 高等代数 | 特征值、Jordan 标准形 | $A^n \to 0 \iff \rho(A) < 1$（[[ALG-THM-043]]） |

其中 $\rho(A) = \max_i |\lambda_i|$ 是谱半径。两条路径的落点相同：当 $\rho(A) < 1$ 时，
$\mathbf{x}_n \to (\mathrm{I} - A)^{-1}\mathbf{b}$；而当 $\rho(A) > 1$ 时，迭代对一般初值发散。

## 直觉理解

**数学分析视角：逐分量看时间序列。**
固定一个分量 $x_n^{(i)}$，它就是一个普通实数列。若能从递推式直接估计出
$|x_{n+1}^{(i)} - x_n^{(i)}| \le q\,|x_n^{(i)} - x_{n-1}^{(i)}|$（$0 < q < 1$），
则相邻项之差被几何级数控制，由 [[ANL-DEF-004]] 的 $\varepsilon$-$N$ 定义与 Cauchy 准则，
该分量收敛。这里**不需要**分量单调，只需要“越来越挤”。

**高等代数视角：整体看矩阵幂。**
把向量序列看成矩阵幂作用的轨道：$\mathbf{x}_n = A^n\mathbf{x}_0 + \sum_{k=0}^{n-1}A^k\mathbf{b}$。
若 $\rho(A) < 1$，由 Jordan 标准形（[[ALG-THM-043]]）可把 $A$ 写成
$A = PJP^{-1}$，其中 $J$ 的每个 Jordan 块 $\lambda \mathrm{I} + N$ 满足
$$
(\lambda \mathrm{I} + N)^n = \sum_{j=0}^{m-1}\binom{n}{j}\lambda^{n-j}N^j,
$$
而 $|\lambda|^n \to 0$、多项式因子 $n^j$ 抵不过几何衰减，故 $A^n \to 0$。
于是 $\mathbf{x}_n \to (\mathrm{I} - A)^{-1}\mathbf{b}$。这一论证**与分量选取无关**，是结构性的。

两视角的等价性来自：矩阵收敛（按任意矩阵范数）等价于每个元素收敛（有限维空间中范数等价），
而每个元素序列的收敛由 [[ANL-DEF-004]] 刻画。因此“逐分量收敛”与“矩阵整体收敛”是同一件事的两种语言。
注意谱半径判据通常要借助 [[ALG-THM-041]] Cayley–Hamilton 定理或 Jordan 标准形来完成特征值的完整信息，
而分析视角往往只需一个容易验证的压缩常数 $q$。

## 一个具体例子

取
$$
A = \begin{pmatrix} \tfrac12 & \tfrac15 \\[2pt] 0 & \tfrac13 \end{pmatrix},
\qquad \mathbf{b} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}.
$$
$A$ 的特征值为 $\tfrac12, \tfrac13$，故 $\rho(A) = \tfrac12 < 1$。由 [[ALG-THM-043]]，$A^n \to 0$，
迭代收敛到不动点
$$
\mathbf{x}^* = (\mathrm{I} - A)^{-1}\mathbf{b}
= \begin{pmatrix} \tfrac12 & -\tfrac15 \\[2pt] 0 & \tfrac23 \end{pmatrix}^{-1}
\begin{pmatrix} 1 \\ 1 \end{pmatrix}
= \begin{pmatrix} \tfrac{13}{5} \\[2pt] \tfrac32 \end{pmatrix}.
$$
分析视角：分量 $x_n^{(2)}$ 满足 $x_{n+1}^{(2)} = \tfrac13 x_n^{(2)} + 1$，直接解得
$x_n^{(2)} \to \tfrac32$；分量 $x_n^{(1)}$ 也满足压缩递推，故收敛。两条路径得到同一个极限。

## 常见误区

- ✗ **把“谱半径小于 1”误写成“特征值都小于 1”。** 特征值可能是复数：$A=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$
  的特征值为 $\pm \mathrm{i}$，$|\lambda|=1$，迭代不收敛；但按实数大小比较会误判为“小于 1”。
  判据必须是 $|\lambda| < 1$（模长）。
- ✗ **把“某个给定范数（如 2-范数、$\infty$-范数）小于 1”与“存在某个范数小于 1”混为一谈。**
  给定范数下 $\|A\|<1$ 只是收敛的充分条件：$A=\begin{pmatrix}0&2\\0&0\end{pmatrix}$ 有 $\rho(A)=0$，
  但 $\|A\|_2 = 2$；不过 $A^2=0$，迭代仍在两步后终止。
  若允许范数依赖 $A$，则 Householder 定理给出
  $\rho(A)<1 \iff$ 存在某个范数使 $\|A\|<1$（见 [[CROSS-002]]）。
  谱半径是“渐近”压缩率，固定范数是“一步”压缩率。
- ✗ **把“每个分量都单调”当成收敛的必要条件。** 例如
  $A=\tfrac12\begin{pmatrix}1&-1\\1&1\end{pmatrix}$ 的特征值为 $(1\pm\mathrm{i})/2$，模为 $\tfrac{\sqrt2}{2}<1$；
  取 $\mathbf{b}=0$ 时分量会**振荡**衰减，并不单调。收敛靠的是 Cauchy 准则（或矩阵幂的收敛），而不是单调性。

## 应用场景

### PageRank（搜索引擎排序）

PageRank 的迭代矩阵（含传送项）为
$G = cM + \frac{1-c}{N}\mathbf{1}\mathbf{1}^{\mathsf T}$，其中 $M$ 为行随机矩阵、$c\in(0,1)$ 为阻尼因子。
$G$ 仍是随机矩阵，故 $\rho(G)=1$ 且主特征值 $1$ 单重；其余特征值满足 $|\lambda|\le c<1$。
**分析视角**：每个分量受平均化压缩，幂迭代 $\mathbf{r}_{k+1}=G\mathbf{r}_k$ 的相邻两项之差被几何控制；
**代数视角**：收敛到主特征向量（PageRank 向量），收敛速率由次特征值 $|\lambda_2|\le c$ 决定（特征值间隙）。

### Leontief 投入产出模型（经济学）

总产出满足 $\mathbf{x} = A\mathbf{x} + \mathbf{d}$。若每行（或每列）和 $< 1$，可证 $\rho(A)<1$，
从而 $\mathbf{x} = (\mathrm{I} - A)^{-1}\mathbf{d}$ 长期均衡存在。
**分析视角**：逐分量估计 $x_n^{(i)}$ 的压缩性，证明它是 Cauchy 列；
**代数视角**：诺伊曼级数 $(\mathrm{I} - A)^{-1} = \sum_{k\ge0} A^k$ 在 $\rho(A)<1$ 时收敛。

## 链接

- 数学分析：[[ANL-THM-006]] 单调有界定理、[[ANL-DEF-004]] 数列收敛的 $\varepsilon$-$N$ 定义、[[CROSS-002]] 迭代法收敛的完整版本
- 高等代数：[[ALG-THM-043]] Jordan 标准形的存在与唯一、[[ALG-THM-041]] Cayley–Hamilton 定理、[[ALG-EX-018]] 矩阵幂与递推
- 生成函数视角：[[CROSS-010]]
