# R1: Topic and Motivation — Outline

Corresponding manuscript section: Introduction / Motivation. The 40% Project grade is based on the LaTeX manuscript, not this folder; see the “What Is Actually Graded” section in `../../README.md`.

## Structure (recommended: 1.5–2 pages)

1. **Background:** Traditional stock forecasting treats each stock as an independent time series (for example, a standalone LSTM), even though stocks have real connections (shared industry, supply chains, and institutional ownership) that can influence co-movement.
2. **Paper and method:** Feng et al. (2019), *Temporal Relational Ranking for Stock Prediction* (RSR). In brief, Temporal Graph Convolution encodes industry and Wikidata relations into the ranking task in a time-sensitive way. The model predicts the relative ranking of next-day stock returns rather than treating each stock as independent.
3. **Why this paper:**
   - Journal tier: entry 11 on the NYCU CS A-tier journal list (`journal-ranking/交大資工A級期刊_20200910Updated.xlsx`).
   - The official code runs locally after a TF1-to-TF2 compatibility patch, and the baseline has run successfully, making a replication feasible.
   - Personal connection: I am also building a multi-agent system for trading and investment decisions. It currently lacks cross-stock relation signals; RSR shows a concrete way to turn relations into model inputs (see `R1.md`, section 3).
4. **Research question:**
   - RQ1 (replication): Does relational information (industry/Wikidata) improve stock-ranking prediction performance relative to a baseline without relations?
5. **Expected contribution:** Replicate a high-quality published result and check whether its conclusion—that relational information improves ranking performance—holds in a fresh run.

**See the full draft in [R1.md](R1.md)**. It is ready to adapt into `../../manuscript/main.tex`, section 1.

## Source Material

- `../../README.md` (project summary and method)
- `../../../Temporal_Relational_Stock_Ranking/README.md` (official summary)
- Full paper: `../../文獻_論文參考/feng2019-temporal-relational-ranking.pdf`

## To Do

- [x] Slides: https://canva.link/psyac0w98zuyn5l (use this for now; the backup link and template-switch plan are in `../../README.md`)
- [x] Paper PDF: `../../文獻_論文參考/feng2019-temporal-relational-ranking.pdf` (author-posted arXiv 1809.09441 version of the same paper as the ACM edition)
- [x] Overleaf: https://www.overleaf.com/read/fjkrqhnbqwgc#e5d02b (read-only link; make sure `venteng@gmail.com` is added as a collaborator—the read-only link alone does not count as sharing)
- [ ] Decide whether to work as a team or independently, and add a statement about it.
- [ ] Push the GitHub repository (the local project is committed; see `../../PLAN-R1-R4.md`).
- [ ] If time allows, ask the instructor/TA for template edit access and move the slides to a copy of the template (optional; the content is ready).
