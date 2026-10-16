# CWON temporal holdout validation

New analysis added by this revision: `scripts/cwon_holdout_validation.py`.

## Design
- Fit window: production data ≤ 2014; CWON wealth observations 1995–2014 only.
- Holdout: CWON 2015–2019, never used in fitting.
- No-leakage rule: the level normalisation (mean offset between the
  model-implied log capital ratio and the reported CWON ratio) is fitted
  on 1995–2014 only, then applied unchanged to the holdout years.
- Candidates compared on the identical metric: M0 (instant PIM),
  production-only (M1 μ̂ + production-fitted β̂), joint (M4 μ̂, β̂ with
  the wealth term restricted to ≤ 2014).

## Results (data/cwon_holdout_summary.json)
- Median holdout residual (RMSE of demeaned log ratio): joint 4.1 %,
  production-only 5.0 %, M0 5.1 %.
- Joint beats production-only in 23/39 countries; beats M0 in 27/39.
- Share of holdout residuals within 5 %: joint 51 %, production-only
  46 %, M0 44 %.

## Interpretation
The wealth constraint contains genuine out-of-sample information about
the capital trajectory, but the improvement is modest and the holdout
residuals are larger than the in-sample 1–3 % agreement of the
R&D-intensive economies in Figure 2. The manuscript now reports both —
the in-sample correspondence as descriptive and the holdout as the
discipline test — and drops the earlier "within 1–2 % for most
countries" phrasing.

Outputs: `data/cwon_holdout_validation.csv`, `data/cwon_holdout_summary.json`,
`figures/fig_cwon_holdout.png` (Supplementary Figure 14), SI §S.25.
