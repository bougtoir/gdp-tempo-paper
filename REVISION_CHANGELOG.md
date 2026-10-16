# REVISION CHANGELOG — SCED autonomous revision pass (2026-09-27)

Baseline: commit 7e056d18 on devin/1790497801-sced-submission.
Governing document: Devin_SCED_single_VM_autonomous_revision_prompt.txt.
All work performed sequentially on a single VM; no child sessions.

## New analysis
- `scripts/cwon_holdout_validation.py` (Phase 3): strict temporal holdout
  of the CWON wealth constraint (fit ≤ 2014, evaluate 2015–2019,
  train-only normalisation). Outputs `data/cwon_holdout_validation.csv`,
  `data/cwon_holdout_summary.json`, `figures/fig_cwon_holdout.png`.
  Result: median holdout residual joint 4.1 % < production-only 5.0 %
  < M0 5.1 %; joint best in 23/39.
- `scripts/identification_surface_check.py` (Phase 4): objective-surface
  flatness check on the estimation grid. Joint surface tighter than
  production-only in 21/39 countries. Output `data/identification_surface.csv`.

## Manuscript (manuscript_en.md)
- Abstract rewritten: dropped "reconcile ... within 1–2 % for most
  countries", "validated", "statistically sharp"; added holdout result.
- §4.3: corrected the stated estimation grids to the actual code grids
  (μ: 25-pt linspace 0.01–6.0; μ₁: 11-pt linspace −0.08 to +0.12;
  β: 18-pt linspace 0–0.34); "posterior-like surface" → "objective
  surface"; removed stale "1000-draw" bootstrap mention (actual n=100/120).
- §5.1: μ̂_M1 median corrected 0.3 → 0.26 years.
- §5.2: "confirming" → "indicating" (×2).
- §5.3: US/KOR/ISR "within 1–2 %" → "a few per cent"; new paragraph
  reporting the CWON temporal holdout with computed placeholders.
- §6.3: "posteriors" → "objective surfaces"; ridge-collapse claim
  tempered to match the surface-flatness check.
- §6.5: "agree to within 1–2 % for most countries" → qualified with the
  holdout result.
- Contributions paragraph: third contribution is now M_obs; the
  demographic framework is presented as the methodological source
  rather than a contribution in itself.

## Supporting information (supporting_information_en.md)
- S.11: bootstrap rejection counts corrected to the actual
  bootstrap_ci.csv values (μ = 0: 39/39; β = 0: 7/39);
  "posterior region" → "95 % bootstrap region"; ridge-collapse wording
  tempered.
- S.20: "statistically sharp" → "statistically well-posed".
- New S.25 documenting the CWON temporal holdout (Supplementary
  Figure 14 = figures/fig_cwon_holdout.png).

## Build pipeline
- `scripts/build_docx_pptx.py`: new placeholders __CWON_HOLD_JOINT__,
  __CWON_HOLD_PROD__, __CWON_HOLD_M0__, __CWON_TRAIN_JOINT__,
  __CWON_JOINT_BEATS__, __CWON_N__ filled from
  data/cwon_holdout_summary.json; new FIG_LIST entry fig19 for the
  holdout figure.

## Audit outputs created
- REVISION_BASELINE_INVENTORY.md, CURRENT_RESULT_MAP.csv
- NUMERICAL_CONSISTENCY_AUDIT.md, NUMERICAL_CORRECTIONS.csv
- CWON_HOLDOUT_VALIDATION.md, OBSERVABLE_TEMPO_PROVENANCE.csv
- identification_surface_summary.md, FLOW_STOCK_COMPARABILITY_AUDIT.md
- REFERENCE_AND_NOVELTY_AUDIT.md, HOSTILE_REVIEW_FINAL.md
- FINAL_REPRODUCIBILITY_CHECK.md, FINAL_HANDOFF.md

## Not changed
- No new references added; no robustness-explosion additions (robustness
  budget respected: only CWON holdout + numerical consistency).
- manuscript_ja.md left unchanged (excluded from submission).
