# GATE 4 — Focused revision log

Changes limited to interval provenance, uncertainty reporting, OBES format compliance. No refitting; no new estimands.

1. manuscript_en.md §5.4: added interval-provenance paragraph distinguishing (a) within-country temporal ranges in Table 2 from (b) cross-country bootstrap CIs on the 35-country medians ([−5.0,−3.9] K gap; [1.5,2.1] pp TFP/LS) and LOO ranges; scope caveat (lags/δ uncertainty bounded separately).
2. Abstract: condensed 271→78 words (OBES ≤100-word rule, verified). Claims preserved: +1.7 pp TFP/LS medians, ≤1.1 % intangible correction, M_obs corroboration.
3. Title page: added Abstract, Keywords, marked word count (≈11,400 incl. figure/table equivalents).
4. table5_k_level.csv headers "95% CI"→"range (2.5–97.5 pct)"; docx caption clarifies.
5. scripts/cross_country_uncertainty.py (new) + data/cross_country_uncertainty* outputs.
6. k_level_analysis.py docstring corrected (non-CI interpretation).

Preserved untouched: all estimates, Wilcoxon p≈0.18 nonsignificant result,
23/39 CWON holdout finding, μ–δ confound caveat, Japan CWON caveat,
β residual-identification caveat, all negative results.
