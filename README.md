# 112700019-Paul

ML & FinTech · Fall 2026 · Professor Huei-Wen Teng
Department of Information Management and Finance, National Yang Ming Chiao Tung University

- **GitHub:** https://github.com/paul931130/112700019-Paul
- **Overleaf manuscript:** https://www.overleaf.com/read/fjkrqhnbqwgc#e5d02b
  Read-only link. Please make sure `venteng@gmail.com` has been added as a collaborator.
- **Canva slides:** https://canva.link/psyac0w98zuyn5l

## Paper Replication

Feng, Fuli, Xiangnan He, Xiang Wang, Cheng Luo, Yiqun Liu, and Tat-Seng Chua. “Temporal Relational Ranking for Stock Prediction.” *ACM Transactions on Information Systems* 37, no. 2 (2019): Article 27. https://doi.org/10.1145/3309547.

Official code: https://github.com/fulifeng/Temporal_Relational_Stock_Ranking

This project is a direct replication, with no architectural extensions. It compares the official baseline (Rank_LSTM, without a relation graph) with RSR (a static industry-relation graph). See `Project/README.md` and `Project/manuscript/main.tex` for the full write-up, results, and discussion.

## Code

Python and Jupyter Notebooks:

- [`in-class-exercise/IC-0914.ipynb`](in-class-exercise/IC-0914.ipynb) — In-class EDA exercise using this project's stock and relation data (the RSR replication universe). Colab-compatible; it automatically clones the official RSR repository if local data is unavailable.
- [`HW/HW-0914-Q8.ipynb`](HW/HW-0914-Q8.ipynb) — ISLP `2.4, Q8: EDA of the `College` dataset.
- [`HW/HW-0914.md`](HW/HW-0914.md) / [`HW/HW-0914-Q3a.jpg`](HW/HW-0914-Q3a.jpg) — ISLP `2.4, Q2, Q3, and Q7.
- [`HW/HW-0921.md`](HW/HW-0921.md) — Hierarchical clustering and K-means.

The Project folder (`Project/`) is part of this repository. It contains the motivation (R1), EDA notebook (R2), model training results and logs (R3), analysis draft (R4), and manuscript source (`Project/manuscript/main.tex`). The model training code (baseline Rank_LSTM and RSR) remains in an external clone of the official repository: `Temporal_Relational_Stock_Ranking/training/`. It is too large to commit here and is referenced by path in `Project/README.md`.

## Data

- **Sequential and relation data:** The NASDAQ portion of the official RSR dataset (`Temporal_Relational_Stock_Ranking/data/`), from https://github.com/fulifeng/Temporal_Relational_Stock_Ranking — 1,026 tickers, 1,246 trading days (from 2013-01-01), and an industry-relation graph with 97 categories.
- **`College` dataset** (homework Q8): https://www.statlearning.com/s/College.csv, from *An Introduction to Statistical Learning* (James et al., 2023).
- **Corporate credit rating dataset** (from an earlier draft, retained for reference and not used as the primary project dataset): `kirtandelwadia/corporate-credit-rating-with-financial-ratios` on Kaggle.
