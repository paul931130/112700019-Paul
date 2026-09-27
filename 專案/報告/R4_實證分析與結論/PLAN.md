# R4: Empirical Analysis and Conclusion — Outline

Corresponding manuscript section: Results / Conclusion. The 40% Project grade is based on the LaTeX manuscript, not this folder; see “What Is Actually Graded” in `../../README.md`.

## Structure

1. **Did the replication succeed?** Compare the R3 baseline and RSR results with the original paper's conclusion that the relation graph significantly improves ranking performance. The numbers need not match exactly, but the direction should. If they differ, discuss possible reasons such as data period, hyperparameters, or random seed.
2. **Comparison with the original paper:** Explain how differences in methods, data period, and market coverage affect comparability.
3. **Limitations:** Data end at a particular date; only the with/without-relation-graph ablation has been fully compared. Decide whether to add industry vs. Wikidata or NASDAQ vs. NYSE results, depending on time.
4. **Future work:** Address the syllabus prompt “Potential of your projects.” Possible extensions include trying different relation sources, Wikidata relations, or NYSE.

## Writing Reminder

- Tie every conclusion to a table or figure in R3; avoid unsupported assertions.

**See the complete draft in [R4.md](R4.md)**; it is ready.

## To Do

- [x] Scope is set as a straight replication with no dynamic-relation extension. ``6–7` of `../../manuscript/main.tex` have been rewritten to discuss only the baseline-vs-RSR replication and comparison with the original paper.
- [ ] Decide whether to keep the dynamic-relation exploration notes from the latter part of `../R3_模型與實驗設計/PROGRESS.md` as an appendix or exclude them from the manuscript.
- [ ] After the R3 robustness checks (new seed and hyperparameter search), revisit the three candidate explanations in R4.md `2.
