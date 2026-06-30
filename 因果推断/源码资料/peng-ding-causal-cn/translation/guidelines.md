# 中文译本翻译规范

## 翻译原则

本译本采用“忠实翻译 + 注解”的策略。数学骨架必须忠实于英文原书，包括公式、编号、图表、引用、例子、命题、证明和原有 label。正文叙述使用自然中文，必要时加入简短译者注，但不改变原书的数学含义。

## 当前翻译口径

- 书名、part 标题、章节标题、节标题、小节标题和习题标题默认保留英文原文，不翻译成中文。
- 正文普通叙述翻译为自然中文。
- 因果推断 technical terms 默认保留英文，例如 `potential outcome`、`Fisher randomization test`、`propensity score`、`instrumental variable`；必要时可在第一次出现时用中文短语解释，但英文术语必须保留。
- 人名、数据集名称、软件包名称、定理冠名、方法冠名保留英文，例如 `Neyman`、`Fisher`、`Rubin`、`LaLonde`、`JOBS II`、`mediation`。
- 数学环境、公式、图表、R 代码、label、citation key 不翻译、不改写；只翻译 surrounding prose。

## 模板与结构规则

- 本工程必须完全沿用英文原书 `notes/peng-ding-causal/` 的 `krantz.cls` 模板、主文件结构、part/chapter/include 顺序、label、图表目录和 `causal.bib`。
- 中文编译只允许做必要适配：使用 XeLaTeX、`fontspec`、`xeCJK`，并优先使用项目内 `fonts/source-han-serif/` 的思源宋体（Source Han Serif）。
- 禁止改成 `amsbook`、现有中文学习笔记模板，或任何自创教材模板。
- 未翻译章节可以暂时保留英文原书源码作为底稿，但文件名、位置和 include 关系必须与原书保持一致；后续逐章替换为中文。

## 术语规则

- 核心 technical terms 优先保持英文；如果需要中文解释，第一次出现可写作“English term（中文解释）”，例如 “Fisher randomization test（Fisher randomization test 的检验思想）”，但不得把英文术语完全替换掉。
- 后文通常继续使用英文术语；若英文缩写在领域中常用，则保留缩写，例如 “Fisher randomization test, FRT”。
- 同一术语必须服从 `translation/terminology.md`，不得在不同章节自由改译。
- 暂不确定的术语先记录到术语表，状态标为“待确认”，不要在章节内各自决定。

## LaTeX 规则

- 保留原书已有 label，例如 `chapter::correlationassociation`、`eq::short-regression`、`prop::2x2-independence`。
- 新增译者注和问答 label 使用新前缀，例如 `sec:qa-...`、`sec:trans-note-...`。
- 正文引用统一使用 `\cref`；数学公式仍可使用 `\eqref`。
- 禁止使用 `\bm`，向量用 `\mathbf`，矩阵用 `\boldsymbol`。
- 禁止使用 `\I`，指示函数写作 `\mathbb{I}`。
- 禁止使用 Unicode 下标，例如 `$n₁$`；应写作 `$n_1$`。
- `.tex` 文件中不得出现 Markdown 标题、列表或加粗语法。

## QA 同步规则

用户在对话中提出实质性学习问题时：

1. 先在对话中口语化回答。
2. 写入 `appendix/qa.tex`，每个问题一个 `\subsection{...}\label{sec:qa-...}`。
3. 若问题对应正文自然位置，在正文加短脚注：`\footnote{相关讨论见附录 \cref{sec:qa-...}。}`。
4. 若问题改变了术语译法或解释方式，同步更新 `translation/terminology.md`。
5. 因果推断通用学习问题也需要同步或镜像到既有中文笔记的 `notes/A-First-Course-in-Causal-Inference/appendix/qa.tex`。

## Sub-Agent 分工规则

- 翻译 agent 只负责指定章节，不得改其他章节。
- 审查 agent 检查术语、label、`\cref`、禁用命令、Markdown 残留和编译风险。
- 每批翻译完成后必须运行本目录 `compile.sh`。
- 遇到跨章术语争议时，先更新术语表，再统一修正文稿。

## 习题解答规则

- 习题解答统一写在 `solutions/chapterXXsolutions.tex`，不直接插入原章节正文。
- 每章解答文件只负责对应章节的 Homework Problems；sub-agent 不得跨章写入。
- 每个题目使用：
  `\begin{exercisesolution}{题目英文标题}{简短中文说明} ... \end{exercisesolution}`。
- 解答必须完整、系统，至少包含主要推导或论证、关键直觉、与正文的引用关系，以及一个简短的“用途/Remark”说明。
- 引用正文命题、定理、公式、图表时优先用原书已有 label，例如 `\cref{prop::2x2-independence}`、`\eqref{eq::short-regression}`。
- 如需引用外部文献，使用 `\citet` 或 `\citep`，不得手写非 BibTeX 文献条目。
- 解答中的 technical terms 和人名继续保持英文优先，中文解释服务于理解，不替换核心英文术语。
- 解答同样遵守 LaTeX 红线：无 `\bm`、无 `\I`、无 `\tag`、无 Unicode 下标、无 Markdown 语法。
