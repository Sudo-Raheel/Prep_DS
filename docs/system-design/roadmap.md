# ML System Design Roadmap

Four weeks of interview preparation for senior applied scientist and data scientist roles.
Raheel • October 2026 • 5 to 6 hours per week

**Goal.** By the end of week 4, take any open-ended prompt (“design a system that …”) and talk through a complete, defensible design in 40 minutes, including the serving and monitoring parts that research-focused candidates most often leave thin.

**Weekly rhythm.** Four weekday sessions of 45 to 60 minutes for reading and concepts, plus one weekend session of about 90 minutes: one timed case spoken aloud (40 minutes), then a written review against the rubric in Section 5. Speaking aloud is the part that matters most; reading alone does not prepare you for the round.

## The answer framework

Use the same eight steps for every case. The minutes are a guide for a 45-minute round and leave a short buffer for questions.

| # | Step | What to cover | Min |
|---|---|---|---|
| 1 | Clarify | Business goal, users, scale, latency, what action the output drives, constraints (regulation, explainability) | 5 |
| 2 | Metrics | One offline metric, one online or business metric, and the guardrail metric that stops you over-optimising | 4 |
| 3 | Data and labels | Sources, how labels arise, label delay and noise, class imbalance, leakage risks | 6 |
| 4 | Features | Entity, aggregate, velocity, sequence and graph features; which are available at decision time | 6 |
| 5 | Model | Simple baseline first, then the stronger model and why; training cost and interpretability | 6 |
| 6 | Validation | Temporal splits, backtesting, calibration, slice analysis, threshold choice against capacity | 4 |
| 7 | Serving | Real-time versus batch, latency budget, feature freshness, fallbacks, how the score becomes a decision | 7 |
| 8 | Monitoring | Data and concept drift, alerting, feedback loop, retraining trigger, safe rollout | 5 |

Steps 2 to 6 are your home ground from fraud modelling. Steps 7 and 8 are the gap this roadmap is built to close, and they are also where interviewers separate senior candidates from mid-level ones.

## Week-by-week plan

### Week 1: Framework and home ground

- **Read:** Huyen, chapters 1, 2, 4, 5 and 6 (overview, system design, training data, feature engineering, model development and offline evaluation).

- **Learn:** The eight-step framework until you can recite it without notes. How to state requirements as numbers: transactions per second, latency budget, acceptable false-positive rate.

- **Practise:** Case 1 (real-time payment fraud) twice: once written and untimed, once spoken and timed.

- **Done when:** You have a two-page written design for Case 1 that you would be happy to defend, using only non-confidential detail.

### Week 2: Serving and production (the main gap)

- **Read:** Huyen, chapters 7, 8 and 9 (deployment and prediction service, distribution shifts and monitoring, continual learning and testing in production). Skim chapters 3 and 10 for vocabulary.

- **Learn:** Batch versus online prediction; feature stores and online/offline skew; latency budgets; shadow deployment, canary release and A/B testing; retraining triggers; model fallbacks.

- **Practise:** Case 2 (account takeover) and Case 3 (lending application fraud), both spoken and timed.

- **Done when:** You can spend seven unbroken minutes on serving and monitoring for a fraud system without drifting back to modelling.

### Week 3: Cases outside fraud

- **Read:** Aminian and Xu: the introductory chapter, then the video recommendation, ad click prediction and harmful content detection chapters.

- **Learn:** Candidate generation followed by ranking; embeddings and two-tower models; approximate nearest-neighbour retrieval; cold start; position bias; exploration versus exploitation.

- **Practise:** Case 4 (recommendation), Case 5 (ad click prediction) and Case 6 (harmful content detection).

- **Done when:** You can design a retrieval-and-ranking system from a blank page, since interviewers often deliberately leave your domain.

### Week 4: LLM systems and full mocks

- **Read:** One current engineering write-up each on retrieval-augmented generation, agent design, and LLM evaluation (company engineering blogs are the best source; pick recent ones).

- **Learn:** The RAG pipeline (chunking, embedding, retrieval, reranking, generation); agents with tools; guardrails; evaluation with fixed test sets, model-graded checks and human review; cost, latency and caching; audit trails for regulated decisions.

- **Practise:** Case 7 (fraud investigation assistant) and Case 8 (dispute resolution assistant), then two full 45-minute mocks with a peer, or recorded and replayed.

- **Done when:** Both mocks score 3 or more on every rubric line.

## Case bank

| # | Case | What makes it hard |
|---|---|---|
| 1 | Real-time payment fraud detection | Sub-second latency, extreme imbalance, delayed and noisy labels, adaptive adversaries |
| 2 | Account takeover detection | Session and device signals, few confirmed labels, friction cost of step-up authentication |
| 3 | Lending application fraud | Synthetic identities, bureau and alternate data, no outcome label for rejected applicants |
| 4 | Video or product recommendation | Two-stage retrieval and ranking, cold start, feedback loops in the training data |
| 5 | Ad click prediction | Very high volume, calibration matters, continual training on fresh data |
| 6 | Harmful content detection | Multi-modal inputs, policy changes, human review capacity as a constraint |
| 7 | Fraud investigation assistant (LLM) | Grounding in case data, hallucination risk, auditability, analyst trust |
| 8 | Dispute resolution assistant (LLM) | Tool use, escalation rules, evaluating open-ended answers |

For Cases 1 to 3, prepare the points that tie back to your own work: sampling under extreme imbalance, training with noisy labels, and why random splits overstate fraud model performance.

## Concept checklist

Tick each item once you can explain it in two minutes with an example.

#### Data and features
- [ ] Label delay and how it biases recent data
- [ ] Leakage through future information
- [ ] Point-in-time correct feature joins
- [ ] Feature store: offline and online paths
- [ ] Online/offline skew and how to detect it
- [ ] Streaming versus batch aggregates

#### Serving
- [ ] Batch versus online prediction
- [ ] Latency budget across the request path
- [ ] Model compression and caching
- [ ] Fallback when a model or feature is down
- [ ] Score to decision: thresholds and rules

#### Release and monitoring
- [ ] Shadow deployment and canary release
- [ ] A/B testing and its limits in fraud
- [ ] Data drift versus concept drift
- [ ] Monitoring without immediate labels
- [ ] Retraining triggers and cadence
- [ ] Feedback loops and selection bias

#### Retrieval, ranking and LLMs
- [ ] Candidate generation and ranking stages
- [ ] Two-tower models and ANN search
- [ ] Cold start and position bias
- [ ] RAG pipeline and its failure points
- [ ] Evaluating LLM outputs
- [ ] Guardrails, cost and latency trade-offs

## Self-review rubric

After each timed case, score yourself from 1 (missing) to 4 (strong) and write one sentence on what to fix next time.

| Line | A score of 4 looks like |
|---|---|
| Problem framing | Asked for scale, latency and the business action before proposing anything |
| Metrics | Named offline, online and guardrail metrics and linked them |
| Data and labels | Raised label delay, noise and leakage unprompted |
| Modelling | Started simple, justified each step up in complexity |
| Serving | Gave a latency budget and a fallback path |
| Monitoring | Explained drift detection and the retraining trigger |
| Trade-offs | Stated at least three explicit trade-offs and chose a side |
| Communication | Kept to time, drew the system, checked in with the interviewer |

## Common mistakes

- Jumping to the model before agreeing what the system is for.

- Spending 25 minutes on modelling and two on serving.

- Proposing a complex model with no baseline to compare against.

- Quoting AUC alone on an imbalanced problem.

- Describing a random train-test split for time-ordered data.

- Ignoring what happens when a feature source or the model is unavailable.

- Presenting one design as the only option instead of naming the trade-offs.

## If an interview arrives early

A five-day compressed version, about 90 minutes per day:

1.  Memorise the framework; write out Case 1 in full.

2.  Huyen chapters 7 and 8; tick the Serving and Release checklists.

3.  Case 1 spoken and timed, then Case 2.

4.  One case outside fraud (Case 4) and, if the role mentions LLMs, Case 7.

5.  One full mock, scored against the rubric; fix the two lowest lines.

## Resources

- Chip Huyen, *Designing Machine Learning Systems* (O’Reilly, 2022). The main text for concepts.

- Ali Aminian and Alex Xu, *Machine Learning System Design Interview* (2023). Worked cases in interview format.

- Stanford CS 329S, *Machine Learning Systems Design*: lecture notes, free online, as a lighter alternative to the Huyen book.

- Engineering blogs from payments and marketplace companies on their fraud and risk platforms, for realistic architectures and vocabulary.
