---
title: "Taylor 公式综合应用"
type: problem
id: ANL-PROB-013
subject: analysis
chapter: 03-differentiation
tags:
  - 微分
  - Taylor 公式
  - 极限
  - 误差估计
depends:
  - ANL-THM-025
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §6.3 综合习题"
difficulty: 4
tests:
  - ANL-THM-025
related:
  - ANL-EX-010
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

1. **Taylor 求极限**：用 Taylor 展开求
    $$ \lim_{x \to 0} \frac{e^x - 1 - x - x^2/2}{x^3}. $$
2. **误差估计**：用 Taylor 公式计算 $\sin(0.1)$ 至 $7$ 位有效数字（即误差 $< 10^{-7}$），并给出严格误差上界。
3. **不等式证明**：证明对一切 $x \geq 0$，
    $$ e^x \geq 1 + x + \frac{x^2}{2}. $$

## 提示

<details><summary>点击展开提示</summary>

- **第 1 题**：把 $e^x$ 展开到 $x^3$ 阶（含 Peano 余项 $o(x^3)$，[[ANL-THM-025]] Peano 形式即可），分子化简。
- **第 2 题**：$\sin x = x - \dfrac{x^3}{6} + \dfrac{x^5}{120} - \cdots$。用[[ANL-THM-025]] Lagrange 余项给误差严格上界：取展开到 $x^3$ 阶，$R_4(x) = \dfrac{f^{(4)}(\xi)}{4!} x^4$。注意 $\sin$ 的奇偶性使 4 阶余项实质上是 $x^5$ 项。
- **第 3 题**：用 Lagrange 余项形式 $e^x = 1 + x + \dfrac{x^2}{2} + \dfrac{e^\xi}{6} x^3$，对 $x \geq 0$ 余项非负即可。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题

**解**：由[[ANL-THM-025]] Peano 形式，$e^x$ 在 $0$ 处展开到 $x^3$ 阶：
$$
e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + o(x^3) \quad (x \to 0).
$$

代入分子：
$$
e^x - 1 - x - \frac{x^2}{2} = \frac{x^3}{6} + o(x^3).
$$

故
$$
\frac{e^x - 1 - x - x^2/2}{x^3} = \frac{1}{6} + \frac{o(x^3)}{x^3} \to \frac{1}{6} + 0 = \frac{1}{6}. \quad\blacksquare
$$

> **对比 L'Hospital 法则**：本题用 [[ANL-THM-024]] L'Hospital 需求导 $3$ 次，
> Taylor 仅展开一次得到答案——这是 Taylor 处理"高阶 $0/0$"型的优势。

### 第 2 题

**解**：取 $f(x) = \sin x$ 在 $0$ 处 Taylor 展开到 $x^3$ 阶（含 Lagrange 余项）：
$$
\sin x = x - \frac{x^3}{6} + \frac{f^{(4)}(\xi)}{4!} x^4
$$
其中 $\xi$ 介于 $0$ 与 $x$ 之间。$f^{(4)}(t) = \sin t$，故 $|f^{(4)}(\xi)| = |\sin \xi| \leq 1$。

因此
$$
\left| \sin(0.1) - \left( 0.1 - \frac{0.001}{6} \right) \right| \leq \frac{1}{24} \cdot (0.1)^4 = \frac{10^{-4}}{24} \approx 4.17 \times 10^{-6}.
$$

**精度不足！** 升至 $x^5$ 阶展开（$\sin$ 奇函数，$x^4$ 项系数为 $0$，故"展到 $x^3$ 余项实质 $\sim x^5$"。
但严格地用 Lagrange 余项需直接展开到含 $x^5$ 阶）：

$$
\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} + R_5(x), \quad R_5(x) = \frac{f^{(6)}(\xi)}{6!} x^6,
$$
$|f^{(6)}(\xi)| = |\sin \xi| \leq 1$，故
$$
|R_5(0.1)| \leq \frac{(0.1)^6}{720} \approx 1.39 \times 10^{-9}.
$$

**计算近似值**：
$$
\sin(0.1) \approx 0.1 - \frac{0.001}{6} + \frac{10^{-5}}{120} = 0.1 - 0.000\,166\,67 + 0.000\,000\,083 \approx 0.099\,833\,42.
$$

**严格误差上界**：$|\sin(0.1) - 0.099\,833\,42| < 1.4 \times 10^{-9} < 10^{-7}$。

故 $\sin(0.1) \approx 0.099\,833\,4$（保留 $7$ 位）。$\blacksquare$

> **关键观察**：用 Lagrange 余项时，**展开阶数不一定要凑齐到目标阶数**——
> 对奇 / 偶函数，可"跳过"某些项利用对称性获得更紧的余项估计。
> 实务中常采用"展到下一个非零项 + 估其后余项"。

### 第 3 题

**证明**：由[[ANL-THM-025]] Lagrange 余项形式（$n = 2$）：$\exists \xi \in (0, x)$ 使
$$
e^x = 1 + x + \frac{x^2}{2} + \frac{e^\xi}{6} x^3.
$$

由 $\xi \geq 0$，$e^\xi \geq 1 > 0$；又 $x \geq 0$ 故 $x^3 \geq 0$。
因此余项 $\dfrac{e^\xi}{6} x^3 \geq 0$。

代入：
$$
e^x = 1 + x + \frac{x^2}{2} + \underbrace{\frac{e^\xi}{6} x^3}_{\geq 0} \geq 1 + x + \frac{x^2}{2}. \quad\blacksquare
$$

> **推广**：对一切 $x \geq 0$，$e^x \geq \displaystyle \sum_{k=0}^n \frac{x^k}{k!}$。
> 同理 $x \leq 0$ 时方向反转奇偶——证明留作变式。

</details>

## 考察点

- [[ANL-THM-025]] Peano 余项用于求极限（处理高阶 $0/0$）
- [[ANL-THM-025]] Lagrange 余项用于**严格的**误差估计
- 对奇 / 偶函数 Taylor 展开的对称性观察（节省余项阶数）
- Lagrange 余项的非负性 ⇒ 不等式（第 3 题模式）

## 备注

**Taylor 公式的两种用法**：

| 形式 | 用途 | 关键 |
|---|---|---|
| Peano 余项 $o((x-x_0)^n)$ | 求极限、渐近行为 | "$o(\cdot)$ 的代数运算" |
| Lagrange 余项 $\dfrac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}$ | 误差估计、不等式证明 | "找 $\sup \|f^{(n+1)}\|$" |

**对比 L'Hospital 法则与 Taylor**：

| | L'Hospital | Taylor |
|---|---|---|
| 适用 | $0/0$, $\infty/\infty$ | $0/0$（高阶尤佳） |
| 计算量 | 重复求导 $k$ 次 | 一次展开 $k$ 阶 |
| 直观性 | 弱 | 强（看到主导项） |
| 不等式证明 | 不擅长 | 擅长（余项控制） |
| 处理振荡分母 | 失败（$x^2 \sin(1/x)$ 反例） | 同样需小心 |
