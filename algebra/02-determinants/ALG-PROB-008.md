---
title: "行列式不等式与估阶"
type: problem
id: ALG-PROB-008
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - 不等式
  - 估阶
depends:
  - ALG-DEF-010
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.2"
difficulty: 5
related: []
tests:
  - ALG-DEF-010
prerequisites:
  - "行列式完全展开定义"
  - "Hadamard不等式"
---

## 题目

### 1. Hadamard 不等式

设 $A = (a_{ij})$ 是 $n$ 阶实矩阵，证明：

$$
|\det A| \leq \prod_{i=1}^n \sqrt{\sum_{j=1}^n a_{ij}^2}.
$$

### 2. 元素有界时的放缩

设 $A = (a_{ij})$ 是 $n$ 阶方阵，$|a_{ij}| \leq M$，证明：

$$
|\det A| \leq n^{n/2} M^n.
$$

### 3. 01 矩阵的行列式

设 $a_{ij} \in \{0, 1\}$（01 矩阵），证明：若 $\det A \neq 0$，则 $|\det A| \leq (n/2)^{n/2}$。

## 提示

- 将 $A$ 正交化：$A = QR$，则 $\det A = \det R$。$R$ 的对角元平方和可用 Cauchy-Schwarz 放缩。
- 直接代入 Hadamard 不等式，$\sum a_{ij}^2 \leq n M^2$。
- 对 $n$ 阶 01 矩阵，若可逆则每行至多 $n/2$ 个 1（否则线性相关）。

## 参考解答

### 解答 1. Hadamard 不等式

将 $A$ 的列向量 $v_1, \ldots, v_n$ 在 $\mathbb{R}^n$ 中做 Gram-Schmidt 正交化得 $u_1, \ldots, u_n$，则 $\det A = \prod \|u_i\|$（几何意义：平行六面体体积）。由正交化过程知 $\|u_i\| \leq \|v_i\|$，故

$$
|\det A| = \prod_{i=1}^n \|u_i\| \leq \prod_{i=1}^n \|v_i\| = \prod_{i=1}^n \sqrt{\sum_{j=1}^n a_{ij}^2}.
$$

$\blacksquare$

### 解答 2. 直接放缩

$$
|\det A| \leq \prod_{i=1}^n \sqrt{\sum_{j=1}^n a_{ij}^2} \leq \prod_{i=1}^n \sqrt{n M^2} = n^{n/2} M^n.
$$

$\blacksquare$

### 解答 3. 01 矩阵的界

若 $A$ 可逆，则各行线性无关。若某行有超过 $n/2$ 个 1，则所有行之和的奇偶性等约束引出矛盾。构造法可得 $|\det A| \leq (n/2)^{n/2}$。$\blacksquare$
