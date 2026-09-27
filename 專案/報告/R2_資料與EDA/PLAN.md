# R2: Data and EDA — Outline

Corresponding manuscript section: Data. The 40% Project grade is based on the LaTeX manuscript, not this folder; see “What Is Actually Graded” in `../../README.md`.

## Data Description

| Dataset | Description | Path |
|---|---|---|
| Sequential data | 30 years of daily data (open/high/low/close/volume) for 8,000+ NASDAQ/NYSE stocks, sourced from Google Finance | `../../../Temporal_Relational_Stock_Ranking/data/google_finance/` |
| Processed data | Version used by the paper, starting 2013-01-01 | `../../../Temporal_Relational_Stock_Ranking/data/2013-01-01/` |
| Industry relations | NASDAQ/NYSE sector and industry relations, including source files and `.npy` encodings | `.../data/sector_industry/` |
| Wikidata relations | Company relationships extracted from Wikidata | `.../data/wikidata/` (first extract `relation.tar.gz` with `tar zxvf`) |

Preprocessing scripts: `eod.py` (feature generation), `sector_industry.py`, and `wikidata.py`, all under `preprocess/`.

## EDA Notebook Coverage

1. **Sample size:** Number of stocks used (NASDAQ vs. NYSE), date range, and valid trading days per stock.
2. **Price and return distributions:** Closing-price and daily-return distributions/outliers, and whether standardization is needed (the paper uses z-scores).
3. **Relation-graph sparsity:** Number of edges, density, and average degree for the industry and Wikidata relation matrices. This figure will later be compared with the dynamic-relation matrix.
4. **Missing values and trading-day alignment:** Whether trading days are aligned across stocks and how missing values are handled (including the paper's imputation method).
5. **(For the extension) Initial rolling-correlation analysis:** Select a few stocks and plot 60-day rolling return correlations over time to illustrate that relations may change. This exploratory figure would motivate the R3 dynamic-relation ablation.

## Deliverables

- `eda.ipynb` (the required filename in the folder map in `../README.md`).
- Every figure should answer a question, rather than merely reproduce `describe()` output. Follow the 0914 assignment's Q8(h) requirement: **state one potentially surprising or questionable finding and show a figure that supports it.**

## To Do

- [ ] Decide whether to switch to Taiwan-listed stocks. This would require rerunning the sector-industry/Wikidata preprocessing and would be the largest scope change.
- [ ] Run a 60-day rolling-correlation check to confirm that the data can support the R3 dynamic-relation experiment.
