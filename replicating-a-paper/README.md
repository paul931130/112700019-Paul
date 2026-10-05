# Machine Learning & FinTech — Final Project

## Replicating a High-Quality Paper

Feng, Fuli, Xiangnan He, Xiang Wang, Cheng Luo, Yiqun Liu, and Tat-Seng Chua. "Temporal Relational Ranking for Stock Prediction." *ACM Transactions on Information Systems* 37, no. 2 (2019): Article 27. https://doi.org/10.1145/3309547.

- Journal tier: NYCU CS A-tier journal list (`共用參考資料` or the course GitHub's `journal-ranking/交大資工A級期刊_20200910Updated.xlsx`, entry 11)
- Official code: https://github.com/fulifeng/Temporal_Relational_Stock_Ranking
- Local replication environment: `../Temporal_Relational_Stock_Ranking` (cloned, TF1→TF2 compatibility patched, venv set up, baseline RankLSTM verified working)
- **Always set `TF_USE_LEGACY_KERAS=1` before running any training command** (e.g.
  `TF_USE_LEGACY_KERAS=1 python rank_lstm.py -p ../data/2013-01-01 -m NASDAQ -l 4 -u 32`),
  otherwise it fails at the `BasicLSTMCell` line with `AttributeError: BasicLSTMCell is not available with Keras 3`.
  Details in `reports/R3_model_and_experiments/PROGRESS.md`.

## Paper Summary and Method

Proposes the Relational Stock Ranking (RSR) model with Temporal Graph Convolution, encoding relations between stocks (industry relation, Wikidata relation) into a ranking task in a time-sensitive way, to predict the relative ranking of next-day stock returns — replacing the prior approach of treating stocks as independent entities.

## What Is Actually Graded (per syllabus + official GitHub)

The `reports/R1~R4` folders originally referenced a "corresponding grading rubric item," but that rubric could not be traced to any source — neither syllabus (`slides/20260907-Ch00-Syllabus.pdf`, `slides/20260914-Ch00-Syllabus.pdf`) nor the official GitHub (`202609-ML-FinTech/00-course-info`, verified directly via the GitHub API on 2026-09-14) contains such a table, nor any statement about "R1/R2/R3/R4 each being graded separately." Below is the verified, actual basis:

**Grading policy** (`20260907-Ch00-Syllabus.pdf` p.6):

| Item | % | Content |
|---|---|---|
| Participation | 20% | In-class exercises, presentations (project/MFS/HW), class wrap-ups, subject to cold calls |
| **Project** | **40%** | **Graded on the manuscript (written in LaTeX)**, plus slides for the presentation |
| Exam | 40% | In-class exam, one double-sided A4 cheat sheet allowed |

**Your personal repo structure** (same source, p.5):

```
202609-ML-FinTech-<studentID>-<nickname>/
├── homework/
└── replicating-a-paper/   ← README.md, logs, snapshots, data and codes
```

**The Project's README.md must include** (p.10 "Your GitHub Repo"): a link to your GitHub page, a Chicago-style citation of the replicated paper, a link to the Overleaf manuscript, a link to the Canva slides, "Code" (Jupyter Notebook), and "Data" (dataset or link).

**What is actually graded is the Project's 40% LaTeX manuscript**, not this folder itself. The content under `reports/R1~R4` (motivation, EDA, model experiments, conclusion) is still real material the manuscript needs — the only thing dropped is the mistaken framing that each folder is "worth X% of a grading rubric." The four folders are now just draft sections written before assembling the manuscript:

| Folder | Corresponding manuscript section | Content |
|---|---|---|
| `reports/R1_topic_and_motivation` | Introduction / Motivation | Paper introduction, why this paper, RQ1 |
| `reports/R2_data_and_eda` | Data | Raw data description, EDA notebook (`eda.ipynb`) |
| `reports/R3_model_and_experiments` | Methods / Experiments | Baseline (Rank_LSTM) vs. RSR, with ablation (relation graph present/absent, industry vs. wiki) |
| `reports/R4_results_and_conclusion` | Results / Conclusion | Interpretation of results, comparison with the original paper, discussion |
| `references` | References | Full text of the replicated paper, related-literature notes |
| `程式碼` | — | Points to `../Temporal_Relational_Stock_Ranking`, or holds a cleaned-up Jupyter Notebook version |
| `資料` | — | Dataset or dataset-link description |

## Scope (decided): a straight replication, no extension

A "dynamic cross-stock relation" extension was considered at one point (see the exploration notes in `reports/R3_model_and_experiments/PROGRESS.md`), but has been **dropped** — this project is a straight replication of Feng et al. (2019)'s RSR, with no new method added. The dynamic-relation code (`preprocess/dynamic_relation.py`, `training/dynamic_relation_rank_lstm.py`) and its log files are left in place as a record of that exploration, but do not appear in the final manuscript's conclusions.

## Data

- **Sequential Data**: 30 years of historical daily data (open, high, low, close, volume) for 8,000+ NASDAQ/NYSE stocks, sourced from Google Finance; the paper uses the processed version starting 2013-01-01
- **Industry Relation**: sector/industry relations among NASDAQ/NYSE stocks
- **Wiki Relation**: company relations extracted from Wikidata
- Data is provided with the official repo, at: `../Temporal_Relational_Stock_Ranking/data/`

## Code

Python, Jupyter Notebook (the README requires a Jupyter Notebook submission; the original training scripts are `.py`, additionally cleaned up into `.ipynb`):
- `training/rank_lstm.py`: baseline, Rank_LSTM (no relation graph)
- `training/relation_rank_lstm.py`: full model, Relational Stock Ranking (RSR)

## Manuscript / Slides

- Overleaf: https://www.overleaf.com/read/fjkrqhnbqwgc#e5d02b
  (this is a read-only share link; if `venteng@gmail.com` has not been added as a collaborator yet,
  that still needs to be done separately — a read-only link does not count as sharing with the instructor)
- Canva Slides: https://canva.link/psyac0w98zuyn5l
  (using this for submission for now; once the instructor/TA grants edit access to the
  `20260920-template-ML&FinTech` template (https://www.canva.com/design/DAHROU_9H8o/...),
  switch to a copy of that template instead.
  Remember to share it with venteng@gmail.com)
  - Backup: https://canva.link/a6bv496rvwdfbl5 (AI-generated plain-white minimalist version;
    R1 content is fully filled in, R2/R3/R4 are placeholders; mimics the template's layout logic
    but has no NYCU logo)

## GitHub

- Student ID: 112700019 · Nickname: Paul
- Personal repo: https://github.com/paul931130/112700019-Paul
- Pushed: `homework/`, `in-class-exercise/` and `replicating-a-paper/` are tracked and pushed
  (`Temporal_Relational_Stock_Ranking/`, `共用參考資料`, `replicating-a-paper/coding/GCNET-Code`,
  `replicating-a-paper/coding/HGTAN` are external clones, excluded via `.gitignore`, not part of the personal repo)
