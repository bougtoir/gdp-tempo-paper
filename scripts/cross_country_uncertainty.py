"""Cross-country uncertainty for the 35-country medians (Gate 2).

Estimand: median over countries of DeltaK_i = 2010-2019 mean K_pct_diff
(and the corresponding TFP-shift / labour-share-shift medians).

Inference model: treating the 35 countries as exchangeable draws from a
conceptual superpopulation of economies with comparable asset composition,
we resample WHOLE COUNTRIES (not country-years) with replacement,
B = 10,000 draws, fixed seed, and take the 2.5/97.5 percentiles of the
resampled medians (percentile bootstrap). The SAME resampled country index
set is used for all three statistics so the intervals are coherent.

Important scope note: this interval captures only cross-country sampling
uncertainty. It does NOT include uncertainty in the calibrated
asset-specific gestation lags (dwellings/buildings 2.0 yr, transport 0.5,
ICT 0.3, machinery 0.8, IPP 3.0) nor in the depreciation series; those are
bounded separately by the 0.5x-2.0x lag-scaling robustness check
(Supplementary Table 2 / table13).

Outputs:
  data/cross_country_uncertainty.json
  data/cross_country_uncertainty_summary.csv
"""
import json
import os

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
DATA = os.path.join(ROOT, "data")

B = 10_000
SEED = 20261016

kdf = pd.read_csv(os.path.join(DATA, "k_level_diff.csv"))
recent = kdf[(kdf["year"] >= 2010) & (kdf["year"] <= 2019)]
per_country = (
    recent.groupby("iso3")
    .agg(K=("K_pct_diff", "mean"), TFP=("TFP_shift_pct", "mean"), LS=("ls_shift_pp", "mean"))
    .reset_index()
)
assert len(per_country) == 35, len(per_country)

stats = {
    "K_gap_pct": per_country["K"].values,
    "TFP_shift_pp": np.abs(per_country["TFP"].values),  # reported as +1.7 pp shift
    "LS_shift_pp": per_country["LS"].values,
}

rng = np.random.default_rng(SEED)
n = len(per_country)
res = {}
boot_medians = {k: np.empty(B) for k in stats}
for b in range(B):
    idx = rng.integers(0, n, n)  # whole-country resampling, shared across stats
    for k, v in stats.items():
        boot_medians[k][b] = np.median(v[idx])

rows = []
for k, v in stats.items():
    meds = boot_medians[k]
    lo, hi = np.percentile(meds, [2.5, 97.5])
    loo = np.array([np.median(np.delete(v, i)) for i in range(n)])
    mad = float(np.median(np.abs(v - np.median(v))))
    rows.append({
        "statistic": k,
        "median": float(np.median(v)),
        "country_boot_ci_lo": round(float(lo), 2),
        "country_boot_ci_hi": round(float(hi), 2),
        "q25": round(float(np.percentile(v, 25)), 2),
        "q75": round(float(np.percentile(v, 75)), 2),
        "min": round(float(v.min()), 2),
        "max": round(float(v.max()), 2),
        "loo_median_min": round(float(loo.min()), 2),
        "loo_median_max": round(float(loo.max()), 2),
        "MAD": round(mad, 2),
    })

out = {
    "estimand": "median over countries of 2010-2019 country-mean gap/shift",
    "n_countries": n,
    "bootstrap": {"type": "whole-country percentile", "B": B, "seed": SEED,
                  "resampling_unit": "country", "shared_indices_across_stats": True},
    "scope": "cross-country sampling uncertainty only; excludes calibrated "
             "gestation-lag and depreciation uncertainty (bounded separately)",
    "results": rows,
}
with open(os.path.join(DATA, "cross_country_uncertainty.json"), "w") as f:
    json.dump(out, f, indent=2)
pd.DataFrame(rows).to_csv(
    os.path.join(DATA, "cross_country_uncertainty_summary.csv"), index=False)

for r in rows:
    print(r)
