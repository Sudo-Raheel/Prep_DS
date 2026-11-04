**SQL Roadmap for Data Science Interviews**\
14 days, one hour a day, for someone who already thinks in pandas\

------------------------------------------------------------------------

Week 1 covers the basics. Week 2 covers what interviewers test most: CTEs, window functions and dates, applied to fraud-style questions.

# Setup (Day 0, 20 minutes)

- **Dialect:** learn PostgreSQL syntax, which is the safest default for interviews.

- **Where to practise:** install DuckDB (`pip install duckdb`). It runs SQL directly on pandas DataFrames, so you can write a query and check it against the pandas version you already know.

- **Daily format:** 20 minutes on the concept, then 40 minutes typing queries yourself.

# Week 1: the basics

\@c c L L L@ & **Day** & **Topic** & **pandas equivalent** & **Watch out for**\
$\square$& 1 & `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `DISTINCT` & column selection, boolean masks, `sort_values` & SQL describes the result, not the steps\
$\square$& 2 & `AND`/`OR`, `IN`, `BETWEEN`, `LIKE`, `IS NULL`, `COALESCE` & `isin`, `between`, `str.contains`, `fillna` & `col = NULL` is never true, so use `IS NULL`\
$\square$& 3 & `COUNT`, `SUM`, `AVG`, `MIN`/`MAX`, `GROUP BY` & `groupby().agg()` & `COUNT(*)`, `COUNT(col)` and `COUNT(DISTINCT col)` differ\
$\square$& 4 & `HAVING`, `CASE WHEN`, conditional aggregation & filtering after `groupby`, `np.where` & `WHERE` filters rows, `HAVING` filters groups\
$\square$& 5 & `INNER JOIN`, `LEFT JOIN` & `merge(how=...)` & Check the row count before and after every join\
$\square$& 6 & Self-joins, anti-joins, duplicate keys & `merge` on the same frame, `indicator=True` & Duplicate keys multiply rows, and NULL keys never match\
$\square$& 7 & Review with 8 to 10 easy problems & — & Execution order: `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `SELECT`, `ORDER BY`\

**Checkpoint for day 4.** You should be able to write fraud rate by merchant from memory:

    SELECT merchant_id,
           AVG(CASE WHEN is_fraud THEN 1.0 ELSE 0 END) AS fraud_rate
    FROM transactions
    GROUP BY merchant_id
    HAVING COUNT(*) >= 100;

# Week 2: interview level

\@c c L L L@ & **Day** & **Topic** & **pandas equivalent** & **Practice question**\
$\square$& 8 & Subqueries and CTEs (`WITH`) & intermediate DataFrames & Users whose spend is above the average\
$\square$& 9 & `ROW_NUMBER`, `RANK`, `DENSE_RANK` & `groupby().cumcount()`, `rank` & Each user’s first transaction\
$\square$& 10 & `LAG`, `LEAD` & `groupby().shift()` & Gap since each user’s previous transaction\
$\square$& 11 & Running totals and window frames & `cumsum`, `rolling` & Running spend per user\
$\square$& 12 & `DATE_TRUNC`, `EXTRACT`, intervals & `dt.floor`, `dt.hour`, `Timedelta` & Fraud rate by week\
$\square$& 13 & Fraud patterns combining all of the above & — & Three or more transactions within ten minutes\
$\square$& 14 & Timed mock: 5 medium problems, explained aloud & — & —\

**Checkpoint for day 10.** Gap since each user’s previous transaction:

    SELECT user_id,
           txn_time,
           txn_time - LAG(txn_time) OVER (
               PARTITION BY user_id
               ORDER BY txn_time
           ) AS gap_since_previous
    FROM transactions;

# After day 14

- Do 30 to 50 problems across LeetCode’s SQL set, DataLemur and StrataScratch, at 3 or 4 a day.

- Redo any problem you got wrong two days later, without looking at the solution.

- Prioritise fraud-style questions: transactions per user in the last 24 hours, first transaction per user, bursts of activity in a short window, and fraud rate by merchant or by week.
