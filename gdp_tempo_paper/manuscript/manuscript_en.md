# Time-Varying Time-to-Build in Capital Accounting: Reconciling Flow- and Stock-Based National Wealth Measures through a Time-Varying Perpetual Inventory Method with Intangible Capital

**Tatsuki Onishi**

Data Science AI Innovation Research Promotion Center, Shiga University

1-1-1, Bamba, Hikone, Shiga, 522-8522 Japan

Telephone: +81-749-27-1023. E-mail: bougtoir@gmail.com. ORCID: 0000-0001-7261-9062.

**Keywords**: time-to-build; perpetual inventory method; intangible capital; national wealth accounting; flow-stock consistency; Beyond-GDP.

**JEL codes**: E01 (Measurement and Data on National Income and Product Accounts); E22 (Investment; Capital; Intangible Capital); O47 (Measurement of Economic Growth; Aggregate Productivity).

**CRediT contribution statement.** O.T.: Conceptualization, Methodology, Software, Formal analysis, Writing - original draft, Writing - review & editing.

**Declaration of generative artificial intelligence (AI) in scientific writing.** We used generative AI to help with formatting the text and choosing words that suited the tone, and to help writing codes.

**Conflict of interest.** The author declares no conflict of interest.

**Data and code availability.** Penn World Table 10.01 and World Bank CWON data used in this study are publicly available from the Groningen Growth and Development Centre and the World Bank, respectively. All analysis scripts, intermediate results, and manuscript sources are archived in the accompanying public repository.

---

**Abstract** (145 words). Standard perpetual-inventory capital stocks assume that investment contributes to productive capacity immediately (zero time-to-build) and that intangible capital is absent. We relax both assumptions simultaneously, allowing the mean investment-to-output lag μ(t) to drift linearly over time and augmenting the production function with an R&D-based intangible stock weighted by share β. Across 39 OECD and middle-income economies (Penn World Table 10.01, World Bank CWON), allowing a positive time-to-build reduces the median out-of-sample MAPE of GDP level forecasts from 4.60% to 4.06%; allowing μ(t) to drift further reduces it to 3.99%. Adding intangible capital alone does not improve prediction (MAPE 4.72%), but jointly identifying (μ, β) against both production and wealth data reconciles the flow and stock accounts to within 1–2% for most advanced economies. The heuristic analogy to demographic tempo effects (Bongaarts-Feeney, Goldstein-Lutz-Scherbov) is outlined, with explicit discussion of where the analogy holds and where it breaks down.

**Keywords**: time-to-build; perpetual inventory method; intangible capital; wealth accounting; Beyond-GDP.

**JEL codes**: E01, E22, O47.

---

## 1. Introduction

Every macroeconomist has encountered two separate but related complaints about the way we measure national prosperity. First, Gross Domestic Product (GDP) is a flow measure that ignores depletion, depreciation, and the growing stock of intangible assets that drives modern productivity growth (Stiglitz, Sen, and Fitoussi, 2009; Corrado, Hulten, and Sichel, 2009; Haskel and Westlake, 2017). Second, stock-based alternatives such as the Inclusive Wealth Index (Managi and Kumar, 2018), the United Nations SEEA (UNECE, 2014), and the World Bank Changing Wealth of Nations (Lange, Wodon, and Carey, 2018) are attractive in principle but rarely line up with independently reconstructed capital stocks and never with one another. Flow-based and stock-based national accounts have lived side by side for twenty-five years without being reconciled.

This paper argues that a substantial share of this discrepancy can be attributed to two specification choices in the standard perpetual inventory method (PIM): the assumption that investment contributes to productive capacity immediately (zero time-to-build), and the exclusion of intangible capital from the production function. We relax both assumptions simultaneously. We allow the mean investment-to-output lag μ(t) to drift linearly over time, and we augment the production function with an R&D-based intangible capital stock weighted by a share parameter β. The key empirical finding is that recognising a positive time-to-build — with or without time variation — reduces the median out-of-sample GDP level forecast error from 4.60% to 4.06% across 39 OECD and middle-income economies, a 12% relative improvement. Adding a linear drift to μ(t) reduces it further to 3.99%. Intangible capital alone does not improve out-of-sample prediction (MAPE 4.72%), but jointly identifying (μ, β) against both production data (Penn World Table) and wealth data (World Bank CWON) reconciles the flow and stock accounts to within 1–2% for most advanced economies. The joint identification also reveals that neither parameter is well identified from production data alone; the wealth-side constraint is essential.

The demographic analogy that motivates the joint treatment of μ and β is a heuristic borrowing from Bongaarts and Feeney (1998) and Goldstein, Lutz, and Scherbov (2003). In demography, a rising mean age at childbearing was shown to depress period fertility mechanically, and a "forgotten" parity-specific variance parameter was shown to restore the consistency between period and cohort accounts. The structural similarity — a flow statistic contaminated by drift in a timing distribution, with a single omitted quantity parameter — is suggestive. However, a caveat is in order from the outset. The time-to-build in capital accounting is a gestation lag with a clear engineering interpretation (Kydland and Prescott, 1982), not a statistical artifact of period-cohort aggregation. The demographic tempo adjustment corrects a purely compositional bias; the capital-accounting adjustment corrects a production-function timing mis-specification. The two problems involve different statistical objects and different identifying assumptions. The analogy is a useful pedagogical device and a source of hypotheses, not a claim of formal equivalence. We return to this distinction in Sections 3.4 and 6.2.

The remainder of the paper is organised as follows. Section 2 reviews the relevant literatures in capital accounting, intangible capital, and wealth measurement. Section 3 develops the time-varying PIM production function, the intangible augmentation, and the joint flow-stock identification framework. Section 4 describes the data, the five nested models M0–M4, and the estimation protocol. Section 5 reports results, including out-of-sample forecasts, flow-stock reconciliation, and bootstrap confidence intervals. Section 6 discusses implications for the interpretation of the Solow residual, the demographic analogy, and the Beyond-GDP debate, and explicitly states limitations. Section 7 concludes.

## 2. Related literature

### 2.1 Capital accounting, PIM, and asset-specific measurement

The perpetual inventory method (PIM) is the standard framework for constructing capital stocks in national accounts and in cross-country datasets such as the Penn World Table (PWT; Feenstra, Inklaar, and Timmer, 2015). The OECD *Measuring Capital* manual (OECD, 2009) codifies best practice: asset-specific service lives, age-efficiency profiles (geometric, linear, or hyperbolic), and vintage corrections. The PIM is not a single equation but a family of implementations whose accuracy depends on how well the assumed retirement and depreciation patterns match the actual composition of investment.

A large empirical literature has estimated time-to-build parameters from project-level and industry-level data. Mayer (1960) found mean gestation lags of 1–2 years for US manufacturing plant and equipment. Koeva (2000) reported similar estimates from cross-country aggregates. Kydland and Prescott (1982) embedded a multi-period investment lag in a business-cycle model and showed it improves propagation of technology shocks. Kaboski (2005) documented cross-industry heterogeneity — construction and mining have longer lags than retail and services — but estimated time-invariant lags within each industry. Altug (1989), Christiano and Todd (1996), and Edge (2007) allowed the lag distribution to vary with sectoral composition or stochastic structure, but did not allow the mean lag to drift systematically over the multi-decade horizons that characterise the post-1990 shift toward intangible-intensive investment.

Our work builds on this literature by letting the mean time-to-build drift linearly over time. While sectoral composition change has been the most studied channel through which the aggregate lag could evolve (OECD, 2009, Chap. 5), we model the drift parsimoniously as a linear trend, without attributing it to any single structural cause. A complementary tradition — vintage capital models (Solow, 1960; Jorgenson, 1973; Hulten, 1992) — recognises that capital of different vintages embodies different technologies and therefore different effective ages. Our approach is distinct from and simpler than vintage models: we do not track each vintage separately but instead adjust the timing with which all investment enters the stock, which is a coarser but more tractable correction for the aggregate production-function context.

We also acknowledge a limitation that the asset-specific PIM literature would flag: our aggregate μ(t) collapses potentially heterogeneous asset-level lags into a single parameter. If short-lived equipment (IT hardware, vehicles) and long-lived structures (R&D labs, power plants) have diverging lag trends, the aggregate μ(t) may mask offsetting compositional shifts. Section 6.5 discusses the implications.

### 2.2 Intangible capital

The programme begun by Corrado, Hulten, and Sichel (2005, 2009) has by now produced robust international evidence that software, R&D, design, brand, organisational capital, and training account for 30–60% of productivity growth in advanced economies (INTAN-Invest: Corrado et al., 2016; Roth, 2023). The 2008 revision of the SNA formally incorporated R&D into produced capital, but broader intangibles — organisational capital, brand, training, purchased design services, some categories of financial innovation — remain excluded from most official balance sheets, including the World Bank CWON (Lange et al., 2018, Chap. 3). De Rassenfosse and Jaffe (2018) and Haskel and Westlake (2017, 2022) emphasise that this omission biases not only the level of measured capital but also the implied productivity growth rate whenever the intangible share is expanding.

Our treatment follows CHS (2009) in assuming a geometric PIM for intangible capital with a fixed depreciation rate δ_I = 0.15. This is a deliberate simplification. More recent work (Corrado et al., 2020) uses asset-specific depreciation rates for different intangible categories, which would refine the measurement. However, given that our R&D expenditure data are at the national aggregate level and our sample spans 39 countries with varying data quality, the single-depreciation assumption is a necessary compromise. Importantly, the intangible share β is not a global constant: Japan, Germany, and some East-Asian economies retain a smaller intangible share than the United States even under harmonised measurement (Corrado et al., 2020), so β ought to be a country-specific parameter, which is how we treat it in Section 4.

### 2.3 Wealth accounting and flow-stock reconciliation

The Beyond-GDP movement, from Stiglitz-Sen-Fitoussi (2009) through Jorgenson (2018) and Managi-Kumar (2018), proposes to replace or augment GDP with wealth-style aggregates. Empirically, however, the three main aggregates — SEEA, IWI, and CWON — disagree materially both with each other and with independently reconstructed perpetual-inventory stocks (Arrow et al., 2012; Dasgupta, 2021). The mainstream diagnosis blames measurement error and the treatment of natural capital. We show that a more mundane culprit — a mis-specified time-to-build and an omitted intangible share — explains a sizeable fraction of the discrepancy.

A separate strand of work has examined the consistency between flow-based and stock-based accounts from an accounting-identity perspective. Jorgenson (2018) emphasises that the production and wealth accounts are linked by the accumulation identity *dW/dt = S(Y) − δW*, but notes that empirical implementations rarely enforce this linkage. Our joint identification framework (Section 3.3) is a direct econometric application of this identity, which distinguishes it from most existing wealth-accounting studies that treat the production and wealth sides independently.

### 2.4 Tempo effects in demography: a heuristic analogy

Bongaarts and Feeney (1998) introduced the adjustment *TFR\** = *TFR*/(1 − *r(t)*) where *r(t)* is the annual change in the mean age at childbearing. Goldstein, Lutz, and Scherbov (2003) showed that Bongaarts-Feeney was an upper bound unless a parity-specific "forgotten" variance σ was re-introduced. Kohler, Billari, and Ortega (2002) and Bongaarts and Sobotka (2012) confirmed both findings across Europe. The structural lesson — that flow statistics of a stock process can be contaminated by drift in the timing distribution, and that a single omitted quantity parameter can restore consistency — is the heuristic that motivates our joint treatment of μ and β.

We emphasise that this is a heuristic analogy, not a formal identity. The demographic tempo effect corrects a compositional bias arising from period-cohort aggregation in heterogeneous populations. The capital-accounting correction adjusts a production-function timing mis-specification. The mathematical forms are similar (a distributed lag with a drifting mean), but the identifying assumptions and the interpretation of the parameters differ. We use the demographic vocabulary ("tempo", "forgotten parameter") as a pedagogical convenience and to highlight the structural symmetry, but we do not claim that the two problems reduce to the same statistical object.

### 2.5 The gap this paper fills

The literatures above individually treat (i) capital time-to-build, (ii) intangibles, (iii) wealth aggregates, and (iv) demographic tempo. To our knowledge, no prior work simultaneously (a) estimates a time-varying time-to-build, (b) recovers the CHS intangible share, and (c) disciplines both with a wealth-accounting identity. A secondary contribution is to treat the PIM and the wealth-stock equations as two equally informative windows onto the same latent process rather than as competing aggregates whose disagreement is a nuisance to be absorbed into residuals.

## 3. Theory

### 3.1 Flow-side production function with time-varying time-to-build

The textbook production function treats investment as if it matures instantly:

    K_instant(t) = (1 − δ_{t-1}) K_instant(t−1) + I_{t-1},                         (M0)

so the Solow (1957) residual aggregates all mis-specification into total factor productivity (TFP). Since Mayer (1960) and Kydland-Prescott (1982) it is well known that, in reality, investment accrues to the stock only after a lag. We write this as a distributed-lag perpetual inventory:

    K(t; μ) = (1 − δ_{t-1}) K(t−1; μ) + Σₛ w_s(μ) I_{t-1-s},                     (M1)

with geometric weights *w_s(μ) = (1 − θ)·θ^s* and *θ = μ/(1+μ)*, so the mean lag is exactly *μ* years. Our first extension is to allow μ to drift linearly over time:

    μ(t) = μ₀ + μ₁·(t − t₀),                                                    (M2)

where μ₁ captures the secular trend in the mean time-to-build. A positive μ₁ indicates that typical projects are becoming longer-lived — for example because new investment is increasingly digital infrastructure, R&D platforms, or complex systems that require multi-year assembly — and a negative μ₁ would indicate the opposite.

Equation (M2) is a reduced form. We do not attribute the drift to any single structural cause; it could reflect sectoral composition change (OECD, 2009), rising intangible intensity (Corrado et al., 2016), or regulatory lengthening of project approval times. The linear specification is the simplest possible and is motivated by the demographic literature's treatment of the mean age at childbearing (Bongaarts and Feeney, 1998), but we emphasise that this is a modelling choice rather than a structural estimate. We test a constant-lag alternative (M1) alongside M2 in all specifications.

### 3.2 Stock-side intangibles

Let *K_tang(t)* be the tangible PIM stock from (M1)–(M2) and *K_I(t)* be an intangible stock built from R&D expenditure by a geometric PIM with depreciation δ_I = 0.15 (Corrado-Hulten-Sichel, 2009). A production function augmented by intangibles reads:

    log Y_t = α log K_tang(t) + β log K_I(t) + (1 − α − β) log L_t + log A_t,    (M3)

where β is the intangible output share. Standard practice imposes β = 0 (Solow; also M0 and M1 here). We estimate β per country.

### 3.3 Unifying identity: the flow-stock joint loss

Any consistent national wealth aggregate *W(t)* must satisfy the book-keeping identity

    dW/dt = S(Y) − δ_W · W,                                                       (1)

where *S(Y)* is gross saving and *δ_W* is the aggregate depreciation rate. Under (1), the same parameters {μ, β} that govern the production side should also govern the reproducible-capital trajectory implied by the wealth account. We therefore define a single joint loss:

    L_total(μ, β) = L_production(μ, β) + λ · L_wealth(μ, β),                      (2)

where *L_production* is the growth-rate residual from the production function (M3) and *L_wealth* is the within-country trajectory RMSE between the PIM stock *K_tang(t; μ) + β · K_I(t)* and the CWON produced-capital series NW.PCA.TO(t). Minimising (2) delivers the "M4 joint" estimates (μ̂_joint, β̂_joint) used below; setting λ = 0 recovers production-only estimates.

### 3.4 Relational PIM: a new identification framework (M5)

A limitation shared by M0–M4 is that the PIM stock is constructed independently of wealth data; the CWON series enters only through the penalty term in (2). We now introduce a method that treats the wealth account as an explicit benchmark for the capital stock trajectory, analogous to the Brass relational model in demography.

The Brass (1971) relational model expresses a target life-table function as a linear transformation of a standard life-table function. When Goldstein, Lutz, and Scherbov (2003) re-introduced the parity-specific variance σ as the "forgotten parameter," they effectively estimated a relational model in which the period fertility schedule was related to a cohort standard through two parameters: a level shift and a slope (spread) parameter.

We port this logic to capital accounting. Let *K_CWON(t)* be the produced-capital series from the World Bank CWON, and let *K_PIM(t; μ, β)* be the PIM-constructed capital stock. Define the relational model:

    log K_PIM(t; μ, β) = ρ₁ + ρ₂ · log K_CWON(t) + ε(t),                         (M5)

with ε(t) assumed stationary. The parameters (ρ₁, ρ₂) are novel diagnostic quantities:

- **ρ₂ ≈ 1, ρ₁ ≈ 0**: the PIM and CWON accounts agree up to random noise — the benchmark case.
- **ρ₂ ≠ 1**: a systematic bias exists: if ρ₂ < 1, the PIM stock is compressing the wealth account's movements (e.g., because the PIM's geometric depreciation smooths out asset-price revaluations that CWON captures). If ρ₂ > 1, the PIM stock is amplifying them.
- **ρ₁** captures the mean log-level difference between the two accounts after controlling for the slope.

The key methodological innovation is to use (M5) as an *identification device* rather than a post-estimation diagnostic. We define the **M5 estimator**:

    (μ̂_M5, β̂_M5) = argmin_{μ, β} L_total(μ, β),
    subject to: ρ̂₂(μ, β) ≥ 1 − τ  and  |ρ̂₁(μ, β)| ≤ ν,

where ρ̂₁ and ρ̂₂ are the OLS estimates from (M5) evaluated at the candidate (μ, β), and τ and ν are user-specified tolerance parameters (we set τ = 0.10 and ν = 0.05 in the baseline, and test sensitivity). The constraint ensures that the PIM stock is not systematically compressing or amplifying the wealth-account trajectory beyond a pre-specified tolerance. This is a **relational PIM** (RPIM): the wealth account constrains the PIM not through a black-box penalty weight λ but through an explicit diagnostic that has a direct demographic analogue.

The estimator differs from M4 in two ways. First, M4 minimises an unconstrained weighted sum of production and wealth losses; M5 imposes an explicit constraint on the (ρ₁, ρ₂) diagnostic, which is interpretable as "the PIM stock must respect the shape of the wealth-account trajectory." Second, the M5 framework produces (ρ₁, ρ₂) as by-products that can be compared across countries — a new set of diagnostic statistics for national accounts consistency — whereas M4's λ is a scalar whose value is difficult to compare across settings.

We also note a natural connection to the δ-drift problem (Section 6.5). If ρ₂ < 1 for a country even after joint estimation, one interpretation is that the PIM depreciation rate δ_t is too high, causing the stock to converge too rapidly toward a steady-state level; a downward adjustment of δ would shift ρ₂ toward unity. We explore this in the δ-ρ₂ sensitivity analysis below.

### 3.5 Heuristic correspondence between population and capital accounting

Table A1 (Appendix) lays out the mapping between the demographic variables that Bongaarts-Feeney-Goldstein-Lutz-Scherbov analysed and the capital-accounting variables we analyse. We include this mapping for two reasons. First, it helps readers familiar with the demographic literature to see the structural parallels. Second, it highlights where the analogy breaks down: capital stocks depreciate via an estimated δ_t rather than via well-measured mortality rates, and the time-to-build is a gestation lag rather than a period-cohort aggregation bias. The mapping is a pedagogical device, not a formal equivalence.

## 4. Data and methods

### 4.1 Data

We use **Penn World Table 10.01** (Feenstra, Inklaar, and Timmer, 2015) for real GDP output (*rgdpna*), tangible capital stock (*rnna*), investment share (*csh_i*), depreciation (*delta*), employment (*emp*), average hours (*avh*), human-capital index (*hc*), and labour share (*labsh*). For R&D intensity we use **World Bank WDI** series *GB.XPD.RSDV.GD.ZS*. For wealth we use **World Bank Changing Wealth of Nations** 2021 release (Lange, Wodon, and Carey, 2018) — specifically *NW.PCA.TO* (produced capital total), *NW.HCA.TO* (human capital total), and *NW.TOW.TO* (total wealth).

The sample is 39 OECD and middle-income economies for which all series are available. The GDP sample runs from 1970 to 2019; CWON runs 1995–2020; we take the intersection 1995–2019 when both are needed.

### 4.2 Models M0–M5 and additional benchmarks

We estimate six nested production-function specifications:

* **M0**: Solow baseline, *K_tang* as (M0), β = 0.
* **M1**: Constant-lag PIM (M1) with *μ = μ*\* estimated per country by minimising Test B (growth-rate RMSE).
* **M2**: Time-varying lag μ(t) = μ₀ + μ₁·(t − t₀) from (M2).
* **M3**: M0 tangible stock augmented with intangible stock K_I and β estimated by growth-rate fit.
* **M4**: Joint identification (Section 3.3), minimising (2) over (μ, β) simultaneously against CWON.
* **M5**: **Relational PIM (RPIM)**, as defined in Section 3.4. Minimises (2) subject to the (ρ₁, ρ₂) constraints ρ̂₂ ≥ 0.90 and |ρ̂₁| ≤ 0.05.

To address the question of whether the improvement in fit comes from allowing *any* positive lag versus specifically from the time variation in μ(t), we also estimate two additional benchmarks:

* **M1a (AR(1) distributed lag)**: K(t) = (1 − δ)K(t−1) + φ·I(t−1) + (1−φ)·I(t−2). This is a fixed two-period distributed lag with a single parameter φ ∈ [0, 1] estimated per country, which nests M0 (φ = 1) and M1 with μ = 1 (φ = 0) as special cases. Unlike M1, M1a does not use the geometric lag kernel; it provides an alternative non-parametric benchmark against which the geometric assumption of M1–M2 can be tested.
* **M2a (broken-trend μ)**: μ(t) = μ₀ + μ₁·max(0, t − t_break), where t_break is a single structural break estimated by grid search over {1990, 1995, 2000, 2005, 2010}. This tests whether the linear drift in M2 is driven by a single regime change rather than a gradual trend.

For each model we report two within-sample test statistics and one out-of-sample test statistic:

* **Test A (level MAPE)**: mean absolute percentage error of fitted log-GDP against observed log-GDP, decomposing away decade-mean TFP. Lower is better.
* **Test B (growth RMSE)**: root-mean-squared error of 1-year log-GDP differences, in percentage points. Lower is better.
* **Out-of-sample MAPE**: parameters fit on 1970–2014, level forecasts produced for 2015–2019 with a training-window TFP projection. Lower is better.

### 4.3 Estimation protocol and grid search

All five models are estimated by grid search, not gradient optimisation, for three reasons. First, the objective function (2) has known non-convexities induced by the geometric lag kernel, especially when μ is small and the kernel is near-concentrated. Second, grid search produces an explicit posterior-like surface for each (country, model) pair, which we use in the sensitivity checks below. Third, the 39-country × 5-model × 1000-draw bootstrap would be intractable with a Nelder-Mead or BFGS inner loop for many countries. The μ grid is {0.01, 0.05, 0.10, 0.25, 0.50, 1.0, 1.5, 2.0, 3.0, 4.5, 6.0} years and the β grid is {0.00, 0.02, 0.04, ..., 0.34}; μ₁ is searched on {−0.08, −0.04, −0.02, 0, +0.02, +0.04, +0.08} per year. These bounds were selected to bracket all plausible parameter values reported in prior cross-country studies (Kaboski, 2005; Corrado et al., 2016), and we verified that no country's optimum hits the grid boundary. The anchor year t₀ is 1970 for all countries, so that μ₀ is the average lag in the base year; this choice has no effect on fit but makes μ₀ and μ₁ interpretable.

### 4.4 Bootstrap confidence intervals

For every country we residual-bootstrap the growth-rate residuals of M4 one hundred times (block size 1, since the autocorrelation structure of PWT annual-growth residuals is weak after detrending; block size 3 gives nearly identical 95 % intervals on a pilot of five countries). Each bootstrap replicate proceeds as follows: (i) compute fitted growth rates from M4 and the corresponding residuals; (ii) resample the residuals and reconstruct a synthetic log-GDP series; (iii) back out a synthetic investment series using the PWT investment-share *csh_i* and a synthetic R&D intensity using WDI shares; (iv) rebuild *K_tang* and *K_I*; (v) re-run the joint-identification grid, storing (μ_b, β_b). We report 95 % percentile intervals in Figure 3 and per-country medians in the supplementary JSON. Country-specific CIs are narrowest for long, non-volatile series (United States, Canada, Germany, France, United Kingdom, Japan, Australia) and widest for short or post-transition series (Estonia, Latvia, Chile). We do not adjust the 95 % intervals for multiple testing across countries; the reader who wants a conservative reading should apply a Bonferroni-style 5 %/39 ≈ 0.13 % threshold, under which μ = 0 is still rejected for 14 countries and β = 0 for 9 countries.

### 4.5 γ_price sensitivity

To test whether the residual PIM-CWON gap in countries such as Japan reflects an asset-price re-evaluation effect rather than a real capital gap, we re-run the comparison under five counterfactual scenarios in which CWON PCA is inflated/deflated at an annual rate γ_price ∈ {−0.04, −0.02, 0, +0.02, +0.04}. A large γ_price sensitivity for a specific country would indicate that asset-price revaluation explains most of its gap; a small sensitivity would indicate a genuine real discrepancy. The interval ±0.04 per year brackets the observed rate of deflation in Japanese urban land prices during the 1990s (Nishimura and Saita, 2005) as well as the observed rate of reflation in US commercial real-estate between 2009 and 2019, so the grid is economically meaningful rather than arbitrary. We stress that γ_price is not intended to be an additional estimand of the joint framework — if it were, it would enter (2) alongside μ and β. Rather, it is a diagnostic: a residual gap between the PIM account and the CWON account at a specific γ_price value admits exactly one of three interpretations, namely (a) quantity mis-measurement in the PIM, (b) quantity mis-measurement in CWON, or (c) genuine composition change (e.g. a real shift from tangible to intangible capital that neither account has fully absorbed). The γ_price sweep helps identify (a) and (b) against (c).

### 4.6 δ-ρ₂ joint sensitivity

As noted in Section 3.4, the ρ₂ diagnostic from (M5) is informative about potential δ-drift. If a country's estimated ρ₂ is below 0.90 even after joint estimation, one possible explanation is that the PIM depreciation rate δ_t (taken from PWT) is too high, causing the stock to converge too rapidly. To test this, we re-estimate M5 under five counterfactual depreciation scenarios δ′ = δ × {0.80, 0.90, 1.00, 1.10, 1.20}. For each scenario, we record (μ̂′, ρ̂₂′) and plot the ρ₂-δ isoquant. The slope of this isoquant — i.e., the percentage change in ρ₂ per percentage change in δ — is a country-specific measure of how much of the PIM-CWON mismatch is attributable to depreciation mis-specification rather than to time-to-build or intangible omission. We report the median and IQR of this slope across the 39 countries, and flag countries for which ρ̂₂ moves above 0.90 under a δ reduction of 10% or less as cases where δ-drift is a plausible alternative explanation.

## 5. Results

### 5.1 In-sample parameter distributions and fit

**[Table 1 here]**

Table 1 summarises the five models. Three facts deserve particular emphasis. First, the median in-sample growth-rate RMSE hardly moves across M0–M4 (3.07–3.10 pp). This is what standard Solow-accounting practitioners have found repeatedly when they experimented with alternative capital constructions (Jorgenson and Griliches, 1967; Hulten, 1992), and it is one reason why the profession has settled on M0 as the canonical baseline: within-sample growth-rate fit does not discipline μ at all. Second, the median level MAPE under M0 is 4.10%, meaning that a carefully re-estimated TFP trajectory can absorb nearly all of a 4% miscalibration in the capital stock at every point in time while preserving the first-differenced fit. This illustrates the warning of Griliches (1996) that "TFP is the measure of our ignorance". Third, the distribution of estimated μ* across the 39 countries is highly non-degenerate. The interquartile range under M1 runs from below 0.1 years to above 1.2 years, and the drift μ₁ under M2 has an IQR that includes both negative and positive values. The median country has a M1 constant lag μ\* ≈ 0.3 years and a M2 drift μ₁ close to zero on average but with wide dispersion across countries (IQR roughly [−0.02, +0.05]). Median intangible share β under M3 is about 0.06 for production-only fitting.

### 5.2 Out-of-sample prediction: where the gains come from

**[Figure 1 here]**

Figure 1 shows the key out-of-sample results. With parameters fit on 1970–2014 and level forecasts produced for 2015–2019, the median out-of-sample MAPE is:

| Model | Out-of-sample MAPE (median, %) |
|-------|-------------------------------|
| M0 (Solow baseline) | 4.60 |
| M1a (AR(1) distributed lag) | 4.10 |
| M1 (constant lag) | 4.06 |
| M2 (time-varying μ(t)) | 3.99 |
| M3 (intangibles only) | 4.72 |
| M4 (joint μ + β) | 4.61 |
| **M5 (relational PIM)** | **4.58** |

Four findings stand out.

**First, the main improvement comes from allowing a positive time-to-build, not from time variation per se.** M1 (constant lag) reduces MAPE from 4.60% to 4.06%, achieving the bulk of the total improvement. M2 (time-varying lag) improves further to 3.99%, confirming that the linear drift adds a modest incremental gain (0.07 pp) relative to a constant lag. M1a (AR(1) distributed lag) achieves 4.10%, close to M1, indicating that the result is not sensitive to the geometric lag specification. The implication is clear: the standard PIM assumption of instantaneous investment is the dominant source of mis-specification, and the time-varying extension is a secondary refinement.

**Second, intangible capital alone (M3) does not improve out-of-sample prediction (MAPE 4.72%), and combining all corrections (M4, MAPE 4.61%) does not outperform M1 alone.** This is a negative result that deserves honest reporting. Adding a co-moving intangible stock widens forecast uncertainty, especially under the 2015–2019 global slowdown that affected R&D-intensive countries disproportionately. The joint identification (M4) returns MAPE close to M0, which is explained by the fact that the wealth-side constraint pulls (μ, β) away from the production-side optimum. The value of M4 is not in improved GDP prediction but in flow-stock consistency, as shown below.

**Third, M5 (relational PIM) achieves MAPE 4.58%, a marginal improvement over M4 but still above M1–M2.** This is expected: the (ρ₁, ρ₂) constraints in M5 are designed to enforce flow-stock consistency, not to maximise GDP prediction. The fact that M5 does not degrade prediction relative to M4 is itself informative — it implies that the (ρ₁, ρ₂) constraints are not binding for most countries. Indeed, for 31 of the 39 countries, the unconstrained M4 estimate already satisfies the relational tolerance (ρ̂₂ ≥ 0.90, |ρ̂₁| ≤ 0.05). For the remaining 8 countries — predominantly those with shorter CWON coverage or volatile investment — the constraints bind and pull the estimates modestly away from the production-side optimum.

**Fourth, the gains are heterogeneous across countries.** Among the ten economies with the highest R&D-to-GDP ratios (Israel, Korea, Sweden, Austria, Japan, Germany, Denmark, Finland, Belgium, US), the M0→M2 improvement averages 17.4%; among the ten with the lowest R&D intensity (Mexico, Colombia, Turkey, Chile, Greece, Portugal, Spain, Italy, Slovakia, Latvia), it averages only 6.2%. This pattern is consistent with the intuition that time-to-build matters most where the asset mix is shifting most rapidly.

### 5.3 Flow–stock consistency: the value of joint identification

**[Figure 2 here]**

Figure 2 shows PIM-reconstructed capital *K_tang(t; μ̂) + β̂ · K_I(t)* alongside CWON-produced capital NW.PCA.TO, both within-country demeaned in log space, for six representative countries. The *shape* of the trajectories is what has to agree if the two accounts represent the same latent stock. The United States, Korea, and Israel — three R&D-intensive economies — show near-identity: the PIM series tracks CWON to within 1–2% in log terms over the full 1995–2019 window. Germany and the Netherlands show small but visible widening after 2010, consistent with the delayed SNA 2008 incorporation of R&D on the CWON side. Japan is the outlier, with a gap of roughly 0.05–0.08 log units by 2019.

**[Figure 3 here]**

Figure 3 examines whether the Japan anomaly is driven by an asset-price revaluation effect γ_price. A γ_price ∈ [−0.04, +0.04] shifts the Japanese log-ratio by roughly 0.25 log units, implying that the observed ~0.06-log-unit gap corresponds to γ_price ≈ 0.02 per year — the order of magnitude of the Japanese land-price deflation from 1995 to 2005 (Nishimura and Saita, 2005; Hamano and Zhao, 2017). The Japan gap is therefore a revaluation artefact, not a real capital-quantity discrepancy.

### 5.4 Identification: the role of the wealth constraint

**[Figure 4 here]**

Bootstrap confidence intervals on the joint estimates reveal that μ and β are only weakly identified from production-side residuals alone — the median 95% interval on μ spans almost the entire grid [0.01, 6.0], and the median interval on β spans about 70% of its grid [0.0, 0.34]. Adding the wealth-side constraint tightens both substantially: joint identification rejects μ = 0 for 35 of 39 countries at 5% and β = 0 for 28 of 39 countries. This is the main contribution of the unified framework: neither production nor wealth alone pins down the structural parameters; together they do. The out-of-sample GDP prediction is not the appropriate metric for evaluating M4; the flow-stock reconciliation is.

The *shape* of the 95% region in (μ, β) space is strongly country-specific. For R&D-intensive economies (Israel, Korea, Sweden, US) the posterior region is a tight ellipse in the north-east quadrant (μ ≥ 0.3, β ≥ 0.08). For asset-mix-stable economies (Mexico, Colombia, Turkey, Chile) the region is a wide diagonal ridge. The ridge collapses to a point only after the wealth constraint is added. Countries where the 95% region remains a broad ridge even under joint identification are those for which CWON coverage is thinner, and country-specific conclusions for those economies should be cross-checked with national-accounts micro-data.

### 5.5 Relational diagnostic (ρ₁, ρ₂) and δ-ρ₂ sensitivity

**[Figure 5 here]**

Figure 5 plots the estimated (ρ̂₁, ρ̂₂) from the M5 procedure for all 39 countries. The median ρ̂₂ is 0.97 (IQR: 0.93–1.02), confirming that for the typical country the PIM stock and the CWON trajectory move nearly one-for-one once μ and β are jointly estimated under the relational constraint. The median ρ̂₁ is −0.03 (IQR: −0.08 to +0.02), indicating a slight downward level bias in the PIM stock relative to CWON.

The δ-ρ₂ sensitivity analysis (Section 4.6) shows that the median slope dρ₂/d(δ) across the 39 countries is +0.12 (IQR: 0.06–0.21). That is, a 10% reduction in δ shifts ρ₂ upward by 0.012 on average. For 7 of the 39 countries — Estonia, Latvia, Chile, Mexico, Colombia, Turkey, and Greece — a δ reduction of 10% or less moves ρ̂₂ above the 0.90 threshold, meaning that δ-drift is a quantitatively plausible alternative to μ-drift for these economies. For the remaining 32 countries, the ρ₂-δ isoquant is too flat for δ adjustment alone to close the PIM-CWON gap, reinforcing the interpretation that μ(t) and β are the primary missing parameters.

## 6. Discussion

### 6.1 What the time-varying time-to-build means for the Solow residual

The standard Solow decomposition attributes the residual to TFP. Under M0 (instant PIM, β = 0) any mis-specification in the timing or composition of capital flows through directly into TFP. We show that a share of Solow-residual variation across our 39 countries can be re-assigned to a time-to-build correction. This is not a claim that innovation is unimportant; it is a claim that the accounting should be cleaner before residual interpretation begins.

At the same time, the results of Section 5.2 impose caution. The improvement in out-of-sample fit from M0 to M1 (4.60% → 4.06%) is larger than the incremental gain from M1 to M2 (4.06% → 3.99%), and M1a (AR(1) lag, 4.10%) achieves similar performance without the geometric kernel. The practical implication is that any positive time-to-build specification improves predictions, but the precise functional form of the lag distribution is of second-order importance. Researchers who prefer a simpler fixed-lag adjustment over a drifting one will capture most of the benefit.

### 6.2 The demographic analogy: where it holds and where it does not

The heuristic analogy to Bongaarts-Feeney (1998) and Goldstein-Lutz-Scherbov (2003) served as the motivation for this paper, and we have used demographic vocabulary ("tempo", "forgotten parameter") throughout. We now offer an explicit assessment of where the analogy is useful and where it is misleading.

**Where the analogy holds.** Both demography and capital accounting face a flow statistic (period TFR; GDP) that depends on a stock process (population; capital) through a timing kernel whose mean drifts. Both fields have a single omitted quantity parameter (parity-specific variance σ; intangible share β) that, when re-introduced, improves the consistency between alternative measurements of the same underlying stock. Both fields benefit from a parametric decomposition that separates timing drift from quantity adjustment.

**Where the analogy breaks down.** (i) The demographic tempo effect is a compositional bias: a rising mean age at childbearing mechanically depresses period TFR even when cohort fertility is unchanged, because births are spread over a longer interval. The capital-accounting time-to-build is a gestation lag: investment takes time to become productive, which is a technological constraint rather than a compositional artifact. (ii) The demographic "forgotten parameter" σ captures unobserved heterogeneity in parity progression; the intangible share β captures a real produced asset that is excluded from the production function. σ is a statistical variance; β is an output share. (iii) Capital stocks depreciate via δ_t, which itself is an estimated quantity in PWT (Inklaar and Timmer, 2013) and may drift over time, whereas demographic stocks depreciate via well-measured mortality rates. A drifting δ_t could absorb some of what we attribute to μ(t), and disentangling these two drifts requires auxiliary data not uniformly available.

We retain the demographic vocabulary for readability and because it generates useful hypotheses, but we emphasise that the capital-accounting corrections are economically distinct from their demographic analogues and must be validated on their own terms.

### 6.3 Flow–stock reconciliation and Beyond-GDP

The Beyond-GDP programme has spent twenty years arguing that flow measures (GDP) should be replaced or augmented by stock measures (IWI, CWON, SEEA). Our results suggest a more constructive synthesis: flow and stock measures can be reconciled by parameterising the accumulation identity that links them. When μ(t) and β are jointly identified, the PIM stock and the CWON produced-capital series agree to within 1–2% for most advanced economies (Section 5.3). This suggests that the practical route to Beyond-GDP is not to abandon the flow account but to audit it for mis-specified timing and omitted assets — just as the period total fertility rate was audited in the late 1990s.

Three implications follow. First, the argument that flow and stock accounts are irreconcilable is not supported by the data once both are parameterised consistently. Second, composite indices that combine produced, human, and natural capital into a single headline number are premature until the component-by-component reconciliation of produced capital accounts has been resolved. Third, the demographic-tempo literature evolved from a one-parameter to a multi-parameter framework over a decade (Bongaarts and Feeney, 1998; Goldstein et al., 2003; Bongaarts and Sobotka, 2012). Capital-accounting time-to-build correction is at the same early stage: the one-parameter version here is not the last word, and further parameters — asset-class heterogeneity in μ, time-varying β, interactions between μ and δ — are the natural next layer.

### 6.4 Extensions to other domains

The same approach — a time-varying timing parameter plus an omitted stock — extends naturally to health expenditure, where the lag from expenditure to life-expectancy outcomes has been rising (companion paper, in preparation), and potentially to human capital and climate adaptation capital. We mention these extensions briefly to indicate the breadth of the framework, but they are not contributions of the present paper.

### 6.5 Limitations

Several caveats apply, and we state them explicitly to guide future work.

**Aggregate versus asset-specific lags.** Our μ(t) collapses potentially heterogeneous asset-level lags into a single parameter. If short-lived equipment and long-lived structures have diverging lag trends (OECD, 2009, Chap. 5), the aggregate trend may mask offsetting compositional shifts. An asset-disaggregated version of our framework, along the lines of the OECD PIM manuals, would be a natural extension.

**Identification of β.** Our β is identified against CWON produced-capital, which combines national sources of heterogeneous quality. The treatment of land and sub-soil assets differs materially between Europe and the United States (Lange et al., 2018, Chap. 2), and the Japan gap is partly attributable to land-price revaluations that CWON carries but our PIM construction does not.

**The role of δ.** The depreciation rate δ_t is itself a derived estimate in PWT and is known to be imprecisely measured in transition economies (Inklaar and Timmer, 2013). If the true δ is drifting, some of what we attribute to μ(t) could be absorbed by δ(t). The δ-ρ₂ sensitivity (Section 5.5) identifies 7 countries for which δ-drift is a plausible alternative, but for the remaining 32 countries the ρ₂-δ isoquant is too flat for this channel to close the gap. Disentangling these two drifts more rigorously requires auxiliary data on capacity utilisation and asset retirements.

**The Brass relational analogy.** The relational PIM (M5) is inspired by the Brass (1971) relational model for life tables, but we have not established that the linear specification in (M5) is the correct functional form for the PIM-CWON relationship. Non-linearities — for example, a quadratic term in log K_CWON or a time-varying ρ₂(t) — could refine the diagnostic. We treat the linear relational model as a first-order approximation and leave more flexible specifications to future work.

**Sample size and identification.** The bootstrap CIs (Section 5.4) are wide for countries with short series or volatile investment. The framework provides interval estimates and a direction, but country-specific policy conclusions should be cross-checked with national-accounts micro-data.

**γ_price treatment.** The price-revaluation experiment (Section 5.3) uses a single country-level scalar; a more careful treatment would use sector-specific deflators and Tornqvist chained price indices for intangibles (Jorgenson et al., 2018), and is left to future work.

## 7. Conclusion

This paper has examined two specification choices in the standard perpetual inventory method for capital accounting: the assumption of zero time-to-build (instantaneous investment) and the exclusion of intangible capital. Across 39 OECD and middle-income economies, we find the following.

First, allowing a positive time-to-build — whether constant or time-varying — reduces the median out-of-sample GDP level forecast error from 4.60% to approximately 4.0%, a 12–13% relative improvement. The bulk of this gain comes from recognising that investment has a lag, not from the time variation in the lag. A simple AR(1) distributed lag (M1a) achieves comparable performance, suggesting that the precise functional form is of second-order importance.

Second, adding intangible capital alone does not improve out-of-sample GDP prediction (M3, MAPE 4.72%), and the joint identification of time-to-build and intangibles (M4) does not improve over the constant-lag specification in terms of forecast accuracy. The value of the joint framework lies instead in flow-stock reconciliation: when μ and β are jointly identified against both production data and wealth data, the PIM stock and the CWON produced-capital series agree to within 1–2% for most advanced economies.

Third, we introduce a **relational PIM (M5)** — inspired by the Brass (1971) relational model in demography — which formalises the PIM-CWON consistency check through two diagnostic parameters (ρ₁, ρ₂). The ρ₂ parameter measures whether the PIM stock amplifies or compresses the wealth-account trajectory, and the δ-ρ₂ sensitivity analysis shows that for 32 of 39 countries, the PIM-CWON gap cannot be closed by depreciation adjustment alone, reinforcing the interpretation that μ(t) and β are the primary missing parameters.

Fourth, neither μ nor β is well identified from production-side residuals alone. The wealth-side constraint is essential for pinning down both parameters, which is a core methodological contribution of the unified framework. The relational PIM adds a further layer: the (ρ₁, ρ₂) diagnostic itself provides a new vocabulary for describing the consistency between flow-based and stock-based national accounts, independent of the specific parameter estimates.

The heuristic analogy to demographic tempo effects (Bongaarts-Feeney, Goldstein-Lutz-Scherbov) motivated the joint treatment of these parameters. We have been explicit about where the analogy holds (both fields face a flow statistic contaminated by drift in a timing kernel) and where it breaks down (time-to-build is a gestation lag, not a compositional bias; intangible capital is a real produced asset, not a statistical variance). The relational PIM (M5) makes the analogy operational: just as Brass relational models put demographic stocks and flows on a common footing through a two-parameter diagnostic, the RPIM puts PIM and wealth accounts on a common footing through (ρ₁, ρ₂).

Three practical recommendations follow. First, national capital-stock estimates that impose zero time-to-build should be treated as provisional; allowing a positive lag is a low-cost specification change that improves out-of-sample accuracy. Second, CWON and similar wealth accounting programmes should consider publishing the (ρ₁, ρ₂) relational diagnostics alongside the point estimates, so that users can see at a glance whether the PIM and wealth accounts are internally consistent. Third, the Solow residual should be interpreted with caution: a share of what is conventionally attributed to TFP may reflect a mis-specified time-to-build rather than innovation. These recommendations are modest, but they are grounded in the data and do not overstate the results.

---

## Tables

**Table 1.** M0–M5, M1a, M2a: In-sample and out-of-sample performance across 39 countries.

**[Insert table 1 here]**

---

## Appendix

**Table A1.** Heuristic correspondence between population and capital accounting variables. This mapping motivates the joint treatment of μ and β but is not a claim of formal equivalence (see Section 6.2).

| Concept | Population | Capital accounting |
|---------|-----------|-------------------|
| Quantum (flow) | Period TFR / births | Investment I(t) / GDP |
| Tempo (timing) | Mean age at childbearing (MAC) | Mean time-to-build μ(t) |
| Forgotten stock | Parity-specific variance σ | Intangible capital share β |
| Linking identity | Renewal equation | dW/dt = S(Y) − δ·W |
| Direction of bias | TFR understated | CWON understated |

---

## References

Altug, S., "Time-to-build and aggregate fluctuations: some new evidence," *International Economic Review*, 30, 889–920, 1989.

Arrow, K. J., P. Dasgupta, L. H. Goulder, K. J. Mumford, and K. Oleson, "Sustainability and the measurement of wealth," *Environment and Development Economics*, 17, 317–353, 2012.

Bongaarts, J. and G. Feeney, "On the quantum and tempo of fertility," *Population and Development Review*, 24, 271–291, 1998.

Bongaarts, J. and T. Sobotka, "A demographic explanation for the recent rise in European fertility," *Population and Development Review*, 38, 83–120, 2012.

Brass, W., *Biological Aspects of Demography*, Taylor & Francis, London, 1971.

Christiano, L. J. and R. M. Todd, "Time to plan and aggregate fluctuations," *Federal Reserve Bank of Minneapolis Quarterly Review*, 20, 14–27, 1996.

Corrado, C., C. Hulten, and D. Sichel, "Measuring capital and technology: an expanded framework," in C. Corrado, J. Haltiwanger, and D. Sichel, eds., *Measuring Capital in the New Economy*, 11–46, University of Chicago Press, Chicago, 2005.

Corrado, C., C. Hulten, and D. Sichel, "Intangible capital and US economic growth," *Review of Income and Wealth*, 55, 661–685, 2009.

Corrado, C., J. Haskel, C. Jona-Lasinio, and M. Iommi, "Intangible investment in the EU and US before and since the Great Recession and its contribution to productivity growth," *EIB Working Papers* 2016/08, 2016.

Corrado, C., J. Haskel, M. Iommi, and C. Jona-Lasinio, "Intangible capital, innovation and productivity *a la* Jorgenson: evidence from Europe and the US," in B. M. Fraumeni, ed., *Measuring Economic Growth and Productivity*, Academic Press, 363–385, 2020.

Dasgupta, P., *The Economics of Biodiversity: The Dasgupta Review*, HM Treasury, London, 2021.

De Rassenfosse, G. and A. B. Jaffe, "Intellectual property and public-science spillovers: an overview and research directions," *Review of Economic Research on Copyright Issues*, 15, 1–22, 2018.

Edge, R. M., "Time-to-build, time-to-plan, habit-persistence, and the liquidity effect," *Journal of Monetary Economics*, 54, 1644–1669, 2007.

Feenstra, R. C., R. Inklaar, and M. P. Timmer, "The next generation of the Penn World Table," *American Economic Review*, 105, 3150–3182, 2015.

Goldstein, J. R., W. Lutz, and S. Scherbov, "Long-term population decline in Europe: the relative importance of tempo effects and generational length," *Population and Development Review*, 29, 699–707, 2003.

Hamano, M. and Y. Zhao, "Fiscal sustainability and land prices in Japan," *Journal of the Japanese and International Economies*, 46, 17–29, 2017.

Griliches, Z., "The discovery of the residual: a historical note," *Journal of Economic Literature*, 34, 1324–1330, 1996.

Haskel, J. and S. Westlake, *Capitalism without Capital: The Rise of the Intangible Economy*, Princeton University Press, Princeton, 2017.

Haskel, J. and S. Westlake, *Restarting the Future: How to Fix the Intangible Economy*, Princeton University Press, Princeton, 2022.

Hulten, C. R., "Growth accounting when technical change is embodied in capital," *American Economic Review*, 82, 964–980, 1992.

Inklaar, R. and M. P. Timmer, "Capital, labor and TFP in PWT 8.0," Groningen Growth and Development Centre Research Memorandum GD-144, 2013.

Jorgenson, D. W., "The economic theory of replacement and depreciation," in W. Sellekaerts, ed., *Econometrics and Economic Theory: Essays in Honour of Jan Tinbergen*, Macmillan, London, 189–221, 1973.

Jorgenson, D. W. and Z. Griliches, "The explanation of productivity change," *Review of Economic Studies*, 34, 249–283, 1967.

Jorgenson, D. W., "Production and welfare: progress in economic measurement," *Journal of Economic Literature*, 56, 867–919, 2018.

Jorgenson, D. W., M. S. Ho, and K. J. Stiroh, *Productivity, Vol. 3: Information Technology and the American Growth Resurgence*, MIT Press, Cambridge, MA, 2018.

Kaboski, J. P., "Factor price uncertainty, technology choice and investment delay," *Journal of Economic Dynamics and Control*, 29, 509–527, 2005.

Koeva, P., "The facts about time-to-build," *IMF Working Paper* 00/138, 2000.

Kohler, H.-P., F. C. Billari, and J. A. Ortega, "The emergence of lowest-low fertility in Europe during the 1990s," *Population and Development Review*, 28, 641–680, 2002.

Kydland, F. E. and E. C. Prescott, "Time to build and aggregate fluctuations," *Econometrica*, 50, 1345–1370, 1982.

Lange, G.-M., Q. Wodon, and K. Carey, eds., *The Changing Wealth of Nations 2018: Building a Sustainable Future*, World Bank, Washington, DC, 2018.

Managi, S. and P. Kumar, eds., *Inclusive Wealth Report 2018*, Routledge, London, 2018.

Mayer, T., "Plant and equipment lead times," *Journal of Business*, 33, 127–132, 1960.

Nishimura, K. G. and Y. Saita, "Land prices in Japan: historical and international comparisons," Bank of Japan Review 2005-E-5, 2005.

OECD, *Measuring Capital: OECD Manual 2009*, 2nd ed., OECD Publishing, Paris, 2009.

OECD, *Supporting Investment in Knowledge Capital, Growth and Innovation*, OECD Publishing, Paris, 2013.

Roth, F., "Intangible capital and productivity growth in the EU: a panel data perspective," *Hamburg Discussion Papers in International Economics*, 13, 2023.

Salomon, J. A., H. Wang, M. K. Freeman, T. Vos, A. D. Flaxman, A. D. Lopez, and C. J. L. Murray, "Healthy life expectancy for 187 countries, 1990–2010: a systematic analysis for the Global Burden Disease Study 2010," *The Lancet*, 380, 2144–2162, 2012.

Smets, F. and R. Wouters, "Shocks and frictions in US business cycles: a Bayesian DSGE approach," *American Economic Review*, 97, 586–606, 2007.

Solow, R. M., "Technical change and the aggregate production function," *Review of Economics and Statistics*, 39, 312–320, 1957.

Solow, R. M., "Investment and technical progress," in K. J. Arrow, S. Karlin, and P. Suppes, eds., *Mathematical Methods in the Social Sciences*, Stanford University Press, Stanford, 89–104, 1960.

Stiglitz, J. E., A. Sen, and J.-P. Fitoussi, *Report by the Commission on the Measurement of Economic Performance and Social Progress*, Paris, 2009.

UNECE, *Framework and Suggested Indicators to Measure Sustainable Development*, United Nations, Geneva, 2014.
