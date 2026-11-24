# Naive Bayes for Fraud in Production: Q&A

!!! note "About the numbers"
    Numbers marked "demo" come from `nb_demo.py` (run and checked). † = from memory, verify.

**Notation.** $x=(x_1,\dots,x_d)$ are the features of one click. $\pi$ is the fraud base rate. $\mathrm{LR}_j(x_j)=P(x_j\mid\text{fraud})\,/\,P(x_j\mid\text{genuine})$.

---

## Q1. In one breath, what is Naive Bayes doing?

It computes the posterior odds of fraud by starting from the prior odds and multiplying in one likelihood ratio per feature:

$$\text{posterior odds}=\text{prior odds}\times \mathrm{LR}_1\times \mathrm{LR}_2\times\cdots\times \mathrm{LR}_d$$

The "naive" part is the assumption that features are **conditionally independent given the class**, which is what allows the product.

In log space it is a sum, which is how it is computed and explained in practice:

$$\boxed{\log\text{ posterior odds}=\log\text{ prior odds}+\sum_j \log \mathrm{LR}_j(x_j)}$$

---

## Q2. I get one ratio per feature. How do I turn many ratios into one decision?

You do not make a statement per ratio. You combine them into one number, then compare it with a threshold.

Steps for one click:

1. Look up each feature's LR (Q3).
2. Take logs and add them: $S=\sum_j \log \mathrm{LR}_j$.
3. Add the log prior odds: $z=\log\frac{\pi}{1-\pi}+S$.
4. Convert: $P(\text{fraud}\mid x)=\dfrac{1}{1+e^{-z}}$.
5. Compare $P$ with the operating threshold (flag, review, block).

**Worked example (toy).** $\pi=1/50{,}000$. Three features with LR $35$, $20$, $10$.

| Term | Value |
|:--|:--|
| log prior odds | $\ln(1/49{,}999)=-10.82$ |
| $\ln 35$ | $+3.555$ |
| $\ln 20$ | $+2.996$ |
| $\ln 10$ | $+2.303$ |
| $z$ = sum | $-1.966$ |
| $P(\text{fraud})=1/(1+e^{1.966})$ | **0.1228, about 12%** |

Same answer as the product form: $7{,}000\times(1/49{,}999)=0.14$ odds, and $0.14/1.14=12.3\%$.

Features with LR $<1$ (negative log) pull the score down. A click can have two scary features and one reassuring one, and the sum balances them.

---

## Q3. How do I compute $\mathrm{LR}_j$ for each feature?

**A table per feature, built on training data only.**

Continuous feature (for example clicks per minute):

1. Make bins. Use quantiles of the **pooled** data (all classes together), so no bin is nearly empty.
2. Count frauds per bin ($c_f$) and genuine per bin ($c_g$).
3. Smooth: $p_f(b)=\dfrac{c_f(b)+\alpha}{N_f+\alpha B}$, and the same for genuine. $\alpha=1$ is Laplace smoothing, $B$ is the number of bins.
4. $\log \mathrm{LR}(b)=\log p_f(b)-\log p_g(b)$.

Categorical feature (device type, country, publisher): the same, with categories as bins. Put rare categories into an "other" bucket. Keep a bucket for "unseen", whose LR is $1$ (log $0$) or its smoothed value.

**Why smoothing.** A bin with 0 frauds would give $\mathrm{LR}=0$, and one such feature would force the score to "never fraud" whatever the other features say. With 0 genuine you would get infinity.

**Alternatives to bins:** a kernel density estimate per class, or a parametric fit (Gaussian, or log-normal for rates) if you trust the shape. Bins are the most robust, and they are directly readable.

**Demo output** (bins from pooled quantiles, $\alpha=1$) for one suspicious click:

| Feature | log LR | LR |
|:--|:-:|:-:|
| clicks/min = 25 | $+1.94$ | 7.0 |
| timing regularity = 0.85 | $+2.05$ | 7.8 |
| device age bucket = new | $+1.50$ | 4.5 |
| **sum** | **$+5.50$** | |

---

## Q4. What logical statement can I make from the ratios? (the explanation)

Each feature's log LR is its **contribution** to the score, in the same units as the log odds. Because the sum is exact, the explanation is exact. The log LR is often called **weight of evidence**.

The statement for the demo click, at production prior $\pi=1/50{,}000$:

> Baseline log odds are $-10.82$ (about 1 in 50,000). Clicks/min adds $+1.94$, timing regularity adds $+2.05$, device age adds $+1.50$. Total log odds $=-10.82+5.50=-5.32$, so $P(\text{fraud})\approx 0.49\%$. That is about 240 times the base rate, but still below 1%.

Two things you can say with it:

- **Which features drove the flag:** rank by contribution.
- **What a number means:** "this click is 240× more likely fraud than a random one" (the combined LR is $e^{5.5}\approx 245$) is a different statement from "this click is probably fraud". The first is evidence; the second also needs the prior. In extreme imbalance a high LR can still mean a low probability, so threshold on the calibrated probability (or expected cost), not on the LR alone.

This is the Shapley/SHAP idea in its simplest form: for Naive Bayes, the per-feature log LRs are already an exact additive attribution, with the log prior odds as the baseline.

---

## Q5. Why use the production prior and not the training prior?

The tables for LR do not depend on the class balance (each is computed within a class), but the prior term does.

Demo, same click, same LRs:

| Prior used | $P(\text{fraud})$ |
|:--|:-:|
| training prior ($400/200{,}400=0.2\%$) | 32.8% |
| production prior $1/50{,}000$ | **0.49%** |

If you train on a rebalanced or undersampled set and forget to swap the prior, probabilities are inflated by about the ratio of prior odds. Fix: use the true production $\pi$ in the prior term. This is the same idea as prior-shift correction for any classifier.

Bonus: the prior is one number you can update weekly from recent confirmed rates, **without refitting any LR table**. That is a real production advantage.

---

## Q6. What is the main way this goes wrong?

**Correlated features double-count evidence**, so the model is over-confident.

Demo: repeat the clicks/min feature as a fourth feature (perfectly correlated with itself). The same click then goes from 0.49% to **3.3%**, with no new information.

Real examples: click rate and click-timing regularity, device age and OS version, IP reputation and ASN reputation.

What to do:

- Check conditional correlations (within the fraud class and within genuine) and drop or merge redundant features.
- Combine a correlated group into one feature (a joint table over two binned features, or a small model that outputs one score) and give Naive Bayes that.
- **Calibrate the output** (Platt or isotonic) on a held-out time slice, because the ranking is often fine even when the probabilities are not.
- If you need the model to learn how much to trust each feature, use logistic regression (Q8).

---

## Q7. Why would anyone use Naive Bayes in production instead of XGBoost?

Reasons that hold up:

- **Exact, cheap explanations** (Q4). No SHAP approximation needed.
- **Fast and tiny:** scoring is $d$ table lookups and additions.
- **Easy to update:** tables are counts, so new labelled data increments them. You can refresh daily, and per segment (per publisher or region).
- **Works with little data per segment** and gives a sensible cold-start baseline.
- **Easy to audit and to override:** an analyst can read a table and change one bin.
- Good as a **first-stage filter** in a cascade, or a monitoring baseline, where interpretability matters more than the last bit of accuracy.

Reasons against, to say honestly:

- The independence assumption (Q6) hurts probabilities and cannot capture interactions (for example "high click rate matters only on mobile").
- Binning loses information from continuous features.
- Usually beaten on ranking quality by boosted trees when there are many interacting features.

A balanced answer: use it as an explainable baseline or stage-1 filter; use boosted trees for the final ranking and explain those with SHAP.

---

## Q8. How is Naive Bayes related to logistic regression?

Naive Bayes with binned features is a **linear model in the log-odds**:

$$\text{log odds}=b+\sum_j w_j(\text{bin}_j),\qquad w_j=\log \mathrm{LR}_j,\quad b=\text{log prior odds}.$$

Logistic regression has the same form (a sum of per-feature terms), but it **learns the weights jointly** by maximising the likelihood, so it can down-weight redundant features. Naive Bayes estimates each term separately, so it cannot.

Useful trick: use the log LR (weight of evidence) of each binned feature as the input to a logistic regression. This is a classic credit-scoring scorecard approach†: the interpretable bins from Naive Bayes, and weights that fix the double counting.

---

## Q9. What if a continuous feature is skewed or has outliers?

- Bins by quantile handle skew with no assumption; the top bin catches outliers.
- Parametric option: Gaussian Naive Bayes assumes $x_j\mid\text{class}\sim N(\mu_c,\sigma_c^2)$. For heavy-tailed rates, fit it on $\log x$ (a log-normal). If the assumption is wrong, the LR can be badly wrong in the tails, which is exactly where fraud lives, so check it against the histogram.
- Do not extrapolate: cap the LR at the extreme bins.

---

## Q10. How do I build and validate it so there is no leakage?

1. Split **by time**, with a maturity gap so labels (chargebacks, confirmed fraud) have arrived. Never random-split.
2. Fit bins and tables on the train window only. Computing quantile edges on all data is mild leakage.
3. Set the prior from production, not from the training set.
4. Evaluate with PR-AUC and precision at the review capacity (top-$k$), not accuracy.
5. Check calibration on the validation slice (reliability curve, Brier score, ECE).
6. Remember that labels are noisy (missed frauds sit in the "genuine" counts), which makes fraud look more like genuine in every table and shrinks the LRs toward 1.

---

## Q11. How do I monitor it?

- **Drift in the tables:** compare each feature's bin distribution now vs training (PSI $=\sum (A-E)\ln(A/E)$; rule of thumb 0.1 and 0.25†). PSI detects covariate shift only, not a change in $P(\text{fraud}\mid x)$.
- **Drift in LRs:** refit the tables on the latest matured window and compare log LR per bin. Large moves show adversaries adapting.
- **Prior:** track the confirmed fraud rate.
- **Calibration:** predicted vs observed rate by score decile on matured labels.
- Alert when a feature's contribution distribution shifts (for example a feature stuck at its top bin).

---

## Q12. Questions an interviewer might ask, with short answers

??? question "Write Naive Bayes for fraud."
    $$\log\text{odds}(\text{fraud}\mid x)=\log\frac{\pi}{1-\pi}+\sum_j\log\frac{P(x_j\mid\text{fraud})}{P(x_j\mid\text{genuine})}.$$

??? question "Why is it \"naive\"?"
    It assumes features are independent given the class, so the joint likelihood factorises into a product.

??? question "Why work in log space?"
    Products of many small numbers underflow, sums are stable, and the log LR contributions are additive and readable.

??? question "A feature has 0 fraud counts in a bin. What happens, and what do you do?"
    $\mathrm{LR}=0$ for that bin, which vetoes fraud on that feature alone. Use additive smoothing ($\alpha>0$) or merge bins.

??? question "The model says 30% for a click that is fraud 0.5% of the time in production. Why?"
    Probably the prior from a rebalanced training set was used, or correlated features double-counted. Fix the prior, check feature correlations, and calibrate.

??? question "Does Naive Bayes need a calibrated threshold?"
    Yes. The ranking may be good while the probabilities are over-confident, so calibrate on a time-held-out slice before thresholding by cost.

??? question "How would you explain one flagged click?"
    List the baseline log odds and each feature's log LR, sorted, then the total and the resulting probability.

??? question "Naive Bayes vs XGBoost?"
    See Q7. Naive Bayes is exactly explainable, cheap and incremental but assumes independence; boosted trees capture interactions and rank better but need SHAP for explanations.

---

## Q13. Practice (answer aloud, then check)

1. With $\pi=1/50{,}000$, three LRs of 35, 20 and 10: compute $P(\text{fraud})$.
2. The same click, but a fourth feature with LR $0.1$ is added. New $P$?
3. Why does a duplicated feature raise the score?
4. Why does the training prior give a different answer from the production prior, when the LR tables are the same?
5. Explain a flag using only log LRs.
6. When would you replace Naive Bayes with logistic regression on weight-of-evidence features?

??? success "Answers to 1 and 2"
    1. About 12% (see Q2).
    2. Add $\ln 0.1=-2.303$: $z=-4.269$, so $P\approx 1.4\%$.

---

## Code (run and checked)

`nb_demo.py` is not part of this repo yet. The core is this:

```python
def fit_lr_table(col, y, nb=8, alpha=1.0, cat=False):
    if cat:
        edges = None; b = col.astype(int); B = int(col.max()) + 1
    else:
        edges = np.quantile(col, np.linspace(0, 1, nb + 1)[1:-1])   # pooled quantiles
        b = np.digitize(col, edges); B = nb
    cf = np.bincount(b[y == 1], minlength=B) + alpha                  # smoothed fraud counts
    cg = np.bincount(b[y == 0], minlength=B) + alpha                  # smoothed genuine counts
    return edges, np.log((cf / cf.sum()) / (cg / cg.sum()))           # log LR per bin

# score one click
z = np.log(pi / (1 - pi)) + sum(log_lr_of_each_feature)               # log prior odds + sum of log LRs
p = 1 / (1 + np.exp(-z))
```
