# Manuscript 骨架

給 Overleaf 用的章節骨架。對應 R1~R4 草稿資料夾 → manuscript 章節；`[R2]`/`[R3]` 這種標記指向
已經有真實內容可以直接搬過去的地方，不用重寫。

## Title

*Does the Relation, or Its Change Over Time, Predict Stock Returns? A Replication of
Temporal Relational Ranking with a Dynamic-Relation Extension*
（暫定，定稿前再調整）

## Abstract

一段（150–250 字）：問題 → 方法 → 主要發現。等 R3/R4 數字齊了再寫，是全文最後寫的部分。

## 1. Introduction

來源：`報告/R1_主題與動機/PLAN.md`，內容已經有草稿，只差潤成正式段落。

- 1.1 背景問題：為什麼股票不該被當獨立個體預測
- 1.2 本文複製的論文：Feng et al. (2019) RSR — 一段話講完核心方法
- 1.3 Research Questions：RQ1（複製）、RQ2（延伸：動態關聯）
- 1.4 Contribution 一句話總結

## 2. Related Work

新的一節，R1 PLAN.md 沒直接涵蓋，但素材已經在手上：

- RSR 之外的關係型股價預測方法：HGTAN（hypergraph）、GCNET（graph conv）——各一段，
  說明跟本文延伸方向（動態 vs. 靜態關係圖）的差異
- 從 `文獻_論文參考/related-literature-shortlist.md` 挑 2–4 篇（供應鏈關聯、跨市場資訊傳導）
  當作「為什麼關聯會隨時間變化」這個假設的外部支持

## 3. Data

`[R2]` 來源：`報告/R2_資料與EDA/eda.ipynb`，A1/A2/A3/B1 的發現直接改寫成敘述文字：

- 3.1 資料來源：NASDAQ 1,026 檔、`data/2013-01-01/`，1,246 個交易日（≈5 年，不是 README 說的 30 年）
- 3.2 關係圖：industry relation，156 檔（15%）為 ETF/基金、非個股，已排除
- 3.3 資料清理：`-1234` 缺值代碼、ETF 排除後的樣本數

## 4. Methods

`[R3]` 三個模型設定，來源：`報告/R3_模型與實驗設計/PROGRESS.md`：

- 4.1 Baseline：Rank_LSTM（無關係圖）
- 4.2 RSR：固定 industry 關係圖 + Temporal Graph Convolution（複製目標）
- 4.3 本文延伸：動態關聯——滾動窗口相關係數，逐窗口重估關係圖
  （`preprocess/dynamic_relation.py`，已驗證機制：邊密度隨窗口從 4.6% 變動到 33.8%）

## 5. Experiments and Results

- 5.1 評估指標：MSE、MRR-Top1、模擬報酬（`training/evaluator.py`）
- 5.2 Baseline 結果 `[R3 已有真數字]`：Test MSE 0.000377、mrrt 0.049、btl 1.02（NASDAQ 全量，50 epochs）
- 5.3 RSR 結果：**待補**（embedding 已匯出，`data/pretrain/NASDAQ_rank_lstm_seq-4_unit-32_0.npy`，
  差最後一次全量訓練）
- 5.4 動態關聯結果：**待補**（腳本可動，還沒接進 `relation_rank_lstm.py`、還沒全量跑）
- 5.5 Ablation 比較表：baseline / RSR / 動態，三欄同一組指標

## 6. Discussion

`[R4]` 來源：`報告/R4_實證分析與結論/PLAN.md` 的三種情境（動態明顯更好 / 沒差異 / 更差），
等 5.4 數字出來後選一種改寫：

- 6.1 複製是否成功：跟原論文方向是否一致
- 6.2 動態關聯的解讀：不管結果好壞都要講原因
- 6.3 與原論文的差異：資料期間、市場範圍
- 6.4 限制

## 7. Conclusion and Future Work

一段總結 + 呼應 syllabus「Potentials of your projects」：若動態關聯有效，下一步可以往
thesis/journal publication 延伸。

## References

Chicago style。`文獻_論文參考/` 底下的論文全部要列進來，主要複製論文用 Chicago 格式標明。

---

## 現在能寫的 vs. 還要等的

| 章節 | 現在能不能寫 |
|---|---|
| 1 Introduction | ✅ 能寫，素材齊了 |
| 2 Related Work | ✅ 能寫，素材齊了 |
| 3 Data | ✅ 能寫，`eda.ipynb` 內容直接改寫 |
| 4 Methods | ✅ 能寫，三個模型設定都定案了 |
| 5.2 Baseline 結果 | ✅ 能寫，真數字已經有 |
| 5.3 RSR 結果 | ⏳ 等全量訓練跑完 |
| 5.4 動態關聯結果 | ⏳ 等 `relation_rank_lstm.py` 接上動態關係圖 + 全量跑完 |
| 6 Discussion / 7 Conclusion | ⏳ 等 5.3、5.4 都有數字才能寫 |
| Abstract | ⏳ 全部寫完最後才寫 |
