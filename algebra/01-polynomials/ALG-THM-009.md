---
title: "有理根定理 + Eisenstein 判别法 + Gauss 引理"
type: theorem
id: ALG-THM-009
subject: algebra
chapter: 01-polynomials
tags:
  - 多项式
  - 有理根
  - Eisenstein
  - Gauss引理
  - 不可约性
depends:
  - ALG-DEF-007
  - ALG-DEF-006
uses: []
status: draft
source: "丘维声《高等代数》第3版 §1.5"
difficulty: 4
related:
  - ALG-THM-002
  - ALG-THM-007
corollaries: []
applications:
  - "符号计算：CAS 系统的有理根搜索与不可约性判定"
  - "编码理论：分圆多项式的不可约性（$\\\\Phi_n(x)$ 的不可约性决定 CRC/RS 码的代数性质）"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设 $f(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_0 \in \mathbb{Z}[x]$ 是整系数多项式，$a_n \neq 0$。

## 结论

### 有理根定理（Rational Root Theorem）

若 $p/q \in \mathbb{Q}$（$p, q$ 互素，$q > 0$）是 $f$ 的根，则 $p \mid a_0$ 且 $q \mid a_n$。

特别地：

- 若 $f$ 是**首一**多项式（$a_n = 1$），则任意有理根都是整数，且整除常数项 $a_0$。
- 有理根的候选集为 $\{\pm p/q : p \mid a_0,\; q \mid a_n\}$（有限集，可逐一验证）。

### Gauss 引理（Gauss's Lemma）

> **本原多项式的乘积仍是本原多项式**。

等价表述：若 $f, g \in \mathbb{Z}[x]$ 都是本原多项式（[[ALG-DEF-007]]），则 $fg$ 也是本原的。

#### 推论（$\mathbb{Z}[x]$ 上的唯一分解）

> 若 $f \in \mathbb{Z}[x]$ 在 $\mathbb{Z}[x]$ 中可约（可分解为两个非常数整系数多项式之积），则在 $\mathbb{Q}[x]$ 中也可约。反之，若 $f$ 在 $\mathbb{Q}[x]$ 中可约且 $f$ 本原，则在 $\mathbb{Z}[x]$ 中也可约。

因此，$\mathbb{Q}[x]$ 上的因式分解问题可以安全地"去分母"后在 $\mathbb{Z}[x]$ 中操作。

### Eisenstein 判别法（Eisenstein's Criterion）

设 $f(x) = a_n x^n + \cdots + a_0 \in \mathbb{Z}[x]$。若存在素数 $p$ 满足：

1. $p \nmid a_n$（最高次项不被 $p$ 整除）；
2. $p \mid a_{n-1}, a_{n-2}, \ldots, a_0$（其余所有系数都被 $p$ 整除）；
3. $p^2 \nmid a_0$（常数项不被 $p^2$ 整除）。

则 $f$ 在 $\mathbb{Q}[x]$ 中**不可约**。

## 几何/直觉理解

**有理根定理**将"找有理根"从无限搜索变成有限枚举：一个整系数多项式的有理根只能是 $\pm$ (常数项的因子)/(首项系数的因子)。

> 例如 $f(x) = 2x^3 - x^2 - 4x + 2$，有理根只可能是 $\pm 1, \pm 2, \pm 1/2$——共 6 个候选，逐一验证即可。这比漫无目的地试要高效得多。

**Gauss 引理**在直觉上很自然：如果两个整系数多项式各自系数互素，它们的乘积系数也不会有公共因子。但证明并非平凡——需要通过容度的性质严谨论证。

**Eisenstein 判别法**是一个**充分但非必要**的条件：找到一个素数 $p$ 满足那些整除条件，就能立刻判定多项式不可约。它虽不总能适用，但一旦适用就极为强大。很多经典不可约多项式都可用它判定：

- $x^n - 2$（取 $p = 2$）在 $\mathbb{Q}[x]$ 不可约；
- $x^{p-1} + x^{p-2} + \cdots + 1$（分圆多项式，取 $p$ 本身经变换后用 Eisenstein）。

## 证明

### 有理根定理

设 $p/q$ 是 $f$ 的根，$p, q$ 互素。则 $f(p/q) = 0$，代入得

$$
a_n \left(\frac{p}{q}\right)^{\!n} + a_{n-1} \left(\frac{p}{q}\right)^{\!n-1} + \cdots + a_1 \left(\frac{p}{q}\right) + a_0 = 0.
$$

两边乘以 $q^n$：

$$
a_n p^n + a_{n-1} p^{n-1} q + \cdots + a_1 p q^{n-1} + a_0 q^n = 0.
$$

整理：
$$
a_n p^n = -q (a_{n-1} p^{n-1} + \cdots + a_0 q^{n-1}) \implies q \mid a_n p^n.
$$

由于 $\gcd(p, q)=1$，$q$ 与 $p$ 无公共因子，故 $q \mid a_n$。同理移项得 $p \mid a_0$。$\blacksquare$

### Gauss 引理

设 $f, g \in \mathbb{Z}[x]$ 本原。反设 $h = fg$ 非本原，则存在素数 $p$ 整除 $h$ 的所有系数。

将 $f, g$ 的系数模 $p$ 得 $\bar f, \bar g \in \mathbb{F}_p[x]$。因 $f$ 本原，$\bar f \neq 0$（至少有一个系数不被 $p$ 整除）；同理 $\bar g \neq 0$。而 $h$ 的系数全部被 $p$ 整除，故 $\bar h = \bar f \bar g = 0 \in \mathbb{F}_p[x]$。

由于 $\mathbb{F}_p$ 是域，$\mathbb{F}_p[x]$ 是整环（无零因子），$\bar f \bar g = 0$ 推出 $\bar f = 0$ 或 $\bar g = 0$，矛盾。故 $h$ 本原。$\blacksquare$

### Eisenstein 判别法

设 $f$ 满足 Eisenstein 条件（素数 $p$）。假设 $f$ 在 $\mathbb{Q}[x]$ 中可约，由 Gauss 引理推论，$f$ 在 $\mathbb{Z}[x]$ 中可约：$f = g h$，其中

$$
g(x) = b_r x^r + \cdots + b_0, \quad h(x) = c_s x^s + \cdots + c_0, \quad r, s \geq 1,\; r + s = n.
$$

比较常数项：$a_0 = b_0 c_0$。由条件 $p \mid a_0$ 且 $p^2 \nmid a_0$，故 $p$ **恰好整除** $b_0$ 和 $c_0$ 中的**一个**。不妨设 $p \mid b_0$，$p \nmid c_0$。

比较 $x^n$ 项：$a_n = b_r c_s$，由条件 $p \nmid a_n$，故 $p \nmid b_r$ 且 $p \nmid c_s$。

设 $t$ 是 $g$ 中**最小下标使得 $p \nmid b_t$**。由 $p \mid b_0$ 知 $t \geq 1$。比较 $x^t$ 项系数：

$$
a_t = b_0 c_t + b_1 c_{t-1} + \cdots + b_{t-1} c_1 + b_t c_0.
$$

前面 $t$ 项都含 $p$ 的因子（因为 $b_0, \ldots, b_{t-1}$ 都被 $p$ 整除），最后一项 $b_t c_0$ 不被 $p$ 整除（$p \nmid b_t, p \nmid c_0$），故 $a_t$ 不被 $p$ 整除。

但 $t < n$（因 $r \geq 1$，$t$ 在 $g$ 的下标范围内且 $t \leq r < n$），由条件知 $p \mid a_{n-1}, \ldots, a_0$，故 $p \mid a_t$，矛盾。$\blacksquare$

## 常见错误

- ✗ 把有理根定理当充分条件使用：候选有理根中没有一个为零，**不说明**多项式没有有理根以外的根——它当然可以有**无理根**（如 $\sqrt{2}$）或**复根**。
  反例：$x^2 - 2$ 的有理根候选为 $\pm 1, \pm 2$，全部不是根，但多项式有根 $\pm\sqrt{2} \notin \mathbb{Q}$。
- ✗ 误认为 Eisenstein 判别法是"不可约的充要条件"。它只是**充分条件**——很多不可约多项式不满足 Eisenstein 条件（如 $x^4 + 1$ 在 $\mathbb{Q}[x]$ 不可约，但 Eisenstein 无法直接应用，需要做代换 $x \mapsto x+1$ 后用 Eisenstein）。
- ✗ 忘记 Gauss 引理的"$\mathbb{Q}[x]$ 可约 ⇔ $\mathbb{Z}[x]$ 可约"需要 $f$ 本原。若非本原，先提取容度（[[ALG-DEF-007]]）再应用。
  反例：$f = 2x + 2 = 2(x+1)$ 在 $\mathbb{Q}[x]$ 中不可约，但若直接在 $\mathbb{Z}[x]$ 中看似乎可约——实际上提取容度 2 后得到本原部分 $x+1$，它在 $\mathbb{Z}[x]$ 中不可约。
- ✗ 把 Eisenstein 的 $p$ 和多项式中的常数 $p$ 混淆。$p$ 是一个素数，不是多项式的参数。

## 推论

1. **Eisenstein 多项式的不可约性**：对任意素数 $p$，$x^n - p$ 在 $\mathbb{Q}[x]$ 不可约。更一般地，$x^n - a$ 在 $a$ 有素因子 $p$ 满足 $p \mid a$ 且 $p^2 \nmid a$ 时不可约。
2. **分圆多项式**：$\Phi_p(x) = x^{p-1} + x^{p-2} + \cdots + 1$ 在 $\mathbb{Q}[x]$ 不可约（变换 $x \mapsto x+1$ 后用 Eisenstein）。
3. **有理根的有限枚举**：有理根定理将找根问题从无限降到有限步验证。

## 链接

- 前置：[[ALG-DEF-007]] 本原多项式与容度、[[ALG-DEF-006]] 多项式函数与根
- 关联：[[ALG-THM-002]] 唯一分解定理（Gauss 引理是 $\mathbb{Z}[x]$ 唯一分解的关键）
- 后续：Eisenstein 判别法用于构造有限域 $\mathbb{F}_{p^n}$ 的不可约多项式

## 跨专业应用

- **符号计算**：CAS 系统的 `RationalRoots` 和 `Factor` 函数核心算法完全基于有理根定理和 Eisenstein 判别的组合搜索
- **编码理论**：分圆多项式 $\Phi_n(x)$ 的不可约性是 Reed–Solomon 码和 BCH 码的代数基础——循环码的生成多项式往往是分圆多项式或其因式
- **密码学**：有限域 $\mathbb{F}_{p^n}$ 的构造需要 $\mathbb{F}_p[x]$ 上的 $n$ 次不可约多项式——Eisenstein 判别法是寻找这类多项式的最直接工具
