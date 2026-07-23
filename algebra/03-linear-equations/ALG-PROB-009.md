---
title: "秩与线性相关性综合"
type: problem
id: ALG-PROB-009
subject: algebra
chapter: 03-linear-equations
tags:
  - 秩
  - 线性相关
  - 向量组
depends:
  - ALG-DEF-019
  - ALG-THM-022
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.3"
difficulty: 3
related: []
tests:
  - ALG-THM-022
prerequisites:
  - "行秩 = 列秩"
  - "线性相关性判定"
---

## 题目

设 $\alpha_1, \alpha_2, \alpha_3$ 线性无关。证明 $\alpha_1 + \alpha_2, \alpha_2 + \alpha_3, \alpha_3 + \alpha_1$ 也线性无关。若将条件改为 $\alpha_1, \alpha_2, \alpha_3$ 线性相关，结论是否成立？举例说明。

## 提示

设 $k_1(\alpha_1+\alpha_2) + k_2(\alpha_2+\alpha_3) + k_3(\alpha_3+\alpha_1)=0$，整理成 $\alpha_1,\alpha_2,\alpha_3$ 的线性组合，利用无关性证明系数全为零。
