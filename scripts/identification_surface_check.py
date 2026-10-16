"""Identification / separability check for the (mu, beta) objective surface.

For each country we evaluate the objective surface over the same
(mu, beta) grid used by the joint estimator, twice:
  - production-only:  L_p(mu, beta)
  - joint:            L_p(mu, beta) + 0.3 * L_w(mu, beta)   (eq. 2)

We then measure flatness as the share of grid cells whose objective is
within 5 % of the minimum. A large share means the surface is a broad
ridge (weak separability); a small share means the minimum is localised.

Outputs: data/identification_surface.csv (per-country flatness shares),
and prints a summary used in identification_surface_summary.md.
"""
import os

import numpy as np
import pandas as pd

from run_paper_analyses import (build_intan_stock, pim_lagged,
                                prepare_countries)

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
LAMBDA = 0.3
MU_GRID = np.linspace(0.01, 6.0, 25)
BETA_GRID = np.linspace(0.0, 0.34, 18)
TOL = 0.05


def surfaces(c):
    alpha = 1 - float(np.clip(np.mean(c.labsh), 0.40, 0.75))
    logY = np.log(c.Y)
    logL = np.log(c.emp * c.avh)
    K_intan = build_intan_stock(c.Y, c.rnd_share)
    if K_intan is None:
        return None
    logI = np.log(np.where(K_intan > 0, K_intan, 1e-6))
    idx_map = {int(y): ii for ii, y in enumerate(c.years)}
    ki = [idx_map.get(int(y), None) for y in c.cwon_years]
    lobs = np.log(np.where(c.pca > 0, c.pca, np.nan))
    Lp = np.full((len(MU_GRID), len(BETA_GRID)), np.nan)
    Lw = np.full_like(Lp, np.nan)
    dY = np.diff(logY); dI = np.diff(logI); dL = np.diff(logL)
    for i, mu in enumerate(MU_GRID):
        K = pim_lagged(c.I, c.delta, c.K0, mu)
        K = np.where(K > 0, K, 1e-6)
        dK = np.diff(np.log(K))
        aligned = np.array([K[ii] if ii is not None else np.nan
                            for ii in ki])
        intan_cw = np.array([K_intan[ii] if ii is not None else np.nan
                             for ii in ki])
        for j, beta in enumerate(BETA_GRID):
            if alpha + beta >= 0.95:
                continue
            w_L = 1 - alpha - beta
            pred = alpha * dK + beta * dI + w_L * dL
            g = np.mean(dY - pred)
            Lp[i, j] = np.mean((dY - g - pred) ** 2)
            hat = aligned + beta * intan_cw
            m = np.isfinite(hat) & np.isfinite(lobs) & (hat > 0)
            if m.sum() >= 6:
                d = (np.log(hat[m]) - np.log(hat[m]).mean()) - \
                    (lobs[m] - lobs[m].mean())
                Lw[i, j] = np.mean(d ** 2)
    return Lp, Lw


def flatness(S):
    v = S[np.isfinite(S)]
    return float((v <= v.min() * (1 + TOL)).mean()), float(np.nanmin(S))


def main():
    rows = []
    for c in prepare_countries():
        out = surfaces(c)
        if out is None:
            continue
        Lp, Lw = out
        Lt = Lp + LAMBDA * np.nan_to_num(Lw, nan=np.inf)
        fp, mp = flatness(Lp)
        fj, mj = flatness(Lt)
        i, j = np.unravel_index(np.nanargmin(Lt), Lt.shape)
        rows.append(dict(country=c.country, iso3=c.iso,
                         flat_prod=fp, flat_joint=fj,
                         mu_joint=float(MU_GRID[i]),
                         beta_joint=float(BETA_GRID[j])))
        print(f"{c.country:22s} flat_p={fp:.2f} flat_j={fj:.2f} "
              f"mu*={MU_GRID[i]:.2f} beta*={BETA_GRID[j]:.2f}", flush=True)
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(DATA, "identification_surface.csv"), index=False)
    print("\nmedian flatness production-only:", df.flat_prod.median())
    print("median flatness joint:", df.flat_joint.median())
    print("share with tighter joint surface:",
          (df.flat_joint < df.flat_prod).mean())


if __name__ == "__main__":
    main()
