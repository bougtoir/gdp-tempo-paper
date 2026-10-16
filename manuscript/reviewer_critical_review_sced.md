# Reviewer-critical review for *Structural Change and Economic Dynamics* submission

**Target journal:** *Structural Change and Economic Dynamics* (SCED, Elsevier)
**Date:** 2026-09-27
**Scope:** Pre-submission critical review of the gdp_tempo_paper package after the EAP desk rejection (EAP-D-26-04338; tenth consecutive desk rejection — see `next_journal_candidates.md`).

This review follows the internal checklist: manuscript novelty/focus/logic; statistical design; figures/tables; reproducibility; and strength of claims.

## Diagnosis carried over from ten desk rejections

The accumulated record (RIW, Macroeconomic Dynamics, Economica x2, JEG, J. Macro, Empirical Economics, JPA, Economic Modelling, EAP) shows the paper dies at the desk, i.e. on title + abstract + introduction. Three structural problems recur:

1. **Claim–result gap.** "The Solow residual as a measurement artefact ... and Macroeconomic Policy" promises a sweeping recasting of TFP and a policy agenda; the delivered magnitudes are modest and partly insignificant (median TFP +1.7 pp, capital −4.3 %, OOS MAPE 4.60 % → 3.99 %, Wilcoxon non-significant, n = 35). Editors read that as over-claiming.
2. **Diffuse focus.** Models M0–M4 plus M_obs, RPIM diagnostics, cluster analysis, Monte Carlo, counterfactual wealth, historical episodes, and 2020–2040 projections compete for attention; the core contribution (joint identification of μ(t) and β, and the K/TFP/labour-share corrections it implies) is buried.
3. **Weak motivation in the introduction.** The opening sells a *policy* paper (output gaps, fiscal rules, monetary transmission) that the results do not support at causal-policy strength, while the genuinely novel framing — structural change in investment composition breaks the timing assumptions of national-accounts capital construction — appears only in paragraph 3.

SCED's scope (structural change in economic and technological patterns; econometric and statistical methods applied to those themes) fits the paper only under the measurement framing: the secular shift of investment toward long-gestation intangible assets is a *structural-change* fact, and the paper quantifies what it does to measured capital and productivity. The reframing below implements that.

## Reframing implemented for SCED

1. **Title** — dropped the "Macroeconomic Policy" subtitle and the artefact slogan. New title: "Investment gestation lags, intangible capital, and the measurement of capital and productivity in 39 economies".
2. **Abstract / keywords / JEL** — removed the closing policy sentence and "macroeconomic policy" keyword; JEL narrowed to measurement/productivity codes (E01, E22, O33, O47; dropped E44, E52, E62).
3. **Introduction** — the first two paragraphs were re-anchored on structural change in investment composition (shift toward software, R&D, long-lead systems) rather than policy calibration. The Korea-1997 episode promise ("several percentage points") and the three policy implications were removed; implications are now stated as measurement consequences.
4. **Focus** — the counterfactual produced-capital revaluation paragraph and the historical-episode narrative were removed from the main text (they remain in SI S.4/S.16/S.17); Section 5 now runs: model comparison → OOS → flow–stock consistency → K/TFP/labour-share corrections → variance decomposition.
5. **Discussion** — Section 6.4 ("Concrete policy implications") was replaced by "Implications for measurement practice and comparability"; fiscal/monetary recommendations are reduced to two sentences that flag direction only.
6. **Claims** — throughout, "policy relevance" language was replaced by measurement language; the Wilcoxon non-significance is reported up-front; causal verbs removed.

## Remaining concerns (ranked)

### Highest priority (must fix before submission)

- **Submission fee:** SCED charges USD 100 (since 2025-01-01), refundable if accepted; payable in Editorial Manager. Authors in applicable countries pay VAT on top. Confirm payment method before submitting.
- **Single-anonymized review** (not double): the anonymized-main-text setup is still correct, but the cover letter and title page carry author identity as normal. No risk, but verify the EM field labels.
- **Highlights:** required by Elsevier for this journal; 3–5 bullets, ≤ 85 characters each — rewritten and length-checked in `manuscript/highlights_en.md`.
- **Abstract length:** kept ≤ 250 words.

### High priority

- Figures are embedded inline in the docx **and** supplied as separate files + editable pptx, matching Elsevier's either/or tolerance; captions retained in text.
- "Companion paper (in preparation)" paragraph removed from the literature review — uncitable self-reference that diffuses focus.
- All numerical claims remain generated from result CSV/JSON by `scripts/build_docx_pptx.py` — no hard-coded numbers added by the reframing edits.

### Medium priority

- The JA-language manuscript (`manuscript_ja.md`) is not updated by this reframing and is excluded from the SCED zip; rebuild it only if needed.
- SI is large (17 sections); acceptable for SCED, but the main text now explicitly road-maps it.

### Reproducibility checklist

- [ ] `python scripts/reproduce.py` regenerates results and documents (run on this branch before PR).
- [ ] `python scripts/audit_submission.py` clean.
- [ ] `python scripts/verify_references.py` — all references exist.
- [ ] No CJK characters in English deliverables; equations OMML (latex2word) — enforced by the build script.
- [ ] Public repo `bougtoir/gdp-tempo-paper` syncs this branch via `sync-to-repos.yml`.
