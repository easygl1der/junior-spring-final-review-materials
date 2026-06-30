<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# 从这个 Double 公式你可以得到的一些，比如说各种曲线、各种曲率；我可能在微分极和这个框架下面有很多这种有曲率线、测力线或者是这种线、什么密切平面渐进线，这些东西的定义。你能不能从这个 Double 公式或者是从这个 Weingarten 公式这样的，然后用这里面的量来描述所有的这些微分集合在这个 Do Carmo 框架下面？所有可能涉及到的这些概念，它们都是对应的一个什么什么东西。

可以。你可以把 Do Carmo 这一章的曲面上曲线概念统一看成：**Darboux** 标架把一条空间曲线的弯曲分解成“曲面内的弯曲”和“曲面法向的弯曲”，而 Weingarten 公式把曲面法向的变化编码成形算子。Do Carmo 中 Darboux 三面体 $\{T,V,N\}$ 的公式是 $T'=aV+bN,\ V'=-aT+cN,\ N'=-bT-cV$，其中 $a$ 是测地曲率，$b$ 是法曲率，$-c$ 与测地挠率对应；同时曲率分解满足 $k^2=k_g^2+k_n^2$。[^1]

## 总框架

设 $\alpha(s)\subset S$ 是曲面上的弧长曲线。记

$$
T=\alpha'(s),\qquad N=\text{曲面单位法向},\qquad Q=N\times T.
$$

Darboux 标架是

$$
\{T,Q,N\}.
$$

它的求导公式是

$$
\boxed{
\begin{aligned}
T'&=k_gQ+k_nN,\\
Q'&=-k_gT+\tau_gN,\\
N'&=-k_nT-\tau_gQ.
\end{aligned}
}
$$

而 Weingarten 公式是

$$
\boxed{dN_p(v)=-S_p(v)}.
$$

其中 $S_p$ 是 shape operator，也叫 Weingarten map。它决定第二基本形式：

$$
\mathrm{II}_p(u,v)=\langle S_p(u),v\rangle.
$$

对曲线切向 $T$，有

$$
k_n=\mathrm{II}(T,T)=\langle S(T),T\rangle,
$$

$$
\tau_g=\langle S(T),Q\rangle.
$$

所以你可以这样记：

$$
\boxed{\text{曲面上的曲线}=\text{一个切向 }T+\text{三个标量 }k_g,k_n,\tau_g.}
}
$$

其中：

- $k_g$：曲线自己在曲面内怎么拐；
- $k_n$：曲面沿这个方向怎么向法向弯；
- $\tau_g$：曲面法向沿这条曲线怎么扭。


## 三个曲率量

| 量 | 公式 | 几何意义 | 控制对象 |
| :-- | :-- | :-- | :-- |
| 空间曲率 $k$ | $T'=kn$ | 曲线在 $\mathbb{R}^3$ 中总弯曲 | 曲线本身 |
| 测地曲率 $k_g$ | $k_g=\langle T',Q\rangle$ | 曲线在曲面内的弯曲 | 内蕴方向 |
| 法曲率 $k_n$ | $k_n=\langle T',N\rangle=\langle S(T),T\rangle$ | 曲线沿曲面法向的弯曲 | 第二基本形式 |
| 测地挠率 $\tau_g$ | $\tau_g=\langle S(T),Q\rangle$ | 法向沿曲线的切向旋转 | 主方向偏离程度 |

它们满足

$$
\boxed{k^2=k_g^2+k_n^2}.
$$

这句话非常重要：空间曲率 $k$ 被拆成曲面切平面内的 $k_g$ 和曲面法向的 $k_n$。

## 三类重要曲线

在 Do Carmo 这个框架里，最常见三类曲线分别是把 Darboux 三个量中的某个量置零：


| 曲线类型 | 条件 | Darboux 表现 | 几何解释 |
| :-- | :-- | :-- | :-- |
| 测地线 | $k_g=0$ | $T'=k_nN$ | 曲线不在曲面内“拐弯” |
| 渐近曲线 | $k_n=0$ | $T'=k_gQ$ | 曲线没有法向弯曲 |
| 曲率线 | $\tau_g=0$ | $N'=-k_nT$ | 切向总是主方向 |

这张表是你应该背下来的核心对应关系。

更直观地说：

- 测地线：曲率向量垂直于曲面；
- 渐近曲线：曲率向量落在切平面内；
- 曲率线：曲面法向沿曲线变化时不偏向旁边的 $Q$，只沿 $T$ 变。


## Weingarten 视角

因为

$$
N' = dN(T)=-S(T),
$$

而 Darboux 公式给出

$$
N'=-k_nT-\tau_gQ.
$$

所以

$$
\boxed{S(T)=k_nT+\tau_gQ}.
$$

这句话把所有概念都统一了：


| 条件 | 等价说法 |
| :-- | :-- |
| $T$ 是主方向 | $S(T)\parallel T$ |
| $C$ 是曲率线 | $\tau_g=0$ |
| $T$ 是渐近方向 | $\langle S(T),T\rangle=0$ |
| $C$ 是渐近曲线 | $k_n=0$ |
| $T$ 是共轭于 $Q$ 的方向 | $\langle S(T),Q\rangle=0$ |
| $T,Q$ 是共轭方向 | $\tau_g=0$ |

注意最后一行说明：曲率线方向的正交方向与它共轭，因为主方向正交且共轭。

## 主方向与 Euler 公式

在 $p$ 点取主方向正交基 $e_1,e_2$，令

$$
S(e_1)=\kappa_1 e_1,\qquad S(e_2)=\kappa_2 e_2.
$$

若

$$
T=\cos\theta\,e_1+\sin\theta\,e_2,
$$

并令

$$
Q=-\sin\theta\,e_1+\cos\theta\,e_2,
$$

则有

$$
\boxed{k_n(\theta)=\kappa_1\cos^2\theta+\kappa_2\sin^2\theta}
$$

这就是 Euler 公式。

同时

$$
\boxed{\tau_g(\theta)=(\kappa_2-\kappa_1)\sin\theta\cos\theta}
$$

符号可能随 $Q=N\times T$ 或 $T\times N$ 的约定变化，但零点不变。

因此：

- $k_n=0$ 给渐近方向；
- $\tau_g=0$ 给主方向；
- $k_n$ 的最大最小值给主曲率；
- 达到最大最小的方向给主方向。


## 点的分类

点的类型也由形算子 $S$ 或两个主曲率 $\kappa_1,\kappa_2$ 决定。Do Carmo 用 Gauss 映射微分 $dN_p$ 分类点；等价地说，就是看 $S_p=-dN_p$ 的特征值。[^1]


| 点类型 | 条件 | 渐近方向 |
| :-- | :-- | :-- |
| 椭圆点 | $K=\kappa_1\kappa_2>0$ | 无 |
| 双曲点 | $K=\kappa_1\kappa_2<0$ | 两条 |
| 抛物点 | $K=0$，但 $S\neq 0$ | 一条 |
| 平面点 | $\kappa_1=\kappa_2=0$ | 所有方向 |
| 脐点 | $\kappa_1=\kappa_2$ | 所有方向都是主方向 |

其中

$$
K=\det S=\kappa_1\kappa_2
$$

是 Gauss 曲率，

$$
H=\frac{1}{2}\operatorname{tr}S=\frac{\kappa_1+\kappa_2}{2}
$$

是平均曲率。

## 平面与密切平面

曲线自身有 Frenet 标架

$$
\{T,n,B\}.
$$

曲面给它 Darboux 标架

$$
\{T,Q,N\}.
$$

二者关系由

$$
T'=kn=k_gQ+k_nN
$$

控制。

因此主法向 $n$ 是 $Q,N$ 平面里的某个方向：

$$
n=\frac{k_g}{k}Q+\frac{k_n}{k}N.
$$

曲线的密切平面是

$$
\operatorname{span}\{T,n\}.
$$

曲面的切平面是

$$
\operatorname{span}\{T,Q\}.
$$

法截面平面是

$$
\operatorname{span}\{T,N\}.
$$

所以：


| 情况 | 平面关系 |
| :-- | :-- |
| $k_n=0$ 渐近曲线 | 密切平面等于切平面 |
| $k_g=0$ 测地线 | 密切平面等于法截面平面 |
| $k_g/k=\text{常数}$ | 密切平面与切平面成常角 |
| $k_n/k=\text{常数}$ | 主法向与曲面法向成常角 |

这就是前面练习 3-2,10 里的逻辑来源。

## 最小词典

最后给你一个最实用的“Do Carmo 词典”：


| 概念 | 一句话定义 | 公式判据 |
| :-- | :-- | :-- |
| Gauss 映射 | 给每点取单位法向 | $N:S\to S^2$ |
| Weingarten 映射 | 法向变化的负号 | $S=-dN$ |
| 第二基本形式 | 形算子的二次型 | $\mathrm{II}(u,v)=\langle S(u),v\rangle$ |
| 法曲率 | 某方向的法向弯曲 | $k_n=\mathrm{II}(T,T)$ |
| 主曲率 | 法曲率极值 | $\kappa_1,\kappa_2$ |
| 主方向 | 法曲率取极值方向 | $S(T)=\kappa T$ |
| 曲率线 | 处处切于主方向 | $\tau_g=0$ |
| 渐近方向 | 法曲率为零方向 | $\mathrm{II}(T,T)=0$ |
| 渐近曲线 | 处处切于渐近方向 | $k_n=0$ |
| 测地线 | 曲面内不拐弯 | $k_g=0$ |
| 共轭方向 | 第二基本形式正交 | $\mathrm{II}(u,v)=0$ |
| 脐点 | 两个主曲率相等 | $\kappa_1=\kappa_2$ |
| 平面点 | 形算子为零 | $S=0$ |
| 椭圆点 | $K>0$ | 无渐近方向 |
| 双曲点 | $K<0$ | 两条渐近方向 |
| 抛物点 | $K=0,S\neq0$ | 一条渐近方向 |
| 最小曲面 | 平均曲率为零 | $H=0$ |

你可以把整章理解为一句话：

$$
\boxed{
\text{所有特殊曲线，都是 } k_g,k_n,\tau_g \text{ 或 } S \text{ 的特殊取值。}
}
$$

其中 $k_g$ 属于曲面内在几何，$k_n,\tau_g$ 来自曲面嵌入到 $\mathbb{R}^3$ 后的外在几何。
<span style="display:none">[^2]</span>

<div align="center">⁂</div>

[^1]: Do-Carmo-Differential-Geometry-of-Curves-and-Surfaces.md

[^2]: Wei-Fen-Ji-He-Li-Jun-Bin-z-library.sk-1lib.sk-z-lib.sk-_full.md

