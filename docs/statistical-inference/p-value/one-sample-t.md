# One-Sample $t$-Test

!!! abstract "At a glance"
    $$\boxed{
    \text{sample}
    \rightarrow t_{\mathrm{obs}}
    \rightarrow df=n-1
    \rightarrow \text{tail area under }t_{df}
    \rightarrow p\text{-value}
    }$$

    A one-sample $t$-test produces one observed $t$-value from the sample. The reference $t$-distribution represents the possible values of the statistic under $H_0$, and the alternative hypothesis determines whether the left tail, right tail, or both tails are used.


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
