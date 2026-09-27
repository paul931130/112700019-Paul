# 機器學習與金融科技 — 期末專題

## 複製論文 (Replicating a High-Quality Paper)

Feng, Fuli, Xiangnan He, Xiang Wang, Cheng Luo, Yiqun Liu, and Tat-Seng Chua. "Temporal Relational Ranking for Stock Prediction." *ACM Transactions on Information Systems* 37, no. 2 (2019): Article 27. https://doi.org/10.1145/3309547.

- 期刊等級：交大資工 A 級期刊清單（`共用參考資料` 或課程 GitHub `journal-ranking/交大資工A級期刊_20200910Updated.xlsx` 第 11 筆）
- 官方程式碼：https://github.com/fulifeng/Temporal_Relational_Stock_Ranking
- 本機複製環境：`../Temporal_Relational_Stock_Ranking`（已 clone、已修補 TF1→TF2 相容性、venv 已建立、baseline RankLSTM 已實測跑通）
- **跑訓練指令前務必加 `TF_USE_LEGACY_KERAS=1`**（例如
  `TF_USE_LEGACY_KERAS=1 python rank_lstm.py -p ../data/2013-01-01 -m NASDAQ -l 4 -u 32`），
  不然會在 `BasicLSTMCell` 那行噴 `AttributeError: BasicLSTMCell is not available with Keras 3`。
  細節見 `報告/R3_模型與實驗設計/PROGRESS.md`。

## 論文摘要與方法

提出 Relational Stock Ranking (RSR) 模型與 Temporal Graph Convolution，將股票間的關係（產業關係、Wikidata 關係）以「時間敏感」的方式編碼進排序任務，用於預測股票隔日報酬排名，取代過去把股票視為互相獨立個體的做法。

## 真正的評分依據（以 syllabus + 官方 GitHub 為準）

`報告/R1~R4` 底下原本寫「對應評分表項目」，那張評分表查無出處——兩份 syllabus
（`slides/20260907-Ch00-Syllabus.pdf`、`slides/20260914-Ch00-Syllabus.pdf`）和官方 GitHub
（`202609-ML-FinTech/00-course-info`，2026-09-14 用 GitHub API 直接查證）都沒有這張表，也沒有任何
「R1/R2/R3/R4 分節評分」的說法。以下是查證過的真實依據：

**Grading policy**（`20260907-Ch00-Syllabus.pdf` p.6）：

| 項目 | % | 內容 |
|---|---|---|
| Participation | 20% | 課堂練習、簡報（project/MFS/HW）、課堂總結，會 cold call |
| **Project** | **40%** | **根據 manuscript（LaTeX 撰寫）評分**，另需準備簡報用的 slides |
| Exam | 40% | 課堂考，可帶一張 A4 雙面小抄 |

**你的個人 repo 結構**（同上 p.5）：

```
202609-ML-FinTech-<studentID>-<nickname>/
├── HW/
└── Project/   ← README.md, logs, snapshots, data and codes
```

**Project 的 README.md 要包含**（p.10 "Your GitHub Repo"）：GitHub 頁面連結、Chicago style 引用複製的
論文、Overleaf manuscript 連結、Canva slides 連結、"Code"（Jupyter Notebook）、"Data"（資料集或連結）。

**真正被評分的是 Project 40% 那份 LaTeX manuscript**，不是這個資料夾本身。`報告/R1~R4` 底下的內容
（動機、EDA、模型實驗、結論）都還是 manuscript 需要的真材料，只是拿掉了它們「各自佔幾 % 評分表」的
錯誤框架——四個資料夾現在當成寫 manuscript 前的草稿分節就好：

| 資料夾 | manuscript 對應章節 | 內容 |
|---|---|---|
| `報告/R1_主題與動機` | Introduction / Motivation | 論文介紹、為何選這篇、RQ1/RQ2 |
| `報告/R2_資料與EDA` | Data | 原始資料說明、EDA notebook（`eda.ipynb`） |
| `報告/R3_模型與實驗設計` | Methods / Experiments | Baseline (Rank_LSTM) vs. RSR，含 ablation（有無關係圖、industry vs wiki） |
| `報告/R4_實證分析與結論` | Results / Conclusion | 結果解讀、與原論文比較、延伸討論 |
| `文獻_論文參考` | References | 複製論文全文、相關文獻筆記 |
| `程式碼` | — | 指向 `../Temporal_Relational_Stock_Ranking`，或放置整理過的 Jupyter Notebook 版本 |
| `資料` | — | 資料集或資料連結說明 |

## 範圍（已定案）：單純複製論文，不做延伸

原本考慮加一組「動態跨股票關聯」的延伸實驗（見 `報告/R3_模型與實驗設計/PROGRESS.md` 裡的探索紀錄），
但已決定**不做**——本專案就是單純複製 Feng et al. (2019) 的 RSR，不加新方法。動態關聯相關的程式碼
（`preprocess/dynamic_relation.py`、`training/dynamic_relation_rank_lstm.py`）與 log 檔案先保留在原地，
當作探索過程留存，但不會出現在最終 manuscript 的結論裡。

## 資料

- **Sequential Data**：NASDAQ/NYSE 逾 8,000 檔股票 30 年歷史日線資料（open, high, low, close, volume），來源 Google Finance，論文使用 2013-01-01 起的處理後版本
- **Industry Relation**：NASDAQ/NYSE 股票的產業關係（sector/industry）
- **Wiki Relation**：從 Wikidata 抽取的公司關係
- 資料已隨官方 repo 提供，路徑：`../Temporal_Relational_Stock_Ranking/data/`

## Code

Python，Jupyter Notebook（README 要求交 Jupyter Notebook，原始訓練腳本為 `.py`，另外整理成 `.ipynb`）：
- `training/rank_lstm.py`：Baseline，Rank_LSTM（不含關係圖）
- `training/relation_rank_lstm.py`：完整模型，Relational Stock Ranking (RSR)

## Manuscript / Slides

- Overleaf：（待補連結，分享至 venteng@gmail.com）
- Canva Slides：（待補連結，分享至 venteng@gmail.com）

## GitHub

（待補：學生自己的 GitHub 頁面連結）
