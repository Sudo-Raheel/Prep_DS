# Statistical Tests and $p$-Values

A $p$-value is the probability, assuming the null hypothesis $H_0$ is true, of obtaining a test statistic at least as extreme as the one observed.

Every test in this section follows the same pipeline:

$$\text{data}
\rightarrow
\text{test statistic}
\rightarrow
\text{reference distribution under }H_0
\rightarrow
\text{tail probability}
\rightarrow
p\text{-value}.$$

Only the statistic and the reference distribution change from test to test.

## Which test do I use?

| Question | Data | Test | Reference distribution |
|:--|:--|:--|:--|
| Is the mean equal to a fixed value? ($\sigma$ unknown) | One numeric sample | [One-sample $t$-test](one-sample-t.md) | $t_{n-1}$ |
| Is the mean equal to a fixed value? ($\sigma$ known) | One numeric sample | [$z$-test](z-test.md) | $N(0,1)$ |
| Do two independent groups have the same mean? | Two independent numeric samples | [Independent two-sample $t$-test (Welch)](two-sample-t.md) | $t_{\nu}$ (Welch df) |
| Did the mean change between paired measurements? | Paired numeric observations | [Paired $t$-test](paired-t.md) | $t_{n-1}$ on the differences |
| Same as paired, but without assuming normality | Paired observations | [Wilcoxon signed-rank test](wilcoxon.md) | Signed-rank distribution |
| Are two categorical variables independent? | Contingency table of counts | [Chi-square test of independence](chi-square.md) | $\chi^2$ |
| Do three or more groups have the same mean? | $k\ge 3$ independent samples | [One-way ANOVA](anova.md) | $F_{k-1,\,N-k}$ |

## Background

- [The theoretical $t$-distribution](t-distribution.md): density, symmetry, heavy tails and how a $p$-value is read off it.

## How each page is organized

Every test page starts with an **At a glance** box (the one-line pipeline from data to $p$-value). It then covers the purpose and hypotheses, the test statistic, degrees of freedom, how to compute the $p$-value for right-sided, left-sided and two-sided alternatives, a worked example, and the assumptions.
