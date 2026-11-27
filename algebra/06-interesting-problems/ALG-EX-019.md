---
title: "哈密顿-凯莱定理的若干妙用"
type: example
id: ALG-EX-019
subject: algebra
chapter: 06-interesting-problems
tags:
  - Cayley-Hamilton
  - 矩阵多项式
  - 矩阵幂
  - 逆矩阵
depends:
  - ALG-THM-041
  - ALG-THM-036
  - ALG-DEF-036
uses: []
status: stable
source: "丘维声《高等代数》第3版 §5.5"
difficulty: 3
illustrates:
  - ALG-THM-041
related:
  - ALG-EX-017
  - ALG-PROB-019
---

## 题目

设 $A$ 为 $n$ 阶方阵，$\chi_A(\lambda) = \det(\lambda I - A)$ 为特征多项式，$\operatorname{tr} A$ 为迹。Cayley–Hamilton 定理（[[ALG-THM-041]]）断言 $\chi_A(A) = 0$。本题练习由它派生出的几种计算：

1. 对 $2$ 阶方阵直接验证 $A^2 - (\operatorname{tr} A)A + (\det A)I = 0$；
2. 当 $\det A \neq 0$ 时求 $A^{-1}$ 的矩阵多项式；
3. 把高次多项式 $p(A)$ 降为次数小于 $n$ 的多项式；
4. 导出 $A^k$ 的线性递推，并对一个 $3$ 阶循环矩阵验证定理、求出逆矩阵。

## 分析

Cayley–Hamilton 定理把 $A$ 变成特征多项式的"根"，这是一个可以在矩阵环内移项、乘以 $A^k$ 的关系式，而不是数值方程。围绕它可以做三件事：对高次多项式做带余除法降次；从常数项移项得到逆矩阵；解出最高次幂并递推所有 $A^k$。$2$ 阶情形能直接验证，可用于检查公式的符号；$3$ 阶循环矩阵则给出一个必须真正使用定理的例子。

## 证明 / 解答

### 第一步：二阶情形的直接验证

设 $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$，则 $\operatorname{tr} A = a+d$、$\det A = ad-bc$，且

$$
A^2 = \begin{pmatrix} a^2 + bc & ab + bd \\ ac + cd & bc + d^2 \end{pmatrix}, \qquad (\operatorname{tr} A)A = \begin{pmatrix} a^2 + ad & ab + bd \\ ac + cd & ad + d^2 \end{pmatrix}.
$$

逐元素相减即得

$$
A^2 - (\operatorname{tr} A)A + (\det A)I = \begin{pmatrix} a^2 + bc - (a^2 + ad) + (ad - bc) & ab + bd - (ab + bd) \\ ac + cd - (ac + cd) & bc + d^2 - (ad + d^2) + (ad - bc) \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}.
$$

### 第二步：逆矩阵的多项式表达

把恒等式移项得 $A^2 - (\operatorname{tr} A)A = -(\det A)I$，即 $A\left((\operatorname{tr} A)I - A\right) = (\det A)I$。当 $\det A \neq 0$ 时

$$
A^{-1} = \frac{1}{\det A}\left((\operatorname{tr} A)I - A\right).
$$

例如 $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ 满足 $\operatorname{tr} A = 5$、$\det A = -2$，故 $A^{-1} = -\frac12(5I - A) = \begin{pmatrix} -2 & 1 \\ 3/2 & -1/2 \end{pmatrix}$，直接相乘可验证 $AA^{-1} = I$。

一般地，若 $\chi_A(\lambda) = \lambda^n + c_{n-1}\lambda^{n-1} + \cdots + c_1\lambda + c_0$，则 $c_0 = (-1)^n\det A$；由 $\chi_A(A) = 0$ 两边左乘 $A^{-1}$ 得

$$
A^{-1} = -\frac{1}{c_0}\left(A^{n-1} + c_{n-1}A^{n-2} + \cdots + c_1 I\right).
$$

### 第三步：高次多项式的降次

对任意 $p \in K[x]$ 作带余除法 $p(\lambda) = q(\lambda)\chi_A(\lambda) + r(\lambda)$，$\deg r < n$；代入 $A$ 得

$$
p(A) = q(A)\chi_A(A) + r(A) = r(A).
$$

具体计算：取 $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$，$p(x) = x^5 - 2x^3 + x + 1$。由第一步 $\chi_A(x) = x^2 - 5x - 2$，即在模 $\chi_A$ 下 $x^2 \equiv 5x + 2$，逐次降次得

$$
x^3 \equiv 5x^2 + 2x \equiv 27x + 10, \qquad x^4 \equiv 27x^2 + 10x \equiv 145x + 54, \qquad x^5 \equiv 145x^2 + 54x \equiv 779x + 290.
$$

于是

$$
p(x) \equiv (779x + 290) - 2(27x + 10) + x + 1 = 726x + 271 \pmod{\chi_A},
$$

即 $p(A) = 726A + 271I$。核对：$A^2 = \begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix}$、$A^3 = \begin{pmatrix} 37 & 54 \\ 81 & 118 \end{pmatrix}$、$A^5 = \begin{pmatrix} 1069 & 1558 \\ 2337 & 3406 \end{pmatrix}$，故

$$
A^5 - 2A^3 + A + I = \begin{pmatrix} 997 & 1452 \\ 2178 & 3175 \end{pmatrix} = 726A + 271I.
$$

### 第四步：矩阵幂的线性递推

把 $\chi_A(A) = 0$ 解出最高次幂再乘 $A^k$：

$$
A^{n+k} = -\left(c_{n-1}A^{n-1+k} + \cdots + c_1 A^{1+k} + c_0 A^k\right).
$$

于是 $A^k$ 的每个元素都满足由特征多项式系数给出的 $n$ 阶线性递推。对 $2$ 阶矩阵即 $A^{k+2} = (\operatorname{tr} A)A^{k+1} - (\det A)A^k$。仍取上面的 $A$，则 $A^{k+2} = 5A^{k+1} + 2A^k$。若写成 $A^k = u_k A + v_k I$，则 $u_k, v_k$ 都满足 $x_{k+2} = 5x_{k+1} + 2x_k$，初值为 $(u_0,u_1) = (0,1)$、$(v_0,v_1) = (1,0)$，从而

$$
u_2 = 5,\ u_3 = 27,\ u_4 = 145,\ u_5 = 779; \qquad v_2 = 2,\ v_3 = 10,\ v_4 = 54,\ v_5 = 290.
$$

例如 $A^5 = 779A + 290I$，与第三步算出的 $A^5$ 一致。

### 第五步：三阶循环矩阵的验证与求逆

取循环矩阵 $C = \begin{pmatrix} 1 & 2 & 3 \\ 3 & 1 & 2 \\ 2 & 3 & 1 \end{pmatrix}$，其特征多项式为

$$
\chi_C(\lambda) = \det\begin{pmatrix} \lambda - 1 & -2 & -3 \\ -3 & \lambda - 1 & -2 \\ -2 & -3 & \lambda - 1 \end{pmatrix} = (\lambda - 1)\left[(\lambda - 1)^2 - 6\right] + 2\left[-3(\lambda - 1) - 4\right] - 3\left[9 + 2(\lambda - 1)\right] = \lambda^3 - 3\lambda^2 - 15\lambda - 18.
$$

按 Cayley–Hamilton 定理应有 $C^3 - 3C^2 - 15C - 18I = 0$。直接计算：

$$
C^2 = \begin{pmatrix} 13 & 13 & 10 \\ 10 & 13 & 13 \\ 13 & 10 & 13 \end{pmatrix}, \qquad C^3 = \begin{pmatrix} 72 & 69 & 75 \\ 75 & 72 & 69 \\ 69 & 75 & 72 \end{pmatrix},
$$

而

$$
3C^2 + 15C + 18I = \begin{pmatrix} 39 & 39 & 30 \\ 30 & 39 & 39 \\ 39 & 30 & 39 \end{pmatrix} + \begin{pmatrix} 15 & 30 & 45 \\ 45 & 15 & 30 \\ 30 & 45 & 15 \end{pmatrix} + \begin{pmatrix} 18 & 0 & 0 \\ 0 & 18 & 0 \\ 0 & 0 & 18 \end{pmatrix} = \begin{pmatrix} 72 & 69 & 75 \\ 75 & 72 & 69 \\ 69 & 75 & 72 \end{pmatrix} = C^3.
$$

定理对 $C$ 成立。又 $\chi_C$ 的常数项 $-18 = \det(-C) = -\det C$，故 $\det C = 18$；把 $C^3 - 3C^2 - 15C - 18I = 0$ 写成 $C(C^2 - 3C - 15I) = 18I$，得

$$
C^{-1} = \frac{1}{18}\left(C^2 - 3C - 15I\right) = \frac{1}{18}\begin{pmatrix} -5 & 7 & 1 \\ 1 & -5 & 7 \\ 7 & 1 & -5 \end{pmatrix},
$$

验证 $C$ 与该矩阵之积为 $18I$，即 $CC^{-1} = I$。

$\blacksquare$

## 关键技巧

- **把定理当关系式用**：$\chi_A(A) = 0$ 可在矩阵环内移项、乘 $A^k$，这是所有应用的出发点。
- **带余除法降次**：$p(A)$ 的次数由对 $\chi_A$ 取余控制；这是计算矩阵函数的第一步，若尔当标准形（[[ALG-THM-043]]）是另一条路线。
- **常数项给逆**：$\chi_A$ 的常数项是 $(-1)^n\det A$，$\det A \neq 0$ 时当场得到 $A^{-1}$。
- **递推来自移项**：解出最高次幂再乘 $A^k$，得到所有矩阵幂的线性递推。
- **先小后大**：$2$ 阶直接验证、$3$ 阶用具体数字核对，可靠地检查符号与系数。

## 变式

- **变式 1**：对 $3$ 阶矩阵写出 $A^{-1} = -\frac{1}{c_0}(A^2 + c_2A + c_1I)$，并重做上面循环矩阵的求逆。
- **变式 2（最小多项式）**：Cayley–Hamilton 给出的关系不一定次数最低；例如 $A = I_2$ 的 $\chi_A(\lambda) = (\lambda - 1)^2$，但 $A - I = 0$ 已经成立，可与最小多项式（[[ALG-THM-042]]）比较。
- **变式 3**：证明相似矩阵有相同的特征多项式：$\det(\lambda I - P^{-1}AP) = \det(P^{-1}(\lambda I - A)P) = \det(\lambda I - A)$。
- **变式 4**：用 Cayley–Hamilton 把 $e^{At} = \sum_{k\ge0} A^kt^k/k!$ 化为 $I, A, \ldots, A^{n-1}$ 的含 $t$ 的线性组合，并与矩阵指数解微分方程组对照。

## 链接

- 演示定理：[[ALG-THM-041]] Cayley–Hamilton 定理
- 前置：[[ALG-DEF-036]] 特征多项式、[[ALG-THM-036]] 线性变换与矩阵一一对应
- 相关例题：[[ALG-EX-017]]、[[ALG-PROB-019]]
- 延伸：[[ALG-THM-042]] 最小多项式、[[ALG-THM-043]] 若尔当标准形
