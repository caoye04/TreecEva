import math

# Normalized annual returns for two portfolios over 5 years
portfolio_a = [0.08, 0.12, 0.05, 0.15, 0.09]
portfolio_b = [0.11, 0.07, 0.13, 0.06, 0.10]

# Combine and normalize using logarithmic transformation
combined_log_returns = list(map(lambda x: math.log(1 + x), portfolio_a + portfolio_b))

# Sort to find median performance
sorted_log_returns = sorted(combined_log_returns)

# Calculate median of log returns
n = len(sorted_log_returns)
median_log_return = (sorted_log_returns[n//2] + sorted_log_returns[(n//2)-1]) / 2 if n % 2 == 0 else sorted_log_returns[n//2]

# Convert back to percentage using exponential
final_cagr_percentage = (math.exp(median_log_return) - 1) * 100

print(f"Result: {final_cagr_percentage}")