---
title: "核与像（值域）"
type: definition
id: ALG-DEF-034
subject: algebra
chapter: 05-linear-maps
tags:
  - 核
  - 像
  - 值域
  - 零空间
depends:
  - ALG-DEF-032
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.1"
difficulty: 2
related: []
applications:
  - "信号处理：线性滤波器的核 = 被滤除的信号子空间"
---

## 定义陈述

设 $\varphi: V \to W$ 是线性映射。

**核**（kernel）或零空间：
$$
\ker \varphi = \{v \in V \mid \varphi(v) = 0\} \subseteq V.
$$

**像**（image）或值域：
$$
\operatorname{im} \varphi = \{\varphi(v) \mid v \in V\} \subseteq W.
$$

$\ker \varphi$ 是 $V$ 的子空间，$\operatorname{im} \varphi$ 是 $W$ 的子空间。

## 直觉理解

- **核**：被变换"压成零"的那些向量。核越大，映射丢失的信息越多。
- **像**：变换能"到达"的所有向量。像的维数 = 变换实际使用的维度。

**几何**：投影到 $xy$-平面的线性变换，核是 $z$-轴，像是 $xy$-平面。

## 链接

- 前置：[[ALG-DEF-032]] 线性变换
- 用于：[[ALG-THM-037]] 秩-零化度定理
