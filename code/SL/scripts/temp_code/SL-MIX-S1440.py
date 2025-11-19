from functools import reduce
import math

def compute_volatility_adjustment(prices):
    avg = sum(prices) / len(prices)
    squared_diffs = [(p - avg) ** 2 for p in prices]
    variance = sum(squared_diffs) / len(squared_diffs)
    return math.sqrt(variance)

def find_optimal_threshold(historical_data):
    n = len(historical_data)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        current_price = historical_data[i-1]
        adjustment = compute_volatility_adjustment(historical_data[:i])
        adjusted_price = current_price + adjustment if current_price > 100 else current_price - adjustment
        
        if i >= 2:
            dp[i] = max(dp[i-1], dp[i-2] + adjusted_price)
        else:
            dp[i] = max(dp[i-1], adjusted_price)
    
    return dp[n]

# Market data for 7 consecutive periods
crypto_prices = [95.5, 102.3, 98.7, 105.2, 110.1, 107.8, 112.4]

# Apply filtering to remove outliers using lambda
filtered_prices = list(filter(lambda x: x > 90 and x < 120, crypto_prices))

# Transform prices using a mapping function
transformed_prices = list(map(lambda x: round(x * 1.02, 2), filtered_prices))

# Calculate the optimal threshold using dynamic programming
optimal_threshold = find_optimal_threshold(transformed_prices)

print(f"Result: {optimal_threshold}")