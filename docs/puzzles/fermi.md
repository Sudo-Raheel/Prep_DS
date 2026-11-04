# Puzzle 1: Piano Tuners in Hyderabad

**Question:** Estimate the number of piano tuners in Hyderabad.

**Answer:** This is a Fermi estimation problem. A reasonable approach is:

1.  Estimate the number of pianos in Hyderabad.

2.  Estimate the average number of tunings per piano per year.

3.  Estimate how many tunings a single tuner can perform annually.

4.  Compute 

$$\text{Tuners} = \frac{\text{Total Tunings Per Year}}{\text{Tunings Per Tuner Per Year}}.$$

The exact number is less important than a logical decomposition and reasonable assumptions.

# Puzzle 2: Model Has 99.9% Accuracy

**Question:** A model has 99.9% accuracy on 1 million rows. Is it good?

**Answer:** The first question should be:

*“What is the class distribution?”*

If the dataset is highly imbalanced, accuracy can be misleading. For example, if 99% of observations belong to one class, a model predicting only the majority class achieves 99% accuracy while being useless.

Additional metrics to inspect:

- Precision

- Recall

- F1-score

- ROC-AUC or PR-AUC

# Puzzle 3: Recommendation Algorithms

**Question:** Algorithm A has CTR = 5.1%. Algorithm B has CTR = 5.4%. Can we conclude B is better?

**Answer:** No.

Things to check:

- Sample size

- Randomized A/B test design

- Statistical significance

- Confidence interval of the lift

- Business significance

A small increase may simply be random variation.

# Puzzle 4: Expected Tosses Until First Head

**Question:** A fair coin is tossed until the first Head appears. What is the expected number of tosses?

**Answer:** Let the expectation be $E$.

$$E=\frac12(1)+\frac12(1+E)$$

Solving:

$$E=2.$$

$$\boxed{E=2}$$

This is an example of **first-step analysis**.

# Puzzle 5: Feature X Increased Sales

**Question:** A manager says:

*“Sales increased after Feature X launched, therefore Feature X caused the increase.”*

**Answer:** Correlation is not causation.

Potential confounders:

- Seasonality

- Marketing campaigns

- Existing business trend

- Competitor actions

- Holidays or special events

A better approach is an A/B test or a causal inference framework.

# Puzzle 6: Traffic Lights in Hyderabad

**Question:** Estimate the number of traffic lights in Hyderabad.

**Answer:** One possible decomposition:

1.  Estimate the number of major intersections.

2.  Estimate the proportion that use traffic lights.

3.  Estimate the average number of signal units per intersection.

The focus is on assumptions and reasoning rather than the final numerical answer.

# Puzzle 7: Cancer Detection Metrics

**Question:** For a cancer detection model, which is more important: Accuracy, Precision, or Recall?

**Answer:** Usually Recall is most important because false negatives are very costly.

$$\text{Recall}=\frac{TP}{TP+FN}$$

Missing a cancer patient is often worse than generating an extra false alarm.

However, the correct metric depends on the business and medical costs associated with false positives and false negatives.

# Puzzle 8: Heavy Ball Puzzle

**Question:** One of eight balls is heavier than the others. Using a balance scale, what is the minimum number of weighings required to identify it?

**Answer:** Two weighings.

Reason:

Each weighing has three outcomes:

- Left heavier

- Right heavier

- Equal

Two weighings provide 

$$3^2=9$$

 possible outcome patterns, which is enough to distinguish among eight candidate balls.

# Puzzle 9: First Look at a CSV Dataset

**Question:** You receive a CSV containing 100 columns. What is the first thing you do?

**Answer:** First understand the schema:

- What is the target variable?

- Classification or regression?

- Data types?

- Missing values?

- Duplicates?

Then examine the target distribution and begin exploratory data analysis.
