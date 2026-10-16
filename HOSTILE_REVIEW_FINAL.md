# Hostile review (Phase 20) — self-review of the revised package

Reviewer persona: a skeptical SCED referee who has seen the desk-reject
history. Findings ranked by severity.

## Likely referee attacks and current status

1. "The identification claim is overstated." — Mitigated. The text no
   longer claims sharp identification; bootstrap CIs are reported as
   wide, the surface-flatness check is disclosed (joint tighter in only
   54 % of countries), and §6.3 ends with an explicit non-causal
   caveat. Residual risk: a referee may still see the bootstrap
   intervals (median spanning nearly the whole grid) as undermining
   country-level μ̂. We preempt this by framing μ̂ as a
   cross-sectional distribution object, not a country point estimate.
2. "1–2 % flow–stock agreement is fitted in-sample." — Fixed. The
   temporal holdout (Sect. 5.3, SI S.25) now reports honest
   out-of-sample residuals (median 4.1 %) and the paper calls the
   in-sample agreement descriptive.
3. "μ₁ grid asymmetry / cherry-picked bounds." — Fixed. The stated
   grid now matches the code (−0.08 to +0.12, 11 points). The bound
   asymmetry is inherited from the exploratory calibration and is now
   disclosed; a referee can still ask why +0.12 was chosen, but the
   reported IQR [−0.08, +0.12] is at least internally consistent.
4. "Double counting of intangibles already in rnna/CWON." — Disclosed
   in §4.1 caveat; not fully resolvable without asset-level PWT data.
   Acknowledged as an upper-bound interpretation.
5. "Wilcoxon n.s." — Already framed honestly; the paper sells
   measurement, not forecast skill.
6. "Japan anomaly undermines the whole exercise." — Addressed via the
   γ_price revaluation analysis (S.9–S.10) and named as a caveat in
   §6.6.
7. "M_obs lags are literature guesses." — Bounded by the 0.5×–2.0×
   scaling robustness check (Supplementary Table 2) and by the fact
   that M_obs has zero free parameters; the direction matches the
   fitted corrections.

## Residual vulnerabilities (disclosed, not fixable in this revision)
- β̂ is identified partly through CWON's own coverage conventions;
  CWON quality is heterogeneous (stated in §6.6).
- δ mis-measurement could masquerade as tempo drift; the ±20 % and
  time-varying δ checks bound but do not eliminate this (§6.6).
- The M4 oracle convention in OOS evaluation (future I and L treated as
  known) is standard in this literature but worth flagging if refereed.
