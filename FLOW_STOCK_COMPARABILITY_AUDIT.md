# Flow–stock price-basis and comparability audit (Phase 6)

## Units and price bases
- PWT 10.01 `rnna` / `rgdpna`: real, constant-price series (2017 national
  prices, chained). `csh_i` × `rgdpna` gives the constant-price
  investment series used in every PIM construction.
- CWON `NW.PCA.TO`: current US$ produced capital, 2019 release
  (market exchange rates).
- OECD GFCF by asset (SNA 8A): current national-currency values used
  only as *shares* in μ_obs, so units and price levels cancel.

## What is and is not compared
Because PWT and CWON differ in currency unit, price basis, and base
year, raw levels are never compared. The joint loss (eq. 2) and every
PIM–CWON comparison use *within-country demeaned log ratios*: each
series is expressed as a deviation from its own 1995–2019 mean in logs,
which removes both the constant unit factor and any constant price-gap
level. What the criterion disciplines is the *shape/growth pattern* of
the trajectories, not their absolute level — this is now stated
explicitly in §5.3.

Residual price-level drift (e.g. land-price revaluation carried by CWON
but not by our PIM) is addressed by the γ_price sweep (SI S.9–S.10,
Supplementary Table 12): a ±4 %/yr revaluation grid brackets observed
land-price episodes and shows that only Japan's residual is plausibly
price-driven.

## Depreciation comparability
PWT `delta` is used uniformly inside the PIMs; CWON's own depreciation
conventions differ. The δ-sensitivity experiment (SI S.13,
Supplementary Table 10) perturbs δ by ±20 % and shows median μ̂
invariant at 0.26 years; time-varying δ(t) robustness is reported in
SI S.19.

## Caveat retained
M3/M4 treat the R&D-based intangible stock as a coverage-gap proxy; the
overlap with assets already inside `rnna`/CWON after the 2008 SNA
cannot be netted out exactly (§4.1 caveat retained verbatim).
