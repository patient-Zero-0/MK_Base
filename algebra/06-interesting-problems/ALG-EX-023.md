---
title: "分块矩阵、舒尔补与行列式引理"
type: example
id: ALG-EX-023
subject: algebra
chapter: 06-interesting-problems
tags:
  - 分块矩阵
  - 舒尔补
  - 行列式
  - 矩阵求逆
depends:
  - ALG-THM-015
  - ALG-DEF-015
  - ALG-THM-017
uses: []
status: stable
source: "经典问题；参考丘维声《高等代数》第3版 §2.2、§3.3"
difficulty: 3
illustrates:
  - ALG-THM-015
related: []
---

## 题目

设 $A$ 为 $p$ 阶可逆矩阵，$D$ 为 $q$ 阶方阵，$B$ 为 $p \times q$ 矩阵，$C$ 为 $q \times p$ 矩阵，记舒尔补与分块矩阵为

$$
S = D - C A^{-1} B, \qquad M = \begin{pmatrix} A & B \\ C & D \end{pmatrix}.
$$

完成以下四题：

1. 验证分块恒等式 $M = L \operatorname{diag}(A,S) U$（$L$、$U$ 为主对角块是单位阵的块三角矩阵），从而 $\det M = \det A \cdot \det S$。
2. 当 $S$ 可逆时，求 $M^{-1}$ 的分块表达式并逐块验证。
3. 证明矩阵行列式引理 $\det(I_n + u v^{\mathsf{T}}) = 1 + v^{\mathsf{T}} u$，并用它计算 $u = (1,1,1)^{\mathsf{T}}$、$v = (1,2,3)^{\mathsf{T}}$ 的情形。
4. 讨论 $A$ 不可逆时上述公式的处理方式。

## 分析

分块矩阵可以按块运算，但块与块相乘的顺序不能交换；舒尔补的实质是块消元，用第一块行把 $C$ 消掉，剩下的右下块就是 $S = D - C A^{-1}B$。整个题目围绕同一个想法展开：把 $M$ 分解成两个行列式为 $1$ 的块三角矩阵夹一个块对角矩阵，再用行列式乘法定理（[[ALG-THM-015]]）把 $\det M$ 拆成 $\det A \cdot \det S$。分块求逆公式的验证只是逐块矩阵乘法，关键替换是 $CA^{-1}B = D - S$；行列式引理则是同一个舒尔补公式在 $1 \times 1$ 主元上的特例。

$A$ 不可逆时 $A^{-1}$ 没有意义，但行列式是矩阵元素的多项式。此时可以换一个可逆角块作主元，或借助伴随矩阵（[[ALG-DEF-015]]）把含逆的表达式化为多项式，再用连续性把结论延拓到奇异情形。

## 证明 / 解答

### 第一步：验证分块分解

取

$$
L = \begin{pmatrix} I_p & 0 \\ C A^{-1} & I_q \end{pmatrix},
\qquad
U = \begin{pmatrix} I_p & A^{-1} B \\ 0 & I_q \end{pmatrix}.
$$

按分块乘法计算，先乘块对角矩阵再乘 $U$：

$$
L \operatorname{diag}(A,S) U
= \begin{pmatrix} A & 0 \\ C & S \end{pmatrix}
\begin{pmatrix} I_p & A^{-1}B \\ 0 & I_q \end{pmatrix}
= \begin{pmatrix} A & A A^{-1}B \\ C & C A^{-1}B + S \end{pmatrix}
= \begin{pmatrix} A & B \\ C & D \end{pmatrix}
= M,
$$

最后一步用了 $S = D - C A^{-1}B$。中间第一个等号也用了分块乘法：左上块 $I_p A = A$，右上块 $0$，左下块 $C A^{-1} A = C$，右下块 $S$。

### 第二步：舒尔补公式

先算块三角矩阵的行列式。设 $P$、$Q$ 分别为 $p$、$q$ 阶方阵，$X$ 为 $q \times p$ 矩阵。对 $\begin{pmatrix} P & 0 \\ X & Q \end{pmatrix}$ 按前 $p$ 列作 Laplace 展开（[[ALG-THM-014]]），只有取前 $p$ 行时子式可能非零，因为其他取法会让余子式含右上方零块的一整行零。于是

$$
\det \begin{pmatrix} P & 0 \\ X & Q \end{pmatrix} = \det P \cdot \det Q,
$$

符号为 $(-1)^{(1+\cdots+p)+(1+\cdots+p)} = 1$。取转置（[[ALG-DEF-013]]）得上块三角矩阵也有同样公式。于是 $\det L = 1$，$\det U = 1$，$\det \operatorname{diag}(A,S) = \det A \cdot \det S$，从而

$$
\det M = \det L \cdot \det \operatorname{diag}(A,S) \cdot \det U
= \det A \cdot \det S.
$$

### 第三步：分块求逆

当 $S$ 可逆时，令

$$
M^{-1} = \begin{pmatrix}
A^{-1} + A^{-1} B S^{-1} C A^{-1} & -A^{-1} B S^{-1} \\
-S^{-1} C A^{-1} & S^{-1}
\end{pmatrix}.
$$

与 $M$ 相乘，四个块依次为

$$
\begin{aligned}
\text{(1,1) 块} &= A\left(A^{-1} + A^{-1}BS^{-1}CA^{-1}\right) - B S^{-1} C A^{-1} = I_p, \\
\text{(1,2) 块} &= -A A^{-1} B S^{-1} + B S^{-1} = 0, \\
\text{(2,1) 块} &= C A^{-1} + C A^{-1} B S^{-1} C A^{-1} - D S^{-1} C A^{-1} = 0, \\
\text{(2,2) 块} &= -C A^{-1} B S^{-1} + D S^{-1} = -(D-S)S^{-1} + D S^{-1} = I_q,
\end{aligned}
$$

其中 (1,1) 块用到 $A A^{-1} = I_p$，(2,1) 与 (2,2) 块用到 $C A^{-1} B = D - S$。因此乘积为单位阵，公式成立。

### 第四步：行列式引理

对 $u, v \in \mathbb{R}^n$，考虑 $(n+1)$ 阶分块矩阵

$$
N = \begin{pmatrix} 1 & -v^{\mathsf{T}} \\ u & I_n \end{pmatrix}.
$$

它的两个主对角块 $1$ 与 $I_n$ 都可逆。以 $1$ 为主元用舒尔补公式：$\det N = 1 \cdot \det(I_n - u \cdot 1 \cdot (-v^{\mathsf{T}})) = \det(I_n + uv^{\mathsf{T}})$。以 $I_n$ 为主元：$\det N = \det I_n \cdot \det(1 - (-v^{\mathsf{T}}) I_n^{-1} u) = 1 + v^{\mathsf{T}}u$。同一个行列式的两个值相等，故 $\det(I_n + u v^{\mathsf{T}}) = 1 + v^{\mathsf{T}}u$。

取 $u = (1,1,1)^{\mathsf{T}}$、$v = (1,2,3)^{\mathsf{T}}$，则 $v^{\mathsf{T}}u = 6$，引理给出 $\det = 7$。直接核对：$I_3 + uv^{\mathsf{T}} = \begin{pmatrix} 2 & 2 & 3 \\ 1 & 3 & 3 \\ 1 & 2 & 4 \end{pmatrix}$，按第一行展开得

$$
\det = 2 \cdot (12 - 6) - 2 \cdot (4 - 3) + 3 \cdot (2 - 3) = 12 - 2 - 3 = 7.
$$

### 第五步：主元块不可逆时

当 $A$ 奇异时 $A^{-1}$ 不存在，舒尔补公式右端没有定义。但行列式是矩阵元素的连续函数，有两种处理方式。一是换主元：只要 $D$ 可逆就用 $\det M = \det D \cdot \det(A - B D^{-1}C)$。二是若两个对角块都奇异，用加边法（[[ALG-THM-018]]）或对 $B$、$C$ 作秩分解，把问题化到角块可逆的情形。

不能直接把 $A+tI$ 的公式取极限来代替奇异情形：$t \to 0$ 时 $S(t) = D - C(A+tI)^{-1}B$ 可能发散。例如 $A = (0)$、$B = C = (1)$、$D = (0)$ 时 $S(t) = -1/t$ 没有极限，但乘积 $\det(A+tI)S(t) = t \cdot (-1/t) = -1$ 仍收敛到 $\det M = -1$。

行列式引理则有干净的多项式延拓。设 $A$ 奇异，对充分小的 $t$（使 $A+tI$ 可逆）有

$$
\det(A + tI + uv^{\mathsf{T}}) = \det(A+tI) + v^{\mathsf{T}} \operatorname{adj}(A+tI) u,
$$

这里用了 $(A+tI)\operatorname{adj}(A+tI) = \det(A+tI)I$（[[ALG-DEF-015]]）与可逆性刻画（[[ALG-THM-017]]）。伴随矩阵的元素是 $n-1$ 阶子式，所以两端都是 $t$ 的多项式，在无穷多个 $t$ 上相等，故恒等。令 $t = 0$ 得

$$
\det(A + uv^{\mathsf{T}}) = \det A + v^{\mathsf{T}} \operatorname{adj}(A) u.
$$

例如 $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$、$u = (1,1)^{\mathsf{T}}$、$v = (1,-1)^{\mathsf{T}}$ 时，$\det A = 0$，$\operatorname{adj}(A) = \begin{pmatrix} 4 & -2 \\ -2 & 1 \end{pmatrix}$，$v^{\mathsf{T}}\operatorname{adj}(A)u = 2 + 1 = 3$；直接算 $A + uv^{\mathsf{T}} = \begin{pmatrix} 2 & 1 \\ 3 & 3 \end{pmatrix}$ 的行列式也是 $3$。

$\blacksquare$

## 关键技巧

- **块初等变换**：左乘 $\begin{pmatrix} I & 0 \\ X & I \end{pmatrix}$ 相当于把第一块行乘 $X$ 加到第二块行，行列式不变，这是消元的矩阵语言。
- **舒尔补是块消元的剩余**：化成块三角后剩下的右下块正是 $D - C A^{-1}B$，与解方程消元后保留的方程同源。
- **行列式乘法定理反复用**：先把行列式拆成因子矩阵行列式之积，再分别计算块三角因子的行列式。
- **秩一更新转化为内积**：$\det(I + uv^{\mathsf{T}}) = 1 + v^{\mathsf{T}}u$ 把行列式问题变成内积问题。
- **伴随矩阵作多项式桥梁**：$\det(A+tI)(A+tI)^{-1} = \operatorname{adj}(A+tI)$ 把含逆的表达式变成多项式，是处理奇异情形的标准手段。

## 变式

- **变式 1**：证明 $D$ 可逆时 $\det M = \det D \cdot \det(A - B D^{-1}C)$，并说明 $A$、$D$ 都可逆时两个公式一致。
- **变式 2**：证明 Sherman–Morrison 公式 $(A + uv^{\mathsf{T}})^{-1} = A^{-1} - \dfrac{A^{-1}uv^{\mathsf{T}}A^{-1}}{1 + v^{\mathsf{T}}A^{-1}u}$（分母非零），并在 $A = I_3$ 时用题目中的 $u$、$v$ 验证。
- **变式 3**：把秩一更新换成秩 $r$ 的更新 $UV^{\mathsf{T}}$，证明 Sylvester 行列式恒等式 $\det(I_n + UV^{\mathsf{T}}) = \det(I_r + V^{\mathsf{T}}U)$。
- **变式 4**：用加边法（[[ALG-THM-018]]）另证 $\det(I_n + uv^{\mathsf{T}}) = 1 + v^{\mathsf{T}}u$，并比较两种证法。

## 链接

- 演示定理：[[ALG-THM-015]] 行列式乘法定理、[[ALG-DEF-015]] 伴随矩阵、[[ALG-THM-017]] 可逆性刻画
- 使用工具：[[ALG-THM-014]] Laplace 定理、[[ALG-DEF-013]] 转置行列式、[[ALG-THM-018]] 加边法
- 相关问题：[[ALG-EX-005]] Vandermonde 行列式计算、[[ALG-EX-027]] 四元数与行列式
