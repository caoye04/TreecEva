portfolio_weights = {'tech': 0.4, 'health': 0.3, 'energy': 0.2, 'finance': 0.1}
sector_volatility = {'tech': 1.2, 'health': 0.8, 'energy': 1.5, 'finance': 0.9}
risk_threshold = 1.0

# Lambda to compute weighted risk
compute_weighted_risk = lambda weights, volatilities: sum(w * v for w, v in zip(weights.values(), volatilities.values()))

# Decorator to validate risk scores
def validate_risk_score(func):
    def wrapper(*args, **kwargs):
        score = func(*args, **kwargs)
        return score if score > 0 else 0
    return wrapper

@validate_risk_score
def calculate_base_risk(portfolio_weights, sector_volatility):
    return compute_weighted_risk(portfolio_weights, sector_volatility)

# Short-circuit evaluation with risk threshold
base_risk = calculate_base_risk(portfolio_weights, sector_volatility)
adjusted_risk = base_risk * 1.2 if base_risk > risk_threshold and portfolio_weights['tech'] > 0.3 else base_risk

# Final calculation with hash table lookup
risk_adjustments = {True: 0.9, False: 1.1}
final_risk_score = adjusted_risk * risk_adjustments[adjusted_risk > risk_threshold]

print(f'Result: {final_risk_score}')