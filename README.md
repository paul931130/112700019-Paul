# 112700019-Paul

ML & FinTech · 115-1 · Prof. Huei-Wen Teng
Department of Information Management and Finance, National Yang Ming Chiao Tung University

- **GitHub**: https://github.com/paul931130/112700019-Paul
- **Overleaf manuscript**: _TODO — paste the Overleaf share link once uploaded (see `專案/manuscript/` in the course working folder for `main.tex` / `references.bib`)_
- **Canva slides**: _TODO — paste the Canva share link once created_

## Replicating a paper

Feng, Fuli, Xiangnan He, Xiang Wang, Cheng Luo, Yiqun Liu, and Tat-Seng Chua. "Temporal
Relational Ranking for Stock Prediction." *ACM Transactions on Information Systems* 37, no. 2
(2019): Article 27. https://doi.org/10.1145/3309547.

Official code: https://github.com/fulifeng/Temporal_Relational_Stock_Ranking

Extension (this project): a dynamic, rolling-window relation graph in place of RSR's static
industry/Wikidata graph — see the manuscript's Introduction and Methods sections for the research
questions and architecture.

## Code

Python, Jupyter Notebook:

- [`IC-0914.ipynb`](IC-0914.ipynb) — in-class EDA exercise applied to this project's stock/relation
  data (RSR replication universe), Colab-compatible (auto-clones the official RSR repo if the
  local data isn't found).
- [`homework/HW-0914-Q8.ipynb`](homework/HW-0914-Q8.ipynb) — ISLP §2.4 Q8, `College` dataset EDA.
- [`homework/HW-0914.md`](homework/HW-0914.md) / [`homework/HW-0914-Q3a.jpg`](homework/HW-0914-Q3a.jpg) — ISLP §2.4 Q2, Q3, Q7.

The model training code (baseline Rank\_LSTM, RSR, and the dynamic-relation extension) and the
manuscript source are maintained in the course working folder outside this repo pending a
decision on final repo layout: `Temporal_Relational_Stock_Ranking/training/` and
`專案/manuscript/`. _TODO: bring these into this repo's `Project/` folder to match the course's
required `HW/` + `Project/` structure._

## Data ("rawdata")

- **Sequential + relation data**: NASDAQ portion of the official RSR dataset
  (`Temporal_Relational_Stock_Ranking/data/`), from
  https://github.com/fulifeng/Temporal_Relational_Stock_Ranking — 1,026 tickers, 1,246 trading
  days (2013-01-01 onward), industry-relation graph over 97 categories.
- **`College` dataset** (homework Q8): https://www.statlearning.com/s/College.csv, from
  *An Introduction to Statistical Learning* (James et al. 2023).
- **Corporate credit rating dataset** (earlier draft pass, kept for reference, not the primary
  project data): `kirtandelwadia/corporate-credit-rating-with-financial-ratios` on Kaggle.
