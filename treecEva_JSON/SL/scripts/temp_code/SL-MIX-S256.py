import math
from itertools import combinations

# Portfolio parameters
initial_capital = 10000.0
txn_fees = [0.01, 0.02, 0.015, 0.03]
expected_returns = [0.05, 0.07, 0.04, 0.09]

# Compute adjusted returns considering fees
adjusted_returns = []
for i in range(len(txn_fees)):
    log_fee = math.log(1 + txn_fees[i])
    adj_return = expected_returns[i] - log_fee
    adjusted_returns.append(adj_return)

# Find the best combination of two investments using greedy selection
investment_pairs = list(combinations(adjusted_returns, 2))
profitability_scores = [sum(pair) for pair in investment_pairs]
best_pair_index = profitability_scores.index(max(profitability_scores))
selected_investments = investment_pairs[best_pair_index]

# Calculate compounded yield from selected investments
compounded_yield = 1.0
for rate in selected_investments:
    compounded_yield *= math.exp(rate)

# Apply to initial capital
final_yield = initial_capital * compounded_yield

print(f"Result: {final_yield}")