---
title: "本原多项式与容度（Gauss 引理用）"
type: definition
id: ALG-DEF-007
subject: algebra
chapter: 01-polynomials
tags:
  - 多项式
  - 本原多项式
  - Gauss引理
  - 整系数
depends:
  - ALG-DEF-001
uses: []
status: draft
source: "丘维声《高等代数》第3版 §1.5"
difficulty: 3
related:
  - ALG-THM-002
applications:
  - "代数数论：Gauss 引理是 $\\mathbb{Q}[x]$ 上唯一分解定理证明的关键"
  - "符号计算：有理系数多项式的整系数化与因子提取"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述

### 容度

设 $f(x) = a_n x^n + \cdots + a_0 \in \mathbb{Z}[x]$ 是非零整系数多项式。$f$ 的**容度**（content）定义为各系数的最大公因数（取正数），记作

$$
\operatorname{cont}(f) := \gcd(a_n, a_{n-1}, \ldots, a_0) \in \mathbb{Z}_{>0}.
$$

### 本原多项式

称 $f(x) \in \mathbb{Z}[x]$ 是**本原多项式**（primitive polynomial），若

$$
\operatorname{cont}(f) = 1,
$$

即 $f$ 的系数**互素**（没有大于 1 的公因子）。

### 有理系数 → 整系数

对 $f(x) \in \mathbb{Q}[x]$，总存在正整数 $d$ 使 $d \cdot f(x) \in \mathbb{Z}[x]$；提取公因子后，可唯一写成

$$
f(x) = \frac{c}{d} \cdot \tilde f(x),
$$

其中 $\tilde f \in \mathbb{Z}[x]$ 是本原多项式，$c, d \in \mathbb{Z}$ 互素。这里的 $\frac{c}{d}$（规范化后）称为 $f$ 的**有理容度**。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 整系数多项式 $f \in \mathbb{Z}[x]$ | 系数为整数，不一定互素 |
| 本原多项式 | $\operatorname{cont}(f) = 1$，系数无 >1 公因子 |
| 有理系数多项式 $f \in \mathbb{Q}[x]$ | 可通分化为整系数，再提取容度得本原部分 |

**本原性与底域的关系**：

> 本原多项式是 $\mathbb{Z}[x]$ 的概念，不直接用于 $K[x]$（$K$ 是域）。引入它是因为 $\mathbb{Z}[x]$ 是**整系数环**（不是域上的多项式环），
> 而 Eisenstein 判别法（ALG-THM-009，待建）需要将 $\mathbb{Z}[x]$ 上的分解问题归约到 $\mathbb{Q}[x]$，
> 再借由本原性回到 $\mathbb{Z}[x]$。

## 直觉理解

**容度**就是把多项式系数的"公共整数因子"提取出来：

$$
6x^3 + 9x^2 - 3x + 12 = 3 \cdot (2x^3 + 3x^2 - x + 4),
$$

其中 $\operatorname{cont} = 3$，括号里是**本原多项式**。

**本原多项式** = "系数已经约到最简，没有公共整数因子可提"。

> Gauss 引理（唯一分解定理 ALG-THM-002 中作为工具使用）断言：
> **两个本原多项式的乘积仍是本原的**。
>
> 这看似简单，意义却深远：它使得 $\mathbb{Q}[x]$ 上的因式分解问题可以先"去掉分母"转为 $\mathbb{Z}[x]$，
> 在本原多项式层面完成分解，最后再恢复分母。有理根定理与 Eisenstein 判别法正是建立在这一洞见之上。

## 基本性质

1. 若 $f \in \mathbb{Z}[x]$，则 $f = \operatorname{cont}(f) \cdot \tilde f$，其中 $\tilde f$ 本原。
2. 本原多项式的乘积本原（**Gauss 引理**的核心结论）。
3. 若 $f \in \mathbb{Z}[x]$ 在 $\mathbb{Z}[x]$ 中可约（分解为两个非常数整系数多项式之积），则在 $\mathbb{Q}[x]$ 中也可约；反之，本原性保证了逆命题也成立（Gauss 引理的直接推论）。

## 链接

- 前置：[[ALG-DEF-001]] 一元多项式
- 核心工具：有理根定理 + Eisenstein 判别法（ALG-THM-009，待建）
- 关联：[[ALG-THM-002]] 唯一分解定理（Gauss 引理将 $\mathbb{Z}[x]$ 也纳入唯一分解整环）

## 跨专业应用

- **代数数论**：Dedekind 整环上元素的容度与本原分解是理想的局部-整体原理的雏形
- **符号计算**：有理系数多项式求 `primitive part` 是计算机代数系统（SymPy、Mathematica）提取因子、简化分式的标准步骤
