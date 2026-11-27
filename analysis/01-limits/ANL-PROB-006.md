---
title: "单调有界定理在递推数列中的应用"
type: problem
id: ANL-PROB-006
subject: analysis
chapter: 01-limits
tags:
  - 单调有界
  - 递推数列
  - 不动点
depends:
  - ANL-THM-006
  - ANL-DEF-004
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §2.4 习题"
difficulty: 4
tests:
  - ANL-THM-006
related:
  - ANL-EX-003
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

设 $a_1 = 1$，递推关系
$$
a_{n+1} = \sqrt{2 + a_n}, \quad n \geq 1.
$$

证明 $\{a_n\}$ 收敛，并求其极限。

## 提示

<details><summary>点击展开提示</summary>

- 用 [[ANL-THM-006]] 单调有界定理：先证 $\{a_n\}$ 单调，再证有界。
- **单调性**：用归纳法比较 $a_{n+1}$ 与 $a_n$。先算前几项 $a_1 = 1, a_2 = \sqrt{3} \approx 1.732, a_3 = \sqrt{2 + \sqrt{3}} \approx 1.932$ 看趋势——递增。
- **有界性**：用归纳法证 $a_n < 2$。
- **求极限**：极限若存在为 $L$，则 $L = \sqrt{2 + L}$ 即 $L^2 - L - 2 = 0$，解出 $L = 2$（舍弃 $L = -1$）。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 步：证明有上界

- 基础：$a_1 = 1 < 2$ ✓
- 归纳：设 $a_n < 2$，则 $a_{n+1} = \sqrt{2 + a_n} < \sqrt{2 + 2} = 2$ ✓

故 $\forall n: a_n < 2$。

### 第 2 步：证明单调递增

- 基础：$a_2 = \sqrt{3} > 1 = a_1$ ✓
- 归纳：设 $a_n > a_{n-1}$，则
  $$
  a_{n+1} - a_n = \sqrt{2 + a_n} - \sqrt{2 + a_{n-1}}.
  $$
  分子有理化：
  $$
  = \frac{(2 + a_n) - (2 + a_{n-1})}{\sqrt{2 + a_n} + \sqrt{2 + a_{n-1}}} = \frac{a_n - a_{n-1}}{\sqrt{2 + a_n} + \sqrt{2 + a_{n-1}}} > 0,
  $$
  因分子由归纳假设 $> 0$，分母明显 $> 0$。

故 $\{a_n\}$ 严格单调递增。

### 第 3 步：应用单调有界定理求极限

由 [[ANL-THM-006]]，$\{a_n\}$ 收敛。设 $L = \lim_n a_n$，则 $L \leq 2$ 且 $L \geq a_1 = 1$。

对递推关系 $a_{n+1} = \sqrt{2 + a_n}$ 两边取极限（由 [[ANL-DEF-004]] + 连续性）：
$$
L = \sqrt{2 + L} \implies L^2 = 2 + L \implies L^2 - L - 2 = 0 \implies (L - 2)(L + 1) = 0.
$$

故 $L = 2$ 或 $L = -1$。
由 $L \geq 1 > -1$，舍弃 $L = -1$。

因此 $\displaystyle \lim_{n \to \infty} a_n = 2$。$\blacksquare$

</details>

## 考察点

- [[ANL-THM-006]] 单调有界定理的标准两步法（单调性 + 有界性）
- 递推数列处理的"先证收敛、再代回求极限"模式
- 归纳法证明数列性质的规范写法

## 备注

**为什么不能颠倒顺序？**

> ✗ 错误做法："设 $L = \lim a_n$，由 $L = \sqrt{2 + L}$ 得 $L = 2$。"
> 这一步**预设了 $L$ 存在**——而存在性正是要证的。
> 如果不先证收敛，万一序列发散到 $\infty$ 或振荡，方程 $L = \sqrt{2 + L}$ 没有意义。
> 反例：取 $a_1 = -10$，则 $a_2 = \sqrt{-8}$ 已无定义，序列根本不存在。

**牛顿迭代视角**：本题的递推 $a_{n+1} = \sqrt{2 + a_n}$ 是不动点迭代 $a_{n+1} = g(a_n)$，
其中 $g(x) = \sqrt{2 + x}$。$|g'(x)| = \frac{1}{2\sqrt{2 + x}} < \frac{1}{2}$ 在 $x \in [1, 2]$ 上严格压缩，
故 $g$ 是压缩映射，不动点存在唯一（这是 Banach 不动点定理的初阶应用）。

**变式**：对 $a_1 = c, a_{n+1} = \sqrt{2 + a_n}$，$c \geq 0$ 时极限均为 $2$；
$c < -2$ 时序列从第二项起未定义。
