import math

portfolio_weights = {"tech": 0.45, "health": 0.30, "energy": 0.25}
sector_vols = {"tech": 0.22, "health": 0.18, "energy": 0.28}
risk_free_rate = 0.03
market_return = 0.09

# Compute weighted average volatility
portfolio_vol = sum(w * v for w, v in zip(portfolio_weights.values(), sector_vols.values()))

# Sharpe ratio calculation with floating point adjustments
sharpe_ratio = (market_return - risk_free_rate) / portfolio_vol if portfolio_vol > 0 else 0.0

# Risk thresholds using logical operations
is_high_risk = portfolio_vol > 0.22
is_moderate_gain = sharpe_ratio >= 0.5 and sharpe_ratio < 1.0
is_stable = not is_high_risk and sharpe_ratio > 0.3

# Dictionary comprehension for adjusted weights under high risk
adjusted_weights = {k: w * 0.9 if is_high_risk else w for k, w in portfolio_weights.items()}

# Merge with base weights to ensure defaults
base_weights = {"tech": 0.4, "health": 0.3, "energy": 0.2, "other": 0.1}
merged_weights = {**base_weights, **adjusted_weights}

# Final score calculation using set operations on keys
valid_sectors = frozenset(portfolio_weights.keys())
score_sectors = set(merged_weights.keys()).intersection(valid_sectors)

final_score = sum(merged_weights[s] * sector_vols.get(s, 0) for s in score_sectors)
final_score = round(final_score, 4) if is_moderate_gain else round(final_score * 1.1, 4)

print(f"Result: {final_score}")