# R2 資料與 EDA — 大綱

manuscript 對應章節：Data（真正評分依據是 Project 40% 的 LaTeX manuscript，不是這個資料夾本身——
見 `../../README.md`「真正的評分依據」一節）

## 資料說明（先寫清楚，EDA 才有依據）

| 資料 | 內容 | 路徑 |
|---|---|---|
| Sequential Data | NASDAQ/NYSE 逾 8,000 檔股票 30 年日線（open/high/low/close/volume），來源 Google Finance | `../../../Temporal_Relational_Stock_Ranking/data/google_finance/` |
| 處理後資料 | 論文實際使用版本，2013-01-01 起 | `../../../Temporal_Relational_Stock_Ranking/data/2013-01-01/` |
| Industry Relation | NASDAQ/NYSE 股票的產業關係（sector/industry），含原始檔與 `.npy` 編碼 | `.../data/sector_industry/` |
| Wiki Relation | 從 Wikidata 抽取的公司關係 | `.../data/wikidata/`（需先 `tar zxvf relation.tar.gz`） |

前處理腳本：`eod.py`（產生特徵）、`sector_industry.py`、`wikidata.py`（皆在
`../../../Temporal_Relational_Stock_Ranking/preprocess/`）。

## EDA notebook 要涵蓋的項目

1. **樣本規模**：實際使用的股票數（NASDAQ vs NYSE）、時間範圍、每檔股票的有效交易日數。
2. **價格與報酬分布**：收盤價、日報酬率的分布/離群值，是否需要做標準化（論文用 z-score）。
3. **關係圖的稀疏度**：industry 關係矩陣、wiki 關係矩陣各自的邊數、密度、每檔股票的平均連結數——
   這張圖後面會直接拿來對照「動態關聯」矩陣的稀疏度差異。
4. **缺值與交易日對齊**：不同股票的交易日是否對齊、缺值怎麼處理（論文用的填補方式）。
5. **（延伸用）滾動窗口相關係數初探**：抽幾檔股票，畫出 60 天滾動窗口報酬率相關係數隨時間變化的折線圖，
   直觀展示「關聯不是常數」——這張圖是 R3 動態關聯 ablation 的立論基礎，這裡先做探索性版本即可。

## 產出

- `eda.ipynb`（依 `../README.md` 的資料夾對照表，這是本節指定檔名）
- 圖表全部要能回答一個問題，不要只是 `describe()` 輸出（參考課程作業 0914 對 Q8(h) 的要求：
  **講一個可能有問題/有趣的發現，並附上支持它的圖**）

## 待辦

- [ ] 確認是否要換成台股資料（若換，需重做 sector_industry / wikidata 前處理，是目前最大的範圍變動）
- [ ] 跑一次 60 天滾動相關係數，確認資料量夠不夠支撐 R3 的動態關聯實驗
