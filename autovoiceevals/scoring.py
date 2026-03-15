"""Scoring logic — single source of truth.

The composite score formula and metrics aggregation live here.
No other module computes scores.
"""

from __future__ import annotations

from .config import ScoringConfig
from .models import EvalResult, Metrics


def composite_score(
    should_results: list[dict],
    should_not_results: list[dict],
    avg_latency_ms: float,
    weights: ScoringConfig,
) -> tuple[float, float, float]:
    """Compute composite score from per-criterion results.

    Returns:
        (composite, should_score, should_not_score)
    """
    s_score = (
        sum(1 for c in should_results if c.get("passed"))
        / max(len(should_results), 1)
    )
    sn_score = (
        sum(1 for c in should_not_results if c.get("passed"))
        / max(len(should_not_results), 1)
    )
    lat_score = 1.0 if avg_latency_ms < weights.latency_threshold_ms else 0.5

    composite = (
        weights.should_weight * s_score
        + weights.should_not_weight * sn_score
        + weights.latency_weight * lat_score
    )
    return composite, s_score, sn_score


def aggregate(results: list[EvalResult]) -> Metrics:
    """Aggregate per-scenario eval results into summary metrics."""
    if not results:
        return Metrics(0.0, 0.0, 0.0, 0, 0)

    scores = [r.score for r in results]
    csats = [r.csat_score for r in results]
    n_passed = sum(1 for r in results if r.passed)
    failures: set[str] = set()
    for r in results:
        failures.update(r.failure_modes)

    return Metrics(
        avg_score=sum(scores) / len(scores),
        avg_csat=sum(csats) / len(csats),
        pass_rate=n_passed / len(results),
        n_passed=n_passed,
        n_total=len(results),
        unique_failures=sorted(failures),
    )
