# Paper replication — Machine Learning & FinTech

Feng, Fuli, Xiangnan He, Xiang Wang, Cheng Luo, Yiqun Liu, and Tat-Seng Chua. “Temporal Relational Ranking for Stock Prediction.” *ACM Transactions on Information Systems* 37, no. 2 (2019): Article 27. https://doi.org/10.1145/3309547.

- Student: 112700019 · Paul (Yue Zhen Huang)
- GitHub: https://github.com/paul931130/112700019-Paul
- Overleaf: https://www.overleaf.com/read/fjkrqhnbqwgc#e5d02b
- Canva: https://canva.link/psyac0w98zuyn5l
- Official code and data: https://github.com/fulifeng/Temporal_Relational_Stock_Ranking
- Course rules: https://github.com/202609-ML-FinTech/00-repo-template

Verify instructor sharing separately from these links.

## Scope

Replicate Rank_LSTM (no relation graph) and RSR (static industry relations) on the released NASDAQ data. The multi-agent trading system only motivates the topic. Dynamic-relation experiments are historical exploration and are excluded from the manuscript's conclusions.

## Files

| Path | Contents |
|---|---|
| `manuscript/main.tex` | Sole current manuscript source |
| `manuscript/ref.bib` | Bibliography used by the manuscript |
| `manuscript/figures/` | Figures and their generator |
| `coding/eda.ipynb` | Project EDA notebook |
| `coding/logs/` | Historical execution logs; `dynamic*` logs are exploratory |
| `coding/rsr/` | Patch to the authors' code, pinned requirements and the exact run commands |
| `data/rawdata/` | Immutable downloaded data; empty on purpose, its README says where the data comes from |
| `data/processed-data/` | Generated data; currently a placeholder |
| `_snapshots/feng2019-temporal-relational-ranking.pdf` | Replicated paper |
| `_snapshots/20261005-manuscript.pdf` | R1 manuscript snapshot |
| `_snapshots/20261005-slides.pdf` | R1 slides snapshot |

The existing editable slides file is retained in `_snapshots/`; the PDF is the required submission file. Old drafts, reference notes, planning documents and templates have been archived outside the repository.

## Milestones

| Milestone | Content | Deadline (Asia/Taipei) |
|---|---|---|
| R1 | Paper, motivation and personal interest | 2026-10-05 23:59 |
| R2 | Data description and EDA | 2026-10-19 23:59 |
| R3 | Benchmark models and experiment design | 2026-11-09 23:59 |
| R4 | Empirical analysis and conclusion | 2026-11-30 23:59 |

Grading policy is governed by the current syllabus linked from the course information repository.

## Local archive and data

The archive is a sibling of this repository:

```text
../機器學習與金融科技_本機存檔/20261005-整理/
    move-manifest.json
    external-code/Temporal_Relational_Stock_Ranking/
    local-root/
    project-history/
```

The main stock-data directory is `external-code/Temporal_Relational_Stock_Ranking/data/` inside that archive. The EDA notebook searches `RSR_DATA` / `RSR_DATA_DIR`, then `coding/rsr/upstream/data/` (the clone described in `coding/rsr/README.md`), then `data/rawdata/Temporal_Relational_Stock_Ranking/data/`, then the archive. Set `RSR_DATA` (or `RSR_DATA_DIR`) to the dataset's `data` directory before starting Jupyter to use another location. The archive is local supporting material; it is not available to a GitHub reader.

## Reproducibility status

`coding/rsr/` holds what is needed to re-run the baseline and RSR: the patch against the authors' code
(`rsr-compat.patch`), pinned requirements and the exact commands. The authors' repository is cloned into
`coding/rsr/upstream/` (git-ignored) and its `data/relation.tar.gz` must be extracted there; `data/rawdata/README.md`
explains the data.

Checked: the patch applies cleanly to the authors' commit `cfbb01b` and reproduces the two scripts that produced
`coding/logs/`.

Not verified or missing:

- Training and the EDA notebook have not been re-run from a fresh clone.
- The seed-2 baseline logs (`baseline_seed2*.log`) record no arguments and the saved script has no seed option, so
  that run cannot be reproduced exactly.
- There is no small immutable sample yet. The processed data is about 200 MB and the extracted relation files are
  several GB (NASDAQ industry matrix 817 MB, NYSE 2.6 GB).
- Outputs kept in notebooks and logs are historical, not evidence of a new run. Run Restart & Run All before each
  milestone.
