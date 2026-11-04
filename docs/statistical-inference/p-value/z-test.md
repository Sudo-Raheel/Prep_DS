# $z$-Test

!!! abstract "At a glance"
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
