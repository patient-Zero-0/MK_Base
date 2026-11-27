---
title: "正定矩阵、二次型与极值判定"
type: definition
id: CROSS-007
subject: cross
chapter: _cross
tags:
  - 跨课
  - 正定矩阵
  - 二次型
  - 极值
depends:
  - ALG-THM-044
  - ANL-THM-025
  - ANL-DEF-018
uses: []
status: stable
source: "综合：华东师范大学《数学分析》第5版 §6.1–§6.4 + 丘维声《高等代数》第3版 §5.4"
difficulty: 4
related:
  - ALG-EX-024
  - ANL-PROB-014
---

## 关联说明

设 $f:U\to\mathbb{R}$（$U\subset\mathbb{R}^n$ 为开集）二阶连续可微，$x_0$ 是驻点：$\nabla f(x_0)=0$。由混合偏导的对称性，Hessian 矩阵
$$
H=\bigl(\partial_i\partial_jf(x_0)\bigr)_{1\le i,j\le n}
$$
是对称矩阵。对固定方向 $h$，令 $\varphi(t)=f(x_0+th)$，对一元函数 $\varphi$ 用 Peano 余项的 Taylor 公式（[[ANL-THM-025]]）：
$$
\varphi(1)=\varphi(0)+\varphi'(0)+\frac12\varphi''(0)+o(1)
=f(x_0)+\frac12h^\top Hh+o\bigl(\lVert h\rVert^2\bigr)\qquad(h\to0),
$$
这里用了 $\varphi(0)=f(x_0)$、$\varphi'(0)=\nabla f(x_0)^\top h=0$、$\varphi''(0)=h^\top Hh$。所以极值判定归结为二次型 $h\mapsto h^\top Hh$ 的符号判定。这正是高等代数的正定二次型理论。

| Hessian 类型 | 二次型的符号 | 极值结论 | 代数判别 |
|---|---|---|---|
| 正定 | 对一切 $h\ne0$ 有 $h^\top Hh>0$ | 严格局部极小 | 特征值全正；顺序主子式全正；$H=C^\top C$（$C$ 可逆） |
| 负定 | 对一切 $h\ne0$ 有 $h^\top Hh<0$ | 严格局部极大 | 特征值全负；$-H$ 正定 |
| 不定 | 既有正值又有负值 | 鞍点，不是极值 | 特征值有正有负 |
| 半正定或半负定 | 符号不变但可取到零 | 二阶判别失效 | 有零特征值 |

代数判别依赖谱定理（[[ALG-THM-044]]）：存在正交矩阵 $Q$ 使 $H=Q\Lambda Q^\top$，$\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$。令 $y=Q^\top h$，则
$$
h^\top Hh=\sum_{i=1}^{n}\lambda_iy_i^2 .
$$
于是 $H$ 正定当且仅当所有 $\lambda_i>0$。此时记 $\lambda_{\min}>0$ 为最小特征值，有 $h^\top Hh\ge\lambda_{\min}\lVert h\rVert^2$，从而
$$
f(x_0+h)-f(x_0)\ge\frac{\lambda_{\min}}2\lVert h\rVert^2+o\bigl(\lVert h\rVert^2\bigr)>0
$$
对充分小的 $h\ne0$ 成立，故 $x_0$ 是严格局部极小点。负定情形同理。若 $H$ 不定，取对应正特征值的单位特征向量 $u$ 与对应负特征值的单位特征向量 $v$：沿 $h=tu$ 有 $f(x_0+h)-f(x_0)>0$，沿 $h=tv$ 有 $f(x_0+h)-f(x_0)<0$（$t$ 充分小且非零），故 $x_0$ 的任意邻域内既有函数值更大的点又有更小的点，$x_0$ 不是极值点。

顺序主子式判别（Sylvester 判别法）说：$H$ 正定当且仅当各阶顺序主子式 $\Delta_k=\det\bigl((h_{ij})_{1\le i,j\le k}\bigr)$（$k=1,\dots,n$）全为正。它的直观来源是配方：高斯消元把二次型化为平方和时，每一步的主元就是这些顺序主子式的比值。

## 直觉理解

一元情形：$f''(x_0)>0$ 是极小、$f''(x_0)<0$ 是极大、$f''(x_0)=0$ 无法判定。多元情形把"$f''$"换成"沿每个方向的二阶导数"组成的矩阵：正定意味着沿**所有**方向都向上弯曲，图形是碗底；不定意味着有的方向向上、有的方向向下，图形是马鞍；半正定意味着存在平坦方向，二阶信息不足以判断。

这里容易产生的错觉是"半正定介于正定与不定之间，应该也算极小"。事实是半正定时二次型可以是零方向，函数的升降由更高阶项决定，两种结果都可能出现：$x^4+y^4$ 的 Hessian 是零矩阵却严格极小，而 $x^2-y^4$ 的 Hessian 半正定却是鞍点。

从代数看，判断 $H$ 的类型就是给二次型做标准化：用合同变换化到对角形，正惯性指数等于正特征值个数。谱定理的正交对角化是最方便的标准化方式，因为特征值直接给出二次型在正交方向上的系数。

## 一个具体例子

取 $f(x,y)=x^2+xy+y^2$。梯度为
$$
\nabla f=(2x+y,\;x+2y),
$$
令其为零得唯一的驻点 $x_0=(0,0)$。Hessian 为
$$
H=\begin{pmatrix}2&1\\1&2\end{pmatrix},
$$
其特征多项式为 $\lambda^2-4\lambda+3=(\lambda-1)(\lambda-3)$，特征值 $\lambda_1=1$、$\lambda_2=3$ 全为正，故 $H$ 正定，$x_0$ 是严格局部极小点。

用顺序主子式验证：$\Delta_1=2>0$，$\Delta_2=\det H=3>0$，同样得到正定。用配方直接验证：由
$$
x^2+xy+y^2=\frac12(x+y)^2+\frac12(x^2+y^2)\ge\frac12(x^2+y^2),
$$
可知 $f(0,0)=0$ 且 $(x,y)\ne(0,0)$ 时 $f>0$，故原点其实是全局唯一极小点，且 $\lambda_{\min}=1$ 与配方给出的系数一致。

对照不定情形：$g(x,y)=x^2-y^2$ 在原点的 Hessian 为 $\operatorname{diag}(2,-2)$，不定；沿 $x$ 轴 $g>0$、沿 $y$ 轴 $g<0$，原点确实是鞍点。

## 常见误区

- ✗ **认为 Hessian 半正定就一定是极小点（或半正定就一定不是极小点）。** 两种说法都错。反例一：$f(x,y)=x^2-y^4$ 在原点 $\nabla f=0$、$H=\operatorname{diag}(2,0)$ 半正定，但 $f(t,0)=t^2>0$、$f(0,t)=-t^4<0$，原点是鞍点。反例二：$f(x,y)=x^4+y^4$ 在原点 $H=0$ 半正定，但 $f\ge0=f(0,0)$，原点是严格极小点。半正定时二阶判别确实失效，必须看高阶项。
- ✗ **认为"Hessian 正定"是严格局部极小的必要条件。** 反例：$f(x,y)=x^2+y^4$ 在原点严格局部极小（$f\ge0$ 且仅在原点取等），但 $H=\operatorname{diag}(2,0)$ 只是半正定。极小点处 Hessian 只能保证半正定；正定性是充分条件。

## 链接

- 代数工具：[[ALG-THM-044]] 实对称矩阵正交对角化（谱定理）、[[ALG-EX-024]] 迹、特征值与牛顿恒等式
- 分析工具：[[ANL-THM-025]] Taylor 公式、[[ANL-DEF-018]] 极值（局部极大与局部极小）
- 不等式视角：[[ANL-PROB-014]] Jensen 不等式与 AM-GM（配方与二次型非负性的常用技巧）
