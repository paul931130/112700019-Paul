# R3 進度紀錄

跟 `PLAN.md` 對照著看——這份記錄實際跑過什麼、卡在哪、修了什麼，數字都是真的執行結果，不是預估。

## 環境問題（新發現，已修好）

`專案/README.md` 原本寫「baseline RankLSTM 已實測跑通」，但這次重新跑發現**現在的環境跑不動**：

```
AttributeError: `BasicLSTMCell` is not available with Keras 3.
```

原因：venv 裡的 TensorFlow 版本預設用 Keras 3，但 `rank_lstm.py` / `relation_rank_lstm.py` 用的是
`tf.compat.v1.nn.rnn_cell.BasicLSTMCell` 這種舊版 API，Keras 3 底下不支援。

**修法**：執行指令前加環境變數 `TF_USE_LEGACY_KERAS=1`，讓 `tf.keras` 走舊版 Keras 2（`tf_keras` 套件，
venv 裡已經有裝，只是沒被啟用）。加了之後 baseline 可以正常訓練。以後所有訓練指令都要帶這個環境變數：

```bash
TF_USE_LEGACY_KERAS=1 python rank_lstm.py -p ../data/2013-01-01 -m NASDAQ -l 4 -u 32
```

## 第二個環境問題：RSR（`relation_rank_lstm.py`）少一個檔案

`relation_rank_lstm.py` 初始化時會讀 `data/pretrain/<emb_fname>.npy`（訓練好的序列 embedding），
但這個檔案**官方 repo 沒有附**，README 只說「下載一份預訓練好的 embedding」（Google Drive 連結，
2019 年放的，沒去試連結還有沒有效）。

**做法**：與其依賴一個來源不明、可能失效的外部檔案，直接修改 `training/rank_lstm.py`，讓它在
baseline 訓練完之後，用最終權重把每一天、每支股票的序列 embedding 都算出來並存檔（新增
`--save_emb <path>` 參數）。已經在 30 檔股票的小樣本上驗證過：輸出 shape `(30, 1245, 16)`，
1241/1245 個時間點有值（跟 `get_batch` 的 offset 範圍精確對上，見 `rank_lstm.py` 裡的邏輯）。

## 目前跑過的東西

| 項目 | 指令 | 狀態 |
|---|---|---|
| Baseline 全量訓練（NASDAQ，1026 檔，50 epochs） | `TF_USE_LEGACY_KERAS=1 python rank_lstm.py -p ../data/2013-01-01 -m NASDAQ -l 4 -u 32` | ✅ 已完成，~10 秒/epoch，見 `baseline_train.log` |
| 序列 embedding 匯出（30 檔小樣本，驗證用） | 同上 + `--save_emb` | ✅ 已完成，shape 正確 |
| 動態關聯圖產生器（30 檔小樣本，驗證用） | `python preprocess/dynamic_relation.py -t data/NASDAQ_smoke_test_30.csv -w 60` | ✅ 已完成，21 個 60 天窗口 |

## 動態關聯：初步證據（30 檔股票，21 個 60 天窗口）

`preprocess/dynamic_relation.py`（新寫的腳本，`../../README.md` 延伸方向的實作）用滾動 60 天窗口算
報酬相關係數矩陣、`|corr| > 0.5` 二值化成關係圖，輸出格式跟原本 `_industry_relation.npy` 一樣
`(n, n, 1)`，可以直接餵給 `relation_rank_lstm.py` 現有的 `load_relation_data`。

**邊密度（有連結的股票對比例）在 21 個窗口間從 4.6% 跳到 33.8%（7 倍差距）**——這是本專案要驗證的
假設的第一個直接證據：股票間的關聯強度真的隨時間大幅變動，不是 RSR 論文假設的固定常數。下一步是把
這個腳本跑在全量股票上，並實際訓練「動態關聯版」的 `relation_rank_lstm.py` 跟固定關係圖版比較。

## Baseline 全量結果（NASDAQ，1026 檔，seq=4，unit=32，50 epochs，CPU）

```
Best Valid performance: {'mse': 0.0004948, 'mrrt': 0.02797, 'btl': 2.5018}
Best Test  performance: {'mse': 0.0003774, 'mrrt': 0.04878, 'btl': 1.0184}
```

- `mse`：預測報酬與真實報酬的均方誤差。
- `mrrt`：Mean Reciprocal Rank of correct Top-1（排名指標，越高代表模型排出的第一名越常是真的漲最多）。
- `btl`：Back-Testing Long strategy 的模擬報酬（買進模型排名最前的股票）。

這是複製論文表 3 的 baseline 對照組（原論文的 Rank_LSTM baseline 是拿來跟 RSR 比較用的下限）。

## 動態關聯：全量結果（NASDAQ，1026 檔，21 個 60 天窗口）

`preprocess/dynamic_relation.py` 跑在全量 1026 檔股票上：邊密度在 21 個窗口間從 **3.6% 到 22.5%**
（跟 30 檔小樣本的結論一致，數字略溫和一點）——確認全量規模下，關聯強度一樣隨時間大幅變動，不是
固定常數。

## `dynamic_relation_rank_lstm.py`（新腳本，動態關聯版模型）

把 `relation_rank_lstm.py` 的關係圖從 `tf.constant`（訓練全程寫死一個關係矩陣）改成
`tf.placeholder`，每個訓練 offset 依日期落在哪個 60 天窗口，餵不同的關係矩陣進去。除了這一點，
架構、loss、evaluation 完全跟 `relation_rank_lstm.py` 一樣，這樣效能差異才單純反映「關係圖會不會
隨時間變」，不會混進其他架構差異。30 檔小樣本上驗證過完整跑得動、50 epochs 無錯誤。

## 三組模型比較（NASDAQ，1026 檔，seq=4，unit=32，10 epochs，同一個 embedding，CPU）

RSR 全量訓練原本設定 50 epochs 太慢（每 epoch 要處理 1026×1026 的關係矩陣，~35 秒/epoch，50 epochs
等於要等快半小時），改成三個模型都跑 **10 epochs** 做公平比較，幫 `rank_lstm.py` /
`relation_rank_lstm.py` / `dynamic_relation_rank_lstm.py` 都加了 `--epochs` 參數。

| 模型 | 關係圖 | Test MSE | Test mrrt | Test btl | 秒/epoch |
|---|---|---|---|---|---|
| Baseline (Rank_LSTM) | 無 | 0.0004701 | 0.0377 | 0.672 | ~9.5 |
| RSR（複製目標） | 固定 industry 關係圖 | **0.0003966** | 0.0416 | 0.476 | ~35.5 |
| 動態關聯（本專案延伸） | 60 天滾動窗口相關係數 | 0.0004073 | **0.0475** | **0.869** | ~12.6 |

**10-epoch 當下的解讀**（已被下面完整訓練的結果推翻，留著當對照）：MSE 上固定 RSR 略贏，但 mrrt、
btl 這兩個更貼近實際交易目標的指標，動態關聯版都是三組裡最高的——看起來像是「固定關係圖猜得準數值，
動態關聯圖排得對順序」的漂亮故事。**這個故事在練滿 50 epochs 之後不成立**，見下。

## 三組模型最終比較（NASDAQ，1026 檔，seq=4，unit=32，**50 epochs**，同一個 embedding，CPU）

| 模型 | 關係圖 | Test MSE | Test mrrt | Test btl |
|---|---|---|---|---|
| Baseline (Rank_LSTM) | 無 | 0.0003774 | **0.0488** | 1.018 |
| RSR（複製目標） | 固定 industry 關係圖 | 0.0003774（打平） | 0.0276 | **1.130** |
| 動態關聯（本專案延伸） | 60 天滾動窗口相關係數 | 0.0003778 | 0.0288 | 0.861 |

**訓練滿 50 epochs、收斂之後，方向跟 10-epoch 版完全不一樣**：

- **MSE 幾乎三組打平**——baseline 跟 RSR 到小數點後七位都一樣（0.0003774），動態版只差一點點
  （0.0003778）。收斂後，有沒有關係圖對 MSE 這個指標幾乎沒有差別，RQ1「關係資訊能提升 MSE」在這個
  設定下**不成立**。
- **mrrt 反過來是沒有關係圖的 baseline 最高**（0.0488），RSR 跟動態版都掉到一半左右（0.0276、
  0.0288）。10-epoch 時動態版 mrrt 最高（0.0475）那個結果，在收斂後完全消失。
- **btl 是固定關係圖的 RSR 最高**（1.130），動態版反而是三組裡最低（0.861）。這跟原本假設的方向
  （動態關聯應該更好）相反。
- **結論（誠實版）**：這次的動態關聯做法（60 天滾動 Pearson 相關係數、`|corr|>0.5` 二值化）在完整
  訓練後，**沒有支持 RQ2**。10-epoch 時看到的優勢是訓練還沒收斂時的雜訊，不是真實效果。這本身是一個
  可以寫進 R4 的合理發現——可能的原因：(a) 滾動相關係數雜訊太大，二值化閾值 0.5 太隨意；(b) 60 天
  窗口跟訓練的 date-split 對不齊，導致同一個關係圖被用在橫跨 valid/test 邊界的日期上；(c) 這個資料
  集規模下，固定的產業關係本來就已經接近「夠用」，動態版增加的雜訊蓋過了它增加的訊息量。

## 穩健性檢查 #1：對齊 60 天窗口邊界（候選解釋 (b)，已驗證是真的）

`dynamic_relation.py` 改成 split-aligned 版：窗口不再從第 0 天均勻切，而是分別在
train（0–755）、valid（756–1007）、test（1008–1245）三段內各自切 60 天窗口，任何一個窗口都不會
橫跨 valid/test 邊界。同時輸出 `NASDAQ_boundaries.json` 記錄每個窗口的實際日期範圍，
`dynamic_relation_rank_lstm.py` 也改用這個檔案（`bisect` 查表）決定每個訓練 offset 該用哪個窗口的
關係圖，不再用 `offset // window_days` 這種假設窗口從第 0 天均勻排列的算法。

全量重新產生：22 個窗口（原本 21 個，因為三段各自切多出來的零頭），邊密度 3.3%～20.6%，跟未對齊版
結論一致（關聯強度還是大幅變動）。

**重跑 50 epochs 的結果，對齊窗口之後確實變了**：

| 模型 | Test MSE | Test mrrt | Test btl |
|---|---|---|---|
| Baseline | 0.0003774 | **0.0488** | 1.018 |
| RSR（固定關係圖） | 0.0003774 | 0.0276 | 1.130 |
| 動態關聯（窗口未對齊，舊版） | 0.0003778 | 0.0288 | 0.861 |
| **動態關聯（窗口對齊後，新版）** | 0.0003776 | 0.0311 | **1.214** |

對齊之後,動態版的 **btl 從三組最低（0.861）變成三組最高（1.214）**,mrrt 也從 0.0288 進步到
0.0311（但仍低於 baseline 的 0.0488）,MSE 幾乎沒變。**候選解釋 (b) 得到證實**：窗口沒對齊
valid/test 切分確實是壓低動態版表現的真實原因之一,不是無關緊要的細節。

修正後的結論：動態關聯在**模擬報酬（btl）**上明顯優於固定關係圖和 baseline,但在**排名準確度
（mrrt）**上仍然不如沒有關係圖的 baseline——這是一個比之前「動態關聯全面較差」更細緻、也更有趣的
故事:動態關係圖可能學到了「何時該重壓哪支股票」（影響 btl 這種依賴排名前幾名的策略型指標）,但沒有
學到「精確排出完整順序」（mrrt 要求的是最頂端那一名要對）。

## 還沒做的

- [ ] 拿同一組結果重複第二次（換個隨機種子）確認上面 50-epoch 的方向不是單次隨機性造成的
- [ ] 試試看不同的滾動窗口長度、threshold，或用 DTW 相似度取代 Pearson 相關係數，確認 btl 優勢對做法穩不穩健
- [ ] 深入分析為什麼動態版 btl 贏、mrrt 卻輸——這兩個指標為什麼會不一致，值得在 R4 額外討論一段
