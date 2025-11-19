import math
import statistics

def compute_portfolio_risk(returns):
    n = len(returns)
    if n == 0:
        return 0
    mean_return = sum(returns) / n
    squared_deviations = [(r - mean_return) ** 2 for r in returns]
    variance = sum(squared_deviations) / n
    std_dev = math.sqrt(variance)
    
    # Weighted adjustment based on return consistency
    consistency_factor = 1.0 if std_dev < 0.05 else (0.5 if std_dev < 0.1 else 0.2)
    adjusted_mean = mean_return * consistency_factor
    
    # Fibonacci weighting for time decay (most recent returns have higher weight)
    fib_weights = []
    a, b = 1, 1
    for _ in range(n):
        fib_weights.append(a)
        a, b = b, a + b
    fib_weights.reverse()
    
    weighted_sum = sum(r * w for r, w in zip(returns, fib_weights))
    weight_sum = sum(fib_weights)
    weighted_avg = weighted_sum / weight_sum if weight_sum != 0 else 0
    
    # Final score combines metrics with short-circuit logic
    volatility_penalty = 0.1 if std_dev > 0.15 else (0.05 if std_dev > 0.1 else 0)
    final_score = (weighted_avg * (1 - volatility_penalty)) if weighted_avg > 0 else weighted_avg
    return final_score

portfolio_returns = [0.02, 0.03, -0.01, 0.04, 0.01, -0.02, 0.05]
score_components = {
    'raw_score': compute_portfolio_risk(portfolio_returns),
    'benchmark': 0.025,
}

enhanced_metrics = {k: v * 1000 for k, v in score_components.items()}
baseline_adjustment = 50.0
final_score = enhanced_metrics['raw_score'] + baseline_adjustment if enhanced_metrics['raw_score'] > 0 else baseline_adjustment
print(f'Result: {final_score}')