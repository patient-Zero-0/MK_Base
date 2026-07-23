---
title: "含参数线性方程组的解的讨论"
type: example
id: ALG-EX-011
subject: algebra
chapter: 03-linear-equations
tags:
  - 线性方程组
  - 含参数
  - 分类讨论
depends:
  - ALG-THM-027
  - ALG-THM-026
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.4"
difficulty: 4
illustrates:
  - ALG-THM-027
related: []
---

## 题目

$k$ 取何值时，方程组有唯一解、无穷多解或无解？

$$
\begin{cases}
x_1 + x_2 + kx_3 = 1, \\
x_1 + kx_2 + x_3 = 1, \\
kx_1 + x_2 + x_3 = 1.
\end{cases}
$$

## 解答

**解：** 系数矩阵 $A$ 和增广矩阵 $(A \mid b)$：

$$
A = \begin{pmatrix}
1 & 1 & k \\
1 & k & 1 \\
k & 1 & 1
\end{pmatrix},\quad
(A \mid b) = \left(\begin{array}{ccc|c}
1 & 1 & k & 1 \\
1 & k & 1 & 1 \\
k & 1 & 1 & 1
\end{array}\right).
$$

计算 $\det A = (k+2)(k-1)^2$。

- **$k \neq 1$ 且 $k \neq -2$**：$\det A \neq 0$，$\operatorname{rank}(A) = 3 = \operatorname{rank}(A \mid b)$，**唯一解**。
- **$k = 1$**：$A$ 各行全为 $(1,1,1)$，$\operatorname{rank}(A) = 1$，增广矩阵各行也全为 $(1,1,1 \mid 1)$，$\operatorname{rank}(A \mid b) = 1$，**无穷多解**（自由度 $2$）。
- **$k = -2$**：经初等变换得增广矩阵末行为 $(0,0,0 \mid 3)$，$\operatorname{rank}(A) = 2 < \operatorname{rank}(A \mid b) = 3$，**无解**。

$\blacksquare$
