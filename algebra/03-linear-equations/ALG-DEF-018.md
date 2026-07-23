---
title: "向量组的线性相关与线性无关"
type: definition
id: ALG-DEF-018
subject: algebra
chapter: 03-linear-equations
tags:
  - 向量组
  - 线性相关
  - 线性无关
depends: []
uses: []
status: draft
source: "丘维声《高等代数》第3版 §3.3"
difficulty: 2
related: []
applications:
  - "信号处理：正交基的无关性保证了傅里叶系数的唯一性"
---

## 定义陈述

设 $V$ 是向量空间（或 $\mathbb{R}^n$），$\alpha_1, \ldots, \alpha_s \in V$。

称 $\alpha_1, \ldots, \alpha_s$ **线性相关**，若存在不全为零的 $k_1, \ldots, k_s \in F$ 使得

$$
k_1 \alpha_1 + \cdots + k_s \alpha_s = 0.
$$

否则称它们**线性无关**——即只有 $k_1 = \cdots = k_s = 0$ 时上述等式才成立。

## 直觉理解

- **相关** = 至少有一个向量是其它向量的线性组合，存在冗余。
- **无关** = 每个向量都提供了"新方向"，谁也替代不了谁。
- 单个向量 $\alpha$ 无关 $\iff \alpha \neq 0$。
- 两个向量相关 $\iff$ 它们成比例。
- 包含零向量的向量组一定相关。

## 常见错误

- ✗ 认为相关就是某个向量被"等于"其他向量的组合——并不要求系数全部非零，只要"存在一组不全为零的系数"即可。

## 链接

- 用于：[[ALG-DEF-019]] 向量组的秩、[[ALG-THM-020]] 线性相关性判定
