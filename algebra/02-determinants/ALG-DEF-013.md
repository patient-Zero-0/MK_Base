---
title: "转置行列式"
type: definition
id: ALG-DEF-013
subject: algebra
chapter: 02-determinants
tags:
  - 行列式
  - 转置
depends:
  - ALG-DEF-010
uses: []
status: draft
source: "丘维声《高等代数》第3版 §2.1"
difficulty: 1
related:
  - ALG-THM-010
applications: []
---

## 定义陈述

设 $A = (a_{ij})$ 是 $n$ 阶方阵。$A$ 的**转置** $A^\top = (a_{ji})$。$A^\top$ 的行列式称为 $A$ 的**转置行列式**，即

$$
\det(A^\top) = \sum_{\pi \in S_n} \operatorname{sgn}(\pi) \, a_{\pi(1),1} \, a_{\pi(2),2} \, \cdots \, a_{\pi(n),n}.
$$

## 直觉理解

行列式的定义中，行标固定为 $1,2,\ldots,n$，列标按排列变动。转置行列式交换了行和列的角色。**基本结论**（[[ALG-THM-010]] 性质 1）：$\det(A^\top) = \det(A)$——行和列在行列式中地位对称。

## 链接

- 前置：[[ALG-DEF-010]] $n$ 阶行列式
- 性质：[[ALG-THM-010]] 行列式基本性质（$\det A^\top = \det A$）
