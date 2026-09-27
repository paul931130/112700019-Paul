# R1 簡報大綱（貼進 Canva 用）

課程範本：`專案/範本/20260921_ML_FinTech_Template.pdf`（Canva slides 範本）
內容來源：[R1.md](R1.md)

每個「---」代表一張投影片。條列式，貼進 Canva 後照排版調整即可，不用照抄整句。

---

## Slide 1：標題

**Does Relational Information Improve Stock Return Ranking?**
A Replication of Temporal Relational Ranking for Stock Prediction

- 你的姓名、學號
- 202609 ML & FinTech · Individual Project · R1

---

## Slide 2：背景問題

- 傳統股價預測：把每支股票當成獨立的時間序列（例如單純 LSTM）
- 但股票之間有真實的關聯——同產業、供應鏈、共同基金持股
- 這些關聯會讓股價連動：一家公司的衝擊常常也是整個群體的衝擊
- 把股票視為互相獨立的模型，設計上就看不到這個 channel

---

## Slide 3：複製的論文

**Feng, Fuli, et al. "Temporal Relational Ranking for Stock Prediction."**
*ACM Transactions on Information Systems* 37, no. 2 (2019): Article 27.

- 提出 Relational Stock Ranking (RSR)
- 用 Temporal Graph Convolution 把「產業關係」「Wikidata 關係」編碼進排序任務
- 目標：預測股票隔日報酬的**相對排名**（不是絕對報酬值）
- 排名比絕對值重要——因為 long-short / top-k 交易策略在乎的是相對順序

---

## Slide 4：為什麼選這篇（可行性）

- 期刊等級：交大資工 A 級期刊清單第 11 筆
- 官方程式碼可跑：本機已 clone、修補 TF1→TF2 相容性問題
- baseline (Rank_LSTM) 與 RSR (relation_rank_lstm) 都已訓練跑通、有完整結果
  （50 epochs，NASDAQ 全量 1,026 檔股票）

---

## Slide 5：為什麼選這篇（個人興趣）

- 我另外在做一個**交易/投資決策的多代理人（multi-agent）系統**
- 多個 agent 各自負責不同任務：技術面、消息面/情緒、風險控管
- 目前**缺少「股票間關聯」這一類訊號**——每個 agent 都是針對單一標的分析，
  彼此之間沒把「這支股票跟哪些股票連動」當成輸入
- RSR 示範了具體做法：關係圖 + 對其他股票表徵的注意力權重
- **本專案範圍**：只複製 RSR，驗證這種訊號在最基本任務上是否有用
  （不把它接進多代理人系統、不對架構做修改或延伸）

---

## Slide 6：研究問題

**RQ1（複製）**
關聯資訊（industry relation）是否真的能提升股票排名預測的表現，
相較於不用關聯的 baseline？

---

## Slide 7：預期貢獻

- 複製一個已發表的高品質結果，誠實檢驗原論文的結論在重跑之下是否成立
- 過程中排除的環境/資料問題本身也值得記錄：
  - TensorFlow 1→2 相容性（Keras 3 不支援舊版 API）
  - 資料缺值用 -1234 sentinel 而非 NaN
  - 關係圖裡混入 156 檔 ETF/基金（無真正產業關係）

---

## Slide 8：下一步（R2-R4 預告）

- R2：資料介紹、EDA
- R3：baseline vs. RSR 訓練結果、ablation
- R4：實證分析、與原論文對照、結論
