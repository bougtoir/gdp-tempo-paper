# GATE 5 — Hostile Editorial Review (OBES-targeted version)

Simulated: skeptical handling editor + Referee A (growth accounting) + Referee B (national accounts/capital measurement).

## Editor — "why OBES, and does it merit review?"
- *Attack*: "Eleven rejections; a measurement-curiosity paper." Response: the OBES-published literature this directly extends (dal Borgo et al. 2013; Corrado et al. 2017) is the journal's own research line; the paper adds the timing dimension that line lacks. Verdict: credible fit, not desk-rejectable on scope.
- *Attack*: "Demographic analogy is decorative." Partially true rhetorically — but it is load-bearing methodologically (tempo–quantum decomposition is literally the estimator). Keep it but flagged as the first thing a hostile editor cuts. **Status: ACCEPTABLE — already positioned as hook, not centerpiece.**

## Referee A — Growth accounting

1. **"μ is not identified — production-side fit is flat in μ."** Valid in-sample; the paper already concedes this and leans on the level/holdout evidence. The honest residual weakness: for the 18/39 countries where the joint surface is not tighter, μ̂ is essentially prior-driven by the grid. Manuscript says this. **MAJOR BUT REPAIRABLE → resolved in text: verify §6.3 states this plainly** (it does; see Resolution Log R1).
2. **"Wilcoxon p=0.18 — headline OOS claim is not significant."** Paper reports it. The correct reviewer reading is "consistent direction, underpowered test (n=39)", which the framing supports. **ACCEPTABLE LIMITATION.**
3. **"M_obs lags are literature guesses — circular."** Bounded by 0.5–2.0× scaling robustness and zero free parameters; direction agreement is informative, magnitudes less so. Disclosed. **ACCEPTABLE.**
4. **"μ(t) vs δ(t) confound is the real killer."** Strongest objection: if depreciation drifts, tempo estimates absorb it. ±20 % δ and time-varying-δ checks bound but cannot exclude; no capacity-utilization/retirement data cross-country. **MAJOR — disclosed in §6.6 as disclosed limitation; cannot be eliminated with existing data → ACCEPTABLE LIMITATION with explicit flag, not a claim-destroyer because it does not change the direction of the K-gap result (only attribution share).**
5. **"Why should a 4 % K level gap matter?"** Because it is systematic, concentrated in exactly the countries whose investment mix shifted most, and propagates mechanically to TFP (+1.7 pp) and labour share (+1.7 pp). Magnitudes modest — the claim is calibrated accordingly. **ACCEPTABLE.**

## Referee B — National accounts / capital measurement

6. **"PWT capital vs CWON produced capital are different universes (units, PPP, base years)."** Handled by within-country demeaned log comparison + level normalisation fitted pre-2015 only. Legitimate criticism of comparability limits — partially mitigated. **ACCEPTABLE LIMITATION.**
7. **"Double counting: some intangibles are already in CWON produced capital."** Bounded ≤1.1 %; acknowledged as upper bound. **MINOR — disclosed.**
8. **"Japan anomaly — PIM rises while CWON flattens."** γ_price analysis suggests land-price revaluation; disclosed. A referee could demand more; cannot be resolved without land-price series (out of data scope). **ACCEPTABLE LIMITATION.**
9. **"Geometric kernel is ad hoc."** True — a maintained assumption. M_obs sidesteps it for direction. **MINOR.**
10. **"M4 oracle convention in OOS (future I, L known)."** Standard but should be flagged — **MINOR, add one clause if absent** (Resolution Log R2).

## Strongest desk-rejection argument
"An 11-times-rejected measurement paper whose central identification is an objective-surface narrowing exercise on a grid, with a nonsignificant headline test." — Countered only by: the journal-literature fit (OBES's own intangible-productivity line), the interval-honest reporting, and the parameter-free corroboration. This is the paper's real risk and cannot be argued away; it is priced into target selection.

## Strongest reason to send to review
Direct extension of literature the journal published; novel joint identification; reusable proxy (M_obs) applied researchers can compute; honest uncertainty reporting — exactly the "practical measurement" profile OBES states it wants.

## Highest-value single revision
R1 — make the 21/39 surface-narrowing fact impossible to miss in §5–§6 (it is present; verified). No further prose changes beyond a one-clause flag of the M4 oracle convention.

## Classification summary
- BLOCKER: none found.
- MAJOR BUT REPAIRABLE: R1 (surface narrowing prominence) — done.
- MINOR: R2 (oracle-convention flag) — done.
- ACCEPTABLE LIMITATIONS: μ–δ confound, Japan gap, Wilcoxon n.s., CWON quality, demeaning comparability, double-count bound.
