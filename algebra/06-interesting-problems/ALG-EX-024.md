---
title: "迹、特征值与牛顿恒等式"
type: example
id: ALG-EX-024
subject: algebra
chapter: 06-interesting-problems
tags:
  - 特征多项式
  - 迹
  - 牛顿恒等式
  - 对称多项式
depends:
  - ALG-DEF-036
  - ALG-DEF-035
  - ALG-THM-041
uses: []
status: stable
source: "经典问题；参考丘维声《高等代数》第3版 §1.8、§5.3"
difficulty: 4
illustrates:
  - ALG-DEF-036
related:
  - ALG-THM-044
  - ALG-EX-016
---

## 题目

设 $A$ 为 $n$ 阶复矩阵，特征值为 $\lambda_1, \dots, \lambda_n$（按代数重数计），记幂和为 $p_k = \operatorname{tr}(A^k) = \sum_{i=1}^{n} \lambda_i^k$（$k \ge 1$），并设

$$
\chi_A(\lambda) = \det(\lambda I - A) = \prod_{i=1}^{n}(\lambda - \lambda_i) = \lambda^n - e_1 \lambda^{n-1} + e_2 \lambda^{n-2} - \cdots + (-1)^n e_n,
$$

其中 $e_k$ 是 $\lambda_1, \dots, \lambda_n$ 的 $k$ 阶初等对称多项式（[[ALG-DEF-008]]）。完成以下各题：

1. 证明牛顿恒等式 $k e_k = \sum_{i=1}^{k} (-1)^{i-1} e_{k-i} p_i$（$1 \le k \le n$，约定 $e_0 = 1$）。
2. 说明如何只由 $p_1, \dots, p_n$ 求出特征多项式 $\chi_A$。
3. 用二阶、三阶矩阵各完整验证一次。
4. 联系 Cayley–Hamilton 定理（[[ALG-THM-041]]）解释 $p_k$ 的线性递推。

## 分析

特征值把两组数据连在一起：$\chi_A$ 的系数是初等对称多项式 $e_k$，而 $p_k$ 是特征值的幂和（由 $A$ 可上三角化，见 [[ALG-THM-043]]，$\operatorname{tr}(A^k)$ 等于特征值的 $k$ 次幂之和）。牛顿恒等式说明这两组数据可以互相递推得到。直接对 $k \le n$ 推导并不方便，因为特征多项式只在高次幂上给出关系；统一做法是引入生成函数 $E(t) = \prod_{i=1}^{n}(1 + \lambda_i t)$，它的系数正是 $e_k$，而对数导数恰好给出 $p_k$，比较 $E'(t)$ 两端的系数即可。矩阵层面同理：Cayley–Hamilton 定理说 $\chi_A(A) = 0$，用它乘以 $A$ 的幂再取迹，就得到 $p_k$ 的线性递推，与特征值层面的递推完全一致。

## 证明 / 解答

### 牛顿恒等式的生成函数证明

令 $e_0 = 1$，定义

$$
E(t) = \prod_{i=1}^{n}(1 + \lambda_i t) = \sum_{k=0}^{n} e_k t^k.
$$

作为形式幂级数，$E(0) = 1$ 保证它可逆，且

$$
\frac{E'(t)}{E(t)} = \sum_{i=1}^{n} \frac{\lambda_i}{1 + \lambda_i t} = \sum_{i=1}^{n} \sum_{m=0}^{\infty} (-1)^m \lambda_i^{m+1} t^m = \sum_{m=0}^{\infty} (-1)^m p_{m+1} t^m.
$$

于是 $E'(t) = E(t) \sum_{m=0}^{\infty} (-1)^m p_{m+1} t^m$。左边 $t^{k-1}$ 的系数为 $k e_k$，右边为

$$
\sum_{i=0}^{k-1} e_i (-1)^{k-1-i} p_{k-i} = \sum_{j=1}^{k} (-1)^{j-1} e_{k-j} p_j,
$$

其中做了换元 $j = k - i$，并约定 $e_i = 0$（$i > n$）。比较系数得

$$
k e_k = \sum_{i=1}^{k} (-1)^{i-1} e_{k-i} p_i, \qquad 1 \le k \le n.
$$

当 $k > n$ 时左端系数为 $0$（$E$ 的次数为 $n$），得到幂和的线性递推

$$
p_k - e_1 p_{k-1} + e_2 p_{k-2} - \cdots + (-1)^n e_n p_{k-n} = 0, \qquad k > n.
$$

### 只由幂和确定特征多项式

第 $k$ 个牛顿恒等式除 $e_k$ 外只出现 $e_1, \dots, e_{k-1}$ 与 $p_1, \dots, p_k$，所以按 $k = 1, 2, \dots, n$ 的顺序可以逐个解出 $e_k$。前几项是

$$
e_1 = p_1, \qquad e_2 = \frac{p_1^2 - p_2}{2}, \qquad e_3 = \frac{p_1^3 - 3p_1 p_2 + 2p_3}{6}.
$$

一般地，$p_1, \dots, p_n$ 依次定出 $e_1, \dots, e_n$，从而

$$
\chi_A(\lambda) = \lambda^n - e_1 \lambda^{n-1} + e_2 \lambda^{n-2} - \cdots + (-1)^n e_n.
$$

反过来，上面的 $k > n$ 递推说明 $p_{n+1}, p_{n+2}, \dots$ 全部由 $\chi_A$ 决定。因此对固定阶数 $n$，"前 $n$ 个幂和"与"特征多项式"是互相确定的。

### 二阶矩阵的例子

取 $A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$。则 $p_1 = \operatorname{tr}A = 5$，且

$$
A^2 = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}\begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} = \begin{pmatrix} 5 & 5 \\ 5 & 10 \end{pmatrix}, \qquad p_2 = \operatorname{tr}(A^2) = 15.
$$

由牛顿恒等式 $e_1 = p_1 = 5$，$2e_2 = e_1 p_1 - p_2 = 25 - 15 = 10$，故 $e_2 = 5$，即 $\chi_A(\lambda) = \lambda^2 - 5\lambda + 5$，与 $\operatorname{tr}A = 5$、$\det A = 6 - 1 = 5$ 一致。再用递推检验：$p_3 = e_1 p_2 - e_2 p_1 = 75 - 25 = 50$，而 $A^3 = A^2 A = \begin{pmatrix} 15 & 20 \\ 20 & 35 \end{pmatrix}$，$\operatorname{tr}(A^3) = 50$，结果一致。

### 三阶矩阵的例子

取

$$
C = \begin{pmatrix} 0 & 0 & 6 \\ 1 & 0 & -11 \\ 0 & 1 & 6 \end{pmatrix}.
$$

直接计算幂与迹：

$$
C^2 = \begin{pmatrix} 0 & 6 & 36 \\ 0 & -11 & -60 \\ 1 & 6 & 25 \end{pmatrix}, \qquad
C^3 = \begin{pmatrix} 6 & 36 & 150 \\ -11 & -60 & -239 \\ 6 & 25 & 90 \end{pmatrix},
$$

故 $p_1 = \operatorname{tr}C = 6$，$p_2 = \operatorname{tr}(C^2) = 14$，$p_3 = \operatorname{tr}(C^3) = 36$。由牛顿恒等式

$$
e_1 = 6, \qquad e_2 = \frac{e_1 p_1 - p_2}{2} = \frac{36 - 14}{2} = 11, \qquad e_3 = \frac{e_2 p_1 - e_1 p_2 + p_3}{3} = \frac{66 - 84 + 36}{3} = 6,
$$

因此 $\chi_C(\lambda) = \lambda^3 - 6\lambda^2 + 11\lambda - 6 = (\lambda - 1)(\lambda - 2)(\lambda - 3)$。这个分解可直接验证：三个向量 $v_1 = (6,-5,1)^{\mathsf{T}}$、$v_2 = (3,-4,1)^{\mathsf{T}}$、$v_3 = (2,-3,1)^{\mathsf{T}}$ 分别满足 $C v_1 = v_1$、$C v_2 = 2v_2$、$C v_3 = 3v_3$；特征值互不相同，对应特征向量线性无关，故特征多项式正是上式。再用递推检验 $p_4 = 6 \cdot 36 - 11 \cdot 14 + 6 \cdot 6 = 216 - 154 + 36 = 98 = 1^4 + 2^4 + 3^4$。

### 与 Cayley–Hamilton 定理的联系

由 [[ALG-THM-041]]，

$$
\chi_A(A) = A^n - e_1 A^{n-1} + e_2 A^{n-2} - \cdots + (-1)^n e_n I = 0.
$$

用 $A^{k-n}$（$k \ge n$）右乘并取迹，约定 $p_0 = \operatorname{tr} I = n$，得

$$
p_k - e_1 p_{k-1} + \cdots + (-1)^{n-1} e_{n-1} p_{k-n+1} + (-1)^n e_n p_{k-n} = 0.
$$

取 $k = n$ 就得到 $n e_n = \sum_{i=1}^{n} (-1)^{i-1} e_{n-i} p_i$，与牛顿恒等式一致。

$\blacksquare$

## 关键技巧

- **生成函数是统一工具**：把初等对称多项式装进 $E(t)$，取对数导数后比较系数，一次得到全部牛顿恒等式。
- **三角递推可逆**：$e_k$ 只依赖前面的 $e$ 与前 $k$ 个 $p$，故 $p_1, \dots, p_n$ 与 $\chi_A$ 互相确定。
- **符号约定要统一**：$\chi_A = \det(\lambda I - A)$ 的系数符号交替出现，全程固定 $e_0 = 1$ 可避免出错。
- **两个层面互推**：Cayley–Hamilton 定理给出与"特征值满足特征方程"完全相同的递推。
- **计算顺序**：先算 $p_1, p_2, \dots$，用牛顿恒等式回推 $e_k$，最后与 $\operatorname{tr}$、$\det$ 的直接计算核对。

## 变式

- **变式 1**：对二阶矩阵证明 $p_k = (\operatorname{tr}A) p_{k-1} - (\det A) p_{k-2}$（$k \ge 2$），并验证题目中 $A$ 的 $p_4 = 175$。
- **变式 2**：证明 $\operatorname{tr}(A^2) = (\operatorname{tr}A)^2 - 2e_2$，并说明 $e_2 = \frac{(\operatorname{tr}A)^2 - \operatorname{tr}(A^2)}{2}$ 就是 $\chi_A$ 中 $\lambda^{n-2}$ 的系数。
- **变式 3**：举出两个不相似但特征多项式相同的矩阵（例如 $2I_2$ 与 $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$），说明它们的全部幂和相同，因此幂和数据只确定特征多项式、不决定相似类。
- **变式 4**：若 $A$ 可逆，利用 $e_n = \det A$ 与牛顿恒等式说明 $e_n$ 与 $p_1, \dots, p_n$ 的关系，并解释为什么 $A$ 可逆等价于 $e_n \ne 0$。

## 链接

- 演示定义：[[ALG-DEF-036]] 特征多项式、[[ALG-DEF-035]] 特征值与特征向量
- 关键定理：[[ALG-THM-041]] Cayley–Hamilton 定理
- 前置概念：[[ALG-DEF-008]] 对称多项式与初等对称多项式
- 相关条目：[[ALG-THM-044]] 实对称矩阵的谱定理、[[ALG-EX-016]] 求特征值并对角化
