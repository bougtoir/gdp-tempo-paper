# Identification / separability check (Phase 4)

Script: `scripts/identification_surface_check.py`.
Output: `data/identification_surface.csv`.

Method: evaluate the objective surface over the estimation grid
(μ: 25 points on [0.01, 6.0]; β: 18 points on [0.00, 0.34]) twice per
country — production-only L_p versus joint L_p + 0.3·L_w — and measure
flatness as the share of grid cells within 5 % of the minimum.

Results:
- Median flatness: production-only 19.1 % of grid; joint 13.1 %.
- The joint surface is tighter than the production-only surface in
  21/39 countries (54 %).
- Countries where the joint surface is *flatter* (Mexico, New Zealand,
  Canada, Switzerland, Belgium, Luxembourg, Colombia) are precisely
  those where the demeaned CWON trajectory is nearly flat and therefore
  adds a shallow ridge rather than a sharp minimum.

Consequence for the text: the earlier phrasing that the wealth
constraint "collapses the ridge to a point" was too strong. Manuscript
§6.3 and SI S.11 now say the joint criterion narrows the ridge in most
countries but leaves a broad ridge where CWON coverage is thin, and the
bootstrap rejection counts have been corrected to the actual
`bootstrap_ci.csv` values (μ = 0: 39/39; β = 0: 7/39).

Terminology: all "posterior"/"posterior-like" wording replaced by
"objective surface" / "95 % bootstrap region" (the procedure is a
percentile bootstrap over a grid objective, not Bayesian inference).
