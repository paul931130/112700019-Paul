# Manuscript Outline

Chapter outline for Overleaf. It maps the R1–R4 draft folders to manuscript sections. Tags such as [R2] and [R3] point to existing material that can be adapted directly rather than rewritten from scratch.

## Title

*Does the Relation, or Its Change Over Time, Predict Stock Returns? A Replication of Temporal Relational Ranking with a Dynamic-Relation Extension*
(Provisional; revise before finalizing.)

## Abstract

One paragraph (150–250 words): question → method → main findings. Write this after the R3/R4 results are final; the abstract is usually the last section completed.

## 1. Introduction

Source: `reports/R1_topic_and_motivation/PLAN.md`. A draft exists and needs polishing into formal prose.

- 1.1 Motivation: Why should stocks not be modeled as independent entities?
- 1.2 Replicated paper: Feng et al. (2019), RSR — summarize the core method in one paragraph.
- 1.3 Research questions: RQ1 (replication), RQ2 (extension: dynamic relations).
- 1.4 One-sentence summary of the contribution.

## 2. Related Work

A new section not directly covered by R1 PLAN.md, but source material is available:

- Relation-based stock prediction beyond RSR: HGTAN (hypergraph) and GCNET (graph convolution). Explain how these differ from this project's extension (dynamic vs. static relation graphs).
- Select two to four papers from `references/related-literature-shortlist.md` (supply-chain relations and cross-market information transmission) as external support for the hypothesis that relations change over time.

## 3. Data

[R2] Source: `reports/R2_data_and_eda/eda.ipynb`. Rewrite the A1/A2/A3/B1 findings directly as prose:

- 3.1 Data source: 1,026 NASDAQ stocks in `data/2013-01-01/`, with 1,246 trading days (about five years, not the 30 years stated in the README).
- 3.2 Relation graph: industry relations; 156 tickers (15%) are ETFs/funds, not individual stocks, and have been excluded.
- 3.3 Data cleaning: `-1234` missing-value code and sample size after excluding ETFs.

## 4. Methods

[R3] Three model configurations, sourced from `reports/R3_model_and_experiments/PROGRESS.md`:

- 4.1 Baseline: Rank_LSTM (no relation graph).
- 4.2 RSR: static industry relation graph + Temporal Graph Convolution (replication target).
- 4.3 This project's extension: dynamic relations, re-estimating the relation graph in each rolling window using rolling correlations (`preprocess/dynamic_relation.py`; mechanism verified, with edge density ranging from 4.6% to 33.8% across windows).

## 5. Experiments and Results

- 5.1 Metrics: MSE, MRR-Top1, and simulated return (`training/evaluator.py`).
- 5.2 Baseline results [real R3 numbers available]: Test MSE 0.000377, mrrt 0.049, btl 1.02 (full NASDAQ run, 50 epochs).
- 5.3 RSR results: **pending** (embedding exported to `data/pretrain/NASDAQ_rank_lstm_seq-4_unit-32_0.npy`; one full training run remains).
- 5.4 Dynamic-relation results: **pending** (script runs but has not been integrated into `relation_rank_lstm.py` or run on the full dataset).
- 5.5 Ablation table: baseline / RSR / dynamic, with the same three metrics.

## 6. Discussion

[R4] Source: the three scenarios in `reports/R4_results_and_conclusion/PLAN.md` (dynamic relations clearly better / no difference / worse). Choose and rewrite one after the 5.4 results are available:

- 6.1 Was the replication successful? Did it match the original paper's direction?
- 6.2 Interpret the dynamic-relation results and explain why, whatever the outcome.
- 6.3 Differences from the original paper: data period and market coverage.
- 6.4 Limitations.

## 7. Conclusion and Future Work

Summarize the findings and address the syllabus prompt “Potential of your project”: if dynamic relations help, a next step could be a thesis or journal publication.

## References

Use Chicago style. Include all papers in `references/` and cite the primary replicated paper in Chicago style.

---

## What Can Be Written Now vs. What Must Wait

| Section | Ready to write? |
|---|---|
| 1 Introduction | ✅ Yes; source material is ready |
| 2 Related Work | ✅ Yes; source material is ready |
| 3 Data | ✅ Yes; adapt the contents of `eda.ipynb` |
| 4 Methods | ✅ Yes; all three model configurations are decided |
| 5.2 Baseline results | ✅ Yes; real results are available |
| 5.3 RSR results | ⏳ Wait for the full training run |
| 5.4 Dynamic-relation results | ⏳ Wait for dynamic graph integration into `relation_rank_lstm.py` and a full run |
| 6 Discussion / 7 Conclusion | ⏳ Wait for both 5.3 and 5.4 results |
| Abstract | ⏳ Write last, after the rest is complete |
