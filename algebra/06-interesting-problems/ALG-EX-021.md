---
title: "结式与判别式：方程何时有重根"
type: example
id: ALG-EX-021
subject: algebra
chapter: 06-interesting-problems
tags:
  - 结式
  - 判别式
  - 行列式
  - 重根
depends:
  - ALG-THM-014
  - ALG-THM-006
  - ALG-DEF-012
  - ALG-THM-005
uses: []
status: stable
source: "经典问题；参考丘维声《高等代数》第3版 §1.4、§2.3"
difficulty: 4
illustrates:
  - ALG-THM-014
related:
  - ALG-EX-002
  - ALG-THM-009
---

## 题目

设 $f(x) = a_nx^n + \cdots + a_0$ 与 $g(x) = b_mx^m + \cdots + b_0$ 是复系数非零多项式，$a_nb_m \neq 0$，记 $\deg f = n$、$\deg g = m$，且 $n, m \ge 1$。

1. 定义 Sylvester 矩阵 $S(f,g)$ 与结式 $\operatorname{Res}(f,g) = \det S(f,g)$，并证明 $\operatorname{Res}(f,g) = 0$ 当且仅当 $f$ 与 $g$ 有公共复根；
2. 定义判别式 $\Delta(f) = (-1)^{n(n-1)/2}a_n^{-1}\operatorname{Res}(f,f')$，证明 $\Delta(f) = 0$ 当且仅当 $f$ 有重根；
3. 计算二次与三次多项式的判别式，并举例验证；
4. 说明结式是消元的行列式表达，以及它与 Laplace 展开的关系。

## 分析

两个方程 $f = g = 0$ 有公共解，等价于存在次数受限的非零多项式 $u, v$ 使 $uf + vg = 0$：由 $f \mid vg$ 且 $\deg v < \deg f$ 可推出 $f$ 与 $g$ 有公因式。把 $uf + vg = 0$ 的系数方程排成线性方程组，其系数矩阵与 Sylvester 矩阵互为转置——于是"有没有公共根"变成一个行列式是否为零的问题，这是消元法的线性代数版本。判别式则把这个判据用在 $f$ 与 $f'$ 上：重根处 $f$ 与 $f'$ 同时为零。

## 证明 / 解答

### 第一步：Sylvester 矩阵的定义

以下设 $n, m \ge 1$。$S(f,g)$ 是 $n+m$ 阶方阵：前 $m$ 行是 $f$ 的系数向量的平移（第 $i$ 行把 $a_n$ 放在第 $i$ 列，其后依次是 $a_{n-1}, \ldots, a_0$），后 $n$ 行是 $g$ 的系数向量的平移（第 $m+j$ 行把 $b_m$ 放在第 $j$ 列，其后依次是 $b_{m-1}, \ldots, b_0$）。定义

$$
\operatorname{Res}(f,g) = \det S(f,g).
$$

以 $f = x^2 - 3x + 2$（$n = 2$）、$g = x^2 - 4x + 3$（$m = 2$）为例：

$$
S(f,g) = \begin{pmatrix} 1 & -3 & 2 & 0 \\ 0 & 1 & -3 & 2 \\ 1 & -4 & 3 & 0 \\ 0 & 1 & -4 & 3 \end{pmatrix}.
$$

### 第二步：结式为零当且仅当有公共根

设 $u = \sum_{i=0}^{m-1}u_ix^i$、$v = \sum_{j=0}^{n-1}v_jx^j$，它们各有 $m$ 与 $n$ 个待定系数。乘积 $uf + vg$ 的次数不超过 $m+n-1$，令其全部 $m+n$ 个系数为零，得到 $m+n$ 个线性方程。按降幂排列方程、按 $(u_{m-1}, \ldots, u_0, v_{n-1}, \ldots, v_0)$ 排列未知量，系数矩阵恰为 $S(f,g)^{\mathsf T}$。因此

$$
S(f,g) \text{ 奇异} \iff \exists\, (u,v) \neq (0,0),\ \deg u < m,\ \deg v < n,\ uf + vg = 0.
$$

**必要性**：设这样的 $(u,v)$ 存在。若 $u = 0$，则由 $vg = 0$ 得 $v = 0$（多项式环无零因子），矛盾，故 $u \neq 0$；同理 $v \neq 0$。由 $uf = -vg$ 得 $f \mid vg$。因 $\deg v < n = \deg f$，$f$ 不整除 $v$；令 $d = \gcd(f,v)$，则 $f/d$ 是次数至少为 $1$ 的多项式且整除 $g$。由代数基本定理（[[ALG-THM-007]]），$f/d$ 在 $\mathbb{C}$ 中有根 $\alpha$，它也是 $f$ 与 $g$ 的公共根。

**充分性**：设 $\alpha$ 是公共根，写 $f = (x - \alpha)f_1$、$g = (x - \alpha)g_1$，其中 $\deg f_1 = n-1$、$\deg g_1 = m-1$。取 $u = g_1$、$v = -f_1$，则 $uf + vg = 0$ 且 $\deg u = m-1 < m$、$\deg v = n-1 < n$，是非零解，故 $S(f,g)$ 奇异，即 $\operatorname{Res}(f,g) = 0$。

对第一步中的例子，$f = (x-1)(x-2)$、$g = (x-1)(x-3)$ 有公共根 $1$。对 $S$ 依次作 $R_3 \leftarrow R_3 - R_1$、$R_4 \leftarrow R_4 - R_2$、$R_3 \leftarrow R_3 + R_2$、$R_3 \leftarrow R_3 - 2R_4$，第三行化为零行，故 $\operatorname{Res}(f,g) = 0$；对应的关系式取 $u = x-3$、$v = 2-x$ 即可验证。

### 第三步：判别式与重根

按题目中的归一化定义判别式，以下设 $n = \deg f \ge 2$，此时 $\deg f' = n-1 \ge 1$，第二步的判据适用。由于 $a_n \neq 0$，$\Delta(f) = 0 \iff \operatorname{Res}(f,f') = 0 \iff f$ 与 $f'$ 有公共复根 $\alpha$，即 $f(\alpha) = f'(\alpha) = 0$。

若 $f(\alpha) = f'(\alpha) = 0$，写 $f = (x-\alpha)h$，则 $f' = h + (x-\alpha)h'$，于是 $h(\alpha) = f'(\alpha) = 0$，即 $(x-\alpha) \mid h$，故 $(x-\alpha)^2 \mid f$，$\alpha$ 是 $f$ 的重根。反之若 $(x-\alpha)^2 \mid f$，则 $f(\alpha) = f'(\alpha) = 0$，$\alpha$ 是公共根。所以

$$
\Delta(f) = 0 \iff f \text{ 有重根}.
$$

这与重因式判定（[[ALG-THM-006]]）一致：在 $\mathbb{C}$ 上重根就是重的一次因式，等价于 $\gcd(f,f') \neq 1$。$n = 1$ 时 $f$ 没有重根，把定义中的 Sylvester 矩阵退化情形算进去可得 $\Delta(f) = 1 \neq 0$，结论同样成立。

### 第四步：二次多项式的判别式

$f = ax^2 + bx + c$，$f' = 2ax + b$，此时 $n = 2$、$m = 1$：

$$
S(f,f') = \begin{pmatrix} a & b & c \\ 2a & b & 0 \\ 0 & 2a & b \end{pmatrix}.
$$

按第一行展开：

$$
\operatorname{Res}(f,f') = a\begin{vmatrix} b & 0 \\ 2a & b \end{vmatrix} - b\begin{vmatrix} 2a & 0 \\ 0 & b \end{vmatrix} + c\begin{vmatrix} 2a & b \\ 0 & 2a \end{vmatrix} = ab^2 - 2ab^2 + 4a^2c = -a(b^2 - 4ac).
$$

因此

$$
\Delta(f) = (-1)^{1}a^{-1}\operatorname{Res}(f,f') = b^2 - 4ac,
$$

与中学公式一致。若 $\alpha_1, \alpha_2$ 是两根，由 Vieta 公式 $(\alpha_1 - \alpha_2)^2 = (b^2 - 4ac)/a^2$，即 $\Delta(f) = a^2(\alpha_1 - \alpha_2)^2$，这正是"判别两根是否重合"的含义。

例：$f = 2x^2 - 3x + 1$ 时 $\Delta = 9 - 8 = 1 \neq 0$，两根 $1$ 与 $1/2$ 互异；$f = x^2 - 2x + 1$ 时 $\Delta = 0$，重根 $1$；$f = x^2 + x + 1$ 时 $\Delta = -3 \neq 0$，两根 $(-1 \pm \sqrt{3}\,i)/2$ 互异（虽然无实根）。

### 第五步：三次多项式的判别式

对首一三次多项式总可平移消去二次项，故先计算 $f = x^3 + px + q$ 的判别式；一般三次多项式的首项系数因子见变式 1。此时 $f' = 3x^2 + p$，$n = 3$、$m = 2$：

$$
S(f,f') = \begin{pmatrix} 1 & 0 & p & q & 0 \\ 0 & 1 & 0 & p & q \\ 3 & 0 & p & 0 & 0 \\ 0 & 3 & 0 & p & 0 \\ 0 & 0 & 3 & 0 & p \end{pmatrix}.
$$

作行变换 $R_3 \leftarrow R_3 - 3R_1$、$R_4 \leftarrow R_4 - 3R_2$，得

$$
S' = \begin{pmatrix} 1 & 0 & p & q & 0 \\ 0 & 1 & 0 & p & q \\ 0 & 0 & -2p & -3q & 0 \\ 0 & 0 & 0 & -2p & -3q \\ 0 & 0 & 3 & 0 & p \end{pmatrix}.
$$

前两行前两列形成对角线元素为 $1$ 的阶梯块，按第一列展开两次，得

$$
\operatorname{Res}(f,f') = \det\begin{pmatrix} -2p & -3q & 0 \\ 0 & -2p & -3q \\ 3 & 0 & p \end{pmatrix} = (-2p)(-2p^2) + 3q \cdot 9q = 4p^3 + 27q^2.
$$

其中 $3$ 阶行列式按第一行展开：$(-2p)\begin{vmatrix} -2p & -3q \\ 0 & p \end{vmatrix} + 3q\begin{vmatrix} 0 & -3q \\ 3 & p \end{vmatrix}$。于是

$$
\Delta(f) = (-1)^{3}\cdot 1^{-1}\cdot(4p^3 + 27q^2) = -(4p^3 + 27q^2) = -4p^3 - 27q^2.
$$

例：$f = x^3 - 3x + 2 = (x-1)^2(x+2)$，$p = -3$、$q = 2$，$\Delta = 108 - 108 = 0$，与有二重根 $1$ 一致；$f = x^3 - x = x(x-1)(x+1)$，$p = -1$、$q = 0$，$\Delta = 4 > 0$，三个互异实根；$f = x^3 + x + 1$，$p = q = 1$，$\Delta = -4 - 27 = -31 < 0$，因 $f' = 3x^2 + 1 > 0$ 在 $\mathbb{R}$ 上恒正，$f$ 严格递增，恰有一个实根，另两根为互异的共轭复数。

### 第六步：消元与 Laplace 展开

结式是"消去 $x$"的行列式表达。最简情形 $f = a_1x + a_0$、$g = b_1x + b_0$ 时

$$
\operatorname{Res}(f,g) = \begin{vmatrix} a_1 & a_0 \\ b_1 & b_0 \end{vmatrix} = a_1b_0 - a_0b_1,
$$

$\operatorname{Res}(f,g) = 0$ 等价于两个一次方程成比例，此时它们有公共根；行列式非零时两根不同、无公共根。这是消元最简情形下的完整判据。

计算上，Sylvester 矩阵的元素是系数的平移重复，展开时可以直接使用 Laplace 定理（[[ALG-THM-014]]）与 $k$ 阶子式（[[ALG-DEF-012]]）；实际计算通常先作初等变换消去大量元素（如第五步），把行列式化成含零块的形状，再用 Laplace 展开或按一行（列）展开，比硬展开 $m+n$ 阶行列式省力。判别式虽由结式定义，最终却写成关于系数的多项式，因此判断"是否有重根"只需对系数做一次多项式计算，不必解方程，也不必显式计算结式。

$\blacksquare$

## 关键技巧

- **消元等于线性方程组**：把"存在 $u, v$ 使 $uf + vg = 0$"翻译成齐次线性方程组，Sylvester 矩阵就是它的系数矩阵。
- **公因式与公共根**：在 $\mathbb{C}$ 上结式为零等价于有公共根；$f \mid vg$ 且 $\deg v < \deg f$ 是推出公因式的关键一步。
- **判别式等于结式加导数**：重根条件 $f(\alpha) = f'(\alpha) = 0$ 被 $\operatorname{Res}(f,f')$ 自动检测。
- **先化简再展开**：Sylvester 矩阵结构很强，用行变换制造零块，最后才用 Laplace 展开。
- **核对符号约定**：判别式的符号由归一化因子 $(-1)^{n(n-1)/2}$ 决定，二次、三次情形要与标准公式对照。

## 变式

- **变式 1**：一般三次多项式 $f = ax^3 + bx^2 + cx + d$ 作平移 $x = y - b/(3a)$ 化为 $a(y^3 + py + q)$，说明 $\Delta(f) = -a^4(4p^3 + 27q^2)$，并与展开式 $18abcd - 4b^3d + b^2c^2 - 4ac^3 - 27a^2d^2$ 对照。
- **变式 2**：证明 $\operatorname{Res}(f,gh) = \operatorname{Res}(f,g)\operatorname{Res}(f,h)$，并由此说明判别式在多项式乘法下的变换规律。
- **变式 3**：对 $f = x^4 + px^2 + q$ 写出 Sylvester 矩阵并计算判别式，讨论四次方程重根的判定。
- **变式 4**：计算 $\operatorname{Res}(x^2 - 1, x^3 - 1)$ 并解释结果；再证明 $\operatorname{rank} S(f,g) = n + m - \deg\gcd(f,g)$，说明秩的亏损量就是公共根的个数（计重数）。

## 链接

- 演示定理：[[ALG-THM-014]] Laplace 定理（按 $k$ 行展开）
- 前置：[[ALG-THM-006]] 重因式判定、[[ALG-DEF-012]] $k$ 阶子式、[[ALG-THM-005]] 根的个数不超过次数
- 相关例题：[[ALG-EX-002]] 用形式导数判定并去除重因式
- 相关定理：[[ALG-THM-009]] 有理根定理、[[ALG-THM-007]] 代数基本定理
