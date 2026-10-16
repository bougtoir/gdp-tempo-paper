# GATE 3 — Claim–Evidence Matrix (vs. OBES expectations)

OBES expects: substantive applied contribution, credible estimation/identification, honest uncertainty. Matrix below; labels: SUPPORTED / SUPPORTED WITH QUALIFICATION / UNSUPPORTED / NOT IDENTIFIED.

| # | Claim domain | Specific claim in manuscript | Evidence | Label |
|---|---|---|---|---|
| 1 | Gestation effects | Investment-to-output lag μ is nonzero and varies across countries | M1 μ̂ non-degenerate across 39 (IQR 0.01–2.13 yr); μ CI excludes 0 in 39/39; M_obs corroboration direction | SUPPORTED — but production fit flat in μ; identification via level/holdout not in-sample growth fit |
| 2 | Identifiability | (μ, β) jointly recoverable via wealth constraint | Joint surface tighter in only 21/39; wide bootstrap CIs for short/volatile series; β CI excludes 0 in only 7/39 | SUPPORTED WITH QUALIFICATION — interval identification, not point; must not overstate |
| 3 | Intangible measurement | β captures intangible share omitted from produced capital | β correlated with R&D intensity (slope 0.068, t=2.34); magnitudes ≤1.1 % of produced capital | SUPPORTED WITH QUALIFICATION — β is residual-identified, not directly measured; upper-bound interpretation |
| 4 | Double counting | Adjustment does not double-count intangibles already in CWON | Bounded ≤1.1 % counterfactual; cannot fully exclude without asset-level data | SUPPORTED WITH QUALIFICATION — bounded, disclosed |
| 5 | Capital stock differences | K_obs < K_M0 systematically; median −4.3 % | All 35 M_obs countries negative on 2010–19 means; distribution documented | SUPPORTED — descriptive decomposition, disclosed Greece caveat |
| 6 | TFP/labour-share differences | TFP understated by median 1.7 pp; labour share +1.7 pp | Mechanical consequence of K gap via growth-accounting identity | SUPPORTED — arithmetic, not causal |
| 7 | Cross-country heterogeneity | Effects concentrated where asset mix shifted to long-gestation intangibles | IRL/CRI/KOR/SVK/ISR top-5; least-affected stable-mix economies; cluster analysis (Table 10 series) | SUPPORTED — descriptive association, not causal identification of composition channel |
| 8 | Prediction / OOS | M2 improves OOS level MAPE vs M0 (4.60→3.99 %) | True for median; Wilcoxon p=0.18 n.s.; joint holdout better in 23/39; M4 oracle convention | SUPPORTED WITH QUALIFICATION — modest, nonsignificant; must keep honest framing (already does) |
| 9 | Statistical uncertainty | Bootstrap intervals honest | 95 % bootstrap regions reported; flatness disclosed; Bonferroni caveat offered | SUPPORTED |
| 10 | Generalizability / policy | Implications for potential output, comparability, wealth programs | Logical implications of measurement findings | SUPPORTED WITH QUALIFICATION — normative implication, not empirically tested |

## Estimated quantity vs. interpretation
- μ̂/μ₁ are *objective-surface* estimates on a grid with a sensitivity interpretation (calendar-time drift of effective lag), not identified physical project durations — manuscript already frames this correctly; keep.
- A sensitivity to μ in the level domain is not proof the underlying gestation parameter is physically identified — conditionality must stay explicit where β/μ ride on CWON conventions.

## Gate 3 verdict: **CONDITIONAL PASS**
The core contribution (measurement decomposition + joint identification with honest intervals) is defensible. Two standing conditions for the revision: (i) never let interval identification read as point identification; (ii) keep Wilcoxon n.s. and the 23/39 holdout result visible — concealment is a bigger desk-reject risk than modesty.
