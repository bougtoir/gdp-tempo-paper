# FINAL HANDOFF — SCED submission revision (Phase 21)

## Verdict: READY

## What this revision did
Full autonomous revision pass per
Devin_SCED_single_VM_autonomous_revision_prompt.txt, on top of the
earlier SCED reframing. Single VM, sequential, no child sessions.

### Resolved defects
- Stated estimation grids in §4.3 were wrong; corrected to the actual
  code grids (this also resolves the apparent μ₁ IQR +0.12 vs grid
  +0.08 conflict — the grid was +0.12 all along; the prose was stale).
- SI bootstrap rejection counts were stale (35/28) and contradicted the
  main text; corrected to 39/39 (μ = 0) and 7/39 (β = 0).
- "1–2 % flow–stock agreement for most countries" was an in-sample
  statement presented as general; replaced by calibrated wording plus a
  new strict temporal holdout (joint 4.1 % vs production-only 5.0 %
  median; joint best in 23/39).
- "Posterior"/"statistically sharp" language replaced throughout.
- μ̂_M1 median corrected to 0.26 years.

### New evidence
- CWON temporal holdout (script, data, figure, SI S.25).
- Identification objective-surface flatness check (script + csv + md).
- M_obs provenance ledger (OBSERVABLE_TEMPO_PROVENANCE.csv):
  35 usable countries; DEU/KOR/NOR/POL use the N11MG fallback asset
  scheme; CHE/CHL/CHN/TUR lack coverage and are excluded.
- Full audit trail: NUMERICAL_CONSISTENCY_AUDIT.md,
  NUMERICAL_CORRECTIONS.csv, FLOW_STOCK_COMPARABILITY_AUDIT.md,
  REFERENCE_AND_NOVELTY_AUDIT.md, HOSTILE_REVIEW_FINAL.md,
  FINAL_REPRODUCIBILITY_CHECK.md, REVISION_CHANGELOG.md.

### Submission artefacts
- `SCED_manuscript_revised_final.docx` (inline figures/tables)
- `SCED_supplement_revised_final.docx`
- `SCED_submission_package_FINAL.zip` (56 files incl. title page,
  highlights, cover letter, editable pptx, separate PNGs, table docx,
  all audit docs)
- Branch `devin/1790497801-sced-submission`, PR #550 on bougtoir/wip;
  sync map registered for public repo bougtoir/gdp-tempo-paper.

## Remaining risks (honest)
- Bootstrap CIs are wide; identification claims are deliberately modest.
- CWON coverage heterogeneity and intangible double-counting are
  disclosed caveats, not resolved.
- Japan's PIM–CWON gap is attributed (plausibly) to price revaluation;
  referees may push further.
- SCED charges a US$100 submission fee (refunded if accepted).
