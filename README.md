# 112700019-Paul

ML & FinTech · 115-1 · Prof. Huei-Wen Teng
Department of Information Management and Finance, National Yang Ming Chiao Tung University

- **GitHub**: https://github.com/paul931130/112700019-Paul
- **Overleaf manuscript**: https://www.overleaf.com/read/fjkrqhnbqwgc#e5d02b
  （唯讀連結；記得確認 `venteng@gmail.com` 有被加進協作者）
- **Canva slides**: https://canva.link/psyac0w98zuyn5l

## Replicating a paper

Feng, Fuli, Xiangnan He, Xiang Wang, Cheng Luo, Yiqun Liu, and Tat-Seng Chua. "Temporal
Relational Ranking for Stock Prediction." *ACM Transactions on Information Systems* 37, no. 2
(2019): Article 27. https://doi.org/10.1145/3309547.

Official code: https://github.com/fulifeng/Temporal_Relational_Stock_Ranking

This project is a straight replication — no architectural extension. It compares the official
baseline (Rank_LSTM, no relation graph) against RSR (static industry relation graph); see
`專案/README.md` and `專案/manuscript/main.tex` for the full writeup, results, and discussion.

## Code

Python, Jupyter Notebook:

- [`in-class-exercise/IC-0914.ipynb`](in-class-exercise/IC-0914.ipynb) — in-class EDA exercise
  applied to this project's stock/relation data (RSR replication universe), Colab-compatible
  (auto-clones the official RSR repo if the local data isn't found).
- [`homework/HW-0914-Q8.ipynb`](homework/HW-0914-Q8.ipynb) — ISLP §2.4 Q8, `College` dataset EDA.
- [`homework/HW-0914.md`](homework/HW-0914.md) / [`homework/HW-0914-Q3a.jpg`](homework/HW-0914-Q3a.jpg) — ISLP §2.4 Q2, Q3, Q7.
- [`homework/HW-0921.md`](homework/HW-0921.md) — hierarchical clustering and K-means.

The Project folder (`專案/`) is now part of this repo: motivation (R1), EDA notebook (R2), model
training results and logs (R3), analysis draft (R4), and the manuscript source
(`專案/manuscript/main.tex`). The model training code itself (baseline Rank_LSTM, RSR) stays in
the official repo clone outside this one: `Temporal_Relational_Stock_Ranking/training/` — too
large to commit here, referenced by path in `專案/README.md`.

## Data ("rawdata")

- **Sequential + relation data**: NASDAQ portion of the official RSR dataset
  (`Temporal_Relational_Stock_Ranking/data/`), from
  https://github.com/fulifeng/Temporal_Relational_Stock_Ranking — 1,026 tickers, 1,246 trading
  days (2013-01-01 onward), industry-relation graph over 97 categories.
- **`College` dataset** (homework Q8): https://www.statlearning.com/s/College.csv, from
  *An Introduction to Statistical Learning* (James et al. 2023).
- **Corporate credit rating dataset** (earlier draft pass, kept for reference, not the primary
  project data): `kirtandelwadia/corporate-credit-rating-with-financial-ratios` on Kaggle.
