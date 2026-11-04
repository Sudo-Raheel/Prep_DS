# Paired $t$-Test

!!! abstract "At a glance"
    The paired $t$-test first converts two matched measurements into one set of differences:

    $$(x_i,y_i)\longrightarrow d_i=x_i-y_i.$$

    It then applies a one-sample $t$-test to those differences:

    $$\boxed{
    t_{\mathrm{obs}}
    =
    \frac{\bar{d}}{s_d/\sqrt{n}},
    \qquad
    df=n-1
    }$$

    For two methods evaluated on ten datasets:

    $$\boxed{
    t_{\mathrm{obs}}
    =
    \frac{\bar{d}}{s_d/\sqrt{10}},
    \qquad
    df=9
    }$$

    The complete process is

    $$\boxed{
    \text{paired results}
    \rightarrow
    \text{paired differences}
    \rightarrow
    t_{\mathrm{obs}}
    \rightarrow
    df=n-1
    \rightarrow
    \text{tail probability}
    \rightarrow
    p\text{-value}
    }.$$

    Paste this into your main .tex file:


## Purpose

A paired $t$-test compares two methods or conditions evaluated on the same experimental units or on matched observations.

Examples include:

- Methods A and B evaluated on the same datasets;

- two models evaluated over the same months;

- measurements taken before and after an intervention;

- two approaches evaluated on matched subjects.

The important requirement is a one-to-one correspondence between the observations:

$$(x_1,y_1),(x_2,y_2),\ldots,(x_n,y_n).$$

The two columns are not treated as independent samples. Instead, the paired $t$-test analyzes the difference within each pair.

## Paired Differences

For each pair $i$, define

$$d_i=x_i-y_i.$$

The mean difference is

$$\bar{d}
=
\frac{1}{n}\sum_{i=1}^{n}d_i.$$

The sample standard deviation of the differences is

$$s_d
=
\sqrt{
\frac{
\sum_{i=1}^{n}(d_i-\bar{d})^2
}{
n-1
}
}.$$

The standard error of the mean difference is

$$SE(\bar{d})=\frac{s_d}{\sqrt{n}}.$$

A paired $t$-test is therefore equivalent to applying a one-sample $t$-test to the paired differences.

## Hypotheses

Let $\mu_d$ denote the population mean of the paired differences.

For a two-sided test,

$$H_0:\mu_d=0,$$

$$H_1:\mu_d\neq 0.$$

For a right-sided test,

$$H_0:\mu_d=0,$$

$$H_1:\mu_d>0.$$

For a left-sided test,

$$H_0:\mu_d=0,$$

$$H_1:\mu_d<0.$$

The direction depends on how the differences are defined.

For example, if a larger score is better and

$$d_i=\text{Score}_{A,i}-\text{Score}_{B,i},$$

then the claim that Method A is better corresponds to

$$H_1:\mu_d>0.$$

If a smaller value is better, such as error or loss, the differences can instead be defined as

$$d_i=\text{Loss}_{B,i}-\text{Loss}_{A,i}.$$

With this definition, positive differences again indicate that Method A is better.

## Test Statistic

The paired $t$-statistic is

$$\boxed{
t_{\mathrm{obs}}
=
\frac{\bar{d}}{s_d/\sqrt{n}}
}$$

or, more generally,

$$t_{\mathrm{obs}}
=
\frac{\bar{d}-\mu_{d,0}}{s_d/\sqrt{n}},$$

where the null value is normally

$$\mu_{d,0}=0.$$

The statistic measures how many standard errors the observed mean difference is away from zero.

For example, if

$$t_{\mathrm{obs}}=3,$$

then the average paired difference is three estimated standard errors above zero.

## Degrees of Freedom

For a paired $t$-test,

$$\boxed{df=n-1}$$

where $n$ is the number of pairs, not the total number of individual measurements.

## Example: Comparing Two Methods Across Ten Datasets

Suppose Methods A and B are evaluated on the same ten datasets.

Let

$$A_i=\text{score of Method A on dataset }i,$$

and

$$B_i=\text{score of Method B on dataset }i.$$

For a higher-is-better metric, define

$$d_i=A_i-B_i,
\qquad i=1,\ldots,10.$$

The hypotheses for claiming that Method A is better are

$$H_0:\mu_d=0,$$

$$H_1:\mu_d>0.$$

The average difference is

$$\bar{d}
=
\frac{1}{10}\sum_{i=1}^{10}d_i.$$

The standard deviation of the differences is

$$s_d
=
\sqrt{
\frac{
\sum_{i=1}^{10}(d_i-\bar{d})^2
}{
10-1
}
}.$$

The observed test statistic is

$$\boxed{
t_{\mathrm{obs}}
=
\frac{\bar{d}}{s_d/\sqrt{10}}
}$$

and the degrees of freedom are

$$\boxed{df=10-1=9}.$$

## Computing the $p$-Value

Under the null hypothesis,

$$T\sim t_9.$$

For the one-sided claim that Method A is better,

$$H_1:\mu_d>0,$$

the $p$-value is the right-tail probability

$$\boxed{
p=P(T_9\geq t_{\mathrm{obs}})
}.$$

For a two-sided comparison,

$$H_1:\mu_d\neq 0,$$

the $p$-value is

$$p
=
P(T_9\leq-|t_{\mathrm{obs}}|)
+
P(T_9\geq|t_{\mathrm{obs}}|).$$

Since the $t$-distribution is symmetric,

$$p=2P(T_9\geq|t_{\mathrm{obs}}|).$$

## Role of Dataset Sizes

Suppose the ten datasets contain different numbers of observations:

$$N_1,N_2,\ldots,N_{10}.$$

These dataset sizes do not directly appear in the standard paired $t$-test. Each dataset produces one paired difference:

$$d_i=A_i-B_i.$$

The sample size used by the paired $t$-test is therefore the number of datasets:

$$n=10.$$

Each dataset receives equal weight, regardless of its number of observations.

Consequently, a small dataset and a large dataset each contribute one difference to the test. If this equal weighting is not appropriate, a weighted analysis or a model that accounts for within-dataset uncertainty may be needed.

## Assumptions

The paired $t$-test generally assumes:

1.  each observation in one condition has a meaningful match in the other condition;

2.  the pairs are independent of one another;

3.  the differences $d_1,d_2,\ldots,d_n$ are numerical;

4.  the distribution of the paired differences is approximately normal, especially when the number of pairs is small;

5.  the differences do not contain extreme outliers that dominate their mean and standard deviation.

The two original score distributions do not individually need to be normal. The relevant assumption concerns the distribution of the differences:

$$d_i=x_i-y_i.$$
