# R1–R4 總體規劃

今天是 2026-09-27。四個里程碑都是「manuscript 對應章節 + 上台簡報」，內容寫進
`manuscript/main.tex`，投影片放 Canva，各自資料夾底下的 `PLAN.md`/`R{n}.md` 是草稿。
真正被評分的是 Project 40% 的 LaTeX manuscript（見 `README.md`「真正的評分依據」）。

## 時程總覽

| 里程碑 | 截止 | 剩餘天數 | manuscript 章節 | 狀態 |
|---|---|---|---|---|
| R1 主題與動機 | 10/05 23:59 | 8 天 | §1 Introduction | 內容完成，卡在 Overleaf/Canva/GitHub 連結 |
| R2 資料與EDA | 10/19 23:59 | 22 天 | §3 Data | EDA notebook 已有，PLAN 大綱待寫成 R2.md |
| R3 模型與實驗設計 | 11/09 23:59 | 43 天 | §4 Methods + §5 Results | 訓練結果已跑完，PLAN 待寫成 R3.md、穩健性檢查未做 |
| R4 實證分析與結論 | 11/30 23:59 | 64 天 | §6 Discussion + §7 Conclusion | R4.md 草稿已完成，待 R3 穩健性檢查回頭確認 |

## R1（10/05）— 剩下的是連結，不是內容

- [x] 內容：`報告/R1_主題與動機/R1.md`
- [x] manuscript §1 已同步
- [x] 投影片大綱：`報告/R1_主題與動機/R1_slides_outline.md`
- [x] 本機 git repo 已建立（`homework/`、`專案/` 已 commit）
- [ ] 你動手：GitHub repo 建立 + push（`202609-ML-FinTech-112700019-Paul`）
- [ ] 你動手：Overleaf 專案建立、分享給 `venteng@gmail.com`
- [ ] 你動手：Canva 投影片排版、分享給 `venteng@gmail.com`
- [ ] 三個連結填回 `專案/README.md`
- [ ] 論文全文 PDF 放進 `文獻_論文參考/`（目前是空的）

**這週的唯一任務就是上面三個「你動手」，內容不用再改。**

## R2（10/19）— 把 EDA 寫成文字

現況：`報告/R2_資料與EDA/eda.ipynb` 已經有分析（缺值 sentinel、ETF 混入等發現，已經被
manuscript §3 引用），但 R2 資料夾裡沒有像 R1.md/R4.md 那樣的文字草稿，只有 `PLAN.md` 大綱。

- [ ] 寫 `報告/R2_資料與EDA/R2.md`：把 `eda.ipynb` 的發現整理成文字（資料來源、規模、
      兩個資料品質問題），對應 manuscript §3 Data——**這部分 manuscript 其實已經寫好了**
      （因為 R3/R4 那次改稿時一併帶過），R2.md 主要是補一份給 R2 簡報用的獨立版本
- [ ] 投影片大綱（比照 R1_slides_outline.md 的格式）
- [ ] 確認 `eda.ipynb` 有沒有需要補的圖表（manuscript 目前用文字敘述缺值/ETF問題，沒有配圖）

## R3（11/09）— 內容夠了，缺穩健性檢查

現況：baseline vs. RSR 訓練結果已經跑完並記錄在 `PROGRESS.md`，manuscript §4/§5 已經照這個
結果寫好。`報告/R3_模型與實驗設計/` 目前也還沒有像 R1.md 那樣的獨立文字草稿。

- [ ] 寫 `報告/R3_模型與實驗設計/R3.md`：把 `PLAN.md` 的模型設定 + `PROGRESS.md` 的結果
      整理成一份對應 manuscript §4 Methods + §5 Results 的文字草稿
- [ ] 投影片大綱
- [ ] **穩健性檢查（R4.md §2 列的三個候選原因要靠這個驗證）**：
  - [ ] 換一個隨機種子，重跑 baseline 跟 RSR 的 50 epochs 訓練，確認 mrrt/btl 的分裂結果
        不是單次隨機性造成的
  - [ ] 做一次小範圍超參數搜尋（往原論文 `seq=16, unit=64` 的方向靠近），確認結果對超參數
        設定的敏感度
- [ ] 視時間決定要不要補 wiki 關係或 NYSE 的 ablation（非必須，manuscript 已把這個列為
      limitation，不做也不影響 R3 交付）

## R4（11/30）— 內容已寫好，等 R3 檢查回頭確認

- [x] `報告/R4_實證分析與結論/R4.md` 已完成
- [x] manuscript §6 Discussion + §7 Conclusion 已同步
- [ ] R3 的穩健性檢查做完後，回來確認 R4.md §2 的三個候選原因討論還站不站得住，
      如果換種子後 mrrt/btl 的分裂結果消失或反轉，§6/§7 要跟著改
- [ ] 投影片大綱

## 建議的推進順序

1. **這週先把 R1 剩下的三個連結搞定**（GitHub push、Overleaf、Canva）——內容已經沒問題，
   不要再花時間在 R1 的文字上。
2. 有空檔就先做 R3 的穩健性檢查（換種子、超參數搜尋），因為 R4 的結論品質直接依賴這個，
   越早做完，R4 反覆修改的風險越低。
3. R2.md、R3.md 這兩份「補文字草稿」的優先度最低——manuscript 該有的內容已經在
   §3/§4/§5 裡了，R2.md/R3.md 主要是為了 R2/R4 milestone 上台簡報用，離截止日還有時間，
   不急著現在寫。
