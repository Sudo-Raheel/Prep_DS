# Wilcoxon Signed-Rank Test

!!! abstract "At a glance"
    The Wilcoxon signed-rank procedure is

    $$\boxed{
    \text{paired observations}
    \rightarrow
    d_i
    \rightarrow
    |d_i|
    \rightarrow
    R_i
    \rightarrow
    W^+,W^-
    \rightarrow
    p\text{-value}.
    }$$

    For an exact one-sided test:

    $$\boxed{
    p
    =
    \frac{
    \text{number of sign assignments at least as favorable as observed}
    }{
    2^m
    }.
    }$$

    Paste this into the main LaTeX file:


## Purpose

The Wilcoxon signed-rank test compares two methods or conditions evaluated on the same experimental units.

Examples include:

- two methods evaluated on the same datasets;

- measurements taken before and after an intervention;

- two models evaluated over the same time periods;

- two conditions evaluated on matched observations.

Like the paired $t$-test, the Wilcoxon signed-rank test begins with paired differences. However, it uses the signs and ranks of the differences instead of their raw numerical values.

It is useful when the paired differences are not approximately normal or may contain outliers.

## Paired Differences

Suppose Methods A and B are evaluated on $n$ matched experimental units. Define the paired difference as

$$d_i=A_i-B_i.$$

Therefore:

$$d_i>0$$

means Method A performed better than Method B, assuming higher values are better, while

$$d_i<0$$

means Method B performed better than Method A.

A difference of zero represents a tie:

$$d_i=0.$$

Zero differences are removed before calculating the signed-rank statistic. Let $m$ denote the number of remaining nonzero differences.

## Hypotheses

For a two-sided test, the hypotheses are

$$H_0:
\text{the distribution of paired differences is symmetric around zero},$$

$$H_1:
\text{the distribution of paired differences is not centered at zero}.$$

For the one-sided claim that Method A tends to outperform Method B:

$$H_0:
\text{Method A has no systematic tendency to outperform Method B},$$

$$H_1:
\text{Method A tends to outperform Method B}.$$

Under $H_0$, a difference of a given magnitude is equally likely to receive a positive or negative sign.

## Ranking the Differences

After removing zero differences, calculate the absolute differences:

$$|d_1|,|d_2|,\ldots,|d_m|.$$

Rank these absolute differences from smallest to largest.

Define

$$\boxed{
R_i=\operatorname{rank}(|d_i|)
}$$

where $R_i$ is the rank assigned to the absolute difference $|d_i|$.

If several absolute differences are equal, they receive the average of the ranks they would have occupied.

For example, if five equal differences occupy ranks

$$2,3,4,5,6,$$

each receives the average rank

$$\frac{2+3+4+5+6}{5}=4.$$

## Positive and Negative Rank Sums

The positive rank sum is

$$\boxed{
W^+
=
\sum_{\{i:d_i>0\}}R_i
}$$

and the negative rank sum is

$$\boxed{
W^-
=
\sum_{\{i:d_i<0\}}R_i.
}$$

If Method A consistently performs better than Method B, the large ranks will tend to receive positive signs, producing a large value of $W^+$.

If there are no ties in the ranks, the total rank sum is

$$W^++W^-
=
1+2+\cdots+m
=
\frac{m(m+1)}{2}.$$

## Exact One-Sided $p$-Value

Under $H_0$, each of the $m$ nonzero differences is equally likely to have a positive or negative sign.

Each difference therefore has two possible sign states:

$$+\quad\text{or}\quad-.$$

The total number of possible sign assignments is

$$\boxed{2^m}.$$

For the one-sided hypothesis that Method A tends to outperform Method B, the exact $p$-value is

$$\boxed{
p
=
P(W^+\geq W^+_{\mathrm{obs}}\mid H_0)
}$$

or equivalently,

$$\boxed{
p
=
\frac{
\text{number of sign assignments with }
W^+\geq W^+_{\mathrm{obs}}
}{
2^m
}.
}$$

Thus, the exact $p$-value counts how many possible sign assignments are at least as favorable to Method A as the observed assignment.

## Two-Sided $p$-Value

A two-sided test checks for a systematic difference in either direction.

A common test statistic is

$$W=\min(W^+,W^-).$$

An unusually small value of $W$ indicates that most of the rank weight is concentrated on one side.

The exact two-sided $p$-value includes sign assignments that are at least as extreme in either direction.

Software should generally be used for the two-sided exact calculation, especially when ties are present.

## Normal Approximation

For larger values of $m$, the distribution of $W^+$ can be approximated using a normal distribution.

Write

$$W^+
=
\sum_{i=1}^{m}R_iI_i,$$

where

$$I_i=
\begin{cases}
1, & d_i>0,\\
0, & d_i<0.
\end{cases}$$

Under $H_0$,

$$P(d_i>0)=P(d_i<0)=\frac{1}{2},$$

so

$$E[I_i]=\frac{1}{2}.$$

Therefore,

$$E[W^+]
=
\sum_{i=1}^{m}R_iE[I_i].$$

When the ranks are $1,2,\ldots,m$,

$$E[W^+]
=
\frac{1}{2}\sum_{i=1}^{m}i.$$

Since

$$\sum_{i=1}^{m}i
=
\frac{m(m+1)}{2},$$

we obtain

$$\boxed{
E[W^+]
=
\frac{m(m+1)}{4}.
}$$

Without ties, the variance is

$$\boxed{
\operatorname{Var}(W^+)
=
\frac{m(m+1)(2m+1)}{24}.
}$$

The standardized statistic is then

$$\boxed{
Z
=
\frac{
W^+-\frac{m(m+1)}{4}
}{
\sqrt{
\frac{m(m+1)(2m+1)}{24}
}
}.
}$$

This statistic measures how many standard deviations the observed positive rank sum lies above or below its expected value under $H_0$.

For the right-sided alternative that Method A is better, a large positive $Z$-value produces a small right-tail $p$-value:

$$p=P(Z\geq z_{\mathrm{obs}}).$$

Corrections are required when tied absolute differences are present. Statistical software may also apply a continuity correction.

## PLTE Versus SPE Example

Suppose PLTE and SPE are compared on eight datasets using AUCPR. Since a higher AUCPR is better, define

$$d_i
=
\operatorname{AUCPR}_{\mathrm{PLTE},i}
-
\operatorname{AUCPR}_{\mathrm{SPE},i}.$$

The observed results are

| Dataset |  PLTE  |  SPE   | Difference $d_i$ |
|:-------:|:------:|:------:|:----------------:|
|    1    | $0.81$ | $0.79$ |     $+0.02$      |
|    2    | $0.44$ | $0.42$ |     $+0.02$      |
|    3    | $0.18$ | $0.16$ |     $+0.02$      |
|    4    | $0.25$ | $0.25$ |      $0.00$      |
|    5    | $0.19$ | $0.21$ |     $-0.02$      |
|    6    | $0.55$ | $0.50$ |     $+0.05$      |
|    7    | $0.95$ | $0.94$ |     $+0.01$      |
|    8    | $0.22$ | $0.20$ |     $+0.02$      |

The one-sided hypotheses are

$$H_0:
\text{PLTE has no systematic tendency to outperform SPE},$$

$$H_1:
\text{PLTE tends to achieve higher AUCPR than SPE}.$$

Dataset 4 has a zero difference and is removed. Therefore,

$$m=7.$$

The remaining absolute differences and ranks are

| Dataset |  $d_i$  | $|d_i|$ | $R_i$ |
|:-------:|:-------:|:-------:|:-----:|
|    7    | $+0.01$ | $0.01$  |  $1$  |
|    1    | $+0.02$ | $0.02$  |  $4$  |
|    2    | $+0.02$ | $0.02$  |  $4$  |
|    3    | $+0.02$ | $0.02$  |  $4$  |
|    5    | $-0.02$ | $0.02$  |  $4$  |
|    8    | $+0.02$ | $0.02$  |  $4$  |
|    6    | $+0.05$ | $0.05$  |  $7$  |

The five absolute differences equal to $0.02$ occupy ranks

$$2,3,4,5,6.$$

Their average rank is

$$\frac{2+3+4+5+6}{5}=4.$$

The observed positive rank sum is

$$W^+_{\mathrm{obs}}
=
1+4+4+4+4+7
=
24.$$

The observed negative rank sum is

$$W^-_{\mathrm{obs}}=4.$$

The total rank sum is

$$W^++W^-=24+4=28.$$

This also equals

$$\frac{m(m+1)}{2}
=
\frac{7(8)}{2}
=
28.$$

## Counting the Exact States

Under $H_0$, each of the seven ranks can independently receive a positive or negative sign. Therefore, the total number of possible sign states is

$$2^7=128.$$

The observed result has

$$W^+_{\mathrm{obs}}=24.$$

A result at least as favorable to PLTE requires

$$W^+\geq24.$$

Because the total rank sum is 28,

$$W^-=28-W^+.$$

Therefore,

$$W^+\geq24$$

is equivalent to

$$W^-\leq4.$$

The seven ranks are

$$1,\;4_a,\;4_b,\;4_c,\;4_d,\;4_e,\;7.$$

The possible states satisfying $W^-\leq4$ are:

1.  No negative ranks: 

$$W^-=0.$$

 This gives one state.

2.  Only rank $1$ is negative: 

$$W^-=1.$$

 This gives one state.

3.  Exactly one of the five rank-$4$ observations is negative: 

$$W^-=4.$$

 Since there are five distinct observations with rank $4$, this gives five states.

No other state qualifies. For example,

$$1+4=5>4,$$

and

$$7>4.$$

Therefore, the number of sign assignments at least as favorable to PLTE as the observed result is

$$1+1+5=7.$$

The exact one-sided $p$-value is consequently

$$\boxed{
p
=
\frac{7}{128}
=
0.0546875
\approx0.0547.
}$$

## Interpretation of the PLTE Example

The result should be interpreted as follows:

> Assuming PLTE has no systematic tendency to outperform SPE, the probability of obtaining a signed-rank statistic at least as favorable to PLTE as the observed statistic is approximately $5.47\%$.

It does not mean that there is a $5.47\%$ probability that the null hypothesis is true.

At the significance level

$$\alpha=0.05,$$

the result is not statistically significant because

$$0.0547>0.05.$$

Therefore, the null hypothesis is not rejected at the $5\%$ significance level. The observed results favor PLTE, but the evidence from these datasets does not cross the selected significance threshold.

## Comparison with the Paired $t$-Test

The paired $t$-test uses the raw paired differences:

$$t
=
\frac{\bar{d}}{s_d/\sqrt{n}}.$$

It tests whether the population mean difference is zero.

The Wilcoxon signed-rank test uses:

$$\operatorname{sign}(d_i)
\quad\text{and}\quad
\operatorname{rank}(|d_i|).$$

It tests for a systematic signed shift in the paired differences. A median-centered interpretation requires suitable symmetry assumptions.

The main differences are:

- the paired $t$-test uses the numerical magnitudes of the original differences;

- the Wilcoxon signed-rank test replaces the magnitudes with ranks;

- the paired $t$-test focuses on the mean difference;

- the Wilcoxon test is less sensitive to extreme numerical differences;

- both tests require meaningful pairing and independence between pairs.

## Assumptions

The Wilcoxon signed-rank test generally assumes:

1.  observations are paired meaningfully;

2.  pairs are independent of one another;

3.  the paired differences are at least ordinal and can be ranked;

4.  the distribution of the paired differences is approximately symmetric for the usual interpretation as a test of location;

5.  zero differences are removed before ranking.
