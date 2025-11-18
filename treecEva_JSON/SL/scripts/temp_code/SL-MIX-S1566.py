import statistics
from functools import reduce
from collections import namedtuple

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib_seq = [1, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        return fib_seq

def calculate_weighted_volatility(volatility_data):
    n = len(volatility_data)
    fib_weights = generate_fibonacci(n)
    weighted_sum = sum(v * w for v, w in zip(volatility_data, fib_weights))
    total_weight = sum(fib_weights)
    return weighted_sum / total_weight

def adaptive_risk_engine(historical_volatility):
    base_risk = calculate_weighted_volatility(historical_volatility)
    vol_stats = {
        'mean': statistics.mean(historical_volatility),
        'variance': statistics.variance(historical_volatility),
        'median': statistics.median(historical_volatility)
    }
    
    RiskMetrics = namedtuple('RiskMetrics', ['base_risk', 'volatility_stats'])
    metrics = RiskMetrics(base_risk=base_risk, volatility_stats=vol_stats)
    
    adjustment_factor = 1.0
    if metrics.volatility_stats['variance'] > 0.0004:
        adjustment_factor += 0.2
    if metrics.base_risk > metrics.volatility_stats['median']:
        adjustment_factor += 0.1
    
    # Apply dynamic programming to calculate cumulative adjustments
    dp = [1.0] * len(historical_volatility)
    for i in range(1, len(historical_volatility)):
        if historical_volatility[i] > historical_volatility[i-1]:
            dp[i] = dp[i-1] + 0.05
        else:
            dp[i] = max(1.0, dp[i-1] - 0.02)
    
    cumulative_adjustment = reduce(lambda x, y: x * y, dp, 1.0)
    
    adjusted_risk_score = metrics.base_risk * adjustment_factor * cumulative_adjustment
    return adjusted_risk_score

portfolio_volatility = [0.02, 0.05, 0.03, 0.08, 0.04, 0.06]
adjusted_risk_score = adaptive_risk_engine(portfolio_volatility)
print(f"Result: {round(adjusted_risk_score, 6)}")