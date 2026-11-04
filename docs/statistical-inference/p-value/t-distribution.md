# Theoretical $t$-Distribution

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
