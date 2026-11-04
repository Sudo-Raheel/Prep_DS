# Introduction

A $p$-value is the probability, assuming the null hypothesis $H_0$ is true, of obtaining a test statistic at least as extreme as the one observed.

In general, hypothesis testing follows this structure: 

$$\text{data}
\rightarrow
\text{test statistic}
\rightarrow
\text{reference distribution under }H_0
\rightarrow
\text{tail probability}
\rightarrow
p\text{-value}.$$

Different statistical tests use different test statistics and reference distributions. This document will be expanded gradually, one statistical test at a time.

## Theoretical $t$-Distribution

Under the null hypothesis, the test statistic follows a Student’s $t$-distribution with a specified number of degrees of freedom: 

$$T\sim t_{\nu},$$

 where $\nu$ denotes the degrees of freedom. The probability density function of the theoretical $t$-distribution is 

$$f(t;\nu) = \frac{ \Gamma\left(\frac{\nu+1}{2}\right) }{ \sqrt{\nu\pi}\, \Gamma\left(\frac{\nu}{2}\right) } \left( 1+\frac{t^2}{\nu} \right)^{-\frac{\nu+1}{2}}.$$

 Here:

- $t$ is a possible value of the test statistic;

- $f(t;\nu)$ is the probability density at $t$;

- $\nu$ is the number of degrees of freedom;

- $\pi$ is the constant approximately equal to $3.14159$;

- $\Gamma(\cdot)$ is the gamma function.

For positive integers $k$, the gamma function satisfies 

$$\Gamma(k)=(k-1)!.$$

 The first part, 

$$\frac{ \Gamma\left(\frac{\nu+1}{2}\right) }{ \sqrt{\nu\pi}\, \Gamma\left(\frac{\nu}{2}\right) },$$

 is a normalizing constant. It ensures that the total area under the density curve is equal to one: 

$$\int_{-\infty}^{\infty} f(t;\nu)\,dt=1.$$

 The second part, 

$$\left( 1+\frac{t^2}{\nu} \right)^{-\frac{\nu+1}{2}},$$

 controls the shape and tail thickness of the distribution. Because the density depends on $t^2$, 

$$f(-t;\nu)=f(t;\nu).$$

 Therefore, the $t$-distribution is symmetric around zero. For small values of $\nu$, the distribution has heavier tails. This reflects the additional uncertainty caused by estimating the unknown population standard deviation from a small sample. As the degrees of freedom increase, 

$$t_{\nu}\longrightarrow N(0,1),$$

 so the $t$-distribution approaches the standard normal distribution. The cumulative distribution function is 

$$F_{\nu}(t) = P(T\leq t) = \int_{-\infty}^{t}f(u;\nu)\,du.$$

 The $p$-value is calculated as an area under this theoretical distribution. For example, for a two-sided test, 

$$p = P(T\leq-|t_{\mathrm{obs}}|) + P(T\geq|t_{\mathrm{obs}}|).$$

 Because the distribution is symmetric, 

$$p = 2P(T\geq|t_{\mathrm{obs}}|) = 2\left[1-F_{\nu}(|t_{\mathrm{obs}}|)\right].$$

 The density and cumulative probabilities are normally evaluated using statistical software rather than calculated manually.

# One-Sample $t$-Test

## Purpose

A one-sample $t$-test uses one sample from a population and tests whether the unknown population mean $\mu$ equals a fixed hypothesized value $\mu_0$.

The null hypothesis is 

$$H_0:\mu=\mu_0.$$

The alternative hypothesis depends on the research question: 

$$H_1:\mu>\mu_0 \qquad \text{(right-sided)},$$

 

$$H_1:\mu<\mu_0 \qquad \text{(left-sided)},$$

 

$$H_1:\mu\neq\mu_0 \qquad \text{(two-sided)}.$$

## Test Statistic

The observed test statistic is 

$$t_{\mathrm{obs}}=\frac{\bar{x}-\mu_0}{s/\sqrt{n}},$$

 where

- $\bar{x}$ is the sample mean,

- $\mu_0$ is the hypothesized population mean,

- $s$ is the sample standard deviation,

- $n$ is the sample size,

- $s/\sqrt{n}$ is the standard error of the sample mean.

The sample standard deviation is 

$$s=\sqrt{\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}}.$$

The $n-1$ in this formula corrects the estimate of the population variance because the sample mean is estimated from the data.

## Why Is $s$ Divided by $\sqrt{n}$?

The value $s$ estimates the spread of individual observations. The test statistic requires the spread of the sample mean, called its standard error.

For independent observations with population variance $\sigma^2$, 

$$\operatorname{Var}(\bar{X})
=\operatorname{Var}\left(\frac{X_1+\cdots+X_n}{n}\right)
=\frac{\sigma^2}{n}.$$

Therefore, 

$$\operatorname{SD}(\bar{X})=\frac{\sigma}{\sqrt{n}}.$$

Since $\sigma$ is unknown, it is estimated using $s$: 

$$SE(\bar{X})=\frac{s}{\sqrt{n}}.$$

Thus, $n-1$ and $\sqrt{n}$ have different roles:

- $n-1$ is used when estimating the population variance;

- $\sqrt{n}$ accounts for the reduction in uncertainty produced by averaging $n$ independent observations.

## Degrees of Freedom

For a one-sample $t$-test, 

$$df=n-1.$$

One degree of freedom is lost because the sample mean $\bar{x}$ is estimated from the same observations.

The degrees of freedom determine the shape of the reference $t$-distribution:

- small $df$: wider distribution with heavier tails;

- large $df$: the distribution approaches the standard normal distribution.

The standard $t$-distribution is symmetric around zero for every value of $df$.

## Observed $t$ and Random $T$

The lowercase $t_{\mathrm{obs}}$ is the single value calculated from the available sample: 

$$t_{\mathrm{obs}}=\frac{\bar{x}-\mu_0}{s/\sqrt{n}}.$$

The capital $T$ represents the random test statistic under the assumption that $H_0$ is true: 

$$T\sim t_{df}.$$

Repeated samples are a theoretical thought experiment. Imagine repeatedly drawing samples of size $n$ from a population whose mean is $\mu_0$. Each sample would have a different mean, standard deviation, and $t$-value because of random variation. The theoretical collection of these possible $t$-values follows the $t$-distribution.

In practice, only one sample and one observed $t$-value are needed. That observed value is compared with the theoretical reference distribution.

## Computing the $p$-Value

The $p$-value is a tail probability under the null distribution. Let $F_{t_{df}}$ denote the cumulative distribution function of the $t$-distribution.

### Right-Sided Test

For 

$$H_1:\mu>\mu_0,$$

 large positive values of $T$ support the alternative. Therefore, 

$$p=P(T\geq t_{\mathrm{obs}})
=1-F_{t_{df}}(t_{\mathrm{obs}}).$$

### Left-Sided Test

For 

$$H_1:\mu<\mu_0,$$

 large negative values of $T$ support the alternative. Therefore, 

$$p=P(T\leq t_{\mathrm{obs}})
=F_{t_{df}}(t_{\mathrm{obs}}).$$

### Two-Sided Test

For 

$$H_1:\mu\neq\mu_0,$$

 both unusually positive and unusually negative values contradict $H_0$.

A value is at least as extreme as the observed statistic when 

$$|T|\geq |t_{\mathrm{obs}}|.$$

This is equivalent to 

$$T\leq -|t_{\mathrm{obs}}|
\quad \text{or} \quad
T\geq |t_{\mathrm{obs}}|.$$

Therefore, 

$$p=P(T\leq -|t_{\mathrm{obs}}|)
 +P(T\geq |t_{\mathrm{obs}}|).$$

Since the $t$-distribution is symmetric around zero, the two tail areas are equal: 

$$p=2P(T\geq |t_{\mathrm{obs}}|)
=2\left[1-F_{t_{df}}\left(|t_{\mathrm{obs}}|\right)\right].$$

The expression 

$$P(T\leq |t|)+P(T\geq |t|)$$

 is incorrect because its first term includes the middle of the distribution. The correct left-tail boundary is $-|t|$.

## Numerical Example

Suppose 

$$\bar{x}=105,\qquad
\mu_0=100,\qquad
s=10,\qquad
n=25.$$

The standard error is 

$$SE=\frac{10}{\sqrt{25}}=2.$$

The observed statistic is 

$$t_{\mathrm{obs}}=\frac{105-100}{2}=2.5.$$

The degrees of freedom are 

$$df=25-1=24.$$

For $t_{\mathrm{obs}}=2.5$ and $df=24$, the right-tail area is approximately $0.0098$.

| Test        | Alternative hypothesis | Approximate $p$-value |
|:------------|:-----------------------|:----------------------|
| Right-sided | $\mu>\mu_0$            | $0.0098$              |
| Left-sided  | $\mu<\mu_0$            | $0.9902$              |
| Two-sided   | $\mu\neq\mu_0$         | $2(0.0098)=0.0196$    |

## Effect of Sample Size

The statistic can also be written as 

$$t_{\mathrm{obs}}
=\frac{(\bar{x}-\mu_0)\sqrt{n}}{s}.$$

If the observed difference $\bar{x}-\mu_0$ and standard deviation $s$ remain fixed, increasing $n$ reduces the standard error and increases $|t_{\mathrm{obs}}|$.

In an actual new sample, however, both $\bar{x}$ and $s$ can also change. Therefore, a larger sample does not guarantee a larger observed $t$-value in every dataset.

## Assumptions

A one-sample $t$-test generally assumes:

1.  the observations are independent;

2.  the outcome is numerical;

3.  the population is approximately normal when the sample is small, or the sampling distribution of the mean is approximately normal for a sufficiently large sample;

4.  extreme outliers do not dominate the mean and standard deviation.

## Summary

$$\boxed{
\text{sample}
\rightarrow t_{\mathrm{obs}}
\rightarrow df=n-1
\rightarrow \text{tail area under }t_{df}
\rightarrow p\text{-value}
}$$

A one-sample $t$-test produces one observed $t$-value from the sample. The reference $t$-distribution represents the possible values of the statistic under $H_0$, and the alternative hypothesis determines whether the left tail, right tail, or both tails are used.

# Independent Two-Sample $t$-Test

## Purpose

Welch’s $t$-test compares the population means of two independent groups. Let the two population means be $\mu_1$ and $\mu_2$. The null hypothesis is 

$$H_0:\mu_1=\mu_2,$$

 or equivalently, 

$$H_0:\mu_1-\mu_2=0.$$

 A two-sided alternative is 

$$H_1:\mu_1\neq\mu_2.$$

 The groups must be independent. This means that an observation in Group 1 is not naturally paired with an observation in Group 2. Welch’s $t$-test does not assume that the two population variances are equal. It is therefore generally preferred over the equal-variance Student’s two-sample $t$-test.

## Notation

For Group 1: 

$$x_{11},x_{12},\ldots,x_{1n_1}$$

 and for Group 2: 

$$x_{21},x_{22},\ldots,x_{2n_2}.$$

 The sample means are 

$$\bar{x}_1=\frac{1}{n_1}\sum_{i=1}^{n_1}x_{1i},$$

 and 

$$\bar{x}_2=\frac{1}{n_2}\sum_{i=1}^{n_2}x_{2i}.$$

 The sample standard deviations are 

$$s_1= \sqrt{ \frac{ \sum_{i=1}^{n_1}(x_{1i}-\bar{x}_1)^2 }{ n_1-1 } },$$

 and 

$$s_2= \sqrt{ \frac{ \sum_{i=1}^{n_2}(x_{2i}-\bar{x}_2)^2 }{ n_2-1 } }.$$

 Here,

- $n_1$ is the sample size of Group 1;

- $n_2$ is the sample size of Group 2;

- $\bar{x}_1$ and $\bar{x}_2$ are the sample means;

- $s_1$ and $s_2$ are the sample standard deviations;

- $s_1^2$ and $s_2^2$ are the sample variances.

## Welch’s Test Statistic

Welch’s test statistic is 

$$t_{\mathrm{obs}} = \frac{ \bar{x}_1-\bar{x}_2 }{ \sqrt{ \frac{s_1^2}{n_1} + \frac{s_2^2}{n_2} } }.$$

 The numerator, 

$$\bar{x}_1-\bar{x}_2,$$

 is the observed difference between the two sample means. Under the null hypothesis, the expected difference is zero. Therefore, the more general form is 

$$t_{\mathrm{obs}} = \frac{ (\bar{x}_1-\bar{x}_2)-0 }{ SE(\bar{X}_1-\bar{X}_2) }.$$

## Intuitive Meaning of the $t$-Statistic

The Welch $t$-statistic measures how many standard errors the observed difference between the sample means is away from zero. For example, if 

$$t_{\mathrm{obs}}=3,$$

 then the observed difference between the sample means is three standard errors above zero. A large absolute value, 

$$|t_{\mathrm{obs}}|,$$

 indicates that the difference between the means is large relative to its sampling uncertainty.

## Standard Error of the Difference

The variance of each sample mean is estimated as 

$$\operatorname{Var}(\bar{X}_1) \approx \frac{s_1^2}{n_1},$$

 and 

$$\operatorname{Var}(\bar{X}_2) \approx \frac{s_2^2}{n_2}.$$

 For any two random variables $A$ and $B$, 

$$\operatorname{Var}(A-B) = \operatorname{Var}(A) + \operatorname{Var}(B) - 2\operatorname{Cov}(A,B).$$

 This follows from 

$$\operatorname{Var}(A-B) = E\left[ \left( (A-E[A])-(B-E[B]) \right)^2 \right].$$

 Expanding the square gives 

$$\begin{aligned} \operatorname{Var}(A-B) ={}& E[(A-E[A])^2] + E[(B-E[B])^2] \\ &- 2E[(A-E[A])(B-E[B])]. \end{aligned}$$

 Therefore, 

$$\operatorname{Var}(A-B) = \operatorname{Var}(A) + \operatorname{Var}(B) - 2\operatorname{Cov}(A,B).$$

 Because the two samples are independent, 

$$\operatorname{Cov}(\bar{X}_1,\bar{X}_2)=0.$$

 Thus, 

$$\operatorname{Var}(\bar{X}_1-\bar{X}_2) = \operatorname{Var}(\bar{X}_1) + \operatorname{Var}(\bar{X}_2).$$

 Substituting the estimated variances gives 

$$\operatorname{Var}(\bar{X}_1-\bar{X}_2) \approx \frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}.$$

 Taking the square root gives the standard error: 

$$SE(\bar{X}_1-\bar{X}_2) = \sqrt{ \frac{s_1^2}{n_1} + \frac{s_2^2}{n_2} }.$$

 The variance terms are added even though the sample means are subtracted. The minus sign affects the covariance term, but the covariance is zero when the groups are independent.

## Welch’s Degrees of Freedom

Welch’s $t$-statistic does not generally follow a $t$-distribution with $n_1+n_2-2$ degrees of freedom. Instead, the degrees of freedom are approximated using the Welch–Satterthwaite formula: 

$$df = \frac{ \left( \frac{s_1^2}{n_1} + \frac{s_2^2}{n_2} \right)^2 }{ \frac{ \left(\frac{s_1^2}{n_1}\right)^2 }{ n_1-1 } + \frac{ \left(\frac{s_2^2}{n_2}\right)^2 }{ n_2-1 } }.$$

 The resulting $df$ need not be an integer. Statistical software can use the non-integer value directly.

## Computing the $p$-Value

After calculating $t_{\mathrm{obs}}$ and the Welch degrees of freedom, the $p$-value is computed from the corresponding $t$-distribution: 

$$T\sim t_{df}.$$

 The calculation is similar to the one-sample $t$-test.

### Right-Sided Test

For 

$$H_1:\mu_1>\mu_2,$$

 the $p$-value is 

$$p=P(T\geq t_{\mathrm{obs}}).$$

### Left-Sided Test

For 

$$H_1:\mu_1<\mu_2,$$

 the $p$-value is 

$$p=P(T\leq t_{\mathrm{obs}}).$$

### Two-Sided Test

For 

$$H_1:\mu_1\neq\mu_2,$$

 both positive and negative differences are relevant. Therefore, 

$$p = P(T\leq-|t_{\mathrm{obs}}|) + P(T\geq|t_{\mathrm{obs}}|).$$

 Since the $t$-distribution is symmetric around zero, 

$$p=2P(T\geq|t_{\mathrm{obs}}|).$$

## Assumptions

Welch’s independent two-sample $t$-test generally assumes:

1.  the two groups are independent;

2.  observations within each group are independent;

3.  the outcome variable is numerical;

4.  the population distributions are approximately normal for small samples, or the sample means are approximately normal for sufficiently large samples;

5.  there are no extreme outliers that dominate the sample means and variances.

Equal population variances and equal sample sizes are not required.

## Summary

$$\boxed{ t_{\mathrm{obs}} = \frac{ \text{observed difference between means} }{ \text{standard error of the difference} } }$$

 More explicitly, 

$$\boxed{ t_{\mathrm{obs}} = \frac{ \bar{x}_1-\bar{x}_2 }{ \sqrt{ s_1^2/n_1+s_2^2/n_2 } } }$$

 The complete process is 

$$\boxed{ \text{two independent samples} \rightarrow t_{\mathrm{obs}} \rightarrow \text{Welch }df \rightarrow \text{tail area under }t_{df} \rightarrow p\text{-value} }$$

 Paste this into the main .tex file as the next section:

# Paired $t$-Test

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

## Summary

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

# $z$-Test

## Purpose

A $z$-test is used when the test statistic follows the standard normal distribution:

$$Z\sim N(0,1).$$

For testing a population mean, a $z$-test is appropriate when the population standard deviation $\sigma$ is known.

The null hypothesis is

$$H_0:\mu=\mu_0.$$

The alternative hypothesis may be

$$H_1:\mu>\mu_0
\qquad \text{(right-sided)},$$

$$H_1:\mu<\mu_0
\qquad \text{(left-sided)},$$

or

$$H_1:\mu\neq\mu_0
\qquad \text{(two-sided)}.$$

## When Is the Population Standard Deviation Known?

The population standard deviation $\sigma$ may be considered known when:

- a manufacturing process has been monitored extensively and its variability is well established;

- a calibrated measurement device has a known measurement-error standard deviation;

- data are generated from a simulation with a specified population standard deviation;

- a trusted population-level source provides a fixed value of $\sigma$.

In most practical studies, the true population standard deviation is unknown. Examples include:

- a new experiment;

- customer behaviour measured from a sample;

- performance of a new fraud-detection method;

- a population for which only sample observations are available.

When $\sigma$ is unknown, it is estimated using the sample standard deviation $s$, and a $t$-test is generally used instead.

## One-Sample $z$-Statistic

Suppose a sample of size $n$ has mean $\bar{x}$, and the known population standard deviation is $\sigma$.

The standard error of the sample mean is

$$SE(\bar{X})=\frac{\sigma}{\sqrt{n}}.$$

The observed $z$-statistic is

$$\boxed{
z_{\mathrm{obs}}
=
\frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}
}.$$

The $z$-statistic measures how many known standard errors the observed sample mean is away from the hypothesized population mean.

For example, if

$$z_{\mathrm{obs}}=2,$$

then the sample mean is two standard errors above the hypothesized mean.

## Why Is the Normal Distribution Used?

When the population standard deviation $\sigma$ is known, the standardized sample mean is

$$Z
=
\frac{\bar{X}-\mu_0}{\sigma/\sqrt{n}}.$$

Under the null hypothesis, this statistic follows the standard normal distribution:

$$Z\sim N(0,1),$$

provided the population is normal. For sufficiently large samples, this also follows approximately from the central limit theorem under suitable conditions.

Unlike a $t$-test, the $z$-test does not introduce additional uncertainty by replacing $\sigma$ with the sample estimate $s$.

## Standard Normal Distribution

The probability density function of the standard normal distribution is

$$\phi(z)
=
\frac{1}{\sqrt{2\pi}}
\exp\left(-\frac{z^2}{2}\right).$$

Here:

- $z$ is a possible value of the standardized test statistic;

- $\phi(z)$ is the probability density at $z$;

- $\pi$ is approximately $3.14159$;

- $\exp(a)=e^a$.

The cumulative distribution function is

$$\Phi(z)
=
P(Z\leq z)
=
\int_{-\infty}^{z}\phi(u)\,du.$$

The standard normal distribution is symmetric around zero:

$$\phi(-z)=\phi(z).$$

Unlike the $t$-distribution, its shape does not depend on degrees of freedom.

## Computing the $p$-Value

After calculating $z_{\mathrm{obs}}$, the $p$-value is obtained from the standard normal distribution.

### Right-Sided Test

For

$$H_1:\mu>\mu_0,$$

the $p$-value is

$$p=P(Z\geq z_{\mathrm{obs}})
=1-\Phi(z_{\mathrm{obs}}).$$

### Left-Sided Test

For

$$H_1:\mu<\mu_0,$$

the $p$-value is

$$p=P(Z\leq z_{\mathrm{obs}})
=\Phi(z_{\mathrm{obs}}).$$

### Two-Sided Test

For

$$H_1:\mu\neq\mu_0,$$

the $p$-value includes both tails:

$$p
=
P(Z\leq-|z_{\mathrm{obs}}|)
+
P(Z\geq|z_{\mathrm{obs}}|).$$

Because the standard normal distribution is symmetric,

$$\boxed{
p
=
2P(Z\geq|z_{\mathrm{obs}}|)
=
2\left[1-\Phi(|z_{\mathrm{obs}}|)\right]
}.$$

## Numerical Example

Suppose

$$\bar{x}=105,\qquad
\mu_0=100,\qquad
\sigma=20,\qquad
n=100.$$

The standard error is

$$SE=\frac{20}{\sqrt{100}}=2.$$

Therefore,

$$z_{\mathrm{obs}}
=
\frac{105-100}{2}
=
2.5.$$

For a right-sided test,

$$p=P(Z\geq2.5)\approx0.0062.$$

For a two-sided test,

$$p
=
2P(Z\geq2.5)
\approx
2(0.0062)
=
0.0124.$$

For a left-sided test,

$$p=P(Z\leq2.5)\approx0.9938.$$

## $z$-Test Versus $t$-Test

For a one-sample mean, the $z$-statistic is

$$z
=
\frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}},$$

where the population standard deviation $\sigma$ is known.

The one-sample $t$-statistic is

$$t
=
\frac{\bar{x}-\mu_0}{s/\sqrt{n}},$$

where the unknown population standard deviation is estimated using the sample standard deviation $s$.

Thus,

$$\boxed{
\text{known }\sigma
\Rightarrow
z\text{-test}
}$$

and, for testing a mean,

$$\boxed{
\text{unknown }\sigma
\Rightarrow
t\text{-test}.
}$$

## Degrees of Freedom

The standard normal distribution does not depend on degrees of freedom.

Therefore, an ordinary $z$-test does not require a $df$ value when computing the $p$-value.

## Assumptions

A one-sample mean $z$-test generally assumes:

1.  the observations are independent;

2.  the outcome is numerical;

3.  the population standard deviation $\sigma$ is known;

4.  the population is normal, or the sample is sufficiently large for the sampling distribution of the mean to be approximately normal;

5.  extreme observations do not invalidate the normal approximation.

## Summary

$$\boxed{
z_{\mathrm{obs}}
=
\frac{
\text{observed mean}-\text{hypothesized mean}
}{
\text{known standard error}
}
}$$

More explicitly,

$$\boxed{
z_{\mathrm{obs}}
=
\frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}
}$$

The complete process is

$$\boxed{
\text{sample with known }\sigma
\rightarrow
z_{\mathrm{obs}}
\rightarrow
\text{standard normal tail area}
\rightarrow
p\text{-value}.
}$$

Paste this section into the main LaTeX file:

# Wilcoxon Signed-Rank Test

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

## Summary

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

# Chi-Square Test of Independence

## Purpose

The chi-square test of independence determines whether two categorical variables are statistically associated.

Examples include testing whether:

- fraud status is associated with transaction channel;

- model prediction is associated with the true class;

- payment outcome is associated with customer category;

- transaction type is associated with alert status.

The test uses counts arranged in a contingency table.

## Example Contingency Table

Suppose transactions are classified by channel and fraud status:

|              |  Fraud   | Genuine  | Row total |
|:-------------|:--------:|:--------:|:---------:|
| UPI          | $O_{11}$ | $O_{12}$ |   $R_1$   |
| Card         | $O_{21}$ | $O_{22}$ |   $R_2$   |
| Column total |  $C_1$   |  $C_2$   |    $N$    |

Here:

- $O_{ij}$ is the observed count in row $i$, column $j$;

- $R_i$ is the total count in row $i$;

- $C_j$ is the total count in column $j$;

- $N$ is the total number of observations.

## Hypotheses

The null hypothesis is

$$H_0:
\text{the two categorical variables are independent}.$$

The alternative hypothesis is

$$H_1:
\text{the two categorical variables are associated}.$$

For example:

$$H_0:
\text{fraud status is independent of transaction channel},$$

$$H_1:
\text{fraud status is associated with transaction channel}.$$

The chi-square test is an overall, non-directional test. It determines whether an association exists, but does not directly state which categories cause the association.

## Expected Counts Under the Null Hypothesis

Under $H_0$, the variables are independent.

The expected count in cell $(i,j)$ is

$$\boxed{
E_{ij}
=
\frac{R_iC_j}{N}
}$$

or equivalently,

$$\boxed{
E_{ij}
=
\frac{
(\text{row }i\text{ total})
(\text{column }j\text{ total})
}{
\text{grand total}
}.
}$$

This formula follows from independence.

Under $H_0$,

$$P(\text{row }i\text{ and column }j)
=
P(\text{row }i)P(\text{column }j).$$

The estimated probabilities are

$$P(\text{row }i)=\frac{R_i}{N},$$

and

$$P(\text{column }j)=\frac{C_j}{N}.$$

Therefore,

$$P(\text{row }i\text{ and column }j)
=
\frac{R_i}{N}\frac{C_j}{N}.$$

Multiplying by $N$ observations gives

$$E_{ij}
=
N\left(\frac{R_i}{N}\right)
\left(\frac{C_j}{N}\right)
=
\frac{R_iC_j}{N}.$$

## Chi-Square Test Statistic

The chi-square statistic compares the observed counts with the counts expected under independence:

$$\boxed{
\chi^2_{\mathrm{obs}}
=
\sum_{i=1}^{r}
\sum_{j=1}^{c}
\frac{(O_{ij}-E_{ij})^2}{E_{ij}}
}$$

where:

- $r$ is the number of rows;

- $c$ is the number of columns;

- $O_{ij}$ is the observed count;

- $E_{ij}$ is the expected count under $H_0$.

For each cell,

$$\frac{(O_{ij}-E_{ij})^2}{E_{ij}}$$

measures the cell’s contribution to the total chi-square statistic.

If observed and expected counts are similar, then

$$\chi^2_{\mathrm{obs}}$$

will be small.

If observed and expected counts differ greatly, then

$$\chi^2_{\mathrm{obs}}$$

will be large.

## Why Is the Difference Squared?

The difference is squared:

$$(O_{ij}-E_{ij})^2$$

for two reasons:

1.  positive and negative deviations should not cancel;

2.  larger deviations should contribute more strongly to the test statistic.

The squared difference is divided by $E_{ij}$ so that the deviation is measured relative to the expected size of the cell.

## Degrees of Freedom

For an $r\times c$ contingency table, the degrees of freedom are

$$\boxed{
df=(r-1)(c-1).
}$$

For a $2\times2$ table:

$$df=(2-1)(2-1)=1.$$

The degrees of freedom represent the number of cell counts that can vary freely after the row totals and column totals are fixed.

## Theoretical Chi-Square Distribution

Under $H_0$, the test statistic approximately follows a chi-square distribution:

$$X\sim\chi^2_{\nu},$$

where

$$\nu=df.$$

The probability density function is

$$f(x;\nu)
=
\frac{
1
}{
2^{\nu/2}\Gamma(\nu/2)
}
x^{\nu/2-1}e^{-x/2},
\qquad x>0.$$

Here:

- $x$ is a possible chi-square statistic;

- $\nu$ is the number of degrees of freedom;

- $\Gamma(\cdot)$ is the gamma function;

- $e$ is the exponential constant.

The chi-square distribution contains only nonnegative values:

$$x\geq0.$$

Unlike the normal and $t$-distributions, the chi-square distribution is generally right-skewed. Its shape depends on the degrees of freedom.

## Computing the $p$-Value

A large chi-square statistic indicates that the observed table differs substantially from the table expected under independence.

Therefore, the chi-square test uses only the right tail:

$$\boxed{
p
=
P\left(
X\geq\chi^2_{\mathrm{obs}}
\mid H_0
\right).
}$$

If $F_{\chi^2_{df}}$ is the cumulative distribution function, then

$$\boxed{
p
=
1-F_{\chi^2_{df}}
\left(
\chi^2_{\mathrm{obs}}
\right).
}$$

There is no left-sided or two-sided version in the usual chi-square test of independence. Both positive and negative cell deviations contribute positively because they are squared.

## Numerical Example

Suppose fraud status and transaction channel produce the following table:

|       | Fraud | Genuine | Total |
|:------|:-----:|:-------:|:-----:|
| UPI   | $30$  |  $70$   | $100$ |
| Card  | $10$  |  $90$   | $100$ |
| Total | $40$  |  $160$  | $200$ |

The expected UPI-fraud count under independence is

$$E_{11}
=
\frac{100\times40}{200}
=
20.$$

The expected UPI-genuine count is

$$E_{12}
=
\frac{100\times160}{200}
=
80.$$

Similarly,

$$E_{21}=20,
\qquad
E_{22}=80.$$

Therefore, the expected table is

|      | Fraud | Genuine |
|:-----|:-----:|:-------:|
| UPI  | $20$  |  $80$   |
| Card | $20$  |  $80$   |

The chi-square statistic is

$$\begin{aligned}
\chi^2_{\mathrm{obs}}
={}&
\frac{(30-20)^2}{20}
+
\frac{(70-80)^2}{80}\\
&+
\frac{(10-20)^2}{20}
+
\frac{(90-80)^2}{80}.
\end{aligned}$$

Thus,

$$\chi^2_{\mathrm{obs}}
=
5+1.25+5+1.25
=
12.5.$$

The degrees of freedom are

$$df=(2-1)(2-1)=1.$$

The $p$-value is

$$p=P(X_1\geq12.5).$$

This gives a small $p$-value, providing evidence against the null hypothesis of independence.

Therefore, the sample provides evidence that fraud status is associated with transaction channel.

## Cell Contributions

Each cell contributes

$$C_{ij}
=
\frac{(O_{ij}-E_{ij})^2}{E_{ij}}$$

to the total statistic.

Cells with large contributions are the main sources of disagreement between the observed data and $H_0$.

However, the squared contribution does not show whether the observed count is above or below expectation. For direction, inspect

$$O_{ij}-E_{ij}.$$

A positive value means

$$O_{ij}>E_{ij},$$

while a negative value means

$$O_{ij}<E_{ij}.$$

Standardized residuals can also help identify which cells drive the association.

## Assumptions

The chi-square test of independence generally assumes:

1.  the variables are categorical;

2.  the table contains frequencies or counts, not percentages or continuous measurements;

3.  each observation contributes to only one cell;

4.  observations are independent;

5.  expected cell counts are sufficiently large for the chi-square approximation to be reliable.

If expected counts are very small, particularly in a $2\times2$ table, Fisher’s exact test may be more appropriate.

## Effect Size

A small $p$-value indicates evidence of an association, but does not measure the strength of that association.

For an $r\times c$ table, Cramer’s $V$ is

$$\boxed{
V
=
\sqrt{
\frac{
\chi^2_{\mathrm{obs}}
}{
N\min(r-1,c-1)
}
}.
}$$

Cramer’s $V$ ranges from zero to one:

$$0\leq V\leq1.$$

Larger values indicate a stronger association.

For a $2\times2$ table, the corresponding measure is also called the phi coefficient:

$$\phi=\sqrt{\frac{\chi^2_{\mathrm{obs}}}{N}}.$$

## Summary

The chi-square test of independence follows this process:

$$\boxed{
\text{observed counts}
\rightarrow
\text{expected counts under independence}
\rightarrow
\chi^2_{\mathrm{obs}}
\rightarrow
df
\rightarrow
\text{right-tail probability}
\rightarrow
p\text{-value}.
}$$

The key formulas are

$$\boxed{
E_{ij}
=
\frac{R_iC_j}{N}
}$$

$$\boxed{
\chi^2_{\mathrm{obs}}
=
\sum_{i=1}^{r}
\sum_{j=1}^{c}
\frac{(O_{ij}-E_{ij})^2}{E_{ij}}
}$$

$$\boxed{
df=(r-1)(c-1)
}$$

and

$$\boxed{
p=P\left(
X_{df}\geq\chi^2_{\mathrm{obs}}
\right).
}$$

Below is a LaTeX section for one-way analysis of variance, which compares the means of three or more independent groups.

# One-Way Analysis of Variance

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

## Summary

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
