# Reference and novelty audit (Phase 12)

## Reference verification
`scripts/verify_references.py` re-run 2026-09-27: all 37 references
resolve via DOI or Crossref title match. The only flagged item is Brass
(1971), "On the scale of mortality" — a real book chapter in
*Biological Aspects of Demography* (Taylor & Francis) with no DOI;
the tool's title-match heuristic returned an unrelated result but the
reference itself is genuine and correctly cited. Status: PASS.

## Novelty positioning
- Time-varying time-to-build in growth accounting: no prior cross-country
  estimation found; closest fixed-lag work is Kydland–Prescott (1982),
  Koeva (2000), Kaboski (2005), Edge (2007) — all cited in §2.
- Joint estimation of (μ, β) against a wealth identity: no prior work
  combining production residuals with CWON produced capital found.
- Brass relational model applied to capital accounting (RPIM): no prior
  application found; Brass (1971) and Bongaarts–Feeney (1998) cited as
  the demographic source.
- Observable tempo proxy from OECD asset composition (M_obs): original
  construction; related composition evidence in OECD (2013) and
  Corrado et al. (2020).

Claims are now bounded: "to our knowledge" phrasing retained where the
absence-of-prior-work assertion is made (§2, §3.4); no "first ever"
language.
