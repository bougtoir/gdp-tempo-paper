# GATE 0 — Baseline file selection (v2 revision)

**Prompt reference**: "manuscript 10.docx" is named as an input candidate in the
revision prompt, but no such file was attached to this session (attachments dir
checked 2026-10-16). The only manuscript artefact present is the ZIP package
from Phase 1 (`submission_obes/pkg/GDP_TEMPO_NEXT_SUBMISSION_FINAL.zip`).

**Authoritative record**: `manuscript/manuscript_en.md` (source of truth) →
`build_docx_pptx.py` → `submission_obes/pkg/manuscript.docx`. The ZIP's
manuscript.docx is byte-identical to a rebuild of that source as of Phase-1
commit; all Phase-2 edits below go through manuscript_en.md + rebuild, never
by patching docx.

Frozen numbers rechecked against `data/`: K gap median −4.29% IQR
[−5.29,−3.77] n=35; TFP −1.74pp / LS +1.74pp; OOS M0 4.60% vs M2 3.99%,
Wilcoxon p≈0.18 n=39; CWON holdout joint 4.1% best in 23/39; intangible ≤1.1%;
tempo ≤13.8% (NZL), joint ≤29.7% (FRA); RPIM ρ̂₂ 0.801→0.833. All consistent.
