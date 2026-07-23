---
title: "秩-零化度定理"
type: theorem
id: ALG-THM-037
subject: algebra
chapter: 05-linear-maps
tags:
  - 秩
  - 零化度
  - 维数
depends:
  - ALG-DEF-034
  - ALG-THM-028
uses: []
status: draft
source: "丘维声《高等代数》第3版 §5.1"
difficulty: 3
related: []
corollaries: []
applications:
  - "微分方程：齐次线性 ODE 解空间维数 = 阶数 - 线性无关特解的个数"
---

## 条件

设 $\varphi: V \to W$ 是线性映射，$V$ 是有限维线性空间。

## 结论

> $$
> \dim V = \dim \ker \varphi + \dim \operatorname{im} \varphi.
> $$
>
> 其中 $\dim \operatorname{im} \varphi = \operatorname{rank}(\varphi)$，$\dim \ker \varphi$ 称为**零化度**（nullity）。

## 直觉理解

变换的"维度守恒"：输入空间的维度 = 被压缩掉的维度（核）+ 保留的维度（像）。核越大，像越小，两者互补。

**对比**：这与矩阵的"秩-零化度"形式一致——矩阵的列数 = 零化度 + 秩。

## 证明

取 $\ker \varphi$ 的一组基 $u_1, \ldots, u_r$，扩充为 $V$ 的基 $u_1, \ldots, u_r, v_{r+1}, \ldots, v_n$。则 $\varphi(v_{r+1}), \ldots, \varphi(v_n)$ 是 $\operatorname{im} \varphi$ 的基。由此 $\dim \operatorname{im} \varphi = n - r$。$\blacksquare$

## 链接

- 前置：[[ALG-DEF-034]] 核与像、[[ALG-THM-028]] 基
- 用于：[[ALG-THM-039]] 特征向量无关性
