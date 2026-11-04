**Data Science, Statistics & Machine Learning**\
Interview Question Bank — Deduplicated\
Edited from the supplied notes; repeated questions merged and technical inaccuracies corrected.\

# Probability and Descriptive Statistics

**Q.What is the difference between a population and a sample?**

A *population* contains every unit about which we want to draw conclusions. A *sample* is the subset actually observed. Population quantities (such as the mean $\mu$ or variance $\sigma^2$) are *parameters*; sample quantities (such as $\bar{x}$ or $s^2$) are *statistics*. We usually analyze a sample because measuring the entire population is impractical. Representativeness depends on the sampling design, not merely on sample size.

**Q.What is sampling, and what are the main sampling methods?**

Sampling means selecting observations from a target population to estimate its characteristics. **Probability sampling** includes simple random, systematic (every $k$th eligible unit after a random start), stratified (sample within defined subgroups), cluster (sample groups, then their members), and multistage sampling. **Non-probability sampling** includes convenience, purposive/judgmental, quota, snowball, and voluntary-response sampling. Probability designs support design-based inference when selection probabilities are known; convenience samples can suffer substantial selection bias. Sampling with replacement is useful in bootstrapping but is not a universal requirement for the central limit theorem.

**Q.What is the Central Limit Theorem (CLT), and why does it matter?**

For independent and identically distributed observations with finite population mean $\mu$ and finite, nonzero variance $\sigma^2$, the *standardized sample mean* converges in distribution to a standard normal variable: 

$$\frac{\sqrt{n}(\bar X_n-\mu)}{\sigma}\xrightarrow{d}N(0,1).$$

 Consequently $\bar X_n$ is approximately $N(\mu,\sigma^2/n)$ for sufficiently large $n$. The original observations do *not* become normal; it is the sampling distribution of their mean that does. This enables approximate confidence intervals and tests without requiring a normally distributed population. The often-quoted $n\geq30$ is only a rough heuristic; severe skewness, heavy tails, dependence, or infinite variance can demand different methods.

**Q.What is the Law of Large Numbers (LLN), and how is it different from the CLT?**

The LLN says that the sample mean converges to the population mean as sample size increases under appropriate assumptions. The *weak* LLN gives convergence in probability; the *strong* LLN gives almost-sure convergence. The LLN describes *where* $\bar X_n$ converges; the CLT describes the approximate *shape and scale of its sampling fluctuations*. Neither theorem removes bias arising from a systematically unrepresentative sample.

**Q.How do population means and sample means differ, and when can a sample mean mislead?**

The population mean $\mu=E[X]$ is a fixed characteristic of a population or probability distribution; the sample mean $\bar X=(1/n)\sum_i X_i$ varies with the observed sample. Under simple random sampling, $\bar X$ is often unbiased for $\mu$. It can nevertheless mislead when the sampling frame excludes relevant units, selection or nonresponse is outcome-dependent, observations are dependent in unaccounted ways, or the distribution is extremely heavy-tailed. A larger biased sample can be worse than a smaller representative one.

**Q.What is the difference between a parameter, statistic, estimator, and estimate?**

A *parameter* is a population quantity (e.g., $\mu$). A *statistic* is a function of observed data (e.g., $\bar X$). An *estimator* is the data-dependent rule intended to estimate a parameter, while an *estimate* is the resulting number for a particular sample. For example, $\bar X$ is an estimator of $\mu$; $\bar x=12.4$ is an estimate.

**Q.What are variance and standard deviation?**

Variance measures expected squared deviations from the mean: $\operatorname{Var}(X)=E[(X-\mu)^2]$. Standard deviation is $\sigma=\sqrt{\operatorname{Var}(X)}$. Variance has squared units; standard deviation has the same units as the original variable. Large variance indicates greater dispersion, not necessarily a poorer predictive model. For an independent sample, the usual unbiased sample variance is $s^2=\sum_i(x_i-\bar x)^2/(n-1)$; the population variance divides by the population size $N$.

**Q.What are mean, median, and mode, and when would you use each?**

The *mean* is the arithmetic average and uses all values but is sensitive to extreme observations. The *median* is the central ordered value and is robust to isolated outliers. The *mode* is the most frequently occurring value or category and is meaningful for categorical data. In an exactly normal distribution, mean, median, and mode coincide; with heavily right-skewed data, the mean often exceeds the median.

**Q.What is skewness?**

Skewness summarizes distributional asymmetry. Positive skewness generally indicates a longer right tail, while negative skewness indicates a longer left tail. A common standardized population definition is $E[(X-\mu)^3]/\sigma^3$. Zero skewness does not guarantee symmetry or normality.

**Q.What is the difference between a uniform and a normal distribution?**

A continuous uniform distribution has constant density on a specified interval. A normal distribution has a bell-shaped density determined by its mean and variance, with highest density near its mean. For discrete uniform data, such as a fair die, every allowed value has equal probability. Both are useful models, but their shapes and tail behavior differ.

**Q.Give examples of non-Gaussian distributions and suitable datasets.**

- **Binomial:** number of heads in 20 independent coin flips.

- **Discrete uniform:** result of rolling a fair six-sided die.

- **Exponential:** waiting time to the next event in a homogeneous Poisson process.

- **Poisson:** number of calls reaching a call center per hour if arrivals follow a constant-rate Poisson process.

- **Log-normal:** a plausible model for some positively skewed income or transaction-size measurements.

Human heights are sometimes approximately Gaussian within a sufficiently homogeneous group, but need not be exactly normal.

**Q.What are univariate, bivariate, and multivariate analyses?**

*Univariate* analysis studies one variable (such as a histogram of sales). *Bivariate* analysis studies the joint behavior of two variables (such as advertising spend versus sales). *Multivariate* analysis jointly examines more than two variables (such as sales versus price, promotions, and seasonality). Choice of method depends on data type, research objective, and dependence structure.

**Q.What is covariance, and how is it different from correlation?**

Covariance measures joint linear variation: $\operatorname{Cov}(X,Y)=E[(X-\mu_X)(Y-\mu_Y)]$. Pearson correlation standardizes it: 

$$\rho_{XY}=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}, \qquad -1\leq\rho_{XY}\leq1.$$

 Covariance depends on the measurement scales and has product units; correlation is dimensionless. Positive and negative values indicate directions of linear association. Correlation is invariant under positive rescaling (a negative rescaling changes its sign), and neither metric by itself establishes causality.

**Q.What is the difference between correlation and causation?**

Correlation means variables exhibit statistical association; causation means intervening on one variable would change another under the relevant causal assumptions. Confounding, reverse causation, and selection effects can all produce correlations without the proposed causal effect. Randomized experiments, appropriate causal designs, or explicit causal assumptions are usually needed for causal claims.

**Q.What is statistical interaction?**

An interaction occurs when the effect of predictor $X_1$ on outcome $Y$ depends on another predictor $X_2$. A simple regression representation is 

$$E[Y\mid X_1,X_2]=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_1X_2.$$

 The marginal effect of $X_1$ is $\beta_1+\beta_3X_2$. For example, the effect of medication dosage may depend on age or another clinically relevant characteristic. An interaction is different from a confounder.

**Q.What are confounding variables?**

A confounder is a common cause (or, more generally, a variable creating a backdoor association) of both the putative exposure and outcome. For example, age may affect both physical activity and weight change, thereby distorting the observed activity–weight association. Depending on the causal structure, randomization, stratification, regression adjustment, matching, or weighting can address confounding. Not every predictor associated with the outcome should automatically be adjusted for.

**Q.What is an outlier? How does it differ from noise?**

An *outlier* is an observation unusually far from the main pattern. *Noise* is ordinary unexplained variation or measurement error, which may or may not produce outliers. Investigate anomalies before removal: they might be data-entry errors, genuine rare events, or useful signals. Appropriate responses include correction, robust losses, transformations, sensitivity analysis, or documented exclusion rules.

**Q.What is a scatter plot? How is it different from a box plot or histogram?**

A *scatter plot* displays paired observations of two numerical variables to assess relationships, clusters, and anomalies. A *histogram* bins one numerical variable to show frequency or density. A *box plot* summarizes median, quartiles, spread, and potential outliers, often facilitating comparison across groups. They answer different questions and are complementary.

**Q.How does a histogram differ from a density plot?**

A histogram divides observations into bins and plots frequency or normalized density; its appearance depends on bin width and boundaries. A density plot, often computed using kernel density estimation, gives a smooth estimate of the underlying density and depends on smoothing bandwidth. For small datasets, smoothing can hide multimodality or create misleading apparent structure.

**Q.What is the curse of dimensionality?**

As the number of features grows, observations become sparse relative to the volume of feature space. Distance-based methods can lose discrimination, the sample size required to cover the space increases, and models may overfit. Remedies include feature selection, domain-guided representations, regularization, dimensionality reduction, and collecting more informative data. Not every high-dimensional problem is difficult when data lie near a low-dimensional structure.

**Q.What do eigenvalues and eigenvectors of a covariance matrix mean in PCA?**

Principal component analysis diagonalizes a covariance (or appropriately standardized correlation) matrix. Each eigenvector supplies an orthogonal direction of variance; its eigenvalue quantifies the variance along that direction. Components are ordered by decreasing eigenvalue. PCA is unsupervised and maximizes variance, which need not be the variance relevant to predicting a target.

**Q.How is a covariance matrix used in portfolio optimization?**

For portfolio weights $w$ and an asset-return covariance matrix $\Sigma$, portfolio variance is $w^\top\Sigma w$. Off-diagonal terms measure co-movement and determine diversification benefits or risks. Optimization may minimize variance subject to return, risk, budget, and other constraints. Estimated covariances can be unstable, so regularization or shrinkage is common.

**Q.What is expected value in probability and decision theory?**

Expected value is the probability-weighted average of possible outcomes: $E[X]=\sum_x xP(X=x)$ for a discrete variable (or an integral for continuous variables). In decision theory, select an action by comparing expected *utility* or expected cost under a specified loss function, rather than blindly maximizing average monetary return when risk preferences matter.

**Q.What is the difference between deterministic and probabilistic models?**

A deterministic model returns a fixed output for specified inputs and parameters. A probabilistic model explicitly represents uncertainty through distributions over outcomes, states, or parameters. Deterministic predictions can still have uncertain accuracy, while probabilistic outputs can be summarized by means, intervals, or event probabilities.

**Q.What is a Markov chain or Markov process?**

The Markov property says that, conditional on the present state, the future is independent of the earlier past. For a discrete-time Markov chain, 

$$P(X_{t+1}\mid X_t,X_{t-1},\ldots)=P(X_{t+1}\mid X_t).$$

 Applications include customer state transitions, credit-rating migration, and some finance models. Markov models are assumptions about chosen states; real processes may require richer states or longer memory.

# Sampling, Bias, and Data Preparation

**Q.What is selection bias, and how does it differ from random sampling error?**

Selection bias occurs when inclusion in the analyzed sample depends systematically on variables related to the estimand or outcome. For example, a drug study recruiting only young healthy adults may not generalize to older patients. Random sampling error shrinks as a representative sample grows; selection bias does not necessarily shrink with sample size. Sampling bias is one important form of selection bias.

**Q.What biases can arise during sampling or study participation?**

Important examples include **undercoverage** (eligible groups missing from the sampling frame), **overcoverage** (ineligible or duplicated units), **self-selection/voluntary-response bias** (participation correlated with opinion), **nonresponse bias** (selected units do not respond in outcome-related ways), **attrition bias** (differential dropout), **survivorship bias** (analyzing only those remaining after a filter), and **response bias** (inaccurate answers due to wording or social pressure). Selective reporting or data-dependent stopping can introduce additional bias. Prevention requires careful design, monitoring, and sensitivity analysis.

**Q.Why is data cleaning important?**

Data cleaning identifies and resolves errors, inconsistent units, duplicates, invalid categories, impossible timestamps, missing values, and leakage-prone records. It improves reliability of analysis and deployment, but cleaning choices must be documented to avoid selectively removing inconvenient data. In machine learning, fit learned transformations (for example, imputers or scalers) on training data only and apply them unchanged to validation/test data.

**Q.What is data imputation, and what options are available?**

Imputation fills missing values using simple statistics (median/mode), conditional models, $k$-nearest neighbors, multiple imputation, or model-based methods. Choice depends on whether missingness is MCAR, MAR, or MNAR and on the intended inferential objective. Missing-indicator features can be useful for prediction; simple single imputation can understate uncertainty for inference. Avoid estimating imputation parameters using the test set.

**Q.What is the difference between long and wide data formats?**

In *wide* format, one entity typically occupies one row and repeated measurements appear in separate columns (e.g., `sales_Jan`, `sales_Feb`). In *long* format, each entity–time combination occupies a row, with a `month` column and a `sales` column. Long format often simplifies grouping, plotting, and longitudinal modeling; wide format can be convenient for feature matrices. Reshape with `pandas.melt` and `pivot`/`pivot_table`.

**Q.What are the components commonly found in a dataset?**

A tabular dataset generally contains observations (rows) and variables/features (columns). It may additionally contain a target label (supervised learning), identifiers, timestamps, categorical metadata, missing values, or weights. No target label is guaranteed to exist: unsupervised data have features but no required outcome label. For time series, order and the time index are especially important.

**Q.What is resampling, and why is it used?**

Resampling reuses observed data to quantify uncertainty, evaluate prediction methods, or construct significance tests. **Bootstrapping** samples observations (or suitable blocks) with replacement to approximate a statistic’s sampling distribution. **Cross-validation** holds out folds to estimate out-of-sample predictive performance. **Permutation tests** relabel or rearrange observations under an appropriate null exchangeability assumption. Each answers a different statistical question.

**Q.What is bootstrapping, and what are its limitations?**

Ordinary nonparametric bootstrap draws $n$ observations with replacement from an observed sample of size $n$, computes a statistic, and repeats to estimate uncertainty or confidence intervals. It performs well for many smooth statistics under representative, approximately independent sampling. It can fail for strong dependence, extreme tail quantities, rare classes, or unsuitable statistics; dependent time series typically need a block or model-based bootstrap.

**Q.How does sample size affect precision?**

For independent observations with fixed finite variance, the standard error of the sample mean is $\sigma/\sqrt{n}$; doubling $n$ reduces it by a factor of $1/\sqrt{2}$. Approximate confidence-interval width therefore shrinks like $1/\sqrt{n}$. Reaching half the standard error generally needs about four times as many observations. Selection bias and systematic measurement error are not solved by increasing $n$.

# Hypothesis Testing and Statistical Inference

**Q.What are Type I and Type II errors?**

A **Type I error** is rejecting a true null hypothesis (false positive), with probability $\alpha$ when the test has the stipulated level. A **Type II error** is failing to reject a false null hypothesis (false negative), with probability $\beta$ for a specified alternative. Statistical power is $1-\beta$. A result that is not statistically significant is *not* proof of no effect.

**Q.What is a $p$-value?**

A $p$-value is the probability, *assuming the null hypothesis and test assumptions*, of obtaining a test statistic at least as extreme as the observed statistic (as defined by the test). It is not the probability that the null hypothesis is true, not the probability that results arose “by chance,” and not an effect-size measure. A small $p$-value provides evidence against the null model, but practical importance requires an effect estimate, uncertainty, and context.

**Q.What is a significance level $\alpha$, and how is it different from a $p$-value?**

The significance level $\alpha$ is a threshold chosen before interpreting data that controls a test’s long-run Type I error rate under its assumptions (commonly 0.05). The $p$-value is computed from observed evidence. A conventional decision rule rejects $H_0$ if $p\leq\alpha$. Multiple testing, optional stopping, and model misspecification may invalidate nominal error-rate guarantees.

**Q.What is statistical power, and how does it differ from sensitivity?**

**Power** is $P(\text{reject }H_0\mid H_1\text{ is true})=1-\beta$, defined for a specified effect and testing procedure. It generally increases with larger effects, larger samples, lower noise, and sometimes a higher $\alpha$. **Sensitivity** (recall or true-positive rate) evaluates a binary classifier: $\mathrm{TP}/(\mathrm{TP}+\mathrm{FN})$. Both involve detecting true signals, but one refers to hypothesis tests and the other to diagnostic/classification outcomes; they should not be conflated.

**Q.When are false positives or false negatives more costly?**

The answer depends on downstream consequences. In many cancer-screening settings, *false negatives* can be especially costly because disease may be missed; a higher false-positive rate may be tolerated, subject to the harm of unnecessary testing. In airport threat screening, missed threats (false negatives) may likewise be especially costly. In other contexts, such as automatically denying legitimate financial transactions, false positives can cause serious disruption. Select operating thresholds by considering prevalence and explicit costs, not by assuming that one error type is always worse.

**Q.What is a point estimate versus a confidence interval?**

A *point estimate* is one number, such as $\bar x$ for $\mu$. A *confidence interval* provides a range built by a procedure designed to cover the fixed population parameter in a specified fraction of hypothetical repeated samples. A frequentist 95% interval does *not* assign 95% posterior probability to the already fixed parameter being inside the observed interval; that interpretation would require a Bayesian credible interval with an explicit prior.

**Q.How do you interpret a 95% confidence interval?**

If the sampling and interval procedure were repeated indefinitely under the same assumptions, roughly 95% of the resulting intervals would contain the true parameter. For a single realized interval, frequentist coverage pertains to the construction procedure. The interpretation relies on the underlying sampling and model assumptions.

**Q.What is a confidence interval versus a prediction interval?**

A confidence interval estimates a population characteristic (such as a conditional mean). A prediction interval aims to cover a future individual observation and incorporates both parameter uncertainty and irreducible observation-level variation. Consequently, a prediction interval for an individual response is generally wider than a confidence interval for its expected value at the same predictor settings.

**Q.What is a confidence interval for a proportion?**

For independent Bernoulli observations, $\hat p=k/n$ estimates the population proportion $p$. A large-sample Wald interval is $\hat p\pm z_{1-\alpha/2}\sqrt{\hat p(1-\hat p)/n}$, but its coverage can be poor near 0, 1, or for small $n$. A *Wilson score interval* is often a better default for binomial proportions. Clustered observations require adjusted uncertainty estimates.

**Q.What is the difference between parametric and nonparametric methods?**

*Parametric* models specify a distributional family with a finite-dimensional parameter, such as a normal model with mean and variance. *Nonparametric* methods use more flexible models or tests without committing to a particular finite-dimensional distributional family. Nonparametric does not mean *assumption-free*: independence, exchangeability, smoothness, or distributional conditions may still be essential. Examples include rank-based tests and kernel density estimation.

**Q.How do parametric and nonparametric confidence intervals differ?**

A parametric interval uses an assumed model family to derive a sampling distribution or approximation (e.g., a $t$-interval for a mean). A nonparametric interval often uses bootstrap resampling, ranks, or distribution-free bounds. Neither is automatically superior; coverage depends on the method’s assumptions and sample characteristics. For skewed small samples, consider suitable bootstrap intervals and robust alternatives rather than generic normal formulas.

**Q.What are one-tailed and two-tailed tests?**

A one-sided test targets an effect in a pre-specified direction, such as $H_1:\mu>\mu_0$. A two-sided test targets deviations in either direction, such as $H_1:\mu\ne\mu_0$. Choosing a one-sided test after observing the direction of an effect inflates false-positive risk. Choose the alternative before inspecting outcomes.

**Q.What is the difference between a $z$-test and a $t$-test or $z$-score and $t$-statistic?**

A $z$-statistic uses a standard-normal reference distribution when its null standardization is justified (for example, a mean with known $\sigma$ under a normal model). A one-sample $t$-statistic replaces unknown $\sigma$ with sample $s$: $t=(\bar X-\mu_0)/(s/\sqrt n)$, which follows a $t_{n-1}$ distribution for independent normal observations. A $z$-score can simply be a standardized individual observation; the terms should be tied to their contexts. It is misleading to decide between $t$ and $z$ solely by the rule $n<30$.

**Q.What is the Student $t$-distribution?**

A $t$-distribution is symmetric and bell-shaped, with heavier tails than a normal distribution. It is indexed by degrees of freedom and approaches the standard normal as degrees of freedom grow. In normal-sample inference for a mean with unknown variance, replacing the population standard deviation with a sample estimate produces the $t$ statistic.

**Q.What are degrees of freedom?**

Degrees of freedom quantify independently varying pieces of information after accounting for constraints or estimated parameters. Sample variance uses $n-1$ degrees of freedom because deviations from the sample mean sum to zero. In ordinary least squares with a full-rank design and $p$ estimated coefficients (including intercept), residual degrees of freedom are $n-p$.

**Q.What is a paired $t$-test versus an independent-samples $t$-test?**

A paired $t$-test performs a one-sample test on within-pair differences (e.g., before versus after intervention for the same subject). An independent-samples $t$-test compares means from unrelated groups. Welch’s $t$-test is usually preferred when variances may differ. The dependency structure determines which test is appropriate.

**Q.What is an $F$-test and how is it used in ANOVA?**

An $F$-statistic is a ratio of appropriately scaled variance estimates. In one-way ANOVA it compares between-group and within-group mean squares to test the null hypothesis that population group means are equal. In regression it can compare nested linear models. The classical exact reference distribution relies on model assumptions, including suitable independent errors; Welch ANOVA or robust alternatives may be appropriate when variances differ.

**Q.What are chi-squared tests of independence and goodness of fit?**

A chi-squared *test of independence* assesses association between categorical variables in a contingency table. A *goodness-of-fit* test compares observed category counts with expected counts under a specified distribution. A common statistic is $\chi^2=\sum_j(O_j-E_j)^2/E_j$. Interpretation requires sufficiently appropriate expected counts and a valid sampling model; Fisher’s exact test can help for small contingency tables.

**Q.What are Levene’s test and Bartlett’s test?**

Both test equality of population variances across groups. *Levene’s test* assesses variability using deviations from group centers; its median-centered Brown–Forsythe variation is relatively robust to departures from normality. *Bartlett’s test* is powerful under normality but sensitive to non-normal distributions. A small $p$-value suggests unequal variances, but graphical and substantive assessment also matter.

**Q.What are the Shapiro–Wilk, Kolmogorov–Smirnov, and Q–Q methods for normality?**

Shapiro–Wilk tests the null hypothesis that data arise from a normal distribution. A normal Q–Q plot compares sample quantiles with theoretical normal quantiles and reveals skewness or tail departures. A one-sample Kolmogorov–Smirnov test compares the empirical CDF with a *fully specified* reference CDF; estimating normal parameters from the data changes its null calibration (e.g., Lilliefors adjustment). Normality tests can overreact to trivial departures in huge samples and lack power in tiny ones.

**Q.What is the Mann–Whitney $U$ test?**

The Mann–Whitney $U$ test (Wilcoxon rank-sum) compares the relative ranks of two independent groups. Broadly, it tests whether values from one group tend to be larger than values from the other, with exchangeability assumptions for its null calibration. It is *not* a generic test of median differences unless additional shape assumptions hold.

**Q.What is the Wilcoxon signed-rank test?**

The Wilcoxon signed-rank test uses the magnitudes and signs of paired differences to assess whether their distribution is symmetric about zero (or another hypothesized location). It is useful for paired, non-normal data when this symmetry assumption is reasonable. A sign test makes weaker assumptions but may have less power.

**Q.What is the Kruskal–Wallis test?**

Kruskal–Wallis is a rank-based test for comparing multiple independent groups. Its general null concerns equality of their distributions (under appropriate assumptions), not automatically equality of medians. When shapes and spreads are comparable, rejection may be interpreted as a location difference. Follow significant results with multiplicity-adjusted post-hoc comparisons.

**Q.What is Tukey’s honestly significant difference (HSD) procedure?**

Tukey HSD performs pairwise comparisons of group means while controlling the family-wise error rate, typically following a classical ANOVA with appropriate variance assumptions. Unequal sample sizes can be handled with Tukey–Kramer; unequal variances may call for alternatives such as Games–Howell.

**Q.What is the Bonferroni correction?**

When conducting $m$ tests, Bonferroni controls the family-wise error rate at or below $\alpha$ by testing each at significance level $\alpha/m$ (or multiplying each $p$-value by $m$ and truncating at 1). It remains valid under arbitrary dependence but may be conservative. Holm’s step-down procedure is often more powerful while retaining family-wise error control.

**Q.What is a likelihood function? How is likelihood different from probability?**

For observed data $x$ and parameter $\theta$, a model supplies probability mass or density $f(x\mid\theta)$. Viewing it as a function of *data* for fixed $\theta$ describes outcome probabilities/densities; viewing the same expression as a function of *$\theta$* with $x$ fixed gives the likelihood $L(\theta;x)$. Likelihood values are not probabilities assigned to parameter values and need not integrate to one over parameters.

**Q.What is maximum likelihood estimation (MLE)?**

MLE chooses parameters maximizing the observed-data likelihood: $\hat\theta_{\mathrm{MLE}}=\arg\max_\theta L(\theta;x)$. For independent observations it is often convenient to maximize $\sum_i\log f(x_i\mid\theta)$. Under regularity conditions, MLEs have favorable asymptotic properties, but small-sample bias, model misspecification, and non-identifiability can cause problems.

**Q.How does MLE differ from the method of moments?**

MLE selects parameters that make observed data most likely under a model. The *method of moments* equates sample moments to their corresponding model expectations and solves for parameters. Moment estimators may be simpler but less statistically efficient than well-behaved MLEs, depending on the model and the moments used.

**Q.What is a likelihood-ratio test?**

A likelihood-ratio test compares nested models using $\Lambda=2(\ell_{\mathrm{full}}-\ell_{\mathrm{restricted}})$, where $\ell$ is maximized log likelihood. Under regularity conditions and a null hypothesis away from parameter-space boundaries, $\Lambda$ is approximately chi-squared with degrees of freedom equal to the difference in free parameter counts. Boundary cases and small samples may require special calibration.

**Q.What is the Cram’er–Rao lower bound?**

Under regularity conditions, the variance of an unbiased estimator $\hat\theta$ of a scalar parameter is bounded below by $1/I(\theta)$, where $I(\theta)$ is the Fisher information from the data. The bound describes a theoretical efficiency limit for unbiased estimation; not every estimator achieves it, and its assumptions matter.

**Q.What is a Bayesian approach and how does Bayesian updating work?**

Bayesian inference represents uncertainty about parameters with probability distributions. Bayes’ rule updates a prior $p(\theta)$ using likelihood $p(D\mid\theta)$ to form 

$$p(\theta\mid D)=\frac{p(D\mid\theta)p(\theta)}{p(D)}.$$

 The posterior can be summarized through credible intervals, predictions, or decisions. Priors should be chosen transparently and tested for sensitivity when appropriate.

**Q.What is a conjugate prior?**

A conjugate prior produces a posterior in the same distributional family as the prior for a particular likelihood model. For binomial data, a Beta$(a,b)$ prior combined with $k$ successes in $n$ trials yields a Beta$(a+k,b+n-k)$ posterior. Conjugacy makes calculations convenient but does not ensure the prior is substantively appropriate.

**Q.What is the difference between a credible interval and a confidence interval?**

A Bayesian 95% *credible interval* contains 95% posterior probability for the parameter under a stated prior and model. A frequentist 95% *confidence interval* is obtained through a construction with 95% long-run coverage under repeated sampling. They can numerically coincide in some models, but their interpretations differ.

**Q.What is a Kaplan–Meier estimator?**

The Kaplan–Meier estimator is a nonparametric estimator of the survival function $S(t)=P(T>t)$ from time-to-event data, accommodating right censoring under appropriate independent-censoring assumptions. It updates estimated survival multiplicatively at observed event times. It does not directly adjust for arbitrary covariates; methods such as Cox regression can address that need.

# Regression and Statistical Models

**Q.What is linear regression, and how should coefficients, $p$-values, and $R^2$ be interpreted?**

Linear regression models the conditional mean as $E[Y\mid X]=\beta_0+\sum_j\beta_j X_j$. A coefficient $\beta_j$ is the change in modeled mean response per unit increase in $X_j$ when other included covariates are held constant; it is not automatically causal. A coefficient $p$-value tests an appropriate null such as $H_0:\beta_j=0$ under the model and standard-error assumptions. The in-sample quantity $R^2=1-\mathrm{SSE}/\mathrm{SST}$ measures the fraction of sample outcome variation explained relative to an intercept-only baseline. High $R^2$ does not ensure valid inference, causality, or good out-of-sample predictions.

**Q.What assumptions are relevant to ordinary least squares (OLS)?**

Important distinctions are:

- **Correct conditional-mean specification:** $E[Y\mid X]$ has the specified linear form in coefficients (polynomial features can still be used).

- **Exogeneity:** $E[\varepsilon\mid X]=0$ for standard unbiasedness under suitable sampling conditions; unaddressed confounding or simultaneity can violate it.

- **No perfect multicollinearity:** the design matrix has full column rank.

- **Appropriate error dependence and variance:** independent/uncorrelated homoscedastic errors are important for the classical Gauss–Markov efficiency result and usual simple standard errors.

- **Normality:** not required for OLS point-estimate unbiasedness; it supports certain exact small-sample $t$ and $F$ inference.

Use residual diagnostics and data-generating knowledge. Robust standard errors can correct some variance misspecification but do not cure omitted-variable bias or reverse causation.

**Q.What are underfitting and overfitting?**

Underfitting arises when a model is too restrictive to capture real signal, producing poor training and test performance (high bias). Overfitting occurs when it captures noise or idiosyncrasies of training data and generalizes poorly (often high variance). Compare training and validation learning curves, select complexity by suitable cross-validation, and protect a held-out final test set.

**Q.What is homoscedasticity versus heteroscedasticity?**

Homoscedasticity means the conditional error variance is constant: $\operatorname{Var}(\varepsilon\mid X)=\sigma^2$. Heteroscedasticity means it changes with predictors or fitted levels. Under exogeneity, heteroscedasticity does not by itself make OLS coefficients biased, but classical standard errors and efficiency claims can fail. Diagnostics include residual plots and Breusch–Pagan/White tests; potential remedies include heteroscedasticity-robust standard errors, weighted least squares, or re-specifying the variance model.

**Q.What is autocorrelation of regression errors?**

Autocorrelation occurs when errors at different times are statistically dependent. It can distort usual uncertainty estimates and forecasting assessment. Inspect residual time plots, autocorrelation functions, and suitable tests such as Durbin–Watson for certain first-order correlation settings. Depending on the problem, use HAC standard errors, GLS, or explicit autoregressive/error models.

**Q.What is multicollinearity, and what does VIF measure?**

Multicollinearity occurs when predictors are highly linearly related; *perfect* multicollinearity prevents unique OLS coefficient estimation. Near-collinearity inflates coefficient uncertainty and can make estimates unstable even when predictions remain good. For predictor $j$, $\mathrm{VIF}_j=1/(1-R_j^2)$, where $R_j^2$ comes from regressing it on the other predictors. Values above 5 or 10 are rough prompts for investigation, not universal failure thresholds. Domain-guided removal, centering, combining features, or ridge regularization may help.

**Q.What is endogeneity or omitted-variable bias?**

Endogeneity means an included regressor is correlated with the error term, violating exogeneity. It can arise from confounders omitted from the model, simultaneity, measurement error, or sample selection. Adding an omitted variable helps only when it is correctly identified and observed. Depending on context, randomized designs, instrumental variables, natural experiments, panel methods, or causal modeling may be required.

**Q.Which alternative approaches help when standard OLS assumptions fail?**

For misspecified mean structure, consider transformations, splines, feature interactions, or nonlinear models. For heteroscedasticity, use robust standard errors or WLS. For autocorrelation, consider GLS, HAC inference, or time-series models. For outliers/heavy tails, consider robust or quantile regression. For correlated predictors, use ridge/lasso or domain-guided feature engineering. For endogeneity, consider a valid instrumental-variable or causal identification strategy. Changing the algorithm alone does not fix a causal design problem.

**Q.What is nonlinear regression and how is it different from polynomial regression?**

A model is *linear in parameters* if its fitted mean is a linear combination of unknown coefficients, even if features include $X^2$, splines, or interactions. Thus ordinary polynomial regression can be fitted by OLS. *Nonlinear regression* in the strict parametric sense has coefficients entering nonlinearly, such as $Y=a\exp(bX)+\varepsilon$, and typically requires nonlinear optimization.

**Q.What is regularization, and why is it useful?**

Regularization penalizes model complexity during fitting, often reducing variance and improving generalization. A common objective is 

$$\min_\beta\;\sum_i (y_i-x_i^\top\beta)^2+\lambda\,\mathcal R(\beta).$$

 For ridge, $\mathcal R(\beta)=\|\beta\|_2^2$; for lasso, $\mathcal R(\beta)=\|\beta\|_1$. The intercept is typically left unpenalized after appropriate feature preprocessing. $\lambda$ is tuned on validation data, and regularization can introduce bias while lowering overall prediction error.

**Q.What is the difference between L1 and L2 regularization?**

**L1 (lasso)** penalizes $\sum_j|\beta_j|$ and can drive coefficients exactly to zero, making it useful for feature selection. **L2 (ridge)** penalizes $\sum_j\beta_j^2$ and typically shrinks correlated coefficients smoothly without making them exactly zero. Elastic net mixes both penalties. Scale numerical predictors before comparing penalties, and tune strength on training/validation data.

**Q.What is Huber loss, and when would you use it?**

Huber loss is quadratic for small residuals and grows linearly for large residuals: 

$$L_\delta(r)=\begin{cases}\tfrac12r^2,&|r|\leq\delta,\\\delta(|r|-\tfrac12\delta),&|r|>\delta.\end{cases}$$

 It reduces the impact of large residuals compared with squared loss while retaining smooth behavior near zero. Choose $\delta$ according to residual scale and validate performance against relevant metrics.

**Q.What is adjusted $R^2$, and why can ordinary $R^2$ be misleading?**

Ordinary training $R^2$ generally does not decrease when extra regressors are added to an OLS model with an intercept, even if they are irrelevant. Adjusted $R^2=1-(1-R^2)(n-1)/(n-p)$, where $p$ counts estimated coefficients including the intercept, penalizes the number of model terms. Neither metric replaces held-out predictive evaluation or assumption checks.

**Q.What is the Akaike Information Criterion (AIC)?**

AIC is an in-sample model-selection criterion balancing fit and parameter count: $\mathrm{AIC}=2k-2\log\hat L$, where $k$ is the number of estimated parameters and $\hat L$ is maximum likelihood. Lower AIC favors a model within a comparable candidate set fitted to the same response data. It is not an absolute goodness-of-fit guarantee or a replacement for validation.

**Q.What is logistic regression, and what assumptions matter?**

Logistic regression models a binary outcome’s conditional probability via $\log\frac{p(X)}{1-p(X)}=\beta_0+\beta^\top X$. Assumptions include suitable independent (or correctly modeled dependent) observations, correct logit-scale functional form, no perfect separation when using ordinary finite MLE, and adequately controlled collinearity. Predictor effects are interpreted as changes in log odds, not direct changes in probability. Assess discrimination, calibration, and decision-specific thresholds.

**Q.What is Poisson regression and when should you consider negative binomial regression?**

Poisson regression models nonnegative count outcomes, often with $\log E[Y\mid X]=\beta_0+\beta^\top X$ and optionally an exposure offset. The Poisson distribution equates conditional mean and variance. Strong overdispersion may motivate negative binomial regression, quasi-Poisson variance adjustments, or alternative data-generating models. Check excess zeros and dependence when relevant.

**Q.What is quantile regression?**

Quantile regression models a conditional quantile such as the median rather than the conditional mean. It minimizes an asymmetric absolute-error (pinball) loss. It is useful for skewed outcomes, distributional heterogeneity, or robust conditional-median predictions. It still requires appropriate sampling and model specification; it is not entirely assumption-free.

**Q.What is the Cox proportional hazards model?**

The Cox model relates a time-to-event hazard to covariates as $h(t\mid X)=h_0(t)\exp(\beta^\top X)$, leaving baseline hazard $h_0(t)$ unspecified. The key proportional-hazards assumption is that hazard ratios are constant over time for fixed covariates unless the model explicitly incorporates time-varying effects. Censoring and model diagnostics must be handled appropriately.

**Q.What is the relationship between Pearson correlation and $R^2$ in regression?**

For *simple* OLS regression with one predictor and an intercept, the in-sample $R^2$ equals the squared sample Pearson correlation between $X$ and $Y$. This equality does not apply in the same way to arbitrary multivariable regressions. A correlation coefficient alone does not identify causal effects.

**Q.What is the Breusch–Pagan test?**

The Breusch–Pagan test checks whether error variance changes systematically with specified regressors. It typically regresses squared residuals on covariates and uses an asymptotic reference distribution. A small $p$-value suggests heteroscedasticity; its interpretation depends on model assumptions and test variant. Use it alongside residual plots and robust inference.

# Core Machine Learning

**Q.What is data science? How do supervised and unsupervised learning differ?**

Data science combines data acquisition, domain understanding, statistics, computation, modeling, experimentation, and communication to generate actionable evidence. In **supervised learning**, labeled examples $(X,Y)$ guide prediction of an observed target (classification or regression). In **unsupervised learning**, algorithms seek patterns in features $X$ without required target labels (clustering, dimensionality reduction, density estimation). Neither automatically implies causal inference.

**Q.When should you use classification instead of regression?**

Use classification when the target is categorical, such as fraud versus non-fraud. Use regression when the target is numerical and its magnitude matters, such as revenue or temperature. For binary outcomes, a classifier may estimate $P(Y=1\mid X)$; thresholds convert probabilities into actions. Count and time-to-event outcomes may require specialized predictive models.

**Q.What is a confusion matrix?**

A binary confusion matrix summarizes actual versus predicted labels as true positives (TP), false positives (FP), true negatives (TN), and false negatives (FN). From these counts calculate precision $\mathrm{TP}/(\mathrm{TP}+\mathrm{FP})$, recall $\mathrm{TP}/(\mathrm{TP}+\mathrm{FN})$, specificity $\mathrm{TN}/(\mathrm{TN}+\mathrm{FP})$, and accuracy $(\mathrm{TP}+\mathrm{TN})/N$. When a denominator is zero, the metric requires a specified convention.

**Q.What are precision, recall, specificity, and F1-score?**

$$\mathrm{Precision}=\frac{TP}{TP+FP},\quad
\mathrm{Recall}=\frac{TP}{TP+FN},\quad
\mathrm{Specificity}=\frac{TN}{TN+FP}.$$

 Precision measures reliability of positive predictions; recall (sensitivity) measures coverage of actual positives; specificity measures coverage of actual negatives. Their harmonic mean $F_1=2PR/(P+R)$ balances precision and recall but ignores true negatives and may be unsuitable when costs are asymmetric.

**Q.How does an ROC curve work?**

A receiver operating characteristic (ROC) curve plots true-positive rate (recall) against false-positive rate ($FP/(FP+TN)$) over classification thresholds. ROC–AUC summarizes ranking discrimination: it can be interpreted as the probability that a randomly chosen positive scores higher than a randomly chosen negative, with tie handling. On severely imbalanced data, a precision–recall curve may expose positive-class performance more clearly. Neither curve alone assesses calibration.

**Q.How would you evaluate a logistic regression classifier?**

Evaluate discrimination using ROC–AUC and often PR–AUC, probability quality using log loss or Brier score, calibration using reliability plots, and thresholded decisions using confusion-matrix metrics. Compare against relevant baselines on validation and genuinely held-out test data. Check prevalence shifts, subgroup reliability, and whether features leak future information.

**Q.Is model accuracy the same as model performance?**

No. Accuracy is only one metric and can conceal failure on rare but important cases. In fraud detection with 0.1% prevalence, a model that always predicts “not fraud” can reach 99.9% accuracy while detecting none of the fraud. Choose metrics based on task costs: PR–AUC, recall at fixed precision, expected financial cost, calibration, latency, and robustness may matter more than raw accuracy.

**Q.How do you handle class imbalance?**

Begin with stratified splits (unless ordering or groups require another scheme), a representative test set, and relevant metrics such as PR–AUC or recall at fixed false-positive rate. Consider class weights, threshold tuning, targeted undersampling/oversampling, SMOTE (on training folds only), focal loss, and probability calibration. Ensure synthetic samples or duplicated minority cases never leak across train/test boundaries. Optimizing precision–recall trade-offs is ultimately a decision-cost question.

**Q.How do you evaluate machine-learning models reliably?**

Define the target population, business metric, and leakage risks first. Create development and untouched test partitions; use suitable cross-validation on the development set for model and hyperparameter selection. Select metrics based on prediction task and operating costs, inspect calibration, confidence intervals, subgroup performance, drift sensitivity, and learning curves, then report final performance once on the held-out set.

**Q.What is cross-validation, and when should it be used?**

In $k$-fold cross-validation, data are split into $k$ folds; each fold becomes validation once while the model fits on the other $k-1$. Repeated or stratified variants can reduce sensitivity to splits. For groups or time series, keep correlated entities or future timestamps from leaking into training. All feature selection, imputation, and scaling must occur inside each training fold.

**Q.What are the major methods for preventing overfitting?**

Use a sufficiently representative dataset, validation-based complexity selection, regularization, early stopping, feature selection, pruning, augmentation when valid, and simpler architectures where suitable. Diagnose the generalization gap using learning curves. Do not tune repeatedly on the final test set; doing so converts it into a de facto validation set.

**Q.How is $k$-nearest neighbors (KNN) different from $k$-means?**

**KNN** is a supervised, instance-based algorithm that predicts a label or numerical target from nearby labeled examples. **$k$-means** is an unsupervised clustering algorithm that assigns points to $k$ clusters while iteratively minimizing within-cluster squared Euclidean distances to centroids. The symbol $k$ means neighbor count in KNN and cluster count in $k$-means. Scaling and the chosen distance metric strongly affect both methods.

**Q.What is Bayes’ theorem and how is it used in machine learning?**

Bayes’ theorem is $P(A\mid B)=P(B\mid A)P(A)/P(B)$ when $P(B)>0$. It converts prior probabilities into posterior probabilities using observed evidence. Applications include probabilistic classification, Bayesian parameter estimation, filtering, and uncertainty-aware predictions. Posterior estimates depend on both the likelihood model and prior assumptions.

**Q.Why is Naive Bayes called *naive*?**

Naive Bayes assumes predictors are conditionally independent given the class: $P(X_1,\ldots,X_d\mid Y)=\prod_j P(X_j\mid Y)$. This assumption is often unrealistic (words in a document, for example, are dependent) but yields fast, competitive classifiers in tasks such as text classification. Its raw probabilities can be poorly calibrated when dependence is strong.

**Q.What is the difference between generative and discriminative models?**

A **generative classifier** models a joint distribution $P(X,Y)$, often via $P(X\mid Y)P(Y)$, and can use Bayes’ rule for classification (e.g., Naive Bayes, LDA, QDA). A **discriminative classifier** models $P(Y\mid X)$ or learns a decision boundary directly (e.g., logistic regression, SVM). Modern generative models can also learn $P(X)$ without class labels. Neither family is universally better: compare predictive requirements, assumptions, dataset size, and whether data generation is needed.

**Q.What is deep learning compared with other machine-learning methods?**

Deep learning uses neural networks with multiple learned representation layers. It is especially effective for high-dimensional modalities such as images, speech, and text, often reducing the need for manual feature construction. Compared with simpler tabular algorithms, deep models can require more data, compute, tuning, and interpretability safeguards. Model choice should follow task requirements rather than architectural fashion.

**Q.How do you prune a decision tree?**

Pruning reduces model complexity to improve generalization. *Pre-pruning* stops growth using maximum depth, minimum leaf size, or minimum impurity decrease. *Post-pruning* first grows a tree and then removes branches, often using cost-complexity pruning with penalty $\alpha$ per terminal leaf. Select pruning strength through validation rather than only training fit.

**Q.When are ensembles useful?**

Ensembles combine models to improve robustness or predictive performance. Bagging and random forests average unstable learners to reduce variance; boosting (such as gradient-boosted trees) builds learners sequentially to reduce an objective; stacking learns how to combine base predictions without leakage. Ensembles are valuable for complex tabular prediction but increase runtime, maintenance complexity, and explanation burden.

**Q.What is the kernel trick?**

A kernel $K(x,z)=\langle\phi(x),\phi(z)\rangle$ computes inner products in an implicit feature space without constructing $\phi$ explicitly. Kernel SVMs can therefore learn nonlinear decision boundaries using linear operations in that feature space. Kernel choice, regularization, scaling, and compute cost are crucial; kernel methods can become expensive as sample count grows.

**Q.What is the bias–variance trade-off?**

Prediction error can reflect systematic approximation error (bias), sensitivity to data fluctuations (variance), and irreducible noise. More flexible models often reduce approximation bias but risk higher variance; regularization may increase bias while reducing variance. This decomposition is cleanest for squared-error prediction in a specified setting. Validation helps select the useful complexity level.

**Q.What is the difference between model discrimination and calibration?**

Discrimination asks whether a model ranks positive cases above negative ones, as measured by ROC–AUC. Calibration asks whether predicted probabilities match empirical event frequencies: among observations assigned risk 0.2, about 20% should experience the event under good calibration. A model can have good AUC but poor calibration. Reliability diagrams, Brier score, and log loss help assess probability quality.

**Q.What is the role of train, validation, and test sets?**

The training set fits parameters. The validation set (or development cross-validation) supports model choice, hyperparameter tuning, and threshold selection. The untouched test set estimates final generalization after these choices are frozen. When data have groups, sites, or chronology, split according to the intended deployment scenario; random splitting may substantially overestimate generalization.

**Q.How does XGBoost handle missing values?**

For tree-based boosting, XGBoost can learn a default direction at a split for observations with missing feature values, choosing the direction that improves the training objective. Thus explicit imputation may not be required for supported tree boosters, although missingness mechanisms and feature meaning still matter. It is *not* accurate to claim that missing observations necessarily receive zero leaf weights or that XGBoost uses a fixed number of splits for missing values.

**Q.How can XGBoost address highly imbalanced classes?**

XGBoost supports observation weights and, for binary objectives, `scale_pos_weight` to increase the influence of positive cases. It also supports evaluation metrics such as `aucpr` and tunable decision thresholds (outside model fitting). A starting heuristic is $N_{\mathrm{negative}}/N_{\mathrm{positive}}$, but this is not universally optimal and can worsen probability calibration. Standard XGBoost does not automatically perform stratified sampling at every boosting round. Validate against the true deployment distribution and tune hyperparameters/thresholds without test leakage.

**Q.How do you choose a favorite ML algorithm and explain it in under a minute?**

A strong interview answer names the algorithm, its core mechanism, when it works well, one limitation, and an evaluation strategy. Example: “Gradient-boosted trees build trees sequentially, with each tree correcting the current model’s objective via gradient information. They perform very well on heterogeneous tabular datasets and capture nonlinear interactions. I control overfitting using learning rate, tree depth, subsampling, and early stopping, and validate using a leakage-safe split. Their limitations include tuning complexity and potentially poor extrapolation.

# Neural Networks and Optimization

**Q.What is the vanishing-gradient problem, and how can it be mitigated?**

In backpropagation, gradients are multiplied by successive Jacobians. If their relevant singular values are repeatedly small, early-layer gradients can become tiny, slowing learning. Saturating sigmoid/tanh activations can aggravate this, as can poor initialization or deep recurrent dependencies. Common remedies include ReLU-family activations where suitable, appropriate initialization, residual/skip connections, normalization, gated recurrent architectures, and careful architecture/optimizer design. Adaptive optimizers can help optimization but do not universally eliminate vanishing gradients.

**Q.How does a residual connection help optimization?**

A residual block learns $y=F(x)+x$ (or a projected skip connection). The identity path gives information and gradients a direct route through depth, helping train much deeper networks. It does not literally skip all computations in backpropagation: both the residual branch and skip path contribute to derivatives.

**Q.What is batch normalization, and when might it be less suitable?**

Batch normalization standardizes intermediate activations using batch statistics during training and learned running statistics or equivalent estimates at inference, with trainable scale and shift. It can stabilize and accelerate training in many architectures. Very small batch sizes, distribution shifts, or particular sequence models can make alternatives such as layer or group normalization preferable.

**Q.How do Adam and RMSProp differ from plain gradient descent?**

Plain gradient descent uses a fixed (or scheduled) global learning rate on gradients. RMSProp scales updates using an exponential moving average of squared gradients. Adam additionally tracks a first-moment estimate and applies bias correction. These adaptive methods often improve practical convergence but are not guaranteed to produce better generalization; learning-rate schedules and decoupled weight decay can matter.

# Time-Series Analysis and Forecasting

**Q.What is forecasting, and how is it different from prediction?**

*Prediction* broadly means estimating an unknown outcome, present or future. *Forecasting* specifically estimates future values, commonly respecting time order and using past observations plus available covariates. Forecasts can be generated by statistical models, machine learning, or expert judgment; the distinction is not simply that forecasts are quantitative while predictions are informal.

**Q.What are the key components of a time series?**

Common descriptive components are **trend** (long-run level movement), **seasonality** (regular periodic variation), **cycles** (longer or less regular oscillations), and **irregular variation/noise**. An additive decomposition is $Y_t=T_t+S_t+R_t$, while a multiplicative form may be appropriate when fluctuations scale with the series level. Not every series contains every component.

**Q.What is time-series analysis versus cross-sectional analysis?**

Time-series observations are indexed by time, often with serial dependence and nonstationarity. Cross-sectional observations represent different units at a given time or period. Time-series analyses must account for chronology, autocorrelation, regime changes, and leakage from future information. Panel data combine cross-sectional units observed repeatedly through time.

**Q.What is stationarity, and how can nonstationarity be addressed?**

A weakly stationary series has constant mean, constant finite variance, and autocovariance depending on lag rather than calendar time. Trends, unit roots, changes in variance, and structural breaks can violate this. Remedies may include detrending, differencing, transforms, or models that explicitly account for changing regimes. Not all forecasting approaches require stationarity, and blindly differencing a stable series can be harmful.

**Q.What is the Augmented Dickey–Fuller (ADF) test?**

The ADF test investigates a unit-root null hypothesis against an alternative such as stationarity around a specified deterministic component. It adds lagged difference terms to account for serial correlation. The result depends on lag selection, inclusion of a constant/trend, and sample size. Failure to reject a unit root is not proof of nonstationarity, and structural breaks can complicate the test.

**Q.What cross-validation procedure should be used for time-series forecasting?**

Use *rolling-origin* or *forward-chaining* evaluation that trains only on observations preceding each validation horizon. For example, train on periods $1$–$4$, validate on $5$; then train on $1$–$5$, validate on $6$. A sliding window can be used when older data become irrelevant. Respect forecast horizon, data-release delays, entity grouping, and any needed gap to prevent feature leakage.

**Q.How should missing values in a time series be handled?**

First identify whether missingness reflects sensor failure, genuine absence of events, or irregular sampling. Options include forward filling when justified, interpolation, seasonal imputation, Kalman smoothing/filtering, or model-based estimates. Offline smoothing may use future observations, so it is invalid for a real-time forecasting pipeline if those observations would not yet be available. Validate the impact of imputation on a chronological holdout.

**Q.How can bootstrapping be performed on time-series data?**

Ordinary independent-row bootstrap destroys temporal dependence and can underestimate uncertainty. *Moving-block*, circular-block, stationary-block, or model-based residual bootstrap methods resample data in a way that retains relevant dependence. Block length should reflect the series’ dependence structure and uncertainty objective. For nonstationary series, specialized designs or modeling may be required.

**Q.What is the difference between noise and outliers in a time series?**

Noise is routine unexplained stochastic variation; outliers are unusually large or atypical observations relative to a temporal model. A seasonal spike may look extreme in a raw plot yet be expected after conditioning on day of week or holidays. Investigate anomalies using residuals from a suitable temporal baseline before excluding them.

**Q.What is cointegration?**

Two or more integrated, typically $I(1)$, time series are cointegrated if a nontrivial linear combination is stationary. This indicates a statistically stable long-run equilibrium relationship despite individual stochastic trends. Error-correction models represent both short-run changes and adjustments toward that equilibrium. Cointegration alone does not establish causation.

**Q.What is a GARCH model, and when is it useful?**

GARCH models time-varying conditional variance, widely used for volatility clustering in financial returns. A basic GARCH(1,1) model specifies $\sigma_t^2=\omega+\alpha\varepsilon_{t-1}^2+\beta\sigma_{t-1}^2$. Parameter constraints ensure nonnegative variance; stationarity often additionally requires $\alpha+\beta<1$. It forecasts conditional volatility rather than automatically forecasting the return mean.

**Q.What is a multivariate time series and how can it be forecast?**

A multivariate time series contains several variables observed over time whose past values may help predict one another. A vector autoregression (VAR) uses lagged values of all variables to predict each component, under appropriate stationarity or other modeling conditions. VARMA, vector error-correction models, state-space models, and machine-learning methods are alternatives. Carefully assess leakage, dimensionality, and forecast-horizon stability.

**Q.What is a Markov model’s role in finance?**

Markov chains can describe transitions among credit ratings or market regimes, while continuous-state Markov processes are used in some interest-rate and asset-price models. The next-state distribution depends on the current state under the modeled Markov property. This is a modeling simplification; financial series may exhibit longer memory, latent states, or regime instability.

**Q.What are common forecasting errors and ways to measure them?**

MAE measures mean absolute error, RMSE emphasizes large squared errors, and MASE scales forecast error relative to a naive reference. MAPE can explode or become undefined near zero actual values. For probabilistic forecasts, use coverage and sharpness of prediction intervals, pinball loss for quantiles, or proper scoring rules. Always compare against seasonal-naive and simple baselines appropriate to the forecast horizon.

# Applied Questions, Experiments, and Coding

**Q.What is the goal of A/B testing?**

A/B testing estimates the causal effect of assigning users or other experimental units to two variants under randomization. Define a primary outcome, guardrail metrics, eligible population, unit of randomization, duration, and decision rule *before* starting. Compare conversion rates or other estimands, report effect size and uncertainty, and account for interference, repeated exposure, multiple comparisons, and sequential monitoring. The best variant is the one that improves relevant utility, not automatically the one with the smallest $p$-value.

**Q.How do you uniformly generate an integer from 1 to 7 using a fair six-sided die?**

Roll the die twice and let $a,b\in\{1,\ldots,6\}$. Map the outcome to $k=6(a-1)+(b-1)$, which is uniform on $\{0,\ldots,35\}$. If $k=35$, discard both rolls and repeat. Otherwise return $1+(k\bmod 7)$. Because $35=5\times7$, each output occurs exactly five times among accepted outcomes and therefore has probability $1/7$. The acceptance probability per two-roll attempt is $35/36$.

**Q.How could you design a recommender system for a company?**

Define the objective (relevance, retention, conversion, revenue, or long-term user utility) and interaction logging. Establish popularity and content-based baselines, then consider collaborative filtering or embeddings for candidate generation followed by a ranking model. Address cold starts using content and contextual signals. Use offline ranking metrics (Recall@$K$, NDCG@$K$), exposure-aware evaluation, diversity/fairness checks, and randomized online tests. Production design also needs latency budgets, feedback loops, filtering, privacy controls, and monitoring.

**Q.How would you approach the Netflix Prize-style recommendation problem?**

Start with explicit-rating baselines incorporating global, user, and item biases. Train latent-factor matrix factorization with regularization, explore neighborhood models and temporal dynamics, and compare through user-aware held-out ratings using RMSE if that is the competition metric. Blend complementary models only if they improve validation performance. In a live product, supplement RMSE with top-$K$ usefulness, coverage, cold-start performance, novelty, and online experiments.

**Q.Give pseudocode for a parallel algorithm.**

For a parallel reduction of $n$ values across $P$ workers:

1.  Partition input indices into $P$ disjoint chunks.

2.  On each worker, calculate a local partial sum $s_p$ using only its chunk.

3.  Combine $s_1,\ldots,s_P$ with a tree reduction to obtain the global sum.

4.  Return the global sum (and divide by $n$ if a mean is required).

The computational work is $O(n/P)$ per worker plus communication overhead; tree-reduction depth is $O(\log P)$. For floating-point values, reduction order can cause minor reproducibility differences. This template also generalizes to counts, extrema, and associative summary statistics.

**Q.What should you investigate before deploying an ML model?**

Confirm target definition, leakage-safe validation, data and model versioning, latency, throughput, monitoring, rollback, access controls, security, and reproducibility. Validate calibration, subgroup behavior, drift detection, failure behavior, and retraining triggers. Shadow deployments or staged rollouts reduce release risk. For consequential uses, document how human oversight and error costs affect action thresholds.

**Q.How can you evaluate whether a data-cleaning or feature-engineering change helped?**

Treat the change as a controlled model-pipeline modification. Apply it only within training folds, keep downstream modeling and evaluation procedures comparable, and quantify effects on holdout metrics, uncertainty, runtime, and subgroup performance. Where feasible use paired predictions or repeated validation to reduce comparison noise. Changes to measurement or cohort definitions should also be checked for shifts in the estimand.

# Additional Time-Series Interview Resources

- [DevInterview: Time-Series Interview Questions](https://devinterview.io/questions/machine-learning-and-data-science/time-series-interview-questions/)

- [QFE University: 30 Time-Series Analysis Interview Q&A](https://qfeuniversity.com/30-time-series-analysis-interview-qa/)
