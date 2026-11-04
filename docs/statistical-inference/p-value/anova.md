# One-Way Analysis of Variance

!!! abstract "At a glance"
    One-way ANOVA compares variability between group means with variability within the groups:

    $$\boxed{
    F_{\mathrm{obs}}
    =
    \frac{
    MS_{\mathrm{Between}}
    }{
    MS_{\mathrm{Within}}
    }.
    }$$

    The main formulas are

    $$\boxed{
    SS_{\mathrm{Between}}
    =
    \sum_{i=1}^{k}
    n_i(\bar{x}_i-\bar{x})^2
    }$$

    $$\boxed{
    SS_{\mathrm{Within}}
    =
    \sum_{i=1}^{k}
    \sum_{j=1}^{n_i}
    (x_{ij}-\bar{x}_i)^2
    }$$

    $$\boxed{
    df_{\mathrm{Between}}=k-1
    }$$

    $$\boxed{
    df_{\mathrm{Within}}=N-k
    }$$

    and

    $$\boxed{
    p
    =
    P\left(
    F_{k-1,N-k}
    \geq
    F_{\mathrm{obs}}
    \right).
    }$$

    The complete process is

    $$\boxed{
    \text{independent groups}
    \rightarrow
    \text{between- and within-group variation}
    \rightarrow
    F_{\mathrm{obs}}
    \rightarrow
    F\text{-distribution}
    \rightarrow
    p\text{-value}.
    }$$


## Purpose

One-way analysis of variance, commonly called one-way ANOVA, tests whether the population means of three or more independent groups are equal.

For example, suppose four methods are evaluated using results from independent experimental units:

$$\text{Method A},\quad
\text{Method B},\quad
\text{Method C},\quad
\text{Method D}.$$

ANOVA tests whether the differences among the observed group means are larger than would reasonably be expected from random variation within the groups.

Although ANOVA is commonly used for three or more groups, it can also be used for two independent groups. With two groups, one-way ANOVA is equivalent to the equal-variance independent two-sample $t$-test:

$$F=t^2.$$

## When One-Way ANOVA Is Appropriate

One-way ANOVA is appropriate when:

- there is one categorical explanatory variable;

- the categorical variable contains two or more independent groups;

- the outcome variable is numerical;

- the objective is to compare the population means of the groups.

For example, the categorical variable may be the learning method:

$$\text{Method}\in\{A,B,C,D\},$$

and the numerical outcome may be AUCPR.

The word “one-way” means that the analysis contains one grouping factor.

## Notation

Suppose there are $k$ independent groups.

Let

$$x_{ij}$$

denote observation $j$ from group $i$, where

$$i=1,2,\ldots,k$$

and

$$j=1,2,\ldots,n_i.$$

Here:

- $k$ is the number of groups;

- $n_i$ is the number of observations in group $i$;

- $N$ is the total number of observations.

The total sample size is

$$N=\sum_{i=1}^{k}n_i.$$

The sample mean of group $i$ is

$$\bar{x}_i
=
\frac{1}{n_i}
\sum_{j=1}^{n_i}x_{ij}.$$

The grand mean across all observations is

$$\bar{x}
=
\frac{1}{N}
\sum_{i=1}^{k}
\sum_{j=1}^{n_i}x_{ij}.$$

Equivalently, the grand mean is the weighted average of the group means:

$$\bar{x}
=
\frac{
\sum_{i=1}^{k}n_i\bar{x}_i
}{
N
}.$$

## Hypotheses

The null hypothesis is that all population means are equal:

$$\boxed{
H_0:
\mu_1=\mu_2=\cdots=\mu_k.
}$$

The alternative hypothesis is:

$$\boxed{
H_1:
\text{not all population means are equal}.
}$$

The alternative does not mean that every pair of population means is different. It means that at least one population mean differs from at least one other population mean.

For example, with three groups, the alternative may be true if

$$\mu_1=\mu_2$$

but

$$\mu_3\neq\mu_1.$$

## Basic Idea

ANOVA separates the total variability in the observations into two components:

$$\boxed{
\text{total variability}
=
\text{between-group variability}
+
\text{within-group variability}.
}$$

Between-group variability measures how far the group means are from the grand mean.

Within-group variability measures how far individual observations are from their own group mean.

If $H_0$ is true, both quantities estimate the same underlying population variance.

If the population means differ, the between-group variability tends to be large relative to the within-group variability.

## Total Sum of Squares

The total sum of squares measures the total variability of all observations around the grand mean:

$$\boxed{
SS_{\mathrm{Total}}
=
\sum_{i=1}^{k}
\sum_{j=1}^{n_i}
(x_{ij}-\bar{x})^2.
}$$

## Between-Group Sum of Squares

The between-group sum of squares measures the variability of the group means around the grand mean:

$$\boxed{
SS_{\mathrm{Between}}
=
\sum_{i=1}^{k}
n_i(\bar{x}_i-\bar{x})^2.
}$$

Each squared difference is multiplied by $n_i$ because a group mean represents $n_i$ observations.

If all group means are close to the grand mean, then

$$SS_{\mathrm{Between}}$$

will be small.

If the group means are far apart, then

$$SS_{\mathrm{Between}}$$

will be large.

## Within-Group Sum of Squares

The within-group sum of squares measures the variability of observations around their respective group means:

$$\boxed{
SS_{\mathrm{Within}}
=
\sum_{i=1}^{k}
\sum_{j=1}^{n_i}
(x_{ij}-\bar{x}_i)^2.
}$$

This represents the variation that remains within groups after accounting for their different means.

It is also called the error sum of squares or residual sum of squares:

$$SS_{\mathrm{Error}}=SS_{\mathrm{Within}}.$$

## Decomposition of Variability

The total sum of squares can be decomposed as

$$\boxed{
SS_{\mathrm{Total}}
=
SS_{\mathrm{Between}}
+
SS_{\mathrm{Within}}.
}$$

To understand this decomposition, write

$$x_{ij}-\bar{x}
=
(x_{ij}-\bar{x}_i)
+
(\bar{x}_i-\bar{x}).$$

The total deviation of an observation from the grand mean is the sum of:

1.  its deviation from its group mean;

2.  its group mean’s deviation from the grand mean.

Squaring and summing over all observations produces the ANOVA decomposition.

## Degrees of Freedom

The total degrees of freedom are

$$\boxed{
df_{\mathrm{Total}}=N-1.
}$$

The between-group degrees of freedom are

$$\boxed{
df_{\mathrm{Between}}=k-1.
}$$

The within-group degrees of freedom are

$$\boxed{
df_{\mathrm{Within}}=N-k.
}$$

These satisfy

$$df_{\mathrm{Total}}
=
df_{\mathrm{Between}}
+
df_{\mathrm{Within}}.$$

Indeed,

$$N-1=(k-1)+(N-k).$$

## Mean Squares

The sums of squares depend on the number of observations and groups. Therefore, each sum of squares is divided by its degrees of freedom.

The between-group mean square is

$$\boxed{
MS_{\mathrm{Between}}
=
\frac{
SS_{\mathrm{Between}}
}{
k-1
}.
}$$

The within-group mean square is

$$\boxed{
MS_{\mathrm{Within}}
=
\frac{
SS_{\mathrm{Within}}
}{
N-k
}.
}$$

The within-group mean square estimates the common population variance under the equal-variance ANOVA model.

## The $F$-Statistic

The ANOVA test statistic is

$$\boxed{
F_{\mathrm{obs}}
=
\frac{
MS_{\mathrm{Between}}
}{
MS_{\mathrm{Within}}
}.
}$$

More explicitly,

$$\boxed{
F_{\mathrm{obs}}
=
\frac{
SS_{\mathrm{Between}}/(k-1)
}{
SS_{\mathrm{Within}}/(N-k)
}.
}$$

The $F$-statistic compares variability between the group means with variability within the groups.

If $H_0$ is true, both mean squares estimate the same population variance, so their ratio should generally be near one:

$$F_{\mathrm{obs}}\approx1.$$

If the group means differ substantially, the between-group mean square becomes large relative to the within-group mean square:

$$F_{\mathrm{obs}}>1.$$

A sufficiently large $F$-value provides evidence against $H_0$.

## Theoretical $F$-Distribution

Under the null hypothesis, the ANOVA statistic follows an $F$-distribution:

$$F\sim F_{\nu_1,\nu_2},$$

where

$$\nu_1=k-1$$

is the numerator degrees of freedom and

$$\nu_2=N-k$$

is the denominator degrees of freedom.

The probability density function of an $F$-distribution is

$$f(x;\nu_1,\nu_2)
=
\frac{
1
}{
B\left(\frac{\nu_1}{2},\frac{\nu_2}{2}\right)
}
\left(
\frac{\nu_1}{\nu_2}
\right)^{\nu_1/2}
x^{\nu_1/2-1}
\left(
1+\frac{\nu_1}{\nu_2}x
\right)^{-(\nu_1+\nu_2)/2},
\qquad x>0.$$

Here:

- $x$ is a possible value of the $F$-statistic;

- $\nu_1$ is the numerator degrees of freedom;

- $\nu_2$ is the denominator degrees of freedom;

- $B(\cdot,\cdot)$ is the beta function.

The beta function is related to the gamma function by

$$B(a,b)
=
\frac{
\Gamma(a)\Gamma(b)
}{
\Gamma(a+b)
}.$$

The $F$-distribution contains only nonnegative values and is generally right-skewed.

## Computing the $p$-Value

Large values of the $F$-statistic provide evidence against the null hypothesis. Therefore, ANOVA uses the right tail of the $F$-distribution:

$$\boxed{
p
=
P\left(
F_{\nu_1,\nu_2}
\geq
F_{\mathrm{obs}}
\mid H_0
\right).
}$$

If $G_{\nu_1,\nu_2}$ denotes the cumulative distribution function of the $F$-distribution, then

$$\boxed{
p
=
1-
G_{\nu_1,\nu_2}
(F_{\mathrm{obs}}).
}$$

The standard ANOVA test does not use separate left-sided, right-sided, or two-sided alternatives. Deviations among group means in any direction increase the between-group sum of squares and therefore increase the $F$-statistic.

## Numerical Example

Suppose three independent methods produce the following scores:

$$\text{Method A}: 8,\;9,\;7,$$

$$\text{Method B}: 5,\;6,\;4,$$

$$\text{Method C}: 7,\;8,\;6.$$

There are

$$k=3$$

groups and

$$N=9$$

observations.

The group means are

$$\bar{x}_1=\frac{8+9+7}{3}=8,$$

$$\bar{x}_2=\frac{5+6+4}{3}=5,$$

and

$$\bar{x}_3=\frac{7+8+6}{3}=7.$$

The grand mean is

$$\bar{x}
=
\frac{
8+9+7+5+6+4+7+8+6
}{
9
}
=
\frac{60}{9}
=
\frac{20}{3}.$$

The between-group sum of squares is

$$\begin{aligned}
SS_{\mathrm{Between}}
={}&
3\left(8-\frac{20}{3}\right)^2
+
3\left(5-\frac{20}{3}\right)^2\\
&+
3\left(7-\frac{20}{3}\right)^2.
\end{aligned}$$

Therefore,

$$SS_{\mathrm{Between}}=14.$$

The within-group sum of squares is

$$\begin{aligned}
SS_{\mathrm{Within}}
={}&
\left[(8-8)^2+(9-8)^2+(7-8)^2\right]\\
&+
\left[(5-5)^2+(6-5)^2+(4-5)^2\right]\\
&+
\left[(7-7)^2+(8-7)^2+(6-7)^2\right].
\end{aligned}$$

Thus,

$$SS_{\mathrm{Within}}=6.$$

The degrees of freedom are

$$df_{\mathrm{Between}}=k-1=2,$$

and

$$df_{\mathrm{Within}}=N-k=6.$$

The mean squares are

$$MS_{\mathrm{Between}}
=
\frac{14}{2}
=
7,$$

and

$$MS_{\mathrm{Within}}
=
\frac{6}{6}
=
1.$$

Therefore, the observed $F$-statistic is

$$\boxed{
F_{\mathrm{obs}}
=
\frac{7}{1}
=
7.
}$$

Under $H_0$,

$$F\sim F_{2,6}.$$

The $p$-value is

$$p=P(F_{2,6}\geq7).$$

A small right-tail probability provides evidence that not all three population means are equal.

## ANOVA Table

The calculations are commonly summarized using an ANOVA table:

| Source | Sum of squares | Degrees of freedom | Mean square | $F$ |
|:---|:--:|:--:|:--:|:--:|
| Between groups | $SS_{\mathrm{Between}}$ | $k-1$ | $MS_{\mathrm{Between}}$ | $F_{\mathrm{obs}}$ |
| Within groups | $SS_{\mathrm{Within}}$ | $N-k$ | $MS_{\mathrm{Within}}$ |  |
| Total | $SS_{\mathrm{Total}}$ | $N-1$ |  |  |

For the numerical example:

| Source         | Sum of squares | Degrees of freedom | Mean square | $F$ |
|:---------------|:--------------:|:------------------:|:-----------:|:---:|
| Between groups |      $14$      |        $2$         |     $7$     | $7$ |
| Within groups  |      $6$       |        $6$         |     $1$     |     |
| Total          |      $20$      |        $8$         |             |     |

## Interpreting a Significant Result

A significant ANOVA result supports the conclusion that

$$\text{not all population means are equal}.$$

It does not identify which specific groups differ.

For example, rejecting

$$H_0:\mu_1=\mu_2=\mu_3$$

does not directly tell us whether:

$$\mu_1\neq\mu_2,$$

$$\mu_1\neq\mu_3,$$

or

$$\mu_2\neq\mu_3.$$

Post-hoc comparisons are required to determine which group pairs differ.

A common post-hoc procedure for the equal-variance one-way ANOVA is Tukey’s honestly significant difference procedure.

When performing many pairwise tests, multiplicity must be controlled to avoid increasing the probability of a false positive.

## Effect Size

A small $p$-value indicates evidence that the population means are not all equal, but it does not measure the size of the group effect.

One effect-size measure is eta squared:

$$\boxed{
\eta^2
=
\frac{
SS_{\mathrm{Between}}
}{
SS_{\mathrm{Total}}
}.
}$$

Eta squared represents the proportion of total sample variability associated with group membership.

Another measure is omega squared:

$$\boxed{
\omega^2
=
\frac{
SS_{\mathrm{Between}}
-
(k-1)MS_{\mathrm{Within}}
}{
SS_{\mathrm{Total}}
+
MS_{\mathrm{Within}}
}.
}$$

Omega squared includes a correction intended to reduce the upward bias of sample eta squared.

## Assumptions

Classical one-way ANOVA generally assumes:

1.  observations are independent;

2.  the outcome variable is numerical;

3.  observations within each group are approximately normally distributed, particularly for small samples;

4.  the population variances are equal across groups;

5.  extreme outliers do not dominate the group means and variances.

The equal-variance assumption can be written as

$$\sigma_1^2
=
\sigma_2^2
=
\cdots
=
\sigma_k^2.$$

If equal variances are doubtful, Welch’s ANOVA is generally more appropriate because it does not require equal population variances.

## Independent Versus Repeated-Measures ANOVA

Ordinary one-way ANOVA assumes that the groups are independent.

If the same datasets, subjects, or experimental units are evaluated under every method, the observations are paired rather than independent.

For example, if Methods A, B, C, and D are all evaluated on the same ten datasets, ordinary one-way ANOVA is not appropriate because the scores within each dataset are related.

In that case, an appropriate method may be:

- repeated-measures ANOVA, under suitable parametric assumptions; or

- the Friedman test, as a rank-based nonparametric alternative.

For comparing several machine-learning methods over the same datasets, the repeated-measures structure must therefore be considered.
