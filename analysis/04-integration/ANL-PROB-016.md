---
title: "反常积分综合：高斯积分与 Γ 函数的联系"
type: problem
id: ANL-PROB-016
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 反常积分
  - 高斯积分
  - Gamma 函数
depends:
  - ANL-DEF-029
  - ANL-THM-035
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §11.2 习题（综合改编）"
difficulty: 4
tests:
  - ANL-DEF-029
  - ANL-THM-035
related:
  - ANL-EX-014
  - ANL-THM-033
  - ANL-THM-034
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

1. **收敛性**：用比较判别法（[[ANL-THM-035]]）证明 $\displaystyle\int_0^{\infty} e^{-x^2}\,dx$ 收敛。

2. **求值（高斯积分）**：证明
    $$
    I := \int_0^{\infty} e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2},
    \qquad\text{从而}\quad \int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}.
    $$

3. **与 Γ 函数的联系**：利用 $\displaystyle\Gamma(s) = \int_0^{\infty} t^{s-1}e^{-t}\,dt$（见 [[ANL-EX-014]]），通过换元（[[ANL-THM-033]]）证明
    $$
    \Gamma\!\left(\tfrac{1}{2}\right) = \sqrt{\pi},
    $$
    并由此重新得到第 2 题的结论。

4. **应用（标准正态分布）**：求常数 $c$ 使 $\displaystyle\int_{-\infty}^{\infty} c\,e^{-x^2/2}\,dx = 1$。

## 提示

<details><summary>点击展开提示</summary>

- **第 1 题**：在 $[1,\infty)$ 上 $x^2 \ge x$，故 $e^{-x^2}\le e^{-x}$，而 $\int_1^\infty e^{-x}\,dx$ 收敛；$[0,1]$ 上被积函数连续有界。
- **第 2 题**（经典极坐标技巧）：考虑 $I^2 = \left(\int_0^\infty e^{-x^2}dx\right)\left(\int_0^\infty e^{-y^2}dy\right) = \iint_{x,y>0} e^{-(x^2+y^2)}\,dx\,dy$，化为极坐标。**此步用到二重积分（多元微积分，前向引用）**。
- **第 3 题**：在 $\Gamma(1/2)=\int_0^\infty t^{-1/2}e^{-t}\,dt$ 中令 $t = x^2$。
- **第 4 题**：令 $u = x/\sqrt{2}$ 化归到 $\int e^{-u^2}\,du$。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题：收敛性

被积函数 $e^{-x^2}$ 在 $[0,\infty)$ 上非负连续。拆为
$$
\int_0^{\infty} e^{-x^2}\,dx = \int_0^1 e^{-x^2}\,dx + \int_1^{\infty} e^{-x^2}\,dx.
$$

第一段是连续函数在有限闭区间上的定积分，存在且有限。

第二段：当 $x \ge 1$ 时 $x^2 \ge x$，故 $0 \le e^{-x^2} \le e^{-x}$。而
$$
\int_1^{\infty} e^{-x}\,dx = \lim_{A\to\infty}\big[-e^{-x}\big]_1^A = e^{-1} < \infty.
$$
由比较判别法（[[ANL-THM-035]]，非负被积函数的比较形）知 $\int_1^\infty e^{-x^2}\,dx$ 收敛。

故原反常积分（[[ANL-DEF-029]]）收敛。$\quad\blacksquare$

### 第 2 题：高斯积分求值

由第 1 题，$I = \int_0^\infty e^{-x^2}\,dx$ 是有限正数。考虑
$$
I^2 = \left(\int_0^{\infty} e^{-x^2}\,dx\right)\left(\int_0^{\infty} e^{-y^2}\,dy\right)
= \iint_{\{x>0,\,y>0\}} e^{-(x^2+y^2)}\,dx\,dy.
$$

化为极坐标 $x = r\cos\theta,\ y = r\sin\theta$，第一象限对应 $r\in[0,\infty),\ \theta\in[0,\tfrac{\pi}{2}]$，$dx\,dy = r\,dr\,d\theta$：
$$
I^2 = \int_0^{\pi/2}\!\!\int_0^{\infty} e^{-r^2}\,r\,dr\,d\theta
= \int_0^{\pi/2} d\theta \cdot \int_0^{\infty} r e^{-r^2}\,dr.
$$

内层积分（第一类换元，[[ANL-THM-033]]，令 $u = r^2$）：
$$
\int_0^{\infty} r e^{-r^2}\,dr = \left[-\tfrac{1}{2}e^{-r^2}\right]_0^{\infty} = \tfrac{1}{2}.
$$

故 $I^2 = \dfrac{\pi}{2}\cdot \dfrac{1}{2} = \dfrac{\pi}{4}$，又 $I>0$，得
$$
I = \frac{\sqrt{\pi}}{2}.
$$

由 $e^{-x^2}$ 偶函数，$\displaystyle\int_{-\infty}^{\infty} e^{-x^2}\,dx = 2I = \sqrt{\pi}$。$\quad\blacksquare$

> 极坐标一步使用了二重积分换元（多元微积分），属前向引用；在单变量框架内本积分无初等原函数，无法用 Newton–Leibniz 直接求值，这是高斯积分的经典之处。

### 第 3 题：Γ(1/2) = √π

在 $\Gamma\!\left(\tfrac{1}{2}\right) = \displaystyle\int_0^{\infty} t^{-1/2}e^{-t}\,dt$ 中令 $t = x^2$（$x>0$），则 $dt = 2x\,dx$，$t^{-1/2} = x^{-1}$：
$$
\Gamma\!\left(\tfrac{1}{2}\right) = \int_0^{\infty} x^{-1} e^{-x^2}\cdot 2x\,dx = 2\int_0^{\infty} e^{-x^2}\,dx = 2I.
$$

代入第 2 题 $I = \tfrac{\sqrt\pi}{2}$，得 $\Gamma\!\left(\tfrac{1}{2}\right) = \sqrt{\pi}$。

反之，若已知 $\Gamma(1/2)=\sqrt\pi$（可由 Beta 函数 $B(\tfrac12,\tfrac12)=\pi$ 独立导出），则上式给出 $I = \tfrac12\Gamma(\tfrac12) = \tfrac{\sqrt\pi}{2}$，与第 2 题一致。$\quad\blacksquare$

### 第 4 题：标准正态归一化常数

令 $u = x/\sqrt{2}$，$dx = \sqrt{2}\,du$：
$$
\int_{-\infty}^{\infty} e^{-x^2/2}\,dx = \sqrt{2}\int_{-\infty}^{\infty} e^{-u^2}\,du = \sqrt{2}\cdot \sqrt{\pi} = \sqrt{2\pi}.
$$

故归一化要求 $c\sqrt{2\pi} = 1$，即
$$
c = \frac{1}{\sqrt{2\pi}}.
$$

这正是标准正态分布密度 $\dfrac{1}{\sqrt{2\pi}}e^{-x^2/2}$ 的归一化常数。$\quad\blacksquare$

</details>

## 考察点

- [[ANL-DEF-029]] 无穷限反常积分的收敛定义与"拆区间"处理
- [[ANL-THM-035]] 非负被积函数的比较判别法
- [[ANL-THM-033]] 换元法在反常积分中的应用（$t=x^2$、极坐标）
- [[ANL-EX-014]] Γ 函数定义与 $\Gamma(1/2)$
- 无初等原函数积分的求值思想（升维 + 极坐标）

## 备注

**高斯积分的跨学科地位**：

| 领域 | 出现形式 |
|---|---|
| 概率论 | 正态分布密度归一化 $\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ |
| 统计物理 | 配分函数中的 Gaussian 积分 |
| 量子力学 | 谐振子基态波函数、路径积分 |
| 数值分析 | Gauss–Hermite 求积法权重 |

**方法论提醒**：单变量反常积分若无初等原函数（如 $e^{-x^2}$、$\frac{\sin x}{x}$），常需"换框架"——升维到二重积分（高斯积分）、引入参数求导（Feynman 技巧）、或借助级数/特殊函数（[[ANL-EX-014]] 的 Γ 函数）。这与可用 Newton–Leibniz 直接求值的"计算工具"类积分（[[ANL-THM-034]] 分部、[[ANL-THM-033]] 换元）形成方法上的对照。
