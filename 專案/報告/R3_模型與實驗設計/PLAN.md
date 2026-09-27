# R3 模型與實驗設計 — 大綱

manuscript 對應章節：Methods / Experiments（真正評分依據是 Project 40% 的 LaTeX manuscript，
不是這個資料夾本身——見 `../../README.md`「真正的評分依據」一節）

## 模型設定（兩組，純複製）

| # | 模型 | 關係圖 | 腳本 | 現況 |
|---|---|---|---|---|
| 1 | Baseline | 無 | `training/rank_lstm.py`（`Temporal_Relational_Stock_Ranking`） | 已跑通 |
| 2 | 複製目標 RSR | 固定 industry / wiki 關係圖 + Temporal Graph Convolution | `training/relation_rank_lstm.py` | 已跑通，50 epochs 全量結果見 `PROGRESS.md` |

> 註：`PROGRESS.md` 裡還留著一組「動態關聯」的探索紀錄（滾動窗口相關係數，逐期重估關係圖）——已決定
> 不放進最終 manuscript，範圍就是單純複製上面兩組模型。相關程式碼、log 檔案先保留，不用刪。

## Ablation 設計（沿用原論文）

- 有無關係圖（baseline vs RSR）
- industry 關係 vs wiki 關係（`-rn` 參數：`sector_industry` / `wikidata`）
- NASDAQ vs NYSE

先把 NASDAQ + industry 關係這組做完整、跑出穩定數字，再視時間決定要不要擴大到 wiki 關係或 NYSE。

## 評估指標

沿用 `training/evaluator.py` 裡的指標（論文常用 MRR 排名指標 + IRR 投資報酬模擬）。兩組模型、
每個 ablation 設定都要跑出同一組指標，才能放進同一張比較表。

## 待辦

- [x] 訓練 baseline 與 RSR，把 loss/指標記錄下來（50 epochs 全量結果見 `PROGRESS.md`）
- [ ] 視時間決定是否擴大到 wiki 關係或 NYSE 的 ablation
- [ ] 把兩組模型的比較表整理成 R3 報告的主表，對照原論文表 3
