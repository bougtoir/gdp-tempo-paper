# SCED FINAL FINISHING REPORT (v2 pass, 2026-09-27)

## 1. Changes per issue
- Issue 1 (business-cycle claim): the untested procyclicality paragraph
  was DELETED from §5 Results. A one-sentence hypothesis appears at the
  end of §6.5: "A further extension worth testing is whether shifts in
  the composition of investment over the business cycle create cyclical
  variation in effective gestation; the present analysis does not
  identify this mechanism."
- Issue 2 (Greece / "all 35"): resolved — see
  FINAL_GREECE_DIRECTIONALITY_CHECK.md. Canonical aggregation =
  2010–2019 country mean of K_pct_diff; under it all 35 countries are
  negative. Manuscript now states the aggregation and discloses
  Greece's positive 2014–2019 yearly values.
- Issue 3 (rejects language): "joint identification rejects μ = 0 ..."
  → "the 95 % bootstrap interval on μ excludes zero for 39 of 39
  countries and the interval on β excludes zero for 7 countries"
  (manuscript §4.4 and SI S.11). No hypothesis test exists separately;
  interval wording used throughout.
- Issue 4 (§6.5 CWON rhetoric): "should trust ... now agree to within
  1–2 %" replaced with neutral evidence language citing the temporal
  holdout; "irreconcilable" claim softened to "weakened".

## 2. Greece resolution
Country means over 2010–2019 are negative for all 35 countries
(Greece −0.6 %). Greece has positive yearly values 2014–2019
(mean +0.7 % over those years) — disclosed in text. Table 2 unchanged
(it already uses the mean). Figure 3 caption makes no universal claim.

## 3. Final bootstrap wording
"The 95 % bootstrap interval on μ excludes zero for 39 of 39 countries
and the interval on β excludes zero for 7 countries." Counts verified
against data/bootstrap_ci.csv.

## 4. Business-cycle paragraph
Deleted from Results; one-sentence "extension worth testing" added in
§6.5.

## 5. CWON rhetoric
§6.5 now reads: "The close trajectory agreement, together with the
temporal holdout results of Sect. 5.3, provides additional support for
treating time-varying gestation and the intangible-capital component as
useful accounting corrections, while not implying that CWON itself is
ground truth."

## 6. Headline numbers
Unchanged. Spot check: OOS M0 4.60 %, M2 3.99 %, Wilcoxon p = 0.18
(n = 39); CWON holdout medians joint 4.1 % / prod-only 5.0 % / M0
5.1 %, joint best 23/39; K gap −4.3 %; TFP +1.7 pp; labour share
+1.7 pp; intangible adjustment ≤ 1.1 %; μ₁ grid −0.08 to +0.12
(11 points); 39-country panel, 35-country M_obs subset — all confirmed
against canonical outputs.

## 7. Synchronization
Abstract, introduction, results, discussion, conclusion, SI,
highlights, and cover letter use the same calibrated claims; the cover
letter now cites the temporal holdout instead of the "1–2 %" claim.

## 8. DOCX integrity
manuscript_en.docx rebuilt: 198 OMML equations intact, all
placeholders filled, no tracked changes, figures/tables embedded
inline; audit_submission.py clean (citation order, no raw $).

## 9. Final ZIP contents (SCED_submission_package_FINAL_v2.zip, 58 files)
- SCED_manuscript_submission_final.docx (+pdf) — inline manuscript
- SCED_supplement_submission_final.docx (+pdf)
- SCED_cover_letter_final.docx
- title_page_en.docx, highlights_en.docx, figures_en.pptx (editable)
- Figure_*.png + Supplementary_Figure_*.png separate files, table*.docx
- audit trail docs (CHANGELOG, consistency audit, holdout, provenance,
  comparability, references, hostile review, repro check, Greece check,
  reporting-guideline applicability)

## 10. Reporting guideline
None applicable — see REPORTING_GUIDELINE_APPLICABILITY.md
(PRISMA not applicable: this study is not a systematic review or
meta-analysis). No checklist included.

## 11. Final status
READY FOR SCED SUBMISSION
(remaining caveats are disclosed limitations, not defects: wide
bootstrap intervals, CWON coverage heterogeneity, intangible
double-counting bound, Japan price-revaluation attribution).
