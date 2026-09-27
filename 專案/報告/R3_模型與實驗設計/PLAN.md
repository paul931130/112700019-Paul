# R3: Model and Experimental Design — Outline

Corresponding manuscript section: Methods / Experiments. The 40% Project grade is based on the LaTeX manuscript, not this folder; see “What Is Actually Graded” in `../../README.md`.

## Model Setup (Two Models, Straight Replication)

| # | Model | Relation graph | Script | Status |
|---|---|---|---|---|
| 1 | Baseline | None | `training/rank_lstm.py` (in `Temporal_Relational_Stock_Ranking`) | Runs successfully |
| 2 | RSR replication target | Static industry/Wikidata graph + Temporal Graph Convolution | `training/relation_rank_lstm.py` | Runs successfully; full 50-epoch results are in `PROGRESS.md` |

> Note: `PROGRESS.md` retains an exploratory dynamic-relations run (rolling correlations, with a graph re-estimated over time). This is excluded from the final manuscript; the scope is a straight replication of the two models above. Keep its code and logs as historical records.

## Ablation Design (Following the Original Paper)

- With vs. without a relation graph (baseline vs. RSR).
- Industry vs. Wikidata relations (`-rn` parameter: `sector_industry` / `wikidata`).

Complete the NASDAQ + industry-relation setup first and obtain stable numbers; expand to Wikidata or NYSE only if time permits.

## Evaluation Metrics

Use the metrics in `training/evaluator.py` (the paper's MRR ranking metric plus the IRR return simulation). Both models and each ablation setting must report the same metrics to be compared in one table.

## To Do

- [x] Train the baseline and RSR and record loss/metrics (full 50-epoch results in `PROGRESS.md`).
- [ ] Decide whether to expand the ablation to Wikidata relations or NYSE.
- [ ] Prepare the main comparison table for the R3 report and compare it with Table 3 in the original paper.
