# What drift is

A model is trained on historical data with joint distribution $P_{\text{train}}(X,Y)$ and then applied to new data with joint distribution $P_{\text{serve}}(X,Y)$. **Drift is the gap between the two growing over time**: 

$$P_{\text{train}}(X,Y)\neq P_{\text{serve}}(X,Y).$$

The result is *silent degradation*: the model keeps producing scores and no error is raised, but the scores become less reliable.

Two related ideas are often both called “drift”:

- **Data drift:** the inputs $X$ change.

- **Concept drift:** the meaning of the inputs changes, i.e. the relationship between $X$ and $Y$ changes.

**In one sentence**

Drift is when production data stops matching training data, so performance decays without any error being raised.

------------------------------------------------------------------------

# The three types of drift

The joint distribution can be factorised in two ways: 

$$P(X,Y)=P(Y\mid X)\,P(X)=P(X\mid Y)\,P(Y).$$

 Each type of drift corresponds to one factor changing while the others (ideally) stay fixed.

| **Type** | **What changes** | **Fraud example** | **Main effect** |
|:---|:---|:---|:---|
| Covariate shift | $P(X)$ (the inputs) | Festival-season volume, a new payment channel, a new user segment | Model faces unfamiliar inputs and extrapolates badly |
| Prior / label shift | $P(Y)$ (the fraud rate) | An attack wave raises prevalence from $0.1\%$ to $0.5\%$ | Probabilities are miscalibrated and the threshold is no longer optimal |
| Concept drift | $P(Y\mid X)$ (the relationship) | Fraudsters change tactics, so a pattern that used to mean fraud now looks normal | The model’s learned logic is wrong; the most damaging type |

**Covariate shift.** $P(X)$ changes but $P(Y\mid X)$ is unchanged. The model’s rule is still correct, but it is being applied in regions of input space where it saw little training data.

**Prior (label) shift.** $P(Y)$ changes but $P(X\mid Y)$ is unchanged. Even with a perfect, unchanged classifier, precision changes. With fixed true positive rate (TPR) and false positive rate (FPR), and prevalence $\pi=P(Y=1)$, 

$$\text{Precision}=\frac{\text{TPR}\cdot\pi}{\text{TPR}\cdot\pi+\text{FPR}\cdot(1-\pi)}.$$

 *Example:* with $\text{TPR}=0.8$ and $\text{FPR}=0.001$, 

$$\begin{aligned}
\pi=0.001:&\quad \text{Precision}=\frac{0.0008}{0.0008+0.000999}\approx 0.44,\\[2pt]
\pi=0.005:&\quad \text{Precision}=\frac{0.004}{0.004+0.000995}\approx 0.80.
\end{aligned}$$

 The same classifier looks twice as good purely because the fraud rate changed. This is also why precision-based metrics such as AUCPR depend on prevalence.

**Concept drift.** $P(Y\mid X)$ changes. The same input now has a different probability of being fraud, so the model’s learned decision boundary is simply wrong. Because input distributions can look unchanged, this type cannot be seen from the inputs alone and requires labels.

**In one sentence**

Covariate shift is inputs changing, prior shift is the base rate changing, and concept drift is the input-to-label relationship changing; fraud mostly suffers concept drift.

------------------------------------------------------------------------

# How drift unfolds over time

- **Sudden:** an abrupt change, such as a new attack or a pipeline or schema change.

- **Gradual:** the old pattern slowly gives way to a new one.

- **Incremental:** a series of small steps that add up.

- **Recurring / seasonal:** patterns that return, such as festivals, month-end and salary cycles.

**Why it matters.** Sudden drift needs fast alerts and rollback, gradual drift needs trend monitoring, and seasonal drift needs seasonality-aware baselines so that we do not retrain in a panic every year.

------------------------------------------------------------------------

# Why fraud is special

1.  **Adversarial adaptation.** Fraudsters probe and adapt to avoid blocks, so the drift is caused by an opponent.

2.  **Feedback loop and selection bias.** Blocked fraud disappears from our data, so future training data under-represents the fraud we already catch.

3.  **Delayed labels.** Chargebacks and investigations take weeks, so recent data looks cleaner than it really is.

4.  **Non-malicious change.** App releases, logging changes, upstream bugs and new products shift features without any change in fraud.

5.  **Asymmetric cost.** Missed fraud and false alarms both cost money, and drift can hurt each differently.

**In one sentence**

In fraud, drift is expected, not exceptional, because the adversary adapts and our own blocking changes the data we see.

------------------------------------------------------------------------

# Detecting drift

## The core idea

Every drift check does the same thing. We take two samples of data:

- the **reference sample**: data from the baseline period (usually the training set, or a recent stable month), containing $n_{\text{ref}}$ rows;

- the **current sample**: data from the window we are monitoring (e.g. the last day or week), containing $n_{\text{cur}}$ rows;

and we ask *how different are they?* This question has two distinct parts, and different tools answer different parts.

**Part 1: how big is the difference? (effect size).** PSI, KL divergence, JS divergence and the KS statistic $D$ each condense the gap between the two samples into one number.

**Part 2: could the difference be just luck? (hypothesis test).** Two samples drawn from exactly the same distribution never look identical, because proportions and averages wobble from sample to sample. A hypothesis test starts from 

$$H_0:\ \text{both samples come from the same distribution (no drift)},$$

 and computes the **p-value**: the probability, *if $H_0$ were true*, of seeing a gap at least as large as the one observed. A small p-value means luck alone is an unlikely explanation. The KS test and the chi-square test are of this type.

Both parts are needed. With millions of rows, a test will flag gaps that are real but too small to matter; with a few hundred rows, a large and important gap may fail to reach significance. So we read the *size* of the difference and the *evidence* that it is real together.

Detection is organised in three layers, depending on what we can observe:

| **Layer** | **What is compared** | **Typical tools** | **Needs labels?** |
|:---|:---|:---|:---|
| Input | Distribution of each feature (and combinations of features) | PSI, KS, $\chi^2$, KL, JS, adversarial validation | No |
| Output | Distribution of the model’s scores and the alert rate | PSI, KS on the score | No |
| Performance | Precision, recall, PR-AUC | Matured cohorts, proxies, audit sample | Yes |

## Input layer (needs no labels)

### Setup and notation

Pick one feature, for example the transaction amount. To compare two samples of a continuous feature, we first cut its range into $B$ bins using edges $b_0<b_1<\dots<b_B$.

- The edges are computed **from the reference sample only** (e.g. its deciles, so each reference bin holds $10\%$ of the rows) and then **reused unchanged** for the current sample. If the edges were recomputed on the current data, the bins would silently move with the data and the comparison would be meaningless.

- For a categorical feature, the bins are simply the categories. Missing values get their own bin.

Then, for each bin $i=1,\dots,B$: 

$$e_i=\frac{\text{number of reference rows in bin } i}{n_{\text{ref}}}
\quad\text{(\emph{expected} share: training-time data)},$$

 

$$a_i=\frac{\text{number of current rows in bin } i}{n_{\text{cur}}}
\quad\text{(\emph{actual} share: data now)}.$$

 Both are proportions, so $\sum_i e_i=1$ and $\sum_i a_i=1$. If there is no drift, $a_i\approx e_i$ for every bin. With decile bins, $e_i=0.1$ for all $i$, and the $a_i$ simply tell us how the current rows are spread across the training deciles.

These two vectors, $e=(e_1,\dots,e_B)$ and $a=(a_1,\dots,a_B)$, are the inputs to everything below.

### Population Stability Index (PSI)

**Definition.** 

$$\boxed{
\mathrm{PSI}=\sum_{i=1}^{B}(a_i-e_i)\,\ln\frac{a_i}{e_i}
}$$

**What each piece means.** For every bin we multiply two quantities:

- $a_i-e_i$: the *absolute shift*, i.e. by how many percentage points the share of this bin moved.

- $\ln(a_i/e_i)$: the *relative shift on a log scale*. It is $0$ if the share did not change, positive if the bin grew, negative if it shrank, and it treats doubling ($\ln2\approx0.69$) and halving ($-\ln2$) symmetrically.

**Why multiply them?** The absolute shift alone ignores context: moving from $0.01$ to $0.02$ is a doubling, whereas moving from $0.40$ to $0.41$ is barely a change, yet both are a shift of $0.01$. The log-ratio alone would over-react to bins containing almost no data. The product weighs both: 

$$\begin{aligned}
\text{rare bin: } e=0.01,\ a=0.02:&\quad 0.01\cdot\ln 2\approx 0.00693,\\
\text{common bin: } e=0.40,\ a=0.41:&\quad 0.01\cdot\ln 1.025\approx 0.00025.
\end{aligned}$$

 The same absolute shift counts about $28$ times more in the rare bin. For fraud this is desirable, since risky behaviour usually lives in sparsely populated bins.

**Each term is non-negative.** If $a_i>e_i$, both factors are positive; if $a_i<e_i$, both are negative, and their product is again positive. So shifts in different bins add up and cannot cancel each other. Consequently $\mathrm{PSI}\ge 0$, with $\mathrm{PSI}=0$ exactly when $a=e$. Swapping $a$ and $e$ leaves the value unchanged, so PSI is symmetric.

**Worked example.** Reference shares $e=(0.5,0.3,0.2)$; current shares $a=(0.4,0.3,0.3)$.


| Bin $i$ | $e_i$ | $a_i$ | $\ln(a_i/e_i)$ | $(a_i-e_i)\ln(a_i/e_i)$ |
|:--:|:--:|:--:|:--:|:--:|
| 1 | 0.5 | 0.4 | −0.2231 | $(-0.1)(-0.2231)=0.0223$ |
| 2 | 0.3 | 0.3 | 0 | 0 |
| 3 | 0.2 | 0.3 | 0.4055 | $(0.1)(0.4055)=0.0406$ |
| **PSI** | | | | **0.063** |

A larger shift, $a=(0.2,0.3,0.5)$, gives $(-0.3)\ln0.4+0+(0.3)\ln2.5\approx0.275+0.275=0.550$.

**How to read the value.** The common rule of thumb is: 

$$\begin{aligned}
\mathrm{PSI}<0.1&:\ \text{stable},\\
0.1\le\mathrm{PSI}\le0.25&:\ \text{moderate shift, investigate},\\
\mathrm{PSI}>0.25&:\ \text{significant shift}.
\end{aligned}$$

 By this rule the first example ($0.063$) is stable and the second ($0.550$) is a significant shift. These thresholds are conventions that originated in credit scoring; they are *not* a hypothesis test and carry no p-value.

**Noise floor.** Even with no drift at all, sampling noise gives PSI a positive value. For small differences, $\ln(a_i/e_i)\approx(a_i-e_i)/e_i$, so $\mathrm{PSI}\approx\sum_i(a_i-e_i)^2/e_i$, and one can show that under no drift 

$$\mathbb{E}[\mathrm{PSI}]\approx(B-1)\left(\frac{1}{n_{\text{ref}}}+\frac{1}{n_{\text{cur}}}\right).$$

 For example, with $B=10$ and $n_{\text{ref}}=n_{\text{cur}}=1000$, the noise floor is $9\times0.002=0.018$. PSI computed on small windows or with many bins is therefore noisy, and a value near this floor means nothing.

**Practical caveat.** If some bin has $e_i=0$ or $a_i=0$, the logarithm is undefined. Fix this by merging sparse bins or replacing zeros with a tiny constant (e.g. $10^{-4}$). A bin that is empty in the reference but populated now (a brand-new category) is itself an important drift signal.

### KL divergence

PSI works, but where does it come from? It is built from the **Kullback–Leibler (KL) divergence**, which measures how badly one distribution describes data that actually come from another.

**Definition.** For two distributions $P$ and $Q$ over the same bins (or categories), 

$$\boxed{
D_{\mathrm{KL}}(P\,\|\,Q)=\sum_{i}P_i\ln\frac{P_i}{Q_i}
}$$

 where $P_i$ and $Q_i$ are the probabilities of bin $i$ under $P$ and $Q$. The result is in *nats* (natural logarithm). For drift monitoring, we take $P=a$ (current) and $Q=e$ (reference).

**Intuition: accumulated evidence.** Suppose one observation falls in bin $i$. The quantity $\ln(P_i/Q_i)$ is the log-likelihood ratio: how much more strongly this observation supports “the data follow $P$” than “the data follow $Q$”. If the data *really* follow $P$, the bins occur with frequencies $P_i$, so the average evidence per observation is $\sum_iP_i\ln(P_i/Q_i)$, which is exactly the KL divergence. Hence $D_{\mathrm{KL}}(P\|Q)$ is the average amount of evidence, per observation, with which we could tell the current data apart from the reference. After $n$ observations we have accumulated about $n\,D_{\mathrm{KL}}$ nats of evidence, a fact that reappears in the chi-square test below.

**Properties.**

- **Non-negative, zero only if identical.** Using $\ln x\le x-1$, 

$$-D_{\mathrm{KL}}(P\|Q)=\sum_iP_i\ln\frac{Q_i}{P_i}\le\sum_iP_i\Big(\frac{Q_i}{P_i}-1\Big)=\sum_iQ_i-\sum_iP_i=0,$$

 so $D_{\mathrm{KL}}\ge0$, with equality iff $P=Q$.

- **Asymmetric.** $D_{\mathrm{KL}}(P\|Q)\neq D_{\mathrm{KL}}(Q\|P)$ in general, so it is not a distance. $D_{\mathrm{KL}}(a\|e)$ weights bins by how common they are in the *current* data.

- **Can be infinite.** If $Q_i=0$ while $P_i>0$ (e.g. a new device type that never appeared in the reference), the term $\ln(P_i/0)$ is infinite. The reverse direction blows up if a reference category vanishes.

**Link to PSI.** Adding the two directions, 

$$D_{\mathrm{KL}}(a\|e)+D_{\mathrm{KL}}(e\|a)=\sum_ia_i\ln\frac{a_i}{e_i}+\sum_ie_i\ln\frac{e_i}{a_i}=\sum_i(a_i-e_i)\ln\frac{a_i}{e_i}=\mathrm{PSI}.$$

 So **PSI is the symmetrised KL divergence**, which explains why it is symmetric and non-negative.

**Check on the example** ($a=(0.4,0.3,0.3)$, $e=(0.5,0.3,0.2)$): 

$$D_{\mathrm{KL}}(a\|e)=0.4\ln0.8+0.3\ln1.5\approx-0.0893+0.1216=0.0324,$$

 

$$D_{\mathrm{KL}}(e\|a)=0.5\ln1.25+0.2\ln\tfrac{2}{3}\approx0.1116-0.0811=0.0305,$$

 and the sum $0.0629$ matches the PSI computed above.

### Jensen–Shannon (JS) divergence

KL has two awkward features: it is asymmetric and it can be infinite. JS divergence removes both.

**Definition.** Let $M$ be the average of the two distributions, $M_i=\tfrac12(P_i+Q_i)$. Then 

$$\boxed{
\mathrm{JS}(P,Q)=\tfrac12D_{\mathrm{KL}}(P\,\|\,M)+\tfrac12D_{\mathrm{KL}}(Q\,\|\,M)
}$$

**Intuition.** Instead of comparing $P$ directly with $Q$, compare each of them with their midpoint $M$. Whenever $P_i>0$ or $Q_i>0$, the midpoint satisfies $M_i>0$, so no logarithm ever has a zero in the denominator. A category that exists only in the current data is no longer “infinitely surprising”; it simply contributes a large but finite amount.

**Properties.**

- **Symmetric:** $\mathrm{JS}(P,Q)=\mathrm{JS}(Q,P)$.

- **Always finite and bounded:** $0\le\mathrm{JS}\le\ln2\approx0.693$ nats (equivalently $0$ to $1$ bit if $\log_2$ is used). The maximum occurs when $P$ and $Q$ have no overlap at all. Having a fixed scale makes the number easy to interpret: $0$ means identical, $\ln 2$ means completely disjoint.

- $\sqrt{\mathrm{JS}}$ is a true distance metric.

**Worked example** ($P=a=(0.4,0.3,0.3)$, $Q=e=(0.5,0.3,0.2)$). The midpoint is $M=(0.45,0.30,0.25)$: 

$$D_{\mathrm{KL}}(P\|M)=0.4\ln\tfrac{0.4}{0.45}+0.3\ln\tfrac{0.3}{0.25}\approx-0.0471+0.0547=0.0076,$$

 

$$D_{\mathrm{KL}}(Q\|M)=0.5\ln\tfrac{0.5}{0.45}+0.2\ln\tfrac{0.2}{0.25}\approx0.0527-0.0446=0.0080,$$

 

$$\mathrm{JS}=\tfrac12(0.0076+0.0080)\approx0.0078,$$

 which on a scale whose maximum is $0.693$ is a very small difference.

**When to prefer which.** Use PSI when you want the familiar rule-of-thumb thresholds that risk teams already know. Use JS when bins may be empty or categories can appear and disappear, or when you want a bounded score comparable across features.

### Kolmogorov–Smirnov (KS) test (continuous features)

**Purpose.** PSI, KL and JS need binning, and the answer can depend on how the bins were chosen. The KS test compares two samples of a continuous feature directly, with no bins, and gives a p-value.

**Definition.** For a sample, the **empirical CDF** is 

$$F(x)=\frac{\text{number of rows with value}\le x}{\text{number of rows}},$$

 the fraction of rows at or below $x$. Let $F_{\text{ref}}$ and $F_{\text{cur}}$ be the two empirical CDFs. The KS statistic is 

$$\boxed{
D=\sup_x\big|F_{\text{ref}}(x)-F_{\text{cur}}(x)\big|
}$$

 the largest vertical gap between the two curves.

**Intuition.** If both samples come from the same distribution, their CDFs lie almost on top of each other. $D$ takes values in $[0,1]$ and has a concrete reading: $D=0.10$ means that at some value $x^\ast$, the share of transactions below $x^\ast$ differs by 10 percentage points between the two samples. It detects shifts in location, scale and shape, and is most sensitive near the middle of the distribution rather than the extreme tails.

**Test.** Under $H_0$ (same distribution), $D$ is of the order of $1/\sqrt{n}$ and shrinks as the samples grow. At the $5\%$ significance level we reject $H_0$ when 

$$D>1.358\sqrt{\frac{n_{\text{ref}}+n_{\text{cur}}}{n_{\text{ref}}\,n_{\text{cur}}}}.$$

**Example of statistical versus practical significance.**

- $n_{\text{ref}}=n_{\text{cur}}=1{,}000$: the threshold is $1.358\sqrt{0.002}\approx0.061$, so a gap of about 6 percentage points is needed.

- $n_{\text{ref}}=n_{\text{cur}}=1{,}000{,}000$: the threshold is $1.358\sqrt{2\times10^{-6}}\approx0.0019$, so a gap of just $0.2$ percentage points is “significant”.

This is why, for large samples, $D$ (the effect size) should be read together with the p-value. Also note that KS assumes continuous data: with many tied values (e.g. amounts rounded to whole rupees), its p-values become conservative.

### Chi-square test (categorical features)

**Purpose.** For a categorical feature (payment channel, device type, merchant category), or a binned continuous feature, we want to know whether the *counts* per category in the current sample are consistent with the reference proportions, or whether the gap is bigger than sampling luck explains. The chi-square ($\chi^2$) test answers this.

**Setup.** There are $K$ categories. Under $H_0$ (no drift), each current row falls into category $k$ with the reference probability $e_k$. Let

- $O_k$: the *observed* count in category $k$ in the current sample;

- $E_k=n_{\text{cur}}\,e_k$: the *expected* count if there were no drift.

**Statistic.** 

$$\boxed{
\chi^2=\sum_{k=1}^{K}\frac{(O_k-E_k)^2}{E_k}
}$$

**Why this form?**

- $O_k-E_k$ is the gap between what we saw and what we expected.

- We *square* it so that over-counts and under-counts both add to the total rather than cancelling.

- We *divide by $E_k$* because the natural noise in a count is about $\sqrt{E_k}$ (counts behave roughly like a Poisson variable, whose variance equals its mean). A gap of 10 on an expected count of 20 is huge, while a gap of 10 on an expected count of 10,000 is negligible. The ratio $z_k=(O_k-E_k)/\sqrt{E_k}$ measures the gap in units of its own noise, so each $z_k$ is roughly a standard normal variable under $H_0$.

Thus $\chi^2=\sum_kz_k^2$ is a sum of squared (approximately) standard normal variables. Because the counts must add up to $n_{\text{cur}}$, one of the $K$ terms is determined by the others, so under $H_0$ 

$$\chi^2\sim\chi^2_{K-1}\qquad(K-1\text{ degrees of freedom}),$$

 a distribution whose average value is $K-1$.

**How to read it.** If there is no drift, $\chi^2$ should be close to $K-1$. A value far above that suggests drift. The p-value is $P(\chi^2_{K-1}\ge\chi^2_{\text{obs}})$. For $K=3$ (2 degrees of freedom) the $5\%$ critical value is $5.99$.

**Worked example.** Reference shares $e=(0.5,0.3,0.2)$; current sample of $n_{\text{cur}}=1000$ with observed counts $O=(400,300,300)$. Expected counts: $E=(500,300,200)$. 

$$\chi^2=\frac{(400-500)^2}{500}+\frac{(300-300)^2}{300}+\frac{(300-200)^2}{200}=20+0+50=70\gg5.99,$$

 so we reject $H_0$: drift is almost certain. The same proportions with $n_{\text{cur}}=100$ ($O=(40,30,30)$, $E=(50,30,20)$) give $\chi^2=2+0+5=7$, which only just exceeds $5.99$.

**Key caveats.**

- **Size grows with sample size.** For fixed proportions, $\chi^2=n_{\text{cur}}\sum_k(a_k-e_k)^2/e_k$ grows linearly with $n_{\text{cur}}$. The same tiny shift becomes “significant” with enough data (the example above: $0.07\times1000=70$). Report an effect size (PSI, or $\sum_k(a_k-e_k)^2/e_k$) next to the p-value.

- **Needs reasonable counts.** The normal approximation requires $E_k\gtrsim5$; rare categories should be merged.

- **Connection to KL.** For small shifts, $\chi^2\approx2\,n_{\text{cur}}\,D_{\mathrm{KL}}(a\|e)$. In the example above, $2\times1000\times0.0324\approx65$, close to $70$. This is the “accumulated evidence $\approx n\,D_{\mathrm{KL}}$” idea from the KL section, now turned into a formal test.

### Adversarial validation

**Purpose.** The tools above look at one feature at a time. Adversarial validation looks at all features together and answers: *can a model tell the current data apart from the reference data?*

**Procedure.**

1.  Label every reference row $s=0$ and every current row $s=1$, and stack them into one dataset.

2.  Train a classifier (e.g. gradient-boosted trees) to predict $s$ from the features $X$.

3.  Evaluate it with **cross-validated** (held-out) AUC. Without held-out evaluation, a flexible model can memorise rows and look falsely good.

**Intuition.** If there is no drift, the labels $s$ are essentially coin flips as far as $X$ is concerned, so no classifier can beat chance and AUC $\approx0.5$. If the distributions differ, the classifier can exploit the differences, and the AUC rises towards $1$. The AUC is the probability that a randomly chosen current row receives a higher “looks-current” score than a randomly chosen reference row, so it is a direct measure of how separable the two samples are. As a rough guide, AUC below about $0.55$ is benign, and values around $0.7$ or above indicate substantial drift.

**What it gives.**

- **Where:** the classifier’s feature importances (e.g. permutation importance or SHAP) show which features drive the separation.

- **Multivariate sensitivity:** it detects changes in the *relationships* among features, which univariate tests miss.

- **A by-product:** its predicted probability yields the density ratio used for importance weighting in Section 7.

**Caution.** Remove timestamps, row IDs and other fields that trivially identify the period, otherwise the classifier separates the samples for a meaningless reason.

### Multivariate drift

Checking each feature separately can miss drift entirely. *Example:* transaction amount and hour of day each have the same marginal distribution as before (so PSI and KS on each feature are quiet), but large amounts used to occur mostly in the daytime and now occur mostly at night. Only the *joint* distribution changed, and for fraud this is exactly the kind of change that matters.

Ways to catch it: adversarial validation (above); comparing correlation matrices between the two periods; or reducing the data to a few dimensions (principal components, or the model’s own internal embedding) and applying the same distance and test tools there.

### Many features, many tests

A model with hundreds of features, checked daily, will produce false alarms by chance: at a $5\%$ significance level, about 1 in 20 features flags even when nothing has changed. Rely on effect-size thresholds (PSI, $D$) and rank features by the *magnitude* of the shift rather than counting raw p-values below $0.05$.

## Output layer (needs no labels)

**What is compared.** Let $s(x)\in[0,1]$ be the model’s score for a transaction $x$. The score is a one-number summary of all the features *as the model uses them*, so monitoring its distribution is a compact, label-free drift detector aligned with what the model actually does. We compare the reference and current score distributions with the same tools as above (PSI and KS on the score).

**Alert rate.** For a decision threshold $\tau$, the alert (or block) rate is 

$$r(\tau)=P\big(s(X)\ge\tau\big).$$

 It also matters operationally, since it determines review-queue workload. It also has a useful structure. If the classifier’s TPR and FPR at $\tau$ are unchanged and only the fraud prevalence $\pi$ moves, 

$$r=\text{TPR}\cdot\pi+\text{FPR}\cdot(1-\pi).$$

 With $\text{TPR}=0.8$ and $\text{FPR}=0.001$, moving $\pi$ from $0.1\%$ to $0.5\%$ takes the alert rate from $0.0008+0.000999\approx0.18\%$ to $0.004+0.000995\approx0.50\%$, nearly a threefold jump from prior shift alone.

**How to read it.**

- Alert rate rises *and* features also drifted: likely covariate shift.

- Alert rate rises with stable features: likely a rise in prevalence, or a change in the fraud pattern.

- Alert rate *stable* does not prove the model is fine: under concept drift the model may keep flagging the same number of cases but the *wrong* ones.

## Performance layer (needs labels)

**Metrics.** At threshold $\tau$, 

$$\text{Precision}=\frac{TP}{TP+FP},\qquad\text{Recall}=\frac{TP}{TP+FN},$$

 where $TP$, $FP$, $FN$ are the counts of true positives, false positives and false negatives; PR-AUC is the area under the precision–recall curve.

**The problem: labels arrive late.** Chargebacks and investigations take weeks, so the most recent transactions have unreliable labels. We therefore use:

- **Matured cohorts:** evaluate on data old enough that its labels have settled (e.g. transactions from 60 or more days ago). This is trustworthy but always looks backwards.

- **Proxy metrics** for the recent past: refund and dispute rates, customer complaints, review-queue precision (the share of flagged cases that human reviewers confirm).

- **A random audit sample:** draw transactions at random, have them labelled by humans, and estimate precision and recall from them. Because it is random, it is unbiased, unlike the blocked-and-reviewed data, which is selected by the model itself. Since fraud is rare, one usually samples more heavily from high-score strata and weights each sampled case by the inverse of its sampling probability. The uncertainty of an estimated precision $\hat p$ from $n$ audited flagged cases is about $\hat p\pm1.96\sqrt{\hat p(1-\hat p)/n}$.

**Interpreting a change in performance.** Precision and PR-AUC depend on the prevalence $\pi$ (see Section 2), so a change in them does not by itself prove the classifier got worse. A rank-based metric that does not depend on $\pi$, such as ROC-AUC or recall at a fixed false positive rate, helps separate the causes:

| **Observation** | **What it points to** |
|:---|:---|
| Inputs drifted, but ROC-AUC and recall at fixed FPR are unchanged | Covariate shift that has not hurt the model so far |
| Alert rate and PR-AUC changed, but ROC-AUC and recall at fixed FPR are unchanged | Prior shift (prevalence changed) |
| ROC-AUC or recall at fixed FPR dropped | Concept drift (or covariate shift severe enough to hurt) |
| Inputs, scores and rank metrics all stable, but precision from the audit dropped | Check label definition and label lag before blaming the model |

**Caveat.** A statistically significant drift is not necessarily a performance drop. Only labels (or good proxies) tell us whether it matters.

## Summary of the tools

| **Tool** | **Data type** | **What it tells us** | **Output** |
|:---|:---|:---|:---|
| PSI | Binned or categorical | Size of the shift; symmetrised KL; rule-of-thumb thresholds | A number $\ge0$ |
| KL divergence | Binned or categorical | Average evidence per row that current differs from reference; asymmetric | A number $\ge0$ (can be $\infty$) |
| JS divergence | Binned or categorical | Bounded, symmetric, always-finite version of KL | A number in $[0,\ln2]$ |
| KS test | Continuous | Largest gap between the two CDFs; no binning | $D\in[0,1]$ and p-value |
| Chi-square test | Categorical or binned | Whether the count gaps exceed what luck explains | $\chi^2$ and p-value |
| Adversarial validation | All features jointly | How separable the two samples are, and which features separate them | AUC and importances |

**In one sentence**

I monitor inputs, outputs and performance: input and score drift give early warning without labels, effect-size measures (PSI, KL, JS, $D$) say how big the shift is, tests (KS, $\chi^2$) say whether it is more than luck, and audited matured cohorts confirm whether the model really degraded.

------------------------------------------------------------------------

# Diagnosing whether it is real

Before retraining, find the cause:

- **Pipeline or schema bug?** Check for null spikes, unit changes, or a feature that became constant.

- **Seasonality?** Compare with the same period last year.

- **Label lag?** Recent precision may look wrong because labels have not settled.

- **Segment-specific?** Slice by channel, merchant, geography and device.

- **Real adversarial change?** Look for new clusters or behaviour patterns.

Retraining on a data bug simply bakes the bug into the model.

------------------------------------------------------------------------

# Responding to drift

**Short term.** Recalibrate or move the threshold (the usual fix for prior shift), add or tighten rules as a stopgap, and route more cases to human review.

**Prior shift correction.** If the classifier was trained with prevalence $\pi_{\text{train}}$ and is now deployed where the prevalence is $\pi_{\text{new}}$, the posterior odds are rescaled by the ratio of prior odds: 

$$\frac{p_{\text{new}}(y=1\mid x)}{p_{\text{new}}(y=0\mid x)}
=
\frac{p_{\text{train}}(y=1\mid x)}{p_{\text{train}}(y=0\mid x)}
\cdot
\frac{\pi_{\text{new}}/(1-\pi_{\text{new}})}{\pi_{\text{train}}/(1-\pi_{\text{train}})}.$$

 For $\pi$ moving from $0.1\%$ to $0.5\%$, the odds multiplier is 

$$\frac{0.005/0.995}{0.001/0.999}\approx 5.0.$$

**Covariate shift: importance weighting.** Reweight training examples by the density ratio 

$$w(x)=\frac{p_{\text{serve}}(x)}{p_{\text{train}}(x)}.$$

 This ratio can be estimated with the adversarial classifier from Section 5. If $\hat p(s=1\mid x)$ is its predicted probability that $x$ comes from the serving data, then 

$$w(x)\approx\frac{\hat p(s=1\mid x)}{\hat p(s=0\mid x)}\cdot\frac{n_{\text{train}}}{n_{\text{serve}}}.$$

 The alternative is to retrain on data that covers the new region of input space.

**Retraining.** On a schedule plus triggers (drift alarm, performance drop). Choose the window carefully: recent data tracks new patterns but is noisy, whereas older data is stable but stale. Weighting recent samples is a common compromise.

**Safe deployment.** Shadow mode, champion/challenger comparison, staged rollout and a rollback plan.

**Online or incremental learning** where the problem allows it, with care for noisy or poisoned updates.

**Fighting the feedback loop.** Keep a small randomised exploration or holdout slice, so that we still observe what we would otherwise have blocked.

**In one sentence**

I diagnose first and then respond proportionally: a threshold or calibration fix for prior shift, retraining for concept drift, with shadow testing and rollback.

------------------------------------------------------------------------

# Designing for drift (prevention)

- Prefer **stable, hard-to-game signals** and diverse feature families, so that no single feature can be spoofed.

- Use **time-based validation and rolling backtests** to estimate how fast a model decays.

- Version features and data, and monitor feature freshness and quality.

- Build dashboards and alerts per feature and per segment.

- Plan the **retraining cadence from measured decay**, not from a guess.

------------------------------------------------------------------------

# Interview Q&A to rehearse

## Q1. Features look stable but precision dropped. What happened?

Most likely concept drift: $P(Y\mid X)$ changed, so the same inputs now mean something different. Other possibilities are prior shift (higher or lower prevalence changes precision even for an unchanged classifier), a threshold issue, label-lag artefacts, or a change in the label definition.

## Q2. How would you detect drift with delayed labels?

Monitor inputs (PSI, KS, adversarial validation) and score distributions, track proxy metrics, run a random audit sample, and evaluate on matured cohorts.

## Q3. How often do you retrain?

Based on measured decay and drift triggers, not a fixed guess, and always validated in shadow mode first.

## Q4. How do fraudsters affect your training data?

Through selection bias: blocked fraud disappears from the data. Keep an exploration or holdout slice so that these cases are still observed.
