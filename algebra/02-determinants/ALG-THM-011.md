---
title: "按行（列）展开（Laplace 一行展开）"
type: theorem
id: ALG-THM-011
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - Laplace展开
depends:
  - ALG-DEF-011
  - ALG-DEF-010
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.3"
difficulty: 3
related: []
corollaries: []
applications:
  - "符号计算：递推行列式计算的降阶基础"
---

## 条件

设 $A = (a_{ij})$ 是 $n$ 阶方阵，$A_{ij}$ 是 $a_{ij}$ 的代数余子式（[[ALG-DEF-011]]）。

## 结论

> $\det A$ 可按第 $i$ 行展开：
> $$
> \det A = \sum_{j=1}^{n} a_{ij} A_{ij}, \qquad \text{对固定 } i.
> $$
>
> 也可按第 $j$ 列展开：
> $$
> \det A = \sum_{i=1}^{n} a_{ij} A_{ij}, \qquad \text{对固定 } j.
> $$

此外，**异行（列）展开为零**：
$$
\sum_{j=1}^{n} a_{ij} A_{kj} = 0 \quad (i \neq k), \qquad
\sum_{i=1}^{n} a_{ij} A_{ik} = 0 \quad (j \neq k).
$$

## 直觉理解

将 $n$ 阶行列式"按一行拆开"：第 $i$ 行的每个元素 $a_{ij}$ 乘上它的代数余子式 $A_{ij}$，再加起来。

**异行展开为零**是因为它相当于计算"将第 $k$ 行替换为第 $i$ 行后的行列式"——两行相同，行列式为 0。

## 证明

按第 $i$ 行分离完全展开式：展开式中含 $a_{ij}$ 的项恰为 $a_{ij} A_{ij}$（因为 $A_{ij}$ 包含了 $(-1)^{i+j}$ 和 $(n-1)$ 阶余子式所有排列项）。求和即得。$\blacksquare$

## 常见错误

- ✗ 忘记代数余子式的符号 $(-1)^{i+j}$，直接使用余子式 $M_{ij}$ 展开——漏了符号。
- ✗ 异行展开时仍期望得到 $\det A$——应为 0，这是 Cramer 法则证明的关键。

## 链接

- 前置：[[ALG-DEF-011]] 余子式
- 用于：[[ALG-THM-016]] Cramer 法则、[[ALG-DEF-015]] 伴随矩阵
- 推广：[[ALG-THM-014]] Laplace 定理（$k$ 行展开）
