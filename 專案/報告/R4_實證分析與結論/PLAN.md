# R4 實證分析與結論 — 大綱

manuscript 對應章節：Results / Conclusion（真正評分依據是 Project 40% 的 LaTeX manuscript，
不是這個資料夾本身——見 `../../README.md`「真正的評分依據」一節）

## 結構

1. **複製結果是否成立**：R3 的 baseline vs RSR 比較，是否重現原論文「關係圖顯著提升排名表現」的結論
   （數字不用跟原論文完全一致，但方向要一致；不一致的話要討論可能原因：資料期間不同、超參數、隨機種子）。
2. **與原論文的比較**：方法、資料期間、市場範圍的差異，如何影響可比性。
3. **限制**：資料只到某個時間點、只在一維 ablation（有無關係圖）上做完整比較，industry vs wiki、
   NASDAQ vs NYSE 視時間決定要不要補。
4. **未來方向**：呼應 syllabus「Potentials of your projects」——若要延伸，可以往換不同關係圖來源、
   擴大到 wiki 關係與 NYSE 的方向走。

## 寫作提醒

- 每個結論都要能指回 R3 的一張表或一張圖，不要只下判斷句。

**完整草稿見 [R4.md](R4.md)**——已寫好。

## 待辦

- [x] 範圍已定案為單純複製（不做動態關聯延伸），已重寫 `../../manuscript/main.tex` §6 Discussion +
      §7 Conclusion，只討論 baseline vs RSR 的複製結果與原論文的對照。
- [ ] 動態關聯的探索紀錄（`../R3_模型與實驗設計/PROGRESS.md` 後半段）保留當附錄或不放進 manuscript，
      看時間決定。
- [ ] R4.md §2 列的三個候選原因（超參數、單次訓練、自己匯出的 embedding）還沒有逐一驗證，等
      R3 的穩健性檢查（換種子、超參數搜尋）做完後回來確認。
