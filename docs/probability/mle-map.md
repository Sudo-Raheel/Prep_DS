# MLE and MAP

!!! abstract "At a glance"
    $$\boxed{
    \hat\theta_{\text{MLE}}=\arg\max_\theta \log p(D\mid\theta)
    \qquad
    \hat\theta_{\text{MAP}}=\arg\max_\theta \big[\log p(D\mid\theta)+\log p(\theta)\big]
    }$$

    MLE asks which parameter makes the observed data least surprising. MAP adds a log-prior, so it is the same objective plus a regularizer. A flat prior makes them identical, and as $n\to\infty$ the prior washes out.

## Prerequisites (quick mental check)

- **Probability basics:** random variables, PDFs/PMFs, independence. The i.i.d. assumption lets the likelihood factor into a product.
- **Common distributions:** Bernoulli, Binomial, Gaussian, (Poisson).
- **Logs and calculus:** product $\to$ sum, derivative set to zero.
- **Likelihood vs probability:** $p(\text{data}\mid\theta)$ viewed as a function of $\theta$ with data fixed; *not* a distribution over $\theta$.
- **Expectation and variance:** needed for the bias discussion.

Optional later: KL divergence (MLE $\equiv$ minimizing KL between the empirical distribution and the model), Fisher information (asymptotic normality, Cramér–Rao).

## Notation

| Symbol | Meaning |
| --- | --- |
| $x_1,\dots,x_n$ | the $n$ observed data points |
| $\theta$ | unknown model parameter |
| $p(x\mid\theta)$ | probability (or density) of $x$ when the parameter is $\theta$ |
| $L(\theta)$ | likelihood, $L(\theta)=p(x_1,\dots,x_n\mid\theta)$, as a function of $\theta$ |
| $\prod$ | product, $\prod_{i=1}^n a_i = a_1 a_2\cdots a_n$ |
| $\arg\max_\theta f(\theta)$ | the *value* of $\theta$ that maximizes $f$ |
| $\hat\theta$ | an estimate of $\theta$ computed from data |

**i.i.d.** *Independent*: one point tells nothing about another, so the joint factors into a product ($P(A\cap B)=P(A)P(B)$). *Identically distributed*: all points share the same distribution and the same $\theta$.

## MLE: the core idea

MLE asks: *which parameter value makes the data I actually saw least surprising?* For i.i.d. data,

$$L(\theta)=\prod_{i=1}^n p(x_i\mid\theta),\qquad
\hat\theta_{\text{MLE}}=\arg\max_\theta L(\theta).$$

!!! tip "Key idea: likelihood vs probability"
    $L(\theta)$ has the same formula as the probability of the data, but $\theta$ varies and the data is fixed. It does **not** integrate to 1 over $\theta$ and is **not** "the probability that $\theta=0.7$". That statement needs a prior (MAP/Bayes).

### Why maximize the log-likelihood

Since $\log$ is strictly increasing, $\arg\max_\theta \log L(\theta)=\arg\max_\theta L(\theta)$ (the maximizer keeps the same location in $\theta$). Reasons to use it:

- **Product $\to$ sum:** $\log\prod_i p(x_i\mid\theta)=\sum_i\log p(x_i\mid\theta)$, easier to differentiate.
- **Numerical stability:** a product of many numbers $<1$ underflows to $0$; a sum of logs does not.

!!! warning "Common mistake"
    Taking the log does *not* create uniqueness of the maximizer; $L$ and $\log L$ have identical maximizers. (Log-concavity of a model can help, but it is a separate property.)

### Recipe

1. Write $L(\theta)=\prod_i p(x_i\mid\theta)$.
2. Take the log; drop any terms without $\theta$.
3. Differentiate, set to $0$, solve.
4. Check the second derivative is negative (a max, not a min), and that the answer lies in the valid parameter range.

!!! warning "Sanity check"
    If $\theta$ is a probability and you get $\hat\theta=2$, there is an algebra slip. Re-check the chain rule: $\frac{d}{d\theta}\log(1-\theta)=-\frac{1}{1-\theta}$.

## MLE for the Bernoulli (coin)

Sequence H,H,T with $\theta=P(\text{heads})$: $L(\theta)=\theta^2(1-\theta)$, so $\log L=2\log\theta+\log(1-\theta)$ and

$$\frac{2}{\theta}-\frac{1}{1-\theta}=0\;\Rightarrow\;2(1-\theta)=\theta\;\Rightarrow\;\hat\theta=\tfrac23 .$$

Second derivative $-\frac{2}{\theta^2}-\frac{1}{(1-\theta)^2}<0$, so $\log L$ is concave and $2/3$ is the unique maximum.

**General case: $k$ heads in $n$ flips.**

$$\log L(\theta)=k\log\theta+(n-k)\log(1-\theta)
\;\Rightarrow\;
\frac{k}{\theta}=\frac{n-k}{1-\theta}
\;\Rightarrow\;
\boxed{\hat\theta_{\text{MLE}}=\frac{k}{n}}$$

**Where is $\binom{n}{k}$?** If you record only the count $k$, $P(k\mid\theta)=\binom nk\theta^k(1-\theta)^{n-k}$ and $\log L=\log\binom nk+k\log\theta+(n-k)\log(1-\theta)$. The term $\log\binom nk$ does not contain $\theta$, so it vanishes on differentiation. This is exact (no Stirling approximation). Likewise, for a specific sequence there is no coefficient at all. **General rule:** any factor of $L(\theta)$ independent of $\theta$ can be dropped.

## MLE for the Gaussian

For i.i.d. $x_i\sim\mathcal N(\mu,\sigma^2)$,

$$p(x\mid\mu,\sigma^2)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\Big(-\frac{(x-\mu)^2}{2\sigma^2}\Big),$$

$$\log L(\mu,\sigma^2)=-\frac n2\log(2\pi\sigma^2)-\frac{1}{2\sigma^2}\sum_{i=1}^n(x_i-\mu)^2 .$$

**Mean.** $\mu$ appears only in the last term, so maximizing over $\mu$ means minimizing the **sum of squared errors** $\sum_i(x_i-\mu)^2$. Differentiating: $-2\sum_i(x_i-\mu)=0$, so

$$\hat\mu_{\text{MLE}}=\frac1n\sum_i x_i\quad\text{(the sample mean).}$$

It is the mean of the *sample*, an estimate of the unknown true $\mu$.

**Variance.** With $v=\sigma^2$ and $\mu=\hat\mu$:

$$-\frac{n}{2v}+\frac{1}{2v^2}\sum_i(x_i-\hat\mu)^2=0
\;\Rightarrow\;
\boxed{\hat\sigma^2_{\text{MLE}}=\frac1n\sum_i(x_i-\hat\mu)^2}$$

### Bias: why the sample variance uses $n-1$

!!! tip "Intuition (lead with this in interviews)"
    You used the data to compute $\bar x$, so the deviations are forced to satisfy $\sum_i(x_i-\bar x)=0$. Only $n-1$ of them are free: $n-1$ degrees of freedom. Also, $\bar x$ minimizes $\sum_i(x_i-c)^2$ over $c$, so $\sum_i(x_i-\bar x)^2\le\sum_i(x_i-\mu)^2$, which makes dividing by $n$ underestimate $\sigma^2$.

**Exact calculation.** Using $\sum_i(x_i-\mu)^2=\sum_i(x_i-\bar x)^2+n(\bar x-\mu)^2$:

$$\mathbb{E}\Big[\sum_i(x_i-\mu)^2\Big]=n\sigma^2,\qquad
\mathbb{E}\big[n(\bar x-\mu)^2\big]=n\,\mathrm{Var}(\bar x)=\sigma^2,$$

$$\Rightarrow\;\mathbb{E}\Big[\sum_i(x_i-\bar x)^2\Big]=(n-1)\sigma^2 .$$

Hence dividing by $n-1$ is unbiased, while $\mathbb{E}[\hat\sigma^2_{\text{MLE}}]=\frac{n-1}{n}\sigma^2$.

- The MLE is biased but **consistent**: the bias $\to0$ as $n\to\infty$.
- The $n-1$ estimate is the larger of the two. For $n=100$ the ratio is $100/99\approx1\%$ (small); for $n=5$ it is $25\%$.
- The sample *standard deviation* is still slightly biased (concavity of $\sqrt{\cdot}$, Jensen).

## MLE and loss functions

!!! tip "Core principle"
    **Minimizing a loss = maximizing a log-likelihood under some noise assumption.** Loss $=$ negative log-likelihood (NLL), purely because optimizers are conventionally written to *minimize*.

### Gaussian noise $\Rightarrow$ MSE

For $y_i=f(x_i;\theta)+\varepsilon_i$, $\varepsilon_i\sim\mathcal N(0,\sigma^2)$:

$$\log L(\theta)=\text{const}-\frac{1}{2\sigma^2}\sum_i\big(y_i-f(x_i;\theta)\big)^2,$$

so maximizing $\log L$ $\Leftrightarrow$ minimizing the squared error (MSE up to the factor $1/n$).

### Laplace noise $\Rightarrow$ MAE

Density $p(y\mid f)=\frac{1}{2b}\exp(-|y-f|/b)$:

$$\log L(\theta)=-n\log(2b)-\frac1b\sum_i|y_i-f(x_i;\theta)| ,$$

so MLE minimizes $\sum_i|y_i-f(x_i;\theta)|$, the absolute-error (L1) loss.

### Location estimate: mean vs median

| Noise | Loss | Location estimate |
| --- | --- | --- |
| Gaussian | squared | mean |
| Laplace | absolute | median |

*Why median:* nudging $m$ right increases the distance to points on the left and decreases it to points on the right; $\sum_i|x_i-m|$ stops improving when half the points lie on each side. Example: $\{1,2,3,4,100\}$ has mean $22$ but median $3$. The Laplace density has heavier tails than the Gaussian, so a far point is less surprising and pulls the fit less (linear vs quadratic penalty): MAE is robust to outliers.

### Bernoulli $\Rightarrow$ binary cross-entropy

Let $y_i\in\{0,1\}$ and $p_i=f(x_i;\theta)=P(y_i=1\mid x_i)$.

1. One point (exponents act as a switch): $P(y_i\mid x_i;\theta)=p_i^{\,y_i}(1-p_i)^{1-y_i}$. Check: $y_i=1\to p_i$, $y_i=0\to1-p_i$.
2. Dataset (independence): $L(\theta)=\prod_i p_i^{\,y_i}(1-p_i)^{1-y_i}$.
3. Log: $\log L=\sum_i\big[y_i\log p_i+(1-y_i)\log(1-p_i)\big]$.
4. Negate and average (dividing by $n$ does not change the argmin):

$$\boxed{\mathrm{BCE}(\theta)=-\frac1n\sum_i\big[y_i\log p_i+(1-y_i)\log(1-p_i)\big]}$$

With a constant $p_i=\theta$ this reduces to the coin formula $k\log\theta+(n-k)\log(1-\theta)$.

### Categorical $\Rightarrow$ multi-class cross-entropy

Labels are one-hot $y_{ik}\in\{0,1\}$, $\sum_k y_{ik}=1$; the model gives $p_{ik}=P(\text{class }k\mid x_i)$ (typically via softmax), $\sum_k p_{ik}=1$.

$$P(y_i\mid x_i;\theta)=\prod_{k=1}^K p_{ik}^{\,y_{ik}},\quad
L(\theta)=\prod_i\prod_k p_{ik}^{\,y_{ik}},\quad
\log L=\sum_i\sum_k y_{ik}\log p_{ik},$$

$$\boxed{\mathrm{CE}(\theta)=-\frac1n\sum_i\sum_{k=1}^K y_{ik}\log p_{ik}}$$

With one-hot labels the inner sum collapses to $-\log p_{i,c}$ ($c$ = true class). Binary cross-entropy is the $K=2$ special case. Examples: assigned probability $0.25\Rightarrow$ loss $-\log0.25=\log4\approx1.386$; probability $1\Rightarrow$ loss $0$; probability $\to0\Rightarrow$ loss $\to\infty$ (confident wrong answers are punished very harshly).

!!! example "Interview: why cross-entropy and not MSE for logistic regression?"
    - BCE is exactly the NLL of a Bernoulli model, which matches a $0/1$ label; MSE assumes Gaussian noise, which does not.
    - With a sigmoid output, the MSE gradient vanishes when the model is confidently wrong (saturation), so learning stalls. For softmax/sigmoid + CE, the gradient with respect to the logits is simply $p-y$, which stays large exactly when the model is wrong.

## MLE summary and weakness

1. $L(\theta)=p(\text{data}\mid\theta)$ as a function of $\theta$; a product for i.i.d. data.
2. Take the log (product $\to$ sum, stable), maximize, drop terms without $\theta$.
3. Bernoulli: $\hat\theta=k/n$. Gaussian: sample mean; $\hat\sigma^2$ with $1/n$ (biased, consistent).
4. Loss = NLL: Gaussian $\to$ MSE, Laplace $\to$ MAE, Bernoulli $\to$ BCE, categorical $\to$ CE.
5. Properties: consistent, asymptotically normal, invariant under reparametrization.

**Weakness: overfitting to small data.** Three flips, three heads: $L=\theta^3$, $\log L=3\log\theta$, derivative $3/\theta$ has no zero. Since $\theta\in[0,1]$, the maximum is at the boundary, $\hat\theta_{\text{MLE}}=1$ (agrees with $k/n$). This says tails are impossible, though a fair coin gives 3 heads with probability $1/8$. MLE trusts the data completely and cannot express prior knowledge. **MAP fixes this.**

## MAP: the core idea

Bayes' rule:

$$\underbrace{p(\theta\mid D)}_{\text{posterior}}=\frac{\overbrace{p(D\mid\theta)}^{\text{likelihood}}\;\overbrace{p(\theta)}^{\text{prior}}}{p(D)},$$

where $p(D)$ does not depend on $\theta$. Then

$$\hat\theta_{\text{MAP}}=\arg\max_\theta p(\theta\mid D)=\arg\max_\theta\big[\log p(D\mid\theta)+\log p(\theta)\big].$$

So **MAP = MLE objective + log-prior**.

- Flat prior $\Rightarrow$ $\log p(\theta)$ is constant $\Rightarrow$ MAP $=$ MLE.
- **Framing:** MLE (frequentist): $\theta$ is a fixed unknown constant, the data is random. MAP (Bayesian): $\theta$ is a random variable with a distribution (prior $\to$ posterior), the data is observed.
- MAP is only "half Bayesian": it uses a prior but reports a single point (the posterior peak) instead of the full distribution.

## MAP for the coin with a Beta prior

Prior: $p(\theta)\propto\theta^{\alpha-1}(1-\theta)^{\beta-1}$, with hyperparameters $\alpha,\beta>0$. ($\alpha=\beta=1$ is flat; $\alpha=\beta=2$ is a mild belief that the coin is roughly fair.)

Log-posterior (constants dropped):

$$J(\theta)=(k+\alpha-1)\log\theta+(n-k+\beta-1)\log(1-\theta).$$

Let $A=k+\alpha-1$, $B=n-k+\beta-1$, so $J=A\log\theta+B\log(1-\theta)$.

$$\frac{dJ}{d\theta}=\frac A\theta-\frac B{1-\theta}=0
\;\Rightarrow\;A(1-\theta)=B\theta
\;\Rightarrow\;\theta=\frac{A}{A+B},$$

and $A+B=n+\alpha+\beta-2$. Hence

$$\boxed{\hat\theta_{\text{MAP}}=\frac{k+\alpha-1}{n+\alpha+\beta-2}}$$

Second derivative $-\frac{A}{\theta^2}-\frac{B}{(1-\theta)^2}<0$ when $A,B>0$, so it is a maximum.

- **Check:** $\alpha=\beta=1$ gives $k/n$ (MLE).
- **Example:** $k=n=3$, $\alpha=\beta=2$: $\hat\theta_{\text{MAP}}=\frac{3+2-1}{3+2+2-2}=\frac45=0.8$, versus $\hat\theta_{\text{MLE}}=1$.
- **Pseudo-counts:** the prior acts like $(\alpha-1)$ imaginary heads and $(\beta-1)$ imaginary tails added before the real data. With $\alpha=\beta=2$: $(3+1)/(3+2)=4/5$.
- **Washing out:** as $n\to\infty$, $k$ and $n$ dominate $\alpha,\beta$, so $\hat\theta_{\text{MAP}}\to k/n=\hat\theta_{\text{MLE}}$.

## Still to cover

1. **Regularization link:** Gaussian prior on weights $\to$ L2 (ridge); Laplace prior $\to$ L1 (lasso), derived like MSE/MAE from MLE.
2. **MAP vs MLE vs full Bayesian:** when MAP helps (small data, overfitting, high dimension); limits (point estimate; not invariant under reparametrization, unlike MLE).
3. **Rapid-fire interview questions** on MLE and MAP together.
4. Open question: with $\alpha=\beta=2$ and 30 heads in 30 flips, what is $\hat\theta_{\text{MAP}}$? (Use the boxed formula; compare with the 3-flip case.)
