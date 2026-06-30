# Causal CN 符号与定义总表

> 来源：本表依据 `notes/peng-ding-causal-cn` 的中文译本 `.tex` 源文件整理，重点覆盖 $\tau$ 相关因果效应、混杂/可忽略性/敏感性分析，以及常见估计量。表中“语境”很重要：同一个符号在随机实验、观测研究、工具变量、RDD、mediation、time-varying treatment 中含义会变化。

## 快速索引

| 关注点 | 先看哪些符号 |
|---|---|
| 平均因果效应 | $\tau$, $\tau_i$, $\tau(X)$, $\tau_x$, $\tau_{[k]}$ |
| 处理组/对照组目标量 | $\tau_\mathrm{T}$, $\tau_\mathrm{C}$, $\tau_\mathrm{PF}$, $\tau^h$, $\tau_\mathrm{O}$ |
| 分层与条件效应 | $\tau_{[k]}$, $\hat\tau_\mathrm{S}$, $\pi_{[k]}$, $e_{[k]}$, $\tau_\mathrm{T}(X)$, $\tau_\mathrm{C}(X)$ |
| 分布/分位数效应 | $\mathrm{DCE}_y$, $\mathrm{QCE}_q$, $\tau_q$ |
| 工具变量与依从者 | $Z$, $D$, $U$, $\mathrm{a}$, $\mathrm{c}$, $\mathrm{d}$, $\mathrm{n}$, $\tau_D$, $\tau_Y$, $\tau_{\mathrm{c}}$ |
| RDD/FRDD | $X$, $x_0$, $R_i$, $L_i$, $\tau(x_0)$, $\tau_\mathrm{c}(x_0)$ |
| 混杂与可忽略性 | $X$, $U$, $Z \perp\!\!\!\perp Y(z)\mid X$, $e(X)$, overlap/positivity |
| 敏感性分析 | $\mathrm{RR}_{ZU\mid x}$, $\mathrm{RR}_{UY\mid x}$, E-value, $\varepsilon_1(X)$, $\varepsilon_0(X)$, $\Gamma$ |
| 估计量 | $\hat\tau$, $\hat\tau^\mathrm{ht}$, $\hat\tau^\mathrm{hajek}$, $\hat\tau^\mathrm{reg}$, $\hat\tau^\mathrm{dr}$, matching estimators |
| 后处理变量 | $M$, $M(z)$, $\tau(m_1,m_0)$, $\mathrm{NDE}$, $\mathrm{NIE}$, $\mathrm{CDE}(m)$ |
| 时间变处理 | $X_0$, $Z_1$, $X_1$, $Z_2$, $Y(z_1,z_2)$, MSM, SNM |

## 0. 全书通用记号

| 符号 | 名称/读法 | 定义 | 语境与注意事项 | 主要出处 |
|---|---|---|---|---|
| $Z$ | treatment/exposure/explanatory variable | 处理、暴露或解释变量；二元时 $Z=1$ 表示处理，$Z=0$ 表示对照 | 在 IV 章节中常表示 assignment/instrument，而实际接受 treatment 是 $D$；不要把二者混同 | `frontmatter/notation.tex`; Ch2, Ch21 |
| $D$ | treatment received | 实际接受的 treatment | 在 noncompliance/IV/FRDD/MR 中是被 $Z$ 影响的内生处理变量 | Ch21; Ch23; Ch24; Ch25 |
| $Y$ | outcome | 观测结果变量 | 在 potential outcomes 框架中，$Y$ 是由 $Y(1),Y(0)$ 与 $Z$ 决定的观测值 | Ch2 |
| $X$ | covariates/running/strata variable | 协变量、分层变量；RDD 中是 running variable | 在不同章节中角色不同：观测研究中用于调整混杂，RDD 中决定 cutoff 附近的处理，SRE 中定义 strata | notation; Ch10; Ch20 |
| $i$ | unit index | 个体/实验单元编号，通常 $i=1,\ldots,n$ | 实验单元不一定等同 physical person；同一个人在不同时间可以是不同 experimental units | Ch2 |
| $n,n_1,n_0$ | sample sizes | $n$ 总单元数；$n_1$ 处理组数量；$n_0$ 对照组数量 | CRE 中固定 $n_1,n_0$；BRE 中它们可随机 | Ch3; Ch4 |
| $n_{[k]},n_{[k]1},n_{[k]0}$ | stratum sample sizes | 第 $k$ 层总数、处理组数、对照组数 | SRE/stratification 中使用；若某层 $n_{[k]1}$ 或 $n_{[k]0}$ 为 0，则该层均值差不可定义 | Ch5; Ch10 |
| $\pi_{[k]}$ | stratum proportion | $n_{[k]}/n$ | 把各层效应加权成总体效应：$\tau=\sum_k\pi_{[k]}\tau_{[k]}$ | Ch5 |
| $e_{[k]}$ | stratum treatment fraction | $n_{[k]1}/n_{[k]}$ | SRE 中固定；也可视作离散分层语境下的 propensity score | Ch5 |
| $I(\cdot)$ / $1(\cdot)$ | indicator function | 条件成立取 1，否则取 0 | 文中两种写法混用；RDD/加权公式/分层公式常见 | Ch2; Ch11; Ch20 |
| $\Pr(\cdot)$ | probability | 概率 | 译本中定义为 $\Pr$ | notation |
| $\operatorname{var}(\cdot)$ | variance | 方差 | 有限总体章节中 $\operatorname{var}$ 是对 treatment assignment 随机性取方差；超总体中则对抽样/总体分布取方差 | notation; Ch4; Ch9 |
| $\operatorname{cov}(\cdot,\cdot)$ | covariance | 协方差 | 回归、混杂偏差、IV 中常出现 | notation; Ch1; Ch16; Ch23 |
| $\perp\!\!\!\perp$ / $\not\!\perp\!\!\!\perp$ | independence / non-independence | 独立/条件独立；$\not\!\perp\!\!\!\perp$ 表示不独立 | 可忽略性、随机化、IV 有效性都用条件独立表达 | Ch1; Ch10; Ch16 |
| $\mathrm{RD},\mathrm{RR},\mathrm{OR}$ | risk difference, risk ratio, odds ratio | 二元变量关联尺度：风险差、风险比、优势比 | 属于 association measure；只有在因果识别假设下才可作因果解释 | Ch1; notation |
| $\rho_{ZY}$ | Pearson correlation coefficient | $\operatorname{cov}(Z,Y)/\sqrt{\operatorname{var}(Z)\operatorname{var}(Y)}$ | 关联/线性依赖尺度，不是因果效应 | Ch1 |
| $\beta,\gamma,\alpha$ | regression/model coefficients | 回归或工作模型参数 | 含义随模型而变；不能自动解释为 causal effect，除非识别假设和模型条件成立 | Ch1; Ch10; Ch23; Ch25 |
| $\mu_z(X)$ | conditional outcome mean | $\mu_1(X)=E(Y\mid Z=1,X)$, $\mu_0(X)=E(Y\mid Z=0,X)$ | 在 ignorability 下也等于 $E\{Y(z)\mid X\}$；DR/OR/IPW 推导的核心对象 | Ch12 |
| $e(X)$ | propensity score | $\Pr(Z=1\mid X)$ | 强可忽略性下的倾向得分；同时用于降维、加权、overlap 判断 | Ch11 |
| $o(X)$ | odds of treatment | $e(X)/(1-e(X))$ | ATT 的 IPW/DR 公式常用 | Ch13 |

## 0.1. 教材 LaTeX alias 对照表

> 这一节专门处理源码里的宏别名。正文表格尽量使用更标准、可在 Markdown/MathJax 中直接渲染的写法；若你回到 `.tex` 源文件搜索，可以用“教材源码写法”这一列。

| 教材源码写法 | 本表标准写法 | 教材定义/展开 | 语境与提醒 |
|---|---|---|---|
| $\text{\textbackslash{}ind}$ | $\perp\!\!\!\perp$ | 自定义 picture 符号 | 独立/条件独立；如 $Z\perp\!\!\!\perp Y(z)\mid X$ |
| $\text{\textbackslash{}nind}$ | $\not\!\perp\!\!\!\perp$ | 自定义 picture 加斜杠 | 不独立/条件不独立 |
| $\text{\textbackslash{}pr}$ | $\Pr$ | $\text{\textbackslash{}textup\{pr\}}$ | 概率；本表用更常见的 $\Pr$ |
| $\text{\textbackslash{}var}$ | $\operatorname{var}$ | $\text{\textbackslash{}textup\{var\}}$ | 方差 |
| $\text{\textbackslash{}cov}$ | $\operatorname{cov}$ | $\text{\textbackslash{}textup\{cov\}}$ | 协方差 |
| $\text{\textbackslash{}RD}$ | $\mathrm{RD}$ | $\text{\textbackslash{}textsc\{rd\}}$ | risk difference |
| $\text{\textbackslash{}RR}$ | $\mathrm{RR}$ | $\text{\textbackslash{}textsc\{rr\}}$ | risk ratio/relative risk |
| $\text{\textbackslash{}OR}$ | $\mathrm{OR}$ | $\text{\textbackslash{}textsc\{or\}}$ | odds ratio |
| $\text{\textbackslash{}true}$ | $\mathrm{true}$ | $\text{\textbackslash{}textup\{true\}}$ | true causal $\mathrm{RR}$ 等下标/上标 |
| $\text{\textbackslash{}obs}$ | $\mathrm{obs}$ | $\text{\textbackslash{}textup\{obs\}}$ | observed $\mathrm{RR}$ 等下标/上标 |
| $\text{\textbackslash{}at}$ | $\mathrm{a}$ | $\text{\textbackslash{}textup\{a\}}$ | always taker 的 principal stratum |
| $\text{\textbackslash{}cp}$ | $\mathrm{c}$ | $\text{\textbackslash{}textup\{c\}}$ | complier 的 principal stratum；如 $\tau_{\mathrm{c}}$ |
| $\text{\textbackslash{}df}$ | $\mathrm{d}$ | $\text{\textbackslash{}textup\{d\}}$ | defier 的 principal stratum；注意也和微分 $\mathrm{d}$ 同形 |
| $\text{\textbackslash{}nt}$ | $\mathrm{n}$ | $\text{\textbackslash{}textup\{n\}}$ | never taker 的 principal stratum |
| $\text{\textbackslash{}CDE}$ | $\mathrm{CDE}$ | $\text{\textbackslash{}textsc\{cde\}}$ | controlled direct effect |
| $\text{\textbackslash{}NDE}$ | $\mathrm{NDE}$ | $\text{\textbackslash{}textsc\{nde\}}$ | natural direct effect |
| $\text{\textbackslash{}NIE}$ | $\mathrm{NIE}$ | $\text{\textbackslash{}textsc\{nie\}}$ | natural indirect effect |
| $\text{\textbackslash{}HF}$ | $H_{0\mathrm{F}}$ | $\text{H\_\{0\textbackslash{}textsc\{f\}\}}$ | Fisher sharp null |
| $\text{\textbackslash{}HN}$ | $H_{0\mathrm{N}}$ | $\text{H\_\{0\textbackslash{}textsc\{n\}\}}$ | Neyman null |
| $\text{\textbackslash{}frt}$ | $\mathrm{FRT}$ | $\text{\textbackslash{}textsc\{frt\}}$ | Fisher randomization test |
| $\text{\textbackslash{}tran}$ | ${}^{\mathsf T}$ | ${}^{\mkern-1.5mu\mathsf{T}}$ | 向量/矩阵转置 |
| $\text{\textbackslash{}sumn}$ | $\sum_{i=1}^n$ | $\sum_{i=1}^n$ | 教材常用求和缩写；本表展开为显式求和 |
| $\text{\textbackslash{}summ}$ | $\sum_{j=1}^m$ | $\sum_{j=1}^m$ | mediation 公式中对 mediator 水平求和时常见 |
| $\text{\textbackslash{}AVar}$ | $\operatorname{AsyVar}$ | $\text{\textbackslash{}text\{AsyVar\}}$ | 渐近方差 |
| $\text{\textbackslash{}convergeas}$ | $\stackrel{\mathrm{a.s.}}{\longrightarrow}$ | $\text{\textbackslash{}stackrel\{a.s.\}\{\textbackslash{}longrightarrow\}}$ | almost sure convergence |
| $\text{\textbackslash{}converged}$ | $\stackrel{\mathrm{d}}{\longrightarrow}$ | $\text{\textbackslash{}stackrel\{\textbackslash{}textup\{d\}\}\{\textbackslash{}longrightarrow\}}$ | convergence in distribution |
| $\text{\textbackslash{}iidsim}$ | $\stackrel{\mathrm{IID}}{\sim}$ | $\text{\textbackslash{}stackrel\{\textbackslash{}textup\{IID\}\}\{\textbackslash{}sim\}}$ | 独立同分布抽样 |
| $\text{\textbackslash{}indsim}$ | $\stackrel{\mathrm{ind}}{\sim}$ | $\stackrel{ind}{\sim}$ | 独立但不一定同分布 |
| $\text{\textbackslash{}asim}$ | $\stackrel{\cdot}{\sim}$ | $\stackrel{\cdot}{\sim}$ | 同渐近分布；ReM/渐近推断中出现 |
| $\text{\textbackslash{}letas}$ | $\mathrel{\mathop{=}\limits^\triangle}$ | $\mathrel{\mathop{=}\limits^{\triangle}}$ | “定义为”的教材写法 |
| $\text{\textbackslash{}d}$, $\text{\textbackslash{}diff}$ | $\mathrm{d}$ | $\text{\textbackslash{}textnormal\{d\}}$ / $\text{\textbackslash{}textup\{d\}}$ | 积分微分符号；不要与 defier 的 $\mathrm{d}$ 混淆 |
| $\text{\textbackslash{}N01}$ | $\mathrm{N}(0,1)$ | $\text{\textbackslash{}textsc\{N\}(0,1)}$ | 标准正态分布 |
| $\text{\textbackslash{}logit}$ | $\operatorname{logit}$ | $\text{\textbackslash{}textup\{logit\}}$ | $\operatorname{logit}(w)=\log\{w/(1-w)\}$ |
| $\text{\textbackslash{}expit}$ | $\operatorname{expit}$ | $\text{\textbackslash{}textup\{expit\}}$ | $\operatorname{expit}(w)=1/(1+e^{-w})$ |
| $\text{\textbackslash{}se}$ | $\operatorname{se}$ | $\text{\textbackslash{}textup\{se\}}$ | 标准误 |
| $\text{\textbackslash{}L}$ | $\ell$ | $\ell$ | 小写 ell；似然/损失等语境中使用 |
| $\text{\textbackslash{}U}$ | $u$ | $u$ | 小写 $u$；不要与未测混杂 $U$ 的大写符号混淆 |
| $\text{\textbackslash{}G}$ | $\Gamma$ | $\text{\textbackslash{}text\{Gamma\}}$ | 源码用文字 Gamma；敏感性参数通常写作 $\Gamma$ |

## 1. Potential Outcomes 与基础 $\tau$ 家族

| 符号 | 名称 | 定义 | 语境/解释 | 不要混淆 | 出处 |
|---|---|---|---|---|---|
| $Y_i(1),Y_i(0)$ | potential outcomes | unit $i$ 在处理/对照两个干预水平下的潜在结果 | 在 SUTVA 下 well-defined；一人只能观测其中一个 | 不是两个观测值；另一个通常是 counterfactual | Ch2 |
| $Y_i$ | observed outcome | $Y_i=Z_iY_i(1)+(1-Z_i)Y_i(0)$ | 连接潜在结果和观测结果的 fundamental bridge | 不等同于 $Y_i(1)$ 或 $Y_i(0)$ 的固定一个，取决于 $Z_i$ | Ch2 |
| $Y_i^\mathrm{mis}$ | missing potential outcome | 若 $Z_i=1$ 则为 $Y_i(0)$；若 $Z_i=0$ 则为 $Y_i(1)$ | 反事实/缺失潜在结果 | “实验前两个都可能观测”与“实验后一个反事实”要区分 | Ch2 |
| $\tau_i$ | individual causal effect | $Y_i(1)-Y_i(0)$ | 个体因果效应；允许 treatment effect heterogeneity | 通常无法识别，因为两个潜在结果不能同时观测 | Ch2; Ch4 |
| $\tau$ | ACE/ATE, finite-population average causal effect | $n^{-1}\sum_{i=1}^n\{Y_i(1)-Y_i(0)\}=\bar Y(1)-\bar Y(0)$ | 在有限总体随机实验中是 Science Table 的函数 | 与超总体 $E\{Y(1)-Y(0)\}$ 同符号但随机性来源不同 | Ch2; Ch4 |
| $\tau$ | population average causal effect | $E\{Y(1)-Y(0)\}$ | 超总体/观测研究中常用；省略下标 $i$ | 与有限总体平均同符号；要看章节语境 | Ch9; Ch10; Ch12 |
| $\tau_x$ | subgroup causal effect | $\sum_{i=1}^n I(X_i=x)\{Y_i(1)-Y_i(0)\}\big/\sum_{i=1}^n I(X_i=x)$ | 由二元 subgroup variable $X_i$ 定义的组内平均因果效应 | $x$ 是 subgroup 值，不是 treatment level | Ch2 |
| $\pi_x$ | subgroup proportion | $n^{-1}\sum_{i=1}^n I(X_i=x)$ | 满足 $X_i=x$ 的单元比例；$\tau=\pi_1\tau_1+\pi_0\tau_0$ | 不是 propensity score | Ch2 |
| $\tau(X)$ | CATE | $E\{Y(1)-Y(0)\mid X\}$ | 条件平均因果效应；观测研究识别、加权 estimand 的核心 | 不同于 $\tau_x$ 的有限总体 subgroup 记法，但思想相近 | Ch10; Ch13 |
| $\tau_{[k]}$ | stratum-specific causal effect | $E\{Y(1)-Y(0)\mid X=k\}$ 或有限总体第 $k$ 层效应 | SRE/分层/超总体章节中使用 | 方括号 $[k]$ 表示 stratum，不是函数值 | Ch5; Ch9 |
| $\hat\tau_{[k]}$ | stratum-specific difference-in-means | 第 $k$ 层内处理均值减对照均值 | SRE 的层内估计量；用于构造总体分层估计量 | 层内需同时有 treated 与 control units | Ch5 |
| $\hat\tau_\mathrm{S}$ | stratified estimator | $\sum_{k=1}^K\pi_{[k]}\hat\tau_{[k]}$ | SRE 中估计 $\tau=\sum_k\pi_{[k]}\tau_{[k]}$；FRT 中也可作 statistic | 与简单 $\hat\tau$ 相比，显式使用层权重 | Ch5 |
| $\hat V_\mathrm{S}$ | stratified variance estimator | $\sum_k\pi_{[k]}^2{\hat S^2_{[k]}(1)/n_{[k]1}+\hat S^2_{[k]}(0)/n_{[k]0}}$ | SRE 下 $\hat\tau_\mathrm{S}$ 的 Neyman 型保守方差估计 | 层内样本量太小时可能不稳定 | Ch5 |
| $\hat\tau$ | difference-in-means estimator | $\hat{\bar Y}(1)-\hat{\bar Y}(0)$ | CRE 下估计 $\tau$；FRT 中也可作检验统计量 | 在 FRT sharp null 下是 statistic；Neyman 推断中是 estimator | Ch3; Ch4 |
| $S^2(1),S^2(0)$ | finite population variances | $Y_i(1)$、$Y_i(0)$ 的有限总体方差 | Neyman 方差公式中的固定 Science Table 量 | 不是样本方差；样本版本写作 $\hat S^2(z)$ | Ch4 |
| $S(1,0)$ | finite population covariance | $Y_i(1)$ 与 $Y_i(0)$ 的有限总体协方差 | 不能由数据识别，因为同一 unit 不能同时观测两个潜在结果 | 与样本协方差不同 | Ch4 |
| $S^2(\tau)$ | effect heterogeneity variance | $(\tau_i-\tau)^2$ 的有限总体方差 | Neyman variance conservativeness 的缺失项 | 越大时保守方差与真实方差差距越大 | Ch4 |
| $\hat V$ | Neyman conservative variance estimator | $\hat S^2(1)/n_1+\hat S^2(0)/n_0$ | 估计 $\operatorname{var}(\hat\tau)$，期望多出 $S^2(\tau)/n$ | 不能识别 sharp 的真实方差除非常数效应 | Ch4 |

## 2. 观测研究中的 $\tau$、选择偏差与识别

| 符号 | 名称 | 定义 | 语境/解释 | 条件/注意事项 | 出处 |
|---|---|---|---|---|---|
| $\tau_\mathrm{T}$ | ATT | $E\{Y(1)-Y(0)\mid Z=1\}$ | treated units 上的平均因果效应 | 目标人群是已接受 treatment 的 units | Ch10; Ch13 |
| $\tau_\mathrm{C}$ | ATC | $E\{Y(1)-Y(0)\mid Z=0\}$ | control units 上的平均因果效应 | 目标人群是 controls | Ch10; Ch13 |
| $\tau_\mathrm{PF}$ | prima facie causal effect | $E(Y\mid Z=1)-E(Y\mid Z=0)$ | 观测均值差；“表面”因果效应 | 通常有 selection bias；随机化下才等于因果效应 | Ch10 |
| $\tau_\mathrm{T}(X)$ | conditional ATT | $E\{Y(1)-Y(0)\mid Z=1,X\}$ | 给定 $X$ 后 treated units 的条件平均因果效应 | 在均值可忽略性下等于 $\tau(X)$ 和 $\tau_\mathrm{PF}(X)$ | Ch10 |
| $\tau_\mathrm{C}(X)$ | conditional ATC | $E\{Y(1)-Y(0)\mid Z=0,X\}$ | 给定 $X$ 后 control units 的条件平均因果效应 | 在均值可忽略性下等于 $\tau(X)$ 和 $\tau_\mathrm{PF}(X)$ | Ch10 |
| $\tau_\mathrm{PF}(X)$ | conditional prima facie effect | $E(Y\mid Z=1,X)-E(Y\mid Z=0,X)$ | 给定协变量后的观测条件均值差 | 在均值可忽略性下等于 $\tau(X)$ | Ch10 |
| selection bias for ATT | selection bias | $\tau_\mathrm{PF}-\tau_\mathrm{T}=E\{Y(0)\mid Z=1\}-E\{Y(0)\mid Z=0\}$ | 处理组与对照组在 control potential outcome 上的差异 | 随机化下为 0；观测研究中通常不为 0 | Ch10 |
| selection bias for ATC | selection bias | $\tau_\mathrm{PF}-\tau_\mathrm{C}=E\{Y(1)\mid Z=1\}-E\{Y(1)\mid Z=0\}$ | 两组在 treated potential outcome 上的差异 | 衡量 treatment group/control group 潜在结果分布不同 | Ch10 |
| $Z\perp\!\!\!\perp{Y(1),Y(0)}$ | randomization | treatment 与潜在结果独立 | CRE/随机实验的根本平衡性质 | 保证 $\tau=\tau_{\mathrm{T}}=\tau_{\mathrm{C}}=\tau_{\mathrm{PF}}$ | Ch9; Ch10 |
| mean ignorability | mean independence | $E\{Y(0)\mid Z=1,X\}=E\{Y(0)\mid Z=0,X\}$ 且 $E\{Y(1)\mid Z=1,X\}=E\{Y(1)\mid Z=0,X\}$ | 保证条件均值层面无选择偏差 | 识别平均因果效应足够，但不一定识别分布/分位数效应 | Ch10 |
| weak ignorability | weak ignorability | $Z\perp\!\!\!\perp Y(0)\mid X$ 和 $Z\perp\!\!\!\perp Y(1)\mid X$ | 比均值条件强；用条件独立表达 | 对平均效应足够但不总是必要 | Ch10 |
| strong ignorability | strong ignorability | $Z\perp\!\!\!\perp{Y(1),Y(0)}\mid X$ 加 overlap | Rosenbaum--Rubin 经典条件 | 常同时包含 $0<e(X)<1$ | Ch10; Ch11 |
| unconfoundedness | 无混杂性 | 通常指 $Z\perp\!\!\!\perp{Y(1),Y(0)}\mid X$ | 直观含义：控制 $X$ 后没有未测共同原因 | 本质上不可直接检验 | Ch10; Ch16 |
| identification | 识别 | 参数可写成 observed data 分布的函数 | $\tau$ 在 ignorability 下可非参数识别 | 不需要 parametric model 时叫 nonparametric identification | Ch10 |
| partial identification | 部分识别 | 观测分布与参数多个取值相容 | 无 ignorability 但有 bounded outcome 时常得到 bounds | 与 point identification 相对 | Ch18 |
| g-formula | g-formula/outcome formula | $\tau=E\{E(Y\mid Z=1,X)-E(Y\mid Z=0,X)\}$ | 观测研究 outcome-regression 识别公式 | 需 mean ignorability/overlap 支撑条件均值 | Ch10 |
| $\mathrm{DCE}_y$ | distributional causal effect | $\Pr\{Y(1)>y\}-\Pr\{Y(0)>y\}$ | 比较两个潜在结果分布的 survival functions | ignorability 下可由边际潜在结果分布识别 | Ch10 |
| $\mathrm{QCE}_q$ | quantile causal effect | $\operatorname{quantile}_q{Y(1)}-\operatorname{quantile}_q{Y(0)}$ | 比较两个 marginal potential outcome distributions 的分位数 | 与个体效应分布的分位数不同 | Ch10 |
| $\tau_q$ | quantile of individual causal effects | $\operatorname{quantile}_q{Y(1)-Y(0)}$ | 个体因果效应 $Y(1)-Y(0)$ 的第 $q$ 分位数 | 一般不可识别，因为只知道两个边际分布不足以确定差值分布 | Ch10 |

## 3. Propensity Score、Overlap 与权重目标量

| 符号 | 名称 | 定义 | 语境/解释 | 注意事项 | 出处 |
|---|---|---|---|---|---|
| $e(X,Y(1),Y(0))$ | general propensity score | $\Pr\{Z=1\mid X,Y(1),Y(0)\}$ | 最一般的 treatment assignment probability | strong ignorability 下化简为 $e(X)$ | Ch11 |
| $e(X)$ | propensity score | $\Pr(Z=1\mid X)$ | 给定协变量后接受处理的概率 | 是一维标量；用于降维、分层、加权、matching | Ch11 |
| $\hat e(X_i)$ | estimated propensity score | 由 logistic 或其他 treatment model 拟合得到 | 实际估计量中使用 | 模型错设会影响 IPW/DR；估计 PS 的不确定性要考虑 | Ch11; Ch12 |
| dimension reduction property | PS 降维性质 | 若 $Z\perp\!\!\!\perp{Y(1),Y(0)}\mid X$，则 $Z\perp\!\!\!\perp{Y(1),Y(0)}\mid e(X)$ | 只需按 $e(X)$ 条件化即可去除由 $X$ 引起的混杂 | 依赖原始 $X$ 下 ignorability 成立 | Ch11 |
| overlap/positivity | 重叠/正性 | $0<e(X)<1$ | 保证两个处理水平在每个 $X$ 下都有机会出现 | $e(X)=0/1$ 时 counterfactual 可能极端甚至 ill-defined | Ch11 |
| strong overlap | 强重叠 | $0<\alpha_L\le e(X)\le\alpha_U<1$ | 渐近理论常用，避免权重爆炸 | 高维 $X$ 下很强；实际中常需 trimming/truncation | Ch11 |
| $\alpha_L,\alpha_U$ | truncation thresholds | 截断 estimated PS 的上下界 | 稳定 IPW 权重 | 会引入任意性并改变分析 | Ch11 |
| $\tau^h$ | weighted causal estimand | $E\{h(X)\tau(X)\}/E\{h(X)\}$ | Li 等统一的观测研究目标量家族 | $h(X)$ 改变目标总体 | Ch13 |
| $h(X)=1$ | ATE weighting | 对应 $\tau$ | combined population | treated 权重 $1/e(X)$，control 权重 $1/(1-e(X))$ | Ch13 |
| $h(X)=e(X)$ | ATT weighting | 对应 $\tau_{\mathrm{T}}$ | treated population | treated 权重 1，control 权重 $e(X)/(1-e(X))$ | Ch13 |
| $h(X)=1-e(X)$ | ATC weighting | 对应 $\tau_{\mathrm{C}}$ | control population | treated 权重 $(1-e(X))/e(X)$，control 权重 1 | Ch13 |
| $h_\mathrm{O}(X)=e(X)\{1-e(X)\}$ | overlap weights | 对应 overlap population | 对 $e(X)=1/2$ 附近单位赋最大权重 | 目标量是 $\tau_{\mathrm{O}}$，不是原始全体 ATE | Ch13; Ch14 |
| $\tau_\mathrm{O}$ | overlap-weighted causal effect | $E[e(X)\{1-e(X)\}\tau(X)] / E[e(X)\{1-e(X)\}]$ | 关注 overlap 最好的 population | 若 $e(X)\perp\!\!\!\perp\tau(X)$ 或效应常数，则等于 $\tau$ | Ch13; Ch14 |
| $r(X)$ | reduced covariate/score | $X$ 的某个低维函数 | no-overlap 章节中若 $e(X)$ 缺乏 overlap，可考虑在 $r(X)$ 上识别 | 目标和假设随 $r$ 改变；不能机械等同完整 $X$ 调整 | Ch20 |
| $e(r(X))$ | propensity score on reduced score | $\Pr\{Z=1\mid r(X)\}$ | 在 $r(X)$ 上的 IPW/overlap 公式使用 | 当 $r(X)=X$ 时退化为标准 PS 公式 | Ch20 |

## 4. 常用估计量总表

| 符号 | 名称 | 定义/构造 | 估计目标 | 关键条件 | 出处 |
|---|---|---|---|---|---|
| $\hat\tau$ | difference-in-means | $\hat{\bar Y}(1)-\hat{\bar Y}(0)$ | CRE 中的 $\tau$；也可作 FRT statistic | CRE 下无偏；方差由 Neyman 公式刻画 | Ch3; Ch4 |
| $\hat\tau_\mathrm{F}$ | Fisher ANCOVA estimator | OLS $Y_i$ 对 $(1,Z_i,X_i)$ 回归中 $Z_i$ 的系数 | CRE 中 ATE | 可提高/降低效率；finite sample 有 bias；需 EHW SE | Ch6 |
| $\hat\tau_\mathrm{L}$ | Lin estimator | OLS $Y_i$ 对 $(1,Z_i,X_i,Z_iX_i)$ 回归中 $Z_i$ 的系数，通常 $X$ 中心化 | CRE 中 ATE | 大样本效率好；EHW SE 保守 | Ch6; Ch9 |
| $\hat\tau(\beta_1,\beta_0)$ | linearly adjusted estimator | 两组分别用 $\beta_z$ 调整 outcome 后的均值差 | CRE 中 ATE | 固定 $\beta$ 时无偏；选择好可降方差 | Ch6 |
| $\hat\tau_\mathrm{pred}$ | predictive estimator | 用模型预测 missing/counterfactual outcomes，再与 observed outcomes 组合 | ATE | 依赖 outcome model；CRE/观测研究中形式不同 | Ch6; Ch14; Ch18 |
| $\hat\tau_\mathrm{proj}$ | projective estimator | 对所有 units 的 $\hat\mu_1(X_i)-\hat\mu_0(X_i)$ 求平均 | ATE | outcome model 正确时一致 | Ch6; Ch18 |
| $\hat\tau^\mathrm{reg}$ | outcome regression estimator | $n^{-1}\sum_{i=1}^n\{\hat\mu_1(X_i)-\hat\mu_0(X_i)\}$ | 观测研究 ATE | outcome model 正确时一致 | Ch10; Ch12 |
| $\hat\tau^\mathrm{ht}$ | HT/IPW estimator | $n^{-1}\sum_{i=1}^n Z_iY_i/\hat e(X_i)-n^{-1}\sum_{i=1}^n (1-Z_i)Y_i/\{1-\hat e(X_i)\}$ | ATE | PS model 正确；对 location shift 不 invariant，权重可爆炸 | Ch11 |
| $\widehat{1}_{\mathrm{T}},\widehat{1}_{\mathrm{C}}$ | HT normalizing factors | $n^{-1}\sum_{i=1}^n Z_i/\hat e(X_i)$, $n^{-1}\sum_{i=1}^n(1-Z_i)/(1-\hat e(X_i))$ | 常数 1 的两种估计 | 解释 HT 不 invariant 的原因 | Ch11 |
| $\hat\tau^\mathrm{hajek}$ | Hajek IPW estimator | 对 treated/control 的 IPW 均值分别规范化后相减 | ATE | 比 HT 更稳定；对 outcome location shift invariant | Ch11 |
| $\hat\tau^\mathrm{dr}$ | doubly robust/AIPW estimator | $\hat\tau^\mathrm{reg}$ 加上 treated/control residual 的 IPW 修正 | ATE | PS model 或 outcome model 至少一个正确时一致 | Ch12 |
| $\hat\mu_z^\mathrm{dr}$ | DR potential outcome mean estimator | $n^{-1}\sum_{i=1}^n [I(Z_i=z)\{Y_i-\hat\mu_z(X_i)\}/\hat p_z(X_i)+\hat\mu_z(X_i)]$ | $E\{Y(z)\}$ | DR 性质来自 residual augmentation | Ch12 |
| $\hat\tau_{\mathrm{T}}^\mathrm{reg}$ | ATT outcome regression estimator | $n_1^{-1}\sum_{i=1}^n Z_i\{Y_i-\hat\mu_0(X_i)\}$ | ATT | 只需建模 control outcome mean | Ch13 |
| $\hat\tau_{\mathrm{T}}^\mathrm{ht}$ | ATT HT estimator | $\hat{\bar Y}(1)-n_1^{-1}\sum_{i=1}^n \hat o(X_i)(1-Z_i)Y_i$ | ATT | $\hat o(X)=\hat e(X)/(1-\hat e(X))$ | Ch13 |
| $\hat\tau_{\mathrm{T}}^\mathrm{hajek}$ | ATT Hajek estimator | $\hat{\bar Y}(1)- \sum_{i=1}^n \hat o(X_i)(1-Z_i)Y_i / \sum_{i=1}^n \hat o(X_i)(1-Z_i)$ | ATT | 更稳定的 odds-weighted control mean | Ch13 |
| $\hat\tau_{\mathrm{T}}^\mathrm{dr}$ | ATT DR estimator | $\hat{\bar Y}(1)-\hat\mu_{0\mathrm{T}}^\mathrm{dr}$ | ATT | PS model 或 control outcome model 正确时一致 | Ch13 |
| $\hat\tau^m$ | matching estimator | 填补每个 unit 缺失 potential outcome 后取平均差 | ATE | matching with replacement；高维 $X$ 下有 bias | Ch15 |
| $\hat B$ | matching bias estimate | 基于 $\hat\mu_{1-Z_i}(X_i)-\hat\mu_{1-Z_i}(X_k)$ 的匹配偏差估计 | matching bias | 校正不完全匹配导致的 bias | Ch15 |
| $\hat\tau^\mathrm{mbc}$ | bias-corrected matching estimator | $\hat\tau^m-\hat B$ | ATE | AI matching estimator；可写成 outcome regression 加 residual 修正 | Ch15 |
| $K_i$ | matching reuse count | unit $i$ 被用作匹配对象的次数 | matching linear expansion | $1+K_i/M$ 类似非参数估计的 inverse PS 权重 | Ch15 |
| $\hat\psi_i$ | matching influence-style term | $\hat\mu_1(X_i)-\hat\mu_0(X_i)+(2Z_i-1)(1+K_i/M)\{Y_i-\hat\mu_{Z_i}(X_i)\}$ | $\hat\tau^\mathrm{mbc}$ 的线性展开 | 用于方差估计 | Ch15 |
| $\hat\tau_{\mathrm{T}}^\mathrm{m}$ | matching ATT estimator | $n_1^{-1}\sum_{i=1}^n Z_i\{Y_i-\hat Y_i(0)\}$ | ATT | 只为 treated units 填补 control outcome | Ch15 |
| $\hat\tau_{\mathrm{T}}^\mathrm{mbc}$ | bias-corrected matching ATT | $\hat\tau_{\mathrm{T}}^\mathrm{m}-\hat B_{\mathrm{T}}$ | ATT | 有 linear expansion 与 DR 类似 | Ch15 |
| $\hat V^\mathrm{mbc}$ | matching variance estimator | $n^{-2}\sum_{i=1}^n(\hat\psi_i-\hat\tau^\mathrm{mbc})^2$ | matching ATE 方差 | 简单 bootstrap 对 matching estimator 本身不可靠；线性展开可用 | Ch15 |

## 5. 混杂、诊断与 over-adjustment

| 符号/概念 | 定义 | 语境 | 关键提醒 | 出处 |
|---|---|---|---|---|
| confounder / 混杂因子 | 同时影响 treatment 与 outcome 的 common cause | Yule--Simpson 悖论、观测研究 | $X$ 若同时关联 $Z$ 与 $Y$，边际与条件关联方向可能相反 | Ch1; Ch10 |
| $U$ | unmeasured confounder | 未观测混杂因子 | 若 $Z\perp\!\!\!\perp Y(z)\mid(X,U)$ 但 $Z\not\!\perp\!\!\!\perp Y(z)\mid X$，则仅控制 $X$ 不够 | Ch16; Ch17 |
| $X$ as sufficient covariates | 足以消除混杂的协变量集合 | $Z\perp\!\!\!\perp Y(z)\mid X$ | 关键是选对 $X$，不是越多越好 | Ch16 |
| negative outcome $Y^\mathrm{n}$ | negative outcome | 与 $Y$ 有相似 confounding structure，但已知 $Z$ 对其效应应为 0 | 若估出非零效应，提示 unmeasured confounding | Ch16 |
| $\tau(Z\to Y^\mathrm{n})$ | negative outcome effect | $E\{Y^\mathrm{n}(1)-Y^\mathrm{n}(0)\}$ | 常希望为 0 | Ch16 |
| negative exposure $Z^\mathrm{n}$ | negative exposure | 与 $Z$ 共享 confounding structure，但已知对 $Y$ 无效应 | 与 negative outcome 对偶 | Ch16 |
| $\tau(Z^\mathrm{n}\to Y)$ | negative exposure effect | $E\{Y(1^\mathrm{n})-Y(0^\mathrm{n})\}$ | 常希望为 0 | Ch16 |
| covariate balance check | 协变量平衡检查 | PS 建模后检查 treated/control covariate balance | 失败通常 falsify PS model specification，不直接 falsify unconfoundedness | Ch16 |
| M-bias | M-structure adjustment bias | $U_1 -> X <- U_2$ 且 $U_1 -> Z$, $U_2 -> Y$ | 不调整 $X$ 时 $Z\perp\!\!\!\perp Y$；调整 collider $X$ 反而打开路径 | Ch16 |
| $\rho_{ZY\mid X}$ | partial correlation | 给定 $X$ 后 $Z,Y$ 的偏相关 | M-bias 正态线性例子中与 $-abcd$ 成比例 | Ch16 |
| Z-bias / IV bias | 调整 instrument-like covariate 放大 bias | $X -> Z -> Y$, $U -> Z,Y$ | $X$ 越强预测 $Z$，调整后 unmeasured confounder 在 $Z$ 中比重越大 | Ch16 |
| $\tau_\mathrm{unadj}$ | unadjusted linear effect | $\operatorname{cov}(Z,Y)/\operatorname{var}(Z)=\tau+cb/(a^2+b^2+1)$ | Z-bias 线性例子中的未调整估计极限 | Ch16 |
| $\tau_\mathrm{adj}$ | adjusted linear effect | $\tau+bc/(b^2+1)$ | Z-bias 中调整 $X$ 后 bias 更大 | Ch16 |
| $X_R$ | random noise covariate | 不影响 treatment/outcome | 纳入增加有限样本 variability | Ch16 |
| $X_Z$ | instrument-like covariate | 只通过 treatment 影响 outcome | 无 unmeasured confounding 时不致偏但增方差；有时会放大 bias | Ch16 |
| $X_Y$ | outcome predictor | 只影响 outcome 不影响 treatment | 可提高 precision，通常值得调整 | Ch16 |
| $X_I$ | post-treatment variable | 受 treatment 和 outcome 影响 | 推断 treatment 对 outcome 时不应作为 pretreatment covariate 调整 | Ch16 |

## 6. 敏感性分析符号

| 符号 | 名称 | 定义 | 语境/解释 | 出处 |
|---|---|---|---|---|
| latent ignorability | 潜在可忽略性 | $Z\perp\!\!\!\perp{Y(1),Y(0)}\mid(X,U)$ | 允许存在未测混杂 $U$，但假定控制 $U$ 后可忽略 | Ch17 |
| $\mathrm{RR}_{ZY\mid x}^\mathrm{true}$ | true conditional causal RR | $\Pr\{Y(1)=1\mid X=x\}/\Pr\{Y(0)=1\mid X=x\}$ | 二元 outcome 的真实条件因果风险比 | Ch17 |
| $\mathrm{RR}_{ZY\mid x}^\mathrm{obs}$ | observed conditional RR | $\Pr(Y=1\mid Z=1,X=x)/\Pr(Y=1\mid Z=0,X=x)$ | 受未测混杂影响的观测风险比 | Ch17 |
| $\mathrm{RR}_{ZU\mid x}$ | treatment-confounder association | $\Pr(U=1\mid Z=1,X=x)/\Pr(U=1\mid Z=0,X=x)$ | 混杂强度之一 | Ch17 |
| $\mathrm{RR}_{UY\mid x}$ | confounder-outcome association | $\Pr(Y=1\mid U=1,X=x)/\Pr(Y=1\mid U=0,X=x)$ | 混杂强度之一 | Ch17 |
| bounding factor | 上界因子 | $\mathrm{RR}_{ZU} \mathrm{RR}_{UY} /(\mathrm{RR}_{ZU}+\mathrm{RR}_{UY}-1)$ | 在 $Z\perp\!\!\!\perp Y\mid(X,U)$ 下约束 observed RR | Ch17 |
| E-value | E-value | $\mathrm{RR}_{\mathrm{obs}} + \sqrt{\mathrm{RR}_{\mathrm{obs}}(\mathrm{RR}_{\mathrm{obs}}-1)}$ | 解释掉 observed RR 所需的最大 confounding measure 至少达到的水平 | Ch17 |
| $f_{1,x}, f_{0,x}$ | confounder prevalence | $\Pr(U=1\mid Z=1,X=x)$, $\Pr(U=1\mid Z=0,X=x)$ | E-value identity 中的额外 sensitivity parameters | Ch17 |
| $\underline y,\overline y$ | outcome bounds | 结果变量上下界 | Manski worst-case bounds 中使用 | Ch18 |
| Manski bounds | worst-case bounds | 仅用 outcome 有界性约束 $E\{Y(1)\}$, $E\{Y(0)\}$ 与 $\tau$ | 无 ignorability 时只给 partial identification | Ch18 |
| monotonicity $Y(1)\ge Y(0)$ | 单调性假设 | treatment 不伤害任何 unit | 可把 $\tau$ 下界提升到 0 | Ch18 |
| $\varepsilon_1(X)$ | sensitivity parameter for $Y(1)$ | $E\{Y(1)\mid Z=1,X\}/E\{Y(1)\mid Z=0,X\}$ | outcome-regression sensitivity analysis 中刻画 treated/control counterfactual mean 差异 | Ch18 |
| $\varepsilon_0(X)$ | sensitivity parameter for $Y(0)$ | $E\{Y(0)\mid Z=1,X\}/E\{Y(0)\mid Z=0,X\}$ | 若等于 1 则回到 ignorability 的均值版本 | Ch18 |
| $w_1(X),w_0(X)$ | sensitivity IPW correction factors | $w_1=e(X)+{1-e(X)}/\varepsilon_1(X)$, $w_0=e(X)\varepsilon_0(X)+1-e(X)$ | 修正经典 IPW 公式以允许未测混杂 | Ch18 |
| $\Gamma$ | Rosenbaum sensitivity parameter | matched pair 内 treatment odds ratio 上界 | $\Gamma=1$ 回到 ideal MPE；越大表示越强 omitted variable 偏离 | Ch19 |
| $e_{ij}$ | matched-data propensity score | $\Pr\{Z_{ij}=1\mid X_i,Y_{ij}(1),Y_{ij}(0)\}$ | Rosenbaum matched sensitivity model | Ch19 |
| $o_{ij}$ | treatment odds in pair | $e_{ij}/(1-e_{ij})$ | 用于 pair 内 odds ratio bound | Ch19 |
| $\pi_{i1}$ | pair conditional treatment probability | $\Pr\{Z_{i1}=1\mid X_i,\mathbb S_i,Z_{i1}+Z_{i2}=1\}$ | ignorability 下为 1/2；Rosenbaum model 下在 $[1/(1+\Gamma),\Gamma/(1+\Gamma)]$ | Ch19 |
| $S_i$ | sign indicator | $I(\hat\tau_i>0)$ | Rosenbaum worst-case p-value 的 Bernoulli 随机量 | Ch19 |
| $T=\sum S_iq_i$ | sensitivity test statistic | sign/pair t/Wilcoxon 等统计量的一般形式 | worst-case distribution 下 $S_i \sim \operatorname{Bernoulli}(\Gamma/(1+\Gamma))$ | Ch19 |

## 7. IV、CACE/LATE、TSLS 与 MR

| 符号 | 名称 | 定义 | 语境/解释 | 注意事项 | 出处 |
|---|---|---|---|---|---|
| $Z$ | assignment / IV | 鼓励设计中的随机分配；计量中作为 instrument | 影响实际接受 treatment $D$，但不应直接影响 $Y$ | 不等同于实际 treatment $D$ | Ch21; Ch23 |
| $D$ | treatment received | 实际接受的 treatment | noncompliance/IV 中被 $Z$ 推动 | 因果问题常是 $D$ 对 $Y$ 的效应 | Ch21 |
| $D(1),D(0)$ | potential treatment received | assigned $Z=1/0$ 时实际接受 treatment 的潜在值 | 定义 compliance types | 与 $Y(1),Y(0)$ 同属 assignment $Z$ 的潜在值 | Ch21 |
| $U={D(1),D(0)}$ | latent compliance status | compliance behavior 的潜在变量 | principal strata 的一种 | 不能对单个 unit 完全观测 | Ch21 |
| $\mathrm{a}$ | always taker | $D(1)=1,D(0)=1$ | 无论分配如何都接受 treatment | exclusion restriction 下 assignment 对其 outcome 无效 | Ch21 |
| $\mathrm{c}$ | complier | $D(1)=1,D(0)=0$ | 只有被鼓励/分配处理时才接受 treatment | CACE/LATE 目标群体 | Ch21 |
| $\mathrm{d}$ | defier | $D(1)=0,D(0)=1$ | 分配处理反而不处理、分配对照反而处理 | monotonicity 排除 defiers | Ch21 |
| $\mathrm{n}$ | never taker | $D(1)=0,D(0)=0$ | 无论分配如何都不接受 treatment | exclusion restriction 下 assignment 对其 outcome 无效 | Ch21 |
| $\tau_D$ | first-stage effect | $E\{D(1)-D(0)\}=E(D\mid Z=1)-E(D\mid Z=0)$ | assignment 对实际 treatment 的平均效应 | IV 不能弱到 $\tau_D=0$ | Ch21 |
| $\tau_Y$ | ITT effect on outcome | $E\{Y(1)-Y(0)\}=E(Y\mid Z=1)-E(Y\mid Z=0)$ | assignment 对 outcome 的平均效应 | ITT 回答的是 $Z$ 的 effect，不是 $D$ 的 effect | Ch21 |
| $\pi_\mathrm{c}$ | complier proportion | $\Pr(U=\mathrm{c})=\tau_D$ under monotonicity | compliers 在总体中的比例 | randomization + monotonicity 下可识别 | Ch21 |
| $\tau_\mathrm{c}$ | CACE/LATE | $E\{Y(1)-Y(0)\mid U=\mathrm{c}\}$ | compliers 中 assignment/treatment-induced effect | 在 IV 假设下 $\tau_{\mathrm{c}}=\tau_Y/\tau_D$ | Ch21 |
| $\pi_u$ | compliance-type proportion | $\Pr(U=u)$, $u=\mathrm{a},\mathrm{n},\mathrm{c},\mathrm{d}$ | IV mixture 分解中各 latent strata 的比例 | 部分比例需 monotonicity/exclusion/randomization 才可识别 | Ch21; Ch22 |
| $\tau_u$ | compliance-type causal effect | $E\{Y(1)-Y(0)\mid U=u\}$ | assignment 对 latent compliance type $u$ 的平均效应 | 若 exclusion restriction 成立，$\tau_{\mathrm{a}}=\tau_{\mathrm{n}}=0$ | Ch21; Ch22 |
| $\mu_{zu}$ | compliance-type potential mean | $E\{Y(z)\mid U=u\}$ | IV inequalities 和 mixture disentangling 中使用 | binary outcome 时 $0\le\mu_{zu}\le1$ 产生可检验不等式 | Ch22 |
| $\mu_\mathrm{a},\mu_\mathrm{n}$ | exclusion-restricted means | always taker/never taker 下 $Y(1)$ 与 $Y(0)$ 的共同均值 | exclusion restriction 给出 $\mu_{1\mathrm{a}}=\mu_{0\mathrm{a}}=\mu_\mathrm{a}$ 与 $\mu_{1\mathrm{n}}=\mu_{0\mathrm{n}}=\mu_\mathrm{n}$ | 只在 exclusion restriction 语境下可这样合并 | Ch22 |
| $\mu_{1\mathrm{c}},\mu_{0\mathrm{c}}$ | complier potential means | $E\{Y(1)\mid U=\mathrm{c}\}$, $E\{Y(0)\mid U=\mathrm{c}\}$ | $\tau_{\mathrm{c}}=\mu_{1\mathrm{c}}-\mu_{0\mathrm{c}}$；也用于 IV inequalities | 和 $\mu_{\mathrm{a}},\mu_{\mathrm{n}}$ 一起 disentangle mixture distributions | Ch22 |
| Wald/IV estimator $\hat\tau_\mathrm{c}$ | Wald ratio estimator | $\hat\tau_Y/\hat\tau_D$ | 估计 CACE/LATE | weak IV 时有限样本性质差，方差可无穷 | Ch21 |
| Bloom estimator | one-sided noncompliance estimator | $\hat\tau_\mathrm{c}=\hat\tau_Y/\hat\tau_D$ | one-sided noncompliance 中的 Wald/CACE 估计量名称 | 译本注明 Bloom 的记号与本章不同 | Ch22 |
| $\tau_\mathrm{at}$ | as-treated contrast | $E(Y\mid D=1)-E(Y\mid D=0)$ | 按实际接受 treatment 分组的观测比较 | 在 noncompliance 下通常混合 always takers、never takers、compliers，不等于 CACE | Ch22 |
| $\tau_\mathrm{pp}$ | per-protocol contrast | $E(Y\mid Z=1,D=1)-E(Y\mid Z=0,D=0)$ | 只比较遵从分配的 units | 仍是混合量；通常不等于 CACE | Ch22 |
| $\tau_{Z=1},\tau_{Z=0}$ | assignment-conditional received-treatment contrasts | 给定 $Z=1$ 或 $Z=0$ 后比较 $D=1$ 与 $D=0$ 的 outcome | 用来展示其他 naive analyses 的缺陷 | 比较的 latent strata 组成不同 | Ch22 |
| $Q$ in IV inequalities | IV inequality test variable | $DY$, $D(1-Y)$, $(D-1)Y$, $D+Y-DY$ | binary outcome 下 IV assumptions 的 testable implications | 若 $E(Q\mid Z=1)-E(Q\mid Z=0)<0$，说明 IV assumptions 被数据反驳 | Ch22 |
| adjusted outcome $A_i$ | IV variance device | $A_i=Y_i-\tau_\mathrm{c} D_i$; sample 用 $\hat A_i=Y_i-\hat\tau_\mathrm{c} D_i$ | delta-method 方差估计 | 用 $\hat\tau_A/\tau_D$ 近似 ratio estimator 误差 | Ch21 |
| FAR confidence set | Fieller--Anderson--Rubin | $\{b: \hat\tau_A^2(b)/\hat V_A(b)\le z^2\}$ | weak IV robust confidence set | 可为空、闭区间、双区间或全实线 | Ch21 |
| linear IV model | 线性 IV 模型 | $Y=D^T\beta+\varepsilon$, $E(\varepsilon Z)=0$ | econometric IV 视角 | 允许 $E(\varepsilon D)\ne0$，但要求 instrument 与 error 不相关 | Ch23 |
| $\hat\beta_\mathrm{iv}$ | IV estimator | $(\sum Z_iD_i^T)^{-1} \sum Z_iY_i$ | just-identified linear IV | 需 $E(ZD^T)$ full rank | Ch23 |
| scalar IV ratio | scalar IV coefficient | $\operatorname{cov}(Z,Y)/\operatorname{cov}(Z,D)$ | binary $Z,D$ 时等同 Wald/CACE 识别公式 | 连接计量 IV 与 potential outcomes CACE | Ch23 |
| TSLS | two-stage least squares | 第一阶段用 IV 预测 $D$，第二阶段回归 $Y$ | 过识别/线性 IV 常用 | 在 FRDD 中 local TSLS 估计 local CACE | Ch23; Ch24 |
| MR $G_1,\ldots,G_p$ | genetic IVs | SNPs/genetic instruments | Mendelian randomization 中的 IVs | 可能因 pleiotropy 违反 exclusion restriction | Ch25 |
| MR $\beta$ | causal effect of $D$ on $Y$ | structural model 中 $Y$ 对 treatment $D$ 的系数 | MR 的目标效应 | summary-statistics MR 中通过 $\Gamma_j/\gamma_j$ 估计 | Ch25 |
| MR $\gamma_j$ | gene-treatment association | $D$ 对 $G_j$ 的 reduced-form coefficient | first-stage genetic association | weak/invalid IV 问题要注意 | Ch25 |
| MR $\Gamma_j$ | gene-outcome association | $Y$ 对 $G_j$ 的 reduced-form coefficient | outcome association | valid IV 下 $\Gamma_j=\beta\gamma_j$ | Ch25 |
| MR $\alpha_j$ | direct genetic effect | invalid IV model 中 $G_j$ 对 $Y$ 的直接效应 | pleiotropy/exclusion violation | valid IV 要求 $\alpha_j=0$ | Ch25 |
| $\hat\beta_j$ | ratio estimate in MR | $\hat\Gamma_j/\hat\gamma_j$ | 单个 genetic IV 对 $\beta$ 的 ratio estimator | 用 delta method 给 SE | Ch25 |
| fixed-effect MR estimator | fixed-effect estimator | 方差倒数加权组合多个 $\hat\beta_j$ | summary statistics MR | 有是否忽略 $\hat\gamma_j$ 不确定性的不同版本 | Ch25 |

## 8. RDD 与 FRDD

| 符号 | 名称 | 定义 | 语境/解释 | 注意事项 | 出处 |
|---|---|---|---|---|---|
| $X$ | running variable | 决定 treatment cutoff 的变量 | RDD 中不再只是普通 covariate | 与观测研究调整变量语境不同 | Ch20 |
| $x_0$ | cutoff point | 阈值 | $Z=I(X\ge x_0)$ | RDD 只识别 cutoff 附近 local effect | Ch20 |
| $\tau(x_0)$ | local average causal effect at cutoff | $E\{Y(1)-Y(0)\mid X=x_0\}$ | sharp RDD 目标量 | 依赖左右连续性；不是全体 ATE | Ch20 |
| RDD identification | discontinuity formula | $\lim_{\epsilon\to0+}E(Y\mid Z=1,X=x_0+\epsilon)-\lim_{\epsilon\to0+}E(Y\mid Z=0,X=x_0-\epsilon)$ | 通过 cutoff 两侧极限识别 | 形式不同于 g-formula/IPW | Ch20 |
| $R_i$ | right running component | $\max(X_i-x_0,0)$ | local linear RDD 回归 | 与 $L_i$ 一起允许 cutoff 两侧不同斜率 | Ch20 |
| $L_i$ | left running component | $\min(X_i-x_0,0)$ | local linear RDD 回归 | $R_i,L_i$ 均以 cutoff 中心化 | Ch20 |
| $\hat\tau(x_0)$ | RDD estimator | OLS $Y_i$ 对 ${1,Z_i,R_i,L_i}$ 中 $Z_i$ 的系数 | cutoff 处 local effect | bandwidth/neighborhood 选择带 bias-variance tradeoff | Ch20 |
| FRDD $\tau_D(x_0)$ | first-stage discontinuity | $E\{D(1)-D(0)\mid X=x_0\}$ | cutoff 对实际 treatment 的 local effect | 分母非零才可识别 local CACE | Ch24 |
| FRDD $\tau_Y(x_0)$ | reduced-form discontinuity | $E\{Y(1)-Y(0)\mid X=x_0\}$ | cutoff 对 outcome 的 local effect | 与 sharp RDD 的 outcome jump 对应 | Ch24 |
| $\tau_\mathrm{c}(x_0)$ | local complier average causal effect | $E\{Y(1)-Y(0)\mid D(1)>D(0),X=x_0\}$ | fuzzy RDD 目标量 | $\tau_{\mathrm{c}}(x_0)=\tau_Y(x_0)/\tau_D(x_0)$ | Ch24 |
| $\hat\tau_\mathrm{c}(x_0)$ | FRDD estimator | $\hat\tau_Y(x_0)/\hat\tau_D(x_0)$ 或 local TSLS | 估计 cutoff 处 local CACE | 指定 bandwidth $h$ 后化为 local TSLS | Ch24 |
| $h$ | bandwidth/neighborhood width | 使用 $X_i\in [x_0-h,x_0+h]$ 的 local data | RDD/FRDD 的局部样本选择 | 小 $h$ 低 bias 高 variance，大 $h$ 高 bias 低 variance | Ch24 |

## 9. Principal Stratification, Mediation, CDE

| 符号 | 名称 | 定义 | 语境/解释 | 注意事项 | 出处 |
|---|---|---|---|---|---|
| $M$ | post-treatment/intermediate variable | treatment 之后发生的变量 | principal stratification/mediation/CDE 中核心 | 不应像 pretreatment covariate 那样 naive conditioning | Ch26 |
| $M(1),M(0)$ | potential intermediate values | treatment/control 下 $M$ 的潜在值 | principal strata 的定义基础 | $M$ 受 treatment 影响，观测值不能直接作为 subgroup covariate | Ch26 |
| $\tau(m_1,m_0)$ | principal stratification average causal effect | $E\{Y(1)-Y(0)\mid M(1)=m_1,M(0)=m_0\}$ | 在由 $M$ 的联合潜在值定义的子群内比较 | 通常难识别；compliance 是一个特例 | Ch26 |
| $\tau(1,1)$ | survivor/employed average causal effect 等 | $E\{Y(1)-Y(0)\mid M(1)=1,M(0)=1\}$ | truncation by death 中唯一良好定义的 subgroup effect | 常叫 SACE；也可为 dissociative effect | Ch26 |
| $\tau(1,0)$ | associative/complier-like effect | $E\{Y(1)-Y(0)\mid M(1)=1,M(0)=0\}$ | noncompliance 中可对应 CACE | 是否可识别依赖 monotonicity/exclusion 等 | Ch26 |
| $\tau(0,1)$ | defier-like principal effect | $E\{Y(1)-Y(0)\mid M(1)=0,M(0)=1\}$ | 二元 $M$ 的四个 principal strata 之一 | strong monotonicity 时该层为空 | Ch26 |
| $\tau(0,0)$ | never/survivor-complement principal effect | $E\{Y(1)-Y(0)\mid M(1)=0,M(0)=0\}$ | 二元 $M$ 的四个 principal strata 之一；常属于 dissociative effect | 是否有实质含义取决于 $M$ 的应用语境 | Ch26 |
| $\pi_{(m_1,m_0)}$ | principal stratum proportion | $\Pr(M(1)=m_1,M(0)=m_0)$ | latent strata 的比例 | monotonicity 下某些比例可由 observed $M,Z$ 识别 | Ch26 |
| $\pi_{(1,1)},\pi_{(0,0)},\pi_{(1,0)}$ | binary principal-stratum proportions | monotonicity 下常有 $\pi_{(1,1)}=\Pr(M=1\mid Z=0)$, $\pi_{(0,0)}=\Pr(M=0\mid Z=1)$, $\pi_{(1,0)}=\Pr(M=1\mid Z=1)-\Pr(M=1\mid Z=0)$ | 用 observed $M,Z$ 识别 latent strata 比例 | 若无 monotonicity，四个比例识别更难 | Ch26 |
| $\pi(X)$ | principal score | $\Pr\{M(1)=1\mid X\}$ | principal score method | 类似 propensity score，但目标是 latent principal stratum | Ch26 |
| $\pi_{(m_1,m_0)}(X)$ | conditional principal score | $\Pr\{M(1)=m_1,M(0)=m_0\mid X\}$ | principal score method 的条件版 | 权重型识别公式使用这些条件概率 | Ch26 |
| $w_{z,(m_1,m_0)}(X)$ | principal-score weight | 由 conditional/marginal principal scores 的比值构造 | 用 observed subgroup 的加权均值识别 principal-stratum causal effects | 依赖 principal ignorability 和 monotonicity 类假设 | Ch26 |
| dissociative effects | 解离效应 | $m_1=m_0$ 的 principal strata 内效应，如 $\tau(1,1)$, $\tau(0,0)$ | treatment 不改变 $M$ 的子群内，度量不经由 $M$ 变化的效应 | 不等同于 mediation 中的 natural direct effect | Ch26 |
| associative effects | 关联效应 | $m_1\ne m_0$ 的 principal strata 内效应，如 $\tau(1,0)$, $\tau(0,1)$ | treatment 改变 $M$ 的子群内效应 | 不能简单解释为 direct 或 indirect effect | Ch26 |
| $Y(z,m)$ | controlled potential outcome | 同时把 treatment 设为 $z$、mediator 设为 $m$ 时的 outcome | CDE/mediation 共同使用 | 不同于 $Y(z)$；多了 mediator intervention | Ch27; Ch28 |
| $M_z$ | shorthand for $M(z)$ | treatment $z$ 下 mediator 的潜在值 | nested potential outcome 中使用 | 译本用 $M_z$ 避免括号过多 | Ch27 |
| $Y(z,M_{z'})$ | nested potential outcome | treatment 设为 $z$，mediator 设为其在 $z'$ 下的自然值 | mediation 的 cross-world counterfactual | $z\ne z'$ 时没有单一物理实验可同时观测 | Ch27 |
| composition | composition assumption | $Y(z,M_z)=Y(z)$ | 保证自然 mediator 值下的 nested outcome 回到标准 potential outcome | 本质是假设/定义约定 | Ch27 |
| $\tau$ in mediation | total effect | $E\{Y(1)-Y(0)\}$ | treatment 对 outcome 的总效应 | 在 composition 下可分解为 NDE+NIE | Ch27 |
| $\mathrm{NDE}$ | natural direct effect | $E\{Y(1,M_0)-Y(0,M_0)\}$ | mediator 固定在 control 下自然值时 treatment 的效应 | 依赖 cross-world potential outcomes | Ch27 |
| $\mathrm{NIE}$ | natural indirect effect | $E\{Y(1,M_1)-Y(1,M_0)\}$ | treatment 固定为 1 时 mediator 改变带来的效应 | 与 NDE 一起分解 total effect | Ch27 |
| cross-world independence | cross-world assumption | $Y(z,m)\perp\!\!\!\perp M(z')\mid X$ | mediation formula 的关键假设之一 | 无法由物理实验保证，是最强/最形而上假设 | Ch27 |
| mediation formula | mediation identification | $E\{Y(z,M_{z'})\mid X=x\}=\sum_m E(Y\mid Z=z,M=m,X=x)\Pr(M=m\mid Z=z',X=x)$ | 识别 NDE/NIE 的公式 | 需 sequential ignorability + treatment-mediator ignorability + cross-world independence | Ch27 |
| $\mathrm{CDE}(m)$ | controlled direct effect | $E\{Y(1,m)-Y(0,m)\}$ | mediator 固定为 $m$ 时 treatment 的直接效应 | 不定义 indirect effect；不需要 cross-world independence | Ch28 |
| $\mu_{zm}$ | joint-treatment potential mean | $E\{Y(z,m)\}$ | CDE 中把 $(Z,M)$ 当作四水平 treatment | 用 OR/IPW/DR 识别 | Ch28 |
| $\mu_{zm}(x)$ | conditional mean for joint treatment | $E(Y\mid Z=z,M=m,X=x)$ | CDE outcome model | 与 $e_{zm}(x)$ 配合 | Ch28 |
| $e_{zm}(x)$ | joint propensity score | $\Pr(Z=z,M=m\mid X=x)=\Pr(Z=z\mid X=x)\Pr(M=m\mid Z=z,X=x)$ | CDE IPW/DR | 需要 joint overlap | Ch28 |
| $\hat\mu_{zm}^\mathrm{reg}$ | CDE outcome regression mean | $n^{-1}\sum\hat\mu_{zm}(X_i)$ | 估计 $\mu_{zm}$ | 然后 $\hat\mu_{1m}-\hat\mu_{0m}$ 估计 CDE | Ch28 |
| $\hat\mu_{zm}^\mathrm{ht/haj/dr}$ | CDE IPW/Hajek/DR mean | 用 $I(Z=z,M=m)$ 与 joint PS 构造 | 估计 $\mu_{zm}$ | 与 ATE 的估计量平行 | Ch28 |

## 10. Time-Varying Treatment 与 Robins 系列记号

| 符号 | 名称 | 定义 | 语境/解释 | 注意事项 | 出处 |
|---|---|---|---|---|---|
| $X_0$ | baseline covariates | treatment 前协变量 | 两时间点设定中的 baseline history | 条件化于 $X_0$ 后讨论 sequential randomization | Ch29 |
| $Z_1,Z_2$ | time-varying treatments | 时间点 1 和 2 的处理 | 时间顺序：$X_0 -> Z_1 -> X_1 -> Z_2 -> Y$ | $Z_1$ 可能影响 $X_1$，$X_1$ 又影响 $Z_2$ 与 $Y$ | Ch29 |
| $X_1$ | time-varying covariate/confounder | 介于两个 treatments 之间的协变量 | 同时是 $Z_1$ 的后处理变量，也是 $Z_2-Y$ 的混杂变量 | 直接分层会有 post-treatment adjustment 问题 | Ch29 |
| $Y(z_1,z_2)$ | time-varying potential outcome | treatment history 固定为 $(z_1,z_2)$ 时的 outcome | 二元两期 treatment 下每个 unit 有 4 个 potential outcomes | 多期时数量随 $K$ 指数增长 | Ch29 |
| sequential ignorability | sequential randomization | $Z_1\perp\!\!\!\perp Y(z_1,z_2)\mid X_0$ 且 $Z_2\perp\!\!\!\perp Y(z_1,z_2)\mid(Z_1,X_1,X_0)$ | 给定已观测历史后每期 treatment 像 randomized | 排除 treatment-outcome confounding，但可允许 $X_1-Y$ 有未测混杂 | Ch29 |
| $E\{Y(z_1,z_2)\}$ g-formula | recursive g-formula | $E[ E\{ E(Y\mid z_2,z_1,X_1,X_0)\mid z_1,X_0 \} ]$ | outcome modeling 识别公式 | plug-in 要建模 $X_1$，可能引发 g-null paradox | Ch29 |
| $\tilde Y_2(z_1,z_2)$ | inner recursive mean | $E(Y\mid Z_2=z_2,Z_1=z_1,X_1,X_0)$ | recursive estimation 的第一层 | 拟合 $Y$ 关于 $(X_1,X_0)$ | Ch29 |
| $\tilde Y_1(z_1,z_2)$ | outer recursive mean | $E\{\tilde Y_2(z_1,z_2)\mid Z_1=z_1,X_0\}$ | recursive estimation 的第二层 | 避免直接建模 $X_1$ 的分布 | Ch29 |
| $e(z_1,X_0)$ | first-time propensity | $\Pr(Z_1=z_1\mid X_0)$ | time-varying IPW 的第一期分母 | 需 positivity | Ch29 |
| $e(z_2,Z_1,X_1,X_0)$ | second-time propensity | $\Pr(Z_2=z_2\mid Z_1,X_1,X_0)$ | time-varying IPW 的第二期分母 | 权重是两期 propensity 的乘积倒数 | Ch29 |
| time-varying IPW formula | sequential IPW | $E[1(Z_1=z_1)1(Z_2=z_2)Y/{e(z_1,X_0)e(z_2,Z_1,X_1,X_0)}]$ | 识别 $E\{Y(z_1,z_2)\}$ | 权重可不稳定；需要 overlap | Ch29 |
| $\hat E^\mathrm{ht}{Y(z_1,z_2)}$ | time-varying HT estimator | 样本平均的 sequential IPW | 估计 treatment history 下 mean potential outcome | location shift 不 invariant，有限样本可能不稳定 | Ch29 |
| $\hat E^\mathrm{haj}{Y(z_1,z_2)}$ | time-varying Hajek estimator | HT 除以相应的 $\hat{1}^\mathrm{ht}(z_1,z_2)$ | 稳定化的 treatment-history mean | 是 normalized IPW | Ch29 |
| MSM | marginal structural model | $E\{Y(z_1,z_2)\}=f(z_1,z_2;\beta)$ | 用低维模型概括许多 treatment histories 的平均潜在结果 | 多期时避免直接估计指数多个均值 | Ch29 |
| MSM with $X_0$ | baseline-covariate MSM | $E\{Y(z_1,z_2)\mid X_0\}=f(z_1,z_2,X_0;\beta)$ | 条件化 baseline covariates 的 MSM | 常用 WLS/IPW 估计 | Ch29 |
| IPW under MSM | weighted estimating criterion | 对每个 treatment history 用 sequential IPW 加权最小化 ${Y-f(history,X_0;b)}^2$ | 从 observed data 求 $\beta$ | 权重为各期 propensity 倒数乘积 | Ch29 |
| SNM | structural nested model | 条件 causal contrast 用 $g_1,g_2$ 参数化 | Robins 为 overlap/IPW 困难提出的替代 | 比 MSM 更局部，定义 sequential blip effects | Ch29 |
| $\overline Z_K,\overline X_K$ | treatment/covariate history | 多时间点历史向量 | 多期推广中使用 | $Y(\overline z_K)$ 的数量随 $K$ 指数增长 | Ch29 |

## 11. 缩略语与中文名

| 缩略语 | 英文 | 中文 | 语境 |
|---|---|---|---|
| ACE/ATE | average causal effect / average treatment effect | 平均因果效应/平均处理效应 | 通常对应 $\tau$ |
| AI | Abadie and Imbens | Abadie--Imbens 匹配估计量 | matching estimators |
| ANCOVA | analysis of covariance | 协方差分析 | 回归调整 |
| ATT | average causal effect on the treated | 处理组平均因果效应 | $\tau_\mathrm{T}$ |
| ATC | average causal effect on the control | 对照组平均因果效应 | $\tau_\mathrm{C}$ |
| BMI | body mass index | 身体质量指数 | 示例变量 |
| CATE | conditional average causal effect | 条件平均因果效应 | $\tau(X)$ |
| CACE | complier average causal effect | 依从者平均因果效应 | $\tau_\mathrm{c}$ |
| LATE | local average treatment effect | 局部平均处理效应 | 与 CACE 常同义 |
| CDE | controlled direct effect | 受控直接效应 | $\mathrm{CDE}(m)$ |
| NDE | natural direct effect | 自然直接效应 | $\mathrm{NDE}$ |
| NIE | natural indirect effect | 自然间接效应 | $\mathrm{NIE}$ |
| SUTVA | stable unit treatment value assumption | 稳定单元处理值假设 | no interference + consistency |
| CRE | completely randomized experiment | 完全随机实验 | 固定 $n_1,n_0$ 的随机分配 |
| BRE | Bernoulli randomized experiment | Bernoulli 随机实验 | $Z_i$ Bernoulli，$n_1$ 随机 |
| CLT | central limit theorem | 中心极限定理 | 渐近近似 |
| SRE | stratified randomized experiment | 分层随机实验 | strata 内 CRE |
| MPE | matched-pairs experiment | 配对实验 | 每对一个 treated 一个 control |
| FRT | Fisher randomization test | Fisher 随机化检验 | sharp null 下随机化分布 |
| HT | Horvitz--Thompson estimator | Horvitz--Thompson 估计量 | IPW 的未规范化版本 |
| IPW | inverse propensity score weighting | 逆倾向得分加权 | 用 $1/e(X)$ 等权重 |
| DR/AIPW | doubly robust / augmented IPW | 双重稳健/增广 IPW | outcome model 或 PS model 正确即可 |
| OLS | ordinary least squares | 普通最小二乘 | 回归估计 |
| WLS | weighted least squares | 加权最小二乘 | 权重回归 |
| EHW | Eicker--Huber--White | EHW 稳健标准误 | misspecification robust SE |
| FWL | Frisch--Waugh--Lovell | Frisch--Waugh--Lovell 定理 | 线性回归附录 |
| IID | independent and identically distributed | 独立同分布 | 超总体/概率论 |
| IV | instrumental variable | 工具变量 | 处理内生性/未测混杂 |
| ILS | indirect least squares | 间接最小二乘 | IV/FRDD |
| LASSO | least absolute shrinkage and selection operator | 最小绝对收缩与选择算子 | 高维/机器学习回归 |
| TSLS | two-stage least squares | 两阶段最小二乘 | 线性 IV 估计 |
| ITT | intention-to-treat | 意向治疗分析 | assignment $Z$ 对 outcome 的效应 |
| FAR | Fieller--Anderson--Rubin | FAR 置信集 | weak IV robust interval |
| MLE | maximum likelihood estimate | 极大似然估计 | 统计附录/模型估计 |
| NHANES | National Health and Nutrition Examination Survey | 美国国家健康与营养调查 | 观测研究示例 |
| RCT | randomized controlled trial | 随机对照试验 | 随机实验 |
| ReM | rerandomization using the Mahalanobis distance | 基于 Mahalanobis 距离的再随机化 | 再随机化设计 |
| RD | risk difference | 风险差 | 关联/二元 outcome |
| RR | risk ratio / relative risk | 风险比/相对风险 | 关联/敏感性分析 |
| OR | odds ratio | 优势比 | 关联/二元 outcome |
| RDD | regression discontinuity design | 回归不连续设计 | cutoff 附近 local effect |
| FRDD | fuzzy regression discontinuity design | 模糊回归不连续设计 | RDD + IV |
| MR | Mendelian randomization | Mendelian 随机化 | genetic IV |
| SNP | single nucleotide polymorphism | 单核苷酸多态性 | MR 中的 genetic instruments |
| MSM | marginal structural model | 边际结构模型 | time-varying treatment |
| SNM | structural nested model | 结构嵌套模型 | Robins time-varying framework |

## 12. 最容易混淆的几组符号

| 易混组 | 区别 |
|---|---|
| $\tau_i$ vs $\tau$ | $\tau_i$ 是个体效应；$\tau$ 是平均效应。$\tau_i$ 基本不可识别，$\tau$ 在随机化或识别假设下可估计。 |
| finite-population $\tau$ vs superpopulation $\tau$ | 前者是固定 Science Table 的有限平均；后者是 $E\{Y(1)-Y(0)\}$。同符号但随机性来源不同。 |
| $\tau$, $\tau_{\mathrm{T}}$, $\tau_{\mathrm{C}}$, $\tau_{\mathrm{PF}}$ | $\tau$ 是全体平均；$\tau_{\mathrm{T}}$/$\tau_{\mathrm{C}}$ 是 treated/control 目标人群；$\tau_{\mathrm{PF}}$ 是观测均值差，通常不是因果效应。 |
| $\tau(X)$, $\tau_{\mathrm{T}}(X)$, $\tau_{\mathrm{C}}(X)$, $\tau_{\mathrm{PF}}(X)$ | 这些是给定 $X$ 后的条件版本；在均值可忽略性下相等，但无该假设时可不同。 |
| $\mathrm{QCE}_q$ vs $\tau_q$ | $\mathrm{QCE}_q$ 比较两个边际潜在结果分布的分位数，ignorability 下可识别；$\tau_q$ 是个体效应 $Y(1)-Y(0)$ 的分位数，一般不可识别。 |
| $Z$ vs $D$ in IV | $Z$ 是 assignment/instrument；$D$ 是实际接受 treatment。IV 目标通常是 $D$ 对 $Y$ 的效应，但识别用 $Z$ 的外生变化。 |
| $\tau_Y$ vs $\tau_{\mathrm{c}}$ | $\tau_Y$ 是 assignment 对 outcome 的 ITT effect；$\tau_{\mathrm{c}}$ 是 compliers 中的 CACE/LATE，等于 $\tau_Y/\tau_D$。 |
| CACE vs as-treated/per-protocol contrasts | $\tau_\mathrm{c}$ 是 latent compliers 的因果效应；$\tau_\mathrm{at}$、$\tau_\mathrm{pp}$ 等是观测分组比较，通常混合多个 compliance strata。 |
| $e(X)$ vs $h(X)$ | $e(X)$ 是 propensity score；$h(X)$ 是定义目标总体的 weighting function。$h(X)$ 可以取 $1$, $e(X)$, $1-e(X)$, $e(X){1-e(X)}$。 |
| $\hat\tau^\mathrm{ht}$ vs $\hat\tau^\mathrm{hajek}$ | HT 是未规范化 IPW，可能不稳定且不平移不变；Hajek 规范化权重，更稳定。 |
| outcome regression vs DR | OR 依赖 outcome model 正确；DR 在 outcome model 或 PS model 至少一个正确时一致。 |
| confounder $X$ vs post-treatment $M$ | $X$ 是 treatment 前变量，可以用于调整；$M$ 受 treatment 影响，直接条件化会改变问题。 |
| NDE/NIE vs CDE | NDE/NIE 使用 cross-world nested potential outcomes，可分解 total effect；CDE 只固定 mediator 为 $m$，不定义 indirect effect。 |
| RDD $X$ vs covariate $X$ | RDD 中 $X$ 是 running variable，用于定义 cutoff；不是普通“越多越好”的 adjustment covariate。 |
| $\Gamma$ vs $\gamma_j$ | $\Gamma$ 是 Rosenbaum sensitivity 或 MR reduced-form gene-outcome coefficient 的大写 gamma，需看语境；$\gamma_j$ 在 MR 中是 gene-treatment association。 |
