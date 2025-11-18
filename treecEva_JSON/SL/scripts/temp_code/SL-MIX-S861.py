import math
from collections import defaultdict

def compute_volatility_factor(returns, index):
    if index <= 1:
        return 1.0
    prev_factor = compute_volatility_factor(returns, index - 1)
    current_return = returns[index - 1]
    smoothed_variance = 0.3 * (current_return ** 2) + 0.7 * (prev_factor ** 2)
    return math.sqrt(smoothed_variance)

def calculate_portfolio_metrics(quarterly_returns):
    n = len(quarterly_returns)
    dp_table = defaultdict(float)
    dp_table[0] = quarterly_returns[0]
    
    for i in range(1, n):
        exp_smoothed = 0.4 * quarterly_returns[i] + 0.6 * dp_table[i-1]
        vol_factor = compute_volatility_factor(quarterly_returns, i)
        dp_table[i] = exp_smoothed * math.log(vol_factor + 1.5)
    
    cumulative_product = 1.0
    for val in dp_table.values():
        cumulative_product *= (1 + val * 0.01)
    
    risk_adjustment = math.exp(cumulative_product - n)
    final_adjusted_return = round(dp_table[n-1] * risk_adjustment, 6)
    return final_adjusted_return

portfolio_quarterly_returns = [0.05, -0.02, 0.03, 0.01, -0.005, 0.04]
final_adjusted_return = calculate_portfolio_metrics(portfolio_quarterly_returns)
print(f"Result: {final_adjusted_return}")