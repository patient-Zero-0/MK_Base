---
title: "线性空间的同构"
type: definition
id: ALG-DEF-030
subject: algebra
chapter: 04-linear-spaces
tags:
  - 同构
  - 线性空间
depends:
  - ALG-DEF-023
uses: []
status: draft
source: "丘维声《高等代数》第3版 §4.6"
difficulty: 3
related: []
applications:
  - "机器学习：核方法将数据映射到高维空间同构于特征空间"
---

## 定义陈述

设 $V, W$ 是域 $F$ 上的线性空间。称 $V$ 与 $W$ **同构**（isomorphic），若存在**线性同构映射** $\varphi: V \to W$——即满足：

1. **线性性**：$\varphi(u+v) = \varphi(u) + \varphi(v)$，$\varphi(au) = a\varphi(u)$；
2. **双射**：$\varphi$ 是单射且满射。

记作 $V \cong W$。

## 直觉理解

同构 = 两个线性空间"结构完全相同"——只是元素的标签不同。本质上它们具有相同的线性结构，一切线性性质（维数、线性相关性、子空间结构）都一样。

**例子**：$\mathbb{R}^2$ 与复平面 $\mathbb{C}$（作为 $\mathbb{R}$-线性空间）同构——$(a,b) \leftrightarrow a+bi$。

## 链接

- 前置：[[ALG-DEF-023]] 线性空间
- 用于：[[ALG-THM-033]] 同构 ⇔ 维数相等
