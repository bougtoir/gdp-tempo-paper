"""CWON temporal holdout validation.

Fits the joint (mu, beta) objective using only the 1995-2014 portion of
the CWON wealth series, then evaluates the implied log capital ratio
against the 2015-2019 CWON observations that were never used in fitting.

Three candidate capital constructions are compared on the SAME holdout
metric:
  - M0:        instant PIM (Solow baseline, no free parameters)
  - prod-only: mu fit on production growth residuals <=2014 (M1), beta
               fit on production residuals only (as in M3/M4 pipeline
               but without the wealth constraint)
  - joint:     mu, beta from fit_joint with the wealth term restricted
               to CWON years <=2014 (exactly the run_oos convention)

Leakage rule: the level normalization (the constant that aligns the
model-implied ratio with the reported CWON ratio) is computed on the
1995-2014 subsample only and then applied to the holdout years.  The
holdout residual therefore measures genuine out-of-sample error in the
level ratio, not a re-fitted demeaned distance.

Outputs:
  data/cwon_holdout_validation.csv   per-country x model residuals
  data/cwon_holdout_summary.json     medians, share within 2 %
  figures/fig_cwon_holdout.png       train vs holdout residual scatter
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from run_paper_analyses import (Country, build_intan_stock, fit_beta_given_K,
                                fit_joint, fit_mu_const, pim_instant,
                                pim_lagged, prepare_countries)

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
FIG = os.path.join(HERE, "..", "figures")
TRAIN_END = 2014  # CWON holdout = 2015-2019
MIN_TRAIN, MIN_HOLD = 6, 2


def implied_ratio_series(c: Country, Ktang, beta, K_intan):
    """log of model-implied wealth ratio K_tang + beta*K_intan at CWON years."""
    idx = {int(y): ii for ii, y in enumerate(c.years)}
    lhat = np.full(len(c.cwon_years), np.nan)
    for j, y in enumerate(c.cwon_years):
        ii = idx.get(int(y))
        if ii is None:
            continue
        v = Ktang[ii] + beta * K_intan[ii]
        if v > 0:
            lhat[j] = np.log(v)
    return lhat


def holdout_rm(lhat, lobs, train_mask, hold_mask):
    """Residual with normalization fitted on train_mask only."""
    tm = train_mask & np.isfinite(lhat) & np.isfinite(lobs)
    hm = hold_mask & np.isfinite(lhat) & np.isfinite(lobs)
    if tm.sum() < MIN_TRAIN or hm.sum() < MIN_HOLD:
        return None, None, 0
    off = np.mean(lhat[tm] - lobs[tm])
    d_ho = (lhat[hm] - lobs[hm]) - off
    d_tr = (lhat[tm] - lobs[tm]) - off
    return float(np.sqrt(np.mean(d_tr ** 2))), \
        float(np.sqrt(np.mean(d_ho ** 2))), int(hm.sum())


def main():
    countries = prepare_countries()
    rows = []
    for c in countries:
        mask_train = c.years <= TRAIN_END
        if mask_train.sum() < 20:
            continue
        alpha = 1 - float(np.clip(np.mean(c.labsh[mask_train]), 0.40, 0.75))
        logY_tr = np.log(c.Y[mask_train])
        emp_t, avh_t, hc_t = c.emp[mask_train], c.avh[mask_train], c.hc[mask_train]
        logLH_tr = np.log(emp_t * avh_t * hc_t)
        logL_tr = np.log(emp_t * avh_t)
        K_intan = build_intan_stock(c.Y, c.rnd_share)
        if K_intan is None:
            continue
        K_intan_tr = K_intan[mask_train]
        I_tr, d_tr, K0 = c.I[mask_train], c.delta[mask_train], c.K0

        # --- fits on <=2014 only ---
        mu_p = fit_mu_const(I_tr, d_tr, K0, logY_tr, logLH_tr, alpha)
        K_p_tr = pim_lagged(I_tr, d_tr, K0, mu_p)
        beta_p = fit_beta_given_K(K_p_tr, K_intan_tr, logY_tr, logL_tr, alpha)

        idx_map = {int(y): ii for ii, y in enumerate(c.years[mask_train])}
        ki_tr = [idx_map.get(int(y)) for y in c.cwon_years
                 if int(y) <= TRAIN_END]
        pca_tr = c.pca[c.cwon_years <= TRAIN_END]
        mu_j, beta_j, _, _ = fit_joint(I_tr, d_tr, K0, K_intan_tr,
                                       logY_tr, logL_tr, alpha, ki_tr,
                                       pca_tr)

        # --- wealth evaluation on CWON years ---
        train_mask = c.cwon_years <= TRAIN_END
        hold_mask = ~train_mask
        lobs = np.log(np.where(c.pca > 0, c.pca, np.nan))
        cands = {
            "M0": (pim_instant(c.I, c.delta, c.K0), 0.0),
            "prod_only": (pim_lagged(c.I, c.delta, c.K0, mu_p), beta_p),
            "joint": (pim_lagged(c.I, c.delta, c.K0, mu_j)
                      if np.isfinite(mu_j) else None,
                      beta_j if np.isfinite(beta_j) else 0.0),
        }
        for model, (Kt, beta) in cands.items():
            if Kt is None:
                continue
            lhat = implied_ratio_series(c, Kt, beta, K_intan)
            rm_tr, rm_ho, n_ho = holdout_rm(lhat, lobs, train_mask, hold_mask)
            if rm_ho is None:
                continue
            rows.append(dict(country=c.country, iso3=c.iso, model=model,
                             mu=mu_p if model == "prod_only"
                             else (mu_j if model == "joint" else 0.0),
                             beta=beta, rm_train=rm_tr, rm_holdout=rm_ho,
                             n_holdout=n_ho))
        print(f"  {c.country:22s} done", flush=True)

    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(DATA, "cwon_holdout_validation.csv"), index=False)

    summ = {}
    for m in ["M0", "prod_only", "joint"]:
        s = df[df.model == m]
        summ[m] = {
            "n": int(len(s)),
            "rm_train_median": float(s.rm_train.median()),
            "rm_holdout_median": float(s.rm_holdout.median()),
            "rm_holdout_q25": float(s.rm_holdout.quantile(0.25)),
            "rm_holdout_q75": float(s.rm_holdout.quantile(0.75)),
            "holdout_within_2pct": float((s.rm_holdout <= np.log(1.02)).mean()),
            "holdout_within_5pct": float((s.rm_holdout <= np.log(1.05)).mean()),
        }
    # paired comparison joint vs prod_only
    piv = df.pivot_table(index="iso3", columns="model", values="rm_holdout")
    paired = piv.dropna(subset=["joint", "prod_only"])
    summ["joint_beats_prod_only"] = f"{int((paired.joint < paired.prod_only).sum())}/{len(paired)}"
    summ["joint_beats_M0"] = f"{int((paired.joint < paired.M0).sum())}/{len(paired)}"
    json.dump(summ, open(os.path.join(DATA, "cwon_holdout_summary.json"), "w"),
              indent=2)
    print(json.dumps(summ, indent=2))

    fig, ax = plt.subplots(figsize=(6, 6))
    colors = {"M0": "grey", "prod_only": "tab:orange", "joint": "tab:blue"}
    for m in ["M0", "prod_only", "joint"]:
        s = df[df.model == m]
        ax.scatter(s.rm_train * 100, s.rm_holdout * 100, s=28, alpha=0.7,
                   label=f"{m} (med {s.rm_holdout.median()*100:.1f}%)",
                   color=colors[m])
    lim = max(df.rm_holdout.max(), df.rm_train.max()) * 105
    ax.plot([0, lim], [0, lim], "k--", lw=0.8, alpha=0.5)
    ax.set_xlabel("In-sample CWON residual, 1995-2014 (%)")
    ax.set_ylabel("Holdout CWON residual, 2015-2019 (%)")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "fig_cwon_holdout.png"), dpi=300)


if __name__ == "__main__":
    main()
