# GATE 0 — Scientific Baseline (frozen record)

Date: 2026-10-16. Source package: `SCED_submission_package_FINAL_v2 (2).zip` (SCED version, rejected 7 Oct 2026). Repo copy: `wip/gdp_tempo_paper` @ master.

## Authoritative files
- Manuscript: `manuscript/manuscript_en.md` → built `SCED_manuscript_submission_final.docx/.pdf` (198 OMML equations, inline figures).
- Supplement: `manuscript/supporting_information_en.md` → `SCED_supplement_submission_final.docx/.pdf` (14 supplementary figures, tables S.1–S.5+).
- Results: `data/*.json`, `data/*.csv`, `tables/*.csv` (frozen; `make reproduce-analysis` regenerates).
- Prior QC/audit: `SCED_FINAL_FINISHING_REPORT.md`, `HOSTILE_REVIEW_FINAL.md`, `NUMERICAL_CONSISTENCY_AUDIT.md`, `identification_surface_summary.md`, `CWON_HOLDOUT_VALIDATION.md`, `FINAL_GREECE_DIRECTIONALITY_CHECK.md`, `FLOW_STOCK_COMPARABILITY_AUDIT.md`, `reviewer_report_economica.md` (present; to be read in Gate 1/5).

## Core research question
How much of the Solow residual and of flow–stock capital disagreement is a *measurement* artefact of two conventions: (a) treating the investment-to-output gestation lag μ as constant/negligible, and (b) omitting intangible capital share β from produced capital?

## Estimands & assumptions
- μ(t) = μ₀ + μ₁·(t−t₀): time-varying mean gestation lag via geometric kernel w_s(μ); θ = μ/(1+μ).
- β: country-specific intangible-capital share entering K_tang + β·K_I.
- Models M0 (instant PIM) → M4 (joint μ,β fitted on production residual + λ·wealth residual, λ=0.3); M_obs = parameter-free tempo proxy from OECD asset-composition × literature lag weights; RPIM (Brass relational model, log–log PIM vs CWON).
- Grids: μ 25 pts 0.01–6.0 yr; β 18 pts 0.00–0.34; μ₁ 11 pts −0.08 to +0.12/yr. Grid search (non-convex); residual bootstrap ×100.

## Data & coverage
PWT 10.01, World Bank CWON (1995–2019+), WDI, OECD GFCF asset detail. 39 OECD/middle-income economies, 1970–2019; M_obs subset = 35 countries with asset-type detail.

## Principal results (verified against data/ outputs)
- OOS MAPE (fit ≤2014 → 2015–19): M0 4.60 % → M2 3.99 % (13 % relative reduction); M1 4.06 %, M4 4.61 %, M_obs 4.17 %. Wilcoxon p = 0.18, n = 39 (not significant).
- K-level gap K_obs/K_M0 − 1, 2010–19 country means: median −4.3 % (IQR −5.3 to −3.8); Ireland −9.2, Costa Rica −7.3, Korea −7.1, Slovakia −6.7, Israel −6.4; least affected Greece −0.6, Japan −1.2, Germany −1.9, Italy −2.1, Portugal −2.6. All 35 negative on country-mean basis; Greece positive in yearly values 2014–19 (+0.7 mean) — disclosed.
- TFP: standard PIM understates log-level TFP by median 1.7 pp (Ireland 4.6 pp). Labour share implied upward shift median 1.7 pp (Korea 3.1, Israel 2.8).
- TFP-growth variance absorbed: tempo alone median 1.7 %, max 13.8 % (NZ); joint median 0.1 %, max 29.7 % (France).
- Intangible counterfactual: ≤1.1 % of produced capital (NLD 1.1, FRA 0.9, NOR 0.9).
- CWON temporal holdout (fit 1995–2014 → 2015–19): median residual joint 4.1 % vs production-only 5.0 % vs M0 5.1 %; joint best in 23/39 (vs M0 27/39).
- Bootstrap 95 % intervals: μ excludes 0 in 39/39; β excludes 0 in 7/39. β̂ median 0.00 (prod-only) / 0.04 (joint); means 0.08 / 0.10.
- RPIM ρ̂₂: 0.801 (M0) → 0.833 (M4); countries in [0.9,1.1]: 9 → 12; gradient on R&D intensity slope 0.068 (t = 2.34) under M4.
- In-sample growth RMSE ~flat across M0–M4 (3.07–3.10 pp) — production fit does not discipline μ.

## Finding categories (kept distinct)
- Measurement decomposition: K gap, TFP/labour-share shifts, variance shares — descriptive.
- Sensitivity: δ ±20 %, μ₁ scaling, M_obs 0.5–2.0× lag robustness.
- Empirical association: RPIM slope on R&D intensity.
- Predictive validation: OOS MAPE + CWON holdout — modest, partly nonsignificant (Wilcoxon 0.18).
- No causal claims; identification via objective-surface narrowing, not point identification.

## Identification limitations (disclosed)
- Joint surface tighter than production-only in only 21/39 (54 %) countries; broad ridge remains for thin-CWON countries (MEX, NZL, CAN, CHE, BEL, LUX, COL).
- β identified partly through CWON conventions; CWON quality heterogeneous (land/subsoil treatment, Japan land-price revaluation likely explains residual Japan gap — γ_price check, S.9–S.10).
- Drifting μ vs drifting δ confound: ±20 % and time-varying δ checks bound but do not eliminate.
- M_obs lag weights are literature-based, not estimated; bounded by 0.5×–2.0× scaling.
- M4 OOS uses oracle convention (future I and L treated as known) — standard but flagged.
- Intangible double counting with rnna/CWON coverage: bounded ≤1.1 %; upper-bound interpretation.
- Business-cycle composition effect on μ(t): untested, stated only as extension.

## Accounting overlap
Produced-capital correction ≤1.1 % bounds overlap between β and assets already in CWON; treated as upper bound.

## Main contribution
First joint time-varying gestation-lag + intangible-share estimation disciplined by a wealth identity across 39 economies; parameter-free observable tempo proxy; Brass relational PIM diagnostic. Claim wording bounded to "to our knowledge".

## Main weaknesses per prior reviews/hostile audit
Identification breadth (7/39 β), modest OOS gains, Wilcoxon n.s., CWON dependence, μ–δ confound, in-sample flatness of production fit, Japan anomaly, fixed-grid edge effects.

## Exclusion list (11 submissions, all excluded)
RIW (desk→reject May 2026), Macroeconomic Dynamics, Economica (×2: Jun + Aug 2026), J. Economic Growth, J. Macroeconomics (fee incurred), Empirical Economics, J. Productivity Analysis, Economic Modelling, Economic Analysis and Policy, SCED.
Decision-stage evidence: desk vs post-review mostly unknown unless correspondence exists; editorial reasons = unknown where no letter.

## Gate 0 verdict: PASS
Authoritative files identified; numbers verified against data/ outputs; no analysis changes made.
