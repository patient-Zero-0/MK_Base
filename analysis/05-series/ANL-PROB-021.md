---
title: "条件收敛与 Riemann 重排定理"
type: problem
id: ANL-PROB-021
subject: analysis
chapter: 05-series
tags:
  - 级数
  - 条件收敛
  - 重排
  - Riemann 重排定理
depends:
  - ANL-DEF-034
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §12.3 综合习题"
difficulty: 5
tests:
  - ANL-DEF-034
related:
  - ANL-THM-042
  - ANL-THM-038
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

设 $\sum a_n$ **条件收敛**（[[ANL-DEF-034]]）。记其正部 $a_n^+ = \max(a_n, 0)$、负部 $a_n^- = \max(-a_n, 0)$。

1. 证明 $\displaystyle\sum a_n^+ = +\infty$ 且 $\displaystyle\sum a_n^- = +\infty$（正项与负项各自之和均发散）。
2. **（Riemann 重排定理）** 证明：对任意给定的 $S \in \mathbb{R}$，存在 $\sum a_n$ 的一个**重排** $\sum a_{\sigma(n)}$ 使其收敛于 $S$。
3. 以交错调和级数 $\displaystyle\sum_{n=1}^\infty \frac{(-1)^{n-1}}{n} = \ln 2$ 为例，说明可重排出和为 $\frac{3}{2}\ln 2$ 的级数。

## 提示

<details><summary>点击展开提示</summary>

- **第 1 题**：反证。注意 $a_n^+ = \frac{|a_n|+a_n}{2}$，$a_n^- = \frac{|a_n|-a_n}{2}$。若两者之一收敛，结合 $\sum a_n$ 收敛会推出 $\sum|a_n|$ 收敛，与条件收敛矛盾。
- **第 2 题**：贪心构造——先取正项累加到刚超过 $S$，再取负项累加到刚低于 $S$，反复进行。由第 1 题两堆"取之不尽"，由 $a_n \to 0$ 保证每次超调幅度趋零。
- **第 3 题**：把交错调和级数按"两正一负"模式重排，用调和级数部分和 $H_n = \ln n + \gamma + o(1)$ 计算。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题：正负部各自发散

由定义 $a_n^+ = \dfrac{|a_n| + a_n}{2}$，$a_n^- = \dfrac{|a_n| - a_n}{2}$，故
$$
a_n^+ + a_n^- = |a_n|, \qquad a_n^+ - a_n^- = a_n. \tag{$\ast$}
$$

**反证**：设 $\sum a_n^+$ 收敛。由 $\sum a_n$ 收敛及 $a_n^- = a_n^+ - a_n$，得 $\sum a_n^-$ 收敛。再由 $(\ast)$，$\sum |a_n| = \sum(a_n^+ + a_n^-)$ 收敛——即 $\sum a_n$ **绝对**收敛，与"条件收敛"（[[ANL-DEF-034]]）矛盾。

故 $\sum a_n^+$ 发散；因正项级数发散即趋于 $+\infty$，得 $\sum a_n^+ = +\infty$。对称地 $\sum a_n^- = +\infty$。$\quad\blacksquare$

> 直观：条件收敛级数的正项之和与负项之和**各自都是无穷大**，收敛全靠两者以恰当节奏抵消。

### 第 2 题：Riemann 重排定理

记 $\sum a_n$ 的非负项依次为 $p_1, p_2, \ldots$（即 $a_n^+$ 中的正者），负项的绝对值依次为 $q_1, q_2, \ldots$。由第 1 题，
$$
\sum p_k = +\infty, \qquad \sum q_k = +\infty;
$$
又 $\sum a_n$ 收敛 ⇒ $a_n \to 0$ ⇒ $p_k \to 0,\ q_k \to 0$。

**贪心构造**（设目标 $S \ge 0$，$S<0$ 对称）：

1. 依次取正项 $p_1, p_2, \ldots$ 累加，直到部分和**首次** $> S$（因 $\sum p_k = +\infty$，必在有限步达成）；
2. 接着取负项 $-q_1, -q_2, \ldots$ 累加，直到部分和**首次** $< S$（因 $\sum q_k = +\infty$，必达成）；
3. 再取正项至首次 $> S$，如此交替无限进行。

这给出 $\sum a_n$ 的一个重排（每个原项恰用一次：正项、负项分别按序取尽）。

**收敛到 $S$**：每个"转折点"处的部分和与 $S$ 之差，不超过**刚加入的那一项**的绝对值（因加入它之前尚在 $S$ 另一侧）。设第 $m$ 个转折由项 $t_m$（某个 $p_k$ 或 $-q_k$）触发，则该处 $|(\text{部分和}) - S| \le |t_m|$。两转折之间部分和单调地朝 $S$ 移动，故全程
$$
|(\text{部分和}) - S| \le \max(\text{近期加入项的绝对值}) \to 0
$$
（因 $p_k, q_k \to 0$）。故重排级数收敛于 $S$。$\quad\blacksquare$

> 同法可使重排级数发散到 $+\infty$、$-\infty$ 或振荡——条件收敛级数的和**完全由求和顺序决定**。

### 第 3 题

原级数 $\sum \frac{(-1)^{n-1}}{n} = \ln 2$。按"**两个正项跟一个负项**"重排：
$$
\underbrace{1 + \frac13}_{} - \frac12 + \underbrace{\frac15 + \frac17}_{} - \frac14 + \underbrace{\frac19 + \frac1{11}}_{} - \frac16 + \cdots
$$

考察其前 $3n$ 项部分和 $T_{3n}$（含前 $2n$ 个正项 $\frac{1}{1},\frac13,\ldots,\frac1{4n-1}$ 与前 $n$ 个负项 $\frac12,\frac14,\ldots,\frac1{2n}$）：
$$
T_{3n} = \sum_{k=1}^{2n}\frac{1}{2k-1} - \sum_{k=1}^{n}\frac{1}{2k}
= \left(\sum_{k=1}^{4n}\frac1k - \sum_{k=1}^{2n}\frac{1}{2k}\right) - \frac12\sum_{k=1}^{n}\frac1k = H_{4n} - \frac12 H_{2n} - \frac12 H_n.
$$
用 $H_m = \ln m + \gamma + o(1)$：
$$
T_{3n} = \big(\ln 4n - \tfrac12\ln 2n - \tfrac12 \ln n\big) + o(1) = \ln\frac{4n}{\sqrt{2n}\cdot\sqrt{n}} + o(1) = \ln\frac{4n}{n\sqrt2} + o(1) = \ln\frac{4}{\sqrt2} + o(1).
$$
而 $\ln\dfrac{4}{\sqrt2} = \ln(2\sqrt2) = \ln 2 + \tfrac12\ln 2 = \tfrac32\ln 2$。故 $T_{3n} \to \tfrac32\ln 2$（相邻部分和差 $\to0$ 保证整体收敛于此）。$\quad\blacksquare$

</details>

## 考察点

- [[ANL-DEF-034]] 条件收敛的本质：正负部各自发散
- 正部 / 负部分解 $a_n^\pm = \frac{|a_n|\pm a_n}{2}$ 的标准技巧
- Riemann 重排的贪心构造与 $a_n \to 0$ 控制超调
- 调和级数渐近 $H_n = \ln n + \gamma + o(1)$ 在重排求和中的应用

## 备注

**绝对收敛 vs 条件收敛的分水岭**：

| 性质 | 绝对收敛 | 条件收敛 |
|---|---|---|
| 正部 / 负部 | 各自收敛 | 各自发散（本题第 1） |
| 任意重排 | 和**不变** | 和可为**任意值**（Riemann，本题第 2） |
| 类比 | 行为如有限和 | 收敛极脆弱，依赖顺序 |

**Riemann 重排定理的震撼**在于：它表明"无穷级数的加法**不满足交换律**"——只要级数仅条件收敛。这是有限和直觉彻底失效之处，也是为何绝对收敛（[[ANL-DEF-034]]）在分析中被如此看重：唯有它能保证求和顺序无关紧要。
