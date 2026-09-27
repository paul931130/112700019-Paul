# R1 投影片內容（貼進 Canva 模板用）

模板連結：https://www.canva.com/design/DAHROU_9H8o/1YNOqtDbEHpyRx1HwdCgMA/edit
（`20260920-template-ML&FinTech`，共 6 頁：標題、R1、R2、R3、R4、結尾，整學期共用同一份）

這次 R1 milestone 只需要填**頁 1（標題）**跟**頁 2（R1）**，R2/R3/R4 那三頁等各自 milestone
再回來填（頁 4、5 的範例已經有現成格式可以參考：3 條 bullet + 一張圖/公式）。

---

## 頁 1：標題頁

原文字 → 換成：

- `Replicating the paper: ?` → **Replicating the paper: Temporal Relational Ranking for Stock Prediction**
- `NAME?` → **Paul (112700019)**
- 下面兩行 affiliation 保留原樣（Department of Information Management and Finance 那兩行），
  除非你的系所跟範本不同再改

---

## 頁 2：R1 — Motivation and Why this topic interests you

原本的公式（Realized Volatility 範例）整塊換掉，改成 3 條 bullet（跟頁 4、5 的排版風格一致）：

- **Stocks are not independent** — industry, supply-chain, and shared-fund ties make returns
  move together, but standard models (e.g. plain LSTM) treat each stock as its own isolated
  time series
- **Feng et al. (2019), Relational Stock Ranking (RSR)** — encodes an industry/Wikidata relation
  graph into a Temporal Graph Convolution, ranking stocks by next-day return instead of
  regressing the value directly
- **Personal connection** — I'm separately building a multi-agent trading/investment system;
  every agent currently analyzes one stock in isolation, with no agent modeling cross-stock
  relations. RSR is a concrete way to turn that relation into a model input, which is why I'm
  replicating it first before considering any downstream use

頁尾左下角原本寫 `Volatility` 的標籤，改成：**RSR** 或 **Relational Stock Ranking**

（右下角那個小圖示是裝飾用的箭頭/走勢圖，不用改，跟你的主題也搭）

---

## 之後 R2/R3/R4 要填的頁（先不用動，留給之後的 milestone）

- 頁 3（R2 Data）：`報告/R2_資料與EDA/` 做完 R2.md 後再回來填
- 頁 4（R3 Methods/Results）：`報告/R3_模型與實驗設計/PROGRESS.md` 的模型比較表
- 頁 5（R4 結論）：`報告/R4_實證分析與結論/R4.md` 已經寫好，屆時直接濃縮成 3 條 bullet
