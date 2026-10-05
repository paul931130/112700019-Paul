# 112700019-Paul

ML & FinTech · Fall 2026 · Professor Huei-Wen Teng
Department of Information Management and Finance, National Yang Ming Chiao Tung University

- **GitHub:** https://github.com/paul931130/112700019-Paul
- **Overleaf:** https://www.overleaf.com/read/fjkrqhnbqwgc#e5d02b
- **Canva:** https://canva.link/psyac0w98zuyn5l
- **Course rules:** https://github.com/202609-ML-FinTech/00-repo-template

Instructor access to Overleaf and Canva must be verified separately.

## Structure

```text
homework/<mmdd>/
in-class-exercise/<mmdd>/
replicating-a-paper/
    README.md
    data/rawdata/
    data/processed-data/
    coding/
    _snapshots/
    manuscript/
```

Course materials, external repositories, old drafts, planning notes and templates are archived outside this repository.

## Paper replication

Feng, Fuli, Xiangnan He, Xiang Wang, Cheng Luo, Yiqun Liu, and Tat-Seng Chua. “Temporal Relational Ranking for Stock Prediction.” *ACM Transactions on Information Systems* 37, no. 2 (2019): Article 27. https://doi.org/10.1145/3309547.

This project compares Rank_LSTM and RSR with static industry relations, without architectural extensions. The multi-agent trading system is personal motivation, not part of the experiment.

- [Project README](replicating-a-paper/README.md)
- [Manuscript source](replicating-a-paper/manuscript/main.tex)
- [R1 manuscript PDF](replicating-a-paper/_snapshots/20261005-manuscript.pdf)
- [R1 slides PDF](replicating-a-paper/_snapshots/20261005-slides.pdf)
- [Replicated paper](replicating-a-paper/_snapshots/feng2019-temporal-relational-ranking.pdf)

## Code and data

- [IC-0914](in-class-exercise/0914/IC-0914.ipynb): RSR stock EDA. This differs from the assigned credit-default exercise; acceptance of the substitution has not been verified.
- [IC-0921](in-class-exercise/0921/IC-0921.ipynb): portfolio clustering.
- [IC-1005](in-class-exercise/1005/IC-1005.ipynb): portfolio PCA.
- [HW-0914 answers](homework/0914/HW-0914.md), [hand-drawn sketch](homework/0914/HW-0914-Q3a.jpg), and [College EDA](homework/0914/HW-0914-Q8.ipynb).
- [HW-0921 answers](homework/0921/HW-0921.md) and hand-worked photographs in the same directory.
- [Project EDA](replicating-a-paper/coding/eda.ipynb); training logs are in `replicating-a-paper/coding/logs/`.
- Stock data and original code: https://github.com/fulifeng/Temporal_Relational_Stock_Ranking (1,026 NASDAQ tickers, 1,246 trading days, 97 industry categories).
- College data: https://www.statlearning.com/s/College.csv; a copy is in `homework/0914/data/College.csv`.

The patch to the authors' training scripts, pinned requirements and run commands are in [replicating-a-paper/coding/rsr](replicating-a-paper/coding/rsr/README.md). The full stock dataset is not stored here; see [its README](replicating-a-paper/data/rawdata/README.md).
