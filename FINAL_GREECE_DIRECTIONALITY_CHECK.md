# Greece / "all 35 countries" directionality check

## Canonical object
- `data/k_level_diff.csv`: per (country, year) `K_pct_diff = (exp(delta_logK) − 1) × 100`, 35 countries × 1950–2019.
- `scripts/k_level_analysis.py` line 67: Table 2 / summary use **country means of K_pct_diff over 2010–2019** (CI = [min, max] of yearly values). Median/IQR in text are computed across the 35 country means.
- Figure 3 (`fig10_k_divergence`): yearly K_obs/K_M0 − 1 time series for six countries (Greece not among them).

## Resolution
- Under the canonical aggregation (2010–2019 country mean) **all 35 countries are negative**; Greece's mean is −0.58 % (Table 2 value −0.6 %).
- Under a yearly reading, Greece is positive in 2014–2019 (+0.08 % to +0.95 %, mean +0.67 % over those years) — the only positive country-years in the panel.
- The pre-revision universal statement was true for the table's aggregation but false as a per-year claim. The manuscript now states the aggregation explicitly and discloses the per-year Greece exception.

No result values changed; only the aggregation definition was made explicit and the per-year exception disclosed.
