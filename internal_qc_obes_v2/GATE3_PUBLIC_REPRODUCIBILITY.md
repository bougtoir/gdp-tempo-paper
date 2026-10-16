# GATE 3 — Independent public reproducibility

Method: fresh clone of https://github.com/bougtoir/gdp-tempo-paper in /tmp
(outside the working tree), `make setup` + `make reproduce-analysis`
(`scripts/reproduce.py --skip-documents`), using ONLY the frozen public
source extracts committed under `source_data/` — no private CSVs, no tokens,
no cached private results.

- Repo commit tested: `6c0d313129ced627128b7fadfe142a08004d02cc` (main, 2026-09-27)
- Result: **"Complete reproduction passed"** — `reproduction/reproduction_report.json` status=passed.
- 23 tracked metrics regenerated IDENTICALLY (k_level n=35, K gap median −4.29, TFP −1.74, LS +1.736, OOS M0 4.6047 / M2 3.9855, tempo 13.8 % NZL, joint 29.7 % FRA, counterfactual ≤1.1 %, fair-eval RMSE row).
- Hand-verified beyond the built-in validator: Wilcoxon M0-vs-M2 p = 0.1756 (n=39, `data/oos.csv` — claim "p≈0.18" reproduced); bootstrap μ excludes 0 in 39/39 and β in 7/39 (`bootstrap_ci.csv`); CWON holdout joint 4.05 % vs prod-only 4.96 % vs M0 5.08 % — joint best; per-country joint-best count verified as claimed.
- Comparison CSV: `data/public_repo_reproduction_comparison.csv` (23/23 match).

## Minimal fixes synchronized to public repo
Branch `obes-v2-uncertainty`, commit `45cc11890057abefb4a913d51e550507714f6aa2`:
new `scripts/cross_country_uncertainty.py`, regenerated `table5_k_level.csv`
with corrected range labels, `data/cross_country_uncertainty*` outputs,
corrected `k_level_analysis.py`. Awaiting merge to main by user (no PR opened
per repo convention; sync also flows via sync-to-repos on merge of wip PR #692).

No material discrepancy → **PASS**.
