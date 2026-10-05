# R3 Progress Log

This log records what was actually run, what failed, and what was fixed, as compared with `PLAN.md`. The reported numbers are execution results, not estimates. The dynamic-relation experiments below are retained as historical exploration; the final project scope is a straight replication.

## Environment Issue (Identified and Fixed)

The project README originally said the baseline RankLSTM had been verified, but a rerun in the current environment failed:

```
AttributeError: `BasicLSTMCell` is not available with Keras 3.
```

The virtual environment's TensorFlow version uses Keras 3 by default, while `rank_lstm.py` and `relation_rank_lstm.py` rely on the older `tf.compat.v1.nn.rnn_cell.BasicLSTMCell` API, which Keras 3 does not support.

**Fix:** Set the `TF_USE_LEGACY_KERAS=1` environment variable before running training. This makes `tf.keras` use Keras 2 via the installed `tf_keras` package. The baseline trains successfully with this variable; include it in every training command.

## Second Environment Issue: RSR Needs an Embedding File

During initialization, `relation_rank_lstm.py` reads `data/pretrain/<emb_fname>.npy`, a trained sequential embedding. The official repository does not include this file; its README points to an embedding on Google Drive, posted in 2019. The link has not been checked.

**Approach:** Rather than depend on an external file of uncertain availability, modify `training/rank_lstm.py` to use the final weights to calculate and save the sequence embedding for each date and stock after baseline training. This adds the `--save_emb <path>` option. It was verified on a 30-stock sample: output shape `(30, 1245, 16)`, with values at 1241 of 1245 time points, matching the offset range in `get_batch`.

## Runs Completed

| Item | Command/configuration | Status |
|---|---|---|
| Full baseline training (NASDAQ, 1,026 stocks, 50 epochs) | `TF_USE_LEGACY_KERAS=1 python rank_lstm.py -p ../data/2013-01-01 -m NASDAQ -l 4 -u 32` | Completed; about 10 seconds per epoch; see `baseline_train.log` |
| Sequence-embedding export (30-stock sample) | Same command plus `--save_emb` | Completed; output shape verified |
| Dynamic-relation graph generator (30-stock sample) | `python preprocess/dynamic_relation.py -t data/NASDAQ_smoke_test_30.csv -w 60` | Completed; 21 rolling windows |

## Dynamic Relations: Initial Evidence (30 Stocks, 21 60-Day Windows)

The new `preprocess/dynamic_relation.py` script computes rolling 60-day return-correlation matrices and thresholds them to binary graphs using `|corr| > 0.5`. It outputs the same `(n, n, 1)` shape as `_industry_relation.npy`, which can be loaded by the existing `load_relation_data` function.

**Edge density (the proportion of linked stock pairs) ranged from 4.6% to 33.8% across the 21 windows**, a sevenfold range. This is initial evidence for the hypothesis that cross-stock relation strength changes over time rather than remaining fixed. The initial plan was to run this on all stocks and compare a dynamic-relation model with the static-graph model.

## Dynamic Relations: Full-Sample Graphs (NASDAQ, 1,026 Stocks, 21 Windows)

On all 1,026 stocks, the 21 windows had edge density from **3.6% to 22.5%**. This is consistent with the small-sample finding, with a somewhat narrower range: relation strength also changes substantially at full scale.

## Dynamic-Relation Model

The experimental `dynamic_relation_rank_lstm.py` replaces the relation graph in `relation_rank_lstm.py` from a fixed `tf.constant` to a `tf.placeholder`. At each training offset, it supplies the relation matrix for the corresponding 60-day window. The rest of the architecture, loss, and evaluation match `relation_rank_lstm.py` so the comparison isolates changes in the graph over time. The complete 50-epoch run was verified on a 30-stock sample.

## Three-Model Comparison (10 Epochs)

The full RSR run at 1,026 stocks processes a 1,026-by-1,026 relation matrix each epoch and takes about 35 seconds per epoch. To make a three-model comparison feasible, all three models were run for **10 epochs** using the same embedding; an `--epochs` option was added to the scripts.

| Model | Relation graph | Test MSE | Test mrrt | Test btl | Seconds/epoch |
|---|---|---:|---:|---:|---:|
| Baseline (Rank_LSTM) | None | 0.0004701 | 0.0377 | 0.672 | ~9.5 |
| RSR | Static industry graph | **0.0003966** | 0.0416 | 0.476 | ~35.5 |
| Dynamic relations | 60-day rolling correlations | 0.0004073 | **0.0475** | **0.869** | ~12.6 |

**The apparent advantage at 10 epochs was later contradicted by the full run.** At 10 epochs, RSR had the lowest MSE, while dynamic relations had the best mrrt and btl. That suggested a neat story in which the fixed graph predicted values better and the dynamic graph ranked stocks better. The story did not hold after 50 epochs.

## Final Three-Model Comparison (50 Epochs)

NASDAQ, 1,026 stocks, `seq=4`, `unit=32`, same embedding, CPU:

| Model | Relation graph | Test MSE | Test mrrt | Test btl |
|---|---|---:|---:|---:|
| Baseline (Rank_LSTM) | None | 0.0003774 | **0.0488** | 1.018 |
| RSR (replication target) | Static industry graph | 0.0003774 (tied) | 0.0276 | **1.130** |
| Dynamic relations (exploratory extension) | 60-day rolling correlations | 0.0003778 | 0.0288 | 0.861 |

After 50 epochs, the results differ from the 10-epoch comparison:

- **MSE is nearly tied across all three models.** Baseline and RSR are identical to seven decimal places (0.0003774); the dynamic model is close (0.0003778). Under this setup, adding a graph made little difference to MSE.
- **The baseline without a relation graph has the highest mrrt** (0.0488). RSR and the dynamic model are roughly half as high (0.0276 and 0.0288). The dynamic model's 10-epoch advantage disappeared after training longer.
- **Static-graph RSR has the highest btl** (1.130). The dynamic model is lowest (0.861), opposite the initial hypothesis.
- **Interpretation at this stage:** The 60-day rolling Pearson correlation graph, thresholded at `|corr| > 0.5`, did not support RQ2 after full training. The 10-epoch advantage appears to have been a pre-convergence artifact. Candidate explanations included noisy rolling correlations and an arbitrary threshold, window boundaries that did not align with the train/validation/test split, and the possibility that the static industry graph was already sufficient at this scale.

## Robustness Check 1: Aligning the 60-Day Windows to Split Boundaries

The dynamic graph script was changed so windows are formed separately within the train (days 0–755), validation (756–1007), and test (1008–1245) periods, preventing any window from crossing a validation/test boundary. The script writes `NASDAQ_boundaries.json` with each window's date range. The model uses this file and binary search to select a graph for each offset instead of assuming windows start uniformly at day zero via `offset // window_days`.

The full dataset produced 22 windows (one more than before because each split has its own remainder), with edge density from 3.3% to 20.6%. This remained consistent with the earlier finding that relation strength changes over time.

**The aligned-window, 50-epoch result changed:**

| Model | Test MSE | Test mrrt | Test btl |
|---|---:|---:|---:|
| Baseline (Rank_LSTM) | 0.0003774 | 0.0488 | 1.018 |
| RSR (static relation graph) | 0.0003774 | 0.0276 | 1.130 |
| Dynamic relations (unaligned windows, earlier version) | 0.0003778 | 0.0288 | 0.861 |
| **Dynamic relations (aligned windows)** | 0.0003776 | 0.0311 | **1.214** |

After alignment, dynamic-model btl moved from the lowest result (0.861) to the highest (1.214), and mrrt rose from 0.0288 to 0.0311, though it remained below the baseline's 0.0488. MSE barely changed. This supports the candidate explanation that the train/validation/test boundary misalignment was one real cause of the earlier reduction in performance.

The revised exploratory interpretation was that dynamic relations outperformed the static graph and baseline on **simulated return (btl)**, but still trailed the baseline on **ranking accuracy (mrrt)**. This may indicate that the dynamic graph helps select high-return stocks for a top-ranked strategy without improving the full ranking order.

## Remaining Checks

- [ ] Repeat the same experiment with another random seed to see whether the 50-epoch direction is stable.
- [ ] Try other rolling-window lengths and thresholds, or use DTW similarity instead of Pearson correlation, to test whether the btl result is robust to the graph-construction method.
- [ ] Analyze why dynamic relations may improve btl while reducing mrrt; the two metrics reward different outcomes and may merit separate discussion in R4.
