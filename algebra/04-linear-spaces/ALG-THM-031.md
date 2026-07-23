---
title: "直和的等价判定"
type: theorem
id: ALG-THM-031
subject: algebra
chapter: 04-linear-spaces
tags:
  - 直和
  - 子空间
  - 判定
depends:
  - ALG-DEF-029
  - ALG-THM-030
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.5"
difficulty: 3
related: []
corollaries: []
applications: []
---

## 条件

设 $U, W$ 是 $V$ 的子空间。

## 结论

以下命题等价：

1. $U + W$ 是直和（$U \cap W = \{0\}$）；
2. $\dim(U + W) = \dim U + \dim W$；
3. $U + W$ 中每个向量表示法唯一。

对多个子空间：$W_1 + \cdots + W_k$ 是直和 $\iff$ $W_i \cap \sum_{j \neq i} W_j = \{0\}$ 对所有 $i$。

## 直觉理解

直和 = 没有冗余 = 维数直接相加 = 分解唯一。

**类比**：坐标系分解——$\mathbb{R}^3 = \mathbb{R}e_1 \oplus \mathbb{R}e_2 \oplus \mathbb{R}e_3$，每个向量分解成三个坐标分量唯一。

## 链接

- 前置：[[ALG-DEF-029]] 直和、[[ALG-THM-030]] 维数公式
