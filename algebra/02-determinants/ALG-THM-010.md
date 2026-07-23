---
title: "行列式基本性质（多线性、反对称、行列对称）"
type: theorem
id: ALG-THM-010
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - 基本性质
  - 多线性
  - 反对称
depends:
  - ALG-DEF-010
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.1–2.2"
difficulty: 3
related:
  - ALG-DEF-013
corollaries: []
applications:
  - "数值分析：LU 分解中行列式可用三角阵对角线乘积计算"
---

## 条件

设 $A$ 是 $n$ 阶方阵，$\det A$ 为其行列式。

## 结论

### 核心性质

1. **转置不变性**：$\det(A^\top) = \det(A)$。
2. **多线性**：行列式对每一行（列）是线性的。若第 $i$ 行 $r_i = u + v$，则
   $$
   \det\begin{pmatrix}\vdots\\ u+v\\ \vdots\end{pmatrix} = \det\begin{pmatrix}\vdots\\ u\\ \vdots\end{pmatrix} + \det\begin{pmatrix}\vdots\\ v\\ \vdots\end{pmatrix}.
   $$
   且 $\det\begin{pmatrix}\vdots\\ cu\\ \vdots\end{pmatrix} = c \cdot \det\begin{pmatrix}\vdots\\ u\\ \vdots\end{pmatrix}$。
3. **反对称性**：交换两行（列），行列式变号。
4. **两行相同 ⇒ 行列式为 0**。
5. **某行乘以常数加到另一行，行列式不变**。
6. **某行全为 0 ⇒ 行列式为 0**。
7. **三角矩阵的行列式等于对角元乘积**：若 $A$ 是上三角或下三角，则 $\det A = a_{11} a_{22} \cdots a_{nn}$。

## 证明（概要）

**性质 1**：由完全展开定义，$\det(A^\top)$ 的求和项与 $\det(A)$ ——对应（$\pi \mapsto \pi^{-1}$），符号相同。

**性质 2**：展开式中每项恰含一个第 $i$ 行元素，故该行线性叠加时整个和式也线性叠加。

**性质 3**：交换两行使列标排列的逆序数变化 $\pm 1$，$\operatorname{sgn}$ 变号。

**性质 4**：由性质 3：交换相同两行得 $\det = -\det$，故 $\det = 0$。

**性质 5**：将新行拆为原行 + 倍加行，由多线性和两行相同推得。

**性质 6**：由多线性提公因子 $0$ 即得。

**性质 7**：上三角阵的展开式中，只有恒等排列 $\pi(i)=i$ 的项非零（其他项必含下三角区域的零元素），故 $\det = a_{11} \cdots a_{nn}$。$\blacksquare$

## 常见错误

- ✗ 认为"某行乘以常数加到另一行"会改变行列式。实际上行列式**不变**——这是初等变换中唯一不改变行列式的操作。
- ✗ 混淆"提公因子"和"行列式乘法"：$k$ 乘一行提 $k$，$k$ 乘整个矩阵提 $k^n$（因为每行都乘了 $k$）。
- ✗ 误认为行列式对矩阵乘法是线性的：$\det(A+B) \neq \det A + \det B$。

## 推论与应用

- 这些性质是**计算行列式的实用工具**：先用行变换化为上三角，再将对角元相乘。
- 性质 5（初等变换不变量）是 Gauss 消元法求行列式的理论基础。
- 性质 7 将三角矩阵的行列式计算降为 $O(n)$。

## 链接

- 前置：[[ALG-DEF-010]] $n$ 阶行列式
- 用于：[[ALG-THM-012]] 初等变换对行列式的影响
- 关联：[[ALG-DEF-013]] 转置行列式
