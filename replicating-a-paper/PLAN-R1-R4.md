# Overall Plan for R1–R4

Today is 2026-09-27. Each of the four milestones consists of the corresponding manuscript section plus an in-class presentation. Manuscript content goes into `manuscript/main.tex` and slides go in Canva; the `PLAN.md`/`R{n}.md` files in each folder are drafts. The 40% Project grade is based on the LaTeX manuscript (see “What Is Actually Graded” in `README.md`).

## Schedule Overview

| Milestone | Deadline | Days remaining | Manuscript sections | Status |
|---|---|---:|---|---|
| R1: Topic and Motivation | 10/05 23:59 | 8 | `1 Introduction | Manuscript PDF pushed; slides PDF pushed |
| R2: Data and EDA | 10/19 23:59 | 22 | `3 Data | EDA notebook exists; PLAN outline still needs to be written up as R2.md |
| R3: Model and Experimental Design | 11/09 23:59 | 43 | `4 Methods + `5 Results | Training results complete; PLAN needs an R3.md draft and robustness checks remain |
| R4: Empirical Analysis and Conclusion | 11/30 23:59 | 64 | `6 Discussion + `7 Conclusion | R4.md draft complete; revisit after R3 robustness checks |

## R1 (10/05): Remaining Items

Course requirement (`repo-template/replicating-a-paper/README.md`): push PDFs of the manuscript and slides to `_snapshots/` as `20261005-manuscript.pdf` and `20261005-slides.pdf`. The commit timestamp is the submission time.

- [x] Content: `reports/R1_topic_and_motivation/R1.md`
- [x] Manuscript `1 Introduction` synchronized
- [x] Slide outline: `reports/R1_topic_and_motivation/R1_slides_outline.md`
- [x] Local Git repository created and pushed to GitHub (`paul931130/112700019-Paul`)
- [x] Overleaf (read-only link) and Canva links added to `README.md`
- [x] Full paper PDF added to `references/`
- [x] `_snapshots/20261005-manuscript.pdf` (compiled from `manuscript/main.tex`)
- [x] `_snapshots/20261005-slides.pdf` (built from the course .pptx template, pages 1-2 only)
- [ ] Your action: add `venteng@gmail.com` as an Overleaf collaborator (Canva share optional now that the PDF is in the repo)

## R2 (10/19): Turn the EDA into Written Findings

Current status: `coding/eda.ipynb` already contains analysis (findings about the missing-value sentinel, ETFs mixed into the graph, etc., already cited in manuscript section 3), but the R2 folder has no written draft like R1.md or R4.md—only a PLAN outline.

- [ ] Write `reports/R2_data_and_eda/R2.md`: summarize the findings from `eda.ipynb` (data sources, scale, and two data-quality issues) for manuscript section 3 Data. The manuscript section itself is already written; this is mainly a standalone version for the R2 presentation.
- [ ] Prepare a slide outline in the same format as `R1_slides_outline.md`.
- [ ] Check whether `eda.ipynb` needs additional figures (the manuscript currently describes the missing-value and ETF issues in text without figures).

## R3 (11/09): Content Is Ready; Robustness Checks Remain

Current status: baseline vs. RSR training results are recorded in `PROGRESS.md`, and manuscript sections 4–5 have been written from those results. The `reports/R3_model_and_experiments/` folder still lacks a standalone written draft like R1.md.

- [ ] Write `reports/R3_model_and_experiments/R3.md`: combine the model setup in `PLAN.md` and results in `PROGRESS.md` into a draft corresponding to manuscript sections 4 Methods + 5 Results.
- [ ] Prepare a slide outline.
- [ ] **Robustness checks (to evaluate the three candidate explanations in R4.md `2):**
  - [ ] Rerun baseline and RSR for 50 epochs with a different random seed to check whether the split in mrrt/btl is a one-off result.
  - [ ] Run a small hyperparameter search moving toward the original paper's `seq=16, unit=64` configuration to assess sensitivity to hyperparameters.
- [ ] Depending on time, consider adding an ablation for Wikidata relations or the NYSE market. This is optional; the manuscript already lists it as a limitation.

## R4 (11/30): Draft Complete; Revisit After R3 Checks

- [x] `reports/R4_results_and_conclusion/R4.md` completed
- [x] Manuscript ``6–7` synchronized
- [ ] After the R3 robustness checks, revisit the three candidate explanations in R4.md `2. If the mrrt/btl split disappears or reverses with another seed, revise ``6–7` accordingly.
- [ ] Prepare a slide outline.

## Suggested Order of Work

1. **Finish R1 by 10/05 23:59**: slides PDF in `_snapshots/`, and Overleaf/Canva shared with the instructor. The writing is ready; avoid revising R1 prose.
2. When time allows, run the R3 robustness checks first (new seed and hyperparameter search), because the quality of the R4 conclusions depends on them. Completing these early reduces the risk of repeatedly revising R4.
3. R2.md and R3.md are lower priority. The manuscript content is already in ``3–5`; the two drafts mainly support the R2/R3 milestone presentations, whose deadlines are still ahead.
