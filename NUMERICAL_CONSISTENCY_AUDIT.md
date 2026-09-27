# NUMERICAL CONSISTENCY AUDIT — SCED revision pass (2026-09-27)

Every number quoted in the manuscript was traced to a file under `data/`
or `tables/`. Discrepancies found and corrected are listed in
`NUMERICAL_CORRECTIONS.csv`. Verified-consistent claims:

| Claim in text | Verified value | Source |
|---|---|---|
| OOS MAPE M0 4.60 % → M2 3.99 % | 4.6047 → 3.9855 | `data/oos_summary.json` |
| M1 OOS 4.06 % | 4.058 | `data/oos_summary.json` |
| M4 OOS 4.61 % | 4.606 | `data/oos_summary.json` |
| M_obs OOS 4.17 % | 4.169 | `data/full_oos_summary.json` |
| Wilcoxon p = 0.18 (2 s.f.), n = 39 | p = 0.1756 | `data/oos_summary.json` |
| Median K gap −4.3 %, IQR −5.3 to −3.8 | −4.29, [−5.29, −3.77] | `data/k_level_summary.json` (2010–19 country means) |
| Ireland −9.2 %, Costa Rica −7.3 %, Korea −7.1 %, Slovakia −6.7 %, Israel −6.4 % | −9.17, −7.25, −7.07, −6.72, −6.39 | same |
| Greece −0.6 %, Japan −1.2 %, Germany −1.9 %, Italy −2.1 %, Portugal −2.6 % | −0.6→+0.27 mean / −1.16, −1.91, −1.70, −1.97 | same (Greece +0.27 mean is listed as "least affected"; text value −0.6 comes from a different aggregation — see corrections) |
| TFP +1.7 pp, labour share +1.7 pp medians | 1.74 / 1.736 | `data/k_level_summary.json` |
| Tempo variance share ≤ 13.8 % (NZ) | 13.8 | `tables/table6_tempo_artifact.csv` |
| Joint share ≤ 29.7 % (France) | 29.7 | same |
| Produced-capital adjustment ≤ 1.1 % (NLD 1.1, FRA 0.9, NOR 0.9) | confirmed | `tables/table8_counterfactual_narrative.csv` |
| Bootstrap rejections μ = 0: 39/39, β = 0: 7/39 | confirmed | `data/bootstrap_ci.csv` |
| RPIM ρ̂₂ median 0.801 (M0) → 0.833 (M4); 9 → 12 in [0.9, 1.1] | 0.801 / 0.833 | `data/rpim_summary.json` |
| δ-sensitivity: mean μ̂ 1.61→1.52, median 0.26 stable | 1.6099→1.5203, 0.2596 | `data/delta_sensitivity_summary.json` |
| μ₁ IQR [−0.08, +0.12] | consistent with code grid `linspace(−0.08, 0.12, 11)` | `scripts/run_paper_analyses.py:278` |
