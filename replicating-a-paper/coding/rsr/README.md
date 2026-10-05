# RSR replication: code, environment, data, commands

This folder lets a reader re-run the baseline (Rank_LSTM) and RSR experiments of Feng et al. (2019) from this
repository alone. The authors' code is **not** copied here: it is AGPL-3.0, so this folder keeps only our changes
as a patch (`rsr-compat.patch`, distributed under the same license).

| File | What it is |
|---|---|
| `rsr-compat.patch` | Our changes to `training/rank_lstm.py` and `training/relation_rank_lstm.py` (apply to upstream commit `cfbb01b`) |
| `requirements.txt` | Packages for the training scripts (versions that produced `../logs/`) |
| `requirements-eda.txt` | Packages for `../eda.ipynb` |
| `upstream/` | Created by step 1 below. Git-ignored. |

## What the patch changes

1. `tensorflow` is imported as `tensorflow.compat.v1` with `tf.disable_v2_behavior()` (the code targets TensorFlow 1).
2. `tf.contrib.rnn.BasicLSTMCell` becomes `tf.nn.rnn_cell.BasicLSTMCell` (`tf.contrib` no longer exists).
3. `rank_lstm.py` gets `--save_emb <path>`: after training it exports the sequential embedding for every date and
   stock to a `.npy` file. `relation_rank_lstm.py` needs this file, and the authors' repository does not ship it
   (its README links a Google Drive file instead).
4. Both scripts get `--epochs` (default 50); `relation_rank_lstm.py` also gets `--seed` (default 123456789, the
   original value).

## Reproduce

Environment used: Windows 11, CPU only, Python 3.12.10.

```bash
# from replicating-a-paper/coding/rsr/
# 1. authors' code at the exact commit, then our patch
git clone https://github.com/fulifeng/Temporal_Relational_Stock_Ranking upstream
git -C upstream checkout cfbb01b
git -C upstream apply ../rsr-compat.patch

# 1b. the industry-relation files ship upstream as a tarball (7 MB; several GB once extracted)
(cd upstream/data && tar zxvf relation.tar.gz)

# 2. environment
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt      # use .venv/bin/pip on macOS / Linux

# 3. run (from upstream/training). TF_USE_LEGACY_KERAS=1 is required.
cd upstream/training
export TF_USE_LEGACY_KERAS=1                       # cmd.exe: set TF_USE_LEGACY_KERAS=1

# baseline, and export the embedding that RSR needs
python rank_lstm.py -p ../data/2013-01-01 -m NASDAQ -t NASDAQ_tickers_qualify_dr-0.98_min-5_smooth.csv \
    -l 4 -u 32 --save_emb ../data/pretrain/NASDAQ_rank_lstm_seq-4_unit-32_0.npy

# RSR with the static industry-relation graph
python relation_rank_lstm.py -p ../data/2013-01-01 -m NASDAQ -l 4 -u 32 \
    -e NASDAQ_rank_lstm_seq-4_unit-32_0.npy -rn sector_industry --epochs 50
```

Output goes to the terminal; the runs in `../logs/` were captured the same way. The commands above are the
arguments recorded inside the logs `baseline_with_emb.log` and `rsr_train_50ep.log`. A 50-epoch run on all 1,026
NASDAQ stocks takes about 10 s per epoch for the baseline and about 35 s per epoch for RSR (CPU).

## Data

Everything ships with the authors' repository, under `upstream/data/`:

- `data/2013-01-01/` (about 200 MB): the processed daily features used by the paper;
- `data/relation.tar.gz` (7 MB): extract it (step 1b) to get `data/relation/`, the industry and Wikidata relation
  matrices. Extracted, the NASDAQ industry matrix alone is 817 MB and the NYSE one 2.6 GB;
- `data/google_finance/`: the raw 30-year files, which make the whole `data/` folder about 6 GB.

Nothing is copied into this repository, so `../../data/rawdata/` is empty on purpose. See
`../../data/rawdata/README.md`.

`../eda.ipynb` finds the data with `find_rsr_data()` in its first code cell: the `RSR_DATA` or `RSR_DATA_DIR`
environment variable, then `rsr/upstream/data`, then the local archive. It needs `data/2013-01-01/` and
`data/relation/sector_industry/NASDAQ_industry_relation.npy`.

## Known gaps

- **Seed-2 baseline is not reproducible from here.** `../logs/baseline_seed2*.log` record no arguments, and the
  patched `rank_lstm.py` has no seed option; the script version that produced them was not saved. The seed-2 RSR run
  (`rsr_seed2_50ep.log`) is reproducible: add `--seed 2` and `-e NASDAQ_rank_lstm_seq-4_unit-32_seed2.npy`.
- **No small sample data yet.** A full run needs the 200 MB processed data and the extracted relation files.
- **Dropped exploration.** `../logs/dynamic_*.log` come from a dynamic-relation extension that is no longer part of
  the project. Its scripts are not in this package.
