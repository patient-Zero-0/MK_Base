---
title: "求向量组的秩与极大无关组"
type: example
id: ALG-EX-009
subject: algebra
chapter: 03-linear-equations
tags:
  - 向量组
  - 秩
  - 极大无关组
depends:
  - ALG-DEF-019
  - ALG-DEF-020
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.3"
difficulty: 3
illustrates:
  - ALG-DEF-019
related: []
---

## 题目

求向量组 $\alpha_1 = (1, 2, 1, 0)$，$\alpha_2 = (2, 1, 0, 1)$，$\alpha_3 = (1, -1, -1, 2)$，$\alpha_4 = (3, 0, -1, 3)$ 的秩和一个极大线性无关组。

## 解答

**解：** 以 $\alpha_i$ 为行构成矩阵，化为行阶梯形（也可用列向量做，等价）：

$$
A = \begin{pmatrix}
1 & 2 & 1 & 0 \\
2 & 1 & 0 & 1 \\
1 & -1 & -1 & 2 \\
3 & 0 & -1 & 3
\end{pmatrix}
\rightarrow \begin{pmatrix}
1 & 2 & 1 & 0 \\
0 & -3 & -2 & 1 \\
0 & -3 & -2 & 2 \\
0 & -6 & -4 & 3
\end{pmatrix}
$$

$$
\rightarrow \begin{pmatrix}
1 & 2 & 1 & 0 \\
0 & -3 & -2 & 1 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0
\end{pmatrix}.
$$

非零行数为 $3$，故 $\operatorname{rank}(\alpha_1, \alpha_2, \alpha_3, \alpha_4) = 3$。

一个极大无关组：$\alpha_1, \alpha_2, \alpha_3$（对应阶梯形前三个主元行）。

验证：$\alpha_4 = \alpha_1 + \alpha_2 - \alpha_3$（可由前三者线性表示）。

$\blacksquare$
