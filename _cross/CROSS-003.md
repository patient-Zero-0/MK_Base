---
title: "柯西-施瓦茨不等式的三种面孔"
type: definition
id: CROSS-003
subject: cross
chapter: _cross
tags:
  - 跨课
  - 柯西-施瓦茨
  - 内积
  - 积分不等式
depends:
  - ANL-PROB-017
  - ALG-THM-044
  - ALG-DEF-023
uses: []
status: stable
source: "综合：华东师范大学《数学分析》第5版 §9.4 + 丘维声《高等代数》第3版 §4.1、§5.4"
difficulty: 3
related:
  - CROSS-005
  - ALG-EX-024
---

## 关联说明

Cauchy–Schwarz 不等式在数学分析里以"积分不等式"出现，在高等代数里以"内积不等式"出现，在概率论里以"期望不等式"出现。三者不是三个定理，而是同一个代数事实在三套语言下的翻译。

| 场景 | 空间与内积 | 不等式形态 | 取等条件 |
|---|---|---|---|
| 有限维向量 | $\mathbb{R}^n$，标准内积 $\sum a_ib_i$ | $(\sum a_ib_i)^2\le(\sum a_i^2)(\sum b_i^2)$ | 两向量成比例 |
| 抽象内积空间 | 任意实内积空间，内积记作 $(u,v)$ | $(u,v)^2\le(u,u)(v,v)$ | $u,v$ 线性相关 |
| 积分 | $C[a,b]$，内积 $\int_a^b fg$ | $(\int_a^b fg)^2\le\int_a^b f^2\int_a^b g^2$ | 连续情形下 $f,g$ 成比例 |
| 概率 | 二阶矩有限的随机变量，内积 $E[XY]$ | $(E[XY])^2\le E[X^2]E[Y^2]$ | 几乎必然成比例 |

统一的证明骨架是判别式法。在任意实内积空间中，对每个实数 $\lambda$ 有
$$
0\le(u+\lambda v,u+\lambda v)=(u,u)+2\lambda(u,v)+\lambda^2(v,v).
$$
若 $v=0$ 则不等式两边都是 $0$；若 $v\ne0$，上式右端是关于 $\lambda$ 的开口向上的二次三项式且恒非负，故判别式不超过 $0$：
$$
4(u,v)^2-4(u,u)(v,v)\le0,
$$
即 $(u,v)^2\le(u,u)(v,v)$，开方得 $\lvert(u,v)\rvert\le\lVert u\rVert\,\lVert v\rVert$。证明只用到内积的正定性、对称性与双线性，因此对 $\mathbb{R}^n$、积分空间、概率空间同时生效。内积是加在[[ALG-DEF-023]] 所述线性空间结构之上的一个二元函数。

## 直觉理解

内积度量"两个对象的对齐程度"：把 $\langle u,v\rangle$ 看成 $u$ 在 $v$ 方向上的投影长度乘以 $\lVert v\rVert$，则不等式说"投影长度不超过 $\lVert u\rVert$"，即
$$
\frac{\lvert(u,v)\rvert}{\lVert u\rVert\,\lVert v\rVert}\le1 .
$$
这正是相关系数与夹角余弦的取值范围限制；在高维和函数空间中，"夹角"依然由这个比值定义，所以不等式是"$\lvert\cos\theta\rvert\le1$"的一般化。

判别式法的直觉是：若不等式反向，即 $(u,v)^2>(u,u)(v,v)$，那么二次三项式 $q(\lambda)=\lVert u+\lambda v\rVert^2$ 会取到负值（因为开口向上且有两个不同实根，两根之间为负）。但 $q(\lambda)$ 是向量范数的平方，是"平方和"，不可能为负。所以反证法只需一句话：平方和非负，判别式非正。

三种面孔的差别只在"和"的具体含义：有限维是有限和，积分是连续和，期望是概率加权和。它们都满足正定性（期望情形要求忽略几乎必然相等的差别）。

## 一个具体例子

离散情形取 $u=(3,4)$、$v=(4,3)$：$\langle u,v\rangle=24$，$\lVert u\rVert^2=\lVert v\rVert^2=25$，于是
$$
24^2=576\le25\cdot25=625,
$$
严格成立；再取 $v=2u=(6,8)$，则左边为 $50^2=2500$，右边为 $25\cdot100=2500$，取等，验证了"成比例才取等"。

积分情形在 $[0,1]$ 上取 $f(x)=x$、$g(x)=1$：
$$
\left(\int_0^1x\,dx\right)^2=\frac14,\qquad
\int_0^1x^2\,dx\cdot\int_0^11\,dx=\frac13\cdot1=\frac13,
$$
故 $\frac14\le\frac13$。此处"夹角余弦"为
$$
\frac{(f,g)}{\lVert f\rVert\,\lVert g\rVert}=\frac{1/2}{\sqrt{1/3}}=\frac{\sqrt3}{2}=\cos\frac{\pi}{6},
$$
即 $f$ 与 $g$ 在函数空间中的夹角为 $30^\circ$。若改成 $f(x)=2x$、$g(x)=x$，则 $(f,g)=2/3$、$\lVert f\rVert^2=4/3$、$\lVert g\rVert^2=1/3$，两边都等于 $4/9$，取等。

概率形式同理：设同一试验的两个随机变量 $X,Y$ 以概率 $1/2$ 分别取 $(1,3)$ 与 $(2,1)$，则
$$
E[XY]=\frac{1\cdot3+2\cdot1}{2}=\frac52,\qquad
E[X^2]=\frac{1+4}{2}=\frac52,\qquad
E[Y^2]=\frac{9+1}{2}=5,
$$
故 $(E[XY])^2=\frac{25}{4}\le\frac{25}{2}=E[X^2]E[Y^2]$。这只是同一个判别式论证在两点分布上的展开，三种面孔的取等条件也完全一致。

## 常见误区

- ✗ **把平方放错位置，写成 $(\int fg)^2\le\int f^2g^2$。** 反例：在 $[0,2]$ 上取 $f=g=1$，左边为 $(\int_0^2 1\,dx)^2=4$，右边为 $\int_0^2 1\,dx=2$，不等式反向。正确做法是把 Cauchy–Schwarz 用在 $fg$ 与常函数 $1$ 上，得到 $(\int fg)^2\le(b-a)\int f^2g^2$，多出的因子 $b-a$ 不能丢。
- ✗ **认为 $f,g$ 都非负（或同号）时积分形式取等。** 反例：在 $[0,1]$ 上取 $f(x)=x$、$g(x)=1-x$，两者都非负，但 $(f,g)=1/6$，故左边为 $1/36$，而 $\lVert f\rVert^2\lVert g\rVert^2=(1/3)(1/3)=1/9$，严格不等。取等要求 $f,g$ 成比例，而不仅仅是同号。

## 链接

- 积分版的不等式链：[[ANL-PROB-017]] 积分不等式（Cauchy–Schwarz、Hölder、Minkowski）
- 内积空间的结构定理：[[ALG-THM-044]] 实对称矩阵正交对角化、[[ALG-DEF-023]] 线性空间公理
- 级数版与函数空间版：[[CROSS-005]] 傅里叶级数与正交基（Bessel 不等式即此不等式的级数形式）
- 相关例题：[[ALG-EX-024]] 迹、特征值与牛顿恒等式（特征值幂和与内积计算相通）
