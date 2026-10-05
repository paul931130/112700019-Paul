# rawdata

The dataset is the one released by Feng et al. (2019): daily end-of-day data from Google Finance, preprocessed by the
authors (`data/2013-01-01/<MARKET>_<TICKER>_1.csv`, `data/relation/`, ticker lists).

It is **not copied here**. `data/2013-01-01/` is about 200 MB and the full `data/` folder about 6 GB with the raw
`google_finance/` files, and the authors' code is AGPL-3.0. Get it by cloning their repository at commit `cfbb01b`
into `coding/rsr/upstream/` (exact steps in `coding/rsr/README.md`). The relation files are inside `data/relation.tar.gz` in that clone and
must be extracted before use. Nothing under `upstream/data/` is edited;
anything our code produces goes to `../processed-data/`.
