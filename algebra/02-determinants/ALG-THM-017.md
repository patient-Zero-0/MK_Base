---
title: "矩阵可逆的充要条件（行列式刻画）"
type: theorem
id: ALG-THM-017
subject: algebra
chapter: 02-determinants
tags:
  - 矩阵
  - 可逆
  - 行列式
depends:
  - ALG-DEF-015
  - ALG-THM-015
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.4"
difficulty: 2
related: []
corollaries: []
applications:
  - "可逆性的标准判别准则——计算行列式即可"
---

## 条件

设 $A$ 是 $n$ 阶方阵。

## 结论

以下命题等价：

1. $A$ 可逆；
2. $\\det A \\neq 0$；
3. $A$ 的行（列）向量组线性无关；
4. $A$ 的秩 $\\operatorname{rank}(A) = n$；
5. $Ax = 0$ 只有零解；
6. 对任意 $b$，$Ax = b$ 有唯一解。

且当 $\\det A \\neq 0$ 时，

$$
A^{-1} = \\frac{1}{\\det A} A^*.
$$

## 证明

(1) $\\Rightarrow$ (2)：$A$ 可逆 $\\Rightarrow \\exists A^{-1}$ 使 $AA^{-1} = I$, 取行列式得 $\\det A \\cdot \\det(A^{-1}) = 1 \\Rightarrow \\det A \\neq 0$。

(2) $\\Rightarrow$ (1)：若 $\\det A \\neq 0$，由伴随矩阵性质 $A\\cdot A^* = (\\det A)I$ 得 $A^{-1} = A^*/\\det A$。$\\blacksquare$

## 常见错误

- ✗ 混淆行列式与秩的关系——满秩等价于行列式非零，但只有方阵才适用。
- ✗ 认为 $\\det A = 0$ 时 $A$ 一定是零矩阵——事实上 $\\det A = 0$ 只是说明 $A$ 是奇异矩阵，可以非零。
