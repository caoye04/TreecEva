import statistics
import math

def compute_adjusted_sharpe(returns, risk_free_rates):
    excess_returns = [r - rf for r, rf in zip(returns, risk_free_rates)]
    mean_excess = statistics.mean(excess_returns)
    std_dev = statistics.stdev(excess_returns) if len(excess_returns) > 1 else 0
    annualization_factor = math.sqrt(4)  # Quarterly to annual
    sharpe_ratio = (mean_excess / std_dev * annualization_factor) if std_dev != 0 else 0
    
    # Adjustment based on consistency measure
    consistency_bonus = 0.5 if all(er > 0 for er in excess_returns) else 0
    adjusted_sharpe_ratio = sharpe_ratio + consistency_bonus
    return adjusted_sharpe_ratio

# Portfolio data
quarterly_returns = [0.05, 0.07, 0.06, 0.08]
risk_free_rates = [0.01, 0.015, 0.01, 0.02]

# Calculate metrics
adjusted_sharpe_ratio = compute_adjusted_sharpe(quarterly_returns, risk_free_rates)
print(f'Result: {adjusted_sharpe_ratio}')