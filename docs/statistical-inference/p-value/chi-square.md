# Chi-Square Test of Independence

!!! abstract "At a glance"
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
