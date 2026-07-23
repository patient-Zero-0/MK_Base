---
title: "子空间与张成证明"
type: problem
id: ALG-PROB-013
subject: algebra
chapter: 04-linear-spaces
tags:
  - 子空间
  - 张成
depends:
  - ALG-DEF-024
  - ALG-DEF-025
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.2"
difficulty: 3
related: []
tests:
  - ALG-DEF-025
prerequisites:
  - "子空间判别法"
  - "张成空间"
---

## 题目

设 $S, T$ 是 $V$ 的子集。证明：

1. $\operatorname{span}(S)$ 是包含 $S$ 的最小子空间。
2. $S \subseteq T \implies \operatorname{span}(S) \subseteq \operatorname{span}(T)$。
3. $\operatorname{span}(S \cap T) \subseteq \operatorname{span}(S) \cap \operatorname{span}(T)$。等号是否总成立？若否，举反例。
