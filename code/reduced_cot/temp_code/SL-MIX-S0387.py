import math
from collections import defaultdict

def volatility_weight(x):
    return 1.0 + abs(math.log(1.0 + abs(x)))

def risk_transform(value, threshold=0.05):
    return value ** 2 if value > threshold else math.sqrt(abs(value))

# Simulated daily returns for 5 assets over 10 days
asset_returns = [
    [0.02, -0.01, 0.03, -0.02, 0.01, 0.04, -0.03, 0.02, -0.01, 0.05],
    [-0.01, 0.02, -0.02, 0.03, -0.01, 0.02, -0.04, 0.03, -0.02, 0.01],
    [0.03, 0.01, -0.03, 0.02, -0.02, 0.01, -0.01, 0.04, -0.03, 0.02],
    [-0.02, 0.03, 0.01, -0.01, 0.04, -0.02, 0.03, -0.01, 0.02, -0.03],
    [0.01, -0.02, 0.04, -0.03, 0.02, -0.01, 0.05, -0.02, 0.01, -0.04]
]

# Asset weights in portfolio
asset_weights = [0.2, 0.15, 0.3, 0.25, 0.1]

# Calculate daily portfolio returns
portfolio_daily_returns = []
for day_idx in range(len(asset_returns[0])):
    daily_return = sum(asset_returns[asset_idx][day_idx] * asset_weights[asset_idx] 
                       for asset_idx in range(len(asset_weights)))
    portfolio_daily_returns.append(daily_return)

# Apply volatility weighting and risk transformation
weighted_returns = [risk_transform(ret) * volatility_weight(ret) for ret in portfolio_daily_returns]

# Compute base risk metrics
avg_daily_return = sum(portfolio_daily_returns) / len(portfolio_daily_returns)
volatility = math.sqrt(sum((r - avg_daily_return) ** 2 for r in portfolio_daily_returns) / (len(portfolio_daily_returns) - 1))

# Risk adjustment logic with short-circuit evaluation
is_high_volatility = volatility > 0.02
has_negative_trend = sum(1 for r in portfolio_daily_returns if r < 0) > len(portfolio_daily_returns) // 2

# Conditional risk scoring
if is_high_volatility and has_negative_trend:
    risk_factor = 1.5
elif is_high_volatility or has_negative_trend:
    risk_factor = 1.2
else:
    risk_factor = 1.0

# Final risk score calculation
raw_risk_score = sum(weighted_returns) * risk_factor
portfolio_risk_score = round(raw_risk_score * 1000, 2)

print(f"Result: {portfolio_risk_score}")