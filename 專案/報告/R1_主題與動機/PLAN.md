# R1 主題與動機 — 大綱

manuscript 對應章節：Introduction / Motivation（真正評分依據是 Project 40% 的 LaTeX manuscript，
不是這個資料夾本身——見 `../../README.md`「真正的評分依據」一節）

## 結構（建議 1.5–2 頁）

1. **背景問題**：傳統股價預測把每支股票當成互相獨立的時間序列（如單純的 LSTM），但股票之間存在真實的關聯
   （同產業、供應鏈、共同基金持股），這些關聯會影響股價連動。
2. **論文與方法**：Feng et al. (2019), *Temporal Relational Ranking for Stock Prediction* (RSR)。
   一句話講清楚它做了什麼：用 Temporal Graph Convolution 把「產業關係」與「Wikidata 關係」以時間敏感的方式
   編碼進排序任務，取代把股票視為獨立個體的作法，目標是預測股票隔日報酬的相對排名。
3. **為什麼選這篇**：
   - 期刊等級：交大資工 A 級期刊清單第 11 筆（`journal-ranking/交大資工A級期刊_20200910Updated.xlsx`）。
   - 官方程式碼可跑（本機已 clone、TF1→TF2 修補、baseline 已跑通），複製的可行性高。
   - 與個人興趣的連結：我另外在做一個交易/投資決策的多代理人系統，目前缺少「股票間關聯」這類
     訊號，RSR 示範了把關聯轉成模型輸入的具體做法（詳見 `R1.md` §3）。
4. **研究問題（RQ）**：
   - RQ1（複製）：關聯資訊（industry / wiki）是否真的能提升股票排名預測的表現，相較於不用關聯的 baseline？
5. **預期貢獻**：複製一個已發表的高品質結果，確認原論文「關聯資訊能提升排名表現」的結論在重跑之下是否成立。

**完整草稿見 [R1.md](R1.md)**——已寫好，供改寫進 `../../manuscript/main.tex` §1 用。

## 素材來源

- `../../README.md`（本 README 已有摘要與方法段落，可直接改寫擴充）
- `../../../Temporal_Relational_Stock_Ranking/README.md`（官方摘要）
- 論文全文：放進 `../../文獻_論文參考/`（目前是空的，記得把 PDF 放進去）

## 待辦

- [x] 投影片：https://canva.link/psyac0w98zuyn5l（先用這份交件；備用連結、待老師開模板編輯
      權限後的切換計畫見 `../../README.md`）
- [x] 論文 PDF：`../../文獻_論文參考/feng2019-temporal-relational-ranking.pdf`
      （arXiv 1809.09441，作者自存檔版本，跟 ACM 正式版同一篇）
- [x] Overleaf：https://www.overleaf.com/read/fjkrqhnbqwgc#e5d02b（唯讀連結，
      記得確認 venteng@gmail.com 有被加進協作者，唯讀連結不算分享）
- [ ] 決定是否組隊 / 獨立完成，補上這段敘述
- [ ] GitHub repo push（本機已 commit，見 `../../PLAN-R1-R4.md`）
- [ ] 有空的話：跟老師/助教要模板的編輯權限，把簡報換成模板複本（非必要，內容已經到位）
