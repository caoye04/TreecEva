from functools import reduce
import statistics

def calculate_transaction_impact(transactions):
    return sum(map(lambda t: abs(t) * 0.01, transactions))

def adjusted_returns(returns, fees):
    return list(map(lambda r, f: r - f, returns, fees))

portfolio_transactions = [1000, -500, 2000, -1500, 3000]
expected_gains = [1.05, 0.98, 1.12, 0.95, 1.08]

# Calculate fee impact using functional programming
fee_impacts = list(map(calculate_transaction_impact, [[t] for t in portfolio_transactions]))

# Adjust expected gains with fee impacts
adj_gains = adjusted_returns(expected_gains, fee_impacts)

# Greedy selection of top performing assets
performance_ranking = {i: adj_gains[i] for i in range(len(adj_gains))}
sorted_assets = sorted(performance_ranking.items(), key=lambda x: x[1], reverse=True)

# Select top 3 assets using greedy approach
selected_indices = [idx for idx, _ in sorted_assets[:3]]
selected_returns = [adj_gains[i] for i in selected_indices]

# Statistical analysis on selected assets
mean_return = statistics.mean(selected_returns)
variance_return = statistics.variance(selected_returns)

# Calculate optimal adjustment with closure
adjustment_factor = 0.75
calculate_optimal = lambda m, v: (m * 1000) / (1 + v) * adjustment_factor
optimal_adjustment = calculate_optimal(mean_return, variance_return)

print(f"Result: {round(optimal_adjustment, 2)}")