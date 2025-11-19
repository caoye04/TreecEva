from functools import wraps
from collections import namedtuple

def transaction_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

def calculate_volatility_index(prices):
    if len(prices) < 2:
        return 0
    changes = [abs(prices[i] - prices[i-1]) for i in range(1, len(prices))]
    return sum(changes) / len(changes)

@transaction_logger
def optimize_rebalancing(market_data):
    # Dynamic programming table for optimal rebalancing
    dp = [0] * (len(market_data) + 1)
    rebalance_actions = [False] * len(market_data)
    
    volatility_threshold = 15.0
    
    for i in range(1, len(market_data) + 1):
        current_prices = market_data[i-1]
        volatility = calculate_volatility_index(current_prices)
        
        # Switch-like logic for rebalancing decision
        if volatility > volatility_threshold * 1.5:
            action_code = 3  # Aggressive rebalance
        elif volatility > volatility_threshold:
            action_code = 2  # Standard rebalance
        elif volatility > volatility_threshold * 0.5:
            action_code = 1  # Conservative rebalance
        else:
            action_code = 0  # No rebalance
        
        # Apply dynamic programming logic
        if action_code >= 2:
            dp[i] = max(dp[i-1] + action_code, dp[i-1])
            rebalance_actions[i-1] = True
        else:
            dp[i] = dp[i-1]
    
    # Count optimal rebalancing actions using list comprehension
    optimal_rebalance_count = sum([1 for action in rebalance_actions if action])
    
    return optimal_rebalance_count

# Market data representing price sequences for different time periods
market_conditions = [
    [100, 105, 110, 108, 115],      # High volatility period
    [115, 116, 117, 118, 119],      # Low volatility period
    [119, 130, 125, 140, 135],      # High volatility period
    [135, 136, 137, 136, 138],      # Low volatility period
    [138, 150, 145, 160, 155, 170]  # Very high volatility period
]

# Execute the optimization
optimal_rebalance_count = optimize_rebalancing(market_conditions)
print(f"Result: {optimal_rebalance_count}")