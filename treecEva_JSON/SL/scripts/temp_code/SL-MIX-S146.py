from collections import defaultdict

def calculate_portfolio_optimization(daily_fluctuations):
    n = len(daily_fluctuations)
    if n == 0:
        return 0
    
    # dp[i] represents maximum gain up to day i
    dp = [0] * n
    dp[0] = max(0, daily_fluctuations[0])
    
    for i in range(1, n):
        # Either take today's fluctuation plus best previous gain, or skip
        dp[i] = max(dp[i-1], daily_fluctuations[i] + (dp[i-2] if i >= 2 else 0))
    
    return dp[n-1]

# Market data for a 7-day period
market_sentiment_scores = [3, -2, 4, -1, 2, 5, -3]
trading_volumes = [100, 150, 120, 200, 80, 160, 90]

# Calculate weighted fluctuations
weighted_fluctuations = [
    score * (volume // 100) 
    for score, volume in zip(market_sentiment_scores, trading_volumes)
]

# Apply dynamic programming optimization
optimal_gain = calculate_portfolio_optimization(weighted_fluctuations)

# Adjust for market conditions
if optimal_gain > 10:
    optimal_gain -= 2
elif optimal_gain < 0:
    optimal_gain = 0
else:
    optimal_gain += 1

print(f"Result: {optimal_gain}")