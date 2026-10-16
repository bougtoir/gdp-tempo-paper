# GATE 1 — Interval provenance audit

## Audit of every interval reported in the manuscript

| Interval | Where | Generator | Correct label? |
|---|---|---|---|
| Per-country (μ,β) "95% CI" | §4.4, Fig. (bootstrap) | `run_bootstrap` residual bootstrap, B=100 replicates, percentile 2.5–97.5 | YES — genuine parametric bootstrap CI |
| OOS MAPE paired bootstrap | §5.1 | percentile bootstrap on 39 country MAPE differences | YES |
| **Table 2 "95% CI" columns** | table5_k_level | `make_table_k_level`: **2.5–97.5 pct of annual values within 2010–19** — a temporal variability range, no sampling model | **NO → fixed** |
| M_obs lag sensitivity 0.5–2.0× | §2.3, Supp. Table 2 | deterministic scaling of calibrated lags | correctly reported as sensitivity range, not CI |
| MC identification (4 countries) | Table 12 caption | MC mean-RMSE error bars | approximate CI — acceptable labelling kept |

## Fix applied
`k_level_analysis.py::make_table_k_level` column headers changed
`"95% CI"` → `"range (2.5–97.5 pct)"`; docstring records the non-CI
interpretation; table caption now states the same. CSV+docx regenerated.

## Cross-country median uncertainty (per prompt requirement)
`scripts/cross_country_uncertainty.py` (NEW): whole-country percentile
bootstrap, B=10,000, seed=20261016, resampling unit = country, identical
resampled index sets across K gap / TFP shift / LS shift. IQR, min–max,
leave-one-country-out median range, and MAD also reported.
Results (data/cross_country_uncertainty.json + summary.csv):

| stat | median | country-boot 95% | IQR | LOO range | MAD |
|---|---|---|---|---|---|
| K gap % | −4.29 | [−4.99, −3.91] | [−5.29, −3.77] | [−4.31, −4.25] | 0.76 |
| TFP shift pp | +1.74 | [1.50, 2.08] | [1.43, 2.68] | [1.72, 1.76] | 0.52 |
| LS shift pp | +1.74 | [1.50, 2.08] | [1.43, 2.68] | [1.72, 1.76] | 0.52 |

Scope note (required): the cross-country CI covers dispersion across
economies only — it excludes uncertainty in the calibrated asset lags
(bounded by the 0.5–2.0× scaling check) and in δ.
