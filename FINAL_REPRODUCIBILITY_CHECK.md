# FINAL REPRODUCIBILITY CHECK (Phase 17)

- `scripts/reproduce.py` was run end-to-end on 2026-09-27 and reported
  "Complete reproduction passed"; `reproduction/reproduction_report.json`
  = status passed (M0 OOS 4.6047, M2 3.9855).
- New scripts `cwon_holdout_validation.py` and
  `identification_surface_check.py` run against the same frozen
  `source_data/` extracts and write deterministic outputs to `data/`.
- `scripts/build_docx_pptx.py` rebuilt manuscript_en.docx,
  supporting_information_en.docx, title_page_en.docx, highlights_en.docx,
  cover_letter_en.docx, figures_en.pptx, and all table docx files; all
  `__*__` placeholders resolve (verified in the built docx XML).
- `scripts/audit_submission.py`: clean — figures and tables cited in
  appearance order, no raw `$`, no stale-version phrases.
- `scripts/verify_references.py`: 37/37 references resolve (Brass 1971
  is a real chapter; title-match heuristic is a false positive).
- No 2-byte characters in English deliverables (checked in audit).
- Public-repo sync: `.github/workflows/sync-to-repos.yml` maps this
  branch to `bougtoir/gdp-tempo-paper` (effective after PR merge since
  the scheduled job reads master's copy of the map).
