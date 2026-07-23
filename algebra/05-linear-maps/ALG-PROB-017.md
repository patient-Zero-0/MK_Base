---
title: "核、像与秩-零化度综合"
type: problem
id: ALG-PROB-017
subject: algebra
chapter: 05-linear-maps
tags:
  - 核
  - 像
  - 秩-零化度
depends:
  - ALG-THM-037
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.1"
difficulty: 3
related: []
tests:
  - ALG-THM-037
prerequisites:
  - "秩-零化度定理"
---

## 题目

设 $\varphi: V \to V$ 是线性变换，$V$ 是 $n$ 维线性空间。证明：

1. $\ker \varphi \subseteq \ker \varphi^2 \subseteq \cdots$，且若 $\ker \varphi^k = \ker \varphi^{k+1}$，则对所有 $m \geq k$，$\ker \varphi^m = \ker \varphi^k$。
2. 若 $\operatorname{im} \varphi = \operatorname{im} \varphi^2$，则 $\varphi$ 可逆。
