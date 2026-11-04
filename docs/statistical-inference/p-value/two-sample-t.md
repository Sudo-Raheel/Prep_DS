# Independent Two-Sample $t$-Test

!!! abstract "At a glance"
    $$\boxed{ t_{\mathrm{obs}} = \frac{ \text{observed difference between means} }{ \text{standard error of the difference} } }$$

     More explicitly, 

    $$\boxed{ t_{\mathrm{obs}} = \frac{ \bar{x}_1-\bar{x}_2 }{ \sqrt{ s_1^2/n_1+s_2^2/n_2 } } }$$

     The complete process is 

    $$\boxed{ \text{two independent samples} \rightarrow t_{\mathrm{obs}} \rightarrow \text{Welch }df \rightarrow \text{tail area under }t_{df} \rightarrow p\text{-value} }$$

     Paste this into the main .tex file as the next section:


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
