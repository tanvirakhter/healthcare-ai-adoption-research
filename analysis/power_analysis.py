"""A priori sample-size calculations for the survey study (v0.1).

Three scenarios, matching the planned analyses:
  1. Multiple regression: 8 predictor constructs -> behavioural intention (Q15).
     Predictors per survey draft v0.1: performance expectancy (Q1-Q2), effort
     expectancy (Q3), social influence (Q4), trust (Q5-Q8, Q11), generative
     risk perception (Q9-Q10), verifiable explainability (Q12), narrative
     explainability (Q13), facilitating conditions (Q14).
  2. SEM feasibility: N:q rules of thumb (Kline, 2016) plus the inverse
     square root method for PLS-SEM (Kock & Hadaya, 2018).
  3. Subgroup contrast: two-group mean difference (e.g. clinical vs
     managerial roles), d = 0.5.

Run from the repo root:
    python analysis/power_analysis.py
Prints the tables and rewrites analysis/sample-size-memo.md.

Uses scipy when available; otherwise falls back to a direct implementation
of the noncentral-F power calculation (Poisson mixture over central F,
regularised incomplete beta via continued fractions).
"""

from __future__ import annotations

import math
from pathlib import Path

ALPHA = 0.05
POWER_TARGET = 0.80
N_PREDICTORS = 8

try:
    from scipy import stats as _st

    def _f_crit(dfn: int, dfd: int) -> float:
        return _st.f.ppf(1 - ALPHA, dfn, dfd)

    def _ncf_power(dfn: int, dfd: int, nc: float) -> float:
        return 1 - _st.ncf.cdf(_f_crit(dfn, dfd), dfn, dfd, nc)

    _BACKEND = "scipy"
except ImportError:  # pragma: no cover - exercised only without scipy

    def _betacf(a: float, b: float, x: float) -> float:
        # Continued fraction for the incomplete beta function (Lentz's method).
        qab, qap, qam = a + b, a + 1.0, a - 1.0
        c, d = 1.0, 1.0 - qab * x / qap
        d = 1.0 / (d if abs(d) > 1e-30 else 1e-30)
        h = d
        for m in range(1, 200):
            m2 = 2 * m
            aa = m * (b - m) * x / ((qam + m2) * (a + m2))
            d = 1.0 / max(1.0 + aa * d, 1e-30) if abs(1.0 + aa * d) > 1e-30 else 1e30
            c = 1.0 + aa / c if abs(1.0 + aa / c) > 1e-30 else 1e-30
            h *= d * c
            aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
            d = 1.0 / (1.0 + aa * d if abs(1.0 + aa * d) > 1e-30 else 1e-30)
            c = 1.0 + aa / c if abs(1.0 + aa / c) > 1e-30 else 1e-30
            delta = d * c
            h *= delta
            if abs(delta - 1.0) < 3e-12:
                break
        return h

    def _betainc(a: float, b: float, x: float) -> float:
        if x <= 0.0:
            return 0.0
        if x >= 1.0:
            return 1.0
        ln_bt = (
            math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
            + a * math.log(x) + b * math.log(1.0 - x)
        )
        bt = math.exp(ln_bt)
        if x < (a + 1.0) / (a + b + 2.0):
            return bt * _betacf(a, b, x) / a
        return 1.0 - bt * _betacf(b, a, 1.0 - x) / b

    def _f_cdf(x: float, dfn: int, dfd: int) -> float:
        return _betainc(dfn / 2.0, dfd / 2.0, dfn * x / (dfn * x + dfd))

    def _f_crit(dfn: int, dfd: int) -> float:
        lo, hi = 0.0, 100.0
        for _ in range(200):
            mid = (lo + hi) / 2.0
            if _f_cdf(mid, dfn, dfd) < 1 - ALPHA:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2.0

    def _ncf_cdf(x: float, dfn: int, dfd: int, nc: float) -> float:
        # Noncentral F as a Poisson-weighted mixture of central F distributions.
        total, term = 0.0, math.exp(-nc / 2.0)
        for j in range(0, 400):
            if j > 0:
                term *= (nc / 2.0) / j
            contrib = term * _f_cdf(x * dfn / (dfn + 2 * j), dfn + 2 * j, dfd)
            total += contrib
            if term < 1e-14 and j > nc:
                break
        return total

    def _ncf_power(dfn: int, dfd: int, nc: float) -> float:
        return 1 - _ncf_cdf(_f_crit(dfn, dfd), dfn, dfd, nc)

    _BACKEND = "fallback (no scipy)"


def regression_n(f2: float, k: int = N_PREDICTORS) -> tuple[int, float]:
    """Smallest N reaching the power target for an R^2 != 0 test, k predictors."""
    for n in range(k + 2, 5000):
        power = _ncf_power(k, n - k - 1, f2 * n)
        if power >= POWER_TARGET:
            return n, power
    raise RuntimeError("no N found below 5000")


def two_group_n(d: float) -> tuple[int, float]:
    """Per-group n for a two-sided two-sample t test at the power target.

    Computed via the equivalent F(1, 2n-2) test with nc = d^2 * n / 2.
    """
    for n in range(4, 5000):
        power = _ncf_power(1, 2 * n - 2, d * d * n / 2.0)
        if power >= POWER_TARGET:
            return n, power
    raise RuntimeError("no n found below 5000")


def sem_nq(indicators: int = 32, factors: int = 8, structural_paths: int = 8) -> dict:
    """Free-parameter count q for the planned CFA/SEM, plus N at standard N:q ratios.

    With one marker loading fixed per factor: (indicators - factors) loadings,
    indicators error variances, factors factor variances, and either factor
    covariances (CFA) or structural paths + disturbances. The CFA case gives
    the larger, more conservative q.
    """
    loadings = indicators - factors
    errors = indicators
    variances = factors
    covariances = factors * (factors - 1) // 2
    q = loadings + errors + variances + covariances
    return {"q": q, "n_10": 10 * q, "n_20": 20 * q, "structural_paths": structural_paths}


def kock_hadaya_n(p_min: float = 0.20) -> int:
    """Inverse square root method for PLS-SEM minimum n (Kock & Hadaya, 2018)."""
    return math.ceil((2.486 / p_min) ** 2)


def main() -> None:
    print(f"Backend: {_BACKEND}; alpha={ALPHA}, target power={POWER_TARGET}\n")

    print(f"1. Multiple regression, k={N_PREDICTORS} predictors -> behavioural intention")
    reg_rows = []
    for label, f2 in (("small", 0.02), ("medium", 0.15), ("large", 0.35)):
        n, power = regression_n(f2)
        reg_rows.append((label, f2, n, power))
        print(f"   f2={f2:<5} ({label:6}) -> N = {n:4d}  (power {power:.3f})")

    sem = sem_nq()
    pls_n = kock_hadaya_n()
    print(f"\n2. SEM feasibility: q = {sem['q']} free parameters "
          f"(32 indicators, 8 factors, CFA-conservative)")
    print(f"   N:q 10:1 -> N = {sem['n_10']};  20:1 -> N = {sem['n_20']}  (Kline, 2016)")
    print(f"   PLS-SEM inverse square root, weakest path 0.20 -> n >= {pls_n} "
          f"(Kock & Hadaya, 2018)")

    n_group, power_g = two_group_n(0.5)
    print(f"\n3. Subgroup contrast, d=0.5 two-sided -> {n_group} per group, "
          f"{2 * n_group} total (power {power_g:.3f})")

    target = 200
    completed = math.ceil(target / 0.8)
    invited = math.ceil(completed / 0.15)
    print(f"\nRecommendation: retain N >= {target} analysable responses "
          f"-> ~{completed} completed at 20% attrition -> ~{invited} invitations "
          f"at a 15% response rate.")

    write_memo(Path(__file__).parent / "sample-size-memo.md",
               reg_rows, sem, pls_n, n_group, target, completed, invited)


def write_memo(path, reg_rows, sem, pls_n, n_group, target, completed, invited) -> None:
    reg_table = "\n".join(
        f"| {label} | {f2} | {n} |" for label, f2, n, _ in reg_rows
    )
    path.write_text(f"""# Sample-Size Memo (a priori power analysis)

Status: working memo for supervisor review. Generated by `power_analysis.py`
(alpha = {ALPHA}, target power = {POWER_TARGET}); rerun the script after any change to the
model specification.

## 1. Multiple regression (primary analysis)

Test of R-squared for {N_PREDICTORS} predictor constructs on behavioural intention (Q15),
predictors as specified in survey draft v0.1.

| Effect size | f-squared | Required N |
|---|---|---|
{reg_table}

A medium effect (f-squared = 0.15) is the planning assumption: UTAUT-family models in
healthcare typically report R-squared for intention between .30 and .50, comfortably
above the medium threshold, so N = {reg_rows[1][2]} is the defensible floor for the
regression analysis alone. Powering for small effects (N = {reg_rows[0][2]}) is not
feasible within the planned recruitment window and is noted as a limitation.

## 2. SEM feasibility

The deployed instrument targets 3-4 items per construct (30-40 items). Taking 32
indicators across 8 factors, the CFA-conservative free-parameter count is
q = {sem['q']}, giving N = {sem['n_10']} at the 10:1 N:q guideline and N = {sem['n_20']}
at 20:1 (Kline, 2016). Covariance-based SEM at those sizes is unrealistic for this
population; this motivates the protocol's use of PLS-SEM, for which the inverse
square root method (Kock & Hadaya, 2018) gives a minimum n of {pls_n} assuming the
weakest path of interest is at least 0.20. Paths weaker than that will be reported
as exploratory, not tested confirmatorily.

## 3. Subgroup contrasts

A two-group comparison (e.g. clinical vs managerial roles) at d = 0.5 requires
{n_group} per group ({2 * n_group} total). Smaller subgroup splits (e.g. by role category)
will not be powered and will be reported descriptively only.

## Recommendation

Retain **N >= {target} analysable responses**: above the regression floor
({reg_rows[1][2]}), above the PLS-SEM minimum ({pls_n}), and sufficient for one
pre-specified two-group contrast. Working backwards: ~{completed} completed
surveys at 20% attrition/quality exclusion, hence ~{invited} invitations at a
conservative 15% response rate. These assumptions (response and attrition rates)
must be revisited after the pilot (n = 20).
""")
    print(f"\nMemo written to {path}")


if __name__ == "__main__":
    main()
