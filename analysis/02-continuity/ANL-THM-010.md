---
title: "函数极限的保号性"
type: theorem
id: ANL-THM-010
subject: analysis
chapter: 02-continuity
tags:
  - 函数极限
  - 保号性
depends:
  - ANL-DEF-008
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §3.2"
difficulty: 2
related:
  - ANL-THM-003
  - ANL-THM-009
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件与结论

设 $\lim_{x \to x_0} f(x) = A$（按 [[ANL-DEF-008]]）。

**保号性（强形式）**：

- 若 $A > 0$，则 $\exists \delta > 0$，$\forall x : 0 < |x - x_0| < \delta \implies f(x) > A/2 > 0$。
- 若 $A < 0$，则 $\exists \delta > 0$，$\forall x : 0 < |x - x_0| < \delta \implies f(x) < A/2 < 0$。

**保号性（弱形式 / 反向）**：

- 若 $\exists \delta > 0$，$\forall x : 0 < |x - x_0| < \delta \implies f(x) \geq 0$，则 $A \geq 0$（**只能弱不等**）。
- 若 $f(x) \leq c$ 在某去心邻域内成立，则 $A \leq c$。

## 直觉理解

数列保号性 [[ANL-THM-003]] 的"连续版本"——结构与论证完全平行。

形式化要点同数列：

- 强方向：$A > 0$ ⇒ 在某去心邻域内 $f > A/2$（**留出余量**的技巧）。
- 反向：仅能从 $f \geq 0$ 推出 $A \geq 0$（**取极限会保留 $\leq, \geq$，丢失 $<, >$**）。

> 极限取**闭包**：$f$ 在 $\geq 0$ 的"闭半轴"上 ⇒ 极限也在 $\geq 0$ 的"闭半轴"上，
> 但**未必**还在严格 $> 0$ 的开半轴上（如 $f(x) = x^2 \geq 0$，但 $\lim_{x \to 0} f = 0$）。

## 证明（强形式，正极限）

**证明：** 在 [[ANL-DEF-008]] 中取 $\varepsilon = A/2 > 0$。
存在 $\delta > 0$ 使 $\forall x : 0 < |x - x_0| < \delta \implies |f(x) - A| < A/2$，即
$$
A - A/2 < f(x) < A + A/2 \implies f(x) > A/2 > 0.
$$
$\blacksquare$

弱形式证明：反证。设 $f \geq 0$ 但 $A < 0$，则由强形式 $f < A/2 < 0$ 在某去心邻域成立，矛盾。$\blacksquare$

## 常见错误

- ✗ 由 $f(x) > 0$ 推 $A > 0$。错。反例：$f(x) = x^2$ 在 $x_0 = 0$ 附近 $f > 0$，但 $\lim f = 0$。
  正确推论是 $A \geq 0$。
- ✗ 把 "$f(x) > g(x)$" 错误地推出 "$A > B$"。
  正确推论是 $A \geq B$（强不等不传给极限）。

## 推论

- **比较定理**：$f(x) \leq g(x)$ 在某去心邻域成立，且两者极限都存在 ⇒ $\lim f \leq \lim g$。
- **除法定理依赖**：[[ANL-THM-009]] 除法部分需要"$\lim g = B \neq 0$ 时 $|g| \geq |B|/2$ 局部成立"——这正是本定理对 $|g|$ 的应用结果。

## 链接

- 前置：[[ANL-DEF-008]]
- 数列版本：[[ANL-THM-003]]
- 应用：[[ANL-THM-009]] 函数极限四则运算（除法的核心引理）
