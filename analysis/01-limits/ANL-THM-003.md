---
title: "数列极限的保号性"
type: theorem
id: ANL-THM-003
subject: analysis
chapter: 01-limits
tags:
  - 极限
  - 保号性
  - 基础定理
depends:
  - ANL-DEF-004
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §2.2"
difficulty: 2
related:
  - ANL-THM-004
  - ANL-THM-005
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件与结论

设 $\{a_n\}$ 收敛，$a_n \to L$（按 [[ANL-DEF-004]]）。则有：

**保号性（强形式）**：

- 若 $L > 0$，则 $\exists N, \forall n > N: a_n > L / 2 > 0$。
- 若 $L < 0$，则 $\exists N, \forall n > N: a_n < L / 2 < 0$。

**保号性（弱形式 / 反向）**：

- 若 $\exists N, \forall n > N: a_n \geq 0$，则 $L \geq 0$（注意只能得到弱不等号 $\geq$，不能得到 $> 0$）。
- 若 $\exists N, \forall n > N: a_n \leq c$，则 $L \leq c$。

## 直觉理解

如果数列收敛于一个**严格正**的极限，那么从某项起所有项也"分享"了正号——并且至少有 $L/2$ 这么多。
形象地：数列像稳定到达某层楼的电梯，停下时位于"楼上"（$L > 0$），那么足够后期它必定也"在楼上"。

**反向方向必须弱化**：所有项 $\geq 0$ 不蕴含极限 $> 0$。
反例：$a_n = 1/n > 0$ 但 $\lim a_n = 0$。
极限取**闭包**：项都在 $\geq 0$ 的"闭半轴"上 → 极限也在 $\geq 0$ 的"闭半轴"上，但**未必**还在严格的"开半轴" $> 0$ 上。

## 证明（强形式，正极限）

**证明：** 在 [[ANL-DEF-004]] 中取 $\varepsilon = L / 2 > 0$。
存在 $N$ 使 $\forall n > N: |a_n - L| < L / 2$，即
$$
L - L / 2 < a_n < L + L / 2 \implies a_n > L / 2 > 0.
$$
$\blacksquare$

弱形式的证明：反证。设 $a_n \geq 0$ 但 $L < 0$，则由强形式 $a_n < L / 2 < 0$ 对充分大 $n$ 成立，
矛盾于 $a_n \geq 0$。故 $L \geq 0$。$\blacksquare$

## 常见错误

- ✗ 由 $a_n > 0$ 推 $L > 0$。错。反例 $a_n = 1/n \to 0$。
  正确推论是 $L \geq 0$（弱不等号）。
- ✗ 把 "$a_n > b_n$" 错误地推出 "$L > L'$"。
  正确推论是 $L \geq L'$。即取极限**保留 $\leq, \geq$，不保留 $<, >$**。
- ✗ 在强形式中误把 $\varepsilon$ 取为 $L$ 而不是 $L / 2$。
  取 $\varepsilon = L$ 只能得 $a_n > 0$，无法得到 $a_n > L / 2$ 的均匀下界——
  需要 $L / 2$ 这一"留出余量"的技巧。

## 推论

- **比较定理**：若 $\exists N, \forall n > N: a_n \leq b_n$，且 $a_n \to L_1, b_n \to L_2$，则 $L_1 \leq L_2$。
- 用于 [[ANL-THM-005]] 夹逼定理的简化证明。
- 在不等式收敛性问题中作为基本工具。

## 链接

- 前置：[[ANL-DEF-004]]
- 相关：[[ANL-THM-004]] 极限四则运算（保号性是其特殊情形）、[[ANL-THM-005]] 夹逼定理
