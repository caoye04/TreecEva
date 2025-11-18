import math

def calculate_modified_sharpe(returns):
    if len(returns) < 2:
        return 0
    mean_return = sum(returns) / len(returns)
    squared_diffs = [(r - mean_return) ** 2 for r in returns]
    variance = sum(squared_diffs) / (len(returns) - 1)
    std_dev = math.sqrt(variance)
    if std_dev == 0:
        return 0
    sharpe_ratio = mean_return / std_dev
    # Apply modification: penalize negative mean returns
    modified_sharpe = sharpe_ratio if mean_return > 0 else sharpe_ratio * -0.5
    return modified_sharpe

# Fund quarterly returns in percentages
fund_alpha_returns = [2.1, -1.5, 3.2, 0.8, -0.4, 1.9, 2.7, -0.3, 1.1, 0.6]
negative_fund_returns = [-2.0, -1.5, -3.0, -0.5, -1.0]

# Process funds using list comprehension
sharpe_scores = [
    calculate_modified_sharpe(returns) 
    for returns in [fund_alpha_returns, negative_fund_returns]
    if len(returns) > 3
]

# Select the highest score after filtering out negative scores
valid_scores = {score for score in sharpe_scores if score > 0}
best_score = max(valid_scores) if valid_scores else 0

# Final adjustment based on number of positive quarters
positive_quarters = sum(1 for r in fund_alpha_returns if r > 0)
adjusted_modifier = 1.2 if positive_quarters > len(fund_alpha_returns) // 2 else 0.8
modified_sharpe_ratio = best_score * adjusted_modifier

print(f"Result: {round(modified_sharpe_ratio, 4)}")